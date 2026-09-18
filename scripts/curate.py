#!/usr/bin/env python3
"""
awesome-jev-live :: curate.py

Stage 2: turn raw candidates into the published index.

This stage is deliberately DETERMINISTIC and LLM-FREE. The list is rebuilt every
two hours from CI, so a model in the loop would make the output drift between
ticks and make any diff unreadable. Every decision here is a rule you can audit.

What it does
  1. Normalize each raw candidate into one entry record.
  2. Reject name collisions -- repos that merely contain the letters "jev"
     (JeVois machine vision, JEvents, Jevil/Deltarune, jEveAssets, JEval, ...).
     Competitor lists include several of these; excluding them is the point.
  3. Assign exactly one category (direct Jev application domain).
  4. Assign a tier (official / community) and an evidence grade
     (official / observed / inferred / unverified) in the 巡检 four-level scheme.
  5. Preserve first_seen across ticks, track star history, merge human overrides.
  6. Append new entries to data/CHANGELOG.md (append-only, never rewritten).

Inputs   data/raw/*.json, data/entries.json (previous), data/overrides.json
Outputs  data/entries.json, data/stats.json, data/CHANGELOG.md
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
DATA = ROOT / "data"
CST = timezone(timedelta(hours=8))
NOW = datetime.now(CST)
STAMP = NOW.isoformat(timespec="seconds")

OFFICIAL_OWNERS = {"typesafe-ai", "typesafe", "typesafeai"}

# Belonging to the official organisation is not by itself evidence of being a
# Jev artifact. The org also carries unrelated repositories that predate the
# product (LLaDA, vllm, pulumi-clickhouse, Overwatch, daggerverse), so the
# official tier is still gated by relevance -- with an allowlist for the
# official pages that carry no description of their own.
OFFICIAL_ALLOWLIST = {
    "typesafe-ai/skills",
    "typesafe-ai/typesafe-sdk-js",
    "typesafe-ai/typesafe-sdk-python",
    "typesafe-ai/system-one-adapter-python",
    "typesafe-ai/typesafe-ai.github.io",
}

# Curated, not exhaustive: below this a repository only stays if the author
# declared Jev in the repository name or in an explicit topic tag.
MIN_STARS = 3

# Discussion noise floor. A 1-point link submission is not an ecosystem signal,
# and HN comment bodies are chatter rather than evidence.
MIN_HN_POINTS = 2

# --------------------------------------------------------------------------
# 1. Name-collision blocklist
# --------------------------------------------------------------------------
# These repositories contain the substring "jev" but have nothing to do with
# TypeSafe's Jev. Every pattern below was verified by hand against the live
# repository. Keeping this list explicit (rather than a clever heuristic) is
# what makes the exclusion auditable.
# Our own repository. It matches every relevance rule by construction -- its
# name contains "jev" and its scripts contain the API endpoints -- and listing
# yourself in your own index is both useless and the source of a real media bug:
# the entry harvested another project's recording out of our own README.
SELF_REPOS = {"wh000wh000/awesome-jev-live"}

COLLISION_REPOS = {
    "jevois/jevois", "jevois/jevoisbase", "jevois/jevois-sdk",
    "jevois/jevois-tutorials", "jevois/jevois-inventor",
    "jevois/jevois-core", "jevois/jevois-core-sdk",
    "patrickpoirier51/JeVois--Python-Tracking",
    "JEvents/JEvents",
    "KRLW890/jevil-simulator", "jeviljester/Verity",
    "GoldenGnu/jeveassets",
    "jevajs/Jeva",
    "QAInsights/JEval",
    "jlop007/jevelin", "AlexandruStanica/Jevelin",
    "ur001/Jevix",
    "simonc/jeveuxapprendreruby.fr",
    "MohawkMEDIC/jeverest",
    "jevinskie/jevmachopp", "jevinskie/jevxpctrace",
    "jeroenvermeulen/JeVe_EasyOTA",
    "grakic/jevrc",
    "tmptrash/jevo",
    "gnlow/Jevi",
    "OpenJEVis/JEVis",
}

# Competitor aggregators are NOT collisions: they are real Jev ecosystem
# artifacts and a reader benefits from seeing them. They are listed under
# "文章、讨论与视频" with an explicit note so the list stays honest about
# the fact that it is not the only one of its kind.
COMPETITOR_LISTS = {
    "Anil-matcha/awesome-jev-by-typesafe",
    "AbdelStark/awesome-typesafe",
    "yibie/awesome-jev",
    "cobanov/awesome-jev",
    "AnotiaWang/awesome-jev",
    "hellogumbo/awesome-jev",
    "OmniJev/awesome-jev",
    "aliaihub/awesome-jev-usecases",
}

# Substring patterns that disqualify a record outright.
COLLISION_PATTERNS = [
    r"jevois",
    r"\bjevents\b",
    r"jevil",
    r"jeveassets",
    r"\bjevix\b",
    r"jevelin",
    r"jeveuxapprendre",
    r"\bjeverest\b",
    r"\bjeval\b",
    r"jeve_easyota",
    r"\bjevrc\b",
    r"openjevis",
    r"\bjevum\b",
    r"omega_jevgy",
    r"jevfwxa",
]

# --------------------------------------------------------------------------
# 2. Relevance rules
# --------------------------------------------------------------------------
# Precision is this list's entire value proposition, so relevance is decided by
# a two-signal rule rather than a keyword soup. The naive approach fails badly:
#
#   "typesafe" is generic software vocabulary  -> middleapi/orpc
#                                                 ("Typesafe APIs Made Simple")
#                                                 TanStack/router, http4k
#   "RLCD" is also Reflective LCD hardware     -> waveshareteam/ESP32-S3-RLCD-4.2
#   "noul" is also a programming language      -> betaveros/noulith
#   "jev" as a substring is a surname/initial  -> jevinskie/*, Jevanleeuwen/*
#
# So: an unambiguous signal accepts on its own. An ambiguous one must be paired
# with a domain word before the repository is treated as part of the ecosystem.

# Unambiguous: a single hit is sufficient.
STRONG_PATTERNS = [
    r"typesafe\.ai",
    r"api\.typesafe\.ai",
    r"jev[\s\-_]?latest",
    r"jev[\s\-_]?distill",
    r"jev[\s\-_]?schema",
    r"\bjev[\s\-_]?1\.\d+",
    r"system[\s\-_]?one[\s\-_]?model",
    r"\bsystemonemodel\b",
]

# Ambiguous: needs at least one DOMAIN word alongside it.
#
# Every entry here has a documented second meaning that put real false
# positives into the list:
#   typesafe  generic "type safety"        -> TanStack/router, http4k, orpc
#   rlcd      reflective LCD hardware      -> waveshareteam/ESP32-S3-RLCD
#   noul      Romanian for "new", a PL     -> geospatialorg, betaveros/noulith
#   systemone a CMS and a dozen toy repos  -> eightarts/SystemOne
#   system one  a generic phrase
MEDIUM_PATTERNS = [
    r"\bjev\b",
    r"\brlcd\b",
    r"\bnoul\b",
    r"system[\s\-_]?one",
    r"\bsystemone\b",
    r"typesafe",
]

# Terms that make one of the ambiguous mentions above unambiguous.
PAIRING_PATTERNS = [
    r"\bjev\b",
    r"\brlcd\b",
    r"system[\s\-_]?one",
    r"\bsystemone\b",
    r"typesafe\.ai",
    r"typesafe[\s\-_]ai",
    r"decision",
    r"judg",
    r"probabil",
    r"calibrat",
]

# Of the ambiguous terms, these two need explicit pairing: a bare mention is
# overwhelmingly likely to mean something else.
NEEDS_PAIRING = [r"typesafe", r"\bnoul\b"]

# An explicit repository topic is the author's own classification. `typesafe`
# is deliberately NOT a token here: on GitHub it overwhelmingly means "type
# safe" and appears on orpc, http4k and easy-reasy, none of which touch this
# ecosystem. Topics corroborate an entry; they never admit one on their own,
# because topic-stuffing is common on high-star link lists.
TOPIC_TOKENS = {"jev", "typesafe-ai", "system-one", "systemone",
                "system_one", "rlcd", "noul", "jev-ai"}

# Domain words that prove an ambiguous mention was meant in the TypeSafe sense.
# Generic AI words (api, ai, llm, model, agent, sdk, prompt, inference) are
# deliberately absent: they co-occur with everything and admitted
# anything_about_game and loki-class false positives.
DOMAIN_PATTERNS = [
    r"decision", r"judg", r"probabil", r"confiden", r"calibrat",
    r"guardrail", r"routing", r"router", r"classif", r"scoring", r"\bscore\b",
    r"verif", r"\bgate\b", r"\bgates\b", r"typed", r"type[\s\-]safe",
    r"system one", r"structured output", r"structured.generat",
    r"constrained.generat", r"reward model", r"benchmark",
    r"eval", r"noul", r"prefill",
]

# A name that literally contains the token "jev" (split on separators and
# camelCase) is accepted even without a description -- NanoJev, jev-router,
# jev-review -- because the author named the project after the product.
def medium_signal(haystack: str) -> bool:
    """
    True when at least one ambiguous term is present AND justified.

    Terms are judged individually rather than as a group. A repository whose only
    claim is `jev` must not be penalised because the words "typesafe" and "noul"
    happen to appear elsewhere in the same string.
    """
    paired = any_match(PAIRING_PATTERNS, haystack)
    # Stand on their own: in this ecosystem these two are not otherwise used.
    for p in (r"\bjev\b", r"\brlcd\b"):
        if re.search(p, haystack, re.I):
            return True
    # Need a Jev-specific term beside them, because each has a common second
    # meaning: "typesafe" is type safety, "noul" is Romanian for "new" and also
    # a programming language, "system one"/"systemone" is a CMS and assorted
    # unrelated repositories.
    for p in (r"typesafe", r"\bnoul\b", r"system[\s\-_]?one", r"\bsystemone\b"):
        if re.search(p, haystack, re.I) and paired:
            return True
    return False


def name_has_jev_token(repo_name: str) -> bool:
    parts: list[str] = []
    for chunk in re.split(r"[-_.\s]+", repo_name or ""):
        parts.extend(re.findall(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|\d+", chunk) or [chunk])
    return any(p.lower() == "jev" for p in parts if p)

# --------------------------------------------------------------------------
# 3. Categories -- ordered; the first match wins
# --------------------------------------------------------------------------
CATEGORIES = [
    ("official-sdk", "官方 SDK 与开发工具", [
        r"typesafe-ai/(typesafe-sdk|system-one-adapter|skills|jev)",
        r"official sdk",
    ]),
    ("community-sdk", "社区客户端、SDK 与适配器", [
        r"\bsdk\b", r"client", r"adapter", r"binding", r"library", r"wrapper",
        r"integration", r"laravel", r"ruby", r"elixir", r"golang", r"\bgo\b sdk",
        r"typescript client", r"python client", r"openai.compatible",
        r"\botp\b", r"genserver", r"graph", r"neo4j", r"postgres", r"sql",
        r"database", r"cli\b", r"command.line",
    ]),
    ("agent-tooling", "Agent 工具链：MCP / hooks / gates / 编码代理", [
        r"\bmcp\b", r"agent", r"claude", r"codex", r"cursor", r"copilot",
        r"coding agent", r"plugin", r"hook", r"skill", r"workflow",
    ]),
    ("routing-guardrails", "路由、护栏与审批", [
        r"rout", r"guardrail", r"firewall", r"moderat", r"policy", r"approval",
        r"safety", r"gate", r"filter", r"triage", r"escalat",
    ]),
    ("evaluation", "评测、校准与基准", [
        r"eval", r"benchmark", r"calibrat", r"test suite", r"measur",
        r"verdict", r"accuracy",
    ]),
    ("research-models", "开源复现、模型权重与架构研究", [
        r"rlcd", r"reproduc", r"paper", r"research", r"nano", r"mini", r"distill",
        r"weights", r"training", r"architecture", r"mlx", r"sglang", r"vllm",
        r"local model", r"open model", r"scorer",
    ]),
    ("apps-demos", "应用、游戏、机器人与交互演示", [
        r"game", r"doom", r"mario", r"robot", r"drone", r"browser",
        r"simulat", r"demo", r"playground", r"visual", r"voice",
        r"dashboard", r"\bui\b", r"\bapp\b", r"music", r"video", r"mujoco",
        r"snake", r"arena", r"autopilot", r"computer.use", r"taxonomy",
        r"trading", r"bot\b", r"snake", r"unity", r"emulator", r"screen",
    ]),
    # Explicit rather than a silent fallback. A curated list should say what
    # belongs here, not accept whatever matched nothing above.
    ("media-discussions", "文章、讨论与同类清单", [
        r"awesome", r"curated", r"directory", r"papers?", r"blog",
        r"article", r"write.?up", r"discussion", r"newsletter", r"reading",
        r"interview", r"podcast", r"showcase", r"field guide",
    ]),
]

DEFAULT_CATEGORY = ("media-discussions", "文章、讨论与视频")

CATEGORY_ORDER = [
    "official-sdk", "community-sdk", "agent-tooling", "routing-guardrails",
    "evaluation", "research-models", "apps-demos", "media-discussions",
]
CATEGORY_TITLES = {key: title for key, title, _patterns in CATEGORIES}
CATEGORY_TITLES[DEFAULT_CATEGORY[0]] = DEFAULT_CATEGORY[1]

# A language-complete index is a listed requirement, so record the
# implementation language of every code entry even when it is not the primary
# organising axis.
LANG_ALIASES = {
    "jupyter notebook": "Jupyter",
    "c++": "C++",
    "c#": "C#",
    "objective-c": "Objective-C",
}


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def any_match(patterns: list[str], text: str) -> bool:
    return any(re.search(p, text, re.I) for p in patterns)


def load_raw(name: str) -> list[dict]:
    path = RAW / f"{name}.json"
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text()).get("items", [])
    except Exception:  # noqa: BLE001
        return []


def norm_lang(value: str | None) -> str:
    if not value:
        return ""
    return LANG_ALIASES.get(value.strip().lower(), value.strip())


def is_collision(full_name: str, haystack: str) -> bool:
    if full_name in COLLISION_REPOS:
        return True
    return any(re.search(p, haystack, re.I) for p in COLLISION_PATTERNS)


def categorize(text: str, full_name: str) -> str:
    if not text and not full_name:
        return DEFAULT_CATEGORY[0]
    for key, _title, patterns in CATEGORIES:
        if any_match(patterns, text):
            return key
    return DEFAULT_CATEGORY[0]


def evidence_grade(tier: str, in_code: bool, strong: bool, explicit: bool) -> str:
    """
    巡检 four-level scheme, applied to a repository.

    The grades only earn their place if they discriminate, so each one is tied
    to a different kind of proof:

      official    published by TypeSafe itself
      observed    proof of real use -- the project turned up in a code search for
                  a Jev-specific API token, or its own text cites typesafe.ai
      inferred    the author declared Jev in the repository name or an explicit
                  topic tag, but no code-level evidence was seen
      unverified  matched only on an ambiguous term plus domain vocabulary
    """
    if tier == "official":
        return "official"
    if in_code or strong:
        return "observed"
    if explicit:
        return "inferred"
    return "unverified"


# --------------------------------------------------------------------------
# repo candidates
# --------------------------------------------------------------------------
def build_repo_entries(repos: list[dict], code_repos: set[str]) -> list[dict]:
    out: list[dict] = []
    rejected: list[tuple[str, str]] = []

    for r in repos:
        full = r.get("full_name") or ""
        if not full:
            continue
        owner = full.split("/")[0].lower()
        repo_name = full.split("/")[-1]
        desc = r.get("description") or ""
        topics = " ".join(r.get("topics") or [])
        # The owner is deliberately excluded from the relevance haystack. If the
        # full name is searched, every repository under `typesafe-ai/` matches
        # the official-org pattern -- which is how LLaDA, vllm, Overwatch and
        # pulumi-clickhouse, all unrelated leftovers, were being graded strong.
        haystack = f"{repo_name} {desc} {topics}"
        full_haystack = f"{full} {desc} {topics}"

        if is_collision(full, full_haystack) or full in SELF_REPOS:
            rejected.append((full, "self" if full in SELF_REPOS else "name collision"))
            continue

        strong = any_match(STRONG_PATTERNS, haystack)
        medium = medium_signal(haystack)
        domain = any_match(DOMAIN_PATTERNS, haystack)
        topics_l = {(t or "").strip().lower() for t in (r.get("topics") or [])}
        topic_hit = bool(topics_l & TOPIC_TOKENS)
        name_hit = name_has_jev_token(repo_name)
        in_code = full in code_repos

        # Admission rule. Code search is a CORROBORATOR, never sufficient on its
        # own: a large repository can contain the string "jev" by accident.
        # Topic tags corroborate too, but do not admit: anything_about_game, a
        # 4.1k-star game-dev link list, carries a `jev` topic it has no use for.
        allowlisted = full in OFFICIAL_ALLOWLIST
        # A human explicitly added this repository to data/seed.json. That
        # bypasses the automated filters but not the evidence grading, because
        # a human saying "include this" is not the same as verifying what it does.
        seeded = bool(r.get("seeded"))
        accepted = (strong or name_hit or (medium and domain) or allowlisted
                    or seeded)
        if not accepted:
            why = "official but off-topic" if owner in OFFICIAL_OWNERS else "no Jev signal"
            rejected.append((full, why))
            continue

        stars = int(r.get("stars") or 0)
        official = owner in OFFICIAL_OWNERS

        # Quality bar. This is a curated list, not an exhaustive dump: a
        # repository that matched only on weak vocabulary and has no traction is
        # noise rather than signal.
        if not (stars >= MIN_STARS or official or strong or name_hit or seeded
                or full in COMPETITOR_LISTS):
            rejected.append((full, "below quality bar"))
            continue

        tier = "official" if official else "community"
        if official:
            # Anything published by TypeSafe belongs in the start-here section,
            # regardless of what its description happens to mention.
            category = "official-sdk"
        elif full in COMPETITOR_LISTS:
            category = "media-discussions"
        else:
            category = categorize(haystack, full)

        out.append({
            "id": f"gh:{full}",
            "kind": "repo",
            "name": full,
            "url": r.get("url") or f"https://github.com/{full}",
            "owner": full.split("/")[0],
            "repo": full.split("/")[-1],
            "summary": desc,
            "category": category,
            "tier": tier,
            "evidence": evidence_grade(
                tier, in_code, strong, name_hit or topic_hit or allowlisted),
            "language": norm_lang(r.get("language")),
            "license": r.get("license") or "",
            "stars": stars,
            "forks": int(r.get("forks") or 0),
            "open_issues": int(r.get("open_issues") or 0),
            "created_at": r.get("created_at") or "",
            "pushed_at": r.get("pushed_at") or "",
            "archived": bool(r.get("archived")),
            "is_fork": bool(r.get("is_fork")),
            "homepage": r.get("homepage") or "",
            "topics": r.get("topics") or [],
            "in_code_search": in_code,
            "is_sibling_list": full in COMPETITOR_LISTS,
            "matched_queries": r.get("matched_queries") or [],
        })

    reasons: dict[str, int] = {}
    for _f, why in rejected:
        reasons[why] = reasons.get(why, 0) + 1
    print(f"   relevance: rejected {len(rejected)} ({reasons})")
    return out


def build_submission_entries(subs: list[dict]) -> list[dict]:
    """
    Turn hand-curated submissions into entries.

    These exist because repository search is structurally blind to work that
    shows up first, or only ever, as a post with a screen recording. They are
    graded like anything else: a human choosing to include something is not the
    same as verifying it, so a submission still lands at `inferred` unless the
    person who added it actually watched the artifact, which is recorded by the
    evidence field they set.
    """
    out: list[dict] = []
    for s in subs:
        sid = s.get("id")
        if not sid or not s.get("url"):
            continue
        # Sibling lists and submissions share the category vocabulary, so an
        # unknown category is a mistake worth surfacing rather than silently
        # dumping into the fallback bucket.
        category = s.get("category") or DEFAULT_CATEGORY[0]
        if category not in CATEGORY_ORDER:
            print(f"  !! submission {sid}: unknown category {category!r}")
            category = DEFAULT_CATEGORY[0]

        summary_map = s.get("summary") or {}
        title_map = s.get("title") or {}
        notes_map = s.get("notes") or {}
        posted = s.get("posted_at") or ""

        out.append({
            "id": sid,
            "kind": "post",
            "name": title_map.get("en") or summary_map.get("en", "")[:60] or sid,
            "title_i18n": title_map,
            "url": s["url"],
            "owner": s.get("author_handle") or s.get("author") or "",
            "author": s.get("author") or "",
            "author_handle": s.get("author_handle") or "",
            "author_url": s.get("author_url") or "",
            "posted_at": posted,
            "summary": summary_map.get("en", ""),
            "summary_i18n": summary_map,
            "notes_i18n": notes_map,
            "notes": notes_map.get("en", ""),
            "category": category,
            "tier": s.get("tier", "community"),
            "evidence": s.get("evidence", "inferred"),
            "language": s.get("language") or "",
            "license": "",
            "stars": 0,
            "forks": 0,
            "created_at": posted,
            "pushed_at": posted,
            "topics": ["submission", s.get("platform") or ""],
            "metrics": s.get("metrics") or {},
            "project_url": s.get("project_url") or "",
            "project_label": s.get("project_label") or {},
            "replies_url": s.get("replies_url") or "",
            "declared_media": s.get("media") or {},
            "is_submission": True,
            "source_note": s.get("source_note") or "",
        })
    return out


def build_model_entries(models: list[dict]) -> list[dict]:
    out = []
    for m in models:
        mid = m.get("id") or ""
        tags = " ".join(m.get("tags") or [])
        haystack = f"{mid} {tags} {m.get('pipeline_tag') or ''}"
        if not any_match(STRONG_PATTERNS, haystack):
            continue
        out.append({
            "id": f"hf:{mid}",
            "kind": "model",
            "name": mid,
            "url": m.get("url"),
            "owner": mid.split("/")[0],
            "summary": "",
            "category": "research-models",
            "tier": "community",
            "evidence": "observed",
            "language": "",
            "license": "",
            "stars": 0,
            "forks": 0,
            "downloads": int(m.get("downloads") or 0),
            "likes": int(m.get("likes") or 0),
            "pushed_at": m.get("last_modified") or "",
            "created_at": "",
            "topics": m.get("tags") or [],
        })
    return out


def build_discussion_entries(hits: list[dict]) -> list[dict]:
    """
    Hacker News items, filtered for signal.

    Comment bodies are dropped: 306 raw hits produced 47 comment records whose
    only qualification was that the word "jev" appeared somewhere in the thread,
    which is noise in a curated index. Stories must clear the points floor and
    match in the TITLE, because the title is what a reader can act on.
    """
    out = []
    for h in hits:
        if (h.get("kind") or "story") != "story":
            continue
        points = int(h.get("points") or 0)
        if points < MIN_HN_POINTS:
            continue
        title = h.get("title") or ""
        if not any_match(STRONG_PATTERNS + [r"\bjev\b", r"typesafe"], title):
            continue
        if is_collision("", title):
            continue
        oid = h.get("id")
        out.append({
            "id": f"hn:{oid}",
            "kind": "story",
            "name": title,
            "url": h.get("url"),
            "owner": h.get("author") or "",
            "summary": re.sub(r"<[^>]+>", " ", h.get("text") or "")[:280].strip(),
            "category": "media-discussions",
            "tier": "community",
            "evidence": "observed",
            "stars": points,
            "forks": int(h.get("num_comments") or 0),
            "created_at": h.get("created_at") or "",
            "pushed_at": h.get("created_at") or "",
            "language": "",
            "license": "",
            "topics": [],
            "hn_points": points,
        })
    return out


# --------------------------------------------------------------------------
# merge with previous state
# --------------------------------------------------------------------------
def merge(previous: dict[str, dict], fresh: list[dict]) -> tuple[list[dict], list[dict]]:
    """Keep first_seen, track star history, report genuinely new entries."""
    merged: list[dict] = []
    new_entries: list[dict] = []
    seen: set[str] = set()

    for e in fresh:
        eid = e["id"]
        seen.add(eid)
        old = previous.get(eid)
        if old:
            e["first_seen"] = old.get("first_seen", STAMP)
            e["last_seen"] = STAMP
            hist = list(old.get("history") or [])
            stars = e.get("stars", 0)
            if not hist or hist[-1].get("stars") != stars:
                hist.append({"t": STAMP, "stars": stars})
            e["history"] = hist[-30:]
            e["stars_delta"] = stars - (old.get("stars") or stars)
            e["is_new"] = False
        else:
            e["first_seen"] = STAMP
            e["last_seen"] = STAMP
            e["history"] = [{"t": STAMP, "stars": e.get("stars", 0)}]
            e["stars_delta"] = 0
            e["is_new"] = True
            new_entries.append(e)
        e["seen_count"] = (old or {}).get("seen_count", 0) + 1
        merged.append(e)
    return merged, new_entries


def apply_overrides(entries: list[dict], overrides: dict) -> list[dict]:
    """
    Human/agent layer. Overrides win, but can never delete an entry that the
    collector keeps finding; they can only refine it or force-exclude it by id.
    """
    blocked = set(overrides.get("exclude") or [])
    by_id = overrides.get("entries") or {}
    out = []
    for e in entries:
        if e["id"] in blocked:
            continue
        ov = by_id.get(e["id"]) or {}
        for key in ("summary", "category", "tier", "evidence", "featured",
                    "media", "title", "notes"):
            if key in ov:
                e[key] = ov[key]
        out.append(e)
    return out


# --------------------------------------------------------------------------
# ranking inside a category
# --------------------------------------------------------------------------
def rank_key(e: dict):
    ev_rank = {"official": 0, "observed": 1, "inferred": 2, "unverified": 3}
    return (
        0 if e.get("featured") else 1,
        ev_rank.get(e.get("evidence", "unverified"), 4),
        -int(e.get("stars") or 0),
        e.get("name", "").lower(),
    )


def main() -> int:
    print(f"== awesome-jev-live :: curate @ {STAMP} ==")

    repos = load_raw("github_repos")
    code = load_raw("github_code")
    models = load_raw("huggingface")
    hits = load_raw("hackernews")
    print(f"   raw: repos={len(repos)} code={len(code)} models={len(models)} hn={len(hits)}")

    code_repos = {c.get("full_name") for c in code if c.get("full_name")}
    code_paths = {c.get("full_name"): c.get("paths") or [] for c in code}

    submissions = []
    sub_path = DATA / "submissions.json"
    if sub_path.exists():
        try:
            submissions = json.loads(sub_path.read_text()).get("submissions", [])
        except Exception as exc:  # noqa: BLE001
            print(f"  !! could not read submissions.json: {exc}", file=sys.stderr)
    print(f"   submissions: {len(submissions)}")

    fresh = (
        build_repo_entries(repos, code_repos)
        + build_model_entries(models)
        + build_discussion_entries(hits)
        + build_submission_entries(submissions)
    )
    print(f"   relevant candidates: {len(fresh)}")

    prev_path = DATA / "entries.json"
    previous: dict[str, dict] = {}
    if prev_path.exists():
        try:
            doc = json.loads(prev_path.read_text())
            previous = {e["id"]: e for e in doc.get("entries", [])}
        except Exception as exc:  # noqa: BLE001
            print(f"  !! could not read previous entries.json: {exc}", file=sys.stderr)

    overrides = {}
    ov_path = DATA / "overrides.json"
    if ov_path.exists():
        try:
            overrides = json.loads(ov_path.read_text())
        except Exception as exc:  # noqa: BLE001
            print(f"  !! could not read overrides.json: {exc}", file=sys.stderr)

    merged, new_entries = merge(previous, fresh)
    merged = apply_overrides(merged, overrides)

    # attach code-search evidence paths, which prove real integration
    for e in merged:
        if e["kind"] == "repo" and e["name"] in code_paths:
            paths = code_paths[e["name"]][:6]
            e["code_paths"] = paths
            if e.get("evidence") == "inferred":
                e["evidence"] = "observed"

    merged.sort(key=lambda e: (CATEGORY_ORDER.index(e["category"])
                               if e["category"] in CATEGORY_ORDER else 99,
                               rank_key(e)))

    dropped = previous.keys() - {e["id"] for e in merged}
    if dropped:
        print(f"   note: {len(dropped)} previously listed entries no longer match")

    payload = {
        "generated_at": STAMP,
        "count": len(merged),
        "categories": CATEGORY_ORDER,
        "category_titles": CATEGORY_TITLES,
        "entries": merged,
    }
    prev_path.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n")

    # ------------------------------------------------------------------
    # stats
    # ------------------------------------------------------------------
    by_cat: dict[str, int] = {}
    by_ev: dict[str, int] = {}
    by_lang: dict[str, int] = {}
    by_tier: dict[str, int] = {}
    for e in merged:
        by_cat[e["category"]] = by_cat.get(e["category"], 0) + 1
        by_ev[e.get("evidence", "unverified")] = by_ev.get(e.get("evidence", "unverified"), 0) + 1
        by_tier[e.get("tier", "community")] = by_tier.get(e.get("tier", "community"), 0) + 1
        lang = e.get("language") or ""
        if lang:
            by_lang[lang] = by_lang.get(lang, 0) + 1

    stats = {
        "generated_at": STAMP,
        "total": len(merged),
        "new_this_tick": len(new_entries),
        "by_category": by_cat,
        "by_evidence": by_ev,
        "by_tier": by_tier,
        "by_language": dict(sorted(by_lang.items(), key=lambda kv: -kv[1])),
        "repos": sum(1 for e in merged if e["kind"] == "repo"),
        "models": sum(1 for e in merged if e["kind"] == "model"),
        "discussions": sum(1 for e in merged if e["kind"] in ("story", "comment")),
        "total_stars": sum(int(e.get("stars") or 0) for e in merged),
    }
    (DATA / "stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1) + "\n")

    # ------------------------------------------------------------------
    # append-only changelog
    # ------------------------------------------------------------------
    log_path = DATA / "CHANGELOG.md"
    if not log_path.exists():
        log_path.write_text(
            "# CHANGELOG — awesome-jev-live\n\n"
            "> Append-only ledger. Written by `scripts/curate.py` on every tick.\n"
            "> Historical lines are never rewritten; corrections are added as new lines.\n\n"
        )
    # only log ticks that actually changed something
    if new_entries or not prev_path.exists():
        lines = [f"\n## {STAMP}\n"]
        lines.append(f"- 收录总数 **{len(merged)}**；本 tick 新增 **{len(new_entries)}**\n")
        for e in sorted(new_entries, key=lambda x: -int(x.get("stars") or 0))[:25]:
            lines.append(
                f"- `+` [{e['name']}]({e['url']}) — {e.get('evidence')} / "
                f"{e.get('category')} — ⭐{e.get('stars', 0)}\n"
            )
        if len(new_entries) > 25:
            lines.append(f"- …另有 {len(new_entries) - 25} 条新增\n")
        with log_path.open("a") as fh:
            fh.writelines(lines)

    print(f"   entries: {len(merged)}  new: {len(new_entries)}")
    print(f"   by category: {by_cat}")
    print(f"   by evidence: {by_ev}")
    print(f"   languages: {len(by_lang)} -> {list(by_lang)[:8]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())