<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>L'indice Jev con valutazione delle prove, che si ricostruisce ogni due ore.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-430-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <b>Italiano</b> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indice live** · Ultima sincronizzazione: `2026-09-19T01:47:12+08:00` (UTC+8)
> · Voci: **430** · Nuove in questo ciclo: **57** · Linguaggi di implementazione: **24**

<sub>Ogni voce qui sotto è stata raccolta, filtrata e ricontrollata dalla pipeline di questo repository. Numeri e timestamp provengono dalle fonti, non da un'istantanea scritta a mano.</sub>

## Indice

- [Che cos'è Jev?](#che-cosè-jev)
- [Come vengono classificate le voci](#come-vengono-classificate-le-voci)
- [SDK ufficiali e strumenti per sviluppatori](#sdk-ufficiali-e-strumenti-per-sviluppatori) — **5**
- [Client, SDK e adattatori della comunità](#client-sdk-e-adattatori-della-comunità) — **74**
- [Strumenti per agenti: MCP, hook, gate e agenti di coding](#strumenti-per-agenti-mcp-hook-gate-e-agenti-di-coding) — **128**
- [Instradamento, guardrail e approvazioni](#instradamento-guardrail-e-approvazioni) — **38**
- [Valutazione, calibrazione e benchmark](#valutazione-calibrazione-e-benchmark) — **32**
- [Riproduzioni aperte, pesi e ricerca sull'architettura](#riproduzioni-aperte-pesi-e-ricerca-sullarchitettura) — **14**
- [Applicazioni, giochi, robotica e demo interattive](#applicazioni-giochi-robotica-e-demo-interattive) — **38**
- [Articoli, discussioni e liste affini](#articoli-discussioni-e-liste-affini) — **101**
- [Progetti per linguaggio di implementazione](#progetti-per-linguaggio-di-implementazione)
- [Come questo elenco resta aggiornato](#come-questo-elenco-resta-aggiornato)

## Che cos&#x27;è Jev?

Jev è il primo **modello System One** di TypeSafe AI. Non scrive prosa. Prende uno stato più domande il cui spazio di risposta definite in anticipo, e restituisce valori tipizzati con distribuzioni di probabilità su cui il vostro codice può diramarsi.

|                 |                                                                                                                                                                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Forma**       | `state + typed questions` → `constrained answers + probabilities` → `your code`                                                                                                                                                                    |
| **Primitive**   | `Choice` (scegli una tra ≤255 opzioni), `Score` (una rubrica 2–10), `Noul` (un sì/no probabilistico)                                                                                                                                               |
| **Endpoint**    | `POST https://api.typesafe.ai/v1/systemone`, modello `jev-1.13.0` / alias `jev-latest`                                                                                                                                                             |
| **Adatto a**    | instradamento, triage, scoring, moderazione, verifica e gate a bassa latenza dentro un flusso di lavoro delimitato                                                                                                                                 |
| **Limiti noti** | il conteggio non è affidabile, l'indirezione a più livelli è debole, e il materiale ufficiale nomina nove classi di irregolarità. Un output valido rispetto allo schema non è la stessa cosa di una decisione corretta: calibrate sui vostri dati. |

## Come vengono classificate le voci

Quasi tutti gli elenchi in questo spazio affermano l'inclusione. Questo dice quanto ha effettivamente verificato, e poi vi lascia filtrare di conseguenza.

| Grado        | Che cosa significa                                                                                                                                                                      |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `official`   | Pubblicato da TypeSafe AI stessa.                                                                                                                                                       |
| `observed`   | Un artefatto pubblico che si può aprire e leggere: codice sorgente reale, configurazione reale, oppure una dichiarazione esplicita di TypeSafe/Jev nel nome o nei topic del repository. |
| `inferred`   | Corrisponde per un segnale ambiguo più un vocabolario di conferma, ma non è ancora stato letto riga per riga.                                                                           |
| `unverified` | Sembra correlato, nulla è confermato in modo indipendente. Inserito solo per scoperta.                                                                                                  |

<a id="official-sdk"></a>

## SDK ufficiali e strumenti per sviluppatori

Tutto ciò che è pubblicato da TypeSafe stessa. Inizia da qui.

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐216 · official · 6 天 · ⭐+20</summary>

##### Dati essenziali

`SDK ufficiali e strumenti per sviluppatori` · Ufficiale · `official` · MIT · typesafe-ai

##### Dati

Stelle **216** (+20) · Fork 10 · Issue aperte 0 · Creato 2026-08-24 · Ultimo push 2026-09-12 · Prima apparizione 2026-09-18

##### Descrizione

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐115 · TypeScript · official · 2 天 · ⭐+3</summary>

##### Dati essenziali

`SDK ufficiali e strumenti per sviluppatori` · Ufficiale · `official` · TypeScript · MIT · typesafe-ai

##### Dati

Stelle **115** (+3) · Fork 8 · Issue aperte 6 · Creato 2026-09-04 · Ultimo push 2026-09-15 · Prima apparizione 2026-09-18

##### Descrizione

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐111 · Python · official · 0 天 · ⭐+5</summary>

##### Dati essenziali

`SDK ufficiali e strumenti per sviluppatori` · Ufficiale · `official` · Python · MIT · typesafe-ai

##### Dati

Stelle **111** (+5) · Fork 11 · Issue aperte 0 · Creato 2026-08-08 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>Trovato in uso nel codice: `README.md`, `src/system_one_adapter/__init__.py`, `src/system_one_adapter/_response.py`, `src/system_one_adapter/_utils/error_handling.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐80 · Python · official · 0 天 · ⭐+2</summary>

##### Dati essenziali

`SDK ufficiali e strumenti per sviluppatori` · Ufficiale · `official` · Python · MIT · typesafe-ai

##### Dati

Stelle **80** (+2) · Fork 7 · Issue aperte 2 · Creato 2026-09-04 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>Trovato in uso nel codice: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 106 天</summary>

##### Dati essenziali

`SDK ufficiali e strumenti per sviluppatori` · Ufficiale · `official` · HTML · typesafe-ai

##### Dati

Stelle **1** · Fork 1 · Issue aperte 1 · Creato 2024-05-28 · Ultimo push 2026-06-04 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<a id="community-sdk"></a>

## Client, SDK e adattatori della comunità

Client tipizzati per l'endpoint System One, in tutte le lingue a cui la comunità è arrivata.

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐17 · Jupyter · observed · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · Jupyter · MIT · jexp

##### Dati

Stelle **17** (+1) · Fork 3 · Issue aperte 1 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · TypeScript · MIT · AntonioCoppe

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · Python · CC0-1.0 · MrJev

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐2 · Elixir · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · Elixir · MIT · nshkrdotcom

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · TypeScript · opaielsheikh

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — ⭐2 · Java · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · Java · MIT · Premo-Cloud

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · Rust · MIT · AkashPriyadarshii

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · JavaScript · MIT · ziyu

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/ivorpad/skillranker">ivorpad/skillranker</a></b> — observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · NOASSERTION · ivorpad

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · Ruby · MIT · javiergradiche

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/jonesmelton/verdict">jonesmelton/verdict</a></b> — OCaml · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · OCaml · MIT · jonesmelton

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

ocaml sdk for typesafe.ai's jev model

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · TypeScript · MIT · nu-sync

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/RadixILS-Dev/typesafe-sdk-go">RadixILS-Dev/typesafe-sdk-go</a></b> — Go · observed · 0 天 · **NEW**</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · Go · MIT · RadixILS-Dev

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

A typesafe.ai client written in golang

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · Elixir · MIT · typesend

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — Python · observed · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `observed` · Python · xingwudao

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐145 · Python · inferred · 0 天 · ⭐+12</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · NOASSERTION · realZachi

##### Dati

Stelle **145** (+12) · Fork 6 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐27 · TypeScript · inferred · 0 天 · ⭐+5</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · nidhi-singh02

##### Dati

Stelle **27** (+5) · Fork 1 · Issue aperte 1 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">Guarda su img.youtube.com</a> · la riproduzione si apre sul sito ospite; GitHub non può incorporarla inline</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gamesonrblx/Jevbridge">gamesonrblx/Jevbridge</a></b> — ⭐13 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · gamesonrblx

##### Dati

Stelle **13** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

> Bridges the typed-decision layer to the agent protocols other tools already speak.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gamesonrblx--jevbridge/772995670b3e42e9.png" width="100%" alt="gamesonrblx/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐12 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · shiftynick

##### Dati

Stelle **12** · Fork 1 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐11 · Elixir · inferred · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Elixir · MIT · dannote

##### Dati

Stelle **11** (+1) · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐9 · JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · JavaScript · MIT · Ying-Kai-Liao

##### Dati

Stelle **9** · Fork 3 · Issue aperte 3 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐6 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · AboveColin

##### Dati

Stelle **6** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Home Assistant integration for TypeSafe Jev. Ask a question about your house and get a probability, a choice or a score as an entity.

</details>

<details>
<summary><b><a href="https://github.com/arunav25/jev-mcp">arunav25/jev-mcp</a></b> — ⭐5 · JavaScript · inferred · 1 天 · ⭐+2</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · JavaScript · MIT · arunav25

##### Dati

Stelle **5** (+2) · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.

</details>

<details>
<summary><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">saibimajdi/typesafeai-dotnet-sdk</a></b> — ⭐5 · C# · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · C# · MIT · saibimajdi

##### Dati

Stelle **5** · Fork 0 · Issue aperte 1 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/sharziki/semdecide">sharziki/semdecide</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · sharziki

##### Dati

Stelle **5** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.

</details>

<details>
<summary><b><a href="https://github.com/docxology/daf-jev">docxology/daf-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · docxology

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill

</details>

<details>
<summary><b><a href="https://github.com/frostney/clean-code-review">frostney/clean-code-review</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · frostney

##### Dati

Stelle **3** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/frostney--clean-code-review/7d8a8de446e1c27b.png" width="100%" alt="frostney/clean-code-review screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/keltokhy/jgrep">keltokhy/jgrep</a></b> — ⭐3 · Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · keltokhy

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.

</details>

<details>
<summary><b><a href="https://github.com/Olti1947/jev-java">Olti1947/jev-java</a></b> — ⭐3 · Java · inferred · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Java · Olti1947

##### Dati

Stelle **3** (+1) · Fork 1 · Issue aperte 7 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Idiomatic Java SDK for TypeSafe AI Jev System One decision engine

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-seo">AkashPriyadarshii/jev-seo</a></b> — ⭐2 · Rust · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Rust · AkashPriyadarshii

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One

</details>

<details>
<summary><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Butochnikov/laravel-typesafe-jev</a></b> — ⭐2 · PHP · inferred · 1 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · PHP · MIT · Butochnikov

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes.

</details>

<details>
<summary><b><a href="https://github.com/tontoko/jev-browser">tontoko/jev-browser</a></b> — ⭐2 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · JavaScript · Apache-2.0 · tontoko

##### Dati

Stelle **2** (+1) · Fork 0 · Issue aperte 3 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.

</details>

<details>
<summary><b><a href="https://github.com/tumf/jev-cli">tumf/jev-cli</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · tumf

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Small dependency-free CLI for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/yzfly/awesome-jev-zh">yzfly/awesome-jev-zh</a></b> — ⭐2 · HTML · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · HTML · CC0-1.0 · yzfly

##### Dati

Stelle **2** · Fork 1 · Issue aperte 1 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/jevclient">AboveColin/jevclient</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · AboveColin

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-scout">AkashPriyadarshii/jev-scout</a></b> — ⭐1 · Rust · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Rust · MIT · AkashPriyadarshii

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring

</details>

<details>
<summary><b><a href="https://github.com/burnigtm/jev-mcp">burnigtm/jev-mcp</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · burnigtm

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client

</details>

<details>
<summary><b><a href="https://github.com/felpsdev/jev-classifier">felpsdev/jev-classifier</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · felpsdev

##### Dati

Stelle **1** · Fork 1 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/felpsdev--jev-classifier/d753de26b0e6c7b6.webp" width="100%" alt="felpsdev/jev-classifier screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-go">Gaurav-Gosain/jev-go</a></b> — ⭐1 · Go · inferred · 2 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Go · MIT · Gaurav-Gosain

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/himomohi/aside-jev">himomohi/aside-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · himomohi

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.

</details>

<details>
<summary><b><a href="https://github.com/jtsang4/jev-cli">jtsang4/jev-cli</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · jtsang4

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

CLI for TypeSafe AI's Jev evaluation model — typed questions in, structured JSON answers out

</details>

<details>
<summary><b><a href="https://github.com/Nasrallah-AL/jev-cli">Nasrallah-AL/jev-cli</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · Nasrallah-AL

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Command-line tool for TypeSafe's Jev AI model

</details>

<details>
<summary><b><a href="https://github.com/rhighs/jev-code">rhighs/jev-code</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · rhighs

##### Dati

Stelle **1** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/assets/jev-code-logo.png" width="100%" alt="rhighs/jev-code screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/StefanoITA/ts-jev-cost-calculator">StefanoITA/ts-jev-cost-calculator</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · StefanoITA

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe.

</details>

<details>
<summary><b><a href="https://github.com/Stumble/jev-go">Stumble/jev-go</a></b> — ⭐1 · Go · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Go · MIT · Stumble

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Community Go SDK for TypeSafe AI Jev / System One

</details>

<details>
<summary><b><a href="https://github.com/zhirschtritt/typesafe-go">zhirschtritt/typesafe-go</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Go · MIT · zhirschtritt

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Idiomatic Go SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-git">AkashPriyadarshii/jev-git</a></b> — Rust · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Rust · MIT · AkashPriyadarshii

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">AkashPriyadarshii/jev-superpowers</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · JavaScript · MIT · AkashPriyadarshii

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions

</details>

<details>
<summary><b><a href="https://github.com/anilsenay/jev">anilsenay/jev</a></b> — Go · inferred · 1 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Go · MIT · anilsenay

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Unofficial Go client for TypeSafe's System One API  and its model, Jev.

</details>

<details>
<summary><b><a href="https://github.com/aryrabelo/jev-accept">aryrabelo/jev-accept</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · aryrabelo

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

One-request acceptance triage for GitHub PRs: Jev judges whether a PR delivers its issue's intent, from the issue->epic chain. Local CLI + GitHub Action, same contract, ~$0.0001 per PR.

</details>

<details>
<summary><b><a href="https://github.com/brnyxx/jev-ra">brnyxx/jev-ra</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · brnyxx

##### Dati

Stelle **0** · Fork 0 · Issue aperte 2 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7592fce4641d10.png" width="100%" alt="brnyxx/jev-ra screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7ddcd1053825a2.gif" width="100%" alt="brnyxx/jev-ra animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/david1gp/jev">david1gp/jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · david1gp

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Result-based TypeSafe System One client library and jev command-line interface.

</details>

<details>
<summary><b><a href="https://github.com/ddfeyes/jev-mode">ddfeyes/jev-mode</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · MIT · ddfeyes

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no deps, MIT.

</details>

<details>
<summary><b><a href="https://github.com/ibrahemid/git-jev-stage">ibrahemid/git-jev-stage</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · ibrahemid

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Stage the git hunks that match a sentence. Exact patch, preview first, staging only, decided per hunk by Jev.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/krw82/jev-playwright-mcp">krw82/jev-playwright-mcp</a></b> — TypeScript · inferred · 1 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · krw82

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.

</details>

<details>
<summary><b><a href="https://github.com/kunobi-ninja/kunobi-jev">kunobi-ninja/kunobi-jev</a></b> — Rust · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Rust · Apache-2.0 · kunobi-ninja

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Rust client for the TypeSafe System One API (Jev)

</details>

<details>
<summary><b><a href="https://github.com/lhotwll217/jev-cli">lhotwll217/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · lhotwll217

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

JSON-in, typed-decisions-out CLI for the TypeSafe System One API

</details>

<details>
<summary><b><a href="https://github.com/manojlds/jev-review">manojlds/jev-review</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · manojlds

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Standalone TypeSafe Jev code-review CLI: typed decisions over a local git diff.

</details>

<details>
<summary><b><a href="https://github.com/mhmdkzr/jev">mhmdkzr/jev</a></b> — Go · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Go · MIT · mhmdkzr

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

An unofficial Go client for TypeSafe's System One Jev model

</details>

<details>
<summary><b><a href="https://github.com/model-clis/jev">model-clis/jev</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Rust · MIT · model-clis

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Typed judgment CLI for the Jev model (TypeSafe System One): state + questions in, calibrated answers and exit codes out

</details>

<details>
<summary><b><a href="https://github.com/mzainzulifqar/jev-php-sdk">mzainzulifqar/jev-php-sdk</a></b> — PHP · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · PHP · MIT · mzainzulifqar

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

PHP SDK for TypeSafe's Jev: send text and typed questions, get typed answers with calibrated confidence. PHP 8.1+, works with any PSR-18 client, Laravel 8–13.

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-go">nekowasabi/jev-routing-go</a></b> — Go · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Go · MIT · nekowasabi

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.

</details>

<details>
<summary><b><a href="https://github.com/ojusave/beat-jev">ojusave/beat-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · TypeScript · MIT · ojusave

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

A penalty shootout powered by Render Workflows, TypeSafe Jev, and Render Postgres. Python and TypeScript examples.

</details>

<details>
<summary><b><a href="https://github.com/okooo5km/jev">okooo5km/jev</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · Apache-2.0 · okooo5km

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Typed decisions from the shell: a stdlib-Python CLI and Agent Skill for TypeSafe Jev on OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch mode.

</details>

<details>
<summary><b><a href="https://github.com/phuthuycoding/jev-audit">phuthuycoding/jev-audit</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · phuthuycoding

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

AI-powered pre-commit auditor backed by TypeSafe System One (Jev) — blocks secrets, vulns & low-quality code in ~300ms. 79-case test corpus at 100% accuracy.

</details>

<details>
<summary><b><a href="https://github.com/SAGAR-TAMANG/sarvam-jev">SAGAR-TAMANG/sarvam-jev</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · Python · SAGAR-TAMANG

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Generation-free typed decisions on Indic LLMs. An open Jev-style inference engine on sarvam-1: constrained logit readout instead of autoregressive JSON. Runs client-side in the browser.

</details>

<details>
<summary><b><a href="https://github.com/shanginn/jev-php">shanginn/jev-php</a></b> — PHP · inferred · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `inferred` · PHP · MIT · shanginn

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Type-safe PHP 8.5 SDK for JEV decisions on OpenRouter: choices, scores, probabilities and typed DTOs.

</details>

<details>
<summary><b><a href="https://github.com/pithings/advocaat">pithings/advocaat</a></b> — ⭐66 · TypeScript · unverified · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `unverified` · TypeScript · MIT · pithings

##### Dati

Stelle **66** (+1) · Fork 1 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/Tangerg/typesafe-sdk-go">Tangerg/typesafe-sdk-go</a></b> — ⭐7 · Go · unverified · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `unverified` · Go · MIT · Tangerg

##### Dati

Stelle **7** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Go SDK for the TypeSafe AI API — typed questions in, probability distributions out.

</details>

<details>
<summary><b><a href="https://github.com/Brainwires/jevwire">Brainwires/jevwire</a></b> — ⭐5 · TypeScript · unverified · 0 天 · ⭐+2</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `unverified` · TypeScript · MIT · Brainwires

##### Dati

Stelle **5** (+2) · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)

</details>

<details>
<summary><b><a href="https://github.com/giuliosmall/pg_typesafe">giuliosmall/pg_typesafe</a></b> — ⭐5 · C · unverified · 0 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `unverified` · C · MIT · giuliosmall

##### Dati

Stelle **5** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/typesafe-cli">y0usaf/typesafe-cli</a></b> — ⭐4 · TypeScript · unverified · 2 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `unverified` · TypeScript · MIT · y0usaf

##### Dati

Stelle **4** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose

</details>

<details>
<summary><b><a href="https://github.com/geilt/typesafe-cli">geilt/typesafe-cli</a></b> — ⭐3 · Python · unverified · 1 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `unverified` · Python · geilt

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.

</details>

<details>
<summary><b><a href="https://github.com/gilljon/typesafe-ai-rs">gilljon/typesafe-ai-rs</a></b> — ⭐3 · Rust · unverified · 1 天</summary>

##### Dati essenziali

`Client, SDK e adattatori della comunità` · Comunità · `unverified` · Rust · MIT · gilljon

##### Dati

Stelle **3** · Fork 0 · Issue aperte 1 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Independent async and blocking Rust SDK for the TypeSafe AI System One API

</details>

<a id="agent-tooling"></a>

## Strumenti per agenti: MCP, hook, gate e agenti di coding

La categoria che cresce più in fretta: hook, server MCP e gate che mettono una decisione tipizzata davanti all'azione successiva di un agente.

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐2808 · TypeScript · observed · 0 天 · ⭐+196</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · TypeScript · MIT · tamaratran

##### Dati

Stelle **2808** (+196) · Fork 140 · Issue aperte 42 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>Trovato in uso nel codice: `src/request.ts`, `README.md`, `src/client.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐121 · JavaScript · inferred · 0 天 · ⭐+3</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · gargpratyush

##### Dati

Stelle **121** (+3) · Fork 5 · Issue aperte 4 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐29 · Python · inferred · 1 天 · ⭐+3</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · 0xNatoshi

##### Dati

Stelle **29** (+3) · Fork 3 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐86 · observed · 0 天 · ⭐+9</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · dbreunig

##### Dati

Stelle **86** (+9) · Fork 2 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐14 · Python · observed · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · Python · MIT · GhalebDweikat

##### Dati

Stelle **14** (+1) · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · Python · MIT · carlaiau

##### Dati

Stelle **7** · Fork 1 · Issue aperte 6 · Creato 2026-03-13 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · Python · MIT · jodan-alberts

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/rajdhakad9826/routeKit">rajdhakad9826/routeKit</a></b> — ⭐2 · TypeScript · observed · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · TypeScript · MIT · rajdhakad9826

##### Dati

Stelle **2** (+1) · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Agent-native LLM model router built with JEV by TypeSafe.ai. Dynamically selects the most suitable model based on task complexity, reasoning requirements, and tool usage.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · TypeScript · MIT · BYK

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · Python · MIT · 24601

##### Dati

Stelle **0** · Fork 0 · Issue aperte 1 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · TypeScript · CrowBe

##### Dati

Stelle **0** · Fork 0 · Issue aperte 1 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · TypeScript · MIT · gorock007

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/kraayenjon/awesome-jev">kraayenjon/awesome-jev</a></b> — observed · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · NOASSERTION · kraayenjon

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `observed` · Python · MIT · yousudip

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐253 · TypeScript · inferred · 1 天 · ⭐+16</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · devagrawal09

##### Dati

Stelle **253** (+16) · Fork 12 · Issue aperte 1 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐113 · TypeScript · inferred · 1 天 · ⭐+2</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · NiazMorshed2007

##### Dati

Stelle **113** (+2) · Fork 9 · Issue aperte 2 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-eval-agent">vinilana/jev-eval-agent</a></b> — ⭐80 · HTML · inferred · 1 天 · ⭐+1</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · HTML · vinilana

##### Dati

Stelle **80** (+1) · Fork 7 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-mcp">jkudish/jev-mcp</a></b> — ⭐71 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · jkudish

##### Dati

Stelle **71** (+4) · Fork 8 · Issue aperte 2 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Proof of concept MCP for Typesafe's new Jev AI model

> An early proof of concept for exposing Jev over MCP, which is how most non-Python toolchains reach it.

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐67 · JavaScript · inferred · 0 天 · ⭐+23</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · fatwang2

##### Dati

Stelle **67** (+23) · Fork 8 · Issue aperte 2 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/pi-jev">y0usaf/pi-jev</a></b> — ⭐65 · TypeScript · inferred · 1 天 · ⭐-40</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · y0usaf

##### Dati

Stelle **65** (-40) · Fork 3 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers

</details>

<details>
<summary><b><a href="https://github.com/RomanSlack/jev-drone">RomanSlack/jev-drone</a></b> — ⭐58 · Python · inferred · 1 天 · ⭐+1</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · RomanSlack

##### Dati

Stelle **58** (+1) · Fork 3 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/romanslack--jev-drone/b23ea2412f437970.png" width="100%" alt="RomanSlack/jev-drone screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wy-coliney/jev-browser-use">wy-coliney/jev-browser-use</a></b> — ⭐43 · JavaScript · inferred · 0 天 · ⭐+10</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · wy-coliney

##### Dati

Stelle **43** (+10) · Fork 2 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wy-coliney--jev-browser-use/581fbd89fe47c952.png" width="100%" alt="wy-coliney/jev-browser-use screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/ask-jev-skill">shantanugoel/ask-jev-skill</a></b> — ⭐26 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · shantanugoel

##### Dati

Stelle **26** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Skill for Hermes, and other agents, to ask typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/logicrw/awesome-jev-projects">logicrw/awesome-jev-projects</a></b> — ⭐25 · JavaScript · inferred · 0 天 · ⭐+5</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · logicrw

##### Dati

Stelle **25** (+5) · Fork 3 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync

</details>

<details>
<summary><b><a href="https://github.com/supercorp-ai/supercov">supercorp-ai/supercov</a></b> — ⭐25 · Rust · inferred · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Rust · MIT · supercorp-ai

##### Dati

Stelle **25** (+1) · Fork 1 · Issue aperte 0 · Creato 2026-08-23 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Code quality and coverage for coding agents

> Code quality and coverage verdicts produced as typed decisions rather than prose, so the result can gate a pipeline directly.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/supercorp-ai--supercov/063226e150cb8a6b.jpg" width="100%" alt="supercorp-ai/supercov screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/compozy/yoshi">compozy/yoshi</a></b> — ⭐10 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · compozy

##### Dati

Stelle **10** (+1) · Fork 1 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/compozy--yoshi/637d8588c227f4de.png" width="100%" alt="compozy/yoshi screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">jomatsu/pi-jev-auto-mode</a></b> — ⭐9 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · jomatsu

##### Dati

Stelle **9** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.

</details>

<details>
<summary><b><a href="https://github.com/blakestone-x/jev-mcp">blakestone-x/jev-mcp</a></b> — ⭐8 · Python · inferred · 1 天 · ⭐+1</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · blakestone-x

##### Dati

Stelle **8** (+1) · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer

</details>

<details>
<summary><b><a href="https://github.com/huntedman/JevLint">huntedman/JevLint</a></b> — ⭐7 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · huntedman

##### Dati

Stelle **7** (+2) · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.

</details>

<details>
<summary><b><a href="https://github.com/DanRWilloughby/snifftest">DanRWilloughby/snifftest</a></b> — ⭐6 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · DanRWilloughby

##### Dati

Stelle **6** (+2) · Fork 0 · Issue aperte 3 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">DECRUX9812/typesafe-skill-router</a></b> — ⭐6 · Python · inferred · 2 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · DECRUX9812

##### Dati

Stelle **6** · Fork 1 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-code">devagrawal09/jev-code</a></b> — ⭐6 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · devagrawal09

##### Dati

Stelle **6** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Bounded TypeSafe Jev workflows for coding agents.

</details>

<details>
<summary><b><a href="https://github.com/TheoOliveira/pi-jev">TheoOliveira/pi-jev</a></b> — ⭐6 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · TheoOliveira

##### Dati

Stelle **6** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">GodsBoy/jev-agent-skill-router</a></b> — ⭐5 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · GodsBoy

##### Dati

Stelle **5** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Typed, confidence-aware agent skill routing with TypeSafe Jev.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/godsboy--jev-agent-skill-router/c80293e37dcd4faf.png" width="100%" alt="GodsBoy/jev-agent-skill-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/inanna-malick/jev-dsl">inanna-malick/jev-dsl</a></b> — ⭐5 · Haskell · inferred · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Haskell · MIT · inanna-malick

##### Dati

Stelle **5** (+1) · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels

</details>

<details>
<summary><b><a href="https://github.com/kikoncuo/jevfire">kikoncuo/jevfire</a></b> — ⭐5 · JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · kikoncuo

##### Dati

Stelle **5** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

JEV-inspired parallel decisions for CUDA LLMs. One context, many decisions. vLLM API, game-agent examples, and reproducible benchmarks.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kikoncuo--jevfire/2d5597bbc6b2c82e.png" width="100%" alt="kikoncuo/jevfire screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/BillionsBobby/JevRouter">BillionsBobby/JevRouter</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · BillionsBobby

##### Dati

Stelle **4** · Fork 1 · Issue aperte 5 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A lightweight Jev-powered router for models, tools, and subagents

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/billionsbobby--jevrouter/f0e638219505d5da.png" width="100%" alt="BillionsBobby/JevRouter screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/GiesN/typesafe-jev-workflow">GiesN/typesafe-jev-workflow</a></b> — ⭐4 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · GiesN

##### Dati

Stelle **4** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/anandi1989/awesome-jev-usecases">anandi1989/awesome-jev-usecases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · MIT · anandi1989

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results

</details>

<details>
<summary><b><a href="https://github.com/anpicasso/hermes-jev-approvals">anpicasso/hermes-jev-approvals</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · anpicasso

##### Dati

Stelle **3** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only.

</details>

<details>
<summary><b><a href="https://github.com/SeeAPI/awesome-jev-use-cases">SeeAPI/awesome-jev-use-cases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · CC-BY-4.0 · SeeAPI

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.

</details>

<details>
<summary><b><a href="https://github.com/zhuyansen/jev-search-rerank-eval">zhuyansen/jev-search-rerank-eval</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · zhuyansen

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Does a TypeSafe Jev rerank beat embedding search? Graded relevance eval (9,831 pairs, 164 zh/en queries) over the Agent Skills Hub catalog, with the judge-circularity bias measured.

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-shield">caiovicentino/jev-shield</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · caiovicentino

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check.

</details>

<details>
<summary><b><a href="https://github.com/doeixd/jev-pref">doeixd/jev-pref</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · doeixd

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/jev-judgment">HyunjunJeon/jev-judgment</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · HyunjunJeon

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Agent Skill: send closed coding-agent judgments to TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/molis-ai/jev-workbench">molis-ai/jev-workbench</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · molis-ai

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/molis-ai--jev-workbench/00f61d8403a941cd.png" width="100%" alt="molis-ai/jev-workbench screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MongLong0214/jev-gate">MongLong0214/jev-gate</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MongLong0214

##### Dati

Stelle **2** · Fork 0 · Issue aperte 5 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.

</details>

<details>
<summary><b><a href="https://github.com/ranjan2829/AskJev">ranjan2829/AskJev</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · ranjan2829

##### Dati

Stelle **2** · Fork 2 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-mcp">rashedInt32/jev-mcp</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · rashedInt32

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/samtay32/jev-system-architect">samtay32/jev-system-architect</a></b> — ⭐2 · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · MIT · samtay32

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives.

</details>

<details>
<summary><b><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher">abhishekashokvkumar/jev-mcp-dispatcher</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · abhishekashokvkumar

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Natural-language MCP tool dispatcher powered entirely by TypeSafe's Jev — no general-purpose LLM. Discovers a simple MCP server's tool signatures at runtime and uses Jev's typed primitives (Choice/Noul) to pick the right tool and extract its arguments straight out of the sentence.

</details>

<details>
<summary><b><a href="https://github.com/bestagentkits/jev-skillful">bestagentkits/jev-skillful</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · bestagentkits

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-starter">hamakyo/jev-starter</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · hamakyo

##### Dati

Stelle **1** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-model-router-demo">jcpsimmons/jev-model-router-demo</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · jcpsimmons

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

</details>

<details>
<summary><b><a href="https://github.com/omni-/ask-jev">omni-/ask-jev</a></b> — ⭐1 · PowerShell · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · PowerShell · MIT · omni-

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions.

</details>

<details>
<summary><b><a href="https://github.com/poponline63/hermes-jev-north-star">poponline63/hermes-jev-north-star</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · poponline63

##### Dati

Stelle **1** · Fork 1 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven.

</details>

<details>
<summary><b><a href="https://github.com/QuentinDanblon/pi-fast-jev-compaction">QuentinDanblon/pi-fast-jev-compaction</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · NOASSERTION · QuentinDanblon

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Verbatim context pruning for the pi coding agent, scored by TypeSafe Jev: stale tool calls and results are dropped or truncated, everything kept stays verbatim.

</details>

<details>
<summary><b><a href="https://github.com/Ravinder82/jev-flash-router">Ravinder82/jev-flash-router</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · Ravinder82

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code

</details>

<details>
<summary><b><a href="https://github.com/rthomas24/jev-realtime-trading">rthomas24/jev-realtime-trading</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · rthomas24

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rthomas24--jev-realtime-trading/f27df5cca6b8e2cf.png" width="100%" alt="rthomas24/jev-realtime-trading screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/codex-jev-compaction">Wang-auspicious/codex-jev-compaction</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · Wang-auspicious

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills.

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/pi-jev-compaction">Wang-auspicious/pi-jev-compaction</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · Wang-auspicious

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev-powered context compaction for Pi. Keep critical instructions and tool history, prune the noise, and fall back gracefully.

</details>

<details>
<summary><b><a href="https://github.com/abeatrix/cline-plugin-jev-browser">abeatrix/cline-plugin-jev-browser</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · abeatrix

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Cline Plugin to add a new computer run tool runs by the typesafe/jev model

</details>

<details>
<summary><b><a href="https://github.com/ably-labs/jev-pong">ably-labs/jev-pong</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · Apache-2.0 · ably-labs

##### Dati

Stelle **0** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Pong where the ball moves one step per model decision. Jev vs LLMs via Vercel AI Gateway, every player and agent on an Ably channel.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b51a044f9d543ef0.png" width="100%" alt="ably-labs/jev-pong screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b5b9b482a58f2c01.gif" width="100%" alt="ably-labs/jev-pong animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/aidil2105/jev-browser-pilot">aidil2105/jev-browser-pilot</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · aidil2105

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification.

</details>

<details>
<summary><b><a href="https://github.com/altregubov/jev-antigravity-mcp">altregubov/jev-antigravity-mcp</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · altregubov

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/alviso/jev-precheck">alviso/jev-precheck</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · alviso

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

A second signature on every write an AI agent makes into a system of record. MCP proxy: fetch the records, derive in code, Jev judges. 98.6% recall, 0 false holds on 288 cases.

</details>

<details>
<summary><b><a href="https://github.com/anisselbd/jev-phishing-bench">anisselbd/jev-phishing-bench</a></b> — Python · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · anisselbd

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/openclaw-jev-harness">AntonioCoppe/openclaw-jev-harness</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · AntonioCoppe

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

OpenClaw plugin: jev-harness DecisionHarness as System One decide layer (policy/confidence/shadow)

</details>

<details>
<summary><b><a href="https://github.com/AStheTECH/mewcp-jev">AStheTECH/mewcp-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · Apache-2.0 · AStheTECH

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

JEV MCP server by MewCP

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-align">caiovicentino/jev-align</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · caiovicentino

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Calibrated alignment verifier for LLM responses and agent plans — powered by Jev

</details>

<details>
<summary><b><a href="https://github.com/Calq-dev/ask-jev">Calq-dev/ask-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · Calq-dev

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Ask Jev a question about a file instead of reading it into the agent's context.

</details>

<details>
<summary><b><a href="https://github.com/cassiomc1/fast-jev-compaction-alt">cassiomc1/fast-jev-compaction-alt</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · cassiomc1

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Continuous, verbatim context compaction for LLM agents using TypeSafe's Jev model.

</details>

<details>
<summary><b><a href="https://github.com/cbruyndoncx/AskJev-MCP">cbruyndoncx/AskJev-MCP</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · cbruyndoncx

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence

</details>

<details>
<summary><b><a href="https://github.com/Clawbuilders/web-qa-jev-agent">Clawbuilders/web-qa-jev-agent</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · Clawbuilders

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Crawls a site with Cloudflare Browser Rendering, triages with typesafe/jev, confirms with vision, files deduped GitHub Issues

</details>

<details>
<summary><b><a href="https://github.com/DoGMaTiiC/hermes-jev">DoGMaTiiC/hermes-jev</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · DoGMaTiiC

##### Dati

Stelle **0** · Fork 0 · Issue aperte 7 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only.

</details>

<details>
<summary><b><a href="https://github.com/duketopceo/jev-compact">duketopceo/jev-compact</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · duketopceo

##### Dati

Stelle **0** · Fork 0 · Issue aperte 1 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP

</details>

<details>
<summary><b><a href="https://github.com/EtienneLescot/jev-router">EtienneLescot/jev-router</a></b> — HTML · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · HTML · MIT · EtienneLescot

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model tier and reasoning depth.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/etiennelescot--jev-router/96217fad0b128b3e.png" width="100%" alt="EtienneLescot/jev-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fast-facts/jev-mcp">fast-facts/jev-mcp</a></b> — Go · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Go · MIT · fast-facts

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/flaviusapop/jev-router">flaviusapop/jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · flaviusapop

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Routes each turn in Claude Code, Codex, Grok and opencode to the cheapest model and reasoning depth that can finish it, using TypeSafe Jev

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/flaviusapop--jev-router/b7f868696d35b78b.png" width="100%" alt="flaviusapop/jev-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Friedjof/jev-mobile">Friedjof/jev-mobile</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · Friedjof

##### Dati

Stelle **0** · Fork 0 · Issue aperte 4 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Fast structured Android control loops with TypeSafe Jev and Mobile MCP

</details>

<details>
<summary><b><a href="https://github.com/gzawadzki/jev-usecases">gzawadzki/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · gzawadzki

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage

</details>

<details>
<summary><b><a href="https://github.com/hangarbay/jev.mcp">hangarbay/jev.mcp</a></b> — Go · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Go · MIT · hangarbay

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/HomenShum/jev-swap">HomenShum/jev-swap</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · HomenShum

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Claude Code skill: swap System 2 LLM pipeline components for System 1 TypeSafe Jev decisions via investigation, live three-arm eval, fallback, and an independent judge

</details>

<details>
<summary><b><a href="https://github.com/IAnMove/jev-game-agent">IAnMove/jev-game-agent</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · IAnMove

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Experimental Jev game agent: RAM, emulator lookahead, checkpoint search and verified recordings. Bring your own ROM and BizHawk.

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-codex-plugin">integrate-your-mind/jev-codex-plugin</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · integrate-your-mind

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Open-source Codex plugin for TypeSafe Jev decision consultation, failure diagnosis, and evidence-based completion review

</details>

<details>
<summary><b><a href="https://github.com/its-panzer/jev-model-router">its-panzer/jev-model-router</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · its-panzer

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A policy router that picks the cheapest Claude model that can finish the job

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/its-panzer--jev-model-router/98819f5aaf8e6373.png" width="100%" alt="its-panzer/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/janegbert/ask-jev">janegbert/ask-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · janegbert

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Ask Jev about a file instead of reading it. A Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-macos-loop">jcpsimmons/jev-macos-loop</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · AGPL-3.0 · jcpsimmons

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jcpsimmons--jev-macos-loop/19bcb6c0f1788073.gif" width="100%" alt="jcpsimmons/jev-macos-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jcpsimmons--jev-macos-loop/c99113da6464b245.gif" width="100%" alt="jcpsimmons/jev-macos-loop animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/jcpsimmons/jev-macos-loop/master/docs/media/jev-finder-batch-demo.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcressler/fast-jev-compaction-codex">jcressler/fast-jev-compaction-codex</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · jcressler

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Task-aware Jev evidence selection and exact local recovery around native Codex compaction.

</details>

<details>
<summary><b><a href="https://github.com/jh1373/jev-search">jh1373/jev-search</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · jh1373

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Search your Obsidian vault locally and offline with no API key, then rerank the top results with Jev only after you approve exactly what gets sent. Experimental preview.

</details>

<details>
<summary><b><a href="https://github.com/jmanhype/jev-dspy-lab">jmanhype/jev-dspy-lab</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · jmanhype

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows

</details>

<details>
<summary><b><a href="https://github.com/JoacoMarc/jev-harness-router">JoacoMarc/jev-harness-router</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · JoacoMarc

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Per-turn harness router on Jev (TypeSafe): one batched call picks the model tier, tools, skill and effort budget for an agent turn, behind a hard latency deadline.

</details>

<details>
<summary><b><a href="https://github.com/kaijia323/dsh-plugin-jev">kaijia323/dsh-plugin-jev</a></b> — HTML · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · HTML · MIT · kaijia323

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">MahmoudAdelbghany/jev-browser</a></b> — JavaScript · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MahmoudAdelbghany

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included.

</details>

<details>
<summary><b><a href="https://github.com/micic-mihajlo/jev-tool-runner">micic-mihajlo/jev-tool-runner</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · micic-mihajlo

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/milanboers/jev-plays-pokemon">milanboers/jev-plays-pokemon</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · NOASSERTION · milanboers

##### Dati

Stelle **0** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Playing Pokemon Red using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/minhgv/jev-mcp">minhgv/jev-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · minhgv

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe Jev MCP decision layer for coding agents and CI

</details>

<details>
<summary><b><a href="https://github.com/morcoan/JevSeek">morcoan/JevSeek</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · morcoan

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools, persistent sessions, React desktop, and documented research.

</details>

<details>
<summary><b><a href="https://github.com/mozbz/jev-review-hook">mozbz/jev-review-hook</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · mozbz

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Jev powered code review hook for agents

</details>

<details>
<summary><b><a href="https://github.com/MSalvalaggio/jev-reflex">MSalvalaggio/jev-reflex</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · MSalvalaggio

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision).

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-mcp">nekowasabi/jev-routing-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · nekowasabi

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/noetion/dsh-jev">noetion/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · noetion

##### Dati

Stelle **0** · Fork 0 · Issue aperte 1 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.

</details>

<details>
<summary><b><a href="https://github.com/Nyarlathoteppppp/pi-jev-context">Nyarlathoteppppp/pi-jev-context</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · Nyarlathoteppppp

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Cache-neutral context trimming for the pi coding agent, powered by TypeSafe Jev: long tool output cut to verbatim key lines before it enters context, with lossless recall. Measured, with pre-registered benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/ourines/hermes-jev">ourines/hermes-jev</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · ourines

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev decision sidekick for Hermes Agent — TypeSafe and Cloudflare, explicit tools and official skill

</details>

<details>
<summary><b><a href="https://github.com/Panebianco00/jev-claude">Panebianco00/jev-claude</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · Panebianco00

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Route Claude Code's coding decisions through TypeSafe Jev: typed choices with probabilities, enforced at plan approval, questions, and risky commands.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-agent-router">Pinutss/jev-agent-router</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · Pinutss

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Explainable AI agent selection with abstention, bounded fallback, and a multi-LLM catalog.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-agent-router/a52e5bc01d9fd842.png" width="100%" alt="Pinutss/jev-agent-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-mcp-router">Pinutss/jev-mcp-router</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · Pinutss

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Select relevant MCP tools under a context-token budget, without executing them.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-mcp-router/3947a2a5cc3750c8.png" width="100%" alt="Pinutss/jev-mcp-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-memory-selector">Pinutss/jev-memory-selector</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · Pinutss

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-plugins">Pinutss/jev-plugins</a></b> — inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · MIT · Pinutss

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Cursor and Hermes marketplace for the four published JEV Labs routers.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-plugins/b3fcd72ac9e61f49.jpg" width="100%" alt="Pinutss/jev-plugins screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/raj8525/universal-jev">raj8525/universal-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · raj8525

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-gates">rashedInt32/jev-gates</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · MIT · rashedInt32

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/3996d0153a09b158.gif" width="100%" alt="rashedInt32/jev-gates screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/464e518e8a602a0d.gif" width="100%" alt="rashedInt32/jev-gates animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/rashedInt32/jev-gates/main/demo/out/jev-gates.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rubichandrap/hermes-jev-guard">rubichandrap/hermes-jev-guard</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · rubichandrap

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check

</details>

<details>
<summary><b><a href="https://github.com/Saik0s/diffusiongemma-jev-macos">Saik0s/diffusiongemma-jev-macos</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · Saik0s

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Local JEV-style decisions with DiffusionGemma on Apple Silicon, with benchmarks and coding-agent examples.

</details>

<details>
<summary><b><a href="https://github.com/shivam-raval96/multiagent-jev-monitor">shivam-raval96/multiagent-jev-monitor</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · shivam-raval96

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/sypherin/jev-trace-classifier">sypherin/jev-trace-classifier</a></b> — Python · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · sypherin

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next

</details>

<details>
<summary><b><a href="https://github.com/szocpaul/jev-compaction-prime">szocpaul/jev-compaction-prime</a></b> — inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · szocpaul

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Verbatim, decision-based context compaction for Prime Agent — instead of summaries, stale tool calls are scored and dropped; everything kept stays byte-for-byte intact.

</details>

<details>
<summary><b><a href="https://github.com/tgiridhar/claude-code-jev-smart-router">tgiridhar/claude-code-jev-smart-router</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · tgiridhar

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task phase and the cost of an undetected error, gated by prompt-cache arithmetic. Proof of concept.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tgiridhar--claude-code-jev-smart-router/28b9e1b2a005c7e2.png" width="100%" alt="tgiridhar/claude-code-jev-smart-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/themsquared/jev-benchmark">themsquared/jev-benchmark</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · Apache-2.0 · themsquared

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.

</details>

<details>
<summary><b><a href="https://github.com/thevibeworks/awesome-typesafe-jev">thevibeworks/awesome-typesafe-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · NOASSERTION · thevibeworks

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/ussyverse/hermes-jev-router">ussyverse/hermes-jev-router</a></b> — Python · inferred · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · ussyverse

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending.

</details>

<details>
<summary><b><a href="https://github.com/wotai-dev/typesafe-jev-tools">wotai-dev/typesafe-jev-tools</a></b> — Shell · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Shell · MIT · wotai-dev

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 149-row comparison of TypeSafe Jev against Claude Haiku 4.5.

</details>

<details>
<summary><b><a href="https://github.com/yangzhou-chaofan/awesome-jev-prompt">yangzhou-chaofan/awesome-jev-prompt</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · JavaScript · CC0-1.0 · yangzhou-chaofan

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

latest top 100 showcases for jev (keep updating) from x / github / latest sources

</details>

<details>
<summary><b><a href="https://github.com/zbloss/jev-plays-pokemon">zbloss/jev-plays-pokemon</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · Python · MIT · zbloss

##### Dati

Stelle **0** · Fork 0 · Issue aperte 2 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Like Claude Plays Pokemon, but with Jev

</details>

<details>
<summary><b><a href="https://github.com/zhangxaochen/dsh-jev">zhangxaochen/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `inferred` · TypeScript · MIT · zhangxaochen

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev (System One decision model) plugin suite for DeepSeek Harness (dsh)

</details>

<details>
<summary><b><a href="https://github.com/DevMortimer/pi-warden">DevMortimer/pi-warden</a></b> — ⭐61 · TypeScript · unverified · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `unverified` · TypeScript · MIT · DevMortimer

##### Dati

Stelle **61** · Fork 2 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop

> Guardrails that steer an agent before it acts. Demonstrates the gate pattern, where the decision is cheap enough to run on every step.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devmortimer--pi-warden/b8dc20ac6694613a.png" width="100%" alt="DevMortimer/pi-warden screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/3clyp50/a0-typesafe-ai">3clyp50/a0-typesafe-ai</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `unverified` · Python · MIT · 3clyp50

##### Dati

Stelle **4** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/3clyp50--a0-typesafe-ai/9aa8ea4ef8241f14.png" width="100%" alt="3clyp50/a0-typesafe-ai screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/pi-quiet-ask">HyunjunJeon/pi-quiet-ask</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `unverified` · TypeScript · MIT · HyunjunJeon

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe Jev as the pi coding agent's quiet decision layer

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hyunjunjeon--pi-quiet-ask/7ee3a99430e853d8.png" width="100%" alt="HyunjunJeon/pi-quiet-ask screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/zoidsh/tenet">zoidsh/tenet</a></b> — ⭐3 · Go · unverified · 0 天</summary>

##### Dati essenziali

`Strumenti per agenti: MCP, hook, gate e agenti di coding` · Comunità · `unverified` · Go · MIT · zoidsh

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

The review gate for code that agents write: rules in plain language, judged on every commit

</details>

<a id="routing-guardrails"></a>

## Instradamento, guardrail e approvazioni

Il caso d'uso in forma di produzione: invia ogni richiesta al modello più economico che sappia davvero gestirla e mantieni un controllo deterministico sull'esito.

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐44 · Rust · observed · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `observed` · Rust · NOASSERTION · Dicklesworthstone

##### Dati

Stelle **44** (+1) · Fork 3 · Issue aperte 1 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐26 · Python · observed · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `observed` · Python · brainstormity

##### Dati

Stelle **26** (+1) · Fork 2 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

<sub>Trovato in uso nel codice: `typesafe/__init__.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 1 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `observed` · Python · MIT · Foadsf

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `observed` · TypeScript · MIT · qddegtya

##### Dati

Stelle **1** · Fork 0 · Issue aperte 3 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Typed decisions from a System One model. An uncertain answer is a different type from a confident one — and the compiler makes you handle it.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `observed` · Python · aniruddh-krovvidi

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐22 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · MIT · yusukebe

##### Dati

Stelle **22** (+4) · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐6 · JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · JavaScript · MIT · mejiasd3v

##### Dati

Stelle **6** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · andrelandgraf

##### Dati

Stelle **3** · Fork 0 · Issue aperte 1 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · MIT · keeltrace

##### Dati

Stelle **3** · Fork 0 · Issue aperte 1 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/jerryfane/omp-jev-compaction">jerryfane/omp-jev-compaction</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · MIT · jerryfane

##### Dati

Stelle **2** · Fork 1 · Issue aperte 2 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · MIT · maker-KK

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · MIT · WiktorB2004

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · MIT · Pinutss

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · MIT · prismhq

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Shashank-H

##### Dati

Stelle **1** · Fork 0 · Issue aperte 1 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/aaronshaf/opencode-jev-model-router">aaronshaf/opencode-jev-model-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · MIT · aaronshaf

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev-based automatic per-turn model routing for OpenCode

</details>

<details>
<summary><b><a href="https://github.com/alexrudloff/inbox-zero-jev">alexrudloff/inbox-zero-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · MIT · alexrudloff

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Conversation-aware inbox triage with Jev: keep, archive, or review.

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Jupyter · MIT · bitnovus

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/carllippert/jev-router">carllippert/jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · MIT · carllippert

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Express with no routes. TypeSafe Jev picks which handler runs.

</details>

<details>
<summary><b><a href="https://github.com/danfry1/jev-triage">danfry1/jev-triage</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · MIT · danfry1

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

GitHub Action that labels, deduplicates and spam-checks issues with Jev, with calibrated confidence for every decision

</details>

<details>
<summary><b><a href="https://github.com/danielhirt/jev-lab">danielhirt/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · danielhirt

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison

</details>

<details>
<summary><b><a href="https://github.com/gnoviawan/omp-jev-tools">gnoviawan/omp-jev-tools</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · NOASSERTION · gnoviawan

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation verification

</details>

<details>
<summary><b><a href="https://github.com/hugo-alves/jev-router-playground">hugo-alves/jev-router-playground</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · JavaScript · MIT · hugo-alves

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Interactive playground for testing Jev model-routing decisions against OpenRouter models

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hugo-alves--jev-router-playground/93692a5f183f12e1.jpg" width="100%" alt="hugo-alves/jev-router-playground screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iefnaf/pi-jev">iefnaf/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · MIT · iefnaf

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Pi extension suite powered by Jev: selective context compaction and model routing

</details>

<details>
<summary><b><a href="https://github.com/kenhuangus/jev-usecases">kenhuangus/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · MIT · kenhuangus

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kenhuangus--jev-usecases/be919255190f6495.png" width="100%" alt="kenhuangus/jev-usecases screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-bot">kevin9327/jev-bot</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · MIT · kevin9327

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.

</details>

<details>
<summary><b><a href="https://github.com/Loule95450/jev-free-router">Loule95450/jev-free-router</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · JavaScript · MIT · Loule95450

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Dynamic per-turn model router on free OpenCode Zen + Go models (fork of gargpratyush/jev-router)

</details>

<details>
<summary><b><a href="https://github.com/makefinks/jev-feed-filter">makefinks/jev-feed-filter</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · MIT · makefinks

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Smart, dynamic AI filtering for X and YouTube feeds using Jev

</details>

<details>
<summary><b><a href="https://github.com/MoonTory/pi-jev-harness">MoonTory/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · MoonTory

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards tool calls

</details>

<details>
<summary><b><a href="https://github.com/nitinnat/jev-gateway">nitinnat/jev-gateway</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · JavaScript · MIT · nitinnat

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A small local HTTP service for TypeSafe AI's Jev through Vercel

</details>

<details>
<summary><b><a href="https://github.com/rajivkuriakose/typesafe-jev-examples">rajivkuriakose/typesafe-jev-examples</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · MIT · rajivkuriakose

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/SadiqOnGithub/jev-lab">SadiqOnGithub/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · TypeScript · SadiqOnGithub

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API

</details>

<details>
<summary><b><a href="https://github.com/TokenTrim/jev-routing-experiment">TokenTrim/jev-routing-experiment</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Python · Apache-2.0 · TokenTrim

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tokentrim--jev-routing-experiment/1c31bd606ebc1994.png" width="100%" alt="TokenTrim/jev-routing-experiment screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ufec/jev-block-android-ad">ufec/jev-block-android-ad</a></b> — Kotlin · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · Kotlin · MIT · ufec

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

JevNoiseGate filters unwanted notifications and SMS on Android. Rather than   matching keywords, an LLM decides what's noise — and only what it explicitly   flags is blocked. Verification codes are matched on-device and never uploaded;   anything uncertain passes through.

</details>

<details>
<summary><b><a href="https://github.com/wadadanet/faq-jev-router">wadadanet/faq-jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `inferred` · JavaScript · MIT · wadadanet

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Cascade FAQ routing with TypeSafe Jev — category → FAQ or not found (GitHub Pages demo)

</details>

<details>
<summary><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">iammrduncan/typesafe-ai-benchmark</a></b> — ⭐31 · TypeScript · unverified · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `unverified` · TypeScript · MIT · iammrduncan

##### Dati

Stelle **31** · Fork 5 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.

> A gateway that mimics the System One interface, which is what makes side-by-side benchmarking possible without rewriting the caller.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/3d66c620e48ff597.gif" width="100%" alt="iammrduncan/typesafe-ai-benchmark animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/iammrduncan/typesafe-ai-benchmark/main/docs/media/theater-demo.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kavehmz/typesafe-playground">kavehmz/typesafe-playground</a></b> — ⭐6 · JavaScript · unverified · 0 天 · ⭐+2</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `unverified` · JavaScript · kavehmz

##### Dati

Stelle **6** (+2) · Fork 2 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/kavehmz/typesafe-playground/main/docs/images/demo03-fable.png" width="100%" alt="kavehmz/typesafe-playground screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/raihankhan-rk/diffjury">raihankhan-rk/diffjury</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Dati essenziali

`Instradamento, guardrail e approvazioni` · Comunità · `unverified` · TypeScript · raihankhan-rk

##### Dati

Stelle **3** · Fork 1 · Issue aperte 2 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

DiffJury — TypeSafe Jev PR risk router + code review coach

</details>

<a id="evaluation"></a>

## Valutazione, calibrazione e benchmark

Come si fa a sapere se le decisioni sono buone. La calibrazione è la questione aperta in questo ecosistema, e questi sono i progetti che la misurano.

<details>
<summary><b><a href="https://github.com/edgardcham/huncho">edgardcham/huncho</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `observed` · TypeScript · MIT · edgardcham

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Decisions as code on System One models: typed questions, thresholds with hysteresis, nested decisions, journal, calibration

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `observed` · Go · MIT · Gaurav-Gosain

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `observed` · Python · Apache-2.0 · hev

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — Python · observed · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `observed` · Python · akash-kamat

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/nishioka-shinji/jev-edgar">nishioka-shinji/jev-edgar</a></b> — Python · observed · 0 天 · **NEW**</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `observed` · Python · nishioka-shinji

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Does Jev, a System One model returning calibrated probabilities, say anything useful about an earnings release before the market prices it?

</details>

<details>
<summary><b><a href="https://github.com/JoshuaSP/open-jev">JoshuaSP/open-jev</a></b> — ⭐14 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · MIT · JoshuaSP

##### Dati

Stelle **14** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Typed JSON inference with DiffusionGemma, with Every and Jev benchmark results

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/joshuasp--open-jev/1d4a9f6368358e43.png" width="100%" alt="JoshuaSP/open-jev screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rorshopping/jev-on-a-laptop">rorshopping/jev-on-a-laptop</a></b> — ⭐14 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · NOASSERTION · rorshopping

##### Dati

Stelle **14** · Fork 1 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Unofficial study: Jev-style parallel typed decisions on stock 1.5B-8B models on an Apple Silicon laptop. Benchmarks, research notes, and a Hugging Face Space demo.

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐7 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · Apache-2.0 · AbdelStark

##### Dati

Stelle **7** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐4 · TypeScript · inferred · 2 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · TypeScript · MIT · y0usaf

##### Dati

Stelle **4** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/abhixhek/jevcal">abhixhek/jevcal</a></b> — ⭐3 · Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · MIT · abhixhek

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abhixhek--jevcal/3dbe2307176737c8.png" width="100%" alt="abhixhek/jevcal screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · NOASSERTION · Heman10x-NGU

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · Apache-2.0 · ikermoel

##### Dati

Stelle **2** · Fork 1 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Open alternative to Jev: typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with benchmarks

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · MIT · wondertwins

##### Dati

Stelle **2** · Fork 1 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rongxinzy/LightJev">rongxinzy/LightJev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · Apache-2.0 · rongxinzy

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Train lightweight language backbones for typed decisions and candidate probabilities. CE/Brier training, evaluation, and an offline end-to-end demo.

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · 4esv

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-eval/main/results/coverage.png" width="100%" alt="4esv/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/aieo-product/jev-gamebenchmark">aieo-product/jev-gamebenchmark</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · MIT · aieo-product

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Sandbox & benchmark: optimize how you ask Jev (TypeSafe System One) to play falling-block puzzle games, head-to-head against LLMs

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · TypeScript · MIT · Danu28

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · TeX · NOASSERTION · dnakhoa

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · eggmasonvalue

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · MIT · jujumilk3

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · JavaScript · MIT · KantaHayashiAI

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and">musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and</a></b> — HTML · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · HTML · MIT · musman550

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@automatewithmusfiraai"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@automatewithmusfiraai">Guarda su youtube.com</a> · la riproduzione si apre sul sito ospite; GitHub non può incorporarla inline</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/onlyoneaman/jev-eval">onlyoneaman/jev-eval</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · TypeScript · MIT · onlyoneaman

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/onlyoneaman--jev-eval/e5d471e96e134f81.png" width="100%" alt="onlyoneaman/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/robipop22/Jev-is-odd">robipop22/Jev-is-odd</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · JavaScript · MIT · robipop22

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Ask Jev by TypeSafe AI whether a number is odd. TypeScript, real token usage, and latency benchmarks.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/robipop22--jev-is-odd/5c4ddde817bd6cdc.png" width="100%" alt="robipop22/Jev-is-odd screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shunta-furukawa/jev-tick-lab">shunta-furukawa/jev-tick-lab</a></b> — inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · shunta-furukawa

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis.

</details>

<details>
<summary><b><a href="https://github.com/teyhouse/jev-secret-detection">teyhouse/jev-secret-detection</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · Python · teyhouse

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" width="100%" alt="teyhouse/jev-secret-detection screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/uspraveen/Jev-Reranker">uspraveen/Jev-Reranker</a></b> — inferred · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `inferred` · MIT · uspraveen

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A System-1 model based memory retrieval reranked using caliberated decision space instead of embeddings

</details>

<details>
<summary><b><a href="https://github.com/Mapika/decider">Mapika/decider</a></b> — ⭐23 · Python · unverified · 0 天 · ⭐-56</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `unverified` · Python · Apache-2.0 · Mapika

##### Dati

Stelle **23** (-56) · Fork 2 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mapika--decider/c67d355f22dcb51a.gif" width="100%" alt="Mapika/decider animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kyotofin/tax-doc-classifier">kyotofin/tax-doc-classifier</a></b> — ⭐8 · TypeScript · unverified · 0 天 · **NEW**</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `unverified` · TypeScript · Apache-2.0 · kyotofin

##### Dati

Stelle **8** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.

</details>

<details>
<summary><b><a href="https://github.com/genai-craft/openvons">genai-craft/openvons</a></b> — ⭐7 · Python · unverified · 0 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `unverified` · Python · NOASSERTION · genai-craft

##### Dati

Stelle **7** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド

</details>

<details>
<summary><b><a href="https://github.com/aabolfazl/typesafe-local">aabolfazl/typesafe-local</a></b> — ⭐4 · Python · unverified · 0 天 · **NEW**</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `unverified` · Python · MIT · aabolfazl

##### Dati

Stelle **4** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/aabolfazl--typesafe-local/ada59cf382af5143.png" width="100%" alt="aabolfazl/typesafe-local screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mithalouni/system-one-open">mithalouni/system-one-open</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### Dati essenziali

`Valutazione, calibrazione e benchmark` · Comunità · `unverified` · Python · NOASSERTION · mithalouni

##### Dati

Stelle **4** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal)

</details>

<a id="research-models"></a>

## Riproduzioni aperte, pesi e ricerca sull&#x27;architettura

Pesi aperti, repliche ridotte e lavoro sull'architettura. Alcuni esistono perché il comportamento di calibrazione non è riproducibile solo dal materiale pubblico.

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐58 · Python · observed · 0 天 · ⭐+7</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `observed` · Python · MIT · kshetrajna12

##### Dati

Stelle **58** (+7) · Fork 3 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐318 · Python · inferred · 0 天 · ⭐+51</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · Python · MIT · TianyuCodings

##### Dati

Stelle **318** (+51) · Fork 26 · Issue aperte 1 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/5055af419619e7e4.gif" width="100%" alt="TianyuCodings/NanoJev animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/assets/side_by_side_maze.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐21 · Python · inferred · 0 天 · ⭐+4</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · Python · MIT · r-ms

##### Dati

Stelle **21** (+4) · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `observed`

##### Dati

Download 25 · Mi piace 2 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 0 天</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `observed`

##### Dati

Download 0 · Mi piace 0 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐129 · Python · inferred · 0 天 · ⭐+7</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · Python · ekzhang

##### Dati

Stelle **129** (+7) · Fork 11 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐21 · Python · inferred · 0 天 · ⭐+2</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · Python · MIT · bnsd55

##### Dati

Stelle **21** (+2) · Fork 3 · Issue aperte 2 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/choxos/jev-reviewer">choxos/jev-reviewer</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · JavaScript · MIT · choxos

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Ask a trial report and its supplements for systematic review data by voice, text or a questions file. Jev (TypeSafe System One) points at the lines; every answer is a verbatim quote with its file and page. PDF, Word and text files; CSV export.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/0cb463e9afed9f49.jpg" width="100%" alt="choxos/jev-reviewer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/9c16f3b518343fe6.gif" width="100%" alt="choxos/jev-reviewer animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/choxos/jev-reviewer/main/documentation/tour.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/featherless-ai/simple-jev">featherless-ai/simple-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · Python · featherless-ai

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Turn any open model into a classifier/jev endpoint

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/featherless-ai/simple-jev/main/imgs/Simple-Jev-Logo.png" width="100%" alt="featherless-ai/simple-jev screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-nethack">integrate-your-mind/jev-nethack</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · Python · integrate-your-mind

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev x NetHack: bounded runner, research code, and completed recording releases

</details>

<details>
<summary><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">legacybridge-tech/pi-typesafe-jev</a></b> — TypeScript · inferred · 1 天</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · TypeScript · NOASSERTION · legacybridge-tech

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.

</details>

<details>
<summary><b><a href="https://github.com/objectgraph/jev-samegame-bench">objectgraph/jev-samegame-bench</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · TypeScript · MIT · objectgraph

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

What should a decision model be shown to play SameGame? 21 prompt strategies for TypeSafe's Jev, 76,795 logged requests and responses, reproducible tables. MIT.

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `inferred` · Python · shellneko

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐5 · Python · unverified · 2 天</summary>

##### Dati essenziali

`Riproduzioni aperte, pesi e ricerca sull&#x27;architettura` · Comunità · `unverified` · Python · NOASSERTION · zhihz

##### Dati

Stelle **5** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<a id="apps-demos"></a>

## Applicazioni, giochi, robotica e demo interattive

Giochi, robot, browser e dashboard. Le demo sono il modo in cui le affermazioni su latenza e costi diventano leggibili.

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `observed` · Python · Apache-2.0 · zadescoxp

##### Dati

Stelle **7** · Fork 1 · Issue aperte 3 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `observed` · TypeScript · daftAI2026

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `observed` · Rust · MIT · markjaquith

##### Dati

Stelle **1** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `observed` · TypeScript · adiun

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `observed` · Dart · Bud-ro

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `observed` · Python · MIT · tirukovelamanoj

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/8c1b0d55baf76296.gif" width="100%" alt="tirukovelamanoj/jev-plays-doom animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/tirukovelamanoj/jev-plays-doom/main/docs/jev-doom.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `observed` · TypeScript · wustep

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://x.com/tspy/status/2100864234523685146">X intent labeller</a></b> — @tspy · observed · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `observed` · [yishan](https://x.com/tspy) · @tspy · x.com

##### Dati

Visualizzazioni 2364 · Mi piace 15 · Commenti 9 · Pubblicato 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A Chrome extension that labels posts in an X timeline with their intent and probability as you scroll, drawn as a tag directly after each post's timestamp. Categories include inducement, provocation, promotion, machine-generated, persuasion, entertainment and information. A side panel reports session counts (seen, judged, correct) and cumulative token cost. The author reports near-instant responses and usable accuracy before any tuning.

<sub>Ricerca del link al progetto originale.</sub>

> Worth reading as a latency argument rather than an accuracy one: labelling a timeline only works if the decision costs less than the scroll, which is the constraint a generative model cannot meet.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/0641644f12a25a45.jpg" width="100%" alt="X intent labeller screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/b80cf3173f63bdd7.gif" width="100%" alt="X intent labeller animation"><br><sub>registrazione animata · <a href="https://video.twimg.com/amplify_video/2100858340331200512/vid/avc1/1242x720/ex2FF5-TerVxo9xX.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐100 · Python · inferred · 0 天 · ⭐+8</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · Python · MIT · hr98w

##### Dati

Stelle **100** (+8) · Fork 11 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐81 · TypeScript · inferred · 0 天 · ⭐+12</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · MIT · jkudish

##### Dati

Stelle **81** (+12) · Fork 4 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/b4ae7fc04353e74c.gif" width="100%" alt="jkudish/jev-browser animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐41 · JavaScript · inferred · 0 天 · ⭐+7</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · JavaScript · MIT · moritzkremb

##### Dati

Stelle **41** (+7) · Fork 6 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/mizchi/jev-playground">mizchi/jev-playground</a></b> — ⭐14 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · mizchi

##### Dati

Stelle **14** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/mario-jev">shantanugoel/mario-jev</a></b> — ⭐10 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · Python · shantanugoel

##### Dati

Stelle **10** · Fork 2 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · emrickgarrett

##### Dati

Stelle **5** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · Python · MIT · komorra

##### Dati

Stelle **5** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>registrazione animata</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/arielweinberger/jev-autopilot">arielweinberger/jev-autopilot</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · arielweinberger

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs $0.01.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/arielweinberger/jev-autopilot/main/docs/demo.png" width="100%" alt="arielweinberger/jev-autopilot screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐3 · JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · JavaScript · vinilana

##### Dati

Stelle **3** · Fork 3 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · Go · MIT · paulsmith

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · MIT · vmendes90

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-mario">4esv/jev-mario</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · Python · 4esv

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe Jev plays Super Mario Bros from a text description of emulator RAM

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-mario/main/runs/1-1-jev-20260918-120708.gif" width="100%" alt="4esv/jev-mario screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-mario/main/runs/1-1-jev-20260918-120708.gif" width="100%" alt="4esv/jev-mario animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/joevidev/ui-generator-instinct-jev">joevidev/ui-generator-instinct-jev</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · joevidev

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · Little-Planet-Labs

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · Python · PistachioAIHQ

##### Dati

Stelle **1** · Fork 1 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/bahramzada/jev-taxi-dispatch">bahramzada/jev-taxi-dispatch</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · JavaScript · MIT · bahramzada

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Real-vaxt taksi dispetçerlik simulyasiyası — TypeSafe JEV (System One) modeli ilə

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/bahramzada--jev-taxi-dispatch/e616f4168b15d3f2.png" width="100%" alt="bahramzada/jev-taxi-dispatch screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/BrendanH18/jev-lab">BrendanH18/jev-lab</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · Python · MIT · BrendanH18

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brendanh18--jev-lab/b16b9535e3744cd3.png" width="100%" alt="BrendanH18/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jflam/jev1">jflam/jev1</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · JavaScript · jflam

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev (TypeSafe System One) proof of concept: smart-home assistant demo

</details>

<details>
<summary><b><a href="https://github.com/JYeswak/jev_playground">JYeswak/jev_playground</a></b> — Shell · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · Shell · MIT · JYeswak

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jyeswak--jev_playground/b6414da07c9c5aa8.jpg" width="100%" alt="JYeswak/jev_playground screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/marcelomar21/demo-tetris-jev">marcelomar21/demo-tetris-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · JavaScript · marcelomar21

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Tetris arcade jogado pelo Jev da TypeSafe AI, com decisões em JSON, antecipação de jogadas e custo por partida.

</details>

<details>
<summary><b><a href="https://github.com/n3ndor/n8n-nodes-typesafe-jev">n3ndor/n8n-nodes-typesafe-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · MIT · n3ndor

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

n8n community node for TypeSafe Jev structured AI decisions

</details>

<details>
<summary><b><a href="https://github.com/PauloLuan/jev-obscura-browser">PauloLuan/jev-obscura-browser</a></b> — inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · PauloLuan

##### Dati

Stelle **0** · Fork 0 · Issue aperte 1 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/pelazas/jev-cmdtab">pelazas/jev-cmdtab</a></b> — Swift · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · Swift · MIT · pelazas

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

macOS app switcher with Apple's Cmd+Tab HUD. Smarter order, same design.

</details>

<details>
<summary><b><a href="https://github.com/PierrunoYT/JevFlow">PierrunoYT/JevFlow</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · PierrunoYT

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

A trading bot powered by TypeSafe AI's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pistachiopranay/jev-synergy-screening">pistachiopranay/jev-synergy-screening</a></b> — inferred · 1 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · pistachiopranay

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/rchovatiya88/cyber-breach-jev">rchovatiya88/cyber-breach-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · JavaScript · rchovatiya88

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model

</details>

<details>
<summary><b><a href="https://github.com/Satpal777/jev-games">Satpal777/jev-games</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · Satpal777

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/Spykoninho/trading-bot-jev">Spykoninho/trading-bot-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · Spykoninho

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Crypto trading bot on Binance testnet using TypeSafe (Jev) to judge news

</details>

<details>
<summary><b><a href="https://github.com/yatharth1706/jev-automation">yatharth1706/jev-automation</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `inferred` · TypeScript · yatharth1706

##### Dati

Stelle **0** · Fork 0 · Issue aperte 1 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Trying automation on web browser via jev from typesafe

</details>

<details>
<summary><b><a href="https://github.com/sorrycc/typesafe-snake">sorrycc/typesafe-snake</a></b> — ⭐17 · TypeScript · unverified · 1 天</summary>

##### Dati essenziali

`Applicazioni, giochi, robotica e demo interattive` · Comunità · `unverified` · TypeScript · sorrycc

##### Dati

Stelle **17** · Fork 2 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code

</details>

<a id="media-discussions"></a>

## Articoli, discussioni e liste affini

Thread di lancio, analisi indipendenti e le altre liste curate di questo spazio. Questo repository non è l'unico, e dirlo è più utile che fingere il contrario.

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐4937 · Python · observed · 0 天 · ⭐+314</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · Python · MIT · browser-use

##### Dati

Stelle **4937** (+314) · Fork 305 · Issue aperte 29 · Creato 2026-09-16 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

i. am. speed.

<sub>Trovato in uso nel codice: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcdb919ac3afb514.gif" width="100%" alt="browser-use/jev-ultrafast animation"><br><sub>registrazione animata · <a href="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/demo.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1885 · observed · 2 天 · ⭐+3</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 1885 · Commenti 494 · Ultimo push 2026-09-15 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐496 · Python · observed · 0 天 · ⭐+14</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · Python · MIT · Anil-matcha

##### Dati

Stelle **496** (+14) · Fork 94 · Issue aperte 8 · Creato 2023-05-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>Trovato in uso nel codice: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐214 · CSS · observed · 0 天 · ⭐+15</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · CSS · MIT · AbdelStark

##### Dati

Stelle **214** (+15) · Fork 30 · Issue aperte 1 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>Trovato in uso nel codice: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐161 · TypeScript · observed · 0 天 · ⭐+22</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · TypeScript · dabit3

##### Dati

Stelle **161** (+22) · Fork 15 · Issue aperte 17 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

<sub>Trovato in uso nel codice: `jev-lint/proxy.mjs`, `jev-tower/jev-proxy.mjs`, `jev-instant-search/bench/dump.ts`, `jev-swarm/jev-proxy.mjs`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐123 · Python · observed · 0 天 · ⭐+17</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · Python · yibie

##### Dati

Stelle **123** (+17) · Fork 16 · Issue aperte 4 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐82 · observed · 0 天 · ⭐+17</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · CC0-1.0 · cobanov

##### Dati

Stelle **82** (+17) · Fork 6 · Issue aperte 5 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐56 · observed · 0 天 · ⭐+6</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · CC0-1.0 · AnotiaWang

##### Dati

Stelle **56** (+6) · Fork 14 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>Trovato in uso nel codice: `README.md`, `README_zh.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐42 · observed · 1 天 · ⭐+2</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 42 · Commenti 10 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐29 · JavaScript · observed · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### Dati

Stelle **29** (+1) · Fork 3 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A community directory of projects built on Jev, TypeSafe AI's System One model.

<sub>Trovato in uso nel codice: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐5 · JavaScript · observed · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · JavaScript · NOASSERTION · OmniJev

##### Dati

Stelle **5** (+1) · Fork 2 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Papers, open reproductions and independent evaluations behind System One models and Jev.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 2 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 5 · Commenti 0 · Ultimo push 2026-09-15 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 4 · Commenti 0 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 4 · Commenti 0 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49757009">Bespoke Nimble: open data, open model, open recipe for an open Jev</a></b> — ⭐3 · observed · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 3 · Commenti 0 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 3 · Commenti 0 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49754951">Show HN: Using Jev to generate game levels in real time</a></b> — ⭐3 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 3 · Commenti 1 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 3 · Commenti 0 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755430">You could have built Jev</a></b> — ⭐3 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 3 · Commenti 0 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### Dati

Stelle **2** · Fork 1 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49753667">Show HN: Explore 2D semantic space with the Jev model</a></b> — ⭐2 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 2 · Commenti 0 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

SemanticSpace is an experiment around Jev, TypeSafe AI’s new model. It uses a Cartesian plane defined by arbitrary phrases for each axis, to map prompts onto the resulting 2D semantic space. You can edit the prompts and axes to visualize virtually any 2D relationship.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49756921">Show HN: Jev helps you to not run malicous code</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 2 · Commenti 0 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49750649">Show HN: Open-Source Alternative to TypeSafe.ai</a></b> — ⭐2 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 2 · Commenti 1 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49744527">Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)</a></b> — ⭐2 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 2 · Commenti 1 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Full disclosure, it was coded with AI, I don&#x27;t claim otherwise. But I wanted to test out tool calls and iterative problem solving using Jev and needed a simple library&#x2F;framework&#x2F;harness to do that.
SOKIT (System One Knowledge, Instructions and Tools) is the result

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49729945">The first (public) System One Model; Jev gives AI the properties of code</a></b> — ⭐2 · observed · 2 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 2 · Commenti 0 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755005">Two techniques for working with System One models</a></b> — ⭐2 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 2 · Commenti 0 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49745212">Typesafe&#x27;s Jev is the fish at the poker table</a></b> — ⭐2 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 2 · Commenti 1 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49733647">Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step</a></b> — ⭐2 · observed · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 2 · Commenti 0 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49734345">Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD</a></b> — ⭐2 · observed · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed`

##### Dati

Punti 2 · Commenti 0 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐1 · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · NOASSERTION · aliaihub

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://github.com/ozers/jevsome-projects">ozers/jevsome-projects</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · JavaScript · MIT · ozers

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Open-source projects that provably call Jev, TypeSafe AI's System One model. Every entry links to the line of code that proves it. Refreshed daily.

</details>

<details>
<summary><b><a href="https://github.com/rhc98/awesome-jev">rhc98/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · TypeScript · NOASSERTION · rhc98

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself.

</details>

<details>
<summary><b><a href="https://github.com/soderlind/ai-provider-for-jev">soderlind/ai-provider-for-jev</a></b> — ⭐1 · PHP · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · PHP · soderlind

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).

</details>

<details>
<summary><b><a href="https://github.com/alpibrusl/lex-judge">alpibrusl/lex-judge</a></b> — Lex · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · Lex · alpibrusl

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Typed judgments from a System One model, as a \[net\]-only Lex effect

</details>

<details>
<summary><b><a href="https://github.com/deepanwadhwa/OpenDecision">deepanwadhwa/OpenDecision</a></b> — Python · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · Python · Apache-2.0 · deepanwadhwa

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Open Type Safe System one model system

</details>

<details>
<summary><b><a href="https://github.com/gzd2032/typesafe-ai-test">gzd2032/typesafe-ai-test</a></b> — observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · gzd2032

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

a test repo for typesafe.ai

</details>

<details>
<summary><b><a href="https://github.com/hide-G/magi-system-on-jev">hide-G/magi-system-on-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · JavaScript · hide-G

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/hide-G/magi-system-on-jev/master/public/ogp.png" width="100%" alt="hide-G/magi-system-on-jev screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/JohnDotOwl/awesome-jev">JohnDotOwl/awesome-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · JavaScript · CC0-1.0 · JohnDotOwl

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A curated list of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/piyush97/focus-tube">piyush97/focus-tube</a></b> — JavaScript · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · JavaScript · MIT · piyush97

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model

</details>

<details>
<summary><b><a href="https://github.com/rbalch/typesafeai-review">rbalch/typesafeai-review</a></b> — Python · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · Python · rbalch

##### Dati

Stelle **0** · Fork 0 · Issue aperte 2 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Using Typesafe.AI to generate diff reviews.

</details>

<details>
<summary><b><a href="https://github.com/robzolkos/omarchy-issue-classifier">robzolkos/omarchy-issue-classifier</a></b> — Ruby · observed · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · Ruby · robzolkos

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Classify the Omarchy issue backlog with Jev, TypeSafe's System One model. Ten typed questions per issue in one request, for a hundredth of a cent each.

</details>

<details>
<summary><b><a href="https://github.com/TheGali/terrarium">TheGali/terrarium</a></b> — JavaScript · observed · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `observed` · JavaScript · MIT · TheGali

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.

</details>

<details>
<summary><b><a href="https://github.com/jarrodwatts/jev-trader">jarrodwatts/jev-trader</a></b> — ⭐809 · TypeScript · inferred · 1 天 · ⭐+36</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · jarrodwatts

##### Dati

Stelle **809** (+36) · Fork 153 · Issue aperte 3 · Creato 2026-09-16 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

</details>

<details>
<summary><b><a href="https://github.com/droidrun/mobile-jev">droidrun/mobile-jev</a></b> — ⭐104 · JavaScript · inferred · 1 天 · ⭐+13</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · JavaScript · MIT · droidrun

##### Dati

Stelle **104** (+13) · Fork 20 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/superagents-lab/jev-search">superagents-lab/jev-search</a></b> — ⭐49 · TypeScript · inferred · 0 天 · ⭐+13</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · superagents-lab

##### Dati

Stelle **49** (+13) · Fork 7 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/superagents-lab--jev-search/5a545ddfd6a52aed.png" width="100%" alt="superagents-lab/jev-search screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mrnugget/jev-shell-history">mrnugget/jev-shell-history</a></b> — ⭐33 · TypeScript · inferred · 0 天 · ⭐+6</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · mrnugget

##### Dati

Stelle **33** (+6) · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Fish-style zsh history autosuggestions ranked by Jev (TypeSafe)

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history animation"><br><sub>registrazione animata</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">IAmUnbounded/save-token-jev-clean</a></b> — ⭐31 · TypeScript · inferred · 0 天 · ⭐+6</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · IAmUnbounded

##### Dati

Stelle **31** (+6) · Fork 7 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/daseinlabs/open-jev">daseinlabs/open-jev</a></b> — ⭐27 · Python · inferred · 0 天 · ⭐+2</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · daseinlabs

##### Dati

Stelle **27** (+2) · Fork 4 · Issue aperte 4 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov"><img src="" width="100%" alt="daseinlabs/open-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hqman/JevScout">hqman/JevScout</a></b> — ⭐14 · Python · inferred · 0 天 · ⭐+4</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · hqman

##### Dati

Stelle **14** (+4) · Fork 1 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4"><img src="" width="100%" alt="hqman/JevScout video"></a><br><sub><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Kevthetech143/super-jev">Kevthetech143/super-jev</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · MIT · Kevthetech143

##### Dati

Stelle **5** · Fork 1 · Issue aperte 1 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

A small, extensible decision-to-action harness for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/mateonunez/jod">mateonunez/jod</a></b> — ⭐3 · TypeScript · inferred · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · mateonunez

##### Dati

Stelle **3** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers.

</details>

<details>
<summary><b><a href="https://github.com/haseeb-heaven/jev-system-one">haseeb-heaven/jev-system-one</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · MIT · haseeb-heaven

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/haseeb-heaven--jev-system-one/e41c848323b1077a.png" width="100%" alt="haseeb-heaven/jev-system-one screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/joelhooks/pi-fast-jev-compaction">joelhooks/pi-fast-jev-compaction</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · joelhooks

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Pi extension: verbatim context compaction with TypeSafe Jev decisions

</details>

<details>
<summary><b><a href="https://github.com/kevinpita/pi-jev-context">kevinpita/pi-jev-context</a></b> — ⭐2 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · kevinpita

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Reversible context pruning for Pi, powered by TypeSafe Jev. Keep useful context without deleting session history.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevinpita--pi-jev-context/9f40314df01e39d4.png" width="100%" alt="kevinpita/pi-jev-context screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/LamplighterPaul/jev-piano">LamplighterPaul/jev-piano</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · LamplighterPaul

##### Dati

Stelle **2** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev cannot generate a single note. Given a piano and the right questions, it improvises anyway.

</details>

<details>
<summary><b><a href="https://github.com/anxkhn/JevPlaysPokemon">anxkhn/JevPlaysPokemon</a></b> — ⭐1 · HTML · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · HTML · GPL-3.0 · anxkhn

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev plays Generation 3 Pokémon via Showdown and a real FireRed ROM.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/anxkhn--jevplayspokemon/fc9ead060d7fa36a.png" width="100%" alt="anxkhn/JevPlaysPokemon screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Charlyhno-eng/jev-document-classification">Charlyhno-eng/jev-document-classification</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · Charlyhno-eng

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/charlyhno-eng--jev-document-classification/113bcf66f1648122.png" width="100%" alt="Charlyhno-eng/jev-document-classification screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/jev-review-action">fatwang2/jev-review-action</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · JavaScript · MIT · fatwang2

##### Dati

Stelle **1** · Fork 0 · Issue aperte 2 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.

</details>

<details>
<summary><b><a href="https://github.com/lbotinelly/jev-little-airways">lbotinelly/jev-little-airways</a></b> — ⭐1 · HTML · inferred · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · HTML · MIT · lbotinelly

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A show-and-tell capability study for Jev, TypeSafe's System One decision model.

</details>

<details>
<summary><b><a href="https://github.com/Red5d/jev-cvss">Red5d/jev-cvss</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · MIT · Red5d

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Fast CVSS scoring from vulnerability descriptions using Typesafe Jev

</details>

<details>
<summary><b><a href="https://github.com/solhosty/last-train-jev">solhosty/last-train-jev</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · solhosty

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

A small detective escape room built with TypeSafe Jev, React, and Express.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/solhosty/last-train-jev/main/docs/preview.png" width="100%" alt="solhosty/last-train-jev screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

<sub>Asset collegato direttamente dal repository upstream perché non è stata dichiarata alcuna licenza di ridistribuzione.</sub>

</details>

<details>
<summary><b><a href="https://github.com/sontakey/awesome-jev">sontakey/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · NOASSERTION · sontakey

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Unofficial list of insanely useful TypeSafe AI Jev / System One projects

</details>

<details>
<summary><b><a href="https://github.com/TanayPadar/gpt-vs-jev">TanayPadar/gpt-vs-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · TanayPadar

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Compare GPT generated language with JEV structured Noul decisions on the same input.

</details>

<details>
<summary><b><a href="https://github.com/tylerjharden/harden-jev-decides">tylerjharden/harden-jev-decides</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · tylerjharden

##### Dati

Stelle **1** · Fork 0 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.

</details>

<details>
<summary><b><a href="https://github.com/Z761293629/pi-jev-helm">Z761293629/pi-jev-helm</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · Z761293629

##### Dati

Stelle **1** · Fork 0 · Issue aperte 6 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/adhamelhayek-lab/jev-connector">adhamelhayek-lab/jev-connector</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · JavaScript · adhamelhayek-lab

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/afanjul/jev-llm">afanjul/jev-llm</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · afanjul

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Fake autoregressive language model powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/aoi-yoneda/haikyuBattleJev">aoi-yoneda/haikyuBattleJev</a></b> — HTML · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · HTML · aoi-yoneda

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev (TypeSafe AI) が打者を判断する配球バトル野球シミュレーション — 9回制・パワプロ風

</details>

<details>
<summary><b><a href="https://github.com/felixfisher/pi-jev-compaction">felixfisher/pi-jev-compaction</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · felixfisher

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Experimental Pi extension using TypeSafe Jev for auditable tool-history compaction

</details>

<details>
<summary><b><a href="https://github.com/havlan/jev-go">havlan/jev-go</a></b> — Go · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Go · MIT · havlan

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/heaven-hm/jev-system-one">heaven-hm/jev-system-one</a></b> — inferred · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · heaven-hm

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

</details>

<details>
<summary><b><a href="https://github.com/igormorais123/JEV">igormorais123/JEV</a></b> — inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · igormorais123

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Testes experimentais com o modelo de classificação JEV

</details>

<details>
<summary><b><a href="https://github.com/jsherman999/jev_local_web_seatch-">jsherman999/jev_local_web_seatch-</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · jsherman999

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-master">kevin9327/jev-master</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · MIT · kevin9327

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Typed System One decisions with Jev: Choice + Score + Noul composed in code.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevin9327--jev-master/cbf05c4561269075.png" width="100%" alt="kevin9327/jev-master screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kspviswa/chakravyuha-jev">kspviswa/chakravyuha-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · JavaScript · MIT · kspviswa

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kspviswa--chakravyuha-jev/4dfa22d0de9f27c1.png" width="100%" alt="kspviswa/chakravyuha-jev screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/lalitsonawane/jev-one-system">lalitsonawane/jev-one-system</a></b> — inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · lalitsonawane

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/LingXuanYin/jev-chat">LingXuanYin/jev-chat</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · NOASSERTION · LingXuanYin

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jev 聊天机：一个「只选不写」的聊天机——每个回复由逐词选择拼装，词典+分级索引+输入法式联想，由真实 Jev（TypeSafe System One）驱动。非官方实验，与 TypeSafe AI 无关联。

</details>

<details>
<summary><b><a href="https://github.com/lukevs/jev-at-home">lukevs/jev-at-home</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · lukevs

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Jev-like inference using open LLMs

</details>

<details>
<summary><b><a href="https://github.com/mashmalol/Vis-Jev-vibe">mashmalol/Vis-Jev-vibe</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · HTML · mashmalol

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/memorysaver/jev-atari-lab">memorysaver/jev-atari-lab</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · GPL-2.0 · memorysaver

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Challenge Atari with Jev: structured decisions, value questions, and replayable experiments

</details>

<details>
<summary><b><a href="https://github.com/nardinmarcus/pi-jev-typesafe">nardinmarcus/pi-jev-typesafe</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · nardinmarcus

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model discovery, and budget caps

</details>

<details>
<summary><b><a href="https://github.com/narulaskaran/jev-data-questions">narulaskaran/jev-data-questions</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · narulaskaran

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/nourhelmi/pi-jev-compaction">nourhelmi/pi-jev-compaction</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · nourhelmi

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Automatic Jev context clearing for Pi. Keep the conversation, prune stale tool output, retrieve originals without rerunning commands.

</details>

<details>
<summary><b><a href="https://github.com/rolottr/x-jev-classifier">rolottr/x-jev-classifier</a></b> — JavaScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · JavaScript · AGPL-3.0 · rolottr

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Chrome extension that stamps every X post with a type badge — alpha, shitpost, AI slop, bait — judged by Jev from Typesafe

</details>

<details>
<summary><b><a href="https://github.com/Sac-Y/Jev-cu">Sac-Y/Jev-cu</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · JavaScript · Sac-Y

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-context-curator">Shashank-H/pi-jev-context-curator</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · Shashank-H

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

A Jev based context curator for pi

</details>

<details>
<summary><b><a href="https://github.com/sub-surface/jev">sub-surface/jev</a></b> — inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · sub-surface

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/sueszli/qwen27b-jev">sueszli/qwen27b-jev</a></b> — inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · MIT · sueszli

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

multiple-choice questions for Qwen3.8-27B, read from logits

</details>

<details>
<summary><b><a href="https://github.com/swipswaps/jev-workspace">swipswaps/jev-workspace</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · swipswaps

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/TKY-27/JevSlop">TKY-27/JevSlop</a></b> — TypeScript · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · MIT · TKY-27

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Jevによるnote記事のAI Slop判定サイト

</details>

<details>
<summary><b><a href="https://github.com/TonyP-MR/jev-curation-engine">TonyP-MR/jev-curation-engine</a></b> — Python · inferred · 0 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · TonyP-MR

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions with existing LLM audit results.

</details>

<details>
<summary><b><a href="https://github.com/valentynkit/awesome-jev-typesafe">valentynkit/awesome-jev-typesafe</a></b> — inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · valentynkit

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/waschbaerwerkstatt-tech/jev-review-vorschau">waschbaerwerkstatt-tech/jev-review-vorschau</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · HTML · waschbaerwerkstatt-tech

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Passwortgeschützte Jev-Review-Auswertung; ausschließlich verschlüsselte HTML-Datei

</details>

<details>
<summary><b><a href="https://github.com/ximhear/jev-kr-name-age">ximhear/jev-kr-name-age</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · TypeScript · ximhear

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

이름으로 나이대를 맞히는 React 웹 (TypeSafe Jev)

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/ximhear/jev-kr-name-age/main/demo/name-age-demo.mp4"><img src="" width="100%" alt="ximhear/jev-kr-name-age video"></a><br><sub><a href="https://raw.githubusercontent.com/ximhear/jev-kr-name-age/main/demo/name-age-demo.mp4">Apri il video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/yogi-miraje/jev-lab">yogi-miraje/jev-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `inferred` · Python · yogi-miraje

##### Dati

Stelle **0** · Fork 0 · Issue aperte 0 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-19

##### Descrizione

Nessuna descrizione upstream è stata pubblicata.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/typesafe-adblock">realZachi/typesafe-adblock</a></b> — ⭐48 · JavaScript · unverified · 1 天 · ⭐+3</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `unverified` · JavaScript · MIT · realZachi

##### Dati

Stelle **48** (+3) · Fork 3 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.

</details>

<details>
<summary><b><a href="https://github.com/devanshbatham/commit-miner">devanshbatham/commit-miner</a></b> — ⭐21 · Rust · unverified · 1 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `unverified` · Rust · devanshbatham

##### Dati

Stelle **21** · Fork 5 · Issue aperte 0 · Creato 2026-09-17 · Ultimo push 2026-09-17 · Prima apparizione 2026-09-18

##### Descrizione

Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.

</details>

<details>
<summary><b><a href="https://github.com/razorback16/openjev">razorback16/openjev</a></b> — ⭐17 · Python · unverified · 0 天 · ⭐+4</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `unverified` · Python · Apache-2.0 · razorback16

##### Dati

Stelle **17** (+4) · Fork 2 · Issue aperte 1 · Creato 2026-09-18 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Open, Jev-compatible System One decision server on DiffusionGemma

</details>

<details>
<summary><b><a href="https://github.com/phyous/tsai-sc">phyous/tsai-sc</a></b> — ⭐13 · Python · unverified · 2 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `unverified` · Python · MIT · phyous

##### Dati

Stelle **13** · Fork 1 · Issue aperte 0 · Creato 2026-09-16 · Ultimo push 2026-09-16 · Prima apparizione 2026-09-18

##### Descrizione

TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.

<table><tr><th align="center" width="50%">Immagine</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/phyous--tsai-sc/f48a030ae92fb1fe.png" width="100%" alt="phyous/tsai-sc screenshot"></td>
<td align="center" valign="top"><sub>nessun media pubblicato</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andysc/IBM-Q-System-One-3D-model">andysc/IBM-Q-System-One-3D-model</a></b> — ⭐12 · OpenSCAD · unverified · 2688 天</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `unverified` · OpenSCAD · andysc

##### Dati

Stelle **12** · Fork 4 · Issue aperte 1 · Creato 2019-03-16 · Ultimo push 2019-05-10 · Prima apparizione 2026-09-18

##### Descrizione

3D-printed model of IBM Q System One

</details>

<details>
<summary><b><a href="https://github.com/zhengxuyu/litjev">zhengxuyu/litjev</a></b> — ⭐4 · Python · unverified · 0 天 · ⭐+1</summary>

##### Dati essenziali

`Articoli, discussioni e liste affini` · Comunità · `unverified` · Python · Apache-2.0 · zhengxuyu

##### Dati

Stelle **4** (+1) · Fork 1 · Issue aperte 3 · Creato 2026-09-17 · Ultimo push 2026-09-18 · Prima apparizione 2026-09-18

##### Descrizione

Turn any off-the-shelf LLM into a Jev -like decision layer

</details>

<a id="projects-by-implementation-language"></a>

## Progetti per linguaggio di implementazione

L'ecosistema è concentrato su Python e TypeScript, ma i client tipizzati continuano a comparire in altre lingue. Questa tabella è generata dalle voci stesse.

| Linguaggio | Voci | Esempi                                                                                             |
| ---------- | ---- | -------------------------------------------------------------------------------------------------- |
| Python     | 138  | `typesafe-ai/system-one-adapter-python`, `typesafe-ai/typesafe-sdk-python`, `MrJev/awesome-jev`    |
| TypeScript | 125  | `typesafe-ai/typesafe-sdk-js`, `AntonioCoppe/jev-harness`, `opaielsheikh/typesafe-migration-guard` |
| JavaScript | 58   | `ziyu/sytem-one-sdk`, `Ying-Kai-Liao/jev-browser`, `arunav25/jev-mcp`                              |
| Go         | 14   | `RadixILS-Dev/typesafe-sdk-go`, `Gaurav-Gosain/jev-go`, `Stumble/jev-go`                           |
| HTML       | 11   | `typesafe-ai/typesafe-ai.github.io`, `yzfly/awesome-jev-zh`, `vinilana/jev-eval-agent`             |
| Rust       | 11   | `AkashPriyadarshii/jev-curate`, `AkashPriyadarshii/jev-seo`, `AkashPriyadarshii/jev-scout`         |
| PHP        | 4    | `Butochnikov/laravel-typesafe-jev`, `mzainzulifqar/jev-php-sdk`, `shanginn/jev-php`                |
| Elixir     | 3    | `nshkrdotcom/typesafe_sdk`, `typesend/typesafe_ai`, `dannote/jev`                                  |
| Java       | 2    | `Premo-Cloud/typesafe-sdk-java`, `Olti1947/jev-java`                                               |
| Jupyter    | 2    | `jexp/neo4jev`, `bitnovus/jev-spam-eval`                                                           |
| Ruby       | 2    | `javiergradiche/ruby_llm-providers-typesafe`, `robzolkos/omarchy-issue-classifier`                 |
| Shell      | 2    | `wotai-dev/typesafe-jev-tools`, `JYeswak/jev_playground`                                           |
| C          | 1    | `giuliosmall/pg_typesafe`                                                                          |
| C#         | 1    | `saibimajdi/typesafeai-dotnet-sdk`                                                                 |
| CSS        | 1    | `AbdelStark/awesome-typesafe`                                                                      |
| Dart       | 1    | `Bud-ro/jev-demos`                                                                                 |
| Haskell    | 1    | `inanna-malick/jev-dsl`                                                                            |
| Kotlin     | 1    | `ufec/jev-block-android-ad`                                                                        |
| Lex        | 1    | `alpibrusl/lex-judge`                                                                              |
| OCaml      | 1    | `jonesmelton/verdict`                                                                              |
| OpenSCAD   | 1    | `andysc/IBM-Q-System-One-3D-model`                                                                 |
| PowerShell | 1    | `omni-/ask-jev`                                                                                    |
| Swift      | 1    | `pelazas/jev-cmdtab`                                                                               |
| TeX        | 1    | `dnakhoa/jev-deferred-crispification`                                                              |

<sub>Vengono conteggiate solo le voci che dichiarano un linguaggio. Le voci di infrastruttura, documentazione e discussione sono escluse da questa tabella.</sub>

## Come questo elenco resta aggiornato

Nessun essere umano modifica il corpo di questo README. Il repository esegue una pipeline in cinque fasi secondo una pianificazione e fa commit solo quando qualcosa è davvero cambiato.

<img src="assets/readme/pipeline.svg" width="100%" alt="Come questo elenco resta aggiornato">

|             |                                                                                                                                                                                                                                                                                                                |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **collect** | ricerca su GitHub attraverso una matrice di query, l'organizzazione ufficiale, la ricerca di codice di GitHub, Hacker News e l'hub Hugging Face.                                                                                                                                                               |
| **curate**  | deterministico e senza LLM, quindi due esecuzioni consecutive sullo stesso input producono un output identico byte per byte. Una regola a due segnali decide la rilevanza; le collisioni di nome (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD e simili) sono escluse da un elenco esplicito e verificabile. |
| **media**   | raccoglie gli screenshot e le registrazioni schermo di ciascun progetto. Gli asset vengono copiati in questo repository solo quando il progetto dichiara una licenza che consente la ridistribuzione; altrimenti l'URL upstream viene collegato direttamente e la scheda lo dichiara.                          |
| **render**  | produce ogni edizione linguistica da un unico template, così i venti README non possono divergere nella struttura.                                                                                                                                                                                             |
| **audit**   | fa fallire la build se a una voce manca un URL, se un link è morto, se due voci duplicano un URL o se un README si discosta dalla sua forma generata.                                                                                                                                                          |

## Come contribuire

Le correzioni sono benvenute e sono il modo più rapido per migliorare questo elenco. Aprite una issue o una pull request se una voce è archiviata o classificata male, o se un progetto è stato escluso per errore come collisione di nome: è proprio in quest'ultima categoria che i filtri automatici hanno più probabilità di sbagliare. Le aggiunte è meglio farle aggiungendo una fonte a `scripts/collect.py` invece di modificare il README, perché il README viene rigenerato a ogni ciclo.

---

<sub>Progetto comunitario indipendente. Non affiliato a TypeSafe AI, né approvato o revisionato da essa. Comportamento del prodotto, prezzi, limiti e alias dei modelli cambiano senza preavviso; verificate sulla documentazione ufficiale tutto ciò su cui fate affidamento. Gli asset restano proprietà dei rispettivi progetti upstream e vengono riprodotti solo dove una licenza lo consente.</sub>

<sub>Generato da · `render.py` · 2026-09-19T01:47:12+08:00</sub>
