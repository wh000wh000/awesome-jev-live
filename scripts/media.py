#!/usr/bin/env python3
"""
awesome-jev-live :: media.py

Stage 3: gather each project's image and video so every entry can render as a
self-contained card ("豆腐块": title / facts / data / summary / image | video).

Three rules govern this stage, and they are the reason it is a separate module
rather than a few lines inside the renderer.

1. LICENCE-AWARE BUNDLING
   Copying a third party's screenshots and videos into our repository is
   redistribution. We only do that when the project declares a licence that
   permits it. Otherwise we record the upstream URL and hot-link it instead, so
   the reader still sees the asset but we never re-host it.

2. CONTENT-ADDRESSED CACHE
   Media is stored under a SHA-256 of its own bytes. A file that has not changed
   is never downloaded twice, never re-written, and never shows up in the diff.
   That is what keeps a 2-hourly job from bloating git history.

3. GRACEFUL DEGRADATION
   GitHub plays a real <video> file inline. It cannot play YouTube, Bilibili or
   any iframe embed. So a card's video column has three honest states:
     file     -> local .mp4/.webm, plays inline
     animated -> local .gif, rendered as an animated image
     external -> poster image plus a link, because inline playback is impossible
"""

from __future__ import annotations

import hashlib
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
MEDIA = ROOT / "media"
CST = timezone(timedelta(hours=8))
NOW = datetime.now(CST)
STAMP = NOW.isoformat(timespec="seconds")

TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
if not TOKEN:
    try:
        import subprocess

        TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True,
                               text=True, timeout=10).stdout.strip() or None
    except Exception:  # noqa: BLE001
        TOKEN = None

UA = "awesome-jev-live/1.0 (+https://github.com/wh000wh000/awesome-jev-live)"

# Limits. GitHub warns above 50 MB per file and rejects above 100 MB, so these
# are deliberately far below that: a README asset should never be large.
MAX_IMAGE_BYTES = 3_500_000
MAX_VIDEO_BYTES = 12_000_000
MAX_ANIM_BYTES = 8_000_000
# Keep at most this much bundled media in the repository. Beyond it we stop
# bundling and fall back to hot-linking, which keeps clones reasonable.
MEDIA_BUDGET_BYTES = 700_000_000
# Per-entry cap so one media-rich project cannot dominate the repository.
MAX_ASSETS_PER_ENTRY = 3

PERMISSIVE = {
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MPL-2.0",
    "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "Unlicense", "0BSD", "Zlib",
    "PostgreSQL", "Python-2.0", "WTFPL", "AGPL-3.0", "GPL-2.0", "GPL-3.0",
    "LGPL-2.1", "LGPL-3.0", "BSL-1.0", "Artistic-2.0",
}

IMG_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".svg"}
VID_EXT = {".mp4", ".webm", ".mov", ".m4v"}
ANIM_EXT = {".gif"}

MAGIC = {
    b"\x89PNG\r\n\x1a\n": ("png", "image"),
    b"\xff\xd8\xff": ("jpg", "image"),
    b"GIF87a": ("gif", "image"),
    b"GIF89a": ("gif", "image"),
    b"RIFF": ("webp", "image"),          # refined below for WEBP/AVI
    b"\x1aE\xdf\xa3": ("webm", "video"),  # EBML -> webm/mkv
    b"\x00\x00\x00\x18ftyp": ("mp4", "video"),
    b"\x00\x00\x00\x1cftyp": ("mp4", "video"),
    b"\x00\x00\x00\x20ftyp": ("mp4", "video"),
}

# Anything matching these is chrome, not content.
BADGE_PATTERNS = [
    r"shields\.io", r"badge\.fury", r"badgen\.net", r"codecov\.io",
    r"travis-ci", r"appveyor", r"circleci", r"coveralls", r"david-dm",
    r"awesome\.re/badge", r"github\.com/.*/actions/workflows",
    r"img\.shields", r"api\.codacy", r"snyk\.io", r"bundlephobia",
    r"contrib\.rocks", r"isitmaintained", r"opencollective", r"buymeacoffee",
    r"ko-fi", r"paypal", r"twitter\.com/intent", r"badge\.svg\?",
    r"star-history", r"visitor-badge", r"hits\.se", r"profile-views",
    r"komarev", r"readme-typing-svg", r"capsule-render",
]

# Names that usually mean "this is the project's real screenshot".
GOOD_HINTS = [
    r"screenshot", r"demo", r"preview", r"hero", r"showcase", r"example",
    r"result", r"output", r"dashboard", r"ui\b", r"screen", r"cover",
    r"banner", r"shot", r"thumb", r"feature", r"architect", r"diagram",
    r"flow", r"compare", r"bench", r"chart", r"plot", r"graph",
]

EXTERNAL_VIDEO_HOSTS = [
    r"youtube\.com", r"youtu\.be", r"bilibili\.com", r"vimeo\.com",
    r"loom\.com", r"streamable\.com", r"asciinema\.org",
]


# --------------------------------------------------------------------------
def http_get(url: str, *, limit: int, head_only: bool = False, tries: int = 3):
    """Return (bytes, content_type, final_url) or (None, None, None)."""
    headers = {"User-Agent": UA, "Accept": "*/*"}
    if TOKEN and "api.github.com" in url:
        headers["Authorization"] = f"Bearer {TOKEN}"
        headers["Accept"] = "application/vnd.github+json"
    req = urllib.request.Request(url, headers=headers, method="HEAD" if head_only else "GET")
    delay = 1.5
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                ctype = (resp.headers.get("Content-Type") or "").split(";")[0].strip()
                length = resp.headers.get("Content-Length")
                if length and int(length) > limit:
                    return None, ctype, resp.geturl()
                if head_only:
                    return b"", ctype, resp.geturl()
                data = resp.read(limit + 1)
                if len(data) > limit:
                    return None, ctype, resp.geturl()
                return data, ctype, resp.geturl()
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 403, 500, 502, 503) and attempt < tries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            return None, None, None
        except Exception:  # noqa: BLE001
            if attempt < tries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            return None, None, None
    return None, None, None


def sniff(data: bytes) -> tuple[str, str]:
    """Return (ext, kind) from magic bytes; ('', 'unknown') when unrecognised."""
    for magic, (ext, kind) in MAGIC.items():
        if data.startswith(magic):
            if magic == b"RIFF":
                if data[8:12] == b"WEBP":
                    return "webp", "image"
                if data[8:12] == b"AVI ":
                    return "avi", "video"
                return "webp", "image"
            return ext, kind
    # mp4 variants put the ftyp box a few bytes in
    if b"ftyp" in data[:16]:
        return "mp4", "video"
    if b"<svg" in data[:400].lower():
        return "svg", "image"
    return "", "unknown"


def store(data: bytes, ext: str, slot: str) -> tuple[str, bool]:
    """Content-address the bytes. Returns (relative path, was_new)."""
    h = hashlib.sha256(data).hexdigest()[:16]
    d = MEDIA / slot
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{h}.{ext}"
    if path.exists() and path.stat().st_size == len(data):
        return str(path.relative_to(ROOT)), False
    path.write_bytes(data)
    return str(path.relative_to(ROOT)), True


# --------------------------------------------------------------------------
# README harvesting
# --------------------------------------------------------------------------
def fetch_readme(full_name: str) -> tuple[str, str]:
    """Return (markdown, default_branch). Empty markdown when unavailable."""
    if not TOKEN:
        return "", "main"
    meta, _ct, _u = http_get(f"https://api.github.com/repos/{full_name}", limit=2_000_000)
    branch = "main"
    if meta:
        try:
            branch = json.loads(meta).get("default_branch") or "main"
        except Exception:  # noqa: BLE001
            pass
    url = f"https://api.github.com/repos/{full_name}/readme"
    data, _ct, _u = http_get(url, limit=1_500_000)
    if not data:
        return "", branch
    try:
        doc = json.loads(data)
        if doc.get("encoding") == "base64" and doc.get("content"):
            import base64

            raw = base64.b64decode(doc["content"]).decode("utf-8", "replace")
            return raw, branch
        if doc.get("download_url"):
            raw, _c, _u = http_get(doc["download_url"], limit=1_500_000)
            if raw:
                return raw.decode("utf-8", "replace"), branch
    except Exception:  # noqa: BLE001
        pass
    return "", branch


def absolutize(src: str, base: str) -> str:
    src = src.strip().strip("<>").strip()
    src = src.split(" ")[0] if " " in src and not src.startswith("http") else src
    src = src.strip("\"'")
    if not src:
        return ""
    if src.startswith(("http://", "https://")):
        return src
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("data:"):
        return ""
    url = urllib.parse.urljoin(base, src.lstrip("./"))
    return url


def is_bad(src: str) -> bool:
    return any(re.search(p, src, re.I) for p in BADGE_PATTERNS)


def harvest(readme: str, base: str) -> dict:
    """Extract ranked image and video candidates from a README."""
    images: list[str] = []
    videos: list[str] = []
    external: list[str] = []

    # markdown images ![alt](src) and html <img src=...>
    for m in re.finditer(r"!\[[^\]]*\]\(\s*([^)\s]+)", readme):
        images.append(absolutize(m.group(1), base))
    for m in re.finditer(r"<img[^>]+src=[\"']([^\"']+)[\"']", readme, re.I):
        images.append(absolutize(m.group(1), base))

    # video tags and <source>
    for m in re.finditer(r"<(?:video|source)[^>]+src=[\"']([^\"']+)[\"']", readme, re.I):
        videos.append(absolutize(m.group(1), base))

    # bare links to media files
    for m in re.finditer(r"\]\(\s*([^)\s]+\.(?:mp4|webm|mov|m4v|gif))", readme, re.I):
        u = absolutize(m.group(1), base)
        (videos if not u.lower().endswith(".gif") else images).append(u)

    # external video embeds -> not playable inline, but the link is valuable
    for m in re.finditer(r"\]\(\s*(https?://[^)\s]+)", readme):
        u = m.group(1)
        if any(re.search(host, u, re.I) for host in EXTERNAL_VIDEO_HOSTS):
            external.append(u)

    def clean(seq: list[str]) -> list[str]:
        seen, out = set(), []
        for u in seq:
            if not u or u in seen or is_bad(u):
                continue
            seen.add(u)
            out.append(u)
        return out

    def score(u: str) -> tuple:
        low = u.lower()
        hinted = any(re.search(h, low) for h in GOOD_HINTS)
        ext = Path(urllib.parse.urlparse(low).path).suffix
        return (
            0 if hinted else 1,
            0 if ext in (".png", ".webp", ".jpg", ".jpeg") else 1,
            len(u),
        )

    images = sorted(clean(images), key=score)
    videos = clean(videos)
    external = clean(external)
    return {"images": images, "videos": videos, "external": external}


# --------------------------------------------------------------------------
def handle_entry(entry: dict, budget: dict) -> dict:
    """
    Build the media record for one entry.

    {
      "bundled": true/false,
      "license_ok": true/false,
      "image": "media/... or https://...",
      "image_remote": "...",
      "video": {"state": "file|animated|external|none", "src": "...", "poster": "..."}
    }
    """
    full = entry["name"]
    lic = (entry.get("license") or "").strip()
    license_ok = lic in PERMISSIVE

    readme, branch = fetch_readme(full)
    if not readme:
        return {"bundled": False, "license_ok": license_ok, "image": "",
                "video": {"state": "none", "src": "", "poster": ""}, "source": "no-readme"}

    base = f"https://raw.githubusercontent.com/{full}/{branch}/"
    found = harvest(readme, base)
    slot = full.replace("/", "--").lower()

    rec: dict = {
        "bundled": False,
        "license_ok": license_ok,
        "license": lic or "unknown",
        "image": "",
        "image_alt": "",
        "video": {"state": "none", "src": "", "poster": ""},
        "source": "readme",
        "candidates": {"images": len(found["images"]), "videos": len(found["videos"]),
                       "external": len(found["external"])},
    }

    # ---- image -------------------------------------------------------
    for url in found["images"][:6]:
        if budget["bytes"] > MEDIA_BUDGET_BYTES:
            rec["image"] = url          # budget exhausted -> hot-link
            rec["source"] = "readme+hotlink"
            break
        data, ctype, _final = http_get(url, limit=MAX_IMAGE_BYTES)
        if not data:
            continue
        ext, kind = sniff(data)
        if kind != "image" or ext == "svg":
            continue                        # SVG screenshots are rare and unsafe to rehost
        if not license_ok:
            rec["image"] = url              # never re-host a restricted asset
            rec["source"] = "readme+hotlink(license)"
            break
        rel, is_new = store(data, ext, slot)
        budget["bytes"] += len(data) if is_new else 0
        budget["files"] += 1 if is_new else 0
        rec["image"] = rel
        rec["bundled"] = True
        rec["image_alt"] = f"{full} screenshot"
        break

    # ---- video -------------------------------------------------------
    # a README <video>/<source> or a linked media file
    if found["videos"]:
        url = found["videos"][0]
        ext = Path(urllib.parse.urlparse(url.lower()).path).suffix
        cap = MAX_ANIM_BYTES if ext in ANIM_EXT else MAX_VIDEO_BYTES
        data, _ct, _final = http_get(url, limit=cap)
        if data:
            sext, kind = sniff(data)
            if kind in ("video", "image") and sext in ("mp4", "webm", "gif"):
                if not rec["image"]:
                    pass
                if license_ok and budget["bytes"] <= MEDIA_BUDGET_BYTES:
                    rel, is_new = store(data, sext, slot)
                    budget["bytes"] += len(data) if is_new else 0
                    budget["files"] += 1 if is_new else 0
                    rec["video"] = {
                        "state": "animated" if sext == "gif" else "file",
                        "src": rel,
                        "poster": rec["image"] if rec["image"].startswith("media/") else "",
                    }
                    rec["bundled"] = True
                else:
                    rec["video"] = {
                        "state": "animated" if sext == "gif" else "file",
                        "src": url,
                        "poster": "",
                        "hotlink": True,
                    }

    # an animated image anywhere in the readme still makes a good "video" column
    if rec["video"]["state"] == "none":
        for url in found["images"]:
            if not url.lower().endswith(".gif"):
                continue
            data, _c, _u = http_get(url, limit=MAX_ANIM_BYTES)
            if not data:
                continue
            sext, kind = sniff(data)
            if sext != "gif":
                continue
            if license_ok and budget["bytes"] <= MEDIA_BUDGET_BYTES:
                rel, is_new = store(data, "gif", slot)
                budget["bytes"] += len(data) if is_new else 0
                budget["files"] += 1 if is_new else 0
                rec["video"] = {"state": "animated", "src": rel, "poster": ""}
                rec["bundled"] = True
            else:
                rec["video"] = {"state": "animated", "src": url, "poster": "",
                                "hotlink": True}
            break

    # external embed (YouTube / Bilibili / Vimeo ...): never playable on GitHub
    if rec["video"]["state"] == "none" and found["external"]:
        rec["video"] = {
            "state": "external",
            "src": found["external"][0],
            "poster": rec["image"] if rec["image"].startswith("media/") else "",
        }

    return rec


def main() -> int:
    print(f"== awesome-jev-live :: media @ {STAMP} ==")
    entries_path = DATA / "entries.json"
    if not entries_path.exists():
        print("   !! data/entries.json missing; run curate.py first", file=sys.stderr)
        return 1

    doc = json.loads(entries_path.read_text())
    entries = doc.get("entries", [])

    media_path = DATA / "media.json"
    prior: dict = {}
    if media_path.exists():
        try:
            prior = json.loads(media_path.read_text()).get("entries", {})
        except Exception:  # noqa: BLE001
            prior = {}

    budget = {"bytes": sum(1 for _ in MEDIA.rglob("*")), "files": 0}
    budget["bytes"] = sum(f.stat().st_size for f in MEDIA.rglob("*") if f.is_file())
    print(f"   existing media: {budget['bytes'] / 1e6:.1f} MB")

    only = set(os.environ.get("MEDIA_ONLY", "").split(",")) - {""}
    max_n = int(os.environ.get("MEDIA_MAX", "0")) or len(entries)

    results = dict(prior)
    processed = 0
    errors = 0
    for e in entries:
        if e["kind"] != "repo":
            continue
        if only and e["id"] not in only and e["name"] not in only:
            continue
        if processed >= max_n:
            break
        # reuse a cached record only when the repo did not move
        cached = prior.get(e["id"])
        if cached and cached.get("pushed_at") == e.get("pushed_at") and cached.get("image"):
            results[e["id"]] = cached
            continue
        try:
            rec = handle_entry(e, budget)
        except Exception as exc:  # noqa: BLE001 - one bad repo must not stop the run
            print(f"   !! {e['name']}: {type(exc).__name__}: {exc}", file=sys.stderr)
            errors += 1
            continue
        rec["pushed_at"] = e.get("pushed_at")
        results[e["id"]] = rec
        processed += 1
        if processed % 10 == 0:
            print(f"   .. {processed} processed, {budget['bytes'] / 1e6:.1f} MB bundled")
        time.sleep(0.25)

    out = {"generated_at": STAMP, "entries": results,
           "bundled_bytes": budget["bytes"], "bundled_files": budget["files"]}
    media_path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")

    with_img = sum(1 for v in results.values() if v.get("image"))
    with_vid = sum(1 for v in results.values() if (v.get("video") or {}).get("state") not in (None, "", "none"))
    bundled = sum(1 for v in results.values() if v.get("bundled"))
    print(f"   media records: {len(results)}  image={with_img} video={with_vid} "
          f"bundled={bundled} errors={errors}")
    print(f"   bundled size: {budget['bytes'] / 1e6:.2f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())