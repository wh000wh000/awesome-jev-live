<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>Der nach Belegstufe geordnete Jev-Index, der sich alle zwei Stunden neu aufbaut.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-445-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <b>Deutsch</b> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Live-Index** · Letzte Synchronisierung: `2026-09-19T03:55:37+08:00` (UTC+8)
> · Einträge: **445** · Neu in diesem Durchlauf: **64** · Implementierungssprachen: **25**

<sub>Jeder Eintrag unten wurde von der Pipeline in diesem Repository gesammelt, gefiltert und erneut geprüft. Zahlen und Zeitstempel stammen aus den Quellen, nicht aus einer handgeschriebenen Momentaufnahme.</sub>

## Inhalt

- [Was ist Jev?](#was-ist-jev)
- [Wie Einträge eingestuft werden](#wie-einträge-eingestuft-werden)
- [Offizielle SDKs und Entwicklerwerkzeuge](#offizielle-sdks-und-entwicklerwerkzeuge) — **5**
- [Community-Clients, SDKs und Adapter](#community-clients-sdks-und-adapter) — **77**
- [Agent-Tooling: MCP, Hooks, Gates und Coding-Agents](#agent-tooling-mcp-hooks-gates-und-coding-agents) — **122**
- [Routing, Guardrails und Freigaben](#routing-guardrails-und-freigaben) — **41**
- [Evaluation, Kalibrierung und Benchmarks](#evaluation-kalibrierung-und-benchmarks) — **34**
- [Offene Reproduktionen, Gewichte und Architekturforschung](#offene-reproduktionen-gewichte-und-architekturforschung) — **17**
- [Anwendungen, Spiele, Robotik und interaktive Demos](#anwendungen-spiele-robotik-und-interaktive-demos) — **37**
- [Artikel, Diskussionen und verwandte Listen](#artikel-diskussionen-und-verwandte-listen) — **112**
- [Projekte nach Implementierungssprache](#projekte-nach-implementierungssprache)
- [Wie diese Liste aktuell bleibt](#wie-diese-liste-aktuell-bleibt)

## Was ist Jev?

Jev ist das erste **System One model** von TypeSafe AI. Es schreibt keine Prosa. Es nimmt einen Zustand plus Fragen, deren Antwortraum Sie vorab festlegen, und liefert typisierte Werte mit Wahrscheinlichkeitsverteilungen zurück, auf die Ihr Code verzweigen kann.

|                        |                                                                                                                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Form**               | `state + typed questions` → `constrained answers + probabilities` → `your code`                                                                                                                                                                    |
| **Primitive**          | `Choice` (eine von ≤255 Optionen wählen), `Score` (ein Raster von 2–10), `Noul` (ein probabilistisches Ja/Nein)                                                                                                                                    |
| **Endpoint**           | `POST https://api.typesafe.ai/v1/systemone`, Modell `jev-1.13.0` / Alias `jev-latest`                                                                                                                                                              |
| **Gute Einsatzfelder** | Routing, Triage, Bewertung, Moderation, Verifikation und Gates mit niedriger Latenz in einem begrenzten Workflow                                                                                                                                   |
| **Bekannte Grenzen**   | Zählen ist unzuverlässig, mehrstufige Indirektion ist schwach, und offizielles Material nennt neun Klassen von Jaggedness. Eine schema-gültige Ausgabe ist nicht dasselbe wie eine korrekte Entscheidung — kalibrieren Sie an Ihren eigenen Daten. |

## Wie Einträge eingestuft werden

Die meisten Listen in diesem Feld behaupten, etwas aufzunehmen. Diese sagt, wie viel sie tatsächlich geprüft hat, und lässt Sie entsprechend filtern.

| Grad         | Bedeutung                                                                                                                                                                                   |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `official`   | Von TypeSafe AI selbst veröffentlicht.                                                                                                                                                      |
| `observed`   | Ein öffentliches Artefakt, das geöffnet und gelesen werden kann — echter Quellcode, echte Konfiguration oder eine ausdrückliche TypeSafe/Jev-Angabe im Repository-Namen oder in den Topics. |
| `inferred`   | Aufgrund eines uneindeutigen Signals plus bestätigenden Vokabulars zugeordnet, aber noch nicht Zeile für Zeile gelesen.                                                                     |
| `unverified` | Sieht verwandt aus, nichts unabhängig bestätigt. Nur zum Auffinden gelistet.                                                                                                                |

<a id="official-sdk"></a>

## Offizielle SDKs und Entwicklerwerkzeuge

Alles, was TypeSafe selbst veröffentlicht. Hier anfangen.

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐225 · official · 6 天 · ⭐+9</summary>

##### Basisfakten

`Offizielle SDKs und Entwicklerwerkzeuge` · Offiziell · `official` · MIT · typesafe-ai

##### Daten

Stars **225** (+9) · Forks 10 · Offene Issues 0 · Erstellt 2026-08-24 · Letzter Push 2026-09-12 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐121 · TypeScript · official · 3 天 · ⭐+6</summary>

##### Basisfakten

`Offizielle SDKs und Entwicklerwerkzeuge` · Offiziell · `official` · TypeScript · MIT · typesafe-ai

##### Daten

Stars **121** (+6) · Forks 8 · Offene Issues 6 · Erstellt 2026-09-04 · Letzter Push 2026-09-15 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐115 · Python · official · 0 天 · ⭐+4</summary>

##### Basisfakten

`Offizielle SDKs und Entwicklerwerkzeuge` · Offiziell · `official` · Python · MIT · typesafe-ai

##### Daten

Stars **115** (+4) · Forks 12 · Offene Issues 0 · Erstellt 2026-08-08 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>Im Code verwendet: `README.md`, `src/system_one_adapter/__init__.py`, `src/system_one_adapter/_response.py`, `src/system_one_adapter/_utils/error_handling.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐81 · Python · official · 0 天 · ⭐+1</summary>

##### Basisfakten

`Offizielle SDKs und Entwicklerwerkzeuge` · Offiziell · `official` · Python · MIT · typesafe-ai

##### Daten

Stars **81** (+1) · Forks 7 · Offene Issues 2 · Erstellt 2026-09-04 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>Im Code verwendet: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 106 天</summary>

##### Basisfakten

`Offizielle SDKs und Entwicklerwerkzeuge` · Offiziell · `official` · HTML · typesafe-ai

##### Daten

Stars **1** · Forks 1 · Offene Issues 1 · Erstellt 2024-05-28 · Letzter Push 2026-06-04 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<a id="community-sdk"></a>

## Community-Clients, SDKs und Adapter

Typisierte Clients für den System-One-Endpoint, in so vielen Sprachen, wie die Community bisher bearbeitet hat.

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐156 · Shell · observed · 0 天 · ⭐+11</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Shell · NOASSERTION · realZachi

##### Daten

Stars **156** (+11) · Forks 7 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

<sub>Im Code verwendet: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐17 · Jupyter · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Jupyter · MIT · jexp

##### Daten

Stars **17** · Forks 3 · Offene Issues 1 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐3 · Rust · observed · 0 天 · ⭐+2</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Rust · MIT · AkashPriyadarshii

##### Daten

Stars **3** (+2) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · TypeScript · MIT · AntonioCoppe

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Python · CC0-1.0 · MrJev

##### Daten

Stars **2** · Forks 1 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐2 · Elixir · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Elixir · MIT · nshkrdotcom

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · TypeScript · opaielsheikh

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — ⭐2 · Java · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Java · MIT · Premo-Cloud

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · JavaScript · MIT · ziyu

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Ruby · MIT · javiergradiche

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/jonesmelton/verdict">jonesmelton/verdict</a></b> — OCaml · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · OCaml · MIT · jonesmelton

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

ocaml sdk for typesafe.ai's jev model

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · TypeScript · MIT · nu-sync

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/RadixILS-Dev/typesafe-sdk-go">RadixILS-Dev/typesafe-sdk-go</a></b> — Go · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Go · MIT · RadixILS-Dev

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A typesafe.ai client written in golang

</details>

<details>
<summary><b><a href="https://github.com/simxnherrera/jevr">simxnherrera/jevr</a></b> — R · observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · R · NOASSERTION · simxnherrera

##### Daten

Stars **0** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A native R client for Jev System One model decisions

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Elixir · MIT · typesend

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — Python · observed · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `observed` · Python · xingwudao

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐29 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · nidhi-singh02

##### Daten

Stars **29** (+2) · Forks 1 · Offene Issues 1 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">Ansehen auf img.youtube.com</a> · die Wiedergabe öffnet auf der Host-Seite; GitHub kann sie nicht direkt einbetten</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gamesonrblx/Jevbridge">gamesonrblx/Jevbridge</a></b> — ⭐16 · TypeScript · inferred · 0 天 · ⭐+3</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · gamesonrblx

##### Daten

Stars **16** (+3) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

> Bridges the typed-decision layer to the agent protocols other tools already speak.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gamesonrblx--jevbridge/772995670b3e42e9.png" width="100%" alt="gamesonrblx/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐13 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · shiftynick

##### Daten

Stars **13** (+1) · Forks 1 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐12 · Elixir · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Elixir · MIT · dannote

##### Daten

Stars **12** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐10 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · JavaScript · MIT · Ying-Kai-Liao

##### Daten

Stars **10** (+1) · Forks 3 · Offene Issues 3 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐7 · Python · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · AboveColin

##### Daten

Stars **7** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Home Assistant integration for TypeSafe Jev. Ask a question about your house and get a probability, a choice or a score as an entity.

</details>

<details>
<summary><b><a href="https://github.com/arunav25/jev-mcp">arunav25/jev-mcp</a></b> — ⭐5 · JavaScript · inferred · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · JavaScript · MIT · arunav25

##### Daten

Stars **5** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.

</details>

<details>
<summary><b><a href="https://github.com/Nasrallah-AL/jev-cli">Nasrallah-AL/jev-cli</a></b> — ⭐5 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · Nasrallah-AL

##### Daten

Stars **5** (+4) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Command-line tool for TypeSafe's Jev AI model

</details>

<details>
<summary><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">saibimajdi/typesafeai-dotnet-sdk</a></b> — ⭐5 · C# · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · C# · MIT · saibimajdi

##### Daten

Stars **5** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/sharziki/semdecide">sharziki/semdecide</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · sharziki

##### Daten

Stars **5** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.

</details>

<details>
<summary><b><a href="https://github.com/frostney/clean-code-review">frostney/clean-code-review</a></b> — ⭐4 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · frostney

##### Daten

Stars **4** (+1) · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/frostney--clean-code-review/7d8a8de446e1c27b.png" width="100%" alt="frostney/clean-code-review screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/keltokhy/jgrep">keltokhy/jgrep</a></b> — ⭐4 · Python · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · keltokhy

##### Daten

Stars **4** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.

</details>

<details>
<summary><b><a href="https://github.com/docxology/daf-jev">docxology/daf-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · docxology

##### Daten

Stars **3** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill

</details>

<details>
<summary><b><a href="https://github.com/Olti1947/jev-java">Olti1947/jev-java</a></b> — ⭐3 · Java · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Java · Olti1947

##### Daten

Stars **3** · Forks 1 · Offene Issues 7 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Idiomatic Java SDK for TypeSafe AI Jev System One decision engine

</details>

<details>
<summary><b><a href="https://github.com/rhighs/jev-code">rhighs/jev-code</a></b> — ⭐3 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · rhighs

##### Daten

Stars **3** (+2) · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/assets/jev-code-logo.png" width="100%" alt="rhighs/jev-code screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/docs/media/session.gif" width="100%" alt="rhighs/jev-code animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-seo">AkashPriyadarshii/jev-seo</a></b> — ⭐2 · Rust · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Rust · AkashPriyadarshii

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One

</details>

<details>
<summary><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Butochnikov/laravel-typesafe-jev</a></b> — ⭐2 · PHP · inferred · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · PHP · MIT · Butochnikov

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes.

</details>

<details>
<summary><b><a href="https://github.com/ibrahemid/git-jev-stage">ibrahemid/git-jev-stage</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · ibrahemid

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Select Git changes for staging with a plain-language description.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/tontoko/jev-browser">tontoko/jev-browser</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · JavaScript · Apache-2.0 · tontoko

##### Daten

Stars **2** · Forks 0 · Offene Issues 3 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.

</details>

<details>
<summary><b><a href="https://github.com/tumf/jev-cli">tumf/jev-cli</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · tumf

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Small dependency-free CLI for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/yzfly/awesome-jev-zh">yzfly/awesome-jev-zh</a></b> — ⭐2 · HTML · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · HTML · CC0-1.0 · yzfly

##### Daten

Stars **2** · Forks 2 · Offene Issues 2 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/jevclient">AboveColin/jevclient</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · AboveColin

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-scout">AkashPriyadarshii/jev-scout</a></b> — ⭐1 · Rust · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Rust · MIT · AkashPriyadarshii

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring

</details>

<details>
<summary><b><a href="https://github.com/anilsenay/jev">anilsenay/jev</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Go · MIT · anilsenay

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Unofficial Go client for TypeSafe's System One API  and its model, Jev.

</details>

<details>
<summary><b><a href="https://github.com/burnigtm/jev-mcp">burnigtm/jev-mcp</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · burnigtm

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client

</details>

<details>
<summary><b><a href="https://github.com/ddfeyes/jev-mode">ddfeyes/jev-mode</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · ddfeyes

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no deps, MIT.

</details>

<details>
<summary><b><a href="https://github.com/felpsdev/jev-classifier">felpsdev/jev-classifier</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · felpsdev

##### Daten

Stars **1** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/felpsdev--jev-classifier/d753de26b0e6c7b6.webp" width="100%" alt="felpsdev/jev-classifier screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-go">Gaurav-Gosain/jev-go</a></b> — ⭐1 · Go · inferred · 2 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Go · MIT · Gaurav-Gosain

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/himomohi/aside-jev">himomohi/aside-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · himomohi

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.

</details>

<details>
<summary><b><a href="https://github.com/mzainzulifqar/jev-php-sdk">mzainzulifqar/jev-php-sdk</a></b> — ⭐1 · PHP · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · PHP · MIT · mzainzulifqar

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

PHP SDK for TypeSafe's Jev: send text and typed questions, get typed answers with calibrated confidence. PHP 8.1+, works with any PSR-18 client, Laravel 8–13.

</details>

<details>
<summary><b><a href="https://github.com/socai-io/jev-social">socai-io/jev-social</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · JavaScript · MIT · socai-io

##### Daten

Stars **1** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Jev-powered social media research through the socai CLI

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/socai-io--jev-social/b95803491d0f55c3.png" width="100%" alt="socai-io/jev-social screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/socai-io--jev-social/0a9e1e30f2fa0829.gif" width="100%" alt="socai-io/jev-social animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/StefanoITA/ts-jev-cost-calculator">StefanoITA/ts-jev-cost-calculator</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · StefanoITA

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe.

</details>

<details>
<summary><b><a href="https://github.com/Stumble/jev-go">Stumble/jev-go</a></b> — ⭐1 · Go · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Go · MIT · Stumble

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Community Go SDK for TypeSafe AI Jev / System One

</details>

<details>
<summary><b><a href="https://github.com/zhirschtritt/typesafe-go">zhirschtritt/typesafe-go</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Go · MIT · zhirschtritt

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Idiomatic Go SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/33Audits/jev-auto">33Audits/jev-auto</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · JavaScript · MIT · 33Audits

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Per-turn model routing for Claude Code. Cheapest tier that can do the job, no API key required, and it calibrates itself from what actually happened.

</details>

<details>
<summary><b><a href="https://github.com/ajshedivy/ibmi-jev">ajshedivy/ibmi-jev</a></b> — Shell · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Shell · Apache-2.0 · ajshedivy

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Ask your Db2 for i tables questions. A Db2 for i SQL SDK powered by TypeSafe's Jev.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-git">AkashPriyadarshii/jev-git</a></b> — Rust · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Rust · MIT · AkashPriyadarshii

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">AkashPriyadarshii/jev-superpowers</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · JavaScript · MIT · AkashPriyadarshii

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions

</details>

<details>
<summary><b><a href="https://github.com/brnyxx/jev-ra">brnyxx/jev-ra</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · MIT · brnyxx

##### Daten

Stars **0** · Forks 0 · Offene Issues 2 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7592fce4641d10.png" width="100%" alt="brnyxx/jev-ra screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7ddcd1053825a2.gif" width="100%" alt="brnyxx/jev-ra animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/david1gp/jev">david1gp/jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · david1gp

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Result-based TypeSafe System One client library and jev command-line interface.

</details>

<details>
<summary><b><a href="https://github.com/fiale-plus/jev-cli">fiale-plus/jev-cli</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · fiale-plus

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/krw82/jev-playwright-mcp">krw82/jev-playwright-mcp</a></b> — TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · krw82

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.

</details>

<details>
<summary><b><a href="https://github.com/kunobi-ninja/kunobi-jev">kunobi-ninja/kunobi-jev</a></b> — Rust · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Rust · Apache-2.0 · kunobi-ninja

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Rust client for the TypeSafe System One API (Jev)

</details>

<details>
<summary><b><a href="https://github.com/lhotwll217/jev-cli">lhotwll217/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · lhotwll217

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

JSON-in, typed-decisions-out CLI for the TypeSafe System One API

</details>

<details>
<summary><b><a href="https://github.com/manojlds/jev-review">manojlds/jev-review</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · manojlds

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Standalone TypeSafe Jev code-review CLI: typed decisions over a local git diff.

</details>

<details>
<summary><b><a href="https://github.com/mgaitan/sqlite-jev">mgaitan/sqlite-jev</a></b> — C · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · C · mgaitan

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Batched natural-language judgments for SQLite, powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/mhmdkzr/jev">mhmdkzr/jev</a></b> — Go · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Go · MIT · mhmdkzr

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

An unofficial Go client for TypeSafe's System One Jev model

</details>

<details>
<summary><b><a href="https://github.com/model-clis/jev">model-clis/jev</a></b> — Rust · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Rust · MIT · model-clis

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Typed judgment CLI for the Jev model (TypeSafe System One): state + questions in, calibrated answers and exit codes out

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing">nekowasabi/jev-routing</a></b> — Go · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Go · MIT · nekowasabi

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.

</details>

<details>
<summary><b><a href="https://github.com/ojusave/beat-jev">ojusave/beat-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · TypeScript · MIT · ojusave

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A penalty shootout powered by Render Workflows, TypeSafe Jev, and Render Postgres. Python and TypeScript examples.

</details>

<details>
<summary><b><a href="https://github.com/okooo5km/jev">okooo5km/jev</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · Apache-2.0 · okooo5km

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed decisions from the shell: a stdlib-Python CLI and Agent Skill for TypeSafe Jev on OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch mode.

</details>

<details>
<summary><b><a href="https://github.com/phuthuycoding/jev-audit">phuthuycoding/jev-audit</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · phuthuycoding

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

AI-powered pre-commit auditor backed by TypeSafe System One (Jev) — blocks secrets, vulns & low-quality code in ~300ms. 79-case test corpus at 100% accuracy.

</details>

<details>
<summary><b><a href="https://github.com/SAGAR-TAMANG/sarvam-jev">SAGAR-TAMANG/sarvam-jev</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `inferred` · Python · SAGAR-TAMANG

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Generation-free typed decisions on Indic LLMs. An open Jev-style inference engine on sarvam-1: constrained logit readout instead of autoregressive JSON. Runs client-side in the browser.

</details>

<details>
<summary><b><a href="https://github.com/giuliosmall/pg_typesafe">giuliosmall/pg_typesafe</a></b> — ⭐76 · C · unverified · 0 天 · ⭐+71</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `unverified` · C · MIT · giuliosmall

##### Daten

Stars **76** (+71) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification

</details>

<details>
<summary><b><a href="https://github.com/pithings/advocaat">pithings/advocaat</a></b> — ⭐68 · TypeScript · unverified · 0 天 · ⭐+2</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `unverified` · TypeScript · MIT · pithings

##### Daten

Stars **68** (+2) · Forks 1 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/obie/ruby_decision_model">obie/ruby_decision_model</a></b> — ⭐16 · Ruby · unverified · 0 天 · **NEW**</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `unverified` · Ruby · MIT · obie

##### Daten

Stars **16** · Forks 2 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Ruby client for decision models such as Typesafe Jev

</details>

<details>
<summary><b><a href="https://github.com/Tangerg/typesafe-sdk-go">Tangerg/typesafe-sdk-go</a></b> — ⭐7 · Go · unverified · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `unverified` · Go · MIT · Tangerg

##### Daten

Stars **7** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Go SDK for the TypeSafe AI API — typed questions in, probability distributions out.

</details>

<details>
<summary><b><a href="https://github.com/Brainwires/jevwire">Brainwires/jevwire</a></b> — ⭐5 · TypeScript · unverified · 0 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `unverified` · TypeScript · MIT · Brainwires

##### Daten

Stars **5** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/typesafe-cli">y0usaf/typesafe-cli</a></b> — ⭐4 · TypeScript · unverified · 2 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `unverified` · TypeScript · MIT · y0usaf

##### Daten

Stars **4** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose

</details>

<details>
<summary><b><a href="https://github.com/geilt/typesafe-cli">geilt/typesafe-cli</a></b> — ⭐3 · Python · unverified · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `unverified` · Python · geilt

##### Daten

Stars **3** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.

</details>

<details>
<summary><b><a href="https://github.com/gilljon/typesafe-ai-rs">gilljon/typesafe-ai-rs</a></b> — ⭐3 · Rust · unverified · 1 天</summary>

##### Basisfakten

`Community-Clients, SDKs und Adapter` · Community · `unverified` · Rust · MIT · gilljon

##### Daten

Stars **3** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Independent async and blocking Rust SDK for the TypeSafe AI System One API

</details>

<a id="agent-tooling"></a>

## Agent-Tooling: MCP, Hooks, Gates und Coding-Agents

Die am schnellsten wachsende Kategorie: Hooks, MCP-Server und Gates, die der nächsten Aktion eines Agenten eine typisierte Entscheidung voranstellen.

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐2948 · TypeScript · observed · 0 天 · ⭐+140</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · TypeScript · MIT · tamaratran

##### Daten

Stars **2948** (+140) · Forks 148 · Offene Issues 44 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>Im Code verwendet: `src/request.ts`, `README.md`, `src/client.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐129 · JavaScript · inferred · 0 天 · ⭐+8</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · gargpratyush

##### Daten

Stars **129** (+8) · Forks 5 · Offene Issues 4 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐31 · Python · inferred · 1 天 · ⭐+2</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · 0xNatoshi

##### Daten

Stars **31** (+2) · Forks 3 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐92 · observed · 0 天 · ⭐+6</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · dbreunig

##### Daten

Stars **92** (+6) · Forks 2 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐15 · Python · observed · 0 天 · ⭐+1</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · Python · MIT · GhalebDweikat

##### Daten

Stars **15** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · Python · MIT · carlaiau

##### Daten

Stars **7** · Forks 1 · Offene Issues 6 · Erstellt 2026-03-13 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/valentynkit/awesome-jev-typesafe">valentynkit/awesome-jev-typesafe</a></b> — ⭐7 · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · CC0-1.0 · valentynkit

##### Daten

Stars **7** · Forks 3 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Typed decisions with TypeSafe's Jev, the first System One model

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · Python · MIT · jodan-alberts

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/rajdhakad9826/routeKit">rajdhakad9826/routeKit</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · TypeScript · MIT · rajdhakad9826

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Agent-native LLM model router built with JEV by TypeSafe.ai. Dynamically selects the most suitable model based on task complexity, reasoning requirements, and tool usage.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · TypeScript · MIT · BYK

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/kraayenjon/awesome-jev">kraayenjon/awesome-jev</a></b> — ⭐1 · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · NOASSERTION · kraayenjon

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · Python · MIT · 24601

##### Daten

Stars **0** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · TypeScript · CrowBe

##### Daten

Stars **0** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · TypeScript · MIT · gorock007

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/uipath-jev-guardrail-connector">jms-dcksn/uipath-jev-guardrail-connector</a></b> — JavaScript · observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · JavaScript · jms-dcksn

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

UiPath bring-your-own-guardrail connector backed by the TypeSafe Jev System One model: plain-language agent policies enforced as calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/Wany-i/jev-decision-layer">Wany-i/jev-decision-layer</a></b> — Python · observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · Python · MIT · Wany-i

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

把决策模型（typesafe/jev-1.13，经 OpenRouter 的 decisions 端点调用）封装成业务决策工具：注册表驱动，带置信度门控与硬约束。非官方项目。

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `observed` · Python · MIT · yousudip

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐261 · TypeScript · inferred · 1 天 · ⭐+8</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · devagrawal09

##### Daten

Stars **261** (+8) · Forks 12 · Offene Issues 1 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐114 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · NiazMorshed2007

##### Daten

Stars **114** (+1) · Forks 9 · Offene Issues 2 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐88 · JavaScript · inferred · 0 天 · ⭐+21</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · fatwang2

##### Daten

Stars **88** (+21) · Forks 10 · Offene Issues 2 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-eval-agent">vinilana/jev-eval-agent</a></b> — ⭐81 · HTML · inferred · 1 天 · ⭐+1</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · HTML · vinilana

##### Daten

Stars **81** (+1) · Forks 7 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-mcp">jkudish/jev-mcp</a></b> — ⭐71 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · jkudish

##### Daten

Stars **71** · Forks 9 · Offene Issues 2 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Proof of concept MCP for Typesafe's new Jev AI model

> An early proof of concept for exposing Jev over MCP, which is how most non-Python toolchains reach it.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/pi-jev">y0usaf/pi-jev</a></b> — ⭐65 · TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · y0usaf

##### Daten

Stars **65** · Forks 3 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers

</details>

<details>
<summary><b><a href="https://github.com/wy-coliney/jev-browser-use">wy-coliney/jev-browser-use</a></b> — ⭐62 · JavaScript · inferred · 0 天 · ⭐+19</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · wy-coliney

##### Daten

Stars **62** (+19) · Forks 2 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wy-coliney--jev-browser-use/581fbd89fe47c952.png" width="100%" alt="wy-coliney/jev-browser-use screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/RomanSlack/jev-drone">RomanSlack/jev-drone</a></b> — ⭐58 · Python · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · RomanSlack

##### Daten

Stars **58** · Forks 3 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/romanslack--jev-drone/b23ea2412f437970.png" width="100%" alt="RomanSlack/jev-drone screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/supercorp-ai/supercov">supercorp-ai/supercov</a></b> — ⭐29 · Rust · inferred · 0 天 · ⭐+4</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Rust · MIT · supercorp-ai

##### Daten

Stars **29** (+4) · Forks 1 · Offene Issues 0 · Erstellt 2026-08-23 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Code quality and coverage for coding agents

> Code quality and coverage verdicts produced as typed decisions rather than prose, so the result can gate a pipeline directly.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/supercorp-ai--supercov/063226e150cb8a6b.jpg" width="100%" alt="supercorp-ai/supercov screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/logicrw/awesome-jev-projects">logicrw/awesome-jev-projects</a></b> — ⭐27 · JavaScript · inferred · 0 天 · ⭐+2</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · logicrw

##### Daten

Stars **27** (+2) · Forks 5 · Offene Issues 3 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/ask-jev-skill">shantanugoel/ask-jev-skill</a></b> — ⭐27 · Python · inferred · 1 天 · ⭐+1</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · shantanugoel

##### Daten

Stars **27** (+1) · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Skill for Hermes, and other agents, to ask typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/compozy/yoshi">compozy/yoshi</a></b> — ⭐11 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · compozy

##### Daten

Stars **11** (+1) · Forks 1 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/compozy--yoshi/637d8588c227f4de.png" width="100%" alt="compozy/yoshi screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/TheoOliveira/pi-jev">TheoOliveira/pi-jev</a></b> — ⭐11 · TypeScript · inferred · 0 天 · ⭐+5</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · TheoOliveira

##### Daten

Stars **11** (+5) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/DanRWilloughby/snifftest">DanRWilloughby/snifftest</a></b> — ⭐9 · TypeScript · inferred · 0 天 · ⭐+3</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · DanRWilloughby

##### Daten

Stars **9** (+3) · Forks 0 · Offene Issues 3 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">jomatsu/pi-jev-auto-mode</a></b> — ⭐9 · TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · jomatsu

##### Daten

Stars **9** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.

</details>

<details>
<summary><b><a href="https://github.com/blakestone-x/jev-mcp">blakestone-x/jev-mcp</a></b> — ⭐8 · Python · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · blakestone-x

##### Daten

Stars **8** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer

</details>

<details>
<summary><b><a href="https://github.com/huntedman/JevLint">huntedman/JevLint</a></b> — ⭐7 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · huntedman

##### Daten

Stars **7** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.

</details>

<details>
<summary><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">DECRUX9812/typesafe-skill-router</a></b> — ⭐6 · Python · inferred · 2 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · DECRUX9812

##### Daten

Stars **6** · Forks 1 · Offene Issues 1 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-code">devagrawal09/jev-code</a></b> — ⭐6 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · devagrawal09

##### Daten

Stars **6** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Bounded TypeSafe Jev workflows for coding agents.

</details>

<details>
<summary><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">GodsBoy/jev-agent-skill-router</a></b> — ⭐5 · Python · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · GodsBoy

##### Daten

Stars **5** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed, confidence-aware agent skill routing with TypeSafe Jev.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/godsboy--jev-agent-skill-router/c80293e37dcd4faf.png" width="100%" alt="GodsBoy/jev-agent-skill-router screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/inanna-malick/jev-dsl">inanna-malick/jev-dsl</a></b> — ⭐5 · Haskell · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Haskell · MIT · inanna-malick

##### Daten

Stars **5** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels

</details>

<details>
<summary><b><a href="https://github.com/anpicasso/hermes-jev-approvals">anpicasso/hermes-jev-approvals</a></b> — ⭐4 · Python · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · anpicasso

##### Daten

Stars **4** (+1) · Forks 2 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only.

</details>

<details>
<summary><b><a href="https://github.com/BillionsBobby/JevRouter">BillionsBobby/JevRouter</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · BillionsBobby

##### Daten

Stars **4** · Forks 1 · Offene Issues 4 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A lightweight Jev-powered router for models, tools, and subagents

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/billionsbobby--jevrouter/f0e638219505d5da.png" width="100%" alt="BillionsBobby/JevRouter screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/GiesN/typesafe-jev-workflow">GiesN/typesafe-jev-workflow</a></b> — ⭐4 · Python · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · GiesN

##### Daten

Stars **4** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/anandi1989/awesome-jev-usecases">anandi1989/awesome-jev-usecases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · MIT · anandi1989

##### Daten

Stars **3** · Forks 1 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results

</details>

<details>
<summary><b><a href="https://github.com/SeeAPI/awesome-jev-use-cases">SeeAPI/awesome-jev-use-cases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · CC-BY-4.0 · SeeAPI

##### Daten

Stars **3** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.

</details>

<details>
<summary><b><a href="https://github.com/zhuyansen/jev-search-rerank-eval">zhuyansen/jev-search-rerank-eval</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · zhuyansen

##### Daten

Stars **3** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the judge-circularity bias measured.

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-shield">caiovicentino/jev-shield</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · caiovicentino

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check.

</details>

<details>
<summary><b><a href="https://github.com/doeixd/jev-pref">doeixd/jev-pref</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · doeixd

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/molis-ai/jev-workbench">molis-ai/jev-workbench</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · molis-ai

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/molis-ai--jev-workbench/00f61d8403a941cd.png" width="100%" alt="molis-ai/jev-workbench screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MongLong0214/jev-gate">MongLong0214/jev-gate</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MongLong0214

##### Daten

Stars **2** · Forks 0 · Offene Issues 5 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.

</details>

<details>
<summary><b><a href="https://github.com/ranjan2829/AskJev">ranjan2829/AskJev</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · ranjan2829

##### Daten

Stars **2** · Forks 2 · Offene Issues 2 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-mcp">rashedInt32/jev-mcp</a></b> — ⭐2 · TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · rashedInt32

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/samtay32/jev-system-architect">samtay32/jev-system-architect</a></b> — ⭐2 · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · MIT · samtay32

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives.

</details>

<details>
<summary><b><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher">abhishekashokvkumar/jev-mcp-dispatcher</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · abhishekashokvkumar

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Natural-language MCP tool dispatcher powered entirely by TypeSafe's Jev — no general-purpose LLM. Discovers a simple MCP server's tool signatures at runtime and uses Jev's typed primitives (Choice/Noul) to pick the right tool and extract its arguments straight out of the sentence.

</details>

<details>
<summary><b><a href="https://github.com/bestagentkits/jev-skillful">bestagentkits/jev-skillful</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · bestagentkits

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-starter">hamakyo/jev-starter</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · hamakyo

##### Daten

Stars **1** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-macos-loop">jcpsimmons/jev-macos-loop</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · AGPL-3.0 · jcpsimmons

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jcpsimmons--jev-macos-loop/19bcb6c0f1788073.gif" width="100%" alt="jcpsimmons/jev-macos-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jcpsimmons--jev-macos-loop/c99113da6464b245.gif" width="100%" alt="jcpsimmons/jev-macos-loop animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/jcpsimmons/jev-macos-loop/master/docs/media/jev-finder-batch-demo.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-model-router-demo">jcpsimmons/jev-model-router-demo</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · jcpsimmons

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

</details>

<details>
<summary><b><a href="https://github.com/noetion/dsh-jev">noetion/dsh-jev</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · noetion

##### Daten

Stars **1** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.

</details>

<details>
<summary><b><a href="https://github.com/omni-/ask-jev">omni-/ask-jev</a></b> — ⭐1 · PowerShell · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · PowerShell · MIT · omni-

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions.

</details>

<details>
<summary><b><a href="https://github.com/poponline63/hermes-jev-north-star">poponline63/hermes-jev-north-star</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · poponline63

##### Daten

Stars **1** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven.

</details>

<details>
<summary><b><a href="https://github.com/Ravinder82/jev-flash-router">Ravinder82/jev-flash-router</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · Ravinder82

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code

</details>

<details>
<summary><b><a href="https://github.com/rthomas24/jev-realtime-trading">rthomas24/jev-realtime-trading</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · rthomas24

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rthomas24--jev-realtime-trading/f27df5cca6b8e2cf.png" width="100%" alt="rthomas24/jev-realtime-trading screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/codex-jev-compaction">Wang-auspicious/codex-jev-compaction</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · Wang-auspicious

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills.

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/pi-jev-compaction">Wang-auspicious/pi-jev-compaction</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · Wang-auspicious

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev-powered context compaction for Pi. Keep critical instructions and tool history, prune the noise, and fall back gracefully.

</details>

<details>
<summary><b><a href="https://github.com/abeatrix/cline-plugin-jev-browser">abeatrix/cline-plugin-jev-browser</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · abeatrix

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Cline Plugin to add a new computer run tool runs by the typesafe/jev model

</details>

<details>
<summary><b><a href="https://github.com/ably-labs/jev-pong">ably-labs/jev-pong</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · Apache-2.0 · ably-labs

##### Daten

Stars **0** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Pong where the ball moves one step per model decision. Jev vs LLMs via Vercel AI Gateway, every player and agent on an Ably channel.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b51a044f9d543ef0.png" width="100%" alt="ably-labs/jev-pong screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b5b9b482a58f2c01.gif" width="100%" alt="ably-labs/jev-pong animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/aidil2105/jev-browser-pilot">aidil2105/jev-browser-pilot</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · aidil2105

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification.

</details>

<details>
<summary><b><a href="https://github.com/altregubov/jev-antigravity-mcp">altregubov/jev-antigravity-mcp</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · altregubov

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/alviso/jev-precheck">alviso/jev-precheck</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · alviso

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A second signature on every write an AI agent makes into a system of record. MCP proxy: fetch the records, derive in code, Jev judges. 98.6% recall, 0 false holds on 288 cases.

</details>

<details>
<summary><b><a href="https://github.com/anisselbd/jev-phishing-bench">anisselbd/jev-phishing-bench</a></b> — Python · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · anisselbd

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/openclaw-jev-harness">AntonioCoppe/openclaw-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · AntonioCoppe

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

OpenClaw plugin: jev-harness DecisionHarness as System One decide layer (policy/confidence/shadow)

</details>

<details>
<summary><b><a href="https://github.com/AStheTECH/mewcp-jev">AStheTECH/mewcp-jev</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · Apache-2.0 · AStheTECH

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

JEV MCP server by MewCP

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-align">caiovicentino/jev-align</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · caiovicentino

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Calibrated alignment verifier for LLM responses and agent plans — powered by Jev

</details>

<details>
<summary><b><a href="https://github.com/cbruyndoncx/AskJev-MCP">cbruyndoncx/AskJev-MCP</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · cbruyndoncx

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence

</details>

<details>
<summary><b><a href="https://github.com/DoGMaTiiC/hermes-jev">DoGMaTiiC/hermes-jev</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · DoGMaTiiC

##### Daten

Stars **0** · Forks 0 · Offene Issues 7 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only.

</details>

<details>
<summary><b><a href="https://github.com/duketopceo/jev-compact">duketopceo/jev-compact</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · duketopceo

##### Daten

Stars **0** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP

</details>

<details>
<summary><b><a href="https://github.com/EtienneLescot/jev-router">EtienneLescot/jev-router</a></b> — HTML · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · HTML · MIT · EtienneLescot

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model tier and reasoning depth.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/etiennelescot--jev-router/96217fad0b128b3e.png" width="100%" alt="EtienneLescot/jev-router screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fast-facts/jev-mcp">fast-facts/jev-mcp</a></b> — Go · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Go · MIT · fast-facts

##### Daten

Stars **0** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/flaviusapop/jev-router">flaviusapop/jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · flaviusapop

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Routes each turn in Claude Code, Codex, Grok and opencode to the cheapest model and reasoning depth that can finish it, using TypeSafe Jev

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/flaviusapop--jev-router/b7f868696d35b78b.png" width="100%" alt="flaviusapop/jev-router screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Friedjof/jev-mobile">Friedjof/jev-mobile</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · Friedjof

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Fast structured Android control loops with TypeSafe Jev and Mobile MCP

</details>

<details>
<summary><b><a href="https://github.com/gholtzap/jev-codex-model-and-effort-router">gholtzap/jev-codex-model-and-effort-router</a></b> — inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · gholtzap

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/gzawadzki/jev-usecases">gzawadzki/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · gzawadzki

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage

</details>

<details>
<summary><b><a href="https://github.com/hangarbay/jev.mcp">hangarbay/jev.mcp</a></b> — Go · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Go · MIT · hangarbay

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/herval/openclaw-jev-plugin">herval/openclaw-jev-plugin</a></b> — inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · herval

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Jev as a message gate to determine if agents should respond

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-codex-plugin">integrate-your-mind/jev-codex-plugin</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · integrate-your-mind

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Open-source Codex plugin for TypeSafe Jev decision consultation, failure diagnosis, and evidence-based completion review

</details>

<details>
<summary><b><a href="https://github.com/its-panzer/jev-model-router">its-panzer/jev-model-router</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · its-panzer

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A policy router that picks the cheapest Claude model that can finish the job

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/its-panzer--jev-model-router/98819f5aaf8e6373.png" width="100%" alt="its-panzer/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcressler/fast-jev-compaction-codex">jcressler/fast-jev-compaction-codex</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · jcressler

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Task-aware Jev evidence selection and exact local recovery around native Codex compaction.

</details>

<details>
<summary><b><a href="https://github.com/jmanhype/jev-dspy-lab">jmanhype/jev-dspy-lab</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · jmanhype

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/jev-pii-guardrail">jms-dcksn/jev-pii-guardrail</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · jms-dcksn

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A UiPath coded agent with a custom PII detection guardrail on the LLM boundary, built on the TypeSafe Jev model as a LangChain awrap_model_call middleware.

</details>

<details>
<summary><b><a href="https://github.com/JoacoMarc/jev-harness-router">JoacoMarc/jev-harness-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · JoacoMarc

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Per-turn harness router on Jev (TypeSafe): one batched call picks the model tier, tools, skill and effort budget for an agent turn, behind a hard latency deadline.

</details>

<details>
<summary><b><a href="https://github.com/kaijia323/dsh-plugin-jev">kaijia323/dsh-plugin-jev</a></b> — HTML · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · HTML · MIT · kaijia323

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/khordoo/jev-reflex-autonomy-lab">khordoo/jev-reflex-autonomy-lab</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · khordoo

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/khordoo/jev-reflex-autonomy-lab/main/docs/images/reflex-dashboard.png" width="100%" alt="khordoo/jev-reflex-autonomy-lab screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">MahmoudAdelbghany/jev-browser</a></b> — JavaScript · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MahmoudAdelbghany

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included.

</details>

<details>
<summary><b><a href="https://github.com/marcAllari/jev-mcp-router">marcAllari/jev-mcp-router</a></b> — inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · marcAllari

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/micic-mihajlo/jev-tool-runner">micic-mihajlo/jev-tool-runner</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · micic-mihajlo

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/milanboers/jev-plays-pokemon">milanboers/jev-plays-pokemon</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · NOASSERTION · milanboers

##### Daten

Stars **0** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Playing Pokemon Red using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/minhgv/jev-mcp">minhgv/jev-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · minhgv

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe Jev MCP decision layer for coding agents and CI

</details>

<details>
<summary><b><a href="https://github.com/morcoan/JevSeek">morcoan/JevSeek</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · morcoan

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools, persistent sessions, React desktop, and documented research.

</details>

<details>
<summary><b><a href="https://github.com/MSalvalaggio/jev-reflex">MSalvalaggio/jev-reflex</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · MSalvalaggio

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision).

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-mcp">nekowasabi/jev-routing-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · nekowasabi

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/Nyarlathoteppppp/pi-jev-context">Nyarlathoteppppp/pi-jev-context</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · Nyarlathoteppppp

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Cache-neutral context trimming for the pi coding agent, powered by TypeSafe Jev: long tool output cut to verbatim key lines before it enters context, with lossless recall. Measured, with pre-registered benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Panebianco00/jev-claude">Panebianco00/jev-claude</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · Panebianco00

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Route Claude Code's coding decisions through TypeSafe Jev: typed choices with probabilities, enforced at plan approval, questions, and risky commands.

</details>

<details>
<summary><b><a href="https://github.com/phin-tech/pi-jev-approver">phin-tech/pi-jev-approver</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · phin-tech

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Shell command safety gate for the Pi coding agent, backed by TypeSafe's Jev judgment model

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-mcp-router">Pinutss/jev-mcp-router</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · Pinutss

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Select relevant MCP tools under a context-token budget, without executing them.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-mcp-router/3947a2a5cc3750c8.png" width="100%" alt="Pinutss/jev-mcp-router screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-memory-selector">Pinutss/jev-memory-selector</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · Pinutss

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-plugins">Pinutss/jev-plugins</a></b> — inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · MIT · Pinutss

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Cursor and Hermes marketplace for the four published JEV Labs routers.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-plugins/b3fcd72ac9e61f49.jpg" width="100%" alt="Pinutss/jev-plugins screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/raj8525/universal-jev">raj8525/universal-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · raj8525

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents

</details>

<details>
<summary><b><a href="https://github.com/rubichandrap/hermes-jev-guard">rubichandrap/hermes-jev-guard</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · rubichandrap

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check

</details>

<details>
<summary><b><a href="https://github.com/Saik0s/diffusiongemma-jev-macos">Saik0s/diffusiongemma-jev-macos</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · Saik0s

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Local JEV-style decisions with DiffusionGemma on Apple Silicon, with benchmarks and coding-agent examples.

</details>

<details>
<summary><b><a href="https://github.com/sypherin/jev-trace-classifier">sypherin/jev-trace-classifier</a></b> — Python · inferred · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · sypherin

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next

</details>

<details>
<summary><b><a href="https://github.com/szocpaul/jev-compaction-prime">szocpaul/jev-compaction-prime</a></b> — inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · szocpaul

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Verbatim, decision-based context compaction for Prime Agent — instead of summaries, stale tool calls are scored and dropped; everything kept stays byte-for-byte intact.

</details>

<details>
<summary><b><a href="https://github.com/tgiridhar/claude-code-jev-smart-router">tgiridhar/claude-code-jev-smart-router</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · tgiridhar

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task phase and the cost of an undetected error, gated by prompt-cache arithmetic. Proof of concept.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tgiridhar--claude-code-jev-smart-router/28b9e1b2a005c7e2.png" width="100%" alt="tgiridhar/claude-code-jev-smart-router screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/themsquared/jev-benchmark">themsquared/jev-benchmark</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · Apache-2.0 · themsquared

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.

</details>

<details>
<summary><b><a href="https://github.com/thevibeworks/awesome-typesafe-jev">thevibeworks/awesome-typesafe-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · NOASSERTION · thevibeworks

##### Daten

Stars **0** · Forks 1 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/trietphan/jev-claw">trietphan/jev-claw</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · MIT · trietphan

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Typed model routing for OpenClaw agents, powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/ussyverse/hermes-jev-router">ussyverse/hermes-jev-router</a></b> — Python · inferred · 2 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Python · MIT · ussyverse

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending.

</details>

<details>
<summary><b><a href="https://github.com/wotai-dev/typesafe-jev-tools">wotai-dev/typesafe-jev-tools</a></b> — Shell · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · Shell · MIT · wotai-dev

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 149-row comparison of TypeSafe Jev against Claude Haiku 4.5.

</details>

<details>
<summary><b><a href="https://github.com/yangzhou-chaofan/awesome-jev-prompt">yangzhou-chaofan/awesome-jev-prompt</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · JavaScript · CC0-1.0 · yangzhou-chaofan

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

latest top 100 showcases for jev (keep updating) from x / github / latest sources

</details>

<details>
<summary><b><a href="https://github.com/zhangxaochen/dsh-jev">zhangxaochen/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `inferred` · TypeScript · MIT · zhangxaochen

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev (System One decision model) plugin suite for DeepSeek Harness (dsh)

</details>

<details>
<summary><b><a href="https://github.com/DevMortimer/pi-warden">DevMortimer/pi-warden</a></b> — ⭐62 · TypeScript · unverified · 0 天 · ⭐+1</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `unverified` · TypeScript · MIT · DevMortimer

##### Daten

Stars **62** (+1) · Forks 3 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop

> Guardrails that steer an agent before it acts. Demonstrates the gate pattern, where the decision is cheap enough to run on every step.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devmortimer--pi-warden/b8dc20ac6694613a.png" width="100%" alt="DevMortimer/pi-warden screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/3clyp50/a0-typesafe-ai">3clyp50/a0-typesafe-ai</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `unverified` · Python · MIT · 3clyp50

##### Daten

Stars **4** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/3clyp50--a0-typesafe-ai/9aa8ea4ef8241f14.png" width="100%" alt="3clyp50/a0-typesafe-ai screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/zoidsh/tenet">zoidsh/tenet</a></b> — ⭐4 · Go · unverified · 0 天 · ⭐+1</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `unverified` · Go · MIT · zoidsh

##### Daten

Stars **4** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

The review gate for code that agents write: rules in plain language, judged on every commit

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/pi-quiet-ask">HyunjunJeon/pi-quiet-ask</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Basisfakten

`Agent-Tooling: MCP, Hooks, Gates und Coding-Agents` · Community · `unverified` · TypeScript · MIT · HyunjunJeon

##### Daten

Stars **3** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe Jev as the pi coding agent's quiet decision layer

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hyunjunjeon--pi-quiet-ask/7ee3a99430e853d8.png" width="100%" alt="HyunjunJeon/pi-quiet-ask screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<a id="routing-guardrails"></a>

## Routing, Guardrails und Freigaben

Der produktionsnahe Anwendungsfall: jede Anfrage an das günstigste Modell schicken, das sie tatsächlich bewältigen kann, und das Ergebnis deterministisch prüfen.

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐44 · Rust · observed · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `observed` · Rust · NOASSERTION · Dicklesworthstone

##### Daten

Stars **44** · Forks 3 · Offene Issues 1 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐26 · Python · observed · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `observed` · Python · brainstormity

##### Daten

Stars **26** · Forks 2 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

<sub>Im Code verwendet: `typesafe/__init__.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 1 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `observed` · Python · MIT · Foadsf

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `observed` · TypeScript · MIT · qddegtya

##### Daten

Stars **1** · Forks 0 · Offene Issues 3 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed decisions from a System One model. An uncertain answer is a different type from a confident one — and the compiler makes you handle it.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `observed` · Python · aniruddh-krovvidi

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/lorensation/llm-cost-optimizer-jev">lorensation/llm-cost-optimizer-jev</a></b> — observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `observed` · Apache-2.0 · lorensation

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

An intelligent routing layer powered by TypeSafe AI's System One model Jev that sits in front of multiple LLM providers, analyzes each incoming request’s complexity, routes it to the cheapest model capable of handling it at acceptable quality, and continuously validates that routing decisions are correct.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐25 · TypeScript · inferred · 0 天 · ⭐+3</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · MIT · yusukebe

##### Daten

Stars **25** (+3) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐6 · JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · JavaScript · MIT · mejiasd3v

##### Daten

Stars **6** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · andrelandgraf

##### Daten

Stars **3** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Python · MIT · keeltrace

##### Daten

Stars **3** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/jerryfane/omp-jev-compaction">jerryfane/omp-jev-compaction</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · MIT · jerryfane

##### Daten

Stars **2** · Forks 1 · Offene Issues 2 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Python · MIT · maker-KK

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐2 · Python · inferred · 1 天 · ⭐+1</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Python · MIT · prismhq

##### Daten

Stars **2** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Python · MIT · WiktorB2004

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Python · MIT · Pinutss

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Shashank-H

##### Daten

Stars **1** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/vtrivedy/jev-plays-games">vtrivedy/jev-plays-games</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · JavaScript · vtrivedy

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Chess, Connect Four, and a decision model. Play Jev or watch Jev play itself.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/vtrivedy/jev-plays-games/main/docs/screenshots/chess.jpg" width="100%" alt="vtrivedy/jev-plays-games screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/aaronshaf/opencode-jev-model-router">aaronshaf/opencode-jev-model-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · MIT · aaronshaf

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev-based automatic per-turn model routing for OpenCode

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Jupyter · MIT · bitnovus

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/carllippert/jev-router">carllippert/jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · MIT · carllippert

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Express with no routes. TypeSafe Jev picks which handler runs.

</details>

<details>
<summary><b><a href="https://github.com/danfry1/jev-triage">danfry1/jev-triage</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · MIT · danfry1

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

GitHub Action that labels, deduplicates and spam-checks issues with Jev, with calibrated confidence for every decision

</details>

<details>
<summary><b><a href="https://github.com/danielhirt/jev-lab">danielhirt/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · danielhirt

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison

</details>

<details>
<summary><b><a href="https://github.com/gnoviawan/omp-jev-tools">gnoviawan/omp-jev-tools</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · NOASSERTION · gnoviawan

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation verification

</details>

<details>
<summary><b><a href="https://github.com/hugo-alves/jev-router-playground">hugo-alves/jev-router-playground</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · JavaScript · MIT · hugo-alves

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Interactive playground for testing Jev model-routing decisions against OpenRouter models

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hugo-alves--jev-router-playground/93692a5f183f12e1.jpg" width="100%" alt="hugo-alves/jev-router-playground screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iefnaf/pi-jev">iefnaf/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · MIT · iefnaf

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Pi extension suite powered by Jev: selective context compaction and model routing

</details>

<details>
<summary><b><a href="https://github.com/kenhuangus/jev-usecases">kenhuangus/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Python · MIT · kenhuangus

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kenhuangus--jev-usecases/be919255190f6495.png" width="100%" alt="kenhuangus/jev-usecases screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-bot">kevin9327/jev-bot</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Python · MIT · kevin9327

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.

</details>

<details>
<summary><b><a href="https://github.com/Loule95450/jev-free-router">Loule95450/jev-free-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · JavaScript · MIT · Loule95450

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Dynamic per-turn model router on free OpenCode Zen + Go models (fork of gargpratyush/jev-router)

</details>

<details>
<summary><b><a href="https://github.com/makefinks/jev-feed-filter">makefinks/jev-feed-filter</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · MIT · makefinks

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Smart, dynamic AI filtering for X and YouTube feeds using Jev

</details>

<details>
<summary><b><a href="https://github.com/mcgalleg/grokbot-jev-jobs">mcgalleg/grokbot-jev-jobs</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · mcgalleg

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Scores public job postings against my resume using TypeSafe's jev via the Vercel AI Gateway. Daily Vercel cron.

</details>

<details>
<summary><b><a href="https://github.com/MoonTory/pi-jev-harness">MoonTory/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · MoonTory

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards tool calls

</details>

<details>
<summary><b><a href="https://github.com/nitinnat/jev-gateway">nitinnat/jev-gateway</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · JavaScript · MIT · nitinnat

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A small local HTTP service for TypeSafe AI's Jev through Vercel

</details>

<details>
<summary><b><a href="https://github.com/perixtar/jev-e2e">perixtar/jev-e2e</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · MIT · perixtar

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Natural-language end-to-end tests for web apps, powered by Jev and Playwright.

</details>

<details>
<summary><b><a href="https://github.com/rajivkuriakose/typesafe-jev-examples">rajivkuriakose/typesafe-jev-examples</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Python · MIT · rajivkuriakose

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/SadiqOnGithub/jev-lab">SadiqOnGithub/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · TypeScript · SadiqOnGithub

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API

</details>

<details>
<summary><b><a href="https://github.com/TokenTrim/jev-routing-experiment">TokenTrim/jev-routing-experiment</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Python · Apache-2.0 · TokenTrim

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tokentrim--jev-routing-experiment/1c31bd606ebc1994.png" width="100%" alt="TokenTrim/jev-routing-experiment screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ufec/jev-block-android-ad">ufec/jev-block-android-ad</a></b> — Kotlin · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · Kotlin · MIT · ufec

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

JevNoiseGate filters unwanted notifications and SMS on Android. Rather than   matching keywords, an LLM decides what's noise — and only what it explicitly   flags is blocked. Verification codes are matched on-device and never uploaded;   anything uncertain passes through.

</details>

<details>
<summary><b><a href="https://github.com/wadadanet/faq-jev-router">wadadanet/faq-jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `inferred` · JavaScript · MIT · wadadanet

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Cascade FAQ routing with TypeSafe Jev — category → FAQ or not found (GitHub Pages demo)

</details>

<details>
<summary><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">iammrduncan/typesafe-ai-benchmark</a></b> — ⭐31 · TypeScript · unverified · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `unverified` · TypeScript · MIT · iammrduncan

##### Daten

Stars **31** · Forks 5 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.

> A gateway that mimics the System One interface, which is what makes side-by-side benchmarking possible without rewriting the caller.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/3d66c620e48ff597.gif" width="100%" alt="iammrduncan/typesafe-ai-benchmark animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/iammrduncan/typesafe-ai-benchmark/main/docs/media/theater-demo.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kavehmz/typesafe-playground">kavehmz/typesafe-playground</a></b> — ⭐7 · JavaScript · unverified · 0 天 · ⭐+1</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `unverified` · JavaScript · kavehmz

##### Daten

Stars **7** (+1) · Forks 2 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/kavehmz/typesafe-playground/main/docs/images/demo03-fable.png" width="100%" alt="kavehmz/typesafe-playground screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/raihankhan-rk/diffjury">raihankhan-rk/diffjury</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Basisfakten

`Routing, Guardrails und Freigaben` · Community · `unverified` · TypeScript · raihankhan-rk

##### Daten

Stars **3** · Forks 1 · Offene Issues 2 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

DiffJury — TypeSafe Jev PR risk router + code review coach

</details>

<a id="evaluation"></a>

## Evaluation, Kalibrierung und Benchmarks

Wie man überhaupt weiß, ob die Entscheidungen gut sind. Kalibrierung ist die offene Frage dieses Ökosystems, und diese Projekte messen sie.

<details>
<summary><b><a href="https://github.com/edgardcham/huncho">edgardcham/huncho</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `observed` · TypeScript · MIT · edgardcham

##### Daten

Stars **1** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Decisions as code on System One models: typed questions, thresholds with hysteresis, nested decisions, journal, calibration

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `observed` · Go · MIT · Gaurav-Gosain

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `observed` · Python · Apache-2.0 · hev

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — Python · observed · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `observed` · Python · akash-kamat

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/nishioka-shinji/jev-edgar">nishioka-shinji/jev-edgar</a></b> — Python · observed · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `observed` · Python · nishioka-shinji

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Does Jev, a System One model returning calibrated probabilities, say anything useful about an earnings release before the market prices it?

</details>

<details>
<summary><b><a href="https://github.com/JoshuaSP/open-jev">JoshuaSP/open-jev</a></b> — ⭐14 · Python · inferred · 1 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · MIT · JoshuaSP

##### Daten

Stars **14** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed JSON inference with DiffusionGemma, with Every and Jev benchmark results

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/joshuasp--open-jev/1d4a9f6368358e43.png" width="100%" alt="JoshuaSP/open-jev screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rorshopping/jev-on-a-laptop">rorshopping/jev-on-a-laptop</a></b> — ⭐14 · Python · inferred · 1 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · NOASSERTION · rorshopping

##### Daten

Stars **14** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Unofficial study: Jev-style parallel typed decisions on stock 1.5B-8B models on an Apple Silicon laptop. Benchmarks, research notes, and a Hugging Face Space demo.

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐7 · Python · inferred · 1 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · Apache-2.0 · AbdelStark

##### Daten

Stars **7** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐5 · TypeScript · inferred · 2 天 · ⭐+1</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · TypeScript · MIT · y0usaf

##### Daten

Stars **5** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/abhixhek/jevcal">abhixhek/jevcal</a></b> — ⭐4 · Python · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · MIT · abhixhek

##### Daten

Stars **4** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abhixhek--jevcal/3dbe2307176737c8.png" width="100%" alt="abhixhek/jevcal screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐4 · Python · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · NOASSERTION · Heman10x-NGU

##### Daten

Stars **4** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · Apache-2.0 · ikermoel

##### Daten

Stars **2** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Open alternative to Jev: typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with benchmarks

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · MIT · wondertwins

##### Daten

Stars **2** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rongxinzy/LightJev">rongxinzy/LightJev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · Apache-2.0 · rongxinzy

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Train lightweight language backbones for typed decisions and candidate probabilities. CE/Brier training, evaluation, and an offline end-to-end demo.

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · 4esv

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-eval/main/results/coverage.png" width="100%" alt="4esv/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/aieo-product/jev-gamebenchmark">aieo-product/jev-gamebenchmark</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · MIT · aieo-product

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Sandbox & benchmark: optimize how you ask Jev (TypeSafe System One) to play falling-block puzzle games, head-to-head against LLMs

</details>

<details>
<summary><b><a href="https://github.com/carson-sweet/jev-plays-brogue">carson-sweet/jev-plays-brogue</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · TypeScript · AGPL-3.0 · carson-sweet

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

TypeSafe's Jev model plays the roguelike Brogue live -- a hand-built expert system for System-2 reasoning, outcome-calibrated self-learning, and a web UI to watch decisions, costs, and training progress.

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · TypeScript · MIT · Danu28

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · TeX · NOASSERTION · dnakhoa

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · eggmasonvalue

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · MIT · jujumilk3

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · JavaScript · MIT · KantaHayashiAI

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and">musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and</a></b> — HTML · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · HTML · MIT · musman550

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@automatewithmusfiraai"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@automatewithmusfiraai">Ansehen auf youtube.com</a> · die Wiedergabe öffnet auf der Host-Seite; GitHub kann sie nicht direkt einbetten</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/onlyoneaman/jev-eval">onlyoneaman/jev-eval</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · TypeScript · MIT · onlyoneaman

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/onlyoneaman--jev-eval/e5d471e96e134f81.png" width="100%" alt="onlyoneaman/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/robipop22/Jev-is-odd">robipop22/Jev-is-odd</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · JavaScript · MIT · robipop22

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Ask Jev by TypeSafe AI whether a number is odd. TypeScript, real token usage, and latency benchmarks.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/robipop22--jev-is-odd/5c4ddde817bd6cdc.png" width="100%" alt="robipop22/Jev-is-odd screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/SHAKULMITTAL22/jev-resume">SHAKULMITTAL22/jev-resume</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · AGPL-3.0 · SHAKULMITTAL22

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Folio: job-specific resume leaderboards with approved rubrics, evidence-backed AI evaluation, and human hiring decisions.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shakulmittal22--jev-resume/e653593f3a00df9d.png" width="100%" alt="SHAKULMITTAL22/jev-resume screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shunta-furukawa/jev-tick-lab">shunta-furukawa/jev-tick-lab</a></b> — inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · shunta-furukawa

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis.

</details>

<details>
<summary><b><a href="https://github.com/teyhouse/jev-secret-detection">teyhouse/jev-secret-detection</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · teyhouse

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" width="100%" alt="teyhouse/jev-secret-detection screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/us/jev-local">us/jev-local</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `inferred` · Python · us

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Local Jev-compatible evaluation server: POST /v1/systemone with typed noul/choice/score, open weights, no waitlist

</details>

<details>
<summary><b><a href="https://github.com/kyotofin/tax-doc-classifier">kyotofin/tax-doc-classifier</a></b> — ⭐65 · TypeScript · unverified · 0 天 · ⭐+57</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `unverified` · TypeScript · Apache-2.0 · kyotofin

##### Daten

Stars **65** (+57) · Forks 5 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.

</details>

<details>
<summary><b><a href="https://github.com/Mapika/decider">Mapika/decider</a></b> — ⭐24 · Python · unverified · 0 天 · ⭐+1</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `unverified` · Python · Apache-2.0 · Mapika

##### Daten

Stars **24** (+1) · Forks 2 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mapika--decider/c67d355f22dcb51a.gif" width="100%" alt="Mapika/decider animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/genai-craft/openvons">genai-craft/openvons</a></b> — ⭐7 · Python · unverified · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `unverified` · Python · NOASSERTION · genai-craft

##### Daten

Stars **7** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド

</details>

<details>
<summary><b><a href="https://github.com/aabolfazl/typesafe-local">aabolfazl/typesafe-local</a></b> — ⭐4 · Python · unverified · 0 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `unverified` · Python · MIT · aabolfazl

##### Daten

Stars **4** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/aabolfazl--typesafe-local/ada59cf382af5143.png" width="100%" alt="aabolfazl/typesafe-local screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mithalouni/system-one-open">mithalouni/system-one-open</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### Basisfakten

`Evaluation, Kalibrierung und Benchmarks` · Community · `unverified` · Python · NOASSERTION · mithalouni

##### Daten

Stars **4** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal)

</details>

<a id="research-models"></a>

## Offene Reproduktionen, Gewichte und Architekturforschung

Offene Gewichte, kleine Nachbauten und Architekturarbeit. Mehrere davon existieren, weil sich das Kalibrierungsverhalten nicht allein aus öffentlichem Material reproduzieren lässt.

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐60 · Python · observed · 0 天 · ⭐+2</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `observed` · Python · MIT · kshetrajna12

##### Daten

Stars **60** (+2) · Forks 3 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐339 · Python · inferred · 0 天 · ⭐+21</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · MIT · TianyuCodings

##### Daten

Stars **339** (+21) · Forks 27 · Offene Issues 1 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/5055af419619e7e4.gif" width="100%" alt="TianyuCodings/NanoJev animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/assets/side_by_side_maze.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐21 · Python · inferred · 0 天</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · MIT · r-ms

##### Daten

Stars **21** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `observed`

##### Daten

Downloads 25 · Likes 2 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 0 天</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `observed`

##### Daten

Downloads 0 · Likes 0 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐142 · Python · inferred · 0 天 · ⭐+13</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · ekzhang

##### Daten

Stars **142** (+13) · Forks 12 · Offene Issues 1 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐23 · Python · inferred · 0 天 · ⭐+2</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · MIT · bnsd55

##### Daten

Stars **23** (+2) · Forks 3 · Offene Issues 2 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/featherless-ai/simple-jev">featherless-ai/simple-jev</a></b> — ⭐10 · Python · inferred · 0 天</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · featherless-ai

##### Daten

Stars **10** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Turn any open model into a classifier/jev endpoint

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/featherless-ai/simple-jev/main/imgs/Simple-Jev-Logo.png" width="100%" alt="featherless-ai/simple-jev screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/wfzyx/von">wfzyx/von</a></b> — ⭐3 · Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · wfzyx

##### Daten

Stars **3** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/choxos/jev-reviewer">choxos/jev-reviewer</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · JavaScript · MIT · choxos

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Ask a trial report and its supplements for systematic review data by voice, text or a questions file. Jev (TypeSafe System One) points at the lines; every answer is a verbatim quote with its file and place. PDF, Word, Excel, PowerPoint, OpenDocument, RTF, HTML and CSV; projects and studies kept in your browser.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/4a551dbca9d0c41e.jpg" width="100%" alt="choxos/jev-reviewer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/71abea319063ce6d.gif" width="100%" alt="choxos/jev-reviewer animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kw2828/OpenJev">kw2828/OpenJev</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · MIT · kw2828

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Browser decision playground and reproducible experiments on memory, uncertainty, and Doom control

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/7caa9b0eff4636a1.png" width="100%" alt="kw2828/OpenJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/af5371a3a94cb693.gif" width="100%" alt="kw2828/OpenJev animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/deep-diver/mini-jev">deep-diver/mini-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · deep-diver

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-nethack">integrate-your-mind/jev-nethack</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · integrate-your-mind

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev x NetHack: bounded runner, research code, and completed recording releases

</details>

<details>
<summary><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">legacybridge-tech/pi-typesafe-jev</a></b> — TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · TypeScript · NOASSERTION · legacybridge-tech

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.

</details>

<details>
<summary><b><a href="https://github.com/objectgraph/jev-samegame-bench">objectgraph/jev-samegame-bench</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · TypeScript · MIT · objectgraph

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

What should a decision model be shown to play SameGame? 21 prompt strategies for TypeSafe's Jev, 76,795 logged requests and responses, reproducible tables. MIT.

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `inferred` · Python · shellneko

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐7 · Python · unverified · 2 天 · ⭐+2</summary>

##### Basisfakten

`Offene Reproduktionen, Gewichte und Architekturforschung` · Community · `unverified` · Python · NOASSERTION · zhihz

##### Daten

Stars **7** (+2) · Forks 1 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<a id="apps-demos"></a>

## Anwendungen, Spiele, Robotik und interaktive Demos

Spiele, Roboter, Browser und Dashboards. Demos sind der Weg, auf dem Aussagen zu Latenz und Kosten lesbar werden.

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐8 · Python · observed · 0 天 · ⭐+1</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `observed` · Python · Apache-2.0 · zadescoxp

##### Daten

Stars **8** (+1) · Forks 1 · Offene Issues 3 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐2 · TypeScript · observed · 0 天 · ⭐+1</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `observed` · TypeScript · daftAI2026

##### Daten

Stars **2** (+1) · Forks 1 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `observed` · Rust · MIT · markjaquith

##### Daten

Stars **1** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `observed` · TypeScript · adiun

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `observed` · Dart · Bud-ro

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/chris-wozniczek/jev-voice-control">chris-wozniczek/jev-voice-control</a></b> — Swift · observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `observed` · Swift · chris-wozniczek

##### Daten

Stars **0** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-bar Swift app.

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `observed` · Python · MIT · tirukovelamanoj

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/8c1b0d55baf76296.gif" width="100%" alt="tirukovelamanoj/jev-plays-doom animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/tirukovelamanoj/jev-plays-doom/main/docs/jev-doom.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `observed` · TypeScript · wustep

##### Daten

Stars **0** · Forks 0 · Offene Issues 4 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://x.com/tspy/status/2100864234523685146">X intent labeller</a></b> — @tspy · observed · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `observed` · [yishan](https://x.com/tspy) · @tspy · x.com

##### Daten

Aufrufe 2364 · Likes 15 · Kommentare 9 · Veröffentlicht 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A Chrome extension that labels posts in an X timeline with their intent and probability as you scroll, drawn as a tag directly after each post's timestamp. Categories include inducement, provocation, promotion, machine-generated, persuasion, entertainment and information. A side panel reports session counts (seen, judged, correct) and cumulative token cost. The author reports near-instant responses and usable accuracy before any tuning.

<sub>Der Link zum Originalprojekt wird noch ermittelt.</sub>

> Worth reading as a latency argument rather than an accuracy one: labelling a timeline only works if the decision costs less than the scroll, which is the constraint a generative model cannot meet.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/0641644f12a25a45.jpg" width="100%" alt="X intent labeller screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/b80cf3173f63bdd7.gif" width="100%" alt="X intent labeller animation"><br><sub>animierte Aufzeichnung · <a href="https://video.twimg.com/amplify_video/2100858340331200512/vid/avc1/1242x720/ex2FF5-TerVxo9xX.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐103 · Python · inferred · 0 天 · ⭐+3</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Python · MIT · hr98w

##### Daten

Stars **103** (+3) · Forks 11 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐89 · TypeScript · inferred · 0 天 · ⭐+8</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · TypeScript · MIT · jkudish

##### Daten

Stars **89** (+8) · Forks 4 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/b4ae7fc04353e74c.gif" width="100%" alt="jkudish/jev-browser animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐54 · JavaScript · inferred · 0 天 · ⭐+13</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · JavaScript · MIT · moritzkremb

##### Daten

Stars **54** (+13) · Forks 8 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/mizchi/jev-playground">mizchi/jev-playground</a></b> — ⭐14 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · TypeScript · mizchi

##### Daten

Stars **14** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐6 · Python · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Python · MIT · komorra

##### Daten

Stars **6** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · TypeScript · emrickgarrett

##### Daten

Stars **5** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/arielweinberger/jev-autopilot">arielweinberger/jev-autopilot</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · TypeScript · arielweinberger

##### Daten

Stars **3** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs $0.01.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/arielweinberger/jev-autopilot/main/docs/demo.png" width="100%" alt="arielweinberger/jev-autopilot screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐3 · JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · JavaScript · vinilana

##### Daten

Stars **3** · Forks 3 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 1 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Go · MIT · paulsmith

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · TypeScript · MIT · vmendes90

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/vmendes90--jev-shield/ee87b261d199a34c.jpg" width="100%" alt="vmendes90/jev-shield screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-mario">4esv/jev-mario</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Python · 4esv

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe Jev plays Super Mario Bros from a text description of emulator RAM

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-mario/main/runs/1-1-branch-jev-20260918-145250.gif" width="100%" alt="4esv/jev-mario screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-mario/main/runs/1-1-branch-jev-20260918-145250.gif" width="100%" alt="4esv/jev-mario animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · TypeScript · Little-Planet-Labs

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Python · PistachioAIHQ

##### Daten

Stars **1** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/bahramzada/jev-taxi-dispatch">bahramzada/jev-taxi-dispatch</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · JavaScript · MIT · bahramzada

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Real-vaxt taksi dispetçerlik simulyasiyası - TypeSafe JEV (System One) modeli ilə

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/bahramzada--jev-taxi-dispatch/e616f4168b15d3f2.png" width="100%" alt="bahramzada/jev-taxi-dispatch screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/BrendanH18/jev-lab">BrendanH18/jev-lab</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Python · MIT · BrendanH18

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brendanh18--jev-lab/b16b9535e3744cd3.png" width="100%" alt="BrendanH18/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/JYeswak/jev_playground">JYeswak/jev_playground</a></b> — Shell · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Shell · MIT · JYeswak

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jyeswak--jev_playground/b6414da07c9c5aa8.jpg" width="100%" alt="JYeswak/jev_playground screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/marcelomar21/demo-tetris-jev">marcelomar21/demo-tetris-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · JavaScript · marcelomar21

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Tetris arcade jogado pelo Jev da TypeSafe AI, com decisões em JSON, antecipação de jogadas e custo por partida.

</details>

<details>
<summary><b><a href="https://github.com/metrox-eth/moss-jev">metrox-eth/moss-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · JavaScript · metrox-eth

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

MOSS × Jev: a recorded-run 3D demo of the litter-picking rover choosing targets with TypeSafe's Jev decision model.

</details>

<details>
<summary><b><a href="https://github.com/n3ndor/n8n-nodes-typesafe-jev">n3ndor/n8n-nodes-typesafe-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · TypeScript · MIT · n3ndor

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

n8n community node for TypeSafe Jev structured AI decisions

</details>

<details>
<summary><b><a href="https://github.com/PauloLuan/jev-obscura-browser">PauloLuan/jev-obscura-browser</a></b> — Rust · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Rust · MIT · PauloLuan

##### Daten

Stars **0** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/PierrunoYT/JevFlow">PierrunoYT/JevFlow</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · TypeScript · PierrunoYT

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A trading bot powered by TypeSafe AI's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pistachiopranay/jev-synergy-screening">pistachiopranay/jev-synergy-screening</a></b> — inferred · 1 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · pistachiopranay

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/premithk/jev-games">premithk/jev-games</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Python · premithk

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/premithk/jev-games/main/output.gif" width="100%" alt="premithk/jev-games screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/premithk/jev-games/main/output.gif" width="100%" alt="premithk/jev-games animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/rchovatiya88/cyber-breach-jev">rchovatiya88/cyber-breach-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · JavaScript · rchovatiya88

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model

</details>

<details>
<summary><b><a href="https://github.com/runsenwu/jev-demo">runsenwu/jev-demo</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · Python · runsenwu

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Testing out jev

</details>

<details>
<summary><b><a href="https://github.com/tanayvasishtha/Slither-Me-Jev">tanayvasishtha/Slither-Me-Jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · JavaScript · tanayvasishtha

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

8 AI snakes, 1 human, 1 arena. Every snake is driven live by TypeSafe's Jev, making all decisions in real time

</details>

<details>
<summary><b><a href="https://github.com/yatharth1706/jev-automation">yatharth1706/jev-automation</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `inferred` · TypeScript · yatharth1706

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Trying automation on web browser via jev from typesafe

</details>

<details>
<summary><b><a href="https://github.com/sorrycc/typesafe-snake">sorrycc/typesafe-snake</a></b> — ⭐17 · TypeScript · unverified · 1 天</summary>

##### Basisfakten

`Anwendungen, Spiele, Robotik und interaktive Demos` · Community · `unverified` · TypeScript · sorrycc

##### Daten

Stars **17** · Forks 2 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code

</details>

<a id="media-discussions"></a>

## Artikel, Diskussionen und verwandte Listen

Launch-Threads, unabhängige Artikel und die anderen kuratierten Listen in diesem Feld. Dieses Repository ist nicht das einzige, und das zu sagen ist nützlicher, als das Gegenteil zu behaupten.

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐5147 · Python · observed · 0 天 · ⭐+210</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · Python · MIT · browser-use

##### Daten

Stars **5147** (+210) · Forks 317 · Offene Issues 29 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

i. am. speed.

<sub>Im Code verwendet: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcdb919ac3afb514.gif" width="100%" alt="browser-use/jev-ultrafast animation"><br><sub>animierte Aufzeichnung · <a href="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/demo.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1886 · observed · 3 天 · ⭐+1</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 1886 · Kommentare 495 · Letzter Push 2026-09-15 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐507 · Python · observed · 0 天 · ⭐+11</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · Python · MIT · Anil-matcha

##### Daten

Stars **507** (+11) · Forks 96 · Offene Issues 1 · Erstellt 2023-05-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>Im Code verwendet: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐220 · CSS · observed · 0 天 · ⭐+6</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · CSS · MIT · AbdelStark

##### Daten

Stars **220** (+6) · Forks 31 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>Im Code verwendet: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐187 · TypeScript · observed · 0 天 · ⭐+26</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · TypeScript · dabit3

##### Daten

Stars **187** (+26) · Forks 17 · Offene Issues 17 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

<sub>Im Code verwendet: `jev-lint/proxy.mjs`, `jev-tower/jev-proxy.mjs`, `jev-instant-search/bench/dump.ts`, `jev-swarm/jev-proxy.mjs`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐141 · Python · observed · 0 天 · ⭐+18</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · Python · yibie

##### Daten

Stars **141** (+18) · Forks 20 · Offene Issues 9 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐89 · observed · 0 天 · ⭐+7</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · CC0-1.0 · cobanov

##### Daten

Stars **89** (+7) · Forks 8 · Offene Issues 7 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐58 · observed · 0 天 · ⭐+2</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · CC0-1.0 · AnotiaWang

##### Daten

Stars **58** (+2) · Forks 16 · Offene Issues 2 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>Im Code verwendet: `README.md`, `README_zh.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐43 · observed · 1 天 · ⭐+1</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 43 · Kommentare 10 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐32 · JavaScript · observed · 0 天 · ⭐+3</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### Daten

Stars **32** (+3) · Forks 6 · Offene Issues 5 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A community directory of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐6 · JavaScript · observed · 0 天 · ⭐+1</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · JavaScript · NOASSERTION · OmniJev

##### Daten

Stars **6** (+1) · Forks 2 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Papers, open reproductions and independent evaluations behind System One models and Jev.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49758022">Lmjtfy – Ask Jev a yes or no question</a></b> — ⭐5 · observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 5 · Kommentare 1 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 2 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 5 · Kommentare 0 · Letzter Push 2026-09-15 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49757009">Bespoke Nimble: open data, open model, open recipe for an open Jev</a></b> — ⭐4 · observed · 0 天 · ⭐+1</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 4 · Kommentare 0 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 4 · Kommentare 0 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 4 · Kommentare 0 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 3 · Kommentare 0 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49757757">Show HN: Jeff – A read-only CLI for semantic code review using Jev</a></b> — ⭐3 · observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 3 · Kommentare 0 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 3 · Kommentare 0 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### Daten

Stars **2** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49753667">Show HN: Explore 2D semantic space with the Jev model</a></b> — ⭐2 · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 2 · Kommentare 0 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

SemanticSpace is an experiment around Jev, TypeSafe AI’s new model. It uses a Cartesian plane defined by arbitrary phrases for each axis, to map prompts onto the resulting 2D semantic space. You can edit the prompts and axes to visualize virtually any 2D relationship.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49750649">Show HN: Open-Source Alternative to TypeSafe.ai</a></b> — ⭐2 · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 2 · Kommentare 1 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49744527">Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)</a></b> — ⭐2 · observed · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 2 · Kommentare 1 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Full disclosure, it was coded with AI, I don&#x27;t claim otherwise. But I wanted to test out tool calls and iterative problem solving using Jev and needed a simple library&#x2F;framework&#x2F;harness to do that.
SOKIT (System One Knowledge, Instructions and Tools) is the result

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49729945">The first (public) System One Model; Jev gives AI the properties of code</a></b> — ⭐2 · observed · 2 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 2 · Kommentare 0 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755005">Two techniques for working with System One models</a></b> — ⭐2 · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 2 · Kommentare 0 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49757995">TypeSafe / Jev latency-focused demos built by Devin</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 2 · Kommentare 0 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49745212">Typesafe&#x27;s Jev is the fish at the poker table</a></b> — ⭐2 · observed · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 2 · Kommentare 1 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49733647">Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step</a></b> — ⭐2 · observed · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 2 · Kommentare 0 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49734345">Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD</a></b> — ⭐2 · observed · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed`

##### Daten

Punkte 2 · Kommentare 0 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐1 · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · NOASSERTION · aliaihub

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://github.com/ozers/jevsome-projects">ozers/jevsome-projects</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · JavaScript · MIT · ozers

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Open-source projects that provably call Jev, TypeSafe AI's System One model. Every entry links to the line of code that proves it. Refreshed daily.

</details>

<details>
<summary><b><a href="https://github.com/rhc98/awesome-jev">rhc98/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · TypeScript · NOASSERTION · rhc98

##### Daten

Stars **1** · Forks 0 · Offene Issues 1 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself.

</details>

<details>
<summary><b><a href="https://github.com/soderlind/ai-provider-for-jev">soderlind/ai-provider-for-jev</a></b> — ⭐1 · PHP · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · PHP · soderlind

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).

</details>

<details>
<summary><b><a href="https://github.com/alpibrusl/lex-judge">alpibrusl/lex-judge</a></b> — Lex · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · Lex · alpibrusl

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed judgments from a System One model, as a \[net\]-only Lex effect

</details>

<details>
<summary><b><a href="https://github.com/deepanwadhwa/OpenDecision">deepanwadhwa/OpenDecision</a></b> — Python · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · Python · Apache-2.0 · deepanwadhwa

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Open Type Safe System one model system

</details>

<details>
<summary><b><a href="https://github.com/gzd2032/typesafe-ai-test">gzd2032/typesafe-ai-test</a></b> — observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · gzd2032

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

a test repo for typesafe.ai

</details>

<details>
<summary><b><a href="https://github.com/hide-G/magi-system-on-jev">hide-G/magi-system-on-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · JavaScript · hide-G

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/hide-G/magi-system-on-jev/master/public/ogp.png" width="100%" alt="hide-G/magi-system-on-jev screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/JohnDotOwl/awesome-jev">JohnDotOwl/awesome-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · JavaScript · CC0-1.0 · JohnDotOwl

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A curated list of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/jtnkminimal/awesome-jev">jtnkminimal/awesome-jev</a></b> — Python · observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · Python · CC0-1.0 · jtnkminimal

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A curated projects built with Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/piyush97/focus-tube">piyush97/focus-tube</a></b> — JavaScript · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · JavaScript · MIT · piyush97

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model

</details>

<details>
<summary><b><a href="https://github.com/rbalch/typesafeai-review">rbalch/typesafeai-review</a></b> — Python · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · Python · rbalch

##### Daten

Stars **0** · Forks 0 · Offene Issues 6 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Using Typesafe.AI to generate diff reviews.

</details>

<details>
<summary><b><a href="https://github.com/robzolkos/omarchy-issue-classifier">robzolkos/omarchy-issue-classifier</a></b> — Ruby · observed · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · Ruby · robzolkos

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Classify the Omarchy issue backlog with Jev, TypeSafe's System One model. Ten typed questions per issue in one request, for a hundredth of a cent each.

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/jev-trader">Shashank-H/jev-trader</a></b> — observed · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · AGPL-3.0 · Shashank-H

##### Daten

Stars **0** · Forks 1 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

An automated trader using SystemOne model - TypesafeAI Jev

</details>

<details>
<summary><b><a href="https://github.com/TheGali/terrarium">TheGali/terrarium</a></b> — JavaScript · observed · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `observed` · JavaScript · MIT · TheGali

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.

</details>

<details>
<summary><b><a href="https://github.com/jarrodwatts/jev-trader">jarrodwatts/jev-trader</a></b> — ⭐826 · TypeScript · inferred · 1 天 · ⭐+17</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · jarrodwatts

##### Daten

Stars **826** (+17) · Forks 155 · Offene Issues 3 · Erstellt 2026-09-16 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

</details>

<details>
<summary><b><a href="https://github.com/droidrun/mobile-jev">droidrun/mobile-jev</a></b> — ⭐120 · JavaScript · inferred · 1 天 · ⭐+16</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · JavaScript · MIT · droidrun

##### Daten

Stars **120** (+16) · Forks 22 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/superagents-lab/jev-search">superagents-lab/jev-search</a></b> — ⭐74 · TypeScript · inferred · 0 天 · ⭐+25</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · superagents-lab

##### Daten

Stars **74** (+25) · Forks 10 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/superagents-lab--jev-search/5a545ddfd6a52aed.png" width="100%" alt="superagents-lab/jev-search screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mrnugget/jev-shell-history">mrnugget/jev-shell-history</a></b> — ⭐38 · TypeScript · inferred · 0 天 · ⭐+5</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · mrnugget

##### Daten

Stars **38** (+5) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Fish-style zsh history autosuggestions ranked by Jev (TypeSafe)

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history animation"><br><sub>animierte Aufzeichnung</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">IAmUnbounded/save-token-jev-clean</a></b> — ⭐34 · TypeScript · inferred · 0 天 · ⭐+3</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · IAmUnbounded

##### Daten

Stars **34** (+3) · Forks 8 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/daseinlabs/open-jev">daseinlabs/open-jev</a></b> — ⭐30 · Python · inferred · 0 天 · ⭐+3</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · daseinlabs

##### Daten

Stars **30** (+3) · Forks 4 · Offene Issues 4 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov"><img src="" width="100%" alt="daseinlabs/open-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hqman/JevScout">hqman/JevScout</a></b> — ⭐14 · Python · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · hqman

##### Daten

Stars **14** · Forks 1 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4"><img src="" width="100%" alt="hqman/JevScout video"></a><br><sub><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4">Video öffnen</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jon-devlapaz/jev-me">jon-devlapaz/jev-me</a></b> — ⭐9 · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · MIT · jon-devlapaz

##### Daten

Stars **9** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Grill-me with Jev optional each turn

</details>

<details>
<summary><b><a href="https://github.com/Kevthetech143/super-jev">Kevthetech143/super-jev</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · MIT · Kevthetech143

##### Daten

Stars **5** · Forks 1 · Offene Issues 4 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A small, extensible decision-to-action harness for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/gamesonrblx/JevML">gamesonrblx/JevML</a></b> — ⭐3 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · gamesonrblx

##### Daten

Stars **3** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Reusable machine-learning primitives for Jev — PCA, MCMC, text diffusion, neural cellular automata, and a task harness that picks the right tool.

</details>

<details>
<summary><b><a href="https://github.com/joelhooks/pi-fast-jev-compaction">joelhooks/pi-fast-jev-compaction</a></b> — ⭐3 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · joelhooks

##### Daten

Stars **3** (+1) · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Pi extension: verbatim context compaction with TypeSafe Jev decisions

</details>

<details>
<summary><b><a href="https://github.com/mateonunez/jod">mateonunez/jod</a></b> — ⭐3 · TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · mateonunez

##### Daten

Stars **3** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers.

</details>

<details>
<summary><b><a href="https://github.com/haseeb-heaven/jev-system-one">haseeb-heaven/jev-system-one</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · MIT · haseeb-heaven

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/haseeb-heaven--jev-system-one/e41c848323b1077a.png" width="100%" alt="haseeb-heaven/jev-system-one screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevinpita/pi-jev-context">kevinpita/pi-jev-context</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · kevinpita

##### Daten

Stars **2** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Reversible context pruning for Pi, powered by TypeSafe Jev. Keep useful context without deleting session history.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevinpita--pi-jev-context/9f40314df01e39d4.png" width="100%" alt="kevinpita/pi-jev-context screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/anxkhn/JevPlaysPokemon">anxkhn/JevPlaysPokemon</a></b> — ⭐1 · HTML · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · HTML · GPL-3.0 · anxkhn

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev plays Generation 3 Pokémon via Showdown and a real FireRed ROM.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/anxkhn--jevplayspokemon/fc9ead060d7fa36a.png" width="100%" alt="anxkhn/JevPlaysPokemon screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Charlyhno-eng/jev-document-classification">Charlyhno-eng/jev-document-classification</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · Charlyhno-eng

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/charlyhno-eng--jev-document-classification/113bcf66f1648122.png" width="100%" alt="Charlyhno-eng/jev-document-classification screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/jev-review-action">fatwang2/jev-review-action</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · JavaScript · MIT · fatwang2

##### Daten

Stars **1** · Forks 0 · Offene Issues 2 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.

</details>

<details>
<summary><b><a href="https://github.com/lbotinelly/jev-little-airways">lbotinelly/jev-little-airways</a></b> — ⭐1 · HTML · inferred · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · HTML · MIT · lbotinelly

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A show-and-tell capability study for Jev, TypeSafe's System One decision model.

</details>

<details>
<summary><b><a href="https://github.com/MumuTW/awesome-jev">MumuTW/awesome-jev</a></b> — ⭐1 · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · CC0-1.0 · MumuTW

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

快速看懂風格鮮明的 Jev：型別化決策的 System One，以及社群熱議的同類模型。

</details>

<details>
<summary><b><a href="https://github.com/rogeriochaves/jev-experiments">rogeriochaves/jev-experiments</a></b> — ⭐1 · Go · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Go · rogeriochaves

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/sontakey/awesome-jev">sontakey/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · NOASSERTION · sontakey

##### Daten

Stars **1** · Forks 1 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Unofficial list of insanely useful TypeSafe AI Jev / System One projects

</details>

<details>
<summary><b><a href="https://github.com/TanayPadar/gpt-vs-jev">TanayPadar/gpt-vs-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · TanayPadar

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Compare GPT generated language with JEV structured Noul decisions on the same input.

</details>

<details>
<summary><b><a href="https://github.com/TheBous/jev-flash-review">TheBous/jev-flash-review</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · TheBous

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/tylerjharden/harden-jev-decides">tylerjharden/harden-jev-decides</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · tylerjharden

##### Daten

Stars **1** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-joust">4esv/jev-joust</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · 4esv

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

TypeSafe Jev vs Jev in NES Joust, bring your own ROM

</details>

<details>
<summary><b><a href="https://github.com/aaazzam/jev">aaazzam/jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · aaazzam

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/AmoghCreator/Jev-ComputerUse">AmoghCreator/Jev-ComputerUse</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · AmoghCreator

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/aoi-yoneda/haikyuBattleJev">aoi-yoneda/haikyuBattleJev</a></b> — HTML · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · HTML · aoi-yoneda

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev (TypeSafe AI) が打者を判断する配球バトル野球シミュレーション — 9回制・パワプロ風

</details>

<details>
<summary><b><a href="https://github.com/AppitStudio/awesome-jev">AppitStudio/awesome-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · NOASSERTION · AppitStudio

##### Daten

Stars **0** · Forks 0 · Offene Issues 4 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Curated Jev resources and runnable examples for typed AI decisions.

</details>

<details>
<summary><b><a href="https://github.com/Argos1111/jev_local">Argos1111/jev_local</a></b> — inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Argos1111

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Replicating Jev with a local LLM

</details>

<details>
<summary><b><a href="https://github.com/CrowdLinker/JevPromptCoach">CrowdLinker/JevPromptCoach</a></b> — inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · CrowdLinker

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A prompt coach built using TypeSafe AI's Jev

</details>

<details>
<summary><b><a href="https://github.com/felixfisher/pi-jev-compaction">felixfisher/pi-jev-compaction</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · felixfisher

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Experimental Pi extension using TypeSafe Jev for auditable tool-history compaction

</details>

<details>
<summary><b><a href="https://github.com/golergka/jev">golergka/jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · golergka

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/gtwatts/pi-jev-typesafe">gtwatts/pi-jev-typesafe</a></b> — inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · gtwatts

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-mahjong-bench">hamakyo/jev-mahjong-bench</a></b> — inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · hamakyo

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/haydarsahin0/Jev">haydarsahin0/Jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · haydarsahin0

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/heaven-hm/jev-system-one">heaven-hm/jev-system-one</a></b> — inferred · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · heaven-hm

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

</details>

<details>
<summary><b><a href="https://github.com/KaushikKC/JevScope">KaushikKC/JevScope</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · KaushikKC

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kaushikkc--jevscope/b2221a397bfa54e2.png" width="100%" alt="KaushikKC/JevScope screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-master">kevin9327/jev-master</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · MIT · kevin9327

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Typed System One decisions with Jev: Choice + Score + Noul composed in code.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevin9327--jev-master/cbf05c4561269075.png" width="100%" alt="kevin9327/jev-master screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kspviswa/chakravyuha-jev">kspviswa/chakravyuha-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · JavaScript · MIT · kspviswa

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kspviswa--chakravyuha-jev/4dfa22d0de9f27c1.png" width="100%" alt="kspviswa/chakravyuha-jev screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/lalitsonawane/jev-one-system">lalitsonawane/jev-one-system</a></b> — inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · lalitsonawane

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/levente-horvath/jev-as-controller">levente-horvath/jev-as-controller</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · levente-horvath

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/levente-horvath/jev-as-controller/main/docs/img/survival.png" width="100%" alt="levente-horvath/jev-as-controller screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

<sub>Asset direkt aus dem Upstream-Repository verlinkt, da keine Lizenz zur Weiterverbreitung angegeben wurde.</sub>

</details>

<details>
<summary><b><a href="https://github.com/levente-horvath/jev-plays-wordle">levente-horvath/jev-plays-wordle</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · levente-horvath

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/LingXuanYin/jev-chat">LingXuanYin/jev-chat</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · NOASSERTION · LingXuanYin

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jev 聊天机：一个「只选不写」的聊天机——每个回复由逐词选择拼装，词典+分级索引+输入法式联想，由真实 Jev（TypeSafe System One）驱动。非官方实验，与 TypeSafe AI 无关联。

</details>

<details>
<summary><b><a href="https://github.com/lookfwd/jev-fact-checker">lookfwd/jev-fact-checker</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · lookfwd

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Uses Typesafe AI Jev to Provide A Tweet Fact Checker

</details>

<details>
<summary><b><a href="https://github.com/mattdyer/jev-chase">mattdyer/jev-chase</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · HTML · mattdyer

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/memorysaver/jev-atari-lab">memorysaver/jev-atari-lab</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · GPL-2.0 · memorysaver

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Challenge Atari with Jev: structured decisions, value questions, and replayable experiments

</details>

<details>
<summary><b><a href="https://github.com/Nachom3/jevTrader">Nachom3/jevTrader</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Rust · Nachom3

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

A High Frecuncy Trader made in Rust using Jev as a decision maker.

</details>

<details>
<summary><b><a href="https://github.com/nardinmarcus/pi-jev-typesafe">nardinmarcus/pi-jev-typesafe</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · nardinmarcus

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model discovery, and budget caps

</details>

<details>
<summary><b><a href="https://github.com/narulaskaran/jev-data-questions">narulaskaran/jev-data-questions</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · narulaskaran

##### Daten

Stars **0** · Forks 0 · Offene Issues 2 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/nourhelmi/pi-jev-compaction">nourhelmi/pi-jev-compaction</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · nourhelmi

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Automatic Jev context clearing for Pi. Keep the conversation, prune stale tool output, retrieve originals without rerunning commands.

</details>

<details>
<summary><b><a href="https://github.com/ochotzas/jev-park">ochotzas/jev-park</a></b> — inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · MIT · ochotzas

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/rolottr/x-jev-classifier">rolottr/x-jev-classifier</a></b> — JavaScript · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · JavaScript · AGPL-3.0 · rolottr

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Chrome extension that stamps every X post with a type badge — alpha, shitpost, AI slop, bait — judged by Jev from Typesafe

</details>

<details>
<summary><b><a href="https://github.com/sandeepvsk10/bigquery-jev-classifier-function">sandeepvsk10/bigquery-jev-classifier-function</a></b> — inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · sandeepvsk10

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/sandrotaje/pi-jev-concise">sandrotaje/pi-jev-concise</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · sandrotaje

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/sub-surface/jev">sub-surface/jev</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · MIT · sub-surface

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/TKY-27/JevSlop">TKY-27/JevSlop</a></b> — TypeScript · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · MIT · TKY-27

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Jevによるnote記事のAI Slop判定サイト

</details>

<details>
<summary><b><a href="https://github.com/TonyP-MR/jev-curation-engine">TonyP-MR/jev-curation-engine</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · TonyP-MR

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions with existing LLM audit results.

</details>

<details>
<summary><b><a href="https://github.com/Tsagaanbayr1/jev-tetris">Tsagaanbayr1/jev-tetris</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · JavaScript · Tsagaanbayr1

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Real-time Tetris versus Jev, a TypeSafe decision model — spins, garbage, B2B chains, and decisions prefetched a piece ahead

</details>

<details>
<summary><b><a href="https://github.com/vafaei-ar/jev-scientific-development">vafaei-ar/jev-scientific-development</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · GPL-3.0 · vafaei-ar

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/Vicente-MD/jev-match">Vicente-MD/jev-match</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · TypeScript · Vicente-MD

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Chrome extension using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/yogi-miraje/jev-lab">yogi-miraje/jev-lab</a></b> — Python · inferred · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `inferred` · Python · yogi-miraje

##### Daten

Stars **0** · Forks 0 · Offene Issues 0 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-19

##### Zusammenfassung

Im Upstream wurde keine Beschreibung veröffentlicht.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/typesafe-adblock">realZachi/typesafe-adblock</a></b> — ⭐49 · JavaScript · unverified · 1 天 · ⭐+1</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `unverified` · JavaScript · MIT · realZachi

##### Daten

Stars **49** (+1) · Forks 3 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.

</details>

<details>
<summary><b><a href="https://github.com/razorback16/openjev">razorback16/openjev</a></b> — ⭐27 · Python · unverified · 0 天 · ⭐+10</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `unverified` · Python · Apache-2.0 · razorback16

##### Daten

Stars **27** (+10) · Forks 4 · Offene Issues 1 · Erstellt 2026-09-18 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Open, Jev-compatible System One decision server on DiffusionGemma

</details>

<details>
<summary><b><a href="https://github.com/devanshbatham/commit-miner">devanshbatham/commit-miner</a></b> — ⭐21 · Rust · unverified · 1 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `unverified` · Rust · devanshbatham

##### Daten

Stars **21** · Forks 5 · Offene Issues 0 · Erstellt 2026-09-17 · Letzter Push 2026-09-17 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.

</details>

<details>
<summary><b><a href="https://github.com/phyous/tsai-sc">phyous/tsai-sc</a></b> — ⭐15 · Python · unverified · 2 天 · ⭐+2</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `unverified` · Python · MIT · phyous

##### Daten

Stars **15** (+2) · Forks 1 · Offene Issues 0 · Erstellt 2026-09-16 · Letzter Push 2026-09-16 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.

<table><tr><th align="center" width="50%">Bild</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/phyous--tsai-sc/f48a030ae92fb1fe.png" width="100%" alt="phyous/tsai-sc screenshot"></td>
<td align="center" valign="top"><sub>keine Medien veröffentlicht</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andysc/IBM-Q-System-One-3D-model">andysc/IBM-Q-System-One-3D-model</a></b> — ⭐12 · OpenSCAD · unverified · 2688 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `unverified` · OpenSCAD · andysc

##### Daten

Stars **12** · Forks 4 · Offene Issues 1 · Erstellt 2019-03-16 · Letzter Push 2019-05-10 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

3D-printed model of IBM Q System One

</details>

<details>
<summary><b><a href="https://github.com/zhengxuyu/litjev">zhengxuyu/litjev</a></b> — ⭐4 · Python · unverified · 0 天</summary>

##### Basisfakten

`Artikel, Diskussionen und verwandte Listen` · Community · `unverified` · Python · Apache-2.0 · zhengxuyu

##### Daten

Stars **4** · Forks 1 · Offene Issues 3 · Erstellt 2026-09-17 · Letzter Push 2026-09-18 · Erstmals gelistet 2026-09-18

##### Zusammenfassung

Turn any off-the-shelf LLM into a Jev -like decision layer

</details>

<a id="projects-by-implementation-language"></a>

## Projekte nach Implementierungssprache

Das Ökosystem konzentriert sich auf Python und TypeScript, doch typisierte Clients tauchen weiterhin in anderen Sprachen auf. Diese Tabelle wird aus den Einträgen selbst erzeugt.

| Sprache    | Einträge | Beispiele                                                                                                      |
| ---------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| Python     | 142      | `typesafe-ai/system-one-adapter-python`, `typesafe-ai/typesafe-sdk-python`, `MrJev/awesome-jev`                |
| TypeScript | 124      | `typesafe-ai/typesafe-sdk-js`, `AntonioCoppe/jev-harness`, `opaielsheikh/typesafe-migration-guard`             |
| JavaScript | 58       | `ziyu/sytem-one-sdk`, `Ying-Kai-Liao/jev-browser`, `arunav25/jev-mcp`                                          |
| Go         | 14       | `RadixILS-Dev/typesafe-sdk-go`, `anilsenay/jev`, `Gaurav-Gosain/jev-go`                                        |
| Rust       | 13       | `AkashPriyadarshii/jev-curate`, `AkashPriyadarshii/jev-seo`, `AkashPriyadarshii/jev-scout`                     |
| HTML       | 10       | `typesafe-ai/typesafe-ai.github.io`, `yzfly/awesome-jev-zh`, `vinilana/jev-eval-agent`                         |
| Shell      | 4        | `realZachi/pg-jev`, `ajshedivy/ibmi-jev`, `wotai-dev/typesafe-jev-tools`                                       |
| Elixir     | 3        | `nshkrdotcom/typesafe_sdk`, `typesend/typesafe_ai`, `dannote/jev`                                              |
| PHP        | 3        | `Butochnikov/laravel-typesafe-jev`, `mzainzulifqar/jev-php-sdk`, `soderlind/ai-provider-for-jev`               |
| Ruby       | 3        | `javiergradiche/ruby_llm-providers-typesafe`, `obie/ruby_decision_model`, `robzolkos/omarchy-issue-classifier` |
| C          | 2        | `mgaitan/sqlite-jev`, `giuliosmall/pg_typesafe`                                                                |
| Java       | 2        | `Premo-Cloud/typesafe-sdk-java`, `Olti1947/jev-java`                                                           |
| Jupyter    | 2        | `jexp/neo4jev`, `bitnovus/jev-spam-eval`                                                                       |
| C#         | 1        | `saibimajdi/typesafeai-dotnet-sdk`                                                                             |
| CSS        | 1        | `AbdelStark/awesome-typesafe`                                                                                  |
| Dart       | 1        | `Bud-ro/jev-demos`                                                                                             |
| Haskell    | 1        | `inanna-malick/jev-dsl`                                                                                        |
| Kotlin     | 1        | `ufec/jev-block-android-ad`                                                                                    |
| Lex        | 1        | `alpibrusl/lex-judge`                                                                                          |
| OCaml      | 1        | `jonesmelton/verdict`                                                                                          |
| OpenSCAD   | 1        | `andysc/IBM-Q-System-One-3D-model`                                                                             |
| PowerShell | 1        | `omni-/ask-jev`                                                                                                |
| R          | 1        | `simxnherrera/jevr`                                                                                            |
| Swift      | 1        | `chris-wozniczek/jev-voice-control`                                                                            |
| TeX        | 1        | `dnakhoa/jev-deferred-crispification`                                                                          |

<sub>Nur Einträge, die eine Sprache angeben, werden gezählt. Infrastruktur-, Dokumentations- und Diskussionseinträge sind von dieser Tabelle ausgenommen.</sub>

## Wie diese Liste aktuell bleibt

Niemand bearbeitet den Text dieses README von Hand. Das Repository führt nach Zeitplan eine Pipeline mit fünf Stufen aus und committet nur, wenn sich tatsächlich etwas geändert hat.

<img src="assets/readme/pipeline.svg" width="100%" alt="Wie diese Liste aktuell bleibt">

|             |                                                                                                                                                                                                                                                                                                                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **collect** | GitHub-Suche über eine Query-Matrix, die offizielle Organisation, die GitHub-Code-Suche, Hacker News und den Hugging Face-Hub.                                                                                                                                                                                                    |
| **curate**  | deterministisch und ohne LLM, sodass zwei aufeinanderfolgende Läufe mit derselben Eingabe byte-identische Ausgaben erzeugen. Eine Zwei-Signal-Regel entscheidet über die Relevanz; Namenskollisionen (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD und ähnliche) werden über eine ausdrückliche, prüfbare Liste ausgeschlossen. |
| **media**   | sammelt die eigenen Screenshots und Bildschirmaufzeichnungen jedes Projekts. Assets werden nur dann in dieses Repository kopiert, wenn das Projekt eine weiterverbreitungsfreundliche Lizenz angibt; andernfalls wird die Upstream-URL direkt verlinkt und die Karte sagt das auch.                                               |
| **render**  | erzeugt alle Sprachausgaben aus einer einzigen Vorlage, sodass die zwanzig READMEs in ihrer Struktur niemals auseinanderlaufen können.                                                                                                                                                                                            |
| **audit**   | lässt den Build fehlschlagen, wenn einem Eintrag eine URL fehlt, wenn ein Link tot ist, wenn zwei Einträge dieselbe URL doppeln oder wenn ein README von seiner erzeugten Form abweicht.                                                                                                                                          |

## Mitwirken

Korrekturen sind willkommen und der schnellste Weg, diese Liste zu verbessern. Öffnen Sie ein Issue oder einen Pull Request, wenn ein Eintrag falsch einsortiert oder falsch eingestuft ist oder wenn ein Projekt zu Unrecht als Namenskollision ausgeschlossen wurde — gerade in dieser letzten Kategorie liegen automatisierte Filter am häufigsten falsch. Ergänzungen gelingen am besten, indem Sie eine Quelle in `scripts/collect.py` hinzufügen, statt das README zu bearbeiten, denn das README wird bei jedem Durchlauf neu erzeugt.

---

<sub>Unabhängiges Community-Projekt. Nicht mit TypeSafe AI verbunden, von ihr unterstützt oder geprüft. Produktverhalten, Preise, Limits und Modell-Aliase ändern sich ohne Ankündigung; prüfen Sie alles Tragende anhand der offiziellen Dokumentation. Assets bleiben Eigentum ihrer Upstream-Projekte und werden nur wiedergegeben, wo eine Lizenz es erlaubt.</sub>

<sub>Erzeugt von · `render.py` · 2026-09-19T03:55:37+08:00</sub>
