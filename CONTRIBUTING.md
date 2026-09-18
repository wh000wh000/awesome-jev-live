# Contributing

Corrections are the fastest way to improve this list, and they are genuinely
welcome. This repository is a pipeline, so **do not edit `README*.md`** — they
are regenerated from `data/` on every tick and any manual change is lost.

## The one thing you probably want to do: add a project

Add its `owner/repo` to `data/seed.json`:

```json
{
  "repositories": [
    "owner/repo"
  ]
}
```

That is the whole change. The next tick picks it up.

A seeded repository bypasses the relevance filter and the star floor, but it
does **not** bypass evidence grading. A human saying "include this" is not the
same as verifying what a project does, so a seed still lands at `inferred`
unless the collector independently finds code-level evidence of Jev usage. That
is deliberate, not an oversight.

## Reporting a misfiled or wrongly excluded entry

Open an issue. The two cases worth reporting are:

**A project was wrongly excluded.** This is the most likely failure of an
automated filter, and it is the most valuable report. Some exclusions are
deliberate and will not change: `JeVois`, `JEvents`, `Jevil`, `jEveAssets`,
`JEval`, `Jevelin`, the Waveshare ESP32-RLCD display boards and `noulith` merely
share letters with this ecosystem. Everything else is fair game.

**An entry is mis-graded or mis-categorised.** Evidence grades mean something
specific:

| Grade | Claim |
| --- | --- |
| `official` | published by TypeSafe AI itself |
| `observed` | the project turned up in a code search for a Jev-specific API token, or its own text cites `typesafe.ai` |
| `inferred` | the author declared Jev in the repository name or an explicit topic tag; no code-level evidence seen |
| `unverified` | matched only on an ambiguous term plus domain vocabulary |

If you believe an entry deserves a better grade, the most useful thing you can
send is a URL to the specific file that uses the API.

## Reporting a broken asset

Cards show a screenshot and, where one exists, a screen recording taken from the
project's own README. Two rules apply:

- Assets are bundled only when the project declares a redistribution-friendly
  licence. Otherwise the upstream URL is linked and the card says so.
- Every bundled asset is capped by size and by format; a project's video that
  exceeds the cap is linked rather than copied.

If an asset of yours appears here and you would rather it did not, open an issue
and it will be removed. If a card shows the wrong image, that is almost always
because the project's README has several candidates and the heuristic picked a
less useful one — say which file it should be and that becomes an override.

## Changing the pipeline itself

The stages are separate on purpose, and each refuses to be clever:

```text
scripts/collect.py   gather raw candidates, SHA-256 change detection
scripts/curate.py    relevance, evidence grading, categorisation
scripts/media.py     licence-aware asset collection, content-addressed cache
scripts/render.py    build all 20 language editions from one template
scripts/audit.py     quality gate; fails the build rather than publishing junk
```

Two constraints that exist for reasons worth preserving:

**`curate.py` must stay deterministic and model-free.** It runs every two hours
in CI. A model in that loop makes the output drift between ticks and turns any
diff into noise. Every decision there must be a rule a reader can audit.

**Adding a language means adding a file, not a code path.** Copy `i18n/en.json`,
translate the values, keep the keys byte-identical, and add the code to `LANGS`
in `scripts/render.py`. `audit.py` will fail the build if the key sets diverge,
which is the point.

## Running the pipeline locally

```bash
export GITHUB_TOKEN=$(gh auth token)      # or rely on the gh CLI fallback

python3 scripts/collect.py                # ~3 min; --only seed for a quick merge
python3 scripts/curate.py
python3 scripts/media.py                  # slow; MEDIA_MAX=20 to sample
python3 scripts/render.py
python3 scripts/audit.py --links 40
python3 scripts/summary.py
```

The visual assets are built separately and are not part of the tick:

```bash
python3 scripts/build_assets.py                 # re-render from the stored subject
python3 scripts/build_assets.py --generate      # needs image router credentials
```