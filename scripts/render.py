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

import html
import json
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

CATEGORY_ORDER = [
    "official-sdk", "community-sdk", "agent-tooling", "routing-guardrails",
    "evaluation", "research-models", "apps-demos", "media-discussions",
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


# --------------------------------------------------------------------------
# language switcher
# --------------------------------------------------------------------------
def lang_switcher(current: str, names: dict[str, str]) -> str:
    parts = []
    for code in LANGS:
        label = names.get(code, code)
        if code == current:
            parts.append(f"<b>{esc(label)}</b>")
        else:
            href = "README.md" if code == "en" else f"README.{code}.md"
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
    bits.append(labels["evidence_short"].get(e.get("evidence", "unverified"),
                                             e.get("evidence", "")))
    age = days_ago(e.get("pushed_at"))
    if age is not None:
        bits.append(f"{age}d" if t["lang"] == "en" else f"{age} 天")
    if e.get("is_new"):
        bits.append("**NEW**")
    elif e.get("stars_delta"):
        bits.append(f"⭐{'+' if e['stars_delta'] > 0 else ''}{e['stars_delta']}")

    summary_line = f'<b><a href="{esc(url)}">{esc(name)}</a></b> — ' + " · ".join(bits)

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
    facts = [f"`{esc(t['categories'].get(e['category'], e['category']))}`",
             esc(t["tiers"].get(e.get("tier", "community"), ""))]
    facts.append(f"`{esc(t['evidence_levels'].get(e.get('evidence', 'unverified'), ''))}`")
    if e.get("language"):
        facts.append(esc(e["language"]))
    if e.get("license"):
        facts.append(esc(e["license"]))
    if kind == "repo":
        facts.append(f"[{esc(e.get('owner', ''))}](https://github.com/{esc(e.get('owner', ''))})")
    elif kind == "post":
        # Attribution matters more than usual here: a post is a person's work,
        # not an organisation's, so the author is a link and the handle is
        # repeated rather than implied.
        who = esc(e.get("author") or e.get("author_handle") or "")
        link = e.get("author_url") or ""
        facts.append(f"[{who}]({esc(link)})" if link else who)
        if e.get("author_handle") and e.get("author"):
            facts.append("@" + esc(e["author_handle"]))
        facts.append(esc(e.get("platform") or (e.get("url") or "").split("/")[2] if "//" in (e.get("url") or "") else ""))
    out.append(f"**{labels['facts']}** · " + " · ".join(f for f in facts if f))
    out.append("")

    # 2. 数据
    metrics = []
    if kind == "repo":
        delta = e.get("stars_delta") or 0
        dstr = f" ({'+' if delta > 0 else ''}{delta})" if delta else ""
        metrics.append(f"{labels['stars']} **{e.get('stars', 0)}**{dstr}")
        metrics.append(f"{labels['forks']} {e.get('forks', 0)}")
        if e.get("open_issues") is not None:
            metrics.append(f"{labels['issues']} {e.get('open_issues', 0)}")
        if e.get("created_at"):
            metrics.append(f"{labels['created']} {str(e['created_at'])[:10]}")
    elif kind == "model":
        metrics.append(f"{labels['downloads']} {e.get('downloads', 0)}")
        metrics.append(f"{labels['likes']} {e.get('likes', 0)}")
    elif kind in ("story", "comment"):
        metrics.append(f"{labels['points']} {e.get('stars', 0)}")
        metrics.append(f"{labels['comments']} {e.get('forks', 0)}")
    elif kind == "post":
        pm = e.get("metrics") or {}
        if pm.get("views"):
            metrics.append(f"{labels['views']} {pm['views']}")
        if pm.get("likes"):
            metrics.append(f"{labels['likes']} {pm['likes']}")
        if pm.get("replies"):
            metrics.append(f"{labels['comments']} {pm['replies']}")
        if e.get("posted_at"):
            metrics.append(f"{labels['posted']} {str(e['posted_at'])[:10]}")
    if kind != "post" and e.get("pushed_at"):
        metrics.append(f"{labels['last_push']} {str(e['pushed_at'])[:10]}")
    metrics.append(f"{labels['first_seen']} {str(e.get('first_seen', ''))[:10]}")
    out.append(f"**{labels['data']}** · " + " · ".join(metrics))
    out.append("")

    # 3. 简介摘要
    out.append(f"**{labels['summary']}**")
    out.append("")
    summary = ""
    if t["lang"] != "en":
        summary = (e.get("summary_i18n") or {}).get(t["lang"], "")
    summary = summary or e.get("summary") or t["labels"]["no_summary"]
    out.append(summary.strip())
    out.append("")

    # The upstream project this post is about. Kept immediately after the
    # summary and given its own labelled line, because for a post this is the
    # only route from "someone built something" to "here is the thing".
    if kind == "post" and e.get("project_url"):
        plabel = (e.get("project_label") or {}).get(t["lang"]) \
            or (e.get("project_label") or {}).get("en") or labels["original_project"]
        out.append(f"➡️ **{esc(plabel)}** — [{md_escape(e['project_url'])}]({e['project_url']})")
        out.append("")
    elif kind == "post":
        # Honest placeholder rather than silence: the reader learns that the
        # link is still being tracked down, not that it does not exist.
        out.append(f"<sub>{labels['project_link_pending']}</sub>")
        out.append("")

    notes = e.get("notes") or ""
    if e.get("notes_i18n"):
        notes = (e["notes_i18n"] or {}).get(t["lang"]) or notes
    if notes:
        out.append(f"> {notes}")
        out.append("")
    if e.get("code_paths"):
        shown = ", ".join(f"`{p}`" for p in e["code_paths"][:4])
        out.append(f"<sub>{labels['found_in_code']}: {shown}</sub>")
        out.append("")

    # 4. 图 | 视频
    m = media.get(e["id"]) or {}
    image = asset_url(m.get("image", ""))
    video = m.get("video") or {}
    vstate = video.get("state", "none")
    vsrc = asset_url(video.get("src", ""))

    if image or vstate != "none":
        out.append(f"<table><tr><th align=\"center\" width=\"50%\">{labels['image']}</th>"
                   f"<th align=\"center\" width=\"50%\">{labels['video']}</th></tr><tr>")
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
def render_language(lang: str, t: dict, entries: list[dict], stats: dict,
                    media: dict, names: dict[str, str]) -> str:
    L: list[str] = []
    labels = t["labels"]

    # hero
    hero = t.get("hero_image", "assets/readme/hero.png")
    L.append('<p align="center">')
    L.append(f'  <img src="{hero}" width="100%" alt="{esc(t["title"])}">')
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
    L.append(f'  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>')
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

    # what is jev
    L.append(f'## {esc(labels["what_is_jev"])}')
    L.append("")
    L.append(t["intro"])
    L.append("")
    for line in t.get("intro_bullets", []):
        L.append(f"- {line}")
    L.append("")

    # evidence legend -- the methodological differentiator
    L.append(f'## {esc(labels["evidence_legend"])}')
    L.append("")
    L.append(t["evidence_intro"])
    L.append("")
    L.append(f"| {labels['grade']} | {labels['meaning']} |")
    L.append("| --- | --- |")
    for key in EVIDENCE_ORDER:
        L.append(f"| `{esc(t['evidence_levels'].get(key, key))}` | {t['evidence_desc'].get(key, '')} |")
    L.append("")

    # contents
    L.append(f'## {esc(labels["contents"])}')
    L.append("")
    for cat in CATEGORY_ORDER:
        n = stats["by_category"].get(cat, 0)
        if not n:
            continue
        anchor = cat
        L.append(f"- [{t['categories'].get(cat, cat)}](#{anchor}) — **{n}**")
    L.append(f"- [{labels['by_language']}](#{labels['by_language_anchor']})")
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
        L.append(f'## {esc(t["categories"].get(cat, cat))} <sub>· {len(rows)}</sub>')
        L.append("")
        if t.get("category_blurbs", {}).get(cat):
            L.append(t["category_blurbs"][cat])
            L.append("")
        for i, e in enumerate(rows, 1):
            L.append(render_card(e, media, t, i))

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
    L.append(f"| {labels['language']} | {labels['total']} | {labels['example_projects']} |")
    L.append("| --- | --- | --- |")
    for lang_name, items in sorted(by_lang.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        ex = ", ".join(f"`{md_escape(x)}`" for x in items[:3])
        L.append(f"| {esc(lang_name)} | {len(items)} | {ex} |")
    L.append("")
    L.append(f"<sub>{labels['language_note']}</sub>")
    L.append("")

    # how it stays current
    L.append(f'## {esc(labels["how_it_works"])}')
    L.append("")
    L.append(t["pipeline_intro"])
    L.append("")
    pipe = "assets/readme/pipeline.svg"
    if (ROOT / pipe).exists():
        L.append(f'<img src="{pipe}" width="100%" alt="{esc(labels["how_it_works"])}">')
        L.append("")
    for line in t.get("pipeline_bullets", []):
        L.append(f"- {line}")
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
        out = ROOT / ("README.md" if code == "en" else f"README.{code}.md")
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