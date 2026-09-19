<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>2 時間ごとに自己再構築される、証拠格付け付きの Jev インデックス。</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-488-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <b>日本語</b> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **ライブインデックス** · 最終同期: `2026-09-19T10:20:34+08:00` (UTC+8)
> · エントリ数: **488** · 今回の追加: **71** · 実装言語: **28**

<sub>以下の各エントリは、本リポジトリのパイプラインが収集・選別・再確認したものです。数値とタイムスタンプは取得元に基づくものであり、手書きのスナップショットではありません。</sub>

## 目次

- [Jev とは？](#jev-とは)
- [エントリの格付け方法](#エントリの格付け方法)
- [公式 SDK と開発者ツール](#公式-sdk-と開発者ツール) — **6**
- [コミュニティ製のクライアント、SDK、アダプタ](#コミュニティ製のクライアントsdkアダプタ) — **74**
- [エージェントツール：MCP、フック、ゲート、コーディングエージェント](#エージェントツールmcpフックゲートコーディングエージェント) — **144**
- [ルーティング、ガードレール、承認](#ルーティングガードレール承認) — **48**
- [評価、キャリブレーション、ベンチマーク](#評価キャリブレーションベンチマーク) — **39**
- [公開再現、重み、アーキテクチャ研究](#公開再現重みアーキテクチャ研究) — **19**
- [アプリケーション、ゲーム、ロボティクス、インタラクティブデモ](#アプリケーションゲームロボティクスインタラクティブデモ) — **42**
- [記事、ディスカッション、類似リスト](#記事ディスカッション類似リスト) — **116**
- [実装言語別のプロジェクト](#実装言語別のプロジェクト)
- [このリストが最新に保たれる仕組み](#このリストが最新に保たれる仕組み)

## Jev とは？

Jev は TypeSafe AI 初の **System One model** です。文章を書くものではありません。状態と、答えの空間をあらかじめ自分で定義する質問を受け取り、コードが分岐に使える確率分布付きの型付き値を返します。

|              |                                                                                               |
| ------------ | --------------------------------------------------------------------------------------------- |
| **形：**       | `state + typed questions` → `constrained answers + probabilities` → `your code`               |
| **プリミティブ：**  | `Choice`（≤255 個の選択肢から 1 つを選ぶ）、`Score`（2〜10 のルーブリック）、`Noul`（確率的な yes/no）                       |
| **エンドポイント：** | `POST https://api.typesafe.ai/v1/systemone`、モデル `jev-1.13.0` / 別名 `jev-latest`                |
| **適した用途：**   | 境界の定まったワークフロー内でのルーティング、トリアージ、スコアリング、モデレーション、検証、低レイテンシのゲート                                     |
| **既知の限界：**   | 計数は信頼できず、多段の間接参照は弱く、公式資料は九種類のギザギザさを挙げています。スキーマに適合した出力は正しい判断と同じではありません。自分のデータでキャリブレーションしてください。 |

## エントリの格付け方法

この分野の多くのリストは掲載を主張するだけです。本リストは、実際にどこまで検証したかを示し、それに応じて絞り込めるようにします。

| 格付け          | 意味                                                                 |
| ------------ | ------------------------------------------------------------------ |
| `official`   | TypeSafe AI 自身が公開。                                                 |
| `observed`   | 開いて読める公開成果物。実際のソース、実際の設定、あるいはリポジトリ名やトピックにおける TypeSafe/Jev の明示的な宣言。 |
| `inferred`   | 曖昧なシグナルと裏付けとなる語彙による一致であり、まだ行単位で読んではいない。                            |
| `unverified` | 関連がありそうだが、独立に確認されたものはない。発見目的のみで掲載。                                 |

<a id="official-sdk"></a>

## 公式 SDK と開発者ツール

TypeSafe 自身が公開したものすべて。まずはここから。

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐285 · official · 6 天 · ⭐+24</summary>

##### 基本情報

`公式 SDK と開発者ツール` · 公式 · `official` · MIT · typesafe-ai

##### データ

スター数 **285** (+24) · フォーク数 17 · 未解決の issue 1 · 作成日 2026-08-24 · 最終プッシュ 2026-09-12 · 初回掲載 2026-09-18

##### 概要

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐134 · TypeScript · official · 3 天 · ⭐+6</summary>

##### 基本情報

`公式 SDK と開発者ツール` · 公式 · `official` · TypeScript · MIT · typesafe-ai

##### データ

スター数 **134** (+6) · フォーク数 10 · 未解決の issue 6 · 作成日 2026-09-04 · 最終プッシュ 2026-09-15 · 初回掲載 2026-09-18

##### 概要

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐124 · Python · official · 0 天 · ⭐+3</summary>

##### 基本情報

`公式 SDK と開発者ツール` · 公式 · `official` · Python · MIT · typesafe-ai

##### データ

スター数 **124** (+3) · フォーク数 13 · 未解決の issue 0 · 作成日 2026-08-08 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>コード内での使用を確認: `README.md`, `src/system_one_adapter/__init__.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐92 · Python · official · 0 天 · ⭐+8</summary>

##### 基本情報

`公式 SDK と開発者ツール` · 公式 · `official` · Python · MIT · typesafe-ai

##### データ

スター数 **92** (+8) · フォーク数 9 · 未解決の issue 2 · 作成日 2026-09-04 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>コード内での使用を確認: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 106 天</summary>

##### 基本情報

`公式 SDK と開発者ツール` · 公式 · `official` · HTML · typesafe-ai

##### データ

スター数 **1** · フォーク数 1 · 未解決の issue 1 · 作成日 2024-05-28 · 最終プッシュ 2026-06-04 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/TypeSafeAI/clarity-judge">TypeSafeAI/clarity-judge</a></b> — ⭐1 · TypeScript · official · 0 天 · **NEW**</summary>

##### 基本情報

`公式 SDK と開発者ツール` · 公式 · `official` · TypeScript · TypeSafeAI

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Multi-axis writing quality checker powered by TypeSafe AI's Jev model. Separate named checks, each with its own verdict and confidence.

</details>

<a id="community-sdk"></a>

## コミュニティ製のクライアント、SDK、アダプタ

System One エンドポイント向けの型付きクライアント。コミュニティが着手した言語の数だけ存在します。

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐20 · Jupyter · observed · 0 天 · ⭐+3</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Jupyter · MIT · jexp

##### データ

スター数 **20** (+3) · フォーク数 5 · 未解決の issue 1 · 作成日 2026-09-16 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐3 · Rust · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Rust · MIT · AkashPriyadarshii

##### データ

スター数 **3** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/ckaraca/awesome-jev">ckaraca/awesome-jev</a></b> — ⭐3 · Python · observed · 0 天 · **NEW**</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Python · CC0-1.0 · ckaraca

##### データ

スター数 **3** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

A curated list of tools, integrations, and experiments built on Jev, TypeSafe AI's System One model for fast, typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — ⭐3 · Java · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Java · MIT · Premo-Cloud

##### データ

スター数 **3** · フォーク数 1 · 未解決の issue 2 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · TypeScript · MIT · AntonioCoppe

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Python · CC0-1.0 · MrJev

##### データ

スター数 **2** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐2 · Elixir · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Elixir · MIT · nshkrdotcom

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · TypeScript · opaielsheikh

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Python · xingwudao

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · JavaScript · MIT · ziyu

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/gpazo/jev-vphone-cli">gpazo/jev-vphone-cli</a></b> — Swift · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Swift · MIT · gpazo

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Jev from Typesafe.ai + vphone-cli

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gpazo--jev-vphone-cli/baa413a8104308f4.jpg" width="100%" alt="gpazo/jev-vphone-cli screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Ruby · MIT · javiergradiche

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · TypeScript · MIT · nu-sync

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/RadixILS-Dev/typesafe-sdk-go">RadixILS-Dev/typesafe-sdk-go</a></b> — Go · observed · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Go · MIT · RadixILS-Dev

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A typesafe.ai client written in golang

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `observed` · Elixir · MIT · typesend

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐169 · Shell · inferred · 0 天 · ⭐+5</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Shell · NOASSERTION · realZachi

##### データ

スター数 **169** (+5) · フォーク数 10 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pinecone-io/cultivar">pinecone-io/cultivar</a></b> — ⭐39 · Python · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · pinecone-io

##### データ

スター数 **39** · フォーク数 2 · 未解決の issue 5 · 作成日 2026-06-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐32 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · nidhi-singh02

##### データ

スター数 **32** (+1) · フォーク数 1 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">視聴先 img.youtube.com</a> · 再生はホストサイト側で開きます。GitHub にはインラインで埋め込めません</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/tacticocc/Jevbridge">tacticocc/Jevbridge</a></b> — ⭐17 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · tacticocc

##### データ

スター数 **17** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tacticocc--jevbridge/772995670b3e42e9.png" width="100%" alt="tacticocc/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐14 · Python · inferred · 0 天 · ⭐+4</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · AboveColin

##### データ

スター数 **14** (+4) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Ask your house a question, get a number back. Home Assistant integration for TypeSafe Jev: typed answers as sensors, four actions for automations, and a conversation agent for Assist.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abovecolin--ha-jev/87fa9143f6990ef1.png" width="100%" alt="AboveColin/HA-Jev screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐13 · Elixir · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Elixir · MIT · dannote

##### データ

スター数 **13** (+1) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐13 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · shiftynick

##### データ

スター数 **13** · フォーク数 1 · 未解決の issue 4 · 作成日 2026-09-16 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shiftynick--jev-axi/e97a8238f41de3c1.gif" width="100%" alt="shiftynick/jev-axi screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shiftynick--jev-axi/e97a8238f41de3c1.gif" width="100%" alt="shiftynick/jev-axi animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐12 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · JavaScript · MIT · Ying-Kai-Liao

##### データ

スター数 **12** (+1) · フォーク数 3 · 未解決の issue 3 · 作成日 2026-09-16 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/keltokhy/jgrep">keltokhy/jgrep</a></b> — ⭐7 · Python · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · keltokhy

##### データ

スター数 **7** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.

</details>

<details>
<summary><b><a href="https://github.com/arunav25/jev-mcp">arunav25/jev-mcp</a></b> — ⭐5 · JavaScript · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · JavaScript · MIT · arunav25

##### データ

スター数 **5** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.

</details>

<details>
<summary><b><a href="https://github.com/Nasrallah-AL/jev-cli">Nasrallah-AL/jev-cli</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · Nasrallah-AL

##### データ

スター数 **5** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Command-line tool for TypeSafe's Jev AI model

</details>

<details>
<summary><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">saibimajdi/typesafeai-dotnet-sdk</a></b> — ⭐5 · C# · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · C# · MIT · saibimajdi

##### データ

スター数 **5** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-16 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/sharziki/semdecide">sharziki/semdecide</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · sharziki

##### データ

スター数 **5** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.

</details>

<details>
<summary><b><a href="https://github.com/frostney/clean-code-review">frostney/clean-code-review</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · frostney

##### データ

スター数 **4** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/frostney--clean-code-review/7d8a8de446e1c27b.png" width="100%" alt="frostney/clean-code-review screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rhighs/jev-code">rhighs/jev-code</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · rhighs

##### データ

スター数 **4** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/assets/jev-code-logo.png" width="100%" alt="rhighs/jev-code screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/docs/media/session.gif" width="100%" alt="rhighs/jev-code animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/romaluev/jev-ego">romaluev/jev-ego</a></b> — ⭐4 · TypeScript · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · NOASSERTION · romaluev

##### データ

スター数 **4** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-19

##### 概要

Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-seo">AkashPriyadarshii/jev-seo</a></b> — ⭐3 · Rust · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Rust · AkashPriyadarshii

##### データ

スター数 **3** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One

</details>

<details>
<summary><b><a href="https://github.com/docxology/daf-jev">docxology/daf-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · docxology

##### データ

スター数 **3** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill

</details>

<details>
<summary><b><a href="https://github.com/EugeneBoondock/jevsql">EugeneBoondock/jevsql</a></b> — ⭐3 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · JavaScript · MIT · EugeneBoondock

##### データ

スター数 **3** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

SQL with natural-language predicates, powered by TypeSafe's Jev. Filter, rank, classify and score rows by meaning — batched, cached and cost-guarded.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/eugeneboondock--jevsql/d6bbe6cf6a2d2e8c.png" width="100%" alt="EugeneBoondock/jevsql screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Olti1947/jev-java">Olti1947/jev-java</a></b> — ⭐3 · Java · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Java · Olti1947

##### データ

スター数 **3** · フォーク数 1 · 未解決の issue 8 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Idiomatic Java SDK for TypeSafe AI Jev System One decision engine

</details>

<details>
<summary><b><a href="https://github.com/burnigtm/jev-mcp">burnigtm/jev-mcp</a></b> — ⭐2 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · burnigtm

##### データ

スター数 **2** (+1) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client

</details>

<details>
<summary><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Butochnikov/laravel-typesafe-jev</a></b> — ⭐2 · PHP · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · PHP · MIT · Butochnikov

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes.

</details>

<details>
<summary><b><a href="https://github.com/ddfeyes/jev-mode">ddfeyes/jev-mode</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · ddfeyes

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no deps, MIT.

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-go">Gaurav-Gosain/jev-go</a></b> — ⭐2 · Go · inferred · 2 天 · ⭐+1</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Go · MIT · Gaurav-Gosain

##### データ

スター数 **2** (+1) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/ibrahemid/git-jev-stage">ibrahemid/git-jev-stage</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · ibrahemid

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Select Git changes for staging with a plain-language description.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Stumble/jev-go">Stumble/jev-go</a></b> — ⭐2 · Go · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Go · MIT · Stumble

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Community Go SDK for TypeSafe AI Jev / System One

</details>

<details>
<summary><b><a href="https://github.com/tontoko/jev-browser">tontoko/jev-browser</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · JavaScript · Apache-2.0 · tontoko

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 3 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.

</details>

<details>
<summary><b><a href="https://github.com/tumf/jev-cli">tumf/jev-cli</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · tumf

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Small dependency-free CLI for TypeSafe Jev

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tumf--jev-cli/f90f005044872607.png" width="100%" alt="tumf/jev-cli screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tumf--jev-cli/f69b319352312892.gif" width="100%" alt="tumf/jev-cli animation"><br><sub>アニメーション記録 · <a href="https://raw.githubusercontent.com/tumf/jev-cli/main/assets/jev-cli-terminal-demo.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/yzfly/awesome-jev-zh">yzfly/awesome-jev-zh</a></b> — ⭐2 · HTML · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · HTML · CC0-1.0 · yzfly

##### データ

スター数 **2** · フォーク数 3 · 未解決の issue 3 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/jevclient">AboveColin/jevclient</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · AboveColin

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-scout">AkashPriyadarshii/jev-scout</a></b> — ⭐1 · Rust · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Rust · MIT · AkashPriyadarshii

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring

</details>

<details>
<summary><b><a href="https://github.com/anilsenay/jev">anilsenay/jev</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Go · MIT · anilsenay

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Unofficial Go client for TypeSafe's System One API  and its model, Jev.

</details>

<details>
<summary><b><a href="https://github.com/felpsdev/jev-classifier">felpsdev/jev-classifier</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · felpsdev

##### データ

スター数 **1** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/felpsdev--jev-classifier/d753de26b0e6c7b6.webp" width="100%" alt="felpsdev/jev-classifier screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gmaxxxie/jev-cli">gmaxxxie/jev-cli</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · gmaxxxie

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/himomohi/aside-jev">himomohi/aside-jev</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · himomohi

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.

</details>

<details>
<summary><b><a href="https://github.com/StefanoITA/ts-jev-cost-calculator">StefanoITA/ts-jev-cost-calculator</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · StefanoITA

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe.

</details>

<details>
<summary><b><a href="https://github.com/zhirschtritt/typesafe-go">zhirschtritt/typesafe-go</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Go · MIT · zhirschtritt

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Idiomatic Go SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/33Audits/jev-auto">33Audits/jev-auto</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · JavaScript · MIT · 33Audits

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Per-turn model routing for Claude Code. Cheapest tier that can do the job, no API key required, and it calibrates itself from what actually happened.

</details>

<details>
<summary><b><a href="https://github.com/acharyaanusha/magic-jev">acharyaanusha/magic-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · acharyaanusha

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

A Magic Jev (8) Ball for pull requests.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/acharyaanusha--magic-jev/f58dfd5f54b0ae6c.gif" width="100%" alt="acharyaanusha/magic-jev animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">AkashPriyadarshii/jev-superpowers</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · JavaScript · MIT · AkashPriyadarshii

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions

</details>

<details>
<summary><b><a href="https://github.com/brnyxx/jev-ra">brnyxx/jev-ra</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · brnyxx

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 2 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7592fce4641d10.png" width="100%" alt="brnyxx/jev-ra screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7ddcd1053825a2.gif" width="100%" alt="brnyxx/jev-ra animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/david1gp/jev">david1gp/jev</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · david1gp

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Result-based TypeSafe System One client library and jev command-line interface.

</details>

<details>
<summary><b><a href="https://github.com/egma-ai/jev-reviewer">egma-ai/jev-reviewer</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · JavaScript · MIT · egma-ai

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Review behavior, not just diffs. Jev prioritizes human attention; OpenAI explains the changes. Local CLI + agent skill + GitHub extension.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/egma-ai--jev-reviewer/db97b1dd85958e4d.png" width="100%" alt="egma-ai/jev-reviewer screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/krw82/jev-playwright-mcp">krw82/jev-playwright-mcp</a></b> — TypeScript · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · krw82

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.

</details>

<details>
<summary><b><a href="https://github.com/Kushwho/jev-codes">Kushwho/jev-codes</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · MIT · Kushwho

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Audit your git diff against YAML coding-standards packs using TypeSafe's Jev model, from a CLI or your AI agent's command/skill.

</details>

<details>
<summary><b><a href="https://github.com/lhotwll217/jev-cli">lhotwll217/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · TypeScript · lhotwll217

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

JSON-in, typed-decisions-out CLI for the TypeSafe System One API

</details>

<details>
<summary><b><a href="https://github.com/mhmdkzr/jev">mhmdkzr/jev</a></b> — Go · inferred · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Go · MIT · mhmdkzr

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

An unofficial Go client for TypeSafe's System One Jev model

</details>

<details>
<summary><b><a href="https://github.com/model-clis/jev">model-clis/jev</a></b> — Rust · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Rust · MIT · model-clis

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Typed judgment CLI for the Jev model (TypeSafe System One): state + questions in, calibrated answers and exit codes out

</details>

<details>
<summary><b><a href="https://github.com/nandansrikrishna/jev-agent-tool">nandansrikrishna/jev-agent-tool</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · MIT · nandansrikrishna

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Bring-your-own-key CLI, Python API, and MCP server for typed judgments with TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing">nekowasabi/jev-routing</a></b> — Go · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Go · MIT · nekowasabi

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.

</details>

<details>
<summary><b><a href="https://github.com/SAGAR-TAMANG/sarvam-jev">SAGAR-TAMANG/sarvam-jev</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Python · SAGAR-TAMANG

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Generation-free typed decisions on Indic LLMs. An open Jev-style inference engine on sarvam-1: constrained logit readout instead of autoregressive JSON. Runs client-side in the browser.

</details>

<details>
<summary><b><a href="https://github.com/yannip1234/codex-jev">yannip1234/codex-jev</a></b> — Rust · inferred · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `inferred` · Rust · Apache-2.0 · yannip1234

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 11 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Experimental Jev compression for Codex, with a macOS menu bar launcher, desktop bridge, and native client.

</details>

<details>
<summary><b><a href="https://github.com/giuliosmall/pg_typesafe">giuliosmall/pg_typesafe</a></b> — ⭐76 · C · unverified · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `unverified` · C · MIT · giuliosmall

##### データ

スター数 **76** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification

</details>

<details>
<summary><b><a href="https://github.com/pithings/advocaat">pithings/advocaat</a></b> — ⭐74 · TypeScript · unverified · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `unverified` · TypeScript · MIT · pithings

##### データ

スター数 **74** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/obie/ruby_decision_model">obie/ruby_decision_model</a></b> — ⭐34 · Ruby · unverified · 0 天 · ⭐+2</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `unverified` · Ruby · MIT · obie

##### データ

スター数 **34** (+2) · フォーク数 2 · 未解決の issue 18 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Ruby client for decision models such as Typesafe Jev

</details>

<details>
<summary><b><a href="https://github.com/Brainwires/jevwire">Brainwires/jevwire</a></b> — ⭐5 · TypeScript · unverified · 0 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `unverified` · TypeScript · MIT · Brainwires

##### データ

スター数 **5** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/typesafe-cli">y0usaf/typesafe-cli</a></b> — ⭐4 · TypeScript · unverified · 2 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `unverified` · TypeScript · MIT · y0usaf

##### データ

スター数 **4** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose

</details>

<details>
<summary><b><a href="https://github.com/geilt/typesafe-cli">geilt/typesafe-cli</a></b> — ⭐3 · Python · unverified · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `unverified` · Python · geilt

##### データ

スター数 **3** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.

</details>

<details>
<summary><b><a href="https://github.com/gilljon/typesafe-ai-rs">gilljon/typesafe-ai-rs</a></b> — ⭐3 · Rust · unverified · 1 天</summary>

##### 基本情報

`コミュニティ製のクライアント、SDK、アダプタ` · コミュニティ · `unverified` · Rust · MIT · gilljon

##### データ

スター数 **3** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Independent async and blocking Rust SDK for the TypeSafe AI System One API

</details>

<a id="agent-tooling"></a>

## エージェントツール：MCP、フック、ゲート、コーディングエージェント

最も伸びているカテゴリ。エージェントの次の行動の前に型付きの判断を差し込むフック、MCP サーバー、ゲート。

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐3310 · TypeScript · observed · 0 天 · ⭐+114</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · TypeScript · MIT · tamaratran

##### データ

スター数 **3310** (+114) · フォーク数 166 · 未解決の issue 45 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>コード内での使用を確認: `src/request.ts`, `README.md`, `src/client.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐144 · JavaScript · inferred · 0 天 · ⭐+6</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · gargpratyush

##### データ

スター数 **144** (+6) · フォーク数 5 · 未解決の issue 5 · 作成日 2026-09-16 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐46 · Python · inferred · 1 天 · ⭐+2</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · 0xNatoshi

##### データ

スター数 **46** (+2) · フォーク数 3 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐104 · observed · 1 天 · ⭐+1</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · dbreunig

##### データ

スター数 **104** (+1) · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐17 · Python · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · Python · MIT · GhalebDweikat

##### データ

スター数 **17** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/valentynkit/awesome-jev-typesafe">valentynkit/awesome-jev-typesafe</a></b> — ⭐8 · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · CC0-1.0 · valentynkit

##### データ

スター数 **8** · フォーク数 3 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Typed decisions with TypeSafe's Jev, the first System One model

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · Python · MIT · carlaiau

##### データ

スター数 **7** · フォーク数 1 · 未解決の issue 6 · 作成日 2026-03-13 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/kraayenjon/awesome-jev">kraayenjon/awesome-jev</a></b> — ⭐6 · observed · 0 天 · ⭐+2</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · NOASSERTION · kraayenjon

##### データ

スター数 **6** (+2) · フォーク数 1 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · Python · MIT · jodan-alberts

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/rajdhakad9826/routeKit">rajdhakad9826/routeKit</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · TypeScript · MIT · rajdhakad9826

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Agent-native LLM model router built with JEV by TypeSafe.ai. Dynamically selects the most suitable model based on task complexity, reasoning requirements, and tool usage.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · TypeScript · MIT · BYK

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/emirbartu/opencode-system-one">emirbartu/opencode-system-one</a></b> — ⭐1 · TypeScript · observed · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · TypeScript · emirbartu

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Opencode plugin using Jev (system one model) as part of software development process. Not affiliated with Opencode team.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · Python · MIT · 24601

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/codaaiteam/jev-typesafe-ai">codaaiteam/jev-typesafe-ai</a></b> — observed · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · codaaiteam

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Unofficial developer notes & examples for Jev, TypeSafe AI's System One model. Try it free: jevtypesafeai.com

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · TypeScript · CrowBe

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · TypeScript · MIT · gorock007

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/uipath-jev-guardrail-connector">jms-dcksn/uipath-jev-guardrail-connector</a></b> — JavaScript · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · JavaScript · jms-dcksn

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

UiPath bring-your-own-guardrail connector backed by the TypeSafe Jev System One model: plain-language agent policies enforced as calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/knowlet/jev-agentworld-web-simulator">knowlet/jev-agentworld-web-simulator</a></b> — TypeScript · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · TypeScript · MIT · knowlet

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

An entire internet — search, pages & links — hallucinated on the fly by the System One Model.

</details>

<details>
<summary><b><a href="https://github.com/Wany-i/jev-decision-layer">Wany-i/jev-decision-layer</a></b> — Python · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · Python · MIT · Wany-i

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

把决策模型（typesafe/jev-1.13，经 OpenRouter 的 decisions 端点调用）封装成业务决策工具：注册表驱动，带置信度门控与硬约束。非官方项目。

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `observed` · Python · MIT · yousudip

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐275 · TypeScript · inferred · 2 天 · ⭐+8</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · devagrawal09

##### データ

スター数 **275** (+8) · フォーク数 14 · 未解決の issue 1 · 作成日 2026-09-16 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐123 · TypeScript · inferred · 1 天 · ⭐+4</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · NiazMorshed2007

##### データ

スター数 **123** (+4) · フォーク数 9 · 未解決の issue 2 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐120 · JavaScript · inferred · 0 天 · ⭐+11</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · fatwang2

##### データ

スター数 **120** (+11) · フォーク数 14 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/wy-coliney/jev-browser-use">wy-coliney/jev-browser-use</a></b> — ⭐109 · JavaScript · inferred · 0 天 · ⭐+15</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · wy-coliney

##### データ

スター数 **109** (+15) · フォーク数 4 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wy-coliney--jev-browser-use/581fbd89fe47c952.png" width="100%" alt="wy-coliney/jev-browser-use screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-eval-agent">vinilana/jev-eval-agent</a></b> — ⭐86 · HTML · inferred · 1 天 · ⭐+2</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · HTML · vinilana

##### データ

スター数 **86** (+2) · フォーク数 8 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-mcp">jkudish/jev-mcp</a></b> — ⭐73 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · jkudish

##### データ

スター数 **73** · フォーク数 10 · 未解決の issue 2 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools.

> An early proof of concept for exposing Jev over MCP, which is how most non-Python toolchains reach it.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/pi-jev">y0usaf/pi-jev</a></b> — ⭐68 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · y0usaf

##### データ

スター数 **68** (+1) · フォーク数 3 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers

</details>

<details>
<summary><b><a href="https://github.com/RomanSlack/jev-drone">RomanSlack/jev-drone</a></b> — ⭐63 · Python · inferred · 2 天 · ⭐+2</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · RomanSlack

##### データ

スター数 **63** (+2) · フォーク数 3 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/romanslack--jev-drone/b23ea2412f437970.png" width="100%" alt="RomanSlack/jev-drone screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/supercorp-ai/supercov">supercorp-ai/supercov</a></b> — ⭐35 · Rust · inferred · 0 天 · ⭐+2</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Rust · MIT · supercorp-ai

##### データ

スター数 **35** (+2) · フォーク数 1 · 未解決の issue 0 · 作成日 2026-08-23 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Code quality and coverage for coding agents

> Code quality and coverage verdicts produced as typed decisions rather than prose, so the result can gate a pipeline directly.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/supercorp-ai--supercov/063226e150cb8a6b.jpg" width="100%" alt="supercorp-ai/supercov screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/logicrw/awesome-jev-projects">logicrw/awesome-jev-projects</a></b> — ⭐33 · JavaScript · inferred · 0 天 · ⭐+4</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · logicrw

##### データ

スター数 **33** (+4) · フォーク数 8 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/ask-jev-skill">shantanugoel/ask-jev-skill</a></b> — ⭐30 · Python · inferred · 1 天 · ⭐+1</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · shantanugoel

##### データ

スター数 **30** (+1) · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Skill for Hermes, and other agents, to ask typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/tamaratran/jev-pruner">tamaratran/jev-pruner</a></b> — ⭐15 · TypeScript · inferred · 0 天 · ⭐+5</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · tamaratran

##### データ

スター数 **15** (+5) · フォーク数 1 · 未解決の issue 7 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Claude Code plugin: trim long Bash output with TypeSafe Jev before the model sees it

</details>

<details>
<summary><b><a href="https://github.com/DanRWilloughby/snifftest">DanRWilloughby/snifftest</a></b> — ⭐14 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · DanRWilloughby

##### データ

スター数 **14** · フォーク数 0 · 未解決の issue 3 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/TheoOliveira/pi-jev">TheoOliveira/pi-jev</a></b> — ⭐14 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · TheoOliveira

##### データ

スター数 **14** (+1) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/kbhuw/jev-sift">kbhuw/jev-sift</a></b> — ⭐13 · JavaScript · inferred · 0 天 · ⭐+9</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · kbhuw

##### データ

スター数 **13** (+9) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification.

</details>

<details>
<summary><b><a href="https://github.com/compozy/yoshi">compozy/yoshi</a></b> — ⭐12 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · compozy

##### データ

スター数 **12** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/compozy--yoshi/637d8588c227f4de.png" width="100%" alt="compozy/yoshi screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">jomatsu/pi-jev-auto-mode</a></b> — ⭐12 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · jomatsu

##### データ

スター数 **12** (+1) · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.

</details>

<details>
<summary><b><a href="https://github.com/BillionsBobby/JevRouter">BillionsBobby/JevRouter</a></b> — ⭐11 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · BillionsBobby

##### データ

スター数 **11** (+4) · フォーク数 1 · 未解決の issue 4 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A lightweight Jev-powered router for models, tools, and subagents

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/billionsbobby--jevrouter/f0e638219505d5da.png" width="100%" alt="BillionsBobby/JevRouter screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/blakestone-x/jev-mcp">blakestone-x/jev-mcp</a></b> — ⭐9 · Python · inferred · 2 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · blakestone-x

##### データ

スター数 **9** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer

</details>

<details>
<summary><b><a href="https://github.com/huntedman/JevLint">huntedman/JevLint</a></b> — ⭐9 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · huntedman

##### データ

スター数 **9** (+1) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.

</details>

<details>
<summary><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">DECRUX9812/typesafe-skill-router</a></b> — ⭐7 · Python · inferred · 2 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · DECRUX9812

##### データ

スター数 **7** · フォーク数 1 · 未解決の issue 1 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-code">devagrawal09/jev-code</a></b> — ⭐6 · TypeScript · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · devagrawal09

##### データ

スター数 **6** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Bounded TypeSafe Jev workflows for coding agents.

</details>

<details>
<summary><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">GodsBoy/jev-agent-skill-router</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · GodsBoy

##### データ

スター数 **5** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Typed, confidence-aware agent skill routing with TypeSafe Jev.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/godsboy--jev-agent-skill-router/c80293e37dcd4faf.png" width="100%" alt="GodsBoy/jev-agent-skill-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/inanna-malick/jev-dsl">inanna-malick/jev-dsl</a></b> — ⭐5 · Haskell · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Haskell · MIT · inanna-malick

##### データ

スター数 **5** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels

</details>

<details>
<summary><b><a href="https://github.com/matthewp/flue-jev-demo">matthewp/flue-jev-demo</a></b> — ⭐5 · TypeScript · inferred · 0 天 · ⭐+3</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · matthewp

##### データ

スター数 **5** (+3) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Flue agent routing with TypeSafe Jev through Cloudflare AI Gateway

</details>

<details>
<summary><b><a href="https://github.com/anpicasso/hermes-jev-approvals">anpicasso/hermes-jev-approvals</a></b> — ⭐4 · Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · anpicasso

##### データ

スター数 **4** · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only.

</details>

<details>
<summary><b><a href="https://github.com/GiesN/typesafe-jev-workflow">GiesN/typesafe-jev-workflow</a></b> — ⭐4 · Python · inferred · 2 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · GiesN

##### データ

スター数 **4** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/runta-dev/jot">runta-dev/jot</a></b> — ⭐4 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · runta-dev

##### データ

スター数 **4** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

The first general-purpose System One agent for Jev

</details>

<details>
<summary><b><a href="https://github.com/anandi1989/awesome-jev-usecases">anandi1989/awesome-jev-usecases</a></b> — ⭐3 · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · MIT · anandi1989

##### データ

スター数 **3** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-mcp">rashedInt32/jev-mcp</a></b> — ⭐3 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · rashedInt32

##### データ

スター数 **3** (+1) · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/SeeAPI/awesome-jev-use-cases">SeeAPI/awesome-jev-use-cases</a></b> — ⭐3 · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · CC-BY-4.0 · SeeAPI

##### データ

スター数 **3** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-align">caiovicentino/jev-align</a></b> — ⭐2 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · caiovicentino

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Calibrated alignment verifier for LLM responses and agent plans — powered by Jev

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-shield">caiovicentino/jev-shield</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · caiovicentino

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check.

</details>

<details>
<summary><b><a href="https://github.com/doeixd/jev-pref">doeixd/jev-pref</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · doeixd

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-model-router-demo">jcpsimmons/jev-model-router-demo</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · jcpsimmons

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

</details>

<details>
<summary><b><a href="https://github.com/molis-ai/jev-workbench">molis-ai/jev-workbench</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · molis-ai

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/molis-ai--jev-workbench/00f61d8403a941cd.png" width="100%" alt="molis-ai/jev-workbench screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MongLong0214/jev-gate">MongLong0214/jev-gate</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MongLong0214

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 5 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.

</details>

<details>
<summary><b><a href="https://github.com/morcoan/JevSeek">morcoan/JevSeek</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · morcoan

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools, persistent sessions, React desktop, and documented research.

</details>

<details>
<summary><b><a href="https://github.com/noetion/dsh-jev">noetion/dsh-jev</a></b> — ⭐2 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · noetion

##### データ

スター数 **2** (+1) · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.

</details>

<details>
<summary><b><a href="https://github.com/ranjan2829/AskJev">ranjan2829/AskJev</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · ranjan2829

##### データ

スター数 **2** · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)

</details>

<details>
<summary><b><a href="https://github.com/samtay32/jev-system-architect">samtay32/jev-system-architect</a></b> — ⭐2 · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · MIT · samtay32

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives.

</details>

<details>
<summary><b><a href="https://github.com/Zaious/jev-capability-atlas">Zaious/jev-capability-atlas</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · NOASSERTION · Zaious

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。

</details>

<details>
<summary><b><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher">abhishekashokvkumar/jev-mcp-dispatcher</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · abhishekashokvkumar

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Natural-language MCP tool dispatcher powered entirely by TypeSafe's Jev — no general-purpose LLM. Discovers a simple MCP server's tool signatures at runtime and uses Jev's typed primitives (Choice/Noul) to pick the right tool and extract its arguments straight out of the sentence.

</details>

<details>
<summary><b><a href="https://github.com/bestagentkits/jev-skillful">bestagentkits/jev-skillful</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · bestagentkits

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.

</details>

<details>
<summary><b><a href="https://github.com/cephalization/jev-oxlint">cephalization/jev-oxlint</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · cephalization

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Digest your skills into oxlint rules powered by jev

</details>

<details>
<summary><b><a href="https://github.com/CrowdLinker/JevPromptCoach">CrowdLinker/JevPromptCoach</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · CrowdLinker

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Claude Code plugin that scores how well you prompt a coding agent, and shows whether your habits are improving. Runs on TypeSafe's Jev model. Zero added latency.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/crowdlinker--jevpromptcoach/5340815130cd47ba.png" width="100%" alt="CrowdLinker/JevPromptCoach screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Dharundp6/jev-carryforward">Dharundp6/jev-carryforward</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · Dharundp6

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written as things happen, recalled per task with TypeSafe's Jev evaluation model via Vercel AI Gateway.

</details>

<details>
<summary><b><a href="https://github.com/Friedjof/jev-mobile">Friedjof/jev-mobile</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · Friedjof

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Fast structured Android control loops with TypeSafe Jev and Mobile MCP

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-starter">hamakyo/jev-starter</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · hamakyo

##### データ

スター数 **1** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-codex-plugin">integrate-your-mind/jev-codex-plugin</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · integrate-your-mind

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Open-source Codex plugin for TypeSafe Jev decision consultation, failure diagnosis, and evidence-based completion review

</details>

<details>
<summary><b><a href="https://github.com/jcressler/fast-jev-compaction-codex">jcressler/fast-jev-compaction-codex</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · jcressler

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Task-aware Jev evidence selection and exact local recovery around native Codex compaction.

</details>

<details>
<summary><b><a href="https://github.com/khordoo/jev-reflex-autonomy-lab">khordoo/jev-reflex-autonomy-lab</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · khordoo

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/khordoo/jev-reflex-autonomy-lab/main/docs/media/reflex-dashboard.png" width="100%" alt="khordoo/jev-reflex-autonomy-lab screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/omni-/ask-jev">omni-/ask-jev</a></b> — ⭐1 · PowerShell · inferred · 2 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · PowerShell · MIT · omni-

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions.

</details>

<details>
<summary><b><a href="https://github.com/poponline63/hermes-jev-north-star">poponline63/hermes-jev-north-star</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · poponline63

##### データ

スター数 **1** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven.

</details>

<details>
<summary><b><a href="https://github.com/RahulBalakavi/claude-code-jev">RahulBalakavi/claude-code-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · RahulBalakavi

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Experimental Jev permission gate for Claude Code via OpenRouter, with reproducible latency and cost benchmarks

</details>

<details>
<summary><b><a href="https://github.com/Ravinder82/jev-flash-router">Ravinder82/jev-flash-router</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · Ravinder82

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code

</details>

<details>
<summary><b><a href="https://github.com/rthomas24/jev-realtime-trading">rthomas24/jev-realtime-trading</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · rthomas24

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rthomas24--jev-realtime-trading/f27df5cca6b8e2cf.png" width="100%" alt="rthomas24/jev-realtime-trading screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Saik0s/diffusiongemma-jev-macos">Saik0s/diffusiongemma-jev-macos</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · Saik0s

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Local JEV-style decisions with DiffusionGemma on Apple Silicon, with benchmarks and coding-agent examples.

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/codex-jev-compaction">Wang-auspicious/codex-jev-compaction</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · Wang-auspicious

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills.

</details>

<details>
<summary><b><a href="https://github.com/wotai-dev/typesafe-jev-tools">wotai-dev/typesafe-jev-tools</a></b> — ⭐1 · Shell · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Shell · MIT · wotai-dev

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 149-row comparison of TypeSafe Jev against Claude Haiku 4.5.

</details>

<details>
<summary><b><a href="https://github.com/altregubov/jev-antigravity-mcp">altregubov/jev-antigravity-mcp</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · altregubov

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/alviso/jev-precheck">alviso/jev-precheck</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · alviso

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A second signature on every write an AI agent makes into a system of record. MCP proxy: fetch the records, derive in code, Jev judges. 98.6% recall, 0 false holds on 288 cases.

</details>

<details>
<summary><b><a href="https://github.com/andyholst/hermes-typesafe-jev">andyholst/hermes-typesafe-jev</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · NOASSERTION · andyholst

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 6 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

TypeSafe Jev MCP server for Hermes Agent — Choice, Noul, Score as first-class tools

</details>

<details>
<summary><b><a href="https://github.com/anisselbd/jev-phishing-bench">anisselbd/jev-phishing-bench</a></b> — Python · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · anisselbd

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/openclaw-jev-harness">AntonioCoppe/openclaw-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · AntonioCoppe

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

OpenClaw plugin: jev-harness DecisionHarness as System One decide layer (policy/confidence/shadow)

</details>

<details>
<summary><b><a href="https://github.com/AStheTECH/mewcp-jev">AStheTECH/mewcp-jev</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · Apache-2.0 · AStheTECH

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

JEV MCP server by MewCP

</details>

<details>
<summary><b><a href="https://github.com/bidurkhatri/jev-mcp-lab">bidurkhatri/jev-mcp-lab</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · Apache-2.0 · bidurkhatri

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/buberlo/dsh-jev">buberlo/dsh-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · buberlo

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Jev-powered decision layer for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/cbruyndoncx/AskJev-MCP">cbruyndoncx/AskJev-MCP</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · cbruyndoncx

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence

</details>

<details>
<summary><b><a href="https://github.com/de-niji/jev-hermes">de-niji/jev-hermes</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · de-niji

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Jev for Hermes: cheap intent gates + verbatim tool compaction on OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/dizk/pi-jev-lens">dizk/pi-jev-lens</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · dizk

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

pi extension that compresses large tool results before they reach the model: jev picks the view, full text stays recallable

</details>

<details>
<summary><b><a href="https://github.com/DoGMaTiiC/hermes-jev">DoGMaTiiC/hermes-jev</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · DoGMaTiiC

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 7 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only.

</details>

<details>
<summary><b><a href="https://github.com/droid-Q/jev-skill-router">droid-Q/jev-skill-router</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · droid-Q

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/droid-Q/jev-skill-router/main/docs/images/dashboard-en.png" width="100%" alt="droid-Q/jev-skill-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/duketopceo/jev-compact">duketopceo/jev-compact</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · duketopceo

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP

</details>

<details>
<summary><b><a href="https://github.com/EtienneLescot/jev-router">EtienneLescot/jev-router</a></b> — HTML · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · HTML · MIT · EtienneLescot

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model tier and reasoning depth.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/etiennelescot--jev-router/96217fad0b128b3e.png" width="100%" alt="EtienneLescot/jev-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fast-facts/jev-mcp">fast-facts/jev-mcp</a></b> — Go · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Go · MIT · fast-facts

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/flaviusapop/jev-router">flaviusapop/jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · flaviusapop

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Routes each turn in Claude Code, Codex, Grok and opencode to the cheapest model and reasoning depth that can finish it, using TypeSafe Jev

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/flaviusapop--jev-router/b7f868696d35b78b.png" width="100%" alt="flaviusapop/jev-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gzawadzki/jev-usecases">gzawadzki/jev-usecases</a></b> — Python · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · gzawadzki

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage

</details>

<details>
<summary><b><a href="https://github.com/hangarbay/jev.mcp">hangarbay/jev.mcp</a></b> — Go · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Go · MIT · hangarbay

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/its-panzer/jev-model-router">its-panzer/jev-model-router</a></b> — Python · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · its-panzer

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A policy router that picks the cheapest Claude model that can finish the job

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/its-panzer--jev-model-router/98819f5aaf8e6373.png" width="100%" alt="its-panzer/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jh1373/jev-search">jh1373/jev-search</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · jh1373

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Search your Obsidian vault locally and offline with no API key, then rerank the top results with Jev only after you approve exactly what gets sent. Experimental preview.

</details>

<details>
<summary><b><a href="https://github.com/jmanhype/jev-dspy-lab">jmanhype/jev-dspy-lab</a></b> — Python · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · jmanhype

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/jev-pii-guardrail">jms-dcksn/jev-pii-guardrail</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · jms-dcksn

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A UiPath coded agent with a custom PII detection guardrail on the LLM boundary, built on the TypeSafe Jev model as a LangChain awrap_model_call middleware.

</details>

<details>
<summary><b><a href="https://github.com/JoacoMarc/jev-harness-router">JoacoMarc/jev-harness-router</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · JoacoMarc

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Per-turn harness router on Jev (TypeSafe): one batched call picks the model tier, tools, skill and effort budget for an agent turn, behind a hard latency deadline.

</details>

<details>
<summary><b><a href="https://github.com/juanlentino/jev-connector">juanlentino/jev-connector</a></b> — PHP · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · PHP · GPL-2.0 · juanlentino

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

WordPress connector for the TypeSafe System One API (Jev): typed questions, confidence-scored answers, core Connectors API key management

</details>

<details>
<summary><b><a href="https://github.com/jxu-dev-c/jev-adaptive-thinking">jxu-dev-c/jev-adaptive-thinking</a></b> — Go · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Go · jxu-dev-c

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

CLIProxyAPI plugin for Jev-powered session model routing with local debug logs

</details>

<details>
<summary><b><a href="https://github.com/kaijia323/dsh-plugin-jev">kaijia323/dsh-plugin-jev</a></b> — HTML · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · HTML · MIT · kaijia323

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/kerpopule/hermes-jev-skills">kerpopule/hermes-jev-skills</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · kerpopule

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (also Claude Code and Codex)

</details>

<details>
<summary><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">MahmoudAdelbghany/jev-browser</a></b> — JavaScript · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MahmoudAdelbghany

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included.

</details>

<details>
<summary><b><a href="https://github.com/Mandrilsquad1441/jev-model-router">Mandrilsquad1441/jev-model-router</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · Mandrilsquad1441

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Pick the best AI model and reasoning effort for any task in ~1s. Plugin for Claude Code, Claude Desktop and Codex, powered by TypeSafe's Jev decision model and live OpenRouter pricing. Balance intelligence, speed and cost, or choose your priority.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mandrilsquad1441--jev-model-router/6187e7fb04b04c08.png" width="100%" alt="Mandrilsquad1441/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/marcAllari/jev-mcp-router">marcAllari/jev-mcp-router</a></b> — inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · marcAllari

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/micic-mihajlo/jev-tool-runner">micic-mihajlo/jev-tool-runner</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · micic-mihajlo

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/minhgv/jev-mcp">minhgv/jev-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · minhgv

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

TypeSafe Jev MCP decision layer for coding agents and CI

</details>

<details>
<summary><b><a href="https://github.com/mjyoke1111/jev-agent-safety-arena">mjyoke1111/jev-agent-safety-arena</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · mjyoke1111

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Real browser-agent safety evaluation: Jev versus a baseline on benign and injected tasks

</details>

<details>
<summary><b><a href="https://github.com/MSalvalaggio/jev-reflex">MSalvalaggio/jev-reflex</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · MSalvalaggio

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision).

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-mcp">nekowasabi/jev-routing-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · nekowasabi

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/Nyarlathoteppppp/pi-jev-context">Nyarlathoteppppp/pi-jev-context</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · Nyarlathoteppppp

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Cache-neutral context trimming for the pi coding agent, powered by TypeSafe Jev: long tool output cut to verbatim key lines before it enters context, with lossless recall. Measured, with pre-registered benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Panebianco00/jev-claude">Panebianco00/jev-claude</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · Panebianco00

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Route Claude Code's coding decisions through TypeSafe Jev: typed choices with probabilities, enforced at plan approval, questions, and risky commands.

</details>

<details>
<summary><b><a href="https://github.com/pedroknigge/mcp_jev">pedroknigge/mcp_jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · pedroknigge

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 3 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Open MCP server to run TypeSafe Jev (System One) packs locally — Choice / Noul / Score for Cursor & agents

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-mcp-router">Pinutss/jev-mcp-router</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · Pinutss

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Select relevant MCP tools under a context-token budget, without executing them.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-mcp-router/3947a2a5cc3750c8.png" width="100%" alt="Pinutss/jev-mcp-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-memory-selector">Pinutss/jev-memory-selector</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · Pinutss

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-plugins">Pinutss/jev-plugins</a></b> — inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · MIT · Pinutss

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Cursor and Hermes marketplace for the four published JEV Labs routers.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-plugins/b3fcd72ac9e61f49.jpg" width="100%" alt="Pinutss/jev-plugins screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/planstack-ai/jev-tetris-benchmark">planstack-ai/jev-tetris-benchmark</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · planstack-ai

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Reproducible Tetris decision benchmark comparing TypeSafe Jev with Claude Haiku

</details>

<details>
<summary><b><a href="https://github.com/raj8525/universal-jev">raj8525/universal-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · raj8525

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents

</details>

<details>
<summary><b><a href="https://github.com/robbyczgw-cla/hermes-plugin-jev">robbyczgw-cla/hermes-plugin-jev</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · robbyczgw-cla

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

TypeSafe/Jev decision signals for Hermes: turn classification, conservative tool shaping, approvals, and coding verification.

</details>

<details>
<summary><b><a href="https://github.com/rubichandrap/hermes-jev-guard">rubichandrap/hermes-jev-guard</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · rubichandrap

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check

</details>

<details>
<summary><b><a href="https://github.com/sebastianbugal/jev">sebastianbugal/jev</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · sebastianbugal

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

TypeSafe's Jev decision model in Claude Code. Ask in plain language, get a typed answer with a calibrated probability.

</details>

<details>
<summary><b><a href="https://github.com/skeptrunedev/jev-recruiter">skeptrunedev/jev-recruiter</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · skeptrunedev

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

A Jev powered LinkedIn recruiting agent. Watch it browse relevant profiles, save links, and review evidence against your hiring brief.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/skeptrunedev--jev-recruiter/d87f759cfd3422af.png" width="100%" alt="skeptrunedev/jev-recruiter screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/stoopid-computers/jev-bot">stoopid-computers/jev-bot</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · stoopid-computers

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Computer Use Agent developed with Jev

</details>

<details>
<summary><b><a href="https://github.com/sypherin/jev-trace-classifier">sypherin/jev-trace-classifier</a></b> — Python · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · sypherin

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next

</details>

<details>
<summary><b><a href="https://github.com/tgiridhar/claude-code-jev-smart-router">tgiridhar/claude-code-jev-smart-router</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · tgiridhar

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task phase and the cost of an undetected error, gated by prompt-cache arithmetic. Proof of concept.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tgiridhar--claude-code-jev-smart-router/28b9e1b2a005c7e2.png" width="100%" alt="tgiridhar/claude-code-jev-smart-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/thanh-abaii/ud-jev-decision-workflow">thanh-abaii/ud-jev-decision-workflow</a></b> — inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · MIT · thanh-abaii

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/themsquared/jev-benchmark">themsquared/jev-benchmark</a></b> — Python · inferred · 1 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · Apache-2.0 · themsquared

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.

</details>

<details>
<summary><b><a href="https://github.com/thevibeworks/awesome-typesafe-jev">thevibeworks/awesome-typesafe-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · NOASSERTION · thevibeworks

##### データ

スター数 **0** · フォーク数 1 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/thumay9700/jev-plays">thumay9700/jev-plays</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · thumay9700

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Autonomous game agent powered by TypeSafe AI's Jev (System One decision engine), starting with Pokémon Red.

</details>

<details>
<summary><b><a href="https://github.com/trietphan/jev-claw">trietphan/jev-claw</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · trietphan

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Typed model routing for OpenClaw agents, powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/ussyverse/hermes-jev-router">ussyverse/hermes-jev-router</a></b> — Python · inferred · 2 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · ussyverse

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-gateway-bench">vinilana/jev-gateway-bench</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · MIT · vinilana

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Benchmark for jev-gateway: real coding agents on chess engine tasks, with Jev routing on and off

</details>

<details>
<summary><b><a href="https://github.com/yangzhou-chaofan/awesome-jev-prompt">yangzhou-chaofan/awesome-jev-prompt</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · JavaScript · CC0-1.0 · yangzhou-chaofan

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

latest top 100 showcases for jev (keep updating) from x / github / latest sources

</details>

<details>
<summary><b><a href="https://github.com/zbloss/jev-plays-pokemon">zbloss/jev-plays-pokemon</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · Python · MIT · zbloss

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 3 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Like Claude Plays Pokemon, but with Jev

</details>

<details>
<summary><b><a href="https://github.com/zhangxaochen/dsh-jev">zhangxaochen/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `inferred` · TypeScript · MIT · zhangxaochen

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Jev (System One decision model) plugin suite for DeepSeek Harness (dsh)

</details>

<details>
<summary><b><a href="https://github.com/DevMortimer/pi-warden">DevMortimer/pi-warden</a></b> — ⭐64 · TypeScript · unverified · 0 天 · ⭐+1</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `unverified` · TypeScript · MIT · DevMortimer

##### データ

スター数 **64** (+1) · フォーク数 5 · 未解決の issue 3 · 作成日 2026-09-16 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop

> Guardrails that steer an agent before it acts. Demonstrates the gate pattern, where the decision is cheap enough to run on every step.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devmortimer--pi-warden/b8dc20ac6694613a.png" width="100%" alt="DevMortimer/pi-warden screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/pi-quiet-ask">HyunjunJeon/pi-quiet-ask</a></b> — ⭐5 · TypeScript · unverified · 1 天 · ⭐+2</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `unverified` · TypeScript · MIT · HyunjunJeon

##### データ

スター数 **5** (+2) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

TypeSafe Jev as the pi coding agent's quiet decision layer

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hyunjunjeon--pi-quiet-ask/7ee3a99430e853d8.png" width="100%" alt="HyunjunJeon/pi-quiet-ask screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/3clyp50/a0-typesafe-ai">3clyp50/a0-typesafe-ai</a></b> — ⭐4 · Python · unverified · 2 天</summary>

##### 基本情報

`エージェントツール：MCP、フック、ゲート、コーディングエージェント` · コミュニティ · `unverified` · Python · MIT · 3clyp50

##### データ

スター数 **4** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/3clyp50--a0-typesafe-ai/9aa8ea4ef8241f14.png" width="100%" alt="3clyp50/a0-typesafe-ai screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<a id="routing-guardrails"></a>

## ルーティング、ガードレール、承認

本番向きのユースケース。各リクエストを実際に処理できる最も安価なモデルに送り、結果には決定論的な検査を残す。

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐49 · Rust · observed · 0 天 · ⭐+1</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `observed` · Rust · NOASSERTION · Dicklesworthstone

##### データ

スター数 **49** (+1) · フォーク数 5 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 2 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `observed` · Python · MIT · Foadsf

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/Justmalhar/awesome-jev-apps">Justmalhar/awesome-jev-apps</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `observed` · Python · MIT · Justmalhar

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Awesome Collection of apps built with Jev - a System One model

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `observed` · TypeScript · MIT · qddegtya

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 3 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Typed decisions from a System One model, where uncertainty is something you have to handle.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `observed` · Python · aniruddh-krovvidi

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/chy4pro/JevBrowserExt">chy4pro/JevBrowserExt</a></b> — TypeScript · observed · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `observed` · TypeScript · MIT · chy4pro

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

⚡ Ultrafast browser automation Chrome Extension (Manifest V3) powered by TypeSafe Jev (TypeSafe.ai, OpenRouter, Cloudflare)

</details>

<details>
<summary><b><a href="https://github.com/lorensation/llm-cost-optimizer-jev">lorensation/llm-cost-optimizer-jev</a></b> — observed · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `observed` · Apache-2.0 · lorensation

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

An intelligent routing layer powered by TypeSafe AI's System One model Jev that sits in front of multiple LLM providers, analyzes each incoming request’s complexity, routes it to the cheapest model capable of handling it at acceptable quality, and continuously validates that routing decisions are correct.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐28 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · MIT · yusukebe

##### データ

スター数 **28** (+2) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐25 · Python · inferred · 0 天 · ⭐-1</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · brainstormity

##### データ

スター数 **25** (-1) · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐6 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · JavaScript · MIT · mejiasd3v

##### データ

スター数 **6** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · andrelandgraf

##### データ

スター数 **3** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · keeltrace

##### データ

スター数 **3** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · maker-KK

##### データ

スター数 **2** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐2 · Python · inferred · 2 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · prismhq

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/vtrivedy/jev-plays-games">vtrivedy/jev-plays-games</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · JavaScript · vtrivedy

##### データ

スター数 **2** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Chess, Connect Four, and a decision model. Play Jev or watch Jev play itself.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/vtrivedy/jev-plays-games/main/docs/screenshots/chess.jpg" width="100%" alt="vtrivedy/jev-plays-games screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · WiktorB2004

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · Pinutss

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Shashank-H

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Jupyter · MIT · bitnovus

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/buberlo/jev-pastepilot">buberlo/jev-pastepilot</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · MIT · buberlo

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Explicit paste-to-action launcher that routes text to useful tools without automatic side effects.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/buberlo--jev-pastepilot/f9f8b5633a938cb0.png" width="100%" alt="buberlo/jev-pastepilot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/buberlo--jev-pastepilot/590a0f155ae53d69.gif" width="100%" alt="buberlo/jev-pastepilot animation"><br><sub>アニメーション記録 · <a href="https://raw.githubusercontent.com/buberlo/jev-pastepilot/main/docs/demo/pastepilot-core.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/buyukcerci/jev-model-router">buyukcerci/jev-model-router</a></b> — inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Apache-2.0 · buyukcerci

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A multi-provider LLM and media router featuring calibrated confidence classification, dynamic policy scoring, and automated fallback management.

</details>

<details>
<summary><b><a href="https://github.com/carllippert/jev-router">carllippert/jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · MIT · carllippert

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Express with no routes. TypeSafe Jev picks which handler runs.

</details>

<details>
<summary><b><a href="https://github.com/danielhirt/jev-lab">danielhirt/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · danielhirt

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison

</details>

<details>
<summary><b><a href="https://github.com/gnoviawan/omp-jev-tools">gnoviawan/omp-jev-tools</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · NOASSERTION · gnoviawan

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation verification

</details>

<details>
<summary><b><a href="https://github.com/hugo-alves/jev-router-playground">hugo-alves/jev-router-playground</a></b> — JavaScript · inferred · 1 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · JavaScript · MIT · hugo-alves

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Interactive playground for testing Jev model-routing decisions against OpenRouter models

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hugo-alves--jev-router-playground/93692a5f183f12e1.jpg" width="100%" alt="hugo-alves/jev-router-playground screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iefnaf/pi-jev">iefnaf/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · MIT · iefnaf

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Pi extension suite powered by Jev: selective context compaction and model routing

</details>

<details>
<summary><b><a href="https://github.com/immanuelsavio/jev-experiment">immanuelsavio/jev-experiment</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · JavaScript · immanuelsavio

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Benchmarking TypeSafe Jev against general-purpose LLMs on support-ticket routing, with a focus on latency, accuracy, and confidence.

</details>

<details>
<summary><b><a href="https://github.com/jolehuit/jev-downloads-sorter">jolehuit/jev-downloads-sorter</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · jolehuit

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A ~/Downloads folder that sorts itself: one Jev decision per file, launchd WatchPaths, no daemon

</details>

<details>
<summary><b><a href="https://github.com/kenhuangus/jev-usecases">kenhuangus/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · kenhuangus

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kenhuangus--jev-usecases/be919255190f6495.png" width="100%" alt="kenhuangus/jev-usecases screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-bot">kevin9327/jev-bot</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · kevin9327

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.

</details>

<details>
<summary><b><a href="https://github.com/Loule95450/jev-free-router">Loule95450/jev-free-router</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · JavaScript · MIT · Loule95450

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Dynamic per-turn model router on free OpenCode Zen + Go models (fork of gargpratyush/jev-router)

</details>

<details>
<summary><b><a href="https://github.com/makefinks/jev-feed-filter">makefinks/jev-feed-filter</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · MIT · makefinks

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Smart, dynamic AI filtering for X and YouTube feeds using Jev

</details>

<details>
<summary><b><a href="https://github.com/mcgalleg/grokbot-jev-jobs">mcgalleg/grokbot-jev-jobs</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · mcgalleg

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Scores public job postings against my resume using TypeSafe's jev via the Vercel AI Gateway. Daily Vercel cron.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-arena">meetr1912/jev-arena</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · meetr1912

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

A calibration arena for TypeSafe Jev: reliability, Brier/ECE, and confidence-gated risk-coverage on analytically-known random worlds.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-sonar">meetr1912/jev-sonar</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · meetr1912

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

TypeSafe Jev plays Battleship: one ~100-question typed fan-out per turn returns a calibrated hit-probability heatmap that is also the move policy.

</details>

<details>
<summary><b><a href="https://github.com/MoonTory/pi-jev-harness">MoonTory/pi-jev-harness</a></b> — TypeScript · inferred · 1 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · MoonTory

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards tool calls

</details>

<details>
<summary><b><a href="https://github.com/perixtar/jev-e2e">perixtar/jev-e2e</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · MIT · perixtar

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Natural-language end-to-end tests for web apps, powered by Jev and Playwright.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/perixtar--jev-e2e/81a240435b11d6f2.gif" width="100%" alt="perixtar/jev-e2e animation"><br><sub>アニメーション記録 · <a href="https://raw.githubusercontent.com/perixtar/jev-e2e/main/docs/assets/ebay-benchmark.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rajivkuriakose/typesafe-jev-examples">rajivkuriakose/typesafe-jev-examples</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · MIT · rajivkuriakose

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/ravikadam/jev-loan-triage">ravikadam/jev-loan-triage</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · JavaScript · ravikadam

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Voice loan-call triage using TypeSafe Jev: intent, info sufficiency and a lending decision from typed AI judgments

</details>

<details>
<summary><b><a href="https://github.com/SadiqOnGithub/jev-lab">SadiqOnGithub/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · SadiqOnGithub

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API

</details>

<details>
<summary><b><a href="https://github.com/SDTakeuchi/jev-api-router">SDTakeuchi/jev-api-router</a></b> — Go · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Go · SDTakeuchi

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/TokenTrim/jev-routing-experiment">TokenTrim/jev-routing-experiment</a></b> — Python · inferred · 1 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · Apache-2.0 · TokenTrim

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tokentrim--jev-routing-experiment/1c31bd606ebc1994.png" width="100%" alt="TokenTrim/jev-routing-experiment screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ufec/jev-block-android-ad">ufec/jev-block-android-ad</a></b> — Kotlin · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Kotlin · MIT · ufec

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

JevNoiseGate filters unwanted notifications and SMS on Android. Rather than   matching keywords, an LLM decides what's noise — and only what it explicitly   flags is blocked. Verification codes are matched on-device and never uploaded;   anything uncertain passes through.

</details>

<details>
<summary><b><a href="https://github.com/viniciosrab/pi-jev-router">viniciosrab/pi-jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · TypeScript · MIT · viniciosrab

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/Zumka1991/jev-telegram-admin">Zumka1991/jev-telegram-admin</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `inferred` · Python · Zumka1991

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

AI moderator for Telegram groups powered by the Jev (TypeSafe System One) decision model

</details>

<details>
<summary><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">iammrduncan/typesafe-ai-benchmark</a></b> — ⭐32 · TypeScript · unverified · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `unverified` · TypeScript · MIT · iammrduncan

##### データ

スター数 **32** · フォーク数 5 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.

> A gateway that mimics the System One interface, which is what makes side-by-side benchmarking possible without rewriting the caller.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/80d6baf37faa23fb.gif" width="100%" alt="iammrduncan/typesafe-ai-benchmark animation"><br><sub>アニメーション記録 · <a href="https://raw.githubusercontent.com/iammrduncan/typesafe-ai-benchmark/main/docs/media/theater-demo.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kavehmz/typesafe-playground">kavehmz/typesafe-playground</a></b> — ⭐9 · JavaScript · unverified · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `unverified` · JavaScript · kavehmz

##### データ

スター数 **9** · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/kavehmz/typesafe-playground/main/docs/images/demo03-fable.png" width="100%" alt="kavehmz/typesafe-playground screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/raihankhan-rk/diffjury">raihankhan-rk/diffjury</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### 基本情報

`ルーティング、ガードレール、承認` · コミュニティ · `unverified` · TypeScript · raihankhan-rk

##### データ

スター数 **3** · フォーク数 1 · 未解決の issue 2 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

DiffJury — TypeSafe Jev PR risk router + code review coach

</details>

<a id="evaluation"></a>

## 評価、キャリブレーション、ベンチマーク

その判断がどれほど良いかを、誰がどうやって知るのか。キャリブレーションはこのエコシステムの未解決課題であり、ここに挙げたのはそれを測定しているプロジェクトです。

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐5 · Python · observed · 0 天 · ⭐+1</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `observed` · Python · Apache-2.0 · ikermoel

##### データ

スター数 **5** (+1) · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Open-source alternative to TypeSafe's Jev: a System One style model layer that gives typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with honest benchmarks

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `observed` · Python · akash-kamat

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/edgardcham/huncho">edgardcham/huncho</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `observed` · TypeScript · MIT · edgardcham

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Decisions as code on System One models: typed questions, thresholds with hysteresis, nested decisions, journal, calibration

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `observed` · Go · MIT · Gaurav-Gosain

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — ⭐1 · Python · observed · 1 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `observed` · Python · Apache-2.0 · hev

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/nishioka-shinji/jev-edgar">nishioka-shinji/jev-edgar</a></b> — Python · observed · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `observed` · Python · nishioka-shinji

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Does Jev, a System One model returning calibrated probabilities, say anything useful about an earnings release before the market prices it?

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐8 · Python · inferred · 1 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · Apache-2.0 · AbdelStark

##### データ

スター数 **8** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐6 · Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · NOASSERTION · Heman10x-NGU

##### データ

スター数 **6** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/abhixhek/jevcal">abhixhek/jevcal</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · MIT · abhixhek

##### データ

スター数 **5** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abhixhek--jevcal/3dbe2307176737c8.png" width="100%" alt="abhixhek/jevcal screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐5 · TypeScript · inferred · 2 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · TypeScript · MIT · y0usaf

##### データ

スター数 **5** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/cablehead/jev.nu">cablehead/jev.nu</a></b> — ⭐2 · Nushell · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Nushell · MIT · cablehead

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Nushell module for the TypeSafe System One API: typed decisions with calibrated probabilities

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 2 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · MIT · wondertwins

##### データ

スター数 **2** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · 4esv

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

</details>

<details>
<summary><b><a href="https://github.com/carson-sweet/jev-plays-brogue">carson-sweet/jev-plays-brogue</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · TypeScript · AGPL-3.0 · carson-sweet

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

TypeSafe's Jev model plays the roguelike Brogue live -- a hand-built expert system for System-2 reasoning, outcome-calibrated self-learning, and a web UI to watch decisions, costs, and training progress.

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · TypeScript · MIT · Danu28

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · TeX · NOASSERTION · dnakhoa

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · eggmasonvalue

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/ickma2311/jev-baselines-eval">ickma2311/jev-baselines-eval</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · MIT · ickma2311

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Pre-registered independent eval of TypeSafe Jev against a nano-class LLM, a frontier LLM, and a supervised encoder (Banking77 + CLINC150 zero-shot)

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ickma2311--jev-baselines-eval/4cef768bc4898704.png" width="100%" alt="ickma2311/jev-baselines-eval screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · MIT · jujumilk3

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · JavaScript · MIT · KantaHayashiAI

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/KiishiAD/jev-loan-identity-benchmark">KiishiAD/jev-loan-identity-benchmark</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · KiishiAD

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Reproducible synthetic benchmark for temporal loan identity resolution with TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/laurentfabre/databricks-jev-pdf-lab">laurentfabre/databricks-jev-pdf-lab</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · laurentfabre

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Precision PDF extraction research: Databricks + Jev, synthetic tests, selective parsing, measured tradeoffs and negative results.

</details>

<details>
<summary><b><a href="https://github.com/llt22/jev-lab">llt22/jev-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · llt22

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

TypeSafe Jev research, benchmarks, evaluation datasets, and reproducible experiments

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-bracket">meetr1912/jev-bracket</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · MIT · meetr1912

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

TypeSafe Jev predicts a synthetic 32-team tournament in round fan-out: calibrated Brier vs Elo/seed/oracle plus Monte Carlo champion odds.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-vickrey">meetr1912/jev-vickrey</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · MIT · meetr1912

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

TypeSafe Jev bids in sealed-bid auctions: threshold fan-out reconstructs a calibrated value CDF, scored by regret and truthfulness.

</details>

<details>
<summary><b><a href="https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and">musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and</a></b> — HTML · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · HTML · MIT · musman550

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@automatewithmusfiraai"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@automatewithmusfiraai">視聴先 youtube.com</a> · 再生はホストサイト側で開きます。GitHub にはインラインで埋め込めません</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/onlyoneaman/jev-eval">onlyoneaman/jev-eval</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · TypeScript · MIT · onlyoneaman

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/onlyoneaman--jev-eval/e5d471e96e134f81.png" width="100%" alt="onlyoneaman/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rorshopping/jev-browser-local">rorshopping/jev-browser-local</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · NOASSERTION · rorshopping

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Run jev-browser on a fully local JEV-style decision engine (no cloud API). Warm-browser fork, VRAM guard, measured benchmarks, run traces.

</details>

<details>
<summary><b><a href="https://github.com/SHAKULMITTAL22/jev-resume">SHAKULMITTAL22/jev-resume</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · AGPL-3.0 · SHAKULMITTAL22

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Folio: job-specific resume leaderboards with approved rubrics, evidence-backed AI evaluation, and human hiring decisions.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shakulmittal22--jev-resume/e653593f3a00df9d.png" width="100%" alt="SHAKULMITTAL22/jev-resume screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shunta-furukawa/jev-tick-lab">shunta-furukawa/jev-tick-lab</a></b> — inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · shunta-furukawa

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis.

</details>

<details>
<summary><b><a href="https://github.com/teyhouse/jev-secret-detection">teyhouse/jev-secret-detection</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · teyhouse

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" width="100%" alt="teyhouse/jev-secret-detection screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/thisisandreeeee/jev-benchmarks">thisisandreeeee/jev-benchmarks</a></b> — inferred · 0 天 · **NEW**</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · MIT · thisisandreeeee

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/us/jev-local">us/jev-local</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · us

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Local Jev-compatible evaluation server: POST /v1/systemone with typed noul/choice/score, open weights, no waitlist

</details>

<details>
<summary><b><a href="https://github.com/yodablocks/jev-orderby-bench">yodablocks/jev-orderby-bench</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `inferred` · Python · MIT · yodablocks

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev.

</details>

<details>
<summary><b><a href="https://github.com/kyotofin/tax-doc-classifier">kyotofin/tax-doc-classifier</a></b> — ⭐130 · TypeScript · unverified · 0 天 · ⭐+17</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `unverified` · TypeScript · Apache-2.0 · kyotofin

##### データ

スター数 **130** (+17) · フォーク数 12 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.

</details>

<details>
<summary><b><a href="https://github.com/Mapika/decider">Mapika/decider</a></b> — ⭐25 · Python · unverified · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `unverified` · Python · Apache-2.0 · Mapika

##### データ

スター数 **25** · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mapika--decider/c67d355f22dcb51a.gif" width="100%" alt="Mapika/decider animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/genai-craft/openvons">genai-craft/openvons</a></b> — ⭐7 · Python · unverified · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `unverified` · Python · NOASSERTION · genai-craft

##### データ

スター数 **7** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド

</details>

<details>
<summary><b><a href="https://github.com/aabolfazl/typesafe-local">aabolfazl/typesafe-local</a></b> — ⭐6 · Python · unverified · 0 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `unverified` · Python · MIT · aabolfazl

##### データ

スター数 **6** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/aabolfazl--typesafe-local/ada59cf382af5143.png" width="100%" alt="aabolfazl/typesafe-local screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mithalouni/system-one-open">mithalouni/system-one-open</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### 基本情報

`評価、キャリブレーション、ベンチマーク` · コミュニティ · `unverified` · Python · NOASSERTION · mithalouni

##### データ

スター数 **4** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal)

</details>

<a id="research-models"></a>

## 公開再現、重み、アーキテクチャ研究

公開された重み、小型の再現実装、アーキテクチャ研究。これらのいくつかが存在するのは、公開資料だけではキャリブレーションの挙動を再現できないからです。

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐63 · Python · observed · 0 天 · ⭐+1</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `observed` · Python · MIT · kshetrajna12

##### データ

スター数 **63** (+1) · フォーク数 4 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐395 · Python · inferred · 1 天 · ⭐+25</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · MIT · TianyuCodings

##### データ

スター数 **395** (+25) · フォーク数 37 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/5055af419619e7e4.gif" width="100%" alt="TianyuCodings/NanoJev animation"><br><sub>アニメーション記録 · <a href="https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/assets/side_by_side_maze.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐22 · Python · inferred · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · MIT · r-ms

##### データ

スター数 **22** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/imserhatdemir/jevspace">imserhatdemir/jevspace</a></b> — HTML · observed · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `observed` · HTML · imserhatdemir

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A DarkOrbit-style space game piloted by Jev — TypeSafe's System One model. Three.js world, deterministic engine, Jev picks the targets.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/imserhatdemir/jevspace/main/docs/screenshot-win.png" width="100%" alt="imserhatdemir/jevspace screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `observed`

##### データ

ダウンロード数 25 · いいね数 4 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 1 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `observed`

##### データ

ダウンロード数 0 · いいね数 0 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐160 · Python · inferred · 0 天 · ⭐+6</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · ekzhang

##### データ

スター数 **160** (+6) · フォーク数 12 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/featherless-ai/simple-jev">featherless-ai/simple-jev</a></b> — ⭐70 · Python · inferred · 0 天 · ⭐+13</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · featherless-ai

##### データ

スター数 **70** (+13) · フォーク数 6 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Turn any open model into a classifier/jev endpoint

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/featherless-ai/simple-jev/main/imgs/Simple-Jev-Logo.png" width="100%" alt="featherless-ai/simple-jev screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐24 · Python · inferred · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · MIT · bnsd55

##### データ

スター数 **24** · フォーク数 3 · 未解決の issue 6 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/siliconkernel/vllm-jev-decison">siliconkernel/vllm-jev-decison</a></b> — ⭐8 · Python · inferred · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · MIT · siliconkernel

##### データ

スター数 **8** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Classification-only typed decisions for vLLM: finite-schema candidate scoring, probabilities, and abstention. No generative fallback.

</details>

<details>
<summary><b><a href="https://github.com/wfzyx/von">wfzyx/von</a></b> — ⭐4 · Python · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · wfzyx

##### データ

スター数 **4** (+1) · フォーク数 1 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/choxos/jev-reviewer">choxos/jev-reviewer</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · JavaScript · MIT · choxos

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay in your browser.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/4a551dbca9d0c41e.jpg" width="100%" alt="choxos/jev-reviewer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/71abea319063ce6d.gif" width="100%" alt="choxos/jev-reviewer animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/deep-diver/mini-jev">deep-diver/mini-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · deep-diver

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/kw2828/OpenJev">kw2828/OpenJev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · MIT · kw2828

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Browser decision playground and reproducible experiments on memory, uncertainty, and Doom control

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/7caa9b0eff4636a1.png" width="100%" alt="kw2828/OpenJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/af5371a3a94cb693.gif" width="100%" alt="kw2828/OpenJev animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/backmeupplz/jev_antispam_bot">backmeupplz/jev_antispam_bot</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · TypeScript · MIT · backmeupplz

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">legacybridge-tech/pi-typesafe-jev</a></b> — TypeScript · inferred · 1 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · TypeScript · NOASSERTION · legacybridge-tech

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.

</details>

<details>
<summary><b><a href="https://github.com/NeU-dev/reddit-jev-sentiment-analyzer">NeU-dev/reddit-jev-sentiment-analyzer</a></b> — inferred · 0 天 · **NEW**</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · NeU-dev

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

A non-commercial personal research prototype for numerical sentiment analysis of public Reddit technology discussions using JEV.

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `inferred` · Python · shellneko

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐9 · Python · unverified · 2 天 · ⭐+1</summary>

##### 基本情報

`公開再現、重み、アーキテクチャ研究` · コミュニティ · `unverified` · Python · NOASSERTION · zhihz

##### データ

スター数 **9** (+1) · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<a id="apps-demos"></a>

## アプリケーション、ゲーム、ロボティクス、インタラクティブデモ

ゲーム、ロボット、ブラウザ、ダッシュボード。レイテンシとコストに関する主張が読める形になるのは、デモを通じてです。

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐10 · Python · observed · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `observed` · Python · Apache-2.0 · zadescoxp

##### データ

スター数 **10** · フォーク数 1 · 未解決の issue 3 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `observed` · TypeScript · daftAI2026

##### データ

スター数 **2** · フォーク数 2 · 未解決の issue 2 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `observed` · Rust · MIT · markjaquith

##### データ

スター数 **1** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `observed` · TypeScript · adiun

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `observed` · Dart · Bud-ro

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/chris-wozniczek/jev-voice-control">chris-wozniczek/jev-voice-control</a></b> — Swift · observed · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `observed` · Swift · chris-wozniczek

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-bar Swift app.

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `observed` · Python · MIT · tirukovelamanoj

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/04e4dd3a1f6c6bae.gif" width="100%" alt="tirukovelamanoj/jev-plays-doom animation"><br><sub>アニメーション記録 · <a href="https://raw.githubusercontent.com/tirukovelamanoj/jev-plays-doom/main/docs/jev-doom.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `observed` · TypeScript · wustep

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://x.com/tspy/status/2100864234523685146">X intent labeller</a></b> — @tspy · observed · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `observed` · [yishan](https://x.com/tspy) · @tspy · x.com

##### データ

表示回数 2364 · いいね数 15 · コメント数 9 · 投稿日 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A Chrome extension that labels posts in an X timeline with their intent and probability as you scroll, drawn as a tag directly after each post's timestamp. Categories include inducement, provocation, promotion, machine-generated, persuasion, entertainment and information. A side panel reports session counts (seen, judged, correct) and cumulative token cost. The author reports near-instant responses and usable accuracy before any tuning.

<sub>元のプロジェクトへのリンクを確認中です。</sub>

> Worth reading as a latency argument rather than an accuracy one: labelling a timeline only works if the decision costs less than the scroll, which is the constraint a generative model cannot meet.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/0641644f12a25a45.jpg" width="100%" alt="X intent labeller screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/b80cf3173f63bdd7.gif" width="100%" alt="X intent labeller animation"><br><sub>アニメーション記録 · <a href="https://video.twimg.com/amplify_video/2100858340331200512/vid/avc1/1242x720/ex2FF5-TerVxo9xX.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐111 · Python · inferred · 0 天 · ⭐+2</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Python · MIT · hr98w

##### データ

スター数 **111** (+2) · フォーク数 12 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐108 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · TypeScript · MIT · jkudish

##### データ

スター数 **108** (+4) · フォーク数 5 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/d9b7631c25d7db06.gif" width="100%" alt="jkudish/jev-browser animation"><br><sub>アニメーション記録 · <a href="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐79 · JavaScript · inferred · 1 天 · ⭐+8</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · MIT · moritzkremb

##### データ

スター数 **79** (+8) · フォーク数 8 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/mizchi/jev-playground">mizchi/jev-playground</a></b> — ⭐15 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · TypeScript · mizchi

##### データ

スター数 **15** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐7 · Python · inferred · 1 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Python · MIT · komorra

##### データ

スター数 **7** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐7 · JavaScript · inferred · 0 天 · ⭐+2</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · vinilana

##### データ

スター数 **7** (+2) · フォーク数 5 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · TypeScript · emrickgarrett

##### データ

スター数 **5** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 1 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Go · MIT · paulsmith

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · TypeScript · MIT · vmendes90

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/vmendes90--jev-shield/ee87b261d199a34c.jpg" width="100%" alt="vmendes90/jev-shield screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0x7067/jev-browse">0x7067/jev-browse</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · MIT · 0x7067

##### データ

スター数 **1** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Browser automation with Jev (TypeSafe) as decision model

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/6b2906f1131adf4c.gif" width="100%" alt="0x7067/jev-browse screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/3efc4d3b381ff9f5.gif" width="100%" alt="0x7067/jev-browse animation"><br><sub>アニメーション記録 · <a href="https://raw.githubusercontent.com/0x7067/jev-browse/main/docs/demo.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/charleeagni/JevPiano">charleeagni/JevPiano</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · charleeagni

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

@typesafeai 's Jev controls the 2 hands and each finger to play the piano in real-time.  Jev only "sees" what we see and plays this from the "note waterfall". It uses  @browser_use 's jev-ultrafast and some decision scheduling to make this happen in real-time.  Sound on 🔈🔉🔊

</details>

<details>
<summary><b><a href="https://github.com/finetuningsingh/jev-chatbot">finetuningsingh/jev-chatbot</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · MIT · finetuningsingh

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Experiment: using TypeSafe Jev as a chatbot by choosing replies one letter or word at a time

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · TypeScript · Little-Planet-Labs

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 2 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Python · PistachioAIHQ

##### データ

スター数 **1** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/acharyaanusha/magic-jev-demo">acharyaanusha/magic-jev-demo</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · acharyaanusha

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 6 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Sample pull requests for demoing Magic Jev. The code is filler.

</details>

<details>
<summary><b><a href="https://github.com/bahramzada/jev-taxi-dispatch">bahramzada/jev-taxi-dispatch</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · MIT · bahramzada

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Real-vaxt taksi dispetçerlik simulyasiyası - TypeSafe JEV (System One) modeli ilə

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/bahramzada--jev-taxi-dispatch/e616f4168b15d3f2.png" width="100%" alt="bahramzada/jev-taxi-dispatch screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/BrendanH18/jev-lab">BrendanH18/jev-lab</a></b> — Python · inferred · 1 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Python · MIT · BrendanH18

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brendanh18--jev-lab/b16b9535e3744cd3.png" width="100%" alt="BrendanH18/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/chahero/driving-jev">chahero/driving-jev</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Python · chahero

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Watch TypeSafe Jev make highway driving decisions. Includes live API and offline gameplay previews.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev-preview.gif" width="100%" alt="chahero/driving-jev screenshot"></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev.mp4"><img src="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev-preview.gif" width="100%" alt="chahero/driving-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev.mp4">動画を開く</a></sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/ethereumdegen/jev-discord-bot">ethereumdegen/jev-discord-bot</a></b> — Rust · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Rust · MIT · ethereumdegen

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/formigacamuflada/jev-computer-use">formigacamuflada/jev-computer-use</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Python · formigacamuflada

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/gua-project/gua-sample-jev-racinggame">gua-project/gua-sample-jev-racinggame</a></b> — inferred · 0 天 · **NEW**</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · gua-project

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/JYeswak/jev_playground">JYeswak/jev_playground</a></b> — Shell · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Shell · MIT · JYeswak

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jyeswak--jev_playground/b6414da07c9c5aa8.jpg" width="100%" alt="JYeswak/jev_playground screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Keitark/jev-gamebook-demo">Keitark/jev-gamebook-demo</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Python · Keitark

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/metrox-eth/moss-jev">metrox-eth/moss-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · metrox-eth

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

MOSS × Jev: a recorded-run 3D demo of the litter-picking rover choosing targets with TypeSafe's Jev decision model.

</details>

<details>
<summary><b><a href="https://github.com/n3ndor/n8n-nodes-typesafe-jev">n3ndor/n8n-nodes-typesafe-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · TypeScript · MIT · n3ndor

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

n8n community node for TypeSafe Jev structured AI decisions

</details>

<details>
<summary><b><a href="https://github.com/parzivale/jev-bot">parzivale/jev-bot</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · Rust · parzivale

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Discord bot that scores how likely a statement is to be true, using TypeSafe's jev model

</details>

<details>
<summary><b><a href="https://github.com/PierrunoYT/JevFlow">PierrunoYT/JevFlow</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · TypeScript · PierrunoYT

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A trading bot powered by TypeSafe AI's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pistachiopranay/jev-synergy-screening">pistachiopranay/jev-synergy-screening</a></b> — inferred · 2 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · pistachiopranay

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/rchovatiya88/cyber-breach-jev">rchovatiya88/cyber-breach-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · rchovatiya88

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model

</details>

<details>
<summary><b><a href="https://github.com/rikkooo/jev-trade">rikkooo/jev-trade</a></b> — inferred · 0 天 · **NEW**</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · rikkooo

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

A market-data trading simulator powered by auditable Jev judgments

</details>

<details>
<summary><b><a href="https://github.com/SuryaManavalan/JevNash">SuryaManavalan/JevNash</a></b> — inferred · 0 天 · **NEW**</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · SuryaManavalan

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Jev harness for playing or working, agnostic of the game or workstream.

</details>

<details>
<summary><b><a href="https://github.com/tanayvasishtha/Slither-Me-Jev">tanayvasishtha/Slither-Me-Jev</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `inferred` · JavaScript · tanayvasishtha

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

8 AI snakes, 1 human, 1 arena. Every snake is driven live by TypeSafe's Jev, making all decisions in real time

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/tanayvasishtha/Slither-Me-Jev/main/menu-screenshot.png" width="100%" alt="tanayvasishtha/Slither-Me-Jev screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/sorrycc/typesafe-snake">sorrycc/typesafe-snake</a></b> — ⭐17 · TypeScript · unverified · 1 天</summary>

##### 基本情報

`アプリケーション、ゲーム、ロボティクス、インタラクティブデモ` · コミュニティ · `unverified` · TypeScript · sorrycc

##### データ

スター数 **17** · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code

</details>

<a id="media-discussions"></a>

## 記事、ディスカッション、類似リスト

ローンチスレッド、独立した記事、この分野の他のキュレーションリスト。本リポジトリは唯一ではなく、そう明言するほうが、そうでないふりをするより有用です。

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐5671 · Python · observed · 0 天 · ⭐+200</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · Python · MIT · browser-use

##### データ

スター数 **5671** (+200) · フォーク数 361 · 未解決の issue 34 · 作成日 2026-09-16 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

i. am. speed.

<sub>コード内での使用を確認: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcdb919ac3afb514.gif" width="100%" alt="browser-use/jev-ultrafast animation"><br><sub>アニメーション記録 · <a href="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/demo.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1890 · observed · 3 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 1890 · コメント数 496 · 最終プッシュ 2026-09-15 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐529 · Python · observed · 0 天 · ⭐+9</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · Python · MIT · Anil-matcha

##### データ

スター数 **529** (+9) · フォーク数 102 · 未解決の issue 4 · 作成日 2023-05-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>コード内での使用を確認: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐235 · TypeScript · observed · 0 天 · ⭐+16</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · TypeScript · dabit3

##### データ

スター数 **235** (+16) · フォーク数 20 · 未解決の issue 17 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

<sub>コード内での使用を確認: `jev-lint/proxy.mjs`</sub>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐232 · CSS · observed · 0 天 · ⭐+8</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · CSS · MIT · AbdelStark

##### データ

スター数 **232** (+8) · フォーク数 34 · 未解決の issue 2 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>コード内での使用を確認: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐181 · Python · observed · 0 天 · ⭐+16</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · Python · yibie

##### データ

スター数 **181** (+16) · フォーク数 25 · 未解決の issue 13 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐118 · observed · 0 天 · ⭐+5</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · CC0-1.0 · cobanov

##### データ

スター数 **118** (+5) · フォーク数 12 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐67 · observed · 0 天 · ⭐+2</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · CC0-1.0 · AnotiaWang

##### データ

スター数 **67** (+2) · フォーク数 19 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>コード内での使用を確認: `README.md`, `README_zh.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐52 · observed · 1 天 · ⭐+1</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 52 · コメント数 12 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐37 · JavaScript · observed · 0 天 · ⭐+4</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### データ

スター数 **37** (+4) · フォーク数 10 · 未解決の issue 10 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A community directory of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐11 · JavaScript · observed · 0 天 · ⭐+2</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · JavaScript · NOASSERTION · OmniJev

##### データ

スター数 **11** (+2) · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Papers, open reproductions and independent evaluations behind System One models and Jev.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49760264">Using jev to improve product experiences is pretty crazy</a></b> — ⭐6 · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 6 · コメント数 3 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 3 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 5 · コメント数 0 · 最終プッシュ 2026-09-15 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 4 · コメント数 0 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 4 · コメント数 0 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 3 · コメント数 0 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755005">Two techniques for working with System One models</a></b> — ⭐3 · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 3 · コメント数 0 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 3 · コメント数 0 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐2 · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · NOASSERTION · aliaihub

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### データ

スター数 **2** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49759706">I used Jev to control a swarm of 15 simulated drones in real time</a></b> — ⭐2 · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 0 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49759999">Jev&#x27;s Architecture Unmasked</a></b> — ⭐2 · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 0 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/jtnkminimal/awesome-jev">jtnkminimal/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · Python · CC0-1.0 · jtnkminimal

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A curated projects built with Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49753667">Show HN: Explore 2D semantic space with the Jev model</a></b> — ⭐2 · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 0 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

SemanticSpace is an experiment around Jev, TypeSafe AI’s new model. It uses a Cartesian plane defined by arbitrary phrases for each axis, to map prompts onto the resulting 2D semantic space. You can edit the prompts and axes to visualize virtually any 2D relationship.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49750649">Show HN: Open-Source Alternative to TypeSafe.ai</a></b> — ⭐2 · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 1 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49744527">Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)</a></b> — ⭐2 · observed · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 1 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Full disclosure, it was coded with AI, I don&#x27;t claim otherwise. But I wanted to test out tool calls and iterative problem solving using Jev and needed a simple library&#x2F;framework&#x2F;harness to do that.
SOKIT (System One Knowledge, Instructions and Tools) is the result

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49729945">The first (public) System One Model; Jev gives AI the properties of code</a></b> — ⭐2 · observed · 2 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 0 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49757995">TypeSafe / Jev latency-focused demos built by Devin</a></b> — ⭐2 · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 0 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49761730">TypeSafe AI&#x27;s Jev Is Not an LLM – and That May Be the Point</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 0 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49745212">Typesafe&#x27;s Jev is the fish at the poker table</a></b> — ⭐2 · observed · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 1 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49733647">Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step</a></b> — ⭐2 · observed · 2 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 0 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49734345">Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD</a></b> — ⭐2 · observed · 2 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 0 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49760138">What is a System One model and why we need it?</a></b> — ⭐2 · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed`

##### データ

ポイント 2 · コメント数 0 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/ozers/jevsome-projects">ozers/jevsome-projects</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · JavaScript · MIT · ozers

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Open-source projects that provably call Jev, TypeSafe AI's System One model. Every entry links to the line of code that proves it. Refreshed daily.

</details>

<details>
<summary><b><a href="https://github.com/rhc98/awesome-jev">rhc98/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · TypeScript · NOASSERTION · rhc98

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself.

</details>

<details>
<summary><b><a href="https://github.com/soderlind/ai-provider-for-jev">soderlind/ai-provider-for-jev</a></b> — ⭐1 · PHP · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · PHP · soderlind

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).

</details>

<details>
<summary><b><a href="https://github.com/aamanlamba/jev-explore">aamanlamba/jev-explore</a></b> — Jupyter · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · Jupyter · aamanlamba

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

An example repository for exploring Jev - the System One model

</details>

<details>
<summary><b><a href="https://github.com/alpibrusl/lex-judge">alpibrusl/lex-judge</a></b> — Lex · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · Lex · alpibrusl

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Typed judgments from a System One model, as a \[net\]-only Lex effect

</details>

<details>
<summary><b><a href="https://github.com/codaaiteam/jev-ai">codaaiteam/jev-ai</a></b> — observed · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · codaaiteam

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Jev AI quickstart & FAQ — TypeSafe AI's System One model. Try it free: jevtypesafeai.com

</details>

<details>
<summary><b><a href="https://github.com/hide-G/magi-system-on-jev">hide-G/magi-system-on-jev</a></b> — JavaScript · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · JavaScript · hide-G

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/hide-G/magi-system-on-jev/master/public/ogp.png" width="100%" alt="hide-G/magi-system-on-jev screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/JohnDotOwl/awesome-jev">JohnDotOwl/awesome-jev</a></b> — JavaScript · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · JavaScript · CC0-1.0 · JohnDotOwl

##### データ

スター数 **0** · フォーク数 1 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

A curated list of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/piyush97/focus-tube">piyush97/focus-tube</a></b> — JavaScript · observed · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · JavaScript · MIT · piyush97

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model

</details>

<details>
<summary><b><a href="https://github.com/rbalch/typesafeai-review">rbalch/typesafeai-review</a></b> — Python · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · Python · rbalch

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Using Typesafe.AI to generate diff reviews.

</details>

<details>
<summary><b><a href="https://github.com/robzolkos/omarchy-issue-classifier">robzolkos/omarchy-issue-classifier</a></b> — Ruby · observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · Ruby · robzolkos

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Classify the Omarchy issue backlog with Jev, TypeSafe's System One model. Ten typed questions per issue in one request, for a hundredth of a cent each.

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/jev-trader">Shashank-H/jev-trader</a></b> — observed · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · AGPL-3.0 · Shashank-H

##### データ

スター数 **0** · フォーク数 1 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

An automated trader using SystemOne model - TypesafeAI Jev

</details>

<details>
<summary><b><a href="https://github.com/TheGali/terrarium">TheGali/terrarium</a></b> — JavaScript · observed · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `observed` · JavaScript · MIT · TheGali

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.

</details>

<details>
<summary><b><a href="https://github.com/jarrodwatts/jev-trader">jarrodwatts/jev-trader</a></b> — ⭐888 · TypeScript · inferred · 1 天 · ⭐+23</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · jarrodwatts

##### データ

スター数 **888** (+23) · フォーク数 170 · 未解決の issue 3 · 作成日 2026-09-16 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

</details>

<details>
<summary><b><a href="https://github.com/droidrun/mobile-jev">droidrun/mobile-jev</a></b> — ⭐144 · JavaScript · inferred · 1 天 · ⭐+9</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · MIT · droidrun

##### データ

スター数 **144** (+9) · フォーク数 22 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/superagents-lab/jev-search">superagents-lab/jev-search</a></b> — ⭐123 · TypeScript · inferred · 0 天 · ⭐+19</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · superagents-lab

##### データ

スター数 **123** (+19) · フォーク数 20 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/superagents-lab--jev-search/5a545ddfd6a52aed.png" width="100%" alt="superagents-lab/jev-search screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mrnugget/jev-shell-history">mrnugget/jev-shell-history</a></b> — ⭐44 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · mrnugget

##### データ

スター数 **44** (+1) · フォーク数 3 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Fish-style zsh history autosuggestions ranked by Jev (TypeSafe)

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history animation"><br><sub>アニメーション記録</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">IAmUnbounded/save-token-jev-clean</a></b> — ⭐40 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · IAmUnbounded

##### データ

スター数 **40** · フォーク数 9 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/daseinlabs/open-jev">daseinlabs/open-jev</a></b> — ⭐32 · Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · daseinlabs

##### データ

スター数 **32** · フォーク数 5 · 未解決の issue 2 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov"><img src="" width="100%" alt="daseinlabs/open-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hqman/JevScout">hqman/JevScout</a></b> — ⭐18 · Python · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · hqman

##### データ

スター数 **18** (+1) · フォーク数 2 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

上流の説明は公開されていません。

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4"><img src="" width="100%" alt="hqman/JevScout video"></a><br><sub><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4">動画を開く</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/oso95/x-scanner">oso95/x-scanner</a></b> — ⭐8 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · oso95

##### データ

スター数 **8** (+1) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter

</details>

<details>
<summary><b><a href="https://github.com/Kevthetech143/super-jev">Kevthetech143/super-jev</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · MIT · Kevthetech143

##### データ

スター数 **5** · フォーク数 1 · 未解決の issue 1 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-18

##### 概要

A small, extensible decision-to-action harness for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/joelhooks/pi-fast-jev-compaction">joelhooks/pi-fast-jev-compaction</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · joelhooks

##### データ

スター数 **4** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Pi extension: verbatim context compaction with TypeSafe Jev decisions

</details>

<details>
<summary><b><a href="https://github.com/haseeb-heaven/jev-system-one">haseeb-heaven/jev-system-one</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · MIT · haseeb-heaven

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/haseeb-heaven--jev-system-one/e41c848323b1077a.png" width="100%" alt="haseeb-heaven/jev-system-one screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevinpita/pi-jev-context">kevinpita/pi-jev-context</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · kevinpita

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Reversible context pruning for Pi, powered by TypeSafe Jev. Keep useful context without deleting session history.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevinpita--pi-jev-context/9f40314df01e39d4.png" width="100%" alt="kevinpita/pi-jev-context screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/lbotinelly/jev-little-airways">lbotinelly/jev-little-airways</a></b> — ⭐2 · HTML · inferred · 1 天 · ⭐+1</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · HTML · MIT · lbotinelly

##### データ

スター数 **2** (+1) · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A show-and-tell capability study for Jev, TypeSafe's System One decision model.

</details>

<details>
<summary><b><a href="https://github.com/oxwen11/awesome-jev">oxwen11/awesome-jev</a></b> — ⭐2 · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · CC0-1.0 · oxwen11

##### データ

スター数 **2** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

A curated list of what people built with Jev

</details>

<details>
<summary><b><a href="https://github.com/1jehuang/jev-pr-labeler">1jehuang/jev-pr-labeler</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · MIT · 1jehuang

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Semantic GitHub PR labels using Jev's typed decisions, with conceptual scope instead of line counts

</details>

<details>
<summary><b><a href="https://github.com/AppitStudio/awesome-jev">AppitStudio/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · NOASSERTION · AppitStudio

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 4 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Curated Jev resources and runnable examples for typed AI decisions.

</details>

<details>
<summary><b><a href="https://github.com/Charlyhno-eng/jev-document-classification">Charlyhno-eng/jev-document-classification</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · Charlyhno-eng

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/charlyhno-eng--jev-document-classification/113bcf66f1648122.png" width="100%" alt="Charlyhno-eng/jev-document-classification screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/jev-review-action">fatwang2/jev-review-action</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · MIT · fatwang2

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 2 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.

</details>

<details>
<summary><b><a href="https://github.com/kazuhideoki/jev-search">kazuhideoki/jev-search</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · kazuhideoki

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Recursive semantic file search using TypeSafe Jev and fzf

</details>

<details>
<summary><b><a href="https://github.com/MumuTW/awesome-jev">MumuTW/awesome-jev</a></b> — ⭐1 · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · CC0-1.0 · MumuTW

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

快速看懂風格鮮明的 Jev：型別化決策的 System One，以及社群熱議的同類模型。

</details>

<details>
<summary><b><a href="https://github.com/sontakey/awesome-jev">sontakey/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · NOASSERTION · sontakey

##### データ

スター数 **1** · フォーク数 1 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Unofficial list of insanely useful TypeSafe AI Jev / System One projects

</details>

<details>
<summary><b><a href="https://github.com/TanayPadar/gpt-vs-jev">TanayPadar/gpt-vs-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · TanayPadar

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Compare GPT generated language with JEV structured Noul decisions on the same input.

</details>

<details>
<summary><b><a href="https://github.com/tylerjharden/harden-jev-decides">tylerjharden/harden-jev-decides</a></b> — ⭐1 · TypeScript · inferred · 2 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · tylerjharden

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.

</details>

<details>
<summary><b><a href="https://github.com/X0EF/jev_projects">X0EF/jev_projects</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · MIT · X0EF

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

list of projects that use typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/Z761293629/pi-jev-helm">Z761293629/pi-jev-helm</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · Z761293629

##### データ

スター数 **1** · フォーク数 0 · 未解決の issue 2 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/agentik-os/jev-radar">agentik-os/jev-radar</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · agentik-os

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/amansoory/JEV2048">amansoory/JEV2048</a></b> — C++ · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · C++ · amansoory

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/amr05008/jev-sandbox">amr05008/jev-sandbox</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · amr05008

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Test bench for TypeSafe's Jev: small, repeatable experiments on where a decision model beats prompt-and-parse

</details>

<details>
<summary><b><a href="https://github.com/Btheriot83/jev-academy">Btheriot83/jev-academy</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · Btheriot83

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Public Jev / TypeSafe academy — zero-to-hero walkthrough for Brandon Theriot

</details>

<details>
<summary><b><a href="https://github.com/caio0452/jev_search">caio0452/jev_search</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · caio0452

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/divo12/jev-v-llm">divo12/jev-v-llm</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · divo12

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/doroper98/Jev_Pendulum">doroper98/Jev_Pendulum</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · doroper98

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/EdwardHong0627/jev-poc">EdwardHong0627/jev-poc</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · EdwardHong0627

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/getvoicify/jev-reviewer">getvoicify/jev-reviewer</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · getvoicify

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/golergka/jev-plays-starcraft-2">golergka/jev-plays-starcraft-2</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · golergka

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/heaven-hm/jev-system-one">heaven-hm/jev-system-one</a></b> — inferred · 2 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · heaven-hm

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

</details>

<details>
<summary><b><a href="https://github.com/jamesward/jev-llm-c4">jamesward/jev-llm-c4</a></b> — Scala · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Scala · jamesward

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/jdhornsby/typesafe-jev">jdhornsby/typesafe-jev</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · jdhornsby

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-master">kevin9327/jev-master</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · MIT · kevin9327

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Typed System One decisions with Jev: Choice + Score + Noul composed in code.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevin9327--jev-master/cbf05c4561269075.png" width="100%" alt="kevin9327/jev-master screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kong75/jev-directory">kong75/jev-directory</a></b> — Astro · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Astro · kong75

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

A curated directory of Jev projects, examples, and patterns.

</details>

<details>
<summary><b><a href="https://github.com/kspviswa/chakravyuha-jev">kspviswa/chakravyuha-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · MIT · kspviswa

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kspviswa--chakravyuha-jev/4dfa22d0de9f27c1.png" width="100%" alt="kspviswa/chakravyuha-jev screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/lalitsonawane/jev-one-system">lalitsonawane/jev-one-system</a></b> — inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · lalitsonawane

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/LingXuanYin/jev-chat">LingXuanYin/jev-chat</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · NOASSERTION · LingXuanYin

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Jev 聊天机：一个「只选不写」的聊天机——每个回复由逐词选择拼装，词典+分级索引+输入法式联想，由真实 Jev（TypeSafe System One）驱动。非官方实验，与 TypeSafe AI 无关联。

</details>

<details>
<summary><b><a href="https://github.com/lookfwd/jev-fact-checker">lookfwd/jev-fact-checker</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · lookfwd

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Uses Typesafe AI Jev to Provide A Tweet Fact Checker

</details>

<details>
<summary><b><a href="https://github.com/manikanda-kumar/jev-dspy-control-plane">manikanda-kumar/jev-dspy-control-plane</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · MIT · manikanda-kumar

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-poker">meetr1912/jev-poker</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · meetr1912

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 4 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Watch Jev (TypeSafe) play heads-up No-Limit Hold'em, with decision probabilities on the side panel. Money/points scoreboard, offline CI, no secrets.

</details>

<details>
<summary><b><a href="https://github.com/memorysaver/jev-atari-lab">memorysaver/jev-atari-lab</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · GPL-2.0 · memorysaver

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Challenge Atari with Jev: structured decisions, value questions, and replayable experiments

</details>

<details>
<summary><b><a href="https://github.com/MrDesjardins/jev-send-guard">MrDesjardins/jev-send-guard</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · MrDesjardins

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/Nachom3/jevTrader">Nachom3/jevTrader</a></b> — Rust · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Rust · Nachom3

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

A High Frecuncy Trader made in Rust using Jev as a decision maker.

</details>

<details>
<summary><b><a href="https://github.com/nardinmarcus/pi-jev-typesafe">nardinmarcus/pi-jev-typesafe</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · nardinmarcus

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model discovery, and budget caps

</details>

<details>
<summary><b><a href="https://github.com/Nolane-x/JEV-language">Nolane-x/JEV-language</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · Nolane-x

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 2 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/oguressive/sample-jev">oguressive/sample-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · oguressive

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/silverzzzzz/jev-binaryoption">silverzzzzz/jev-binaryoption</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · MIT · silverzzzzz

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/sperictao/dsh-auto-review-jev">sperictao/dsh-auto-review-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · sperictao

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/thisisjorge/jev-control-room">thisisjorge/jev-control-room</a></b> — TypeScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · thisisjorge

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Interactive control room for fast typed AI decisions with TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/TonyP-MR/jev-curation-engine">TonyP-MR/jev-curation-engine</a></b> — Python · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · TonyP-MR

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions with existing LLM audit results.

</details>

<details>
<summary><b><a href="https://github.com/toshitoshi-creator/jev-chat-site">toshitoshi-creator/jev-chat-site</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · toshitoshi-creator

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/trungdq88/jev-tetris">trungdq88/jev-tetris</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · trungdq88

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Jev play Tetris in real-time against other AI models

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/trungdq88/jev-tetris/main/docs/screenshot.png" width="100%" alt="trungdq88/jev-tetris screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

<sub>再配布ライセンスが明示されていないため、アセットは上流リポジトリから直リンクしています。</sub>

</details>

<details>
<summary><b><a href="https://github.com/Tsagaanbayr1/jev-tetris">Tsagaanbayr1/jev-tetris</a></b> — JavaScript · inferred · 0 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · Tsagaanbayr1

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-19

##### 概要

Real-time Tetris versus Jev, a TypeSafe decision model — spins, garbage, B2B chains, and decisions prefetched a piece ahead

</details>

<details>
<summary><b><a href="https://github.com/TurboGuo/jev-fedspeech">TurboGuo/jev-fedspeech</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · TurboGuo

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Real-time hawk-or-dove analysis of Fed press conferences with TypeSafe's Jev vs chat models. Live at fedspeech.pages.dev

</details>

<details>
<summary><b><a href="https://github.com/wakamenod/jev.el">wakamenod/jev.el</a></b> — Emacs Lisp · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Emacs Lisp · GPL-3.0 · wakamenod

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/waynesutton/ask-jev-ai">waynesutton/ask-jev-ai</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · waynesutton

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

A public wall where anyone asks a question in three to fifteen words and Jev, TypeSafe's judgment model, answers yes, no, or it depends in about 100 milliseconds. Every judged ask lands on the wall in realtime, with a running count toward one million, showing cost.

</details>

<details>
<summary><b><a href="https://github.com/yuki-dev26/jev-test">yuki-dev26/jev-test</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · JavaScript · yuki-dev26

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-18 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

上流の説明は公開されていません。

</details>

<details>
<summary><b><a href="https://github.com/zaycruz/fast-jev-compaction-pi">zaycruz/fast-jev-compaction-pi</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · TypeScript · MIT · zaycruz

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

Verbatim Jev-guided context compaction for pi — replaces the built-in compaction summary with fast-jev decisions; stale tool calls/results dropped, everything kept stays verbatim.

</details>

<details>
<summary><b><a href="https://github.com/Zogrus/jev-technical-term">Zogrus/jev-technical-term</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `inferred` · Python · MIT · Zogrus

##### データ

スター数 **0** · フォーク数 0 · 未解決の issue 0 · 作成日 2026-09-19 · 最終プッシュ 2026-09-19 · 初回掲載 2026-09-19

##### 概要

YouTubeの解説動画やZoomのセミナーを聞きながら、出てきた技術用語のひとこと解説をリアルタイム表示するローカルツール(判定AIは TypeSafe AI の Jev)

</details>

<details>
<summary><b><a href="https://github.com/realZachi/typesafe-adblock">realZachi/typesafe-adblock</a></b> — ⭐49 · JavaScript · unverified · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `unverified` · JavaScript · MIT · realZachi

##### データ

スター数 **49** · フォーク数 4 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.

</details>

<details>
<summary><b><a href="https://github.com/razorback16/openjev">razorback16/openjev</a></b> — ⭐42 · Python · unverified · 0 天 · ⭐+6</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `unverified` · Python · Apache-2.0 · razorback16

##### データ

スター数 **42** (+6) · フォーク数 6 · 未解決の issue 1 · 作成日 2026-09-18 · 最終プッシュ 2026-09-18 · 初回掲載 2026-09-18

##### 概要

Open, Jev-compatible System One decision server on DiffusionGemma

</details>

<details>
<summary><b><a href="https://github.com/devanshbatham/commit-miner">devanshbatham/commit-miner</a></b> — ⭐22 · Rust · unverified · 1 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `unverified` · Rust · devanshbatham

##### データ

スター数 **22** · フォーク数 5 · 未解決の issue 0 · 作成日 2026-09-17 · 最終プッシュ 2026-09-17 · 初回掲載 2026-09-18

##### 概要

Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.

</details>

<details>
<summary><b><a href="https://github.com/phyous/tsai-sc">phyous/tsai-sc</a></b> — ⭐15 · Python · unverified · 2 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `unverified` · Python · MIT · phyous

##### データ

スター数 **15** · フォーク数 1 · 未解決の issue 0 · 作成日 2026-09-16 · 最終プッシュ 2026-09-16 · 初回掲載 2026-09-18

##### 概要

TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.

<table><tr><th align="center" width="50%">画像</th><th align="center" width="50%">動画</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/phyous--tsai-sc/f48a030ae92fb1fe.png" width="100%" alt="phyous/tsai-sc screenshot"></td>
<td align="center" valign="top"><sub>メディア未公開</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andysc/IBM-Q-System-One-3D-model">andysc/IBM-Q-System-One-3D-model</a></b> — ⭐12 · OpenSCAD · unverified · 2688 天</summary>

##### 基本情報

`記事、ディスカッション、類似リスト` · コミュニティ · `unverified` · OpenSCAD · andysc

##### データ

スター数 **12** · フォーク数 4 · 未解決の issue 1 · 作成日 2019-03-16 · 最終プッシュ 2019-05-10 · 初回掲載 2026-09-18

##### 概要

3D-printed model of IBM Q System One

</details>

<a id="projects-by-implementation-language"></a>

## 実装言語別のプロジェクト

エコシステムは Python と TypeScript に集中していますが、型付きクライアントは他の言語でも現れ続けています。この表はエントリそのものから生成されます。

| 言語         | エントリ数 | 例                                                                                                              |
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

<sub>言語を明示したエントリのみを集計しています。インフラ、ドキュメント、ディスカッションの各エントリはこの表から除外されます。</sub>

## このリストが最新に保たれる仕組み

この README の本文を人が編集することはありません。リポジトリは定期的に 5 段階のパイプラインを実行し、実際に変化があったときだけコミットします。

<img src="assets/readme/pipeline.svg" width="100%" alt="このリストが最新に保たれる仕組み">

|             |                                                                                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **collect** | クエリ行列にわたる GitHub 検索、公式オーガニゼーション、GitHub コード検索、Hacker News、Hugging Face hub。                                                                      |
| **curate**  | 決定論的で LLM を使わないため、同じ入力に対する連続 2 回の実行はバイト単位で同一の出力を生みます。関連性は 2 シグナル規則で判定し、名前の衝突（JeVois、JEvents、Jevil、jEveAssets、ESP32-RLCD など）は明示的で監査可能なリストで除外します。 |
| **media**   | 各プロジェクト自身のスクリーンショットと画面録画を収集します。再配布に適したライセンスが宣言されている場合にのみアセットを本リポジトリへコピーし、それ以外は上流の URL を直リンクして、カードにその旨を記載します。                                    |
| **render**  | 1 つのテンプレートからすべての言語版を生成するため、20 個の README は構造上ずれようがありません。                                                                                         |
| **audit**   | エントリに URL がない場合、リンクが切れている場合、2 つのエントリが URL を重複している場合、README が生成形から逸脱している場合にビルドを失敗させます。                                                           |

## コントリビューション

訂正は歓迎しますし、このリストを改善する最短の方法です。エントリの分類や格付けが誤っている場合、あるいはプロジェクトが名前の衝突として誤って除外されている場合は、issue かプルリクエストを立ててください。最後の類型こそ、自動フィルタが最も間違えやすいところです。追加は README を編集するのではなく `scripts/collect.py` に取得元を足す形が最善です。README は毎回再生成されるためです。

---

<sub>独立したコミュニティプロジェクトです。TypeSafe AI と提携しておらず、その承認もレビューも受けていません。製品の挙動、価格、制限、モデルの別名は予告なく変わります。重要なものは必ず公式ドキュメントで確認してください。アセットは上流プロジェクトに帰属し、ライセンスが許す場合にのみ掲載しています。</sub>

<sub>生成ツール · `render.py` · 2026-09-19T10:20:34+08:00</sub>
