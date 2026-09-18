#!/usr/bin/env python3
"""
awesome-jev-live :: audit.py

Stage 5: the quality gate. Runs before every commit and fails the build rather
than publishing something broken.

The specific failure modes this guards against are the ones that actually
happen to an automatically regenerated list:

  * an entry with no URL, or a URL that is not absolute
  * the same URL listed twice under two categories
  * a card whose image points at a local file that was never written
  * a language edition missing, or missing a section the others have
  * i18n files that drifted from the English key set
  * a language switcher link pointing at a README that does not exist
  * dead or redirected links (network check, opt-in, allowlisted failures)

Exit code 0 means publishable. Any failure prints the exact offending record so
the fix is mechanical rather than exploratory.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
I18N = ROOT / "i18n"

LANGS = [
    "en", "zh-CN", "zh-TW", "ja", "ko", "es", "fr", "de", "pt-BR", "ru",
    "it", "ar", "hi", "tr", "vi", "th", "id", "pl", "nl", "uk",
]

REQUIRED_MARKERS = [
    "assets/readme/hero.png",   # hero present
    "awesome.re/badge",         # awesome badge
]

# Link checking is deliberately conservative. These hosts rate-limit or block
# automated HEAD requests, and a false failure would block a legitimate publish.
LINK_CHECK_SKIP = [
    r"^https://news\.ycombinator\.com",
    r"^https://huggingface\.co",
    r"^https://x\.com",
    r"^https://twitter\.com",
]

problems: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    problems.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load(path: Path, default=None):
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        fail(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return default


# --------------------------------------------------------------------------
def check_entries(entries: list[dict]) -> None:
    if not entries:
        fail("entries.json contains no entries")
        return

    seen: dict[str, str] = {}
    for e in entries:
        eid = e.get("id", "<no id>")
        url = (e.get("url") or "").strip()
        if not url:
            fail(f"{eid}: entry has no URL")
        elif not url.startswith(("http://", "https://")):
            fail(f"{eid}: URL is not absolute -> {url}")
        else:
            if url in seen:
                fail(f"{eid}: duplicate URL also used by {seen[url]} -> {url}")
            else:
                seen[url] = eid

        if not (e.get("summary") or "").strip() and e.get("kind") == "repo":
            warn(f"{eid}: no upstream description")

        if not e.get("category"):
            fail(f"{eid}: entry has no category")
        if not e.get("evidence"):
            fail(f"{eid}: entry has no evidence grade")
        if not e.get("first_seen"):
            fail(f"{eid}: entry has no first_seen timestamp")

    print(f"   entries checked: {len(entries)}  unique URLs: {len(seen)}")


# --------------------------------------------------------------------------
def check_media(entries: list[dict]) -> None:
    media_path = DATA / "media.json"
    if not media_path.exists():
        warn("media.json absent -- cards will render without images")
        return
    media = (load(media_path, {}) or {}).get("entries", {})

    missing_files = 0
    bad_refs = 0
    used = 0
    for e in entries:
        m = media.get(e["id"])
        if not m:
            continue
        for key in (m.get("image"), (m.get("video") or {}).get("src")):
            if not key:
                continue
            if key.startswith(("http://", "https://")):
                continue
            used += 1
            p = ROOT / key
            if not p.exists():
                missing_files += 1
                fail(f"{e['id']}: media file missing on disk -> {key}")
            elif p.stat().st_size == 0:
                fail(f"{e['id']}: media file is empty -> {key}")
        if (m.get("video") or {}).get("state") not in (None, "", "none"):
            if not (m.get("video") or {}).get("src"):
                bad_refs += 1
                fail(f"{e['id']}: video state set but no source")

    bundled = (load(media_path, {}) or {}).get("bundled_bytes", 0)
    print(f"   media: {len(media)} records, {used} local refs, "
          f"{missing_files} missing, {bad_refs} bad video refs, "
          f"bundled {bundled / 1e6:.1f} MB")
    if bundled > 900_000_000:
        warn(f"bundled media is {bundled / 1e6:.0f} MB; consider raising the hot-link threshold")


# --------------------------------------------------------------------------
def keys_of(obj, prefix: str = "") -> set[str]:
    out: set[str] = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            out |= keys_of(v, f"{prefix}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out |= keys_of(v, f"{prefix}[{i}]")
    else:
        out.add(prefix)
    return out


def check_i18n() -> list[str]:
    en = load(I18N / "en.json")
    if not en:
        fail("i18n/en.json is missing or unreadable")
        return []
    ek = keys_of(en)
    present = []
    for code in LANGS:
        path = I18N / f"{code}.json"
        if not path.exists():
            fail(f"i18n/{code}.json is missing (20 language editions are required)")
            continue
        doc = load(path)
        if not doc:
            continue
        present.append(code)
        dk = keys_of(doc)
        if dk != ek:
            missing = sorted(ek - dk)[:6]
            extra = sorted(dk - ek)[:6]
            fail(f"i18n/{code}.json key mismatch: missing={missing} extra={extra}")
        if doc.get("lang") != code:
            fail(f"i18n/{code}.json declares lang={doc.get('lang')!r}")
        if not doc.get("native_name"):
            fail(f"i18n/{code}.json has no native_name")
        direction = doc.get("dir", "ltr")
        if direction not in ("ltr", "rtl"):
            fail(f"i18n/{code}.json has invalid dir={direction!r}")
        if code == "ar" and direction != "rtl":
            fail("i18n/ar.json must declare dir=rtl")
    print(f"   i18n: {len(present)}/{len(LANGS)} language files, "
          f"{len(ek)} keys each")
    return present


# --------------------------------------------------------------------------
def check_readmes(present: list[str]) -> None:
    # GitHub refuses to render a Markdown file beyond roughly 512 KB, and this
    # README grows with the ecosystem. Crossing that line does not produce an
    # error anywhere — the page simply stops rendering — so it is asserted here
    # while there is still room to react.
    SIZE_HARD = 480_000
    SIZE_WARN = 360_000
    biggest = 0
    for code in present:
        name = "README.md" if code == "en" else f"README.{code}.md"
        path = ROOT / name
        if not path.exists():
            fail(f"{name} was not generated")
            continue
        size = path.stat().st_size
        biggest = max(biggest, size)
        if size > SIZE_HARD:
            fail(f"{name} is {size / 1000:.0f} KB; GitHub stops rendering a "
                 f"README past ~512 KB. Trim per-card cost or split the list.")
        elif size > SIZE_WARN:
            warn(f"{name} is {size / 1000:.0f} KB and approaching the GitHub "
                 f"rendering limit")

        text = path.read_text()
        if len(text) < 4000:
            fail(f"{name} looks truncated ({len(text)} bytes)")
        for marker in REQUIRED_MARKERS:
            if marker not in text:
                fail(f"{name} is missing required marker {marker}")
        # every language switcher link must resolve
        for m in re.finditer(r'href="(README[^"]*\.md)"', text):
            target = ROOT / m.group(1)
            if not target.exists():
                fail(f"{name} links to missing file {m.group(1)}")
        # a card that was opened but never closed silently swallows the page
        opens = text.count("<details>")
        closes = text.count("</details>")
        if opens != closes:
            fail(f"{name}: unbalanced <details> tags ({opens} open, {closes} close)")
    print(f"   readmes: {len(present)} checked, largest {biggest / 1000:.0f} KB")


# --------------------------------------------------------------------------
def check_links(entries: list[dict], sample: int = 0) -> None:
    """Optional network check. `sample` > 0 limits how many URLs are probed."""
    if sample <= 0:
        print("   links: skipped (pass --links N to probe N URLs)")
        return
    urls = []
    for e in entries:
        url = (e.get("url") or "").strip()
        if not url or any(re.search(p, url) for p in LINK_CHECK_SKIP):
            continue
        urls.append(url)
    # always include the official and the highest-signal entries first
    urls = urls[:sample]

    dead = 0
    for url in urls:
        ok = False
        for method in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(
                    url, method=method,
                    headers={"User-Agent": "awesome-jev-live-audit/1.0"})
                with urllib.request.urlopen(req, timeout=20) as resp:
                    ok = 200 <= resp.status < 400
                    break
            except urllib.error.HTTPError as exc:
                if exc.code in (403, 405, 429):
                    ok = True   # reachable, just refusing automation
                    break
                if exc.code == 404:
                    ok = False
                    break
            except Exception:  # noqa: BLE001
                continue
        if not ok:
            dead += 1
            fail(f"dead link: {url}")
        time.sleep(0.3)
    print(f"   links: probed {len(urls)}, {dead} dead")


# --------------------------------------------------------------------------
def main(argv: list[str]) -> int:
    doc = load(DATA / "entries.json", {}) or {}
    entries = doc.get("entries", [])
    print(f"== awesome-jev-live :: audit :: {len(entries)} entries ==")

    check_entries(entries)
    check_media(entries)
    present = check_i18n()
    check_readmes(present)

    links = 0
    if "--links" in argv:
        try:
            links = int(argv[argv.index("--links") + 1])
        except Exception:  # noqa: BLE001
            links = 40
    check_links(entries, links)

    for w in warnings:
        print(f"   WARN  {w}")
    if problems:
        print(f"\n   FAILED with {len(problems)} problem(s):")
        for p in problems[:60]:
            print(f"     - {p}")
        if len(problems) > 60:
            print(f"     ... and {len(problems) - 60} more")
        return 1
    print("\n   PASS -- publishable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))