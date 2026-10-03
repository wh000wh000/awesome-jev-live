# Contributing

Corrections are the fastest way to improve this list, and they are genuinely
welcome. Open an issue; that is the whole process.

## Suggesting a project

Open an issue with the repository URL and a sentence on what it does with Jev.
A suggestion bypasses the relevance filter and the star floor.

It does **not** bypass evidence grading. A human saying "include this" is not the
same as verifying what a project does, so a suggested entry still lands at
`inferred` unless independent code-level evidence of Jev usage turns up. That is
deliberate, not an oversight.

## Reporting a misfiled or wrongly excluded entry

Two cases are worth reporting.

**A project was wrongly excluded.** This is the most likely failure of an
automated filter and the most valuable report. Some exclusions are deliberate
and will not change: `JeVois`, `JEvents`, `Jevil`, `jEveAssets`, `JEval`,
`Jevelin`, the Waveshare ESP32-RLCD display boards and `noulith` merely share
letters with this ecosystem. Everything else is fair game.

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

## Translations

Corrections from native speakers are especially welcome. Say which edition and
which string; identifiers such as `MIT`, `MCP`, product names and code spans are
kept verbatim on purpose and should not be translated.