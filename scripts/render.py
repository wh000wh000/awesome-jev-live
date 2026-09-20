#!/usr/bin/env python3
"""
awesome-jev-live :: render.py

Stage 4: render every README from the data. Nothing here is hand-written, so
the 20 language editions can never drift apart in structure.

Card anatomy ("豆腐块"), in the order the specification asks for:

    <details>                      collapsed by default so the page stays scannable
      summary   title + at-a-glance facts
      body
        ## Title
        基本信息   basic facts
        数据       metrics, including star movement since last tick
        简介摘要   what it is and the reusable engineering decision
        图 | 视频  two-column HTML table, image left, playing video right
    </details>

One deliberate implementation note. CommonMark ends an HTML block at the first
blank line and does not parse markdown inside a <td>, so a markdown table placed
inside the layout table silently degrades to plain text. The layout table here
therefore contains only <img>/<video>, and all prose and fact tables live
outside it as ordinary markdown. That is the robust arrangement on GitHub.
"""

from __future__ import annotations

import hashlib
import html
import json
import unicodedata
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
I18N = ROOT / "i18n"

CST = timezone(timedelta(hours=8))
NOW = datetime.now(CST)
STAMP = NOW.isoformat(timespec="seconds")

REPO_URL = "https://github.com/wh000wh000/awesome-jev-live"
RAW_BASE = "https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/"

LANGS = [
    "en", "zh-CN", "zh-TW", "ja", "ko", "es", "fr", "de", "pt-BR", "ru",
    "it", "ar", "hi", "tr", "vi", "th", "id", "pl", "nl", "uk",
]

EVIDENCE_ORDER = ["official", "observed", "inferred", "unverified"]

# Visual grammar. Emoji here are not decoration: they are the fastest way to
# scan forty cards for the one that is a guardrail rather than a client, and
# they survive translation where a word does not.
CATEGORY_EMOJI = {
    "official-sdk": "🏛️",
    "community-sdk": "🧰",
    "agent-tooling": "🤖",
    "routing-guardrails": "🛡️",
    "evaluation": "🧪",
    "research-models": "🔬",
    "apps-demos": "🎮",
    "media-discussions": "📰",
    "other": "🧩",
}

# Not a domain, so it does not compete for a place in the picks strip.
FEATURED_EXCLUDE = {"other"}
EVIDENCE_EMOJI = {
    "official": "✅",
    "observed": "👁️",
    "inferred": "🔎",
    "unverified": "❓",
}

# Translated editions live under docs/ so that a visitor to the repository sees
# one README in the file listing instead of twenty-one, and the first screen is
# the index rather than a wall of filenames.
DOCS_DIR = ROOT / "docs"


SUMMARY_CACHE: dict[str, dict[str, str]] = {}


def load_summary_cache() -> None:
    """
    Translations of entry prose, keyed by the hash of the English source.

    Content-addressed, so an upstream description that changes invalidates its
    own translation instead of silently serving a stale one, and two entries
    with identical text share a single translation. Missing entries fall back to
    English: a half-translated edition is better than an empty one, and the
    cache fills in over successive ticks.
    """
    SUMMARY_CACHE.clear()
    base = DATA / "summaries"
    if not base.exists():
        return
    for path in base.glob("*.json"):
        try:
            SUMMARY_CACHE[path.stem] = json.loads(path.read_text())
        except Exception:  # noqa: BLE001
            SUMMARY_CACHE[path.stem] = {}


def text_hash(text: str) -> str:
    return hashlib.sha1(text.strip().encode("utf-8")).hexdigest()[:16]


def localized(text: str, lang: str, source_lang: str = "en") -> str:
    """
    The cached translation when there is one, otherwise the original.

    `source_lang` is the language the text is already in. Most entries are
    English, but the collection log is Chinese, and for those the English
    edition needs a lookup just as much as the others do.
    """
    if not text or lang == source_lang:
        return text
    return (SUMMARY_CACHE.get(lang) or {}).get(text_hash(text)) or text


def edition_path(code: str) -> pathlib.Path:
    return ROOT / "README.md" if code == "en" else DOCS_DIR / f"README.{code}.md"

# A README is capped at roughly 512 KB by GitHub, and this list grows with the
# ecosystem, so the page cannot hold an unbounded number of full cards. Thai
# crossed 485 KB at 530 entries and the audit stopped the publish -- correctly,
# because the alternative was a page that silently stops rendering.
#
# The head of each category keeps its full card, with its image and recording.
# The tail keeps a one-line entry, so every project still appears and is still
# clickable; what it loses is the media block. That is a real trade and it is
# the only one that bounds the page without dropping projects.
# Two tiers, because ranking and illustration are different questions. The
# ranking decides what a reader should see first; media decides what can be
# shown at all. A single top-N cap pushed most of the 97 entries that publish a
# screenshot into the one-line tail, where their image could not appear.
FULL_CARDS_BY_RANK = 12
MAX_FULL_CARDS_PER_CATEGORY = 34

# Must stay in step with the same list in curate.py. When it drifted, an entire
# category rendered nothing and 72 entries silently vanished from the page.
CATEGORY_ORDER = [
    "official-sdk", "community-sdk", "agent-tooling", "routing-guardrails",
    "evaluation", "research-models", "apps-demos", "media-discussions", "other",
]


# --------------------------------------------------------------------------
def esc(text: str) -> str:
    return html.escape(str(text or ""), quote=True)


def md_escape(text: str) -> str:
    """Make a one-line string safe inside a markdown link caption."""
    return re.sub(r"([\[\]<>`])", r"\\\1", str(text or "")).replace("\n", " ").strip()


def load(path: Path, default):
    try:
        return json.loads(path.read_text())
    except Exception:  # noqa: BLE001
        return default


def asset_url(rel: str) -> str:
    """Turn a repo-relative media path into a raw URL GitHub can serve."""
    if not rel:
        return ""
    if rel.startswith(("http://", "https://")):
        return rel
    return RAW_BASE + rel.lstrip("./")


def days_ago(iso: str) -> int | None:
    if not iso:
        return None
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return max(0, (NOW - dt.astimezone(CST)).days)
    except Exception:  # noqa: BLE001
        return None


def human_age(iso: str, lang: str) -> str:
    d = days_ago(iso)
    if d is None:
        return "—"
    return f"{d}d" if lang == "en" else f"{d} 天"


def bullets_as_table(bullets: list[str]) -> list[str]:
    """
    Render informational bullets as a table.

    The Awesome manifest only accepts list items shaped like
    `- [name](url) - description`, so a bullet that explains something rather
    than linking to it is a defect under awesome-lint. The same content as a
    two-column table is allowed, and scans better than a bulleted paragraph.
    """
    rows: list[list[str]] = []
    for b in bullets:
        m = re.match(r"\*\*(.+?):?\*\*\s*(?:—|-|:)?\s*(.*)$", b.strip())
        if m:
            rows.append([f"**{m.group(1)}**", m.group(2)])
        else:
            rows.append(["", b])
    return md_table(["", ""], rows)


# Sentence terminator per language, for the compact list entries. A one-line
# entry must end with proper punctuation to satisfy the manifest, and appending
# an ASCII period to a Chinese sentence reads wrong.
SENTENCE_END = {"zh-CN": "。", "zh-TW": "。", "ja": "。"}
ALREADY_ENDED = ".!?。！？…:;"


def as_list_description(summary: str, lang: str, limit: int = 80) -> str:
    """
    Shape an upstream description into a manifest-legal list item description.

    Three constraints, each found by running the linter rather than guessed:
    it must end with sentence punctuation, it must not be cut mid-quote (an
    unclosed quote is a lint error and looks broken), and it must stay short.
    """
    text = re.sub(r"\s+", " ", (summary or "").strip())
    text = re.sub(r"([\[\]])", r"\\\1", text)          # neutralise injected markdown
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:—-")
        # A truncated quote or bracket reads as broken. Symmetric delimiters must
        # be tested for parity: comparing count('"') > count('"') is always
        # false, which is how an unclosed quote survived into the published page.
        for sym in ('"', "'"):
            if text.count(sym) % 2:
                text = text[: text.rfind(sym)].rstrip()
        for opener, closer in (("(", ")"), ("[", "]")):
            while text.count(opener) > text.count(closer) and opener in text:
                text = text[: text.rfind(opener)].rstrip()
    # The linter accepts only ASCII sentence punctuation, and an upstream
    # description may be Chinese while the README is English, so a CJK
    # terminator is normalised here. List-item convention, not a rewrite.
    text = text.rstrip()
    if text.endswith(("。", "！", "？")):
        text = text[:-1] + {"。": ".", "！": "!", "？": "?"}[text[-1]]
    if text and text[-1] not in ALREADY_ENDED:
        text += SENTENCE_END.get(lang, ".")
    return text


def gh_slug(text: str) -> str:
    """
    Reproduce GitHub's heading-anchor algorithm closely enough to link to it.

    Hand-rolled `<a id="...">` anchors were language-independent and stable,
    which is why they were used at first, but a ToC entry pointing at one is not
    a link awesome-lint accepts. Deriving the slug from the same string that
    produces the heading keeps the two in sync in all twenty languages,
    including the CJK ones.
    """
    s = re.sub(r"<[^>]+>", "", text).lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    # Trim *after* stripping punctuation: a heading that starts with an emoji
    # leaves a leading space behind, and slugging that produced an anchor
    # beginning with a hyphen, which resolves to nothing.
    s = s.strip()
    # One hyphen per space, not one per run of spaces. GitHub's slugger does not
    # collapse, so "moment — the" becomes "moment--the".
    return s.replace(" ", "-")


def cell_width(text: str) -> int:
    """
    Display width of a table cell, not its character count.

    An emoji occupies two columns and a CJK glyph occupies two, so padding by
    len() leaves every emoji-bearing row misaligned -- 844 lint failures, and a
    visibly ragged table. Variation selectors and combining marks take no space.
    """
    width = 0
    for i, ch in enumerate(text):
        if ch in ("\ufe0f", "\ufe0e") or unicodedata.combining(ch):
            continue
        wide = (unicodedata.east_asian_width(ch) in ("W", "F")
                or ord(ch) >= 0x1F000            # emoji blocks, wide on screen
                or (i + 1 < len(text) and text[i + 1] == "\ufe0f"))
        width += 2 if wide else 1
    return width


def md_table(headers: list[str], rows: list[list[str]]) -> list[str]:
    """
    Render a markdown table with padded cells.

    awesome-lint's table-pipe-alignment rule requires the pipes to line up, and
    the alignment has to be computed from the widest cell rather than guessed,
    because a single long project list makes one column dominate.
    """
    width = cell_width
    cols = len(headers)
    w = [width(h) for h in headers]
    for row in rows:
        for i in range(min(cols, len(row))):
            w[i] = max(w[i], width(row[i]))

    def line(cells: list[str]) -> str:
        padded = []
        for i in range(cols):
            cell = cells[i] if i < len(cells) else ""
            padded.append(cell + " " * max(0, w[i] - width(cell)))
        return "| " + " | ".join(padded) + " |"

    out = [line(headers), "| " + " | ".join("-" * w[i] for i in range(cols)) + " |"]
    out.extend(line(r) for r in rows)
    return out


# --------------------------------------------------------------------------
# language switcher
# --------------------------------------------------------------------------
def lang_switcher(current: str, names: dict[str, str]) -> str:
    """Links are relative to the edition doing the linking: root -> docs, docs -> sibling."""
    in_docs = current != "en"
    parts = []
    for code in LANGS:
        label = names.get(code, code)
        if code == current:
            parts.append(f"<b>{esc(label)}</b>")
        else:
            if code == "en":
                href = "../README.md" if in_docs else "README.md"
            else:
                href = f"README.{code}.md" if in_docs else f"docs/README.{code}.md"
            parts.append(f'<a href="{href}">{esc(label)}</a>')
    # wrap into a readable multi-line block
    return "<sub>" + " · ".join(parts) + "</sub>"


# --------------------------------------------------------------------------
# one card
# --------------------------------------------------------------------------
def render_card(e: dict, media: dict, t: dict, idx: int) -> str:
    labels = t["labels"]
    kind = e.get("kind", "repo")
    name = e.get("name", "")
    # A submission's display title is localized; a repository's name is not.
    if kind == "post":
        name = (e.get("title_i18n") or {}).get(t["lang"]) or name
    url = e.get("url", "")

    # ---- at-a-glance facts for the summary line -------------------
    bits = []
    if e.get("stars"):
        bits.append(f"⭐{e['stars']}")
    if e.get("language"):
        bits.append(esc(e["language"]))
    elif kind == "model":
        bits.append("model")
    elif kind == "post" and e.get("author_handle"):
        bits.append("@" + esc(e["author_handle"]))
    ev = e.get("evidence", "unverified")
    bits.append(f"{EVIDENCE_EMOJI.get(ev, '')} {labels['evidence_short'].get(ev, ev)}")
    age = days_ago(e.get("pushed_at"))
    if age is not None:
        bits.append(f"{age}d" if t["lang"] == "en" else f"{age} 天")
    if e.get("is_new"):
        bits.append("**NEW**")
    elif e.get("stars_delta"):
        bits.append(f"⭐{'+' if e['stars_delta'] > 0 else ''}{e['stars_delta']}")

    cat_icon = CATEGORY_EMOJI.get(e.get("category", ""), "•")
    summary_line = (f'{cat_icon} <b><a href="{esc(url)}">{esc(name)}</a></b> · '
                    + " · ".join(bits))

    # ---- body -----------------------------------------------------
    # Size note: GitHub refuses to render a Markdown file beyond roughly 512 KB,
    # and this README is fully regenerated every two hours, so per-card cost is a
    # hard constraint rather than a style preference. Two consequences:
    #   * the title lives in the <summary> and is not repeated as an <h3>
    #   * facts and metrics are single compact lines, not two five-row tables
    # The one table that remains is the one the design actually calls for:
    # image beside video.
    out: list[str] = []
    out.append("<details>")
    out.append(f"<summary>{summary_line}</summary>")
    out.append("")

    # 1. 基本信息
    # Order and weight follow what a reader actually came for: the summary
    # first, then the few facts that are not already visible in the summary
    # line, then the metrics. An earlier version led with six fact rows and six
    # metric rows and buried the description underneath them.
    out.append(f"##### 📝 {labels['summary']}")
    out.append("")
    summary = ""
    if t["lang"] != "en":
        summary = (e.get("summary_i18n") or {}).get(t["lang"], "")
    summary = summary or e.get("summary") or t["labels"]["no_summary"]
    if not (e.get("summary_i18n") or {}).get(t["lang"]):
        summary = localized(summary, t["lang"], e.get("source_lang") or "en")
    summary = re.sub(r"([\[\]])", r"\\\1", summary.strip())
    out.append(summary)
    out.append("")

    if kind == "post" and e.get("project_url"):
        plabel = (e.get("project_label") or {}).get(t["lang"]) \
            or (e.get("project_label") or {}).get("en") or labels["original_project"]
        out.append(f"➡️ **{esc(plabel)}** — [{md_escape(e['project_url'])}]({e['project_url']})")
        out.append("")
    elif kind == "post":
        out.append(f"<sub>{labels['project_link_pending']}</sub>")
        out.append("")

    notes = e.get("notes") or ""
    if e.get("notes_i18n"):
        notes = (e["notes_i18n"]).get(t["lang"]) or notes
    if not (e.get("notes_i18n") or {}).get(t["lang"]):
        notes = localized(notes, t["lang"], e.get("source_lang") or "en")
    if notes:
        out.append(f"> 💡 {notes}")
        out.append("")

    if e.get("code_paths"):
        shown = ", ".join(f"`{x}`" for x in e["code_paths"][:4])
        out.append(f"<sub>🔧 {labels['found_in_code']}: {shown}</sub>")
        out.append("")

    # Only the facts a reader cannot infer from the summary line above it.
    fact_rows: list[list[str]] = [[
        labels["category"],
        f"`{esc(t['categories'].get(e['category'], e['category']))}`"],
    ]
    ev = e.get("evidence", "unverified")
    fact_rows.append([labels["evidence"],
                      f"{EVIDENCE_EMOJI.get(ev, '')} "
                      f"`{esc(t['evidence_levels'].get(ev, ev))}`"])
    if e.get("language"):
        fact_rows.append([labels["language"], esc(e["language"])])
    if kind == "post":
        who = esc(e.get("author") or e.get("author_handle") or "")
        link = e.get("author_url") or ""
        who_cell = f"[{who}]({esc(link)})" if link else who
        if e.get("author_handle") and e.get("author"):
            who_cell += " · @" + esc(e["author_handle"])
        fact_rows.append([labels["owner"], who_cell])
    out.append(f"##### 📌 {labels['facts']}")
    out.append("")
    out.extend(md_table([labels["field"], labels["value"]], fact_rows))
    out.append("")

    metric_rows: list[list[str]] = []
    if kind == "repo":
        delta = e.get("stars_delta") or 0
        dstr = f" (+{delta})" if delta > 0 else (f" ({delta})" if delta else "")
        metric_rows.append([f"⭐ {labels['stars']}", f"**{e.get('stars', 0)}**{dstr}"])
        if e.get("pushed_at"):
            metric_rows.append([f"🚀 {labels['last_push']}", str(e["pushed_at"])[:10]])
    elif kind == "post":
        pm = e.get("metrics") or {}
        if pm.get("views"):
            metric_rows.append([f"👁️ {labels['views']}", f"**{pm['views']}**"])
        if pm.get("likes"):
            metric_rows.append([f"❤️ {labels['likes']}", str(pm["likes"])])
        if pm.get("replies"):
            metric_rows.append([f"💬 {labels['comments']}", str(pm["replies"])])
        if e.get("posted_at"):
            metric_rows.append([f"📅 {labels['posted']}", str(e["posted_at"])[:10]])
    metric_rows.append([f"📥 {labels['first_seen']}", str(e.get("first_seen", ""))[:10]])
    out.append(f"##### 📊 {labels['data']}")
    out.append("")
    out.extend(md_table([labels["metric"], labels["value"]], metric_rows))
    out.append("")

    # Topics are the project's own tags, so they add scannable, factual detail
    # without inventing a description the maintainer never wrote.
    topics = [x for x in (e.get("topics") or []) if x and x not in ("submission",)]
    if topics:
        out.append("🏷 " + " · ".join(f"`{esc(x)}`" for x in topics[:8]))
        out.append("")

    # 4. 图 | 视频
    m = media.get(e["id"]) or {}
    image = asset_url(m.get("image", ""))
    video = m.get("video") or {}
    vstate = video.get("state", "none")
    vsrc = asset_url(video.get("src", ""))

    if image or vstate != "none":
        # A rule separates the written record from the visual one; without it
        # the image table reads as another field of the data table.
        out.append("---")
        out.append("")
        out.append(f"<table><tr><th align=\"center\" width=\"50%\">🖼 {labels['image']}</th>"
                   f"<th align=\"center\" width=\"50%\">🎬 {labels['video']}</th></tr><tr>")
        # left cell
        if image:
            out.append(f"<td align=\"center\" valign=\"top\">"
                       f"<img src=\"{esc(image)}\" width=\"100%\" alt=\"{esc(name)} screenshot\">"
                       f"</td>")
        else:
            out.append(f"<td align=\"center\" valign=\"top\"><sub>{labels['no_media']}</sub></td>")
        # right cell
        # GitHub's sanitiser removes <video> and <source> from user content, so
        # a video cell built from those tags renders as an empty box. Verified
        # against the published page: the <td> came back with nothing in it.
        # raw.githubusercontent.com also serves MP4 as application/octet-stream
        # with nosniff, so a direct link downloads rather than plays.
        #
        # The only thing that actually moves on GitHub is an animated image, so
        # media.py transcodes a project's recording into a GIF and that GIF is
        # what plays here. The original file is linked for full quality.
        if vstate == "animated" and vsrc:
            full = asset_url(video.get("full_quality") or "")
            extra = (f' · <a href="{esc(full)}">{labels["open_video"]}</a>'
                     if full else "")
            out.append(f"<td align=\"center\" valign=\"top\">"
                       f"<img src=\"{esc(vsrc)}\" width=\"100%\" "
                       f"alt=\"{esc(name)} animation\">"
                       f"<br><sub>{labels['animated_note']}{extra}</sub></td>")
        elif vstate == "file" and vsrc:
            # No GIF could be produced within the size cap, so show the poster
            # and link the file rather than emitting a tag GitHub will delete.
            out.append(f"<td align=\"center\" valign=\"top\">"
                       f"<a href=\"{esc(vsrc)}\">"
                       f"<img src=\"{esc(image) if image else ''}\" width=\"100%\" "
                       f"alt=\"{esc(name)} video\"></a><br>"
                       f"<sub><a href=\"{esc(vsrc)}\">{labels['open_video']}</a></sub></td>")
        elif vstate == "external" and vsrc:
            host = re.sub(r"^www\.", "", re.sub(r"^https?://", "", vsrc).split("/")[0])
            out.append(f"<td align=\"center\" valign=\"top\">"
                       f"<a href=\"{esc(vsrc)}\"><img src=\"{esc(image) if image else ''}\" "
                       f"width=\"100%\" alt=\"video\"></a><br>"
                       f"<sub><a href=\"{esc(vsrc)}\">{labels['watch_on']} {esc(host)}</a> "
                       f"· {labels['external_note']}</sub></td>")
        else:
            out.append(f"<td align=\"center\" valign=\"top\"><sub>{labels['no_media']}</sub></td>")
        out.append("</tr></table>")
        out.append("")
        if m.get("license_ok") is False and m.get("bundled") is False and image.startswith("http"):
            out.append(f"<sub>{labels['hotlink_note']}</sub>")
            out.append("")

    out.append("</details>")
    out.append("")
    return "\n".join(out)


# --------------------------------------------------------------------------
# one language
# --------------------------------------------------------------------------
def render_featured(entries: list[dict], media: dict, t: dict, names: dict) -> list[str]:
    """
    The picks strip: one entry per category, two to a row, each with its own
    image when the project published one.

    Picked by the same ranking that orders the sections, so the strip and the
    list below it can never disagree about which entry is first. Entries arrive
    already sorted, so the first of each category is the ranking leader.

    Written as raw HTML rather than markdown because markdown inside a <td> is
    not parsed: anything that looks like a table or a list there renders as
    literal text.
    """
    by_cat: dict[str, list[dict]] = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)

    def illustrative(rows: list[dict]) -> dict:
        """The highest-ranked entry that can actually show something.

        Only three of eight category leaders publish a screenshot, so a strip
        built strictly from the leaders would be mostly blank. Media is the one
        property that makes this block worth its space, so the leader is taken
        unless a lower-ranked entry can carry the visual, and the rule is stated
        on the page rather than left implicit.
        """
        for row in rows:
            if (media.get(row["id"]) or {}).get("image"):
                return row
        return rows[0]

    picks = [illustrative(rows) for cat in CATEGORY_ORDER
             if cat not in FEATURED_EXCLUDE and (rows := by_cat.get(cat))]

    if not picks:
        return []

    L: list[str] = ['<a id="featured"></a>', ""]
    L.append(f'## {t["labels"]["featured_title"]}')
    L.append("")
    L.append(f'<sub>{t["labels"]["featured_note"]}</sub>')
    L.append("")
    L.append("<table>")
    for i in range(0, len(picks), 2):
        L.append("<tr>")
        for e in picks[i:i + 2]:
            cat = e.get("category", "")
            ev = e.get("evidence", "unverified")
            img = asset_url((media.get(e["id"]) or {}).get("image", ""))
            summary = re.sub(r"\s+", " ",
                             localized(e.get("summary") or "", t["lang"]).strip())
            if len(summary) > 170:
                summary = summary[:167].rsplit(" ", 1)[0] + "…"
            bits = [f'⭐{e.get("stars", 0)}']
            if e.get("language"):
                bits.append(esc(e["language"]))
            bits.append(f'{EVIDENCE_EMOJI.get(ev, "")} '
                        f'{esc(t["labels"]["evidence_short"].get(ev, ev))}')
            L.append('<td width="50%" valign="top">')
            if img:
                L.append(f'<img src="{esc(img)}" width="100%" '
                         f'alt="{esc(e.get("name", ""))}">')
            L.append(f'<b>{CATEGORY_EMOJI.get(cat, "•")} '
                     f'<a href="{esc(e["url"])}">{esc(e.get("name", ""))}</a></b>')
            L.append(f'<sub>{" · ".join(bits)}</sub>')
            if summary:
                L.append(f'<sub>{esc(summary)}</sub>')
            L.append("</td>")
        L.append("</tr>")
    L.append("</table>")
    L.append("")
    return L


def render_language(lang: str, t: dict, entries: list[dict], stats: dict,
                    media: dict, names: dict[str, str]) -> str:
    # Editions under docs/ reach assets and LICENSE one level up.
    asset_prefix = "" if lang == "en" else "../"
    L: list[str] = []
    labels = t["labels"]

    # hero
    hero = asset_prefix + t.get("hero_image", "assets/readme/hero.png")
    L.append('<p align="center">')
    L.append(f'  <img src="{esc(hero)}" width="100%" alt="{esc(t["title"])}">')
    L.append("</p>")
    L.append("")
    L.append(f'<h1 align="center">{esc(t["title"])}</h1>')
    L.append("")
    L.append(f'<p align="center"><b>{t["tagline"]}</b></p>')
    L.append("")

    # badges
    L.append('<p align="center">')
    L.append(f'  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>')
    L.append(f'  <img src="https://img.shields.io/badge/entries-{stats["total"]}-0d9488" alt="entries">')
    L.append(f'  <img src="https://img.shields.io/badge/languages-{len(LANGS)}-1f6feb" alt="languages">')
    L.append(f'  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">')
    L.append(f'  <a href="{asset_prefix}LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>')
    L.append("</p>")
    L.append("")

    # language switcher
    L.append(f'<p align="center">{lang_switcher(lang, names)}</p>')
    L.append("")

    # live strip -- this is the differentiator, so it leads
    new_n = stats.get("new_this_tick", 0)
    L.append("> [!NOTE]")
    L.append(f"> **{labels['live_now']}** · {labels['last_sync']}: `{STAMP}` (UTC+8)")
    L.append(f"> · {labels['total']}: **{stats['total']}** · {labels['new_this_tick']}: **{new_n}** "
             f"· {labels['languages_covered']}: **{len(stats.get('by_language', {}))}**")
    L.append("")
    L.append(f"<sub>{labels['live_note']}</sub>")
    L.append("")

    # The picks strip leads, because the first question a visitor has is "what
    # is actually good here", and answering it with one image per domain beats
    # answering it with a table of contents.
    L.extend(render_featured(entries, media, t, names))

    # contents -- first section, per the Awesome manifesto (awesome-lint
    # remark-lint:awesome-toc). A generated list is long; the table of contents
    # is the only thing that makes it navigable, so it comes before the
    # explanation rather than after it.
    L.append(f'## {esc(labels["contents"])}')
    L.append("")
    # Every h2 in document order. awesome-lint matches ToC entries against
    # headings positionally, so a section that is absent from the ToC
    # desynchronises every entry after it -- which is exactly what happens when
    # the ToC lists only the categories.
    toc: list[str] = [
        # The picks strip is deliberately not listed: it sits above this table,
        # and awesome-toc maps items to the headings *after* the table, so the
        # first item has to be the first section below it.
        f"- [{labels['what_is_jev']}](#{gh_slug(labels['what_is_jev'])})",
        f"- [{labels['evidence_legend']}](#{gh_slug(labels['evidence_legend'])})",
    ]
    for cat in CATEGORY_ORDER:
        n = stats["by_category"].get(cat, 0)
        if not n:
            continue
        title = t["categories"].get(cat, cat)
        toc.append(f"- [{title}](#{gh_slug(title)}) — **{n}**")
    toc.append(f"- [{labels['by_language']}](#{gh_slug(labels['by_language'])})")
    toc.append(f"- [{labels['how_it_works']}](#{gh_slug(labels['how_it_works'])})")
    # "Contributing" is deliberately absent: the manifest wants it out of the
    # table of contents, and awesome-lint enforces that.
    L.extend(toc)
    L.append("")

    # what is jev
    L.append(f'## {esc(labels["what_is_jev"])}')
    L.append("")
    L.append(t["intro"])
    L.append("")
    if t.get("intro_bullets"):
        L.extend(bullets_as_table(t["intro_bullets"]))
        L.append("")

    # evidence legend -- the methodological differentiator
    L.append(f'## {esc(labels["evidence_legend"])}')
    L.append("")
    L.append(t["evidence_intro"])
    L.append("")
    L.extend(md_table([labels['grade'], labels['meaning']],
                      [[f"`{esc(t['evidence_levels'].get(key, key))}`",
                        t['evidence_desc'].get(key, '')] for key in EVIDENCE_ORDER]))
    L.append("")

    # categories
    by_cat: dict[str, list[dict]] = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)

    for cat in CATEGORY_ORDER:
        rows = by_cat.get(cat) or []
        if not rows:
            continue
        L.append(f'<a id="{cat}"></a>')
        L.append("")
        L.append(f'## {esc(t["categories"].get(cat, cat))}')
        L.append("")
        if t.get("category_blurbs", {}).get(cat):
            L.append(t["category_blurbs"][cat])
            L.append("")
        head = list(rows[:FULL_CARDS_BY_RANK])
        head_ids = {x["id"] for x in head}
        # Then any remaining entry that can carry a visual, until the size cap.
        for row in rows[FULL_CARDS_BY_RANK:]:
            if len(head) >= MAX_FULL_CARDS_PER_CATEGORY:
                break
            if (media.get(row["id"]) or {}).get("image"):
                head.append(row)
                head_ids.add(row["id"])
        head_sorted = [r for r in rows if r["id"] in head_ids]
        tail = [r for r in rows if r["id"] not in head_ids]
        for i, e in enumerate(head_sorted, 1):
            L.append(render_card(e, media, t, i))

        if tail:
            L.append("<details>")
            L.append(f"<summary><b>{esc(labels['more_in_category'])}</b> "
                     f"<sub>· {len(tail)}</sub></summary>")
            L.append("")
            for e in tail:
                # The manifest requires `- [name](url) - description`, with a
                # plain hyphen and a properly terminated description.
                desc = as_list_description(
                    localized(e.get("summary") or "", t["lang"],
                              e.get("source_lang") or "en"), t["lang"])
                suffix = f" - {esc(desc)}" if desc else ""
                L.append(f"- [{md_escape(e['name'])}]({e['url']}){suffix}")
            L.append("")
            L.append("</details>")
            L.append("")

    # language coverage
    L.append(f'<a id="{labels["by_language_anchor"]}"></a>')
    L.append("")
    L.append(f'## {esc(labels["by_language"])}')
    L.append("")
    L.append(t["language_intro"])
    L.append("")
    by_lang: dict[str, list[str]] = {}
    for e in entries:
        if e.get("language"):
            by_lang.setdefault(e["language"], []).append(e["name"])
    L.extend(md_table(
        [labels['language'], labels['total'], labels['example_projects']],
        [[esc(lang_name), str(len(items)),
          ", ".join(f"`{md_escape(x)}`" for x in items[:3])]
         for lang_name, items in sorted(by_lang.items(),
                                        key=lambda kv: (-len(kv[1]), kv[0]))]))
    L.append("")
    L.append(f"<sub>{labels['language_note']}</sub>")
    L.append("")

    # how it stays current
    L.append(f'## {esc(labels["how_it_works"])}')
    L.append("")
    L.append(t["pipeline_intro"])
    L.append("")
    pipe = asset_prefix + "assets/readme/pipeline.svg"
    if (ROOT / "assets/readme/pipeline.svg").exists():
        L.append(f'<img src="{esc(pipe)}" width="100%" alt="{esc(labels["how_it_works"])}">')
        L.append("")
    if t.get("pipeline_bullets"):
        L.extend(bullets_as_table(t["pipeline_bullets"]))
        L.append("")

    # contributing / footer
    L.append(f'## {esc(labels["contributing"])}')
    L.append("")
    L.append(t["contributing"])
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"<sub>{t['disclaimer']}</sub>")
    L.append("")
    L.append(f"<sub>{labels['generated']} · `render.py` · {STAMP}</sub>")
    L.append("")
    return "\n".join(L)


# --------------------------------------------------------------------------
def main() -> int:
    doc = load(DATA / "entries.json", None)
    if not doc:
        print("!! data/entries.json missing; run curate.py first")
        return 1
    entries = doc["entries"]
    stats = load(DATA / "stats.json", {})
    media_doc = load(DATA / "media.json", {})
    media = media_doc.get("entries", {}) if isinstance(media_doc, dict) else {}

    load_summary_cache()
    print(f"   summary cache: "
          f"{', '.join(f'{k}={len(v)}' for k, v in sorted(SUMMARY_CACHE.items())) or '(none)'}")

    names = {}
    translations = {}
    for code in LANGS:
        path = I18N / f"{code}.json"
        t = load(path, None)
        if t is None:
            print(f"   !! missing i18n/{code}.json -- skipping")
            continue
        translations[code] = t
        names[code] = t.get("native_name", code)

    written = []
    for code, t in translations.items():
        text = render_language(code, t, entries, stats, media, names)
        out = edition_path(code)
        out.parent.mkdir(parents=True, exist_ok=True)
        old = out.read_text() if out.exists() else None
        if old != text:
            out.write_text(text)
            written.append(out.name)
        else:
            written.append(f"{out.name}(same)")

    print(f"== render :: {len(translations)}/{len(LANGS)} languages, "
          f"{len(entries)} entries ==")
    print("   " + ", ".join(written))
    missing = [c for c in LANGS if c not in translations]
    if missing:
        print(f"   missing translations: {', '.join(missing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())