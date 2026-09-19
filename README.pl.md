<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>Indeks Jev z oceną dowodów, który odbudowuje się co dwie godziny.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-488-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <b>Polski</b> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Indeks na żywo** · Ostatnia synchronizacja: `2026-09-19T10:20:34+08:00` (UTC+8)
> · Wpisy: **488** · Nowe w tym cyklu: **71** · Języki implementacji: **28**

<sub>Każdy wpis poniżej został zebrany, odfiltrowany i ponownie sprawdzony przez potok przetwarzania w tym repozytorium. Liczby i znaczniki czasu pochodzą ze źródeł, a nie z ręcznie napisanego zrzutu.</sub>

## Spis treści

- [Czym jest Jev?](#czym-jest-jev)
- [Jak oceniane są wpisy](#jak-oceniane-są-wpisy)
- [Oficjalne zestawy SDK i narzędzia dla programistów](#oficjalne-zestawy-sdk-i-narzędzia-dla-programistów) — **6**
- [Klienty, zestawy SDK i adaptery społeczności](#klienty-zestawy-sdk-i-adaptery-społeczności) — **74**
- [Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące](#narzędzia-dla-agentów-mcp-hooki-bramki-i-agenty-kodujące) — **144**
- [Routing, zabezpieczenia i zatwierdzenia](#routing-zabezpieczenia-i-zatwierdzenia) — **48**
- [Ewaluacja, kalibracja i benchmarki](#ewaluacja-kalibracja-i-benchmarki) — **39**
- [Otwarte reprodukcje, wagi i badania nad architekturą](#otwarte-reprodukcje-wagi-i-badania-nad-architekturą) — **19**
- [Aplikacje, gry, robotyka i interaktywne dema](#aplikacje-gry-robotyka-i-interaktywne-dema) — **42**
- [Teksty, dyskusje i pokrewne listy](#teksty-dyskusje-i-pokrewne-listy) — **116**
- [Projekty według języka implementacji](#projekty-według-języka-implementacji)
- [Jak ta lista pozostaje aktualna](#jak-ta-lista-pozostaje-aktualna)

## Czym jest Jev?

Jev to pierwszy **System One model** firmy TypeSafe AI. Nie pisze prozy. Przyjmuje stan oraz pytania, których przestrzeń odpowiedzi definiujesz z góry, i zwraca typowane wartości z rozkładami prawdopodobieństwa, na których Twój kod może rozgałęziać.

|                        |                                                                                                                                                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Kształt**            | `state + typed questions` → `constrained answers + probabilities` → `your code`                                                                                                                                                       |
| **Prymitywy**          | `Choice` (wybór jednej z ≤255 opcji), `Score` (skala ocen 2–10), `Noul` (probabilistyczne tak/nie)                                                                                                                                    |
| **Punkt końcowy**      | `POST https://api.typesafe.ai/v1/systemone`, model `jev-1.13.0` / alias `jev-latest`                                                                                                                                                  |
| **Dobre zastosowania** | routing, triage, scoring, moderacja, weryfikacja i bramki o niskim opóźnieniu w ograniczonym przepływie pracy                                                                                                                         |
| **Znane ograniczenia** | liczenie jest zawodne, wielopoziomowe pośrednictwo jest słabe, a materiały oficjalne wymieniają dziewięć klas nierównomierności. Wynik poprawny pod względem schematu to nie to samo co trafna decyzja — kalibruj na własnych danych. |

## Jak oceniane są wpisy

Większość list w tej dziedzinie twierdzi, że coś uwzględnia. Ta mówi, ile faktycznie zweryfikowała, i pozwala odpowiednio filtrować.

| Ocena        | Co to oznacza                                                                                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `official`   | Opublikowane przez samo TypeSafe AI.                                                                                                                                           |
| `observed`   | Publiczny artefakt, który można otworzyć i przeczytać — prawdziwy kod źródłowy, prawdziwa konfiguracja albo wyraźna deklaracja TypeSafe/Jev w nazwie lub temacie repozytorium. |
| `inferred`   | Dopasowane na podstawie niejednoznacznego sygnału i potwierdzającego słownictwa, ale jeszcze nieprzeczytane wiersz po wierszu.                                                 |
| `unverified` | Wygląda na powiązane, nic nie zostało niezależnie potwierdzone. Wymienione wyłącznie w celach odkrywania.                                                                      |

<a id="official-sdk"></a>

## Oficjalne zestawy SDK i narzędzia dla programistów

Wszystko, co publikuje sam TypeSafe. Zacznij tutaj.

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐285 · official · 6 天 · ⭐+24</summary>

##### Podstawowe informacje

`Oficjalne zestawy SDK i narzędzia dla programistów` · Oficjalny · `official` · MIT · typesafe-ai

##### Dane

Gwiazdki **285** (+24) · Forki 17 · Otwarte zgłoszenia 1 · Utworzono 2026-08-24 · Ostatni push 2026-09-12 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐134 · TypeScript · official · 3 天 · ⭐+6</summary>

##### Podstawowe informacje

`Oficjalne zestawy SDK i narzędzia dla programistów` · Oficjalny · `official` · TypeScript · MIT · typesafe-ai

##### Dane

Gwiazdki **134** (+6) · Forki 10 · Otwarte zgłoszenia 6 · Utworzono 2026-09-04 · Ostatni push 2026-09-15 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐124 · Python · official · 0 天 · ⭐+3</summary>

##### Podstawowe informacje

`Oficjalne zestawy SDK i narzędzia dla programistów` · Oficjalny · `official` · Python · MIT · typesafe-ai

##### Dane

Gwiazdki **124** (+3) · Forki 13 · Otwarte zgłoszenia 0 · Utworzono 2026-08-08 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>Znaleziono użycie w kodzie: `README.md`, `src/system_one_adapter/__init__.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐92 · Python · official · 0 天 · ⭐+8</summary>

##### Podstawowe informacje

`Oficjalne zestawy SDK i narzędzia dla programistów` · Oficjalny · `official` · Python · MIT · typesafe-ai

##### Dane

Gwiazdki **92** (+8) · Forki 9 · Otwarte zgłoszenia 2 · Utworzono 2026-09-04 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>Znaleziono użycie w kodzie: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 106 天</summary>

##### Podstawowe informacje

`Oficjalne zestawy SDK i narzędzia dla programistów` · Oficjalny · `official` · HTML · typesafe-ai

##### Dane

Gwiazdki **1** · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2024-05-28 · Ostatni push 2026-06-04 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/TypeSafeAI/clarity-judge">TypeSafeAI/clarity-judge</a></b> — ⭐1 · TypeScript · official · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Oficjalne zestawy SDK i narzędzia dla programistów` · Oficjalny · `official` · TypeScript · TypeSafeAI

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Multi-axis writing quality checker powered by TypeSafe AI's Jev model. Separate named checks, each with its own verdict and confidence.

</details>

<a id="community-sdk"></a>

## Klienty, zestawy SDK i adaptery społeczności

Typowane klienty dla punktu końcowego System One — w tylu językach, w ilu społeczność zdążyła je napisać.

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐20 · Jupyter · observed · 0 天 · ⭐+3</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Jupyter · MIT · jexp

##### Dane

Gwiazdki **20** (+3) · Forki 5 · Otwarte zgłoszenia 1 · Utworzono 2026-09-16 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐3 · Rust · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Rust · MIT · AkashPriyadarshii

##### Dane

Gwiazdki **3** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/ckaraca/awesome-jev">ckaraca/awesome-jev</a></b> — ⭐3 · Python · observed · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Python · CC0-1.0 · ckaraca

##### Dane

Gwiazdki **3** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A curated list of tools, integrations, and experiments built on Jev, TypeSafe AI's System One model for fast, typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — ⭐3 · Java · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Java · MIT · Premo-Cloud

##### Dane

Gwiazdki **3** · Forki 1 · Otwarte zgłoszenia 2 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · TypeScript · MIT · AntonioCoppe

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Python · CC0-1.0 · MrJev

##### Dane

Gwiazdki **2** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐2 · Elixir · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Elixir · MIT · nshkrdotcom

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · TypeScript · opaielsheikh

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Python · xingwudao

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · JavaScript · MIT · ziyu

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/gpazo/jev-vphone-cli">gpazo/jev-vphone-cli</a></b> — Swift · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Swift · MIT · gpazo

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Jev from Typesafe.ai + vphone-cli

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gpazo--jev-vphone-cli/baa413a8104308f4.jpg" width="100%" alt="gpazo/jev-vphone-cli screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Ruby · MIT · javiergradiche

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · TypeScript · MIT · nu-sync

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/RadixILS-Dev/typesafe-sdk-go">RadixILS-Dev/typesafe-sdk-go</a></b> — Go · observed · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Go · MIT · RadixILS-Dev

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A typesafe.ai client written in golang

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `observed` · Elixir · MIT · typesend

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐169 · Shell · inferred · 0 天 · ⭐+5</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Shell · NOASSERTION · realZachi

##### Dane

Gwiazdki **169** (+5) · Forki 10 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pinecone-io/cultivar">pinecone-io/cultivar</a></b> — ⭐39 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · pinecone-io

##### Dane

Gwiazdki **39** · Forki 2 · Otwarte zgłoszenia 5 · Utworzono 2026-06-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐32 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · nidhi-singh02

##### Dane

Gwiazdki **32** (+1) · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">Obejrzyj na img.youtube.com</a> · odtwarzanie otwiera się w witrynie hosta; GitHub nie może osadzić go bezpośrednio</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/tacticocc/Jevbridge">tacticocc/Jevbridge</a></b> — ⭐17 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · tacticocc

##### Dane

Gwiazdki **17** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tacticocc--jevbridge/772995670b3e42e9.png" width="100%" alt="tacticocc/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐14 · Python · inferred · 0 天 · ⭐+4</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · AboveColin

##### Dane

Gwiazdki **14** (+4) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Ask your house a question, get a number back. Home Assistant integration for TypeSafe Jev: typed answers as sensors, four actions for automations, and a conversation agent for Assist.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abovecolin--ha-jev/87fa9143f6990ef1.png" width="100%" alt="AboveColin/HA-Jev screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐13 · Elixir · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Elixir · MIT · dannote

##### Dane

Gwiazdki **13** (+1) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐13 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · shiftynick

##### Dane

Gwiazdki **13** · Forki 1 · Otwarte zgłoszenia 4 · Utworzono 2026-09-16 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shiftynick--jev-axi/e97a8238f41de3c1.gif" width="100%" alt="shiftynick/jev-axi screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shiftynick--jev-axi/e97a8238f41de3c1.gif" width="100%" alt="shiftynick/jev-axi animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐12 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · JavaScript · MIT · Ying-Kai-Liao

##### Dane

Gwiazdki **12** (+1) · Forki 3 · Otwarte zgłoszenia 3 · Utworzono 2026-09-16 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/keltokhy/jgrep">keltokhy/jgrep</a></b> — ⭐7 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · keltokhy

##### Dane

Gwiazdki **7** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.

</details>

<details>
<summary><b><a href="https://github.com/arunav25/jev-mcp">arunav25/jev-mcp</a></b> — ⭐5 · JavaScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · JavaScript · MIT · arunav25

##### Dane

Gwiazdki **5** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.

</details>

<details>
<summary><b><a href="https://github.com/Nasrallah-AL/jev-cli">Nasrallah-AL/jev-cli</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · Nasrallah-AL

##### Dane

Gwiazdki **5** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Command-line tool for TypeSafe's Jev AI model

</details>

<details>
<summary><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">saibimajdi/typesafeai-dotnet-sdk</a></b> — ⭐5 · C# · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · C# · MIT · saibimajdi

##### Dane

Gwiazdki **5** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-16 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/sharziki/semdecide">sharziki/semdecide</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · sharziki

##### Dane

Gwiazdki **5** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.

</details>

<details>
<summary><b><a href="https://github.com/frostney/clean-code-review">frostney/clean-code-review</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · frostney

##### Dane

Gwiazdki **4** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/frostney--clean-code-review/7d8a8de446e1c27b.png" width="100%" alt="frostney/clean-code-review screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rhighs/jev-code">rhighs/jev-code</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · rhighs

##### Dane

Gwiazdki **4** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/assets/jev-code-logo.png" width="100%" alt="rhighs/jev-code screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/docs/media/session.gif" width="100%" alt="rhighs/jev-code animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/romaluev/jev-ego">romaluev/jev-ego</a></b> — ⭐4 · TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · NOASSERTION · romaluev

##### Dane

Gwiazdki **4** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-seo">AkashPriyadarshii/jev-seo</a></b> — ⭐3 · Rust · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Rust · AkashPriyadarshii

##### Dane

Gwiazdki **3** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One

</details>

<details>
<summary><b><a href="https://github.com/docxology/daf-jev">docxology/daf-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · docxology

##### Dane

Gwiazdki **3** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill

</details>

<details>
<summary><b><a href="https://github.com/EugeneBoondock/jevsql">EugeneBoondock/jevsql</a></b> — ⭐3 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · JavaScript · MIT · EugeneBoondock

##### Dane

Gwiazdki **3** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

SQL with natural-language predicates, powered by TypeSafe's Jev. Filter, rank, classify and score rows by meaning — batched, cached and cost-guarded.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/eugeneboondock--jevsql/d6bbe6cf6a2d2e8c.png" width="100%" alt="EugeneBoondock/jevsql screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Olti1947/jev-java">Olti1947/jev-java</a></b> — ⭐3 · Java · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Java · Olti1947

##### Dane

Gwiazdki **3** · Forki 1 · Otwarte zgłoszenia 8 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Idiomatic Java SDK for TypeSafe AI Jev System One decision engine

</details>

<details>
<summary><b><a href="https://github.com/burnigtm/jev-mcp">burnigtm/jev-mcp</a></b> — ⭐2 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · burnigtm

##### Dane

Gwiazdki **2** (+1) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client

</details>

<details>
<summary><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Butochnikov/laravel-typesafe-jev</a></b> — ⭐2 · PHP · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · PHP · MIT · Butochnikov

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes.

</details>

<details>
<summary><b><a href="https://github.com/ddfeyes/jev-mode">ddfeyes/jev-mode</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · ddfeyes

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no deps, MIT.

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-go">Gaurav-Gosain/jev-go</a></b> — ⭐2 · Go · inferred · 2 天 · ⭐+1</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Go · MIT · Gaurav-Gosain

##### Dane

Gwiazdki **2** (+1) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/ibrahemid/git-jev-stage">ibrahemid/git-jev-stage</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · ibrahemid

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Select Git changes for staging with a plain-language description.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Stumble/jev-go">Stumble/jev-go</a></b> — ⭐2 · Go · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Go · MIT · Stumble

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Community Go SDK for TypeSafe AI Jev / System One

</details>

<details>
<summary><b><a href="https://github.com/tontoko/jev-browser">tontoko/jev-browser</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · JavaScript · Apache-2.0 · tontoko

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 3 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.

</details>

<details>
<summary><b><a href="https://github.com/tumf/jev-cli">tumf/jev-cli</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · tumf

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Small dependency-free CLI for TypeSafe Jev

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tumf--jev-cli/f90f005044872607.png" width="100%" alt="tumf/jev-cli screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tumf--jev-cli/f69b319352312892.gif" width="100%" alt="tumf/jev-cli animation"><br><sub>nagranie animowane · <a href="https://raw.githubusercontent.com/tumf/jev-cli/main/assets/jev-cli-terminal-demo.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/yzfly/awesome-jev-zh">yzfly/awesome-jev-zh</a></b> — ⭐2 · HTML · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · HTML · CC0-1.0 · yzfly

##### Dane

Gwiazdki **2** · Forki 3 · Otwarte zgłoszenia 3 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/jevclient">AboveColin/jevclient</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · AboveColin

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-scout">AkashPriyadarshii/jev-scout</a></b> — ⭐1 · Rust · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Rust · MIT · AkashPriyadarshii

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring

</details>

<details>
<summary><b><a href="https://github.com/anilsenay/jev">anilsenay/jev</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Go · MIT · anilsenay

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Unofficial Go client for TypeSafe's System One API  and its model, Jev.

</details>

<details>
<summary><b><a href="https://github.com/felpsdev/jev-classifier">felpsdev/jev-classifier</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · felpsdev

##### Dane

Gwiazdki **1** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/felpsdev--jev-classifier/d753de26b0e6c7b6.webp" width="100%" alt="felpsdev/jev-classifier screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gmaxxxie/jev-cli">gmaxxxie/jev-cli</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · gmaxxxie

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/himomohi/aside-jev">himomohi/aside-jev</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · himomohi

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.

</details>

<details>
<summary><b><a href="https://github.com/StefanoITA/ts-jev-cost-calculator">StefanoITA/ts-jev-cost-calculator</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · StefanoITA

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe.

</details>

<details>
<summary><b><a href="https://github.com/zhirschtritt/typesafe-go">zhirschtritt/typesafe-go</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Go · MIT · zhirschtritt

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Idiomatic Go SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/33Audits/jev-auto">33Audits/jev-auto</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · JavaScript · MIT · 33Audits

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Per-turn model routing for Claude Code. Cheapest tier that can do the job, no API key required, and it calibrates itself from what actually happened.

</details>

<details>
<summary><b><a href="https://github.com/acharyaanusha/magic-jev">acharyaanusha/magic-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · acharyaanusha

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A Magic Jev (8) Ball for pull requests.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/acharyaanusha--magic-jev/f58dfd5f54b0ae6c.gif" width="100%" alt="acharyaanusha/magic-jev animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">AkashPriyadarshii/jev-superpowers</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · JavaScript · MIT · AkashPriyadarshii

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions

</details>

<details>
<summary><b><a href="https://github.com/brnyxx/jev-ra">brnyxx/jev-ra</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · brnyxx

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 2 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7592fce4641d10.png" width="100%" alt="brnyxx/jev-ra screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7ddcd1053825a2.gif" width="100%" alt="brnyxx/jev-ra animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/david1gp/jev">david1gp/jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · david1gp

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Result-based TypeSafe System One client library and jev command-line interface.

</details>

<details>
<summary><b><a href="https://github.com/egma-ai/jev-reviewer">egma-ai/jev-reviewer</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · JavaScript · MIT · egma-ai

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Review behavior, not just diffs. Jev prioritizes human attention; OpenAI explains the changes. Local CLI + agent skill + GitHub extension.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/egma-ai--jev-reviewer/db97b1dd85958e4d.png" width="100%" alt="egma-ai/jev-reviewer screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/krw82/jev-playwright-mcp">krw82/jev-playwright-mcp</a></b> — TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · krw82

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.

</details>

<details>
<summary><b><a href="https://github.com/Kushwho/jev-codes">Kushwho/jev-codes</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · MIT · Kushwho

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Audit your git diff against YAML coding-standards packs using TypeSafe's Jev model, from a CLI or your AI agent's command/skill.

</details>

<details>
<summary><b><a href="https://github.com/lhotwll217/jev-cli">lhotwll217/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · TypeScript · lhotwll217

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

JSON-in, typed-decisions-out CLI for the TypeSafe System One API

</details>

<details>
<summary><b><a href="https://github.com/mhmdkzr/jev">mhmdkzr/jev</a></b> — Go · inferred · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Go · MIT · mhmdkzr

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

An unofficial Go client for TypeSafe's System One Jev model

</details>

<details>
<summary><b><a href="https://github.com/model-clis/jev">model-clis/jev</a></b> — Rust · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Rust · MIT · model-clis

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Typed judgment CLI for the Jev model (TypeSafe System One): state + questions in, calibrated answers and exit codes out

</details>

<details>
<summary><b><a href="https://github.com/nandansrikrishna/jev-agent-tool">nandansrikrishna/jev-agent-tool</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · MIT · nandansrikrishna

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Bring-your-own-key CLI, Python API, and MCP server for typed judgments with TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing">nekowasabi/jev-routing</a></b> — Go · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Go · MIT · nekowasabi

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.

</details>

<details>
<summary><b><a href="https://github.com/SAGAR-TAMANG/sarvam-jev">SAGAR-TAMANG/sarvam-jev</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Python · SAGAR-TAMANG

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Generation-free typed decisions on Indic LLMs. An open Jev-style inference engine on sarvam-1: constrained logit readout instead of autoregressive JSON. Runs client-side in the browser.

</details>

<details>
<summary><b><a href="https://github.com/yannip1234/codex-jev">yannip1234/codex-jev</a></b> — Rust · inferred · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `inferred` · Rust · Apache-2.0 · yannip1234

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 11 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Experimental Jev compression for Codex, with a macOS menu bar launcher, desktop bridge, and native client.

</details>

<details>
<summary><b><a href="https://github.com/giuliosmall/pg_typesafe">giuliosmall/pg_typesafe</a></b> — ⭐76 · C · unverified · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `unverified` · C · MIT · giuliosmall

##### Dane

Gwiazdki **76** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification

</details>

<details>
<summary><b><a href="https://github.com/pithings/advocaat">pithings/advocaat</a></b> — ⭐74 · TypeScript · unverified · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `unverified` · TypeScript · MIT · pithings

##### Dane

Gwiazdki **74** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/obie/ruby_decision_model">obie/ruby_decision_model</a></b> — ⭐34 · Ruby · unverified · 0 天 · ⭐+2</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `unverified` · Ruby · MIT · obie

##### Dane

Gwiazdki **34** (+2) · Forki 2 · Otwarte zgłoszenia 18 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Ruby client for decision models such as Typesafe Jev

</details>

<details>
<summary><b><a href="https://github.com/Brainwires/jevwire">Brainwires/jevwire</a></b> — ⭐5 · TypeScript · unverified · 0 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `unverified` · TypeScript · MIT · Brainwires

##### Dane

Gwiazdki **5** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/typesafe-cli">y0usaf/typesafe-cli</a></b> — ⭐4 · TypeScript · unverified · 2 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `unverified` · TypeScript · MIT · y0usaf

##### Dane

Gwiazdki **4** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose

</details>

<details>
<summary><b><a href="https://github.com/geilt/typesafe-cli">geilt/typesafe-cli</a></b> — ⭐3 · Python · unverified · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `unverified` · Python · geilt

##### Dane

Gwiazdki **3** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.

</details>

<details>
<summary><b><a href="https://github.com/gilljon/typesafe-ai-rs">gilljon/typesafe-ai-rs</a></b> — ⭐3 · Rust · unverified · 1 天</summary>

##### Podstawowe informacje

`Klienty, zestawy SDK i adaptery społeczności` · Społeczność · `unverified` · Rust · MIT · gilljon

##### Dane

Gwiazdki **3** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Independent async and blocking Rust SDK for the TypeSafe AI System One API

</details>

<a id="agent-tooling"></a>

## Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące

Najszybciej rosnąca kategoria: hooki, serwery MCP i bramki, które stawiają typowaną decyzję przed następnym działaniem agenta.

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐3310 · TypeScript · observed · 0 天 · ⭐+114</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · TypeScript · MIT · tamaratran

##### Dane

Gwiazdki **3310** (+114) · Forki 166 · Otwarte zgłoszenia 45 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>Znaleziono użycie w kodzie: `src/request.ts`, `README.md`, `src/client.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐144 · JavaScript · inferred · 0 天 · ⭐+6</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · gargpratyush

##### Dane

Gwiazdki **144** (+6) · Forki 5 · Otwarte zgłoszenia 5 · Utworzono 2026-09-16 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐46 · Python · inferred · 1 天 · ⭐+2</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · 0xNatoshi

##### Dane

Gwiazdki **46** (+2) · Forki 3 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐104 · observed · 1 天 · ⭐+1</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · dbreunig

##### Dane

Gwiazdki **104** (+1) · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐17 · Python · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · Python · MIT · GhalebDweikat

##### Dane

Gwiazdki **17** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/valentynkit/awesome-jev-typesafe">valentynkit/awesome-jev-typesafe</a></b> — ⭐8 · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · CC0-1.0 · valentynkit

##### Dane

Gwiazdki **8** · Forki 3 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Typed decisions with TypeSafe's Jev, the first System One model

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · Python · MIT · carlaiau

##### Dane

Gwiazdki **7** · Forki 1 · Otwarte zgłoszenia 6 · Utworzono 2026-03-13 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/kraayenjon/awesome-jev">kraayenjon/awesome-jev</a></b> — ⭐6 · observed · 0 天 · ⭐+2</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · NOASSERTION · kraayenjon

##### Dane

Gwiazdki **6** (+2) · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · Python · MIT · jodan-alberts

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/rajdhakad9826/routeKit">rajdhakad9826/routeKit</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · TypeScript · MIT · rajdhakad9826

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Agent-native LLM model router built with JEV by TypeSafe.ai. Dynamically selects the most suitable model based on task complexity, reasoning requirements, and tool usage.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · TypeScript · MIT · BYK

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/emirbartu/opencode-system-one">emirbartu/opencode-system-one</a></b> — ⭐1 · TypeScript · observed · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · TypeScript · emirbartu

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Opencode plugin using Jev (system one model) as part of software development process. Not affiliated with Opencode team.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · Python · MIT · 24601

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/codaaiteam/jev-typesafe-ai">codaaiteam/jev-typesafe-ai</a></b> — observed · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · codaaiteam

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Unofficial developer notes & examples for Jev, TypeSafe AI's System One model. Try it free: jevtypesafeai.com

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · TypeScript · CrowBe

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · TypeScript · MIT · gorock007

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/uipath-jev-guardrail-connector">jms-dcksn/uipath-jev-guardrail-connector</a></b> — JavaScript · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · JavaScript · jms-dcksn

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

UiPath bring-your-own-guardrail connector backed by the TypeSafe Jev System One model: plain-language agent policies enforced as calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/knowlet/jev-agentworld-web-simulator">knowlet/jev-agentworld-web-simulator</a></b> — TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · TypeScript · MIT · knowlet

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

An entire internet — search, pages & links — hallucinated on the fly by the System One Model.

</details>

<details>
<summary><b><a href="https://github.com/Wany-i/jev-decision-layer">Wany-i/jev-decision-layer</a></b> — Python · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · Python · MIT · Wany-i

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

把决策模型（typesafe/jev-1.13，经 OpenRouter 的 decisions 端点调用）封装成业务决策工具：注册表驱动，带置信度门控与硬约束。非官方项目。

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `observed` · Python · MIT · yousudip

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐275 · TypeScript · inferred · 2 天 · ⭐+8</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · devagrawal09

##### Dane

Gwiazdki **275** (+8) · Forki 14 · Otwarte zgłoszenia 1 · Utworzono 2026-09-16 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐123 · TypeScript · inferred · 1 天 · ⭐+4</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · NiazMorshed2007

##### Dane

Gwiazdki **123** (+4) · Forki 9 · Otwarte zgłoszenia 2 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐120 · JavaScript · inferred · 0 天 · ⭐+11</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · fatwang2

##### Dane

Gwiazdki **120** (+11) · Forki 14 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/wy-coliney/jev-browser-use">wy-coliney/jev-browser-use</a></b> — ⭐109 · JavaScript · inferred · 0 天 · ⭐+15</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · wy-coliney

##### Dane

Gwiazdki **109** (+15) · Forki 4 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wy-coliney--jev-browser-use/581fbd89fe47c952.png" width="100%" alt="wy-coliney/jev-browser-use screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-eval-agent">vinilana/jev-eval-agent</a></b> — ⭐86 · HTML · inferred · 1 天 · ⭐+2</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · HTML · vinilana

##### Dane

Gwiazdki **86** (+2) · Forki 8 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-mcp">jkudish/jev-mcp</a></b> — ⭐73 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · jkudish

##### Dane

Gwiazdki **73** · Forki 10 · Otwarte zgłoszenia 2 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools.

> An early proof of concept for exposing Jev over MCP, which is how most non-Python toolchains reach it.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/pi-jev">y0usaf/pi-jev</a></b> — ⭐68 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · y0usaf

##### Dane

Gwiazdki **68** (+1) · Forki 3 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers

</details>

<details>
<summary><b><a href="https://github.com/RomanSlack/jev-drone">RomanSlack/jev-drone</a></b> — ⭐63 · Python · inferred · 2 天 · ⭐+2</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · RomanSlack

##### Dane

Gwiazdki **63** (+2) · Forki 3 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/romanslack--jev-drone/b23ea2412f437970.png" width="100%" alt="RomanSlack/jev-drone screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/supercorp-ai/supercov">supercorp-ai/supercov</a></b> — ⭐35 · Rust · inferred · 0 天 · ⭐+2</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Rust · MIT · supercorp-ai

##### Dane

Gwiazdki **35** (+2) · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-08-23 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Code quality and coverage for coding agents

> Code quality and coverage verdicts produced as typed decisions rather than prose, so the result can gate a pipeline directly.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/supercorp-ai--supercov/063226e150cb8a6b.jpg" width="100%" alt="supercorp-ai/supercov screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/logicrw/awesome-jev-projects">logicrw/awesome-jev-projects</a></b> — ⭐33 · JavaScript · inferred · 0 天 · ⭐+4</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · logicrw

##### Dane

Gwiazdki **33** (+4) · Forki 8 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/ask-jev-skill">shantanugoel/ask-jev-skill</a></b> — ⭐30 · Python · inferred · 1 天 · ⭐+1</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · shantanugoel

##### Dane

Gwiazdki **30** (+1) · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Skill for Hermes, and other agents, to ask typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/tamaratran/jev-pruner">tamaratran/jev-pruner</a></b> — ⭐15 · TypeScript · inferred · 0 天 · ⭐+5</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · tamaratran

##### Dane

Gwiazdki **15** (+5) · Forki 1 · Otwarte zgłoszenia 7 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Claude Code plugin: trim long Bash output with TypeSafe Jev before the model sees it

</details>

<details>
<summary><b><a href="https://github.com/DanRWilloughby/snifftest">DanRWilloughby/snifftest</a></b> — ⭐14 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · DanRWilloughby

##### Dane

Gwiazdki **14** · Forki 0 · Otwarte zgłoszenia 3 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/TheoOliveira/pi-jev">TheoOliveira/pi-jev</a></b> — ⭐14 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · TheoOliveira

##### Dane

Gwiazdki **14** (+1) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/kbhuw/jev-sift">kbhuw/jev-sift</a></b> — ⭐13 · JavaScript · inferred · 0 天 · ⭐+9</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · kbhuw

##### Dane

Gwiazdki **13** (+9) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification.

</details>

<details>
<summary><b><a href="https://github.com/compozy/yoshi">compozy/yoshi</a></b> — ⭐12 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · compozy

##### Dane

Gwiazdki **12** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/compozy--yoshi/637d8588c227f4de.png" width="100%" alt="compozy/yoshi screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">jomatsu/pi-jev-auto-mode</a></b> — ⭐12 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · jomatsu

##### Dane

Gwiazdki **12** (+1) · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.

</details>

<details>
<summary><b><a href="https://github.com/BillionsBobby/JevRouter">BillionsBobby/JevRouter</a></b> — ⭐11 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · BillionsBobby

##### Dane

Gwiazdki **11** (+4) · Forki 1 · Otwarte zgłoszenia 4 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A lightweight Jev-powered router for models, tools, and subagents

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/billionsbobby--jevrouter/f0e638219505d5da.png" width="100%" alt="BillionsBobby/JevRouter screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/blakestone-x/jev-mcp">blakestone-x/jev-mcp</a></b> — ⭐9 · Python · inferred · 2 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · blakestone-x

##### Dane

Gwiazdki **9** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer

</details>

<details>
<summary><b><a href="https://github.com/huntedman/JevLint">huntedman/JevLint</a></b> — ⭐9 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · huntedman

##### Dane

Gwiazdki **9** (+1) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.

</details>

<details>
<summary><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">DECRUX9812/typesafe-skill-router</a></b> — ⭐7 · Python · inferred · 2 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · DECRUX9812

##### Dane

Gwiazdki **7** · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-code">devagrawal09/jev-code</a></b> — ⭐6 · TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · devagrawal09

##### Dane

Gwiazdki **6** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Bounded TypeSafe Jev workflows for coding agents.

</details>

<details>
<summary><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">GodsBoy/jev-agent-skill-router</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · GodsBoy

##### Dane

Gwiazdki **5** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typed, confidence-aware agent skill routing with TypeSafe Jev.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/godsboy--jev-agent-skill-router/c80293e37dcd4faf.png" width="100%" alt="GodsBoy/jev-agent-skill-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/inanna-malick/jev-dsl">inanna-malick/jev-dsl</a></b> — ⭐5 · Haskell · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Haskell · MIT · inanna-malick

##### Dane

Gwiazdki **5** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels

</details>

<details>
<summary><b><a href="https://github.com/matthewp/flue-jev-demo">matthewp/flue-jev-demo</a></b> — ⭐5 · TypeScript · inferred · 0 天 · ⭐+3</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · matthewp

##### Dane

Gwiazdki **5** (+3) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Flue agent routing with TypeSafe Jev through Cloudflare AI Gateway

</details>

<details>
<summary><b><a href="https://github.com/anpicasso/hermes-jev-approvals">anpicasso/hermes-jev-approvals</a></b> — ⭐4 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · anpicasso

##### Dane

Gwiazdki **4** · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only.

</details>

<details>
<summary><b><a href="https://github.com/GiesN/typesafe-jev-workflow">GiesN/typesafe-jev-workflow</a></b> — ⭐4 · Python · inferred · 2 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · GiesN

##### Dane

Gwiazdki **4** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/runta-dev/jot">runta-dev/jot</a></b> — ⭐4 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · runta-dev

##### Dane

Gwiazdki **4** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

The first general-purpose System One agent for Jev

</details>

<details>
<summary><b><a href="https://github.com/anandi1989/awesome-jev-usecases">anandi1989/awesome-jev-usecases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · MIT · anandi1989

##### Dane

Gwiazdki **3** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-mcp">rashedInt32/jev-mcp</a></b> — ⭐3 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · rashedInt32

##### Dane

Gwiazdki **3** (+1) · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/SeeAPI/awesome-jev-use-cases">SeeAPI/awesome-jev-use-cases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · CC-BY-4.0 · SeeAPI

##### Dane

Gwiazdki **3** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-align">caiovicentino/jev-align</a></b> — ⭐2 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · caiovicentino

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Calibrated alignment verifier for LLM responses and agent plans — powered by Jev

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-shield">caiovicentino/jev-shield</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · caiovicentino

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check.

</details>

<details>
<summary><b><a href="https://github.com/doeixd/jev-pref">doeixd/jev-pref</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · doeixd

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-model-router-demo">jcpsimmons/jev-model-router-demo</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · jcpsimmons

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

</details>

<details>
<summary><b><a href="https://github.com/molis-ai/jev-workbench">molis-ai/jev-workbench</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · molis-ai

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/molis-ai--jev-workbench/00f61d8403a941cd.png" width="100%" alt="molis-ai/jev-workbench screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MongLong0214/jev-gate">MongLong0214/jev-gate</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MongLong0214

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 5 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.

</details>

<details>
<summary><b><a href="https://github.com/morcoan/JevSeek">morcoan/JevSeek</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · morcoan

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools, persistent sessions, React desktop, and documented research.

</details>

<details>
<summary><b><a href="https://github.com/noetion/dsh-jev">noetion/dsh-jev</a></b> — ⭐2 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · noetion

##### Dane

Gwiazdki **2** (+1) · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.

</details>

<details>
<summary><b><a href="https://github.com/ranjan2829/AskJev">ranjan2829/AskJev</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · ranjan2829

##### Dane

Gwiazdki **2** · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)

</details>

<details>
<summary><b><a href="https://github.com/samtay32/jev-system-architect">samtay32/jev-system-architect</a></b> — ⭐2 · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · MIT · samtay32

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives.

</details>

<details>
<summary><b><a href="https://github.com/Zaious/jev-capability-atlas">Zaious/jev-capability-atlas</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · NOASSERTION · Zaious

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。

</details>

<details>
<summary><b><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher">abhishekashokvkumar/jev-mcp-dispatcher</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · abhishekashokvkumar

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Natural-language MCP tool dispatcher powered entirely by TypeSafe's Jev — no general-purpose LLM. Discovers a simple MCP server's tool signatures at runtime and uses Jev's typed primitives (Choice/Noul) to pick the right tool and extract its arguments straight out of the sentence.

</details>

<details>
<summary><b><a href="https://github.com/bestagentkits/jev-skillful">bestagentkits/jev-skillful</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · bestagentkits

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.

</details>

<details>
<summary><b><a href="https://github.com/cephalization/jev-oxlint">cephalization/jev-oxlint</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · cephalization

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Digest your skills into oxlint rules powered by jev

</details>

<details>
<summary><b><a href="https://github.com/CrowdLinker/JevPromptCoach">CrowdLinker/JevPromptCoach</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · CrowdLinker

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Claude Code plugin that scores how well you prompt a coding agent, and shows whether your habits are improving. Runs on TypeSafe's Jev model. Zero added latency.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/crowdlinker--jevpromptcoach/5340815130cd47ba.png" width="100%" alt="CrowdLinker/JevPromptCoach screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Dharundp6/jev-carryforward">Dharundp6/jev-carryforward</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · Dharundp6

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written as things happen, recalled per task with TypeSafe's Jev evaluation model via Vercel AI Gateway.

</details>

<details>
<summary><b><a href="https://github.com/Friedjof/jev-mobile">Friedjof/jev-mobile</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · Friedjof

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Fast structured Android control loops with TypeSafe Jev and Mobile MCP

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-starter">hamakyo/jev-starter</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · hamakyo

##### Dane

Gwiazdki **1** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-codex-plugin">integrate-your-mind/jev-codex-plugin</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · integrate-your-mind

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Open-source Codex plugin for TypeSafe Jev decision consultation, failure diagnosis, and evidence-based completion review

</details>

<details>
<summary><b><a href="https://github.com/jcressler/fast-jev-compaction-codex">jcressler/fast-jev-compaction-codex</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · jcressler

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Task-aware Jev evidence selection and exact local recovery around native Codex compaction.

</details>

<details>
<summary><b><a href="https://github.com/khordoo/jev-reflex-autonomy-lab">khordoo/jev-reflex-autonomy-lab</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · khordoo

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/khordoo/jev-reflex-autonomy-lab/main/docs/media/reflex-dashboard.png" width="100%" alt="khordoo/jev-reflex-autonomy-lab screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/omni-/ask-jev">omni-/ask-jev</a></b> — ⭐1 · PowerShell · inferred · 2 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · PowerShell · MIT · omni-

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions.

</details>

<details>
<summary><b><a href="https://github.com/poponline63/hermes-jev-north-star">poponline63/hermes-jev-north-star</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · poponline63

##### Dane

Gwiazdki **1** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven.

</details>

<details>
<summary><b><a href="https://github.com/RahulBalakavi/claude-code-jev">RahulBalakavi/claude-code-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · RahulBalakavi

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Experimental Jev permission gate for Claude Code via OpenRouter, with reproducible latency and cost benchmarks

</details>

<details>
<summary><b><a href="https://github.com/Ravinder82/jev-flash-router">Ravinder82/jev-flash-router</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · Ravinder82

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code

</details>

<details>
<summary><b><a href="https://github.com/rthomas24/jev-realtime-trading">rthomas24/jev-realtime-trading</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · rthomas24

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rthomas24--jev-realtime-trading/f27df5cca6b8e2cf.png" width="100%" alt="rthomas24/jev-realtime-trading screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Saik0s/diffusiongemma-jev-macos">Saik0s/diffusiongemma-jev-macos</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · Saik0s

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Local JEV-style decisions with DiffusionGemma on Apple Silicon, with benchmarks and coding-agent examples.

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/codex-jev-compaction">Wang-auspicious/codex-jev-compaction</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · Wang-auspicious

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills.

</details>

<details>
<summary><b><a href="https://github.com/wotai-dev/typesafe-jev-tools">wotai-dev/typesafe-jev-tools</a></b> — ⭐1 · Shell · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Shell · MIT · wotai-dev

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 149-row comparison of TypeSafe Jev against Claude Haiku 4.5.

</details>

<details>
<summary><b><a href="https://github.com/altregubov/jev-antigravity-mcp">altregubov/jev-antigravity-mcp</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · altregubov

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/alviso/jev-precheck">alviso/jev-precheck</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · alviso

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A second signature on every write an AI agent makes into a system of record. MCP proxy: fetch the records, derive in code, Jev judges. 98.6% recall, 0 false holds on 288 cases.

</details>

<details>
<summary><b><a href="https://github.com/andyholst/hermes-typesafe-jev">andyholst/hermes-typesafe-jev</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · NOASSERTION · andyholst

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 6 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

TypeSafe Jev MCP server for Hermes Agent — Choice, Noul, Score as first-class tools

</details>

<details>
<summary><b><a href="https://github.com/anisselbd/jev-phishing-bench">anisselbd/jev-phishing-bench</a></b> — Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · anisselbd

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/openclaw-jev-harness">AntonioCoppe/openclaw-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · AntonioCoppe

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

OpenClaw plugin: jev-harness DecisionHarness as System One decide layer (policy/confidence/shadow)

</details>

<details>
<summary><b><a href="https://github.com/AStheTECH/mewcp-jev">AStheTECH/mewcp-jev</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · Apache-2.0 · AStheTECH

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

JEV MCP server by MewCP

</details>

<details>
<summary><b><a href="https://github.com/bidurkhatri/jev-mcp-lab">bidurkhatri/jev-mcp-lab</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · Apache-2.0 · bidurkhatri

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/buberlo/dsh-jev">buberlo/dsh-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · buberlo

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Jev-powered decision layer for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/cbruyndoncx/AskJev-MCP">cbruyndoncx/AskJev-MCP</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · cbruyndoncx

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence

</details>

<details>
<summary><b><a href="https://github.com/de-niji/jev-hermes">de-niji/jev-hermes</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · de-niji

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Jev for Hermes: cheap intent gates + verbatim tool compaction on OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/dizk/pi-jev-lens">dizk/pi-jev-lens</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · dizk

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

pi extension that compresses large tool results before they reach the model: jev picks the view, full text stays recallable

</details>

<details>
<summary><b><a href="https://github.com/DoGMaTiiC/hermes-jev">DoGMaTiiC/hermes-jev</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · DoGMaTiiC

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 7 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only.

</details>

<details>
<summary><b><a href="https://github.com/droid-Q/jev-skill-router">droid-Q/jev-skill-router</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · droid-Q

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/droid-Q/jev-skill-router/main/docs/images/dashboard-en.png" width="100%" alt="droid-Q/jev-skill-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/duketopceo/jev-compact">duketopceo/jev-compact</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · duketopceo

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP

</details>

<details>
<summary><b><a href="https://github.com/EtienneLescot/jev-router">EtienneLescot/jev-router</a></b> — HTML · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · HTML · MIT · EtienneLescot

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model tier and reasoning depth.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/etiennelescot--jev-router/96217fad0b128b3e.png" width="100%" alt="EtienneLescot/jev-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fast-facts/jev-mcp">fast-facts/jev-mcp</a></b> — Go · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Go · MIT · fast-facts

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/flaviusapop/jev-router">flaviusapop/jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · flaviusapop

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Routes each turn in Claude Code, Codex, Grok and opencode to the cheapest model and reasoning depth that can finish it, using TypeSafe Jev

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/flaviusapop--jev-router/b7f868696d35b78b.png" width="100%" alt="flaviusapop/jev-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gzawadzki/jev-usecases">gzawadzki/jev-usecases</a></b> — Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · gzawadzki

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage

</details>

<details>
<summary><b><a href="https://github.com/hangarbay/jev.mcp">hangarbay/jev.mcp</a></b> — Go · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Go · MIT · hangarbay

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/its-panzer/jev-model-router">its-panzer/jev-model-router</a></b> — Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · its-panzer

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A policy router that picks the cheapest Claude model that can finish the job

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/its-panzer--jev-model-router/98819f5aaf8e6373.png" width="100%" alt="its-panzer/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jh1373/jev-search">jh1373/jev-search</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · jh1373

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Search your Obsidian vault locally and offline with no API key, then rerank the top results with Jev only after you approve exactly what gets sent. Experimental preview.

</details>

<details>
<summary><b><a href="https://github.com/jmanhype/jev-dspy-lab">jmanhype/jev-dspy-lab</a></b> — Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · jmanhype

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/jev-pii-guardrail">jms-dcksn/jev-pii-guardrail</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · jms-dcksn

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A UiPath coded agent with a custom PII detection guardrail on the LLM boundary, built on the TypeSafe Jev model as a LangChain awrap_model_call middleware.

</details>

<details>
<summary><b><a href="https://github.com/JoacoMarc/jev-harness-router">JoacoMarc/jev-harness-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · JoacoMarc

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Per-turn harness router on Jev (TypeSafe): one batched call picks the model tier, tools, skill and effort budget for an agent turn, behind a hard latency deadline.

</details>

<details>
<summary><b><a href="https://github.com/juanlentino/jev-connector">juanlentino/jev-connector</a></b> — PHP · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · PHP · GPL-2.0 · juanlentino

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

WordPress connector for the TypeSafe System One API (Jev): typed questions, confidence-scored answers, core Connectors API key management

</details>

<details>
<summary><b><a href="https://github.com/jxu-dev-c/jev-adaptive-thinking">jxu-dev-c/jev-adaptive-thinking</a></b> — Go · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Go · jxu-dev-c

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

CLIProxyAPI plugin for Jev-powered session model routing with local debug logs

</details>

<details>
<summary><b><a href="https://github.com/kaijia323/dsh-plugin-jev">kaijia323/dsh-plugin-jev</a></b> — HTML · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · HTML · MIT · kaijia323

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/kerpopule/hermes-jev-skills">kerpopule/hermes-jev-skills</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · kerpopule

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (also Claude Code and Codex)

</details>

<details>
<summary><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">MahmoudAdelbghany/jev-browser</a></b> — JavaScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MahmoudAdelbghany

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included.

</details>

<details>
<summary><b><a href="https://github.com/Mandrilsquad1441/jev-model-router">Mandrilsquad1441/jev-model-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · Mandrilsquad1441

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Pick the best AI model and reasoning effort for any task in ~1s. Plugin for Claude Code, Claude Desktop and Codex, powered by TypeSafe's Jev decision model and live OpenRouter pricing. Balance intelligence, speed and cost, or choose your priority.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mandrilsquad1441--jev-model-router/6187e7fb04b04c08.png" width="100%" alt="Mandrilsquad1441/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/marcAllari/jev-mcp-router">marcAllari/jev-mcp-router</a></b> — inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · marcAllari

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/micic-mihajlo/jev-tool-runner">micic-mihajlo/jev-tool-runner</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · micic-mihajlo

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/minhgv/jev-mcp">minhgv/jev-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · minhgv

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe Jev MCP decision layer for coding agents and CI

</details>

<details>
<summary><b><a href="https://github.com/mjyoke1111/jev-agent-safety-arena">mjyoke1111/jev-agent-safety-arena</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · mjyoke1111

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Real browser-agent safety evaluation: Jev versus a baseline on benign and injected tasks

</details>

<details>
<summary><b><a href="https://github.com/MSalvalaggio/jev-reflex">MSalvalaggio/jev-reflex</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · MSalvalaggio

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision).

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-mcp">nekowasabi/jev-routing-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · nekowasabi

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/Nyarlathoteppppp/pi-jev-context">Nyarlathoteppppp/pi-jev-context</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · Nyarlathoteppppp

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Cache-neutral context trimming for the pi coding agent, powered by TypeSafe Jev: long tool output cut to verbatim key lines before it enters context, with lossless recall. Measured, with pre-registered benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Panebianco00/jev-claude">Panebianco00/jev-claude</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · Panebianco00

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Route Claude Code's coding decisions through TypeSafe Jev: typed choices with probabilities, enforced at plan approval, questions, and risky commands.

</details>

<details>
<summary><b><a href="https://github.com/pedroknigge/mcp_jev">pedroknigge/mcp_jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · pedroknigge

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 3 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Open MCP server to run TypeSafe Jev (System One) packs locally — Choice / Noul / Score for Cursor & agents

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-mcp-router">Pinutss/jev-mcp-router</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · Pinutss

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Select relevant MCP tools under a context-token budget, without executing them.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-mcp-router/3947a2a5cc3750c8.png" width="100%" alt="Pinutss/jev-mcp-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-memory-selector">Pinutss/jev-memory-selector</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · Pinutss

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-plugins">Pinutss/jev-plugins</a></b> — inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · MIT · Pinutss

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Cursor and Hermes marketplace for the four published JEV Labs routers.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-plugins/b3fcd72ac9e61f49.jpg" width="100%" alt="Pinutss/jev-plugins screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/planstack-ai/jev-tetris-benchmark">planstack-ai/jev-tetris-benchmark</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · planstack-ai

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Reproducible Tetris decision benchmark comparing TypeSafe Jev with Claude Haiku

</details>

<details>
<summary><b><a href="https://github.com/raj8525/universal-jev">raj8525/universal-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · raj8525

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents

</details>

<details>
<summary><b><a href="https://github.com/robbyczgw-cla/hermes-plugin-jev">robbyczgw-cla/hermes-plugin-jev</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · robbyczgw-cla

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

TypeSafe/Jev decision signals for Hermes: turn classification, conservative tool shaping, approvals, and coding verification.

</details>

<details>
<summary><b><a href="https://github.com/rubichandrap/hermes-jev-guard">rubichandrap/hermes-jev-guard</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · rubichandrap

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check

</details>

<details>
<summary><b><a href="https://github.com/sebastianbugal/jev">sebastianbugal/jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · sebastianbugal

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

TypeSafe's Jev decision model in Claude Code. Ask in plain language, get a typed answer with a calibrated probability.

</details>

<details>
<summary><b><a href="https://github.com/skeptrunedev/jev-recruiter">skeptrunedev/jev-recruiter</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · skeptrunedev

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A Jev powered LinkedIn recruiting agent. Watch it browse relevant profiles, save links, and review evidence against your hiring brief.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/skeptrunedev--jev-recruiter/d87f759cfd3422af.png" width="100%" alt="skeptrunedev/jev-recruiter screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/stoopid-computers/jev-bot">stoopid-computers/jev-bot</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · stoopid-computers

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Computer Use Agent developed with Jev

</details>

<details>
<summary><b><a href="https://github.com/sypherin/jev-trace-classifier">sypherin/jev-trace-classifier</a></b> — Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · sypherin

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next

</details>

<details>
<summary><b><a href="https://github.com/tgiridhar/claude-code-jev-smart-router">tgiridhar/claude-code-jev-smart-router</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · tgiridhar

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task phase and the cost of an undetected error, gated by prompt-cache arithmetic. Proof of concept.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tgiridhar--claude-code-jev-smart-router/28b9e1b2a005c7e2.png" width="100%" alt="tgiridhar/claude-code-jev-smart-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/thanh-abaii/ud-jev-decision-workflow">thanh-abaii/ud-jev-decision-workflow</a></b> — inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · MIT · thanh-abaii

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/themsquared/jev-benchmark">themsquared/jev-benchmark</a></b> — Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · Apache-2.0 · themsquared

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.

</details>

<details>
<summary><b><a href="https://github.com/thevibeworks/awesome-typesafe-jev">thevibeworks/awesome-typesafe-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · NOASSERTION · thevibeworks

##### Dane

Gwiazdki **0** · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/thumay9700/jev-plays">thumay9700/jev-plays</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · thumay9700

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Autonomous game agent powered by TypeSafe AI's Jev (System One decision engine), starting with Pokémon Red.

</details>

<details>
<summary><b><a href="https://github.com/trietphan/jev-claw">trietphan/jev-claw</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · trietphan

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Typed model routing for OpenClaw agents, powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/ussyverse/hermes-jev-router">ussyverse/hermes-jev-router</a></b> — Python · inferred · 2 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · ussyverse

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-gateway-bench">vinilana/jev-gateway-bench</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · MIT · vinilana

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Benchmark for jev-gateway: real coding agents on chess engine tasks, with Jev routing on and off

</details>

<details>
<summary><b><a href="https://github.com/yangzhou-chaofan/awesome-jev-prompt">yangzhou-chaofan/awesome-jev-prompt</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · JavaScript · CC0-1.0 · yangzhou-chaofan

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

latest top 100 showcases for jev (keep updating) from x / github / latest sources

</details>

<details>
<summary><b><a href="https://github.com/zbloss/jev-plays-pokemon">zbloss/jev-plays-pokemon</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · Python · MIT · zbloss

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 3 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Like Claude Plays Pokemon, but with Jev

</details>

<details>
<summary><b><a href="https://github.com/zhangxaochen/dsh-jev">zhangxaochen/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `inferred` · TypeScript · MIT · zhangxaochen

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev (System One decision model) plugin suite for DeepSeek Harness (dsh)

</details>

<details>
<summary><b><a href="https://github.com/DevMortimer/pi-warden">DevMortimer/pi-warden</a></b> — ⭐64 · TypeScript · unverified · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `unverified` · TypeScript · MIT · DevMortimer

##### Dane

Gwiazdki **64** (+1) · Forki 5 · Otwarte zgłoszenia 3 · Utworzono 2026-09-16 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop

> Guardrails that steer an agent before it acts. Demonstrates the gate pattern, where the decision is cheap enough to run on every step.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devmortimer--pi-warden/b8dc20ac6694613a.png" width="100%" alt="DevMortimer/pi-warden screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/pi-quiet-ask">HyunjunJeon/pi-quiet-ask</a></b> — ⭐5 · TypeScript · unverified · 1 天 · ⭐+2</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `unverified` · TypeScript · MIT · HyunjunJeon

##### Dane

Gwiazdki **5** (+2) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe Jev as the pi coding agent's quiet decision layer

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hyunjunjeon--pi-quiet-ask/7ee3a99430e853d8.png" width="100%" alt="HyunjunJeon/pi-quiet-ask screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/3clyp50/a0-typesafe-ai">3clyp50/a0-typesafe-ai</a></b> — ⭐4 · Python · unverified · 2 天</summary>

##### Podstawowe informacje

`Narzędzia dla agentów: MCP, hooki, bramki i agenty kodujące` · Społeczność · `unverified` · Python · MIT · 3clyp50

##### Dane

Gwiazdki **4** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/3clyp50--a0-typesafe-ai/9aa8ea4ef8241f14.png" width="100%" alt="3clyp50/a0-typesafe-ai screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<a id="routing-guardrails"></a>

## Routing, zabezpieczenia i zatwierdzenia

Zastosowanie w kształcie produkcyjnym — kieruj każde żądanie do najtańszego modelu, który faktycznie sobie poradzi, i utrzymuj deterministyczną kontrolę wyniku.

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐49 · Rust · observed · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `observed` · Rust · NOASSERTION · Dicklesworthstone

##### Dane

Gwiazdki **49** (+1) · Forki 5 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 2 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `observed` · Python · MIT · Foadsf

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/Justmalhar/awesome-jev-apps">Justmalhar/awesome-jev-apps</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `observed` · Python · MIT · Justmalhar

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Awesome Collection of apps built with Jev - a System One model

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `observed` · TypeScript · MIT · qddegtya

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 3 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typed decisions from a System One model, where uncertainty is something you have to handle.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `observed` · Python · aniruddh-krovvidi

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/chy4pro/JevBrowserExt">chy4pro/JevBrowserExt</a></b> — TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `observed` · TypeScript · MIT · chy4pro

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

⚡ Ultrafast browser automation Chrome Extension (Manifest V3) powered by TypeSafe Jev (TypeSafe.ai, OpenRouter, Cloudflare)

</details>

<details>
<summary><b><a href="https://github.com/lorensation/llm-cost-optimizer-jev">lorensation/llm-cost-optimizer-jev</a></b> — observed · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `observed` · Apache-2.0 · lorensation

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

An intelligent routing layer powered by TypeSafe AI's System One model Jev that sits in front of multiple LLM providers, analyzes each incoming request’s complexity, routes it to the cheapest model capable of handling it at acceptable quality, and continuously validates that routing decisions are correct.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐28 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · MIT · yusukebe

##### Dane

Gwiazdki **28** (+2) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐25 · Python · inferred · 0 天 · ⭐-1</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · brainstormity

##### Dane

Gwiazdki **25** (-1) · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐6 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · JavaScript · MIT · mejiasd3v

##### Dane

Gwiazdki **6** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · andrelandgraf

##### Dane

Gwiazdki **3** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · keeltrace

##### Dane

Gwiazdki **3** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · maker-KK

##### Dane

Gwiazdki **2** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐2 · Python · inferred · 2 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · prismhq

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/vtrivedy/jev-plays-games">vtrivedy/jev-plays-games</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · JavaScript · vtrivedy

##### Dane

Gwiazdki **2** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Chess, Connect Four, and a decision model. Play Jev or watch Jev play itself.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/vtrivedy/jev-plays-games/main/docs/screenshots/chess.jpg" width="100%" alt="vtrivedy/jev-plays-games screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · WiktorB2004

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · Pinutss

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Shashank-H

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Jupyter · MIT · bitnovus

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/buberlo/jev-pastepilot">buberlo/jev-pastepilot</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · MIT · buberlo

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Explicit paste-to-action launcher that routes text to useful tools without automatic side effects.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/buberlo--jev-pastepilot/f9f8b5633a938cb0.png" width="100%" alt="buberlo/jev-pastepilot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/buberlo--jev-pastepilot/590a0f155ae53d69.gif" width="100%" alt="buberlo/jev-pastepilot animation"><br><sub>nagranie animowane · <a href="https://raw.githubusercontent.com/buberlo/jev-pastepilot/main/docs/demo/pastepilot-core.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/buyukcerci/jev-model-router">buyukcerci/jev-model-router</a></b> — inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Apache-2.0 · buyukcerci

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A multi-provider LLM and media router featuring calibrated confidence classification, dynamic policy scoring, and automated fallback management.

</details>

<details>
<summary><b><a href="https://github.com/carllippert/jev-router">carllippert/jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · MIT · carllippert

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Express with no routes. TypeSafe Jev picks which handler runs.

</details>

<details>
<summary><b><a href="https://github.com/danielhirt/jev-lab">danielhirt/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · danielhirt

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison

</details>

<details>
<summary><b><a href="https://github.com/gnoviawan/omp-jev-tools">gnoviawan/omp-jev-tools</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · NOASSERTION · gnoviawan

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation verification

</details>

<details>
<summary><b><a href="https://github.com/hugo-alves/jev-router-playground">hugo-alves/jev-router-playground</a></b> — JavaScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · JavaScript · MIT · hugo-alves

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Interactive playground for testing Jev model-routing decisions against OpenRouter models

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hugo-alves--jev-router-playground/93692a5f183f12e1.jpg" width="100%" alt="hugo-alves/jev-router-playground screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iefnaf/pi-jev">iefnaf/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · MIT · iefnaf

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Pi extension suite powered by Jev: selective context compaction and model routing

</details>

<details>
<summary><b><a href="https://github.com/immanuelsavio/jev-experiment">immanuelsavio/jev-experiment</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · JavaScript · immanuelsavio

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Benchmarking TypeSafe Jev against general-purpose LLMs on support-ticket routing, with a focus on latency, accuracy, and confidence.

</details>

<details>
<summary><b><a href="https://github.com/jolehuit/jev-downloads-sorter">jolehuit/jev-downloads-sorter</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · jolehuit

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A ~/Downloads folder that sorts itself: one Jev decision per file, launchd WatchPaths, no daemon

</details>

<details>
<summary><b><a href="https://github.com/kenhuangus/jev-usecases">kenhuangus/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · kenhuangus

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kenhuangus--jev-usecases/be919255190f6495.png" width="100%" alt="kenhuangus/jev-usecases screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-bot">kevin9327/jev-bot</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · kevin9327

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.

</details>

<details>
<summary><b><a href="https://github.com/Loule95450/jev-free-router">Loule95450/jev-free-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · JavaScript · MIT · Loule95450

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Dynamic per-turn model router on free OpenCode Zen + Go models (fork of gargpratyush/jev-router)

</details>

<details>
<summary><b><a href="https://github.com/makefinks/jev-feed-filter">makefinks/jev-feed-filter</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · MIT · makefinks

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Smart, dynamic AI filtering for X and YouTube feeds using Jev

</details>

<details>
<summary><b><a href="https://github.com/mcgalleg/grokbot-jev-jobs">mcgalleg/grokbot-jev-jobs</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · mcgalleg

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Scores public job postings against my resume using TypeSafe's jev via the Vercel AI Gateway. Daily Vercel cron.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-arena">meetr1912/jev-arena</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · meetr1912

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A calibration arena for TypeSafe Jev: reliability, Brier/ECE, and confidence-gated risk-coverage on analytically-known random worlds.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-sonar">meetr1912/jev-sonar</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · meetr1912

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

TypeSafe Jev plays Battleship: one ~100-question typed fan-out per turn returns a calibrated hit-probability heatmap that is also the move policy.

</details>

<details>
<summary><b><a href="https://github.com/MoonTory/pi-jev-harness">MoonTory/pi-jev-harness</a></b> — TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · MoonTory

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards tool calls

</details>

<details>
<summary><b><a href="https://github.com/perixtar/jev-e2e">perixtar/jev-e2e</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · MIT · perixtar

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Natural-language end-to-end tests for web apps, powered by Jev and Playwright.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/perixtar--jev-e2e/81a240435b11d6f2.gif" width="100%" alt="perixtar/jev-e2e animation"><br><sub>nagranie animowane · <a href="https://raw.githubusercontent.com/perixtar/jev-e2e/main/docs/assets/ebay-benchmark.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rajivkuriakose/typesafe-jev-examples">rajivkuriakose/typesafe-jev-examples</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · MIT · rajivkuriakose

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/ravikadam/jev-loan-triage">ravikadam/jev-loan-triage</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · JavaScript · ravikadam

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Voice loan-call triage using TypeSafe Jev: intent, info sufficiency and a lending decision from typed AI judgments

</details>

<details>
<summary><b><a href="https://github.com/SadiqOnGithub/jev-lab">SadiqOnGithub/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · SadiqOnGithub

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API

</details>

<details>
<summary><b><a href="https://github.com/SDTakeuchi/jev-api-router">SDTakeuchi/jev-api-router</a></b> — Go · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Go · SDTakeuchi

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/TokenTrim/jev-routing-experiment">TokenTrim/jev-routing-experiment</a></b> — Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · Apache-2.0 · TokenTrim

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tokentrim--jev-routing-experiment/1c31bd606ebc1994.png" width="100%" alt="TokenTrim/jev-routing-experiment screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ufec/jev-block-android-ad">ufec/jev-block-android-ad</a></b> — Kotlin · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Kotlin · MIT · ufec

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

JevNoiseGate filters unwanted notifications and SMS on Android. Rather than   matching keywords, an LLM decides what's noise — and only what it explicitly   flags is blocked. Verification codes are matched on-device and never uploaded;   anything uncertain passes through.

</details>

<details>
<summary><b><a href="https://github.com/viniciosrab/pi-jev-router">viniciosrab/pi-jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · TypeScript · MIT · viniciosrab

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/Zumka1991/jev-telegram-admin">Zumka1991/jev-telegram-admin</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `inferred` · Python · Zumka1991

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

AI moderator for Telegram groups powered by the Jev (TypeSafe System One) decision model

</details>

<details>
<summary><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">iammrduncan/typesafe-ai-benchmark</a></b> — ⭐32 · TypeScript · unverified · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `unverified` · TypeScript · MIT · iammrduncan

##### Dane

Gwiazdki **32** · Forki 5 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.

> A gateway that mimics the System One interface, which is what makes side-by-side benchmarking possible without rewriting the caller.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/80d6baf37faa23fb.gif" width="100%" alt="iammrduncan/typesafe-ai-benchmark animation"><br><sub>nagranie animowane · <a href="https://raw.githubusercontent.com/iammrduncan/typesafe-ai-benchmark/main/docs/media/theater-demo.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kavehmz/typesafe-playground">kavehmz/typesafe-playground</a></b> — ⭐9 · JavaScript · unverified · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `unverified` · JavaScript · kavehmz

##### Dane

Gwiazdki **9** · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/kavehmz/typesafe-playground/main/docs/images/demo03-fable.png" width="100%" alt="kavehmz/typesafe-playground screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/raihankhan-rk/diffjury">raihankhan-rk/diffjury</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Podstawowe informacje

`Routing, zabezpieczenia i zatwierdzenia` · Społeczność · `unverified` · TypeScript · raihankhan-rk

##### Dane

Gwiazdki **3** · Forki 1 · Otwarte zgłoszenia 2 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

DiffJury — TypeSafe Jev PR risk router + code review coach

</details>

<a id="evaluation"></a>

## Ewaluacja, kalibracja i benchmarki

Skąd ktokolwiek wie, że te decyzje są coś warte. Kalibracja to otwarte pytanie w tym ekosystemie, a te projekty ją mierzą.

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐5 · Python · observed · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `observed` · Python · Apache-2.0 · ikermoel

##### Dane

Gwiazdki **5** (+1) · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Open-source alternative to TypeSafe's Jev: a System One style model layer that gives typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with honest benchmarks

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `observed` · Python · akash-kamat

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/edgardcham/huncho">edgardcham/huncho</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `observed` · TypeScript · MIT · edgardcham

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Decisions as code on System One models: typed questions, thresholds with hysteresis, nested decisions, journal, calibration

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `observed` · Go · MIT · Gaurav-Gosain

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — ⭐1 · Python · observed · 1 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `observed` · Python · Apache-2.0 · hev

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/nishioka-shinji/jev-edgar">nishioka-shinji/jev-edgar</a></b> — Python · observed · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `observed` · Python · nishioka-shinji

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Does Jev, a System One model returning calibrated probabilities, say anything useful about an earnings release before the market prices it?

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐8 · Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · Apache-2.0 · AbdelStark

##### Dane

Gwiazdki **8** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐6 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · NOASSERTION · Heman10x-NGU

##### Dane

Gwiazdki **6** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/abhixhek/jevcal">abhixhek/jevcal</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · MIT · abhixhek

##### Dane

Gwiazdki **5** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abhixhek--jevcal/3dbe2307176737c8.png" width="100%" alt="abhixhek/jevcal screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐5 · TypeScript · inferred · 2 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · TypeScript · MIT · y0usaf

##### Dane

Gwiazdki **5** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/cablehead/jev.nu">cablehead/jev.nu</a></b> — ⭐2 · Nushell · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Nushell · MIT · cablehead

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nushell module for the TypeSafe System One API: typed decisions with calibrated probabilities

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 2 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · MIT · wondertwins

##### Dane

Gwiazdki **2** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · 4esv

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

</details>

<details>
<summary><b><a href="https://github.com/carson-sweet/jev-plays-brogue">carson-sweet/jev-plays-brogue</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · TypeScript · AGPL-3.0 · carson-sweet

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

TypeSafe's Jev model plays the roguelike Brogue live -- a hand-built expert system for System-2 reasoning, outcome-calibrated self-learning, and a web UI to watch decisions, costs, and training progress.

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · TypeScript · MIT · Danu28

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · TeX · NOASSERTION · dnakhoa

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · eggmasonvalue

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/ickma2311/jev-baselines-eval">ickma2311/jev-baselines-eval</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · MIT · ickma2311

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Pre-registered independent eval of TypeSafe Jev against a nano-class LLM, a frontier LLM, and a supervised encoder (Banking77 + CLINC150 zero-shot)

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ickma2311--jev-baselines-eval/4cef768bc4898704.png" width="100%" alt="ickma2311/jev-baselines-eval screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · MIT · jujumilk3

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · JavaScript · MIT · KantaHayashiAI

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/KiishiAD/jev-loan-identity-benchmark">KiishiAD/jev-loan-identity-benchmark</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · KiishiAD

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Reproducible synthetic benchmark for temporal loan identity resolution with TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/laurentfabre/databricks-jev-pdf-lab">laurentfabre/databricks-jev-pdf-lab</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · laurentfabre

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Precision PDF extraction research: Databricks + Jev, synthetic tests, selective parsing, measured tradeoffs and negative results.

</details>

<details>
<summary><b><a href="https://github.com/llt22/jev-lab">llt22/jev-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · llt22

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

TypeSafe Jev research, benchmarks, evaluation datasets, and reproducible experiments

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-bracket">meetr1912/jev-bracket</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · MIT · meetr1912

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

TypeSafe Jev predicts a synthetic 32-team tournament in round fan-out: calibrated Brier vs Elo/seed/oracle plus Monte Carlo champion odds.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-vickrey">meetr1912/jev-vickrey</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · MIT · meetr1912

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

TypeSafe Jev bids in sealed-bid auctions: threshold fan-out reconstructs a calibrated value CDF, scored by regret and truthfulness.

</details>

<details>
<summary><b><a href="https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and">musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and</a></b> — HTML · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · HTML · MIT · musman550

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@automatewithmusfiraai"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@automatewithmusfiraai">Obejrzyj na youtube.com</a> · odtwarzanie otwiera się w witrynie hosta; GitHub nie może osadzić go bezpośrednio</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/onlyoneaman/jev-eval">onlyoneaman/jev-eval</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · TypeScript · MIT · onlyoneaman

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/onlyoneaman--jev-eval/e5d471e96e134f81.png" width="100%" alt="onlyoneaman/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rorshopping/jev-browser-local">rorshopping/jev-browser-local</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · NOASSERTION · rorshopping

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Run jev-browser on a fully local JEV-style decision engine (no cloud API). Warm-browser fork, VRAM guard, measured benchmarks, run traces.

</details>

<details>
<summary><b><a href="https://github.com/SHAKULMITTAL22/jev-resume">SHAKULMITTAL22/jev-resume</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · AGPL-3.0 · SHAKULMITTAL22

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Folio: job-specific resume leaderboards with approved rubrics, evidence-backed AI evaluation, and human hiring decisions.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shakulmittal22--jev-resume/e653593f3a00df9d.png" width="100%" alt="SHAKULMITTAL22/jev-resume screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shunta-furukawa/jev-tick-lab">shunta-furukawa/jev-tick-lab</a></b> — inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · shunta-furukawa

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis.

</details>

<details>
<summary><b><a href="https://github.com/teyhouse/jev-secret-detection">teyhouse/jev-secret-detection</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · teyhouse

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" width="100%" alt="teyhouse/jev-secret-detection screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/thisisandreeeee/jev-benchmarks">thisisandreeeee/jev-benchmarks</a></b> — inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · MIT · thisisandreeeee

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/us/jev-local">us/jev-local</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · us

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Local Jev-compatible evaluation server: POST /v1/systemone with typed noul/choice/score, open weights, no waitlist

</details>

<details>
<summary><b><a href="https://github.com/yodablocks/jev-orderby-bench">yodablocks/jev-orderby-bench</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `inferred` · Python · MIT · yodablocks

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev.

</details>

<details>
<summary><b><a href="https://github.com/kyotofin/tax-doc-classifier">kyotofin/tax-doc-classifier</a></b> — ⭐130 · TypeScript · unverified · 0 天 · ⭐+17</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `unverified` · TypeScript · Apache-2.0 · kyotofin

##### Dane

Gwiazdki **130** (+17) · Forki 12 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.

</details>

<details>
<summary><b><a href="https://github.com/Mapika/decider">Mapika/decider</a></b> — ⭐25 · Python · unverified · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `unverified` · Python · Apache-2.0 · Mapika

##### Dane

Gwiazdki **25** · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mapika--decider/c67d355f22dcb51a.gif" width="100%" alt="Mapika/decider animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/genai-craft/openvons">genai-craft/openvons</a></b> — ⭐7 · Python · unverified · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `unverified` · Python · NOASSERTION · genai-craft

##### Dane

Gwiazdki **7** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド

</details>

<details>
<summary><b><a href="https://github.com/aabolfazl/typesafe-local">aabolfazl/typesafe-local</a></b> — ⭐6 · Python · unverified · 0 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `unverified` · Python · MIT · aabolfazl

##### Dane

Gwiazdki **6** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/aabolfazl--typesafe-local/ada59cf382af5143.png" width="100%" alt="aabolfazl/typesafe-local screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mithalouni/system-one-open">mithalouni/system-one-open</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### Podstawowe informacje

`Ewaluacja, kalibracja i benchmarki` · Społeczność · `unverified` · Python · NOASSERTION · mithalouni

##### Dane

Gwiazdki **4** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal)

</details>

<a id="research-models"></a>

## Otwarte reprodukcje, wagi i badania nad architekturą

Otwarte wagi, małe repliki i prace nad architekturą. Część z nich istnieje, bo zachowania kalibracyjne nie dają się odtworzyć wyłącznie z materiałów publicznych.

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐63 · Python · observed · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `observed` · Python · MIT · kshetrajna12

##### Dane

Gwiazdki **63** (+1) · Forki 4 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐395 · Python · inferred · 1 天 · ⭐+25</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · MIT · TianyuCodings

##### Dane

Gwiazdki **395** (+25) · Forki 37 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/5055af419619e7e4.gif" width="100%" alt="TianyuCodings/NanoJev animation"><br><sub>nagranie animowane · <a href="https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/assets/side_by_side_maze.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐22 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · MIT · r-ms

##### Dane

Gwiazdki **22** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/imserhatdemir/jevspace">imserhatdemir/jevspace</a></b> — HTML · observed · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `observed` · HTML · imserhatdemir

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A DarkOrbit-style space game piloted by Jev — TypeSafe's System One model. Three.js world, deterministic engine, Jev picks the targets.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/imserhatdemir/jevspace/main/docs/screenshot-win.png" width="100%" alt="imserhatdemir/jevspace screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `observed`

##### Dane

Pobrania 25 · Polubienia 4 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 1 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `observed`

##### Dane

Pobrania 0 · Polubienia 0 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐160 · Python · inferred · 0 天 · ⭐+6</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · ekzhang

##### Dane

Gwiazdki **160** (+6) · Forki 12 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/featherless-ai/simple-jev">featherless-ai/simple-jev</a></b> — ⭐70 · Python · inferred · 0 天 · ⭐+13</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · featherless-ai

##### Dane

Gwiazdki **70** (+13) · Forki 6 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Turn any open model into a classifier/jev endpoint

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/featherless-ai/simple-jev/main/imgs/Simple-Jev-Logo.png" width="100%" alt="featherless-ai/simple-jev screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐24 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · MIT · bnsd55

##### Dane

Gwiazdki **24** · Forki 3 · Otwarte zgłoszenia 6 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/siliconkernel/vllm-jev-decison">siliconkernel/vllm-jev-decison</a></b> — ⭐8 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · MIT · siliconkernel

##### Dane

Gwiazdki **8** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Classification-only typed decisions for vLLM: finite-schema candidate scoring, probabilities, and abstention. No generative fallback.

</details>

<details>
<summary><b><a href="https://github.com/wfzyx/von">wfzyx/von</a></b> — ⭐4 · Python · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · wfzyx

##### Dane

Gwiazdki **4** (+1) · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/choxos/jev-reviewer">choxos/jev-reviewer</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · JavaScript · MIT · choxos

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay in your browser.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/4a551dbca9d0c41e.jpg" width="100%" alt="choxos/jev-reviewer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/71abea319063ce6d.gif" width="100%" alt="choxos/jev-reviewer animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/deep-diver/mini-jev">deep-diver/mini-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · deep-diver

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/kw2828/OpenJev">kw2828/OpenJev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · MIT · kw2828

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Browser decision playground and reproducible experiments on memory, uncertainty, and Doom control

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/7caa9b0eff4636a1.png" width="100%" alt="kw2828/OpenJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/af5371a3a94cb693.gif" width="100%" alt="kw2828/OpenJev animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/backmeupplz/jev_antispam_bot">backmeupplz/jev_antispam_bot</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · TypeScript · MIT · backmeupplz

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">legacybridge-tech/pi-typesafe-jev</a></b> — TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · TypeScript · NOASSERTION · legacybridge-tech

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.

</details>

<details>
<summary><b><a href="https://github.com/NeU-dev/reddit-jev-sentiment-analyzer">NeU-dev/reddit-jev-sentiment-analyzer</a></b> — inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · NeU-dev

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A non-commercial personal research prototype for numerical sentiment analysis of public Reddit technology discussions using JEV.

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `inferred` · Python · shellneko

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐9 · Python · unverified · 2 天 · ⭐+1</summary>

##### Podstawowe informacje

`Otwarte reprodukcje, wagi i badania nad architekturą` · Społeczność · `unverified` · Python · NOASSERTION · zhihz

##### Dane

Gwiazdki **9** (+1) · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<a id="apps-demos"></a>

## Aplikacje, gry, robotyka i interaktywne dema

Gry, roboty, przeglądarki i pulpity. Dema to sposób, w jaki twierdzenia o opóźnieniach i kosztach stają się czytelne.

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐10 · Python · observed · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `observed` · Python · Apache-2.0 · zadescoxp

##### Dane

Gwiazdki **10** · Forki 1 · Otwarte zgłoszenia 3 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `observed` · TypeScript · daftAI2026

##### Dane

Gwiazdki **2** · Forki 2 · Otwarte zgłoszenia 2 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `observed` · Rust · MIT · markjaquith

##### Dane

Gwiazdki **1** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `observed` · TypeScript · adiun

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `observed` · Dart · Bud-ro

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/chris-wozniczek/jev-voice-control">chris-wozniczek/jev-voice-control</a></b> — Swift · observed · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `observed` · Swift · chris-wozniczek

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-bar Swift app.

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `observed` · Python · MIT · tirukovelamanoj

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/04e4dd3a1f6c6bae.gif" width="100%" alt="tirukovelamanoj/jev-plays-doom animation"><br><sub>nagranie animowane · <a href="https://raw.githubusercontent.com/tirukovelamanoj/jev-plays-doom/main/docs/jev-doom.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `observed` · TypeScript · wustep

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://x.com/tspy/status/2100864234523685146">X intent labeller</a></b> — @tspy · observed · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `observed` · [yishan](https://x.com/tspy) · @tspy · x.com

##### Dane

Wyświetlenia 2364 · Polubienia 15 · Komentarze 9 · Opublikowano 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A Chrome extension that labels posts in an X timeline with their intent and probability as you scroll, drawn as a tag directly after each post's timestamp. Categories include inducement, provocation, promotion, machine-generated, persuasion, entertainment and information. A side panel reports session counts (seen, judged, correct) and cumulative token cost. The author reports near-instant responses and usable accuracy before any tuning.

<sub>Trwa ustalanie linku do projektu źródłowego.</sub>

> Worth reading as a latency argument rather than an accuracy one: labelling a timeline only works if the decision costs less than the scroll, which is the constraint a generative model cannot meet.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/0641644f12a25a45.jpg" width="100%" alt="X intent labeller screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/b80cf3173f63bdd7.gif" width="100%" alt="X intent labeller animation"><br><sub>nagranie animowane · <a href="https://video.twimg.com/amplify_video/2100858340331200512/vid/avc1/1242x720/ex2FF5-TerVxo9xX.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐111 · Python · inferred · 0 天 · ⭐+2</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Python · MIT · hr98w

##### Dane

Gwiazdki **111** (+2) · Forki 12 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐108 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · TypeScript · MIT · jkudish

##### Dane

Gwiazdki **108** (+4) · Forki 5 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/d9b7631c25d7db06.gif" width="100%" alt="jkudish/jev-browser animation"><br><sub>nagranie animowane · <a href="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐79 · JavaScript · inferred · 1 天 · ⭐+8</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · MIT · moritzkremb

##### Dane

Gwiazdki **79** (+8) · Forki 8 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/mizchi/jev-playground">mizchi/jev-playground</a></b> — ⭐15 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · TypeScript · mizchi

##### Dane

Gwiazdki **15** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐7 · Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Python · MIT · komorra

##### Dane

Gwiazdki **7** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐7 · JavaScript · inferred · 0 天 · ⭐+2</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · vinilana

##### Dane

Gwiazdki **7** (+2) · Forki 5 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · TypeScript · emrickgarrett

##### Dane

Gwiazdki **5** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 1 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Go · MIT · paulsmith

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · TypeScript · MIT · vmendes90

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/vmendes90--jev-shield/ee87b261d199a34c.jpg" width="100%" alt="vmendes90/jev-shield screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0x7067/jev-browse">0x7067/jev-browse</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · MIT · 0x7067

##### Dane

Gwiazdki **1** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Browser automation with Jev (TypeSafe) as decision model

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/6b2906f1131adf4c.gif" width="100%" alt="0x7067/jev-browse screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/3efc4d3b381ff9f5.gif" width="100%" alt="0x7067/jev-browse animation"><br><sub>nagranie animowane · <a href="https://raw.githubusercontent.com/0x7067/jev-browse/main/docs/demo.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/charleeagni/JevPiano">charleeagni/JevPiano</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · charleeagni

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

@typesafeai 's Jev controls the 2 hands and each finger to play the piano in real-time.  Jev only "sees" what we see and plays this from the "note waterfall". It uses  @browser_use 's jev-ultrafast and some decision scheduling to make this happen in real-time.  Sound on 🔈🔉🔊

</details>

<details>
<summary><b><a href="https://github.com/finetuningsingh/jev-chatbot">finetuningsingh/jev-chatbot</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · MIT · finetuningsingh

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Experiment: using TypeSafe Jev as a chatbot by choosing replies one letter or word at a time

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · TypeScript · Little-Planet-Labs

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 2 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Python · PistachioAIHQ

##### Dane

Gwiazdki **1** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/acharyaanusha/magic-jev-demo">acharyaanusha/magic-jev-demo</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · acharyaanusha

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 6 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Sample pull requests for demoing Magic Jev. The code is filler.

</details>

<details>
<summary><b><a href="https://github.com/bahramzada/jev-taxi-dispatch">bahramzada/jev-taxi-dispatch</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · MIT · bahramzada

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Real-vaxt taksi dispetçerlik simulyasiyası - TypeSafe JEV (System One) modeli ilə

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/bahramzada--jev-taxi-dispatch/e616f4168b15d3f2.png" width="100%" alt="bahramzada/jev-taxi-dispatch screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/BrendanH18/jev-lab">BrendanH18/jev-lab</a></b> — Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Python · MIT · BrendanH18

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brendanh18--jev-lab/b16b9535e3744cd3.png" width="100%" alt="BrendanH18/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/chahero/driving-jev">chahero/driving-jev</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Python · chahero

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Watch TypeSafe Jev make highway driving decisions. Includes live API and offline gameplay previews.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev-preview.gif" width="100%" alt="chahero/driving-jev screenshot"></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev.mp4"><img src="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev-preview.gif" width="100%" alt="chahero/driving-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev.mp4">Otwórz wideo</a></sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/ethereumdegen/jev-discord-bot">ethereumdegen/jev-discord-bot</a></b> — Rust · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Rust · MIT · ethereumdegen

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/formigacamuflada/jev-computer-use">formigacamuflada/jev-computer-use</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Python · formigacamuflada

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/gua-project/gua-sample-jev-racinggame">gua-project/gua-sample-jev-racinggame</a></b> — inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · gua-project

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/JYeswak/jev_playground">JYeswak/jev_playground</a></b> — Shell · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Shell · MIT · JYeswak

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jyeswak--jev_playground/b6414da07c9c5aa8.jpg" width="100%" alt="JYeswak/jev_playground screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Keitark/jev-gamebook-demo">Keitark/jev-gamebook-demo</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Python · Keitark

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/metrox-eth/moss-jev">metrox-eth/moss-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · metrox-eth

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

MOSS × Jev: a recorded-run 3D demo of the litter-picking rover choosing targets with TypeSafe's Jev decision model.

</details>

<details>
<summary><b><a href="https://github.com/n3ndor/n8n-nodes-typesafe-jev">n3ndor/n8n-nodes-typesafe-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · TypeScript · MIT · n3ndor

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

n8n community node for TypeSafe Jev structured AI decisions

</details>

<details>
<summary><b><a href="https://github.com/parzivale/jev-bot">parzivale/jev-bot</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · Rust · parzivale

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Discord bot that scores how likely a statement is to be true, using TypeSafe's jev model

</details>

<details>
<summary><b><a href="https://github.com/PierrunoYT/JevFlow">PierrunoYT/JevFlow</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · TypeScript · PierrunoYT

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A trading bot powered by TypeSafe AI's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pistachiopranay/jev-synergy-screening">pistachiopranay/jev-synergy-screening</a></b> — inferred · 2 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · pistachiopranay

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/rchovatiya88/cyber-breach-jev">rchovatiya88/cyber-breach-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · rchovatiya88

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model

</details>

<details>
<summary><b><a href="https://github.com/rikkooo/jev-trade">rikkooo/jev-trade</a></b> — inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · rikkooo

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A market-data trading simulator powered by auditable Jev judgments

</details>

<details>
<summary><b><a href="https://github.com/SuryaManavalan/JevNash">SuryaManavalan/JevNash</a></b> — inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · SuryaManavalan

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Jev harness for playing or working, agnostic of the game or workstream.

</details>

<details>
<summary><b><a href="https://github.com/tanayvasishtha/Slither-Me-Jev">tanayvasishtha/Slither-Me-Jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `inferred` · JavaScript · tanayvasishtha

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

8 AI snakes, 1 human, 1 arena. Every snake is driven live by TypeSafe's Jev, making all decisions in real time

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/tanayvasishtha/Slither-Me-Jev/main/menu-screenshot.png" width="100%" alt="tanayvasishtha/Slither-Me-Jev screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/sorrycc/typesafe-snake">sorrycc/typesafe-snake</a></b> — ⭐17 · TypeScript · unverified · 1 天</summary>

##### Podstawowe informacje

`Aplikacje, gry, robotyka i interaktywne dema` · Społeczność · `unverified` · TypeScript · sorrycc

##### Dane

Gwiazdki **17** · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code

</details>

<a id="media-discussions"></a>

## Teksty, dyskusje i pokrewne listy

Wątki premierowe, niezależne artykuły i inne listy tematyczne w tej dziedzinie. To repozytorium nie jest jedyne, a powiedzenie tego jest bardziej użyteczne niż udawanie inaczej.

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐5671 · Python · observed · 0 天 · ⭐+200</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · Python · MIT · browser-use

##### Dane

Gwiazdki **5671** (+200) · Forki 361 · Otwarte zgłoszenia 34 · Utworzono 2026-09-16 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

i. am. speed.

<sub>Znaleziono użycie w kodzie: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcdb919ac3afb514.gif" width="100%" alt="browser-use/jev-ultrafast animation"><br><sub>nagranie animowane · <a href="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/demo.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1890 · observed · 3 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 1890 · Komentarze 496 · Ostatni push 2026-09-15 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐529 · Python · observed · 0 天 · ⭐+9</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · Python · MIT · Anil-matcha

##### Dane

Gwiazdki **529** (+9) · Forki 102 · Otwarte zgłoszenia 4 · Utworzono 2023-05-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>Znaleziono użycie w kodzie: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐235 · TypeScript · observed · 0 天 · ⭐+16</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · TypeScript · dabit3

##### Dane

Gwiazdki **235** (+16) · Forki 20 · Otwarte zgłoszenia 17 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

<sub>Znaleziono użycie w kodzie: `jev-lint/proxy.mjs`</sub>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐232 · CSS · observed · 0 天 · ⭐+8</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · CSS · MIT · AbdelStark

##### Dane

Gwiazdki **232** (+8) · Forki 34 · Otwarte zgłoszenia 2 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>Znaleziono użycie w kodzie: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐181 · Python · observed · 0 天 · ⭐+16</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · Python · yibie

##### Dane

Gwiazdki **181** (+16) · Forki 25 · Otwarte zgłoszenia 13 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐118 · observed · 0 天 · ⭐+5</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · CC0-1.0 · cobanov

##### Dane

Gwiazdki **118** (+5) · Forki 12 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐67 · observed · 0 天 · ⭐+2</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · CC0-1.0 · AnotiaWang

##### Dane

Gwiazdki **67** (+2) · Forki 19 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>Znaleziono użycie w kodzie: `README.md`, `README_zh.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐52 · observed · 1 天 · ⭐+1</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 52 · Komentarze 12 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐37 · JavaScript · observed · 0 天 · ⭐+4</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### Dane

Gwiazdki **37** (+4) · Forki 10 · Otwarte zgłoszenia 10 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A community directory of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐11 · JavaScript · observed · 0 天 · ⭐+2</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · JavaScript · NOASSERTION · OmniJev

##### Dane

Gwiazdki **11** (+2) · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Papers, open reproductions and independent evaluations behind System One models and Jev.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49760264">Using jev to improve product experiences is pretty crazy</a></b> — ⭐6 · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 6 · Komentarze 3 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 3 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 5 · Komentarze 0 · Ostatni push 2026-09-15 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 4 · Komentarze 0 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 4 · Komentarze 0 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 3 · Komentarze 0 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755005">Two techniques for working with System One models</a></b> — ⭐3 · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 3 · Komentarze 0 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 3 · Komentarze 0 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐2 · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · NOASSERTION · aliaihub

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### Dane

Gwiazdki **2** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49759706">I used Jev to control a swarm of 15 simulated drones in real time</a></b> — ⭐2 · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 0 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49759999">Jev&#x27;s Architecture Unmasked</a></b> — ⭐2 · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 0 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/jtnkminimal/awesome-jev">jtnkminimal/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · Python · CC0-1.0 · jtnkminimal

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A curated projects built with Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49753667">Show HN: Explore 2D semantic space with the Jev model</a></b> — ⭐2 · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 0 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

SemanticSpace is an experiment around Jev, TypeSafe AI’s new model. It uses a Cartesian plane defined by arbitrary phrases for each axis, to map prompts onto the resulting 2D semantic space. You can edit the prompts and axes to visualize virtually any 2D relationship.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49750649">Show HN: Open-Source Alternative to TypeSafe.ai</a></b> — ⭐2 · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 1 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49744527">Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)</a></b> — ⭐2 · observed · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 1 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Full disclosure, it was coded with AI, I don&#x27;t claim otherwise. But I wanted to test out tool calls and iterative problem solving using Jev and needed a simple library&#x2F;framework&#x2F;harness to do that.
SOKIT (System One Knowledge, Instructions and Tools) is the result

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49729945">The first (public) System One Model; Jev gives AI the properties of code</a></b> — ⭐2 · observed · 2 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 0 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49757995">TypeSafe / Jev latency-focused demos built by Devin</a></b> — ⭐2 · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 0 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49761730">TypeSafe AI&#x27;s Jev Is Not an LLM – and That May Be the Point</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 0 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49745212">Typesafe&#x27;s Jev is the fish at the poker table</a></b> — ⭐2 · observed · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 1 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49733647">Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step</a></b> — ⭐2 · observed · 2 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 0 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49734345">Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD</a></b> — ⭐2 · observed · 2 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 0 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49760138">What is a System One model and why we need it?</a></b> — ⭐2 · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed`

##### Dane

Punkty 2 · Komentarze 0 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/ozers/jevsome-projects">ozers/jevsome-projects</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · JavaScript · MIT · ozers

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Open-source projects that provably call Jev, TypeSafe AI's System One model. Every entry links to the line of code that proves it. Refreshed daily.

</details>

<details>
<summary><b><a href="https://github.com/rhc98/awesome-jev">rhc98/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · TypeScript · NOASSERTION · rhc98

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself.

</details>

<details>
<summary><b><a href="https://github.com/soderlind/ai-provider-for-jev">soderlind/ai-provider-for-jev</a></b> — ⭐1 · PHP · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · PHP · soderlind

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).

</details>

<details>
<summary><b><a href="https://github.com/aamanlamba/jev-explore">aamanlamba/jev-explore</a></b> — Jupyter · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · Jupyter · aamanlamba

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

An example repository for exploring Jev - the System One model

</details>

<details>
<summary><b><a href="https://github.com/alpibrusl/lex-judge">alpibrusl/lex-judge</a></b> — Lex · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · Lex · alpibrusl

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typed judgments from a System One model, as a \[net\]-only Lex effect

</details>

<details>
<summary><b><a href="https://github.com/codaaiteam/jev-ai">codaaiteam/jev-ai</a></b> — observed · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · codaaiteam

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Jev AI quickstart & FAQ — TypeSafe AI's System One model. Try it free: jevtypesafeai.com

</details>

<details>
<summary><b><a href="https://github.com/hide-G/magi-system-on-jev">hide-G/magi-system-on-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · JavaScript · hide-G

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/hide-G/magi-system-on-jev/master/public/ogp.png" width="100%" alt="hide-G/magi-system-on-jev screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/JohnDotOwl/awesome-jev">JohnDotOwl/awesome-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · JavaScript · CC0-1.0 · JohnDotOwl

##### Dane

Gwiazdki **0** · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A curated list of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/piyush97/focus-tube">piyush97/focus-tube</a></b> — JavaScript · observed · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · JavaScript · MIT · piyush97

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model

</details>

<details>
<summary><b><a href="https://github.com/rbalch/typesafeai-review">rbalch/typesafeai-review</a></b> — Python · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · Python · rbalch

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Using Typesafe.AI to generate diff reviews.

</details>

<details>
<summary><b><a href="https://github.com/robzolkos/omarchy-issue-classifier">robzolkos/omarchy-issue-classifier</a></b> — Ruby · observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · Ruby · robzolkos

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Classify the Omarchy issue backlog with Jev, TypeSafe's System One model. Ten typed questions per issue in one request, for a hundredth of a cent each.

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/jev-trader">Shashank-H/jev-trader</a></b> — observed · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · AGPL-3.0 · Shashank-H

##### Dane

Gwiazdki **0** · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

An automated trader using SystemOne model - TypesafeAI Jev

</details>

<details>
<summary><b><a href="https://github.com/TheGali/terrarium">TheGali/terrarium</a></b> — JavaScript · observed · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `observed` · JavaScript · MIT · TheGali

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.

</details>

<details>
<summary><b><a href="https://github.com/jarrodwatts/jev-trader">jarrodwatts/jev-trader</a></b> — ⭐888 · TypeScript · inferred · 1 天 · ⭐+23</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · jarrodwatts

##### Dane

Gwiazdki **888** (+23) · Forki 170 · Otwarte zgłoszenia 3 · Utworzono 2026-09-16 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

</details>

<details>
<summary><b><a href="https://github.com/droidrun/mobile-jev">droidrun/mobile-jev</a></b> — ⭐144 · JavaScript · inferred · 1 天 · ⭐+9</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · MIT · droidrun

##### Dane

Gwiazdki **144** (+9) · Forki 22 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/superagents-lab/jev-search">superagents-lab/jev-search</a></b> — ⭐123 · TypeScript · inferred · 0 天 · ⭐+19</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · superagents-lab

##### Dane

Gwiazdki **123** (+19) · Forki 20 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/superagents-lab--jev-search/5a545ddfd6a52aed.png" width="100%" alt="superagents-lab/jev-search screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mrnugget/jev-shell-history">mrnugget/jev-shell-history</a></b> — ⭐44 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · mrnugget

##### Dane

Gwiazdki **44** (+1) · Forki 3 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Fish-style zsh history autosuggestions ranked by Jev (TypeSafe)

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history animation"><br><sub>nagranie animowane</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">IAmUnbounded/save-token-jev-clean</a></b> — ⭐40 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · IAmUnbounded

##### Dane

Gwiazdki **40** · Forki 9 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/daseinlabs/open-jev">daseinlabs/open-jev</a></b> — ⭐32 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · daseinlabs

##### Dane

Gwiazdki **32** · Forki 5 · Otwarte zgłoszenia 2 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov"><img src="" width="100%" alt="daseinlabs/open-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hqman/JevScout">hqman/JevScout</a></b> — ⭐18 · Python · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · hqman

##### Dane

Gwiazdki **18** (+1) · Forki 2 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4"><img src="" width="100%" alt="hqman/JevScout video"></a><br><sub><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4">Otwórz wideo</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/oso95/x-scanner">oso95/x-scanner</a></b> — ⭐8 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · oso95

##### Dane

Gwiazdki **8** (+1) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter

</details>

<details>
<summary><b><a href="https://github.com/Kevthetech143/super-jev">Kevthetech143/super-jev</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · MIT · Kevthetech143

##### Dane

Gwiazdki **5** · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A small, extensible decision-to-action harness for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/joelhooks/pi-fast-jev-compaction">joelhooks/pi-fast-jev-compaction</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · joelhooks

##### Dane

Gwiazdki **4** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Pi extension: verbatim context compaction with TypeSafe Jev decisions

</details>

<details>
<summary><b><a href="https://github.com/haseeb-heaven/jev-system-one">haseeb-heaven/jev-system-one</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · MIT · haseeb-heaven

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/haseeb-heaven--jev-system-one/e41c848323b1077a.png" width="100%" alt="haseeb-heaven/jev-system-one screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevinpita/pi-jev-context">kevinpita/pi-jev-context</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · kevinpita

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Reversible context pruning for Pi, powered by TypeSafe Jev. Keep useful context without deleting session history.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevinpita--pi-jev-context/9f40314df01e39d4.png" width="100%" alt="kevinpita/pi-jev-context screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/lbotinelly/jev-little-airways">lbotinelly/jev-little-airways</a></b> — ⭐2 · HTML · inferred · 1 天 · ⭐+1</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · HTML · MIT · lbotinelly

##### Dane

Gwiazdki **2** (+1) · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A show-and-tell capability study for Jev, TypeSafe's System One decision model.

</details>

<details>
<summary><b><a href="https://github.com/oxwen11/awesome-jev">oxwen11/awesome-jev</a></b> — ⭐2 · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · CC0-1.0 · oxwen11

##### Dane

Gwiazdki **2** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A curated list of what people built with Jev

</details>

<details>
<summary><b><a href="https://github.com/1jehuang/jev-pr-labeler">1jehuang/jev-pr-labeler</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · MIT · 1jehuang

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Semantic GitHub PR labels using Jev's typed decisions, with conceptual scope instead of line counts

</details>

<details>
<summary><b><a href="https://github.com/AppitStudio/awesome-jev">AppitStudio/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · NOASSERTION · AppitStudio

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 4 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Curated Jev resources and runnable examples for typed AI decisions.

</details>

<details>
<summary><b><a href="https://github.com/Charlyhno-eng/jev-document-classification">Charlyhno-eng/jev-document-classification</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · Charlyhno-eng

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/charlyhno-eng--jev-document-classification/113bcf66f1648122.png" width="100%" alt="Charlyhno-eng/jev-document-classification screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/jev-review-action">fatwang2/jev-review-action</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · MIT · fatwang2

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 2 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.

</details>

<details>
<summary><b><a href="https://github.com/kazuhideoki/jev-search">kazuhideoki/jev-search</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · kazuhideoki

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Recursive semantic file search using TypeSafe Jev and fzf

</details>

<details>
<summary><b><a href="https://github.com/MumuTW/awesome-jev">MumuTW/awesome-jev</a></b> — ⭐1 · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · CC0-1.0 · MumuTW

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

快速看懂風格鮮明的 Jev：型別化決策的 System One，以及社群熱議的同類模型。

</details>

<details>
<summary><b><a href="https://github.com/sontakey/awesome-jev">sontakey/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · NOASSERTION · sontakey

##### Dane

Gwiazdki **1** · Forki 1 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Unofficial list of insanely useful TypeSafe AI Jev / System One projects

</details>

<details>
<summary><b><a href="https://github.com/TanayPadar/gpt-vs-jev">TanayPadar/gpt-vs-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · TanayPadar

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Compare GPT generated language with JEV structured Noul decisions on the same input.

</details>

<details>
<summary><b><a href="https://github.com/tylerjharden/harden-jev-decides">tylerjharden/harden-jev-decides</a></b> — ⭐1 · TypeScript · inferred · 2 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · tylerjharden

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.

</details>

<details>
<summary><b><a href="https://github.com/X0EF/jev_projects">X0EF/jev_projects</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · MIT · X0EF

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

list of projects that use typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/Z761293629/pi-jev-helm">Z761293629/pi-jev-helm</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · Z761293629

##### Dane

Gwiazdki **1** · Forki 0 · Otwarte zgłoszenia 2 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/agentik-os/jev-radar">agentik-os/jev-radar</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · agentik-os

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/amansoory/JEV2048">amansoory/JEV2048</a></b> — C++ · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · C++ · amansoory

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/amr05008/jev-sandbox">amr05008/jev-sandbox</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · amr05008

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Test bench for TypeSafe's Jev: small, repeatable experiments on where a decision model beats prompt-and-parse

</details>

<details>
<summary><b><a href="https://github.com/Btheriot83/jev-academy">Btheriot83/jev-academy</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · Btheriot83

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Public Jev / TypeSafe academy — zero-to-hero walkthrough for Brandon Theriot

</details>

<details>
<summary><b><a href="https://github.com/caio0452/jev_search">caio0452/jev_search</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · caio0452

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/divo12/jev-v-llm">divo12/jev-v-llm</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · divo12

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/doroper98/Jev_Pendulum">doroper98/Jev_Pendulum</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · doroper98

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/EdwardHong0627/jev-poc">EdwardHong0627/jev-poc</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · EdwardHong0627

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/getvoicify/jev-reviewer">getvoicify/jev-reviewer</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · getvoicify

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/golergka/jev-plays-starcraft-2">golergka/jev-plays-starcraft-2</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · golergka

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/heaven-hm/jev-system-one">heaven-hm/jev-system-one</a></b> — inferred · 2 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · heaven-hm

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

</details>

<details>
<summary><b><a href="https://github.com/jamesward/jev-llm-c4">jamesward/jev-llm-c4</a></b> — Scala · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Scala · jamesward

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/jdhornsby/typesafe-jev">jdhornsby/typesafe-jev</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · jdhornsby

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-master">kevin9327/jev-master</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · MIT · kevin9327

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Typed System One decisions with Jev: Choice + Score + Noul composed in code.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevin9327--jev-master/cbf05c4561269075.png" width="100%" alt="kevin9327/jev-master screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kong75/jev-directory">kong75/jev-directory</a></b> — Astro · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Astro · kong75

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A curated directory of Jev projects, examples, and patterns.

</details>

<details>
<summary><b><a href="https://github.com/kspviswa/chakravyuha-jev">kspviswa/chakravyuha-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · MIT · kspviswa

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kspviswa--chakravyuha-jev/4dfa22d0de9f27c1.png" width="100%" alt="kspviswa/chakravyuha-jev screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/lalitsonawane/jev-one-system">lalitsonawane/jev-one-system</a></b> — inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · lalitsonawane

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/LingXuanYin/jev-chat">LingXuanYin/jev-chat</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · NOASSERTION · LingXuanYin

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Jev 聊天机：一个「只选不写」的聊天机——每个回复由逐词选择拼装，词典+分级索引+输入法式联想，由真实 Jev（TypeSafe System One）驱动。非官方实验，与 TypeSafe AI 无关联。

</details>

<details>
<summary><b><a href="https://github.com/lookfwd/jev-fact-checker">lookfwd/jev-fact-checker</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · lookfwd

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Uses Typesafe AI Jev to Provide A Tweet Fact Checker

</details>

<details>
<summary><b><a href="https://github.com/manikanda-kumar/jev-dspy-control-plane">manikanda-kumar/jev-dspy-control-plane</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · MIT · manikanda-kumar

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-poker">meetr1912/jev-poker</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · meetr1912

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 4 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Watch Jev (TypeSafe) play heads-up No-Limit Hold'em, with decision probabilities on the side panel. Money/points scoreboard, offline CI, no secrets.

</details>

<details>
<summary><b><a href="https://github.com/memorysaver/jev-atari-lab">memorysaver/jev-atari-lab</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · GPL-2.0 · memorysaver

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Challenge Atari with Jev: structured decisions, value questions, and replayable experiments

</details>

<details>
<summary><b><a href="https://github.com/MrDesjardins/jev-send-guard">MrDesjardins/jev-send-guard</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · MrDesjardins

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/Nachom3/jevTrader">Nachom3/jevTrader</a></b> — Rust · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Rust · Nachom3

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A High Frecuncy Trader made in Rust using Jev as a decision maker.

</details>

<details>
<summary><b><a href="https://github.com/nardinmarcus/pi-jev-typesafe">nardinmarcus/pi-jev-typesafe</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · nardinmarcus

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model discovery, and budget caps

</details>

<details>
<summary><b><a href="https://github.com/Nolane-x/JEV-language">Nolane-x/JEV-language</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · Nolane-x

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 2 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/oguressive/sample-jev">oguressive/sample-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · oguressive

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/silverzzzzz/jev-binaryoption">silverzzzzz/jev-binaryoption</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · MIT · silverzzzzz

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/sperictao/dsh-auto-review-jev">sperictao/dsh-auto-review-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · sperictao

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/thisisjorge/jev-control-room">thisisjorge/jev-control-room</a></b> — TypeScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · thisisjorge

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Interactive control room for fast typed AI decisions with TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/TonyP-MR/jev-curation-engine">TonyP-MR/jev-curation-engine</a></b> — Python · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · TonyP-MR

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions with existing LLM audit results.

</details>

<details>
<summary><b><a href="https://github.com/toshitoshi-creator/jev-chat-site">toshitoshi-creator/jev-chat-site</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · toshitoshi-creator

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/trungdq88/jev-tetris">trungdq88/jev-tetris</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · trungdq88

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Jev play Tetris in real-time against other AI models

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/trungdq88/jev-tetris/main/docs/screenshot.png" width="100%" alt="trungdq88/jev-tetris screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

<sub>Zasób podlinkowany bezpośrednio z repozytorium źródłowego, ponieważ nie zadeklarowano licencji pozwalającej na redystrybucję.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Tsagaanbayr1/jev-tetris">Tsagaanbayr1/jev-tetris</a></b> — JavaScript · inferred · 0 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · Tsagaanbayr1

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Real-time Tetris versus Jev, a TypeSafe decision model — spins, garbage, B2B chains, and decisions prefetched a piece ahead

</details>

<details>
<summary><b><a href="https://github.com/TurboGuo/jev-fedspeech">TurboGuo/jev-fedspeech</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · TurboGuo

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Real-time hawk-or-dove analysis of Fed press conferences with TypeSafe's Jev vs chat models. Live at fedspeech.pages.dev

</details>

<details>
<summary><b><a href="https://github.com/wakamenod/jev.el">wakamenod/jev.el</a></b> — Emacs Lisp · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Emacs Lisp · GPL-3.0 · wakamenod

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/waynesutton/ask-jev-ai">waynesutton/ask-jev-ai</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · waynesutton

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

A public wall where anyone asks a question in three to fifteen words and Jev, TypeSafe's judgment model, answers yes, no, or it depends in about 100 milliseconds. Every judged ask lands on the wall in realtime, with a running count toward one million, showing cost.

</details>

<details>
<summary><b><a href="https://github.com/yuki-dev26/jev-test">yuki-dev26/jev-test</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · JavaScript · yuki-dev26

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-18 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Nie opublikowano opisu ze strony źródłowej.

</details>

<details>
<summary><b><a href="https://github.com/zaycruz/fast-jev-compaction-pi">zaycruz/fast-jev-compaction-pi</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · TypeScript · MIT · zaycruz

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

Verbatim Jev-guided context compaction for pi — replaces the built-in compaction summary with fast-jev decisions; stale tool calls/results dropped, everything kept stays verbatim.

</details>

<details>
<summary><b><a href="https://github.com/Zogrus/jev-technical-term">Zogrus/jev-technical-term</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `inferred` · Python · MIT · Zogrus

##### Dane

Gwiazdki **0** · Forki 0 · Otwarte zgłoszenia 0 · Utworzono 2026-09-19 · Ostatni push 2026-09-19 · Pierwsze dodanie 2026-09-19

##### Podsumowanie

YouTubeの解説動画やZoomのセミナーを聞きながら、出てきた技術用語のひとこと解説をリアルタイム表示するローカルツール(判定AIは TypeSafe AI の Jev)

</details>

<details>
<summary><b><a href="https://github.com/realZachi/typesafe-adblock">realZachi/typesafe-adblock</a></b> — ⭐49 · JavaScript · unverified · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `unverified` · JavaScript · MIT · realZachi

##### Dane

Gwiazdki **49** · Forki 4 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.

</details>

<details>
<summary><b><a href="https://github.com/razorback16/openjev">razorback16/openjev</a></b> — ⭐42 · Python · unverified · 0 天 · ⭐+6</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `unverified` · Python · Apache-2.0 · razorback16

##### Dane

Gwiazdki **42** (+6) · Forki 6 · Otwarte zgłoszenia 1 · Utworzono 2026-09-18 · Ostatni push 2026-09-18 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Open, Jev-compatible System One decision server on DiffusionGemma

</details>

<details>
<summary><b><a href="https://github.com/devanshbatham/commit-miner">devanshbatham/commit-miner</a></b> — ⭐22 · Rust · unverified · 1 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `unverified` · Rust · devanshbatham

##### Dane

Gwiazdki **22** · Forki 5 · Otwarte zgłoszenia 0 · Utworzono 2026-09-17 · Ostatni push 2026-09-17 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.

</details>

<details>
<summary><b><a href="https://github.com/phyous/tsai-sc">phyous/tsai-sc</a></b> — ⭐15 · Python · unverified · 2 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `unverified` · Python · MIT · phyous

##### Dane

Gwiazdki **15** · Forki 1 · Otwarte zgłoszenia 0 · Utworzono 2026-09-16 · Ostatni push 2026-09-16 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.

<table><tr><th align="center" width="50%">Obraz</th><th align="center" width="50%">Wideo</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/phyous--tsai-sc/f48a030ae92fb1fe.png" width="100%" alt="phyous/tsai-sc screenshot"></td>
<td align="center" valign="top"><sub>brak opublikowanych multimediów</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andysc/IBM-Q-System-One-3D-model">andysc/IBM-Q-System-One-3D-model</a></b> — ⭐12 · OpenSCAD · unverified · 2688 天</summary>

##### Podstawowe informacje

`Teksty, dyskusje i pokrewne listy` · Społeczność · `unverified` · OpenSCAD · andysc

##### Dane

Gwiazdki **12** · Forki 4 · Otwarte zgłoszenia 1 · Utworzono 2019-03-16 · Ostatni push 2019-05-10 · Pierwsze dodanie 2026-09-18

##### Podsumowanie

3D-printed model of IBM Q System One

</details>

<a id="projects-by-implementation-language"></a>

## Projekty według języka implementacji

Ekosystem koncentruje się na Pythonie i TypeScripcie, ale typowane klienty wciąż pojawiają się w innych językach. Ta tabela jest generowana z samych wpisów.

| Język      | Wpisy | Przykłady                                                                                                      |
| ---------- | ----- | -------------------------------------------------------------------------------------------------------------- |
| Python     | 157   | `typesafe-ai/system-one-adapter-python`, `typesafe-ai/typesafe-sdk-python`, `ckaraca/awesome-jev`              |
| TypeScript | 136   | `typesafe-ai/typesafe-sdk-js`, `TypeSafeAI/clarity-judge`, `AntonioCoppe/jev-harness`                          |
| JavaScript | 73    | `ziyu/sytem-one-sdk`, `Ying-Kai-Liao/jev-browser`, `arunav25/jev-mcp`                                          |
| Go         | 13    | `RadixILS-Dev/typesafe-sdk-go`, `Gaurav-Gosain/jev-go`, `Stumble/jev-go`                                       |
| Rust       | 13    | `AkashPriyadarshii/jev-curate`, `AkashPriyadarshii/jev-seo`, `AkashPriyadarshii/jev-scout`                     |
| HTML       | 8     | `typesafe-ai/typesafe-ai.github.io`, `yzfly/awesome-jev-zh`, `vinilana/jev-eval-agent`                         |
| Elixir     | 3     | `nshkrdotcom/typesafe_sdk`, `typesend/typesafe_ai`, `dannote/jev`                                              |
| Jupyter    | 3     | `jexp/neo4jev`, `bitnovus/jev-spam-eval`, `aamanlamba/jev-explore`                                             |
| PHP        | 3     | `Butochnikov/laravel-typesafe-jev`, `juanlentino/jev-connector`, `soderlind/ai-provider-for-jev`               |
| Ruby       | 3     | `javiergradiche/ruby_llm-providers-typesafe`, `obie/ruby_decision_model`, `robzolkos/omarchy-issue-classifier` |
| Shell      | 3     | `realZachi/pg-jev`, `wotai-dev/typesafe-jev-tools`, `JYeswak/jev_playground`                                   |
| Java       | 2     | `Premo-Cloud/typesafe-sdk-java`, `Olti1947/jev-java`                                                           |
| Swift      | 2     | `gpazo/jev-vphone-cli`, `chris-wozniczek/jev-voice-control`                                                    |
| Astro      | 1     | `kong75/jev-directory`                                                                                         |
| C          | 1     | `giuliosmall/pg_typesafe`                                                                                      |
| C#         | 1     | `saibimajdi/typesafeai-dotnet-sdk`                                                                             |
| C++        | 1     | `amansoory/JEV2048`                                                                                            |
| CSS        | 1     | `AbdelStark/awesome-typesafe`                                                                                  |
| Dart       | 1     | `Bud-ro/jev-demos`                                                                                             |
| Emacs Lisp | 1     | `wakamenod/jev.el`                                                                                             |
| Haskell    | 1     | `inanna-malick/jev-dsl`                                                                                        |
| Kotlin     | 1     | `ufec/jev-block-android-ad`                                                                                    |
| Lex        | 1     | `alpibrusl/lex-judge`                                                                                          |
| Nushell    | 1     | `cablehead/jev.nu`                                                                                             |
| OpenSCAD   | 1     | `andysc/IBM-Q-System-One-3D-model`                                                                             |
| PowerShell | 1     | `omni-/ask-jev`                                                                                                |
| Scala      | 1     | `jamesward/jev-llm-c4`                                                                                         |
| TeX        | 1     | `dnakhoa/jev-deferred-crispification`                                                                          |

<sub>Liczone są tylko wpisy, które deklarują język. Wpisy dotyczące infrastruktury, dokumentacji i dyskusji są wyłączone z tej tabeli.</sub>

## Jak ta lista pozostaje aktualna

Żaden człowiek nie edytuje treści tego README. Repozytorium uruchamia według harmonogramu potok złożony z pięciu etapów i zatwierdza zmiany tylko wtedy, gdy coś faktycznie się zmieniło.

<img src="assets/readme/pipeline.svg" width="100%" alt="Jak ta lista pozostaje aktualna">

|             |                                                                                                                                                                                                                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **collect** | wyszukiwanie w GitHubie po macierzy zapytań, oficjalna organizacja, wyszukiwanie kodu w GitHubie, Hacker News i hub Hugging Face.                                                                                                                                                    |
| **curate**  | deterministyczny i bez LLM, więc dwa kolejne uruchomienia na tych samych danych dają wynik identyczny bajt w bajt. O trafności decyduje reguła dwóch sygnałów; kolizje nazw (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD i podobne) są wykluczane przez jawną, audytowalną listę. |
| **media**   | zbiera własne zrzuty ekranu i nagrania ekranu każdego projektu. Zasoby są kopiowane do tego repozytorium tylko wtedy, gdy projekt deklaruje licencję przyjazną redystrybucji; w przeciwnym razie źródłowy URL jest podlinkowany bezpośrednio, a karta to odnotowuje.                 |
| **render**  | tworzy każde wydanie językowe z jednego szablonu, dzięki czemu dwadzieścia plików README nigdy nie rozjadą się strukturalnie.                                                                                                                                                        |
| **audit**   | przerywa budowanie, jeśli wpisowi brakuje URL-a, jeśli link jest martwy, jeśli dwa wpisy powtarzają ten sam URL albo jeśli README odbiega od swojej wygenerowanej postaci.                                                                                                           |

## Współtworzenie

Poprawki są mile widziane i są najszybszym sposobem ulepszenia tej listy. Otwórz zgłoszenie lub pull request, jeśli wpis jest źle zakwalifikowany, źle oceniony albo jeśli projekt został błędnie wykluczony jako kolizja nazw — ta ostatnia kategoria to miejsce, w którym automatyczne filtry najczęściej się mylą. Uzupełnienia najlepiej wprowadzać, dodając źródło do `scripts/collect.py`, a nie edytując README, ponieważ README jest generowany od nowa w każdym cyklu.

---

<sub>Niezależny projekt społecznościowy. Niepowiązany z TypeSafe AI, niepopierany przez nią ani przez nią niepoddawany przeglądowi. Zachowanie produktu, ceny, limity i aliasy modeli zmieniają się bez ostrzeżenia; wszystko, co ma znaczenie krytyczne, weryfikuj w oficjalnej dokumentacji. Zasoby pozostają własnością swoich projektów źródłowych i są reprodukowane wyłącznie tam, gdzie pozwala na to licencja.</sub>

<sub>Wygenerowano przez · `render.py` · 2026-09-19T10:20:34+08:00</sub>
