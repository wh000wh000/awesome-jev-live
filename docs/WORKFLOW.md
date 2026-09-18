# The workflow

This repository is regenerated, not maintained. Everything below runs
unattended; nothing in it requires a human except a decision about how the list
should behave.

## The cycle

```text
        every 2 hours (cron 0 */2 * * *, plus manual dispatch)
                              |
   collect.py  ---------------+-- GitHub search (by recency AND by stars)
        |                        -- the official organisation
        |                        -- curated seed list (data/seed.json)
        |                        -- GitHub code search
        |                        -- Hacker News
        |                        -- HuggingFace hub
        |  SHA-256 change detection: an unchanged source contributes nothing
        v
   curate.py  ------------------+-- reject name collisions (explicit list)
        |                        -- two-signal relevance rule
        |                        -- one category per entry
        |                        -- four-level evidence grading
        |                        -- merge previous state, keep first_seen
        |                        -- apply data/overrides.json
        |                        -- append to data/CHANGELOG.md
        v
   media.py  -------------------+-- fetch each project's README
        |                        -- rank image and video candidates
        |                        -- bundle only permissively licensed assets
        |                        -- content-address; never re-fetch unchanged
        v
   render.py  ------------------+-- 20 language editions from one template
        |                        -- collapsible cards: facts, data, summary, media
        v
   audit.py  -------------------+-- URLs absolute and unique; media exists
        |                        -- i18n key parity; anchors resolve
        |                        -- details tags balanced; opt-in link check
        v
   commit  ---------------------+-- ONLY if something changed
```

## Failure behaviour

Each stage is independently runnable and independently survivable.

| Stage fails | Consequence |
| --- | --- |
| `collect` (one source) | that source contributes nothing; other sources still update |
| `curate` | the tick is abandoned; the previous published state stays live |
| `media` | the data update still lands; cards fall back to no media |
| `render` | nothing is committed; the previous editions stay live |
| `audit` | nothing is committed. A broken page is worse than a stale one |

The audit is the point of the design. Everything upstream is allowed to be
imperfect; nothing imperfect reaches `main`.

## Determinism

`curate.py` contains no model calls, and `checks.py` asserts that running it
twice on the same input produces the same list in the same order with the same
grades. That property is what makes a bot-generated diff reviewable: if two
consecutive ticks differ, something in the sources genuinely changed.

Models appear in exactly two places, both one-off and both committed:

- `scripts/build_assets.py --generate` produces the hero subject image.
- The `i18n/*.json` files were translated once and are reviewed like any other
  source file.

## Adding to the list

| Want | Do |
| --- | --- |
| add a project the rules miss | append `owner/repo` to `data/seed.json` |
| improve a summary or pin an entry | edit `data/overrides.json` |
| exclude something permanently | add its id to `overrides.exclude` |
| change what gets searched | edit the query lists in `scripts/collect.py` |
| add a language | add `i18n/<code>.json`, add the code to `LANGS` in `render.py` |

Never edit `README*.md`. They are overwritten on the next tick.

## Running it by hand

```bash
export GITHUB_TOKEN=$(gh auth token)

python3 scripts/collect.py                 # ~4 min, all sources
python3 scripts/collect.py --only seed     # merge just the seed list
python3 scripts/curate.py
MEDIA_MAX=25 python3 scripts/media.py      # sample the media stage
python3 scripts/render.py
python3 scripts/audit.py --links 40
python3 scripts/checks.py
python3 scripts/summary.py
```

## Known limitations

These are real and are stated rather than hidden.

- **Search coverage is not exhaustive.** GitHub search caps at 1000 results per
  query. Two sort orders (recency and stars) close most of the gap, but a
  project that is neither new nor popular can be missed. The seed list exists
  for exactly this.
- **`observed` is not `correct`.** It records that a project was found using a
  Jev-specific API token. It says nothing about whether the project works.
- **Media selection is heuristic.** When a README has several candidates, the
  ranking prefers filenames containing `screenshot`, `demo`, `preview` or
  `hero`. It will sometimes pick a less useful one; say which and it becomes an
  override.
- **Video bundling is size-capped.** A large recording is linked rather than
  copied, so its card will link out instead of playing inline.
- **Scheduled workflows are best-effort.** GitHub delays cron triggers under
  load and disables them after 60 days of repository inactivity. This pipeline
  commits its own changes, which keeps the repository active and keeps itself
  scheduled.