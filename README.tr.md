<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>Kendini her iki saatte bir yeniden kuran, kanıt derecelendirmeli Jev dizini.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-412-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <b>Türkçe</b> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Canlı dizin** · Son eşitleme: `2026-09-18T23:19:50+08:00` (UTC+8)
> · Kayıt: **412** · Bu turda yeni: **44** · Uygulama dilleri: **21**

<sub>Aşağıdaki her kayıt bu depodaki iş akışı tarafından toplandı, filtrelendi ve yeniden kontrol edildi. Sayılar ve zaman damgaları elle yazılmış bir anlık görüntüden değil, kaynaklardan gelir.</sub>

## İçindekiler

- [Jev nedir?](#jev-nedir)
- [Kayıtlar nasıl derecelendirilir](#kayıtlar-nasıl-derecelendirilir)
- [Resmî SDK'lar ve geliştirici araçları](#resmî-sdklar-ve-geliştirici-araçları) — **5**
- [Topluluk istemcileri, SDK'lar ve bağdaştırıcılar](#topluluk-istemcileri-sdklar-ve-bağdaştırıcılar) — **73**
- [Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları](#ajan-araçları-mcp-kancalar-geçitler-ve-kodlama-ajanları) — **111**
- [Yönlendirme, koruma kuralları ve onaylar](#yönlendirme-koruma-kuralları-ve-onaylar) — **43**
- [Değerlendirme, kalibrasyon ve kıyaslamalar](#değerlendirme-kalibrasyon-ve-kıyaslamalar) — **28**
- [Açık yeniden üretimler, ağırlıklar ve mimari araştırması](#açık-yeniden-üretimler-ağırlıklar-ve-mimari-araştırması) — **12**
- [Uygulamalar, oyunlar, robotik ve etkileşimli demolar](#uygulamalar-oyunlar-robotik-ve-etkileşimli-demolar) — **37**
- [Yazılar, tartışmalar ve kardeş listeler](#yazılar-tartışmalar-ve-kardeş-listeler) — **103**
- [Uygulama diline göre projeler](#uygulama-diline-göre-projeler)
- [Bu liste nasıl güncel kalıyor](#bu-liste-nasıl-güncel-kalıyor)

## Jev nedir?

Jev, TypeSafe AI'ın ilk **System One modelidir**. Düzyazı yazmaz. Bir durum ile cevap uzayını önceden sizin tanımladığınız soruları alır ve kodunuzun dallanabileceği olasılık dağılımlarıyla birlikte tipli değerler döndürür.

|                       |                                                                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Biçim**             | `state + typed questions` → `constrained answers + probabilities` → `your code`                                                                                                                |
| **Temel öğeler**      | `Choice` (≤255 seçenekten birini seçer), `Score` (2–10 arası bir rubrik), `Noul` (olasılıksal evet/hayır)                                                                                      |
| **Uç nokta**          | `POST https://api.typesafe.ai/v1/systemone`, model `jev-1.13.0` / takma ad `jev-latest`                                                                                                        |
| **Uygun kullanımlar** | sınırlı bir iş akışı içinde yönlendirme, triyaj, puanlama, moderasyon, doğrulama ve düşük gecikmeli geçitler                                                                                   |
| **Bilinen sınırlar**  | sayma güvenilir değil, çok katmanlı dolaylılık zayıf ve resmî materyal dokuz sınıf pürüzlülük adlandırıyor. Şema-geçerli çıktı doğru kararla aynı şey değildir — kendi verinizle kalibre edin. |

## Kayıtlar nasıl derecelendirilir

Bu alandaki çoğu liste dahil ettiğini iddia eder. Bu liste gerçekte ne kadarını doğruladığını söyler ve buna göre filtrelemenize izin verir.

| Derece       | Anlamı                                                                                                                                              |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `official`   | TypeSafe AI'ın kendisi tarafından yayımlandı.                                                                                                       |
| `observed`   | Açılıp okunabilen kamuya açık bir artefakt — gerçek kaynak kodu, gerçek yapılandırma ya da depo adında veya konusunda açık bir TypeSafe/Jev beyanı. |
| `inferred`   | Belirsiz bir sinyal ile onu destekleyen sözcük dağarcığı üzerinden eşleşti, ancak henüz satır satır okunmadı.                                       |
| `unverified` | İlgili görünüyor, bağımsız olarak doğrulanmış hiçbir şey yok. Yalnızca keşif amacıyla listelendi.                                                   |

<a id="official-sdk"></a>

## Resmî SDK&#x27;lar ve geliştirici araçları

TypeSafe'in kendi yayımladığı her şey. Buradan başlayın.

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐193 · official · 6 天 · ⭐+3</summary>

##### Temel bilgiler

`Resmî SDK&#x27;lar ve geliştirici araçları` · Resmî · `official` · MIT · typesafe-ai

##### Veri

Yıldız **193** (+3) · Fork 10 · Açık issue 0 · Oluşturulma 2026-08-24 · Son push 2026-09-12 · İlk listelenme 2026-09-18

##### Özet

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐112 · TypeScript · official · 2 天 · ⭐+2</summary>

##### Temel bilgiler

`Resmî SDK&#x27;lar ve geliştirici araçları` · Resmî · `official` · TypeScript · MIT · typesafe-ai

##### Veri

Yıldız **112** (+2) · Fork 7 · Açık issue 6 · Oluşturulma 2026-09-04 · Son push 2026-09-15 · İlk listelenme 2026-09-18

##### Özet

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐104 · Python · official · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Resmî SDK&#x27;lar ve geliştirici araçları` · Resmî · `official` · Python · MIT · typesafe-ai

##### Veri

Yıldız **104** (+1) · Fork 9 · Açık issue 0 · Oluşturulma 2026-08-08 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>Kodda kullanıldığı tespit edildi: `README.md`, `src/system_one_adapter/__init__.py`, `src/system_one_adapter/_response.py`, `src/system_one_adapter/_utils/error_handling.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐78 · Python · official · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Resmî SDK&#x27;lar ve geliştirici araçları` · Resmî · `official` · Python · MIT · typesafe-ai

##### Veri

Yıldız **78** (+1) · Fork 7 · Açık issue 1 · Oluşturulma 2026-09-04 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>Kodda kullanıldığı tespit edildi: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 106 天</summary>

##### Temel bilgiler

`Resmî SDK&#x27;lar ve geliştirici araçları` · Resmî · `official` · HTML · typesafe-ai

##### Veri

Yıldız **1** · Fork 1 · Açık issue 1 · Oluşturulma 2024-05-28 · Son push 2026-06-04 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<a id="community-sdk"></a>

## Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar

System One uç noktası için tipli istemciler; topluluğun sıra geldiği ölçüde çok dilde.

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐16 · Jupyter · observed · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · Jupyter · MIT · jexp

##### Veri

Yıldız **16** (+1) · Fork 3 · Açık issue 1 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · TypeScript · MIT · AntonioCoppe

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · Python · CC0-1.0 · MrJev

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐2 · Elixir · observed · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · Elixir · MIT · nshkrdotcom

##### Veri

Yıldız **2** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · TypeScript · opaielsheikh

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — ⭐2 · Java · observed · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · Java · MIT · Premo-Cloud

##### Veri

Yıldız **2** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · Rust · MIT · AkashPriyadarshii

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · JavaScript · MIT · ziyu

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/ehmpathy/rhachet-brains-typesafeai">ehmpathy/rhachet-brains-typesafeai</a></b> — observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · MIT · ehmpathy

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

rhachet brain.atom adapter for typesafe.ai classifier models

</details>

<details>
<summary><b><a href="https://github.com/ivorpad/skillranker">ivorpad/skillranker</a></b> — observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · NOASSERTION · ivorpad

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · Ruby · MIT · javiergradiche

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/jonesmelton/verdict">jonesmelton/verdict</a></b> — OCaml · observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · OCaml · MIT · jonesmelton

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

ocaml sdk for typesafe.ai's jev model

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · TypeScript · MIT · nu-sync

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · Elixir · MIT · typesend

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — Python · observed · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `observed` · Python · xingwudao

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐130 · Python · inferred · 0 天 · ⭐+6</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · NOASSERTION · realZachi

##### Veri

Yıldız **130** (+6) · Fork 6 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐22 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · nidhi-singh02

##### Veri

Yıldız **22** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">İzleme yeri img.youtube.com</a> · oynatma kaynak sitede açılır; GitHub bunu satır içi gömemez</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gamesonrblx/Jevbridge">gamesonrblx/Jevbridge</a></b> — ⭐13 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · gamesonrblx

##### Veri

Yıldız **13** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

> Bridges the typed-decision layer to the agent protocols other tools already speak.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gamesonrblx--jevbridge/772995670b3e42e9.png" width="100%" alt="gamesonrblx/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐12 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · shiftynick

##### Veri

Yıldız **12** (+1) · Fork 1 · Açık issue 1 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐10 · Elixir · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Elixir · MIT · dannote

##### Veri

Yıldız **10** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐8 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · JavaScript · MIT · Ying-Kai-Liao

##### Veri

Yıldız **8** (+1) · Fork 3 · Açık issue 2 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐6 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · MIT · AboveColin

##### Veri

Yıldız **6** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Home Assistant integration for TypeSafe Jev. Ask a question about your house and get a probability, a choice or a score as an entity.

</details>

<details>
<summary><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">saibimajdi/typesafeai-dotnet-sdk</a></b> — ⭐5 · C# · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · C# · MIT · saibimajdi

##### Veri

Yıldız **5** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/sharziki/semdecide">sharziki/semdecide</a></b> — ⭐5 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · MIT · sharziki

##### Veri

Yıldız **5** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.

</details>

<details>
<summary><b><a href="https://github.com/arunav25/jev-mcp">arunav25/jev-mcp</a></b> — ⭐3 · JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · JavaScript · MIT · arunav25

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.

</details>

<details>
<summary><b><a href="https://github.com/docxology/daf-jev">docxology/daf-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · MIT · docxology

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill

</details>

<details>
<summary><b><a href="https://github.com/frostney/clean-code-review">frostney/clean-code-review</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · frostney

##### Veri

Yıldız **3** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/frostney--clean-code-review/7d8a8de446e1c27b.png" width="100%" alt="frostney/clean-code-review screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Butochnikov/laravel-typesafe-jev</a></b> — ⭐2 · PHP · inferred · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · PHP · MIT · Butochnikov

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes.

</details>

<details>
<summary><b><a href="https://github.com/Olti1947/jev-java">Olti1947/jev-java</a></b> — ⭐2 · Java · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Java · Olti1947

##### Veri

Yıldız **2** (+1) · Fork 1 · Açık issue 7 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Idiomatic Java SDK for TypeSafe AI Jev System One decision engine

</details>

<details>
<summary><b><a href="https://github.com/romaluev/jev-ego">romaluev/jev-ego</a></b> — ⭐2 · TypeScript · inferred · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · NOASSERTION · romaluev

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move.

</details>

<details>
<summary><b><a href="https://github.com/tumf/jev-cli">tumf/jev-cli</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · MIT · tumf

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Small dependency-free CLI for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/yzfly/awesome-jev-zh">yzfly/awesome-jev-zh</a></b> — ⭐2 · HTML · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · HTML · CC0-1.0 · yzfly

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/jevclient">AboveColin/jevclient</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · MIT · AboveColin

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.

</details>

<details>
<summary><b><a href="https://github.com/burnigtm/jev-mcp">burnigtm/jev-mcp</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · burnigtm

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client

</details>

<details>
<summary><b><a href="https://github.com/felpsdev/jev-classifier">felpsdev/jev-classifier</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · felpsdev

##### Veri

Yıldız **1** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/felpsdev--jev-classifier/d753de26b0e6c7b6.webp" width="100%" alt="felpsdev/jev-classifier screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-go">Gaurav-Gosain/jev-go</a></b> — ⭐1 · Go · inferred · 2 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Go · MIT · Gaurav-Gosain

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/himomohi/aside-jev">himomohi/aside-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · MIT · himomohi

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.

</details>

<details>
<summary><b><a href="https://github.com/jtsang4/jev-cli">jtsang4/jev-cli</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · jtsang4

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

CLI for TypeSafe AI's Jev evaluation model — typed questions in, structured JSON answers out

</details>

<details>
<summary><b><a href="https://github.com/rhighs/jev-code">rhighs/jev-code</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · rhighs

##### Veri

Yıldız **1** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/assets/jev-code-logo.png" width="100%" alt="rhighs/jev-code screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/StefanoITA/ts-jev-cost-calculator">StefanoITA/ts-jev-cost-calculator</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · MIT · StefanoITA

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe.

</details>

<details>
<summary><b><a href="https://github.com/Stumble/jev-go">Stumble/jev-go</a></b> — ⭐1 · Go · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Go · MIT · Stumble

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Community Go SDK for TypeSafe AI Jev / System One

</details>

<details>
<summary><b><a href="https://github.com/tontoko/jev-browser">tontoko/jev-browser</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · JavaScript · Apache-2.0 · tontoko

##### Veri

Yıldız **1** · Fork 0 · Açık issue 4 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.

</details>

<details>
<summary><b><a href="https://github.com/abeldzan/jev-rs">abeldzan/jev-rs</a></b> — Rust · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Rust · MIT · abeldzan

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Async-first Rust SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-git">AkashPriyadarshii/jev-git</a></b> — Rust · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Rust · MIT · AkashPriyadarshii

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-scout">AkashPriyadarshii/jev-scout</a></b> — Rust · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Rust · MIT · AkashPriyadarshii

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-seo">AkashPriyadarshii/jev-seo</a></b> — Rust · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Rust · AkashPriyadarshii

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">AkashPriyadarshii/jev-superpowers</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · JavaScript · MIT · AkashPriyadarshii

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions

</details>

<details>
<summary><b><a href="https://github.com/anilsenay/jev">anilsenay/jev</a></b> — Go · inferred · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Go · MIT · anilsenay

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Unofficial Go client for TypeSafe's System One API  and its model, Jev.

</details>

<details>
<summary><b><a href="https://github.com/brnyxx/jev-ra">brnyxx/jev-ra</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · MIT · brnyxx

##### Veri

Yıldız **0** · Fork 0 · Açık issue 2 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7592fce4641d10.png" width="100%" alt="brnyxx/jev-ra screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7ddcd1053825a2.gif" width="100%" alt="brnyxx/jev-ra animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/david1gp/jev">david1gp/jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · david1gp

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Result-based TypeSafe System One client library and jev command-line interface.

</details>

<details>
<summary><b><a href="https://github.com/ddfeyes/jev-mode">ddfeyes/jev-mode</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · MIT · ddfeyes

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no deps, MIT.

</details>

<details>
<summary><b><a href="https://github.com/ibrahemid/git-jev-stage">ibrahemid/git-jev-stage</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · ibrahemid

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Stage the git hunks that match a sentence. Exact patch, preview first, staging only, decided per hunk by Jev.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/krw82/jev-playwright-mcp">krw82/jev-playwright-mcp</a></b> — TypeScript · inferred · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · krw82

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.

</details>

<details>
<summary><b><a href="https://github.com/kunobi-ninja/kunobi-jev">kunobi-ninja/kunobi-jev</a></b> — Rust · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Rust · Apache-2.0 · kunobi-ninja

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Rust client for the TypeSafe System One API (Jev)

</details>

<details>
<summary><b><a href="https://github.com/lhotwll217/jev-cli">lhotwll217/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · lhotwll217

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

JSON-in, typed-decisions-out CLI for the TypeSafe System One API

</details>

<details>
<summary><b><a href="https://github.com/manojlds/jev-review">manojlds/jev-review</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · manojlds

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Standalone TypeSafe Jev code-review CLI: typed decisions over a local git diff.

</details>

<details>
<summary><b><a href="https://github.com/mhmdkzr/jev">mhmdkzr/jev</a></b> — Go · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Go · MIT · mhmdkzr

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

An unofficial Go client for TypeSafe's System One Jev model

</details>

<details>
<summary><b><a href="https://github.com/misaalya/jev-traversal">misaalya/jev-traversal</a></b> — inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · misaalya

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

faster than codegraph, slightly more expensive.

</details>

<details>
<summary><b><a href="https://github.com/mzainzulifqar/jev-php-sdk">mzainzulifqar/jev-php-sdk</a></b> — PHP · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · PHP · MIT · mzainzulifqar

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

PHP SDK for TypeSafe's Jev: send text and typed questions, get typed answers with calibrated confidence. PHP 8.1+, works with any PSR-18 client, Laravel 8–13.

</details>

<details>
<summary><b><a href="https://github.com/Nasrallah-AL/jev-cli">Nasrallah-AL/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · TypeScript · MIT · Nasrallah-AL

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Command-line tool for TypeSafe's Jev AI model

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-go">nekowasabi/jev-routing-go</a></b> — Go · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Go · MIT · nekowasabi

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.

</details>

<details>
<summary><b><a href="https://github.com/okooo5km/jev">okooo5km/jev</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · Apache-2.0 · okooo5km

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Typed decisions from the shell: a stdlib-Python CLI and Agent Skill for TypeSafe Jev on OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch mode.

</details>

<details>
<summary><b><a href="https://github.com/phuthuycoding/jev-audit">phuthuycoding/jev-audit</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · phuthuycoding

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

AI-powered pre-commit auditor backed by TypeSafe System One (Jev) — blocks secrets, vulns & low-quality code in ~300ms. 79-case test corpus at 100% accuracy.

</details>

<details>
<summary><b><a href="https://github.com/SAGAR-TAMANG/sarvam-jev">SAGAR-TAMANG/sarvam-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Python · SAGAR-TAMANG

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Generation-free typed decisions on Indic LLMs. An open Jev-style inference engine on sarvam-1: constrained logit readout instead of autoregressive JSON. Runs client-side in the browser.

</details>

<details>
<summary><b><a href="https://github.com/shanginn/jev-php">shanginn/jev-php</a></b> — PHP · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · PHP · MIT · shanginn

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Type-safe PHP 8.5 SDK for JEV decisions on OpenRouter: choices, scores, probabilities and typed DTOs.

</details>

<details>
<summary><b><a href="https://github.com/zhirschtritt/typesafe-go">zhirschtritt/typesafe-go</a></b> — Go · inferred · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `inferred` · Go · MIT · zhirschtritt

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Idiomatic Go SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/pithings/advocaat">pithings/advocaat</a></b> — ⭐65 · TypeScript · unverified · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `unverified` · TypeScript · MIT · pithings

##### Veri

Yıldız **65** (+2) · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/Tangerg/typesafe-sdk-go">Tangerg/typesafe-sdk-go</a></b> — ⭐7 · Go · unverified · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `unverified` · Go · MIT · Tangerg

##### Veri

Yıldız **7** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Go SDK for the TypeSafe AI API — typed questions in, probability distributions out.

</details>

<details>
<summary><b><a href="https://github.com/giuliosmall/pg_typesafe">giuliosmall/pg_typesafe</a></b> — ⭐5 · C · unverified · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `unverified` · C · MIT · giuliosmall

##### Veri

Yıldız **5** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/typesafe-cli">y0usaf/typesafe-cli</a></b> — ⭐4 · TypeScript · unverified · 2 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `unverified` · TypeScript · MIT · y0usaf

##### Veri

Yıldız **4** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose

</details>

<details>
<summary><b><a href="https://github.com/Brainwires/jevwire">Brainwires/jevwire</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `unverified` · TypeScript · MIT · Brainwires

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)

</details>

<details>
<summary><b><a href="https://github.com/geilt/typesafe-cli">geilt/typesafe-cli</a></b> — ⭐3 · Python · unverified · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `unverified` · Python · geilt

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.

</details>

<details>
<summary><b><a href="https://github.com/gilljon/typesafe-ai-rs">gilljon/typesafe-ai-rs</a></b> — ⭐3 · Rust · unverified · 1 天</summary>

##### Temel bilgiler

`Topluluk istemcileri, SDK&#x27;lar ve bağdaştırıcılar` · Topluluk · `unverified` · Rust · MIT · gilljon

##### Veri

Yıldız **3** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Independent async and blocking Rust SDK for the TypeSafe AI System One API

</details>

<a id="agent-tooling"></a>

## Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları

En hızlı büyüyen kategori: bir ajanın sonraki eyleminin önüne tipli bir karar koyan kancalar, MCP sunucuları ve geçitler.

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐2579 · TypeScript · observed · 0 天 · ⭐+128</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · TypeScript · MIT · tamaratran

##### Veri

Yıldız **2579** (+128) · Fork 125 · Açık issue 39 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>Kodda kullanıldığı tespit edildi: `src/request.ts`, `README.md`, `src/client.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐118 · JavaScript · inferred · 0 天 · ⭐+4</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · gargpratyush

##### Veri

Yıldız **118** (+4) · Fork 5 · Açık issue 3 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐26 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · 0xNatoshi

##### Veri

Yıldız **26** · Fork 2 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐75 · observed · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · dbreunig

##### Veri

Yıldız **75** (+2) · Fork 2 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐13 · Python · observed · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · Python · MIT · GhalebDweikat

##### Veri

Yıldız **13** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · Python · MIT · carlaiau

##### Veri

Yıldız **7** · Fork 1 · Açık issue 6 · Oluşturulma 2026-03-13 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · Python · MIT · jodan-alberts

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · TypeScript · MIT · BYK

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · Python · MIT · 24601

##### Veri

Yıldız **0** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · TypeScript · CrowBe

##### Veri

Yıldız **0** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · TypeScript · MIT · gorock007

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `observed` · Python · MIT · yousudip

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐236 · TypeScript · inferred · 1 天 · ⭐+2</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · devagrawal09

##### Veri

Yıldız **236** (+2) · Fork 12 · Açık issue 1 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐108 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · NiazMorshed2007

##### Veri

Yıldız **108** (+4) · Fork 9 · Açık issue 2 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-eval-agent">vinilana/jev-eval-agent</a></b> — ⭐79 · HTML · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · HTML · vinilana

##### Veri

Yıldız **79** · Fork 6 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-mcp">jkudish/jev-mcp</a></b> — ⭐67 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · jkudish

##### Veri

Yıldız **67** (+2) · Fork 8 · Açık issue 2 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Proof of concept MCP for Typesafe's new Jev AI model

> An early proof of concept for exposing Jev over MCP, which is how most non-Python toolchains reach it.

</details>

<details>
<summary><b><a href="https://github.com/RomanSlack/jev-drone">RomanSlack/jev-drone</a></b> — ⭐57 · Python · inferred · 1 天 · ⭐+1</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · RomanSlack

##### Veri

Yıldız **57** (+1) · Fork 3 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/romanslack--jev-drone/b23ea2412f437970.png" width="100%" alt="RomanSlack/jev-drone screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/pi-jev">y0usaf/pi-jev</a></b> — ⭐53 · TypeScript · inferred · 0 天 · ⭐+15</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · y0usaf

##### Veri

Yıldız **53** (+15) · Fork 3 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐39 · JavaScript · inferred · 0 天 · ⭐+17</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · fatwang2

##### Veri

Yıldız **39** (+17) · Fork 7 · Açık issue 23 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/wy-coliney/jev-browser-use">wy-coliney/jev-browser-use</a></b> — ⭐32 · JavaScript · inferred · 0 天 · ⭐+6</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · wy-coliney

##### Veri

Yıldız **32** (+6) · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wy-coliney--jev-browser-use/581fbd89fe47c952.png" width="100%" alt="wy-coliney/jev-browser-use screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/ask-jev-skill">shantanugoel/ask-jev-skill</a></b> — ⭐25 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · shantanugoel

##### Veri

Yıldız **25** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Skill for Hermes, and other agents, to ask typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/supercorp-ai/supercov">supercorp-ai/supercov</a></b> — ⭐24 · Rust · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Rust · MIT · supercorp-ai

##### Veri

Yıldız **24** (+1) · Fork 1 · Açık issue 0 · Oluşturulma 2026-08-23 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Code quality and coverage for coding agents

> Code quality and coverage verdicts produced as typed decisions rather than prose, so the result can gate a pipeline directly.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/supercorp-ai--supercov/063226e150cb8a6b.jpg" width="100%" alt="supercorp-ai/supercov screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/logicrw/awesome-jev-projects">logicrw/awesome-jev-projects</a></b> — ⭐18 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · logicrw

##### Veri

Yıldız **18** (+1) · Fork 2 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync

</details>

<details>
<summary><b><a href="https://github.com/compozy/yoshi">compozy/yoshi</a></b> — ⭐9 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · compozy

##### Veri

Yıldız **9** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/compozy--yoshi/637d8588c227f4de.png" width="100%" alt="compozy/yoshi screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">jomatsu/pi-jev-auto-mode</a></b> — ⭐9 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · jomatsu

##### Veri

Yıldız **9** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.

</details>

<details>
<summary><b><a href="https://github.com/blakestone-x/jev-mcp">blakestone-x/jev-mcp</a></b> — ⭐7 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · blakestone-x

##### Veri

Yıldız **7** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer

</details>

<details>
<summary><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">DECRUX9812/typesafe-skill-router</a></b> — ⭐6 · Python · inferred · 2 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · DECRUX9812

##### Veri

Yıldız **6** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-code">devagrawal09/jev-code</a></b> — ⭐6 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · devagrawal09

##### Veri

Yıldız **6** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Bounded TypeSafe Jev workflows for coding agents.

</details>

<details>
<summary><b><a href="https://github.com/TheoOliveira/pi-jev">TheoOliveira/pi-jev</a></b> — ⭐6 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · TheoOliveira

##### Veri

Yıldız **6** (+2) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">GodsBoy/jev-agent-skill-router</a></b> — ⭐5 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · GodsBoy

##### Veri

Yıldız **5** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Typed, confidence-aware agent skill routing with TypeSafe Jev.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/godsboy--jev-agent-skill-router/c80293e37dcd4faf.png" width="100%" alt="GodsBoy/jev-agent-skill-router screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/huntedman/JevLint">huntedman/JevLint</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · huntedman

##### Veri

Yıldız **5** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.

</details>

<details>
<summary><b><a href="https://github.com/kikoncuo/jevfire">kikoncuo/jevfire</a></b> — ⭐5 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · kikoncuo

##### Veri

Yıldız **5** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

JEV-inspired parallel decisions for CUDA LLMs. One context, many decisions. vLLM API, game-agent examples, and reproducible benchmarks.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kikoncuo--jevfire/2d5597bbc6b2c82e.png" width="100%" alt="kikoncuo/jevfire screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/GiesN/typesafe-jev-workflow">GiesN/typesafe-jev-workflow</a></b> — ⭐4 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · GiesN

##### Veri

Yıldız **4** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/inanna-malick/jev-dsl">inanna-malick/jev-dsl</a></b> — ⭐4 · Haskell · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Haskell · MIT · inanna-malick

##### Veri

Yıldız **4** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels

</details>

<details>
<summary><b><a href="https://github.com/anandi1989/awesome-jev-usecases">anandi1989/awesome-jev-usecases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · MIT · anandi1989

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results

</details>

<details>
<summary><b><a href="https://github.com/anpicasso/hermes-jev-approvals">anpicasso/hermes-jev-approvals</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · anpicasso

##### Veri

Yıldız **3** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only.

</details>

<details>
<summary><b><a href="https://github.com/BillionsBobby/JevRouter">BillionsBobby/JevRouter</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · BillionsBobby

##### Veri

Yıldız **3** · Fork 1 · Açık issue 5 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A lightweight Jev-powered router for models, tools, and subagents

</details>

<details>
<summary><b><a href="https://github.com/SeeAPI/awesome-jev-use-cases">SeeAPI/awesome-jev-use-cases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · CC-BY-4.0 · SeeAPI

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-shield">caiovicentino/jev-shield</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · caiovicentino

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check.

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/jev-judgment">HyunjunJeon/jev-judgment</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · HyunjunJeon

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Agent Skill: send closed coding-agent judgments to TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/molis-ai/jev-workbench">molis-ai/jev-workbench</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · molis-ai

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/molis-ai--jev-workbench/00f61d8403a941cd.png" width="100%" alt="molis-ai/jev-workbench screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MongLong0214/jev-gate">MongLong0214/jev-gate</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MongLong0214

##### Veri

Yıldız **2** · Fork 0 · Açık issue 5 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.

</details>

<details>
<summary><b><a href="https://github.com/ranjan2829/AskJev">ranjan2829/AskJev</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · ranjan2829

##### Veri

Yıldız **2** · Fork 2 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-mcp">rashedInt32/jev-mcp</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · rashedInt32

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/samtay32/jev-system-architect">samtay32/jev-system-architect</a></b> — ⭐2 · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · MIT · samtay32

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives.

</details>

<details>
<summary><b><a href="https://github.com/bestagentkits/jev-skillful">bestagentkits/jev-skillful</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · bestagentkits

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.

</details>

<details>
<summary><b><a href="https://github.com/buchmark/claude-jev">buchmark/claude-jev</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · buchmark

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Claude Code plugin that scores review findings, debug hypotheses and design options with TypeSafe's Jev — calibrated probabilities instead of one more opinion.

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-starter">hamakyo/jev-starter</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · hamakyo

##### Veri

Yıldız **1** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-model-router-demo">jcpsimmons/jev-model-router-demo</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · jcpsimmons

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

</details>

<details>
<summary><b><a href="https://github.com/omni-/ask-jev">omni-/ask-jev</a></b> — ⭐1 · PowerShell · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · PowerShell · MIT · omni-

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions.

</details>

<details>
<summary><b><a href="https://github.com/poponline63/hermes-jev-north-star">poponline63/hermes-jev-north-star</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · poponline63

##### Veri

Yıldız **1** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven.

</details>

<details>
<summary><b><a href="https://github.com/Ravinder82/jev-flash-router">Ravinder82/jev-flash-router</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · Ravinder82

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code

</details>

<details>
<summary><b><a href="https://github.com/rthomas24/jev-realtime-trading">rthomas24/jev-realtime-trading</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · rthomas24

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rthomas24--jev-realtime-trading/f27df5cca6b8e2cf.png" width="100%" alt="rthomas24/jev-realtime-trading screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/codex-jev-compaction">Wang-auspicious/codex-jev-compaction</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · Wang-auspicious

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills.

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/pi-jev-compaction">Wang-auspicious/pi-jev-compaction</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · Wang-auspicious

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev-powered context compaction for Pi. Keep critical instructions and tool history, prune the noise, and fall back gracefully.

</details>

<details>
<summary><b><a href="https://github.com/ably-labs/jev-pong">ably-labs/jev-pong</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · Apache-2.0 · ably-labs

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Pong where the ball moves one step per model decision. Jev vs LLMs via Vercel AI Gateway, every player and agent on an Ably channel.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b51a044f9d543ef0.png" width="100%" alt="ably-labs/jev-pong screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b5b9b482a58f2c01.gif" width="100%" alt="ably-labs/jev-pong animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/aidil2105/jev-browser-pilot">aidil2105/jev-browser-pilot</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · aidil2105

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification.

</details>

<details>
<summary><b><a href="https://github.com/altregubov/jev-antigravity-mcp">altregubov/jev-antigravity-mcp</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · altregubov

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/anisselbd/jev-phishing-bench">anisselbd/jev-phishing-bench</a></b> — Python · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · anisselbd

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-align">caiovicentino/jev-align</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · caiovicentino

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Calibrated alignment verifier for LLM responses and agent plans — powered by Jev

</details>

<details>
<summary><b><a href="https://github.com/cbruyndoncx/AskJev-MCP">cbruyndoncx/AskJev-MCP</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · cbruyndoncx

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence

</details>

<details>
<summary><b><a href="https://github.com/doeixd/jev-pref">doeixd/jev-pref</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · doeixd

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.

</details>

<details>
<summary><b><a href="https://github.com/DoGMaTiiC/hermes-jev">DoGMaTiiC/hermes-jev</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · DoGMaTiiC

##### Veri

Yıldız **0** · Fork 0 · Açık issue 7 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only.

</details>

<details>
<summary><b><a href="https://github.com/duketopceo/jev-compact">duketopceo/jev-compact</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · duketopceo

##### Veri

Yıldız **0** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP

</details>

<details>
<summary><b><a href="https://github.com/enderzcx/spire-jev">enderzcx/spire-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · enderzcx

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Slay the Spire 2 agent controller: planner models, Jev fast decisions, and verified multi-card turn execution

</details>

<details>
<summary><b><a href="https://github.com/EtienneLescot/jev-router">EtienneLescot/jev-router</a></b> — HTML · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · HTML · MIT · EtienneLescot

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model tier and reasoning depth.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/etiennelescot--jev-router/96217fad0b128b3e.png" width="100%" alt="EtienneLescot/jev-router screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/flaviusapop/jev-router">flaviusapop/jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · flaviusapop

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Routes each turn in Claude Code, Codex, Grok and opencode to the cheapest model and reasoning depth that can finish it, using TypeSafe Jev

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/flaviusapop--jev-router/b7f868696d35b78b.png" width="100%" alt="flaviusapop/jev-router screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Friedjof/jev-mobile">Friedjof/jev-mobile</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · Friedjof

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Fast structured Android control loops with TypeSafe Jev and Mobile MCP

</details>

<details>
<summary><b><a href="https://github.com/gzawadzki/jev-usecases">gzawadzki/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · gzawadzki

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage

</details>

<details>
<summary><b><a href="https://github.com/hangarbay/jev.mcp">hangarbay/jev.mcp</a></b> — Go · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Go · MIT · hangarbay

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/HomenShum/jev-swap">HomenShum/jev-swap</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · HomenShum

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Claude Code skill: swap System 2 LLM pipeline components for System 1 TypeSafe Jev decisions via investigation, live three-arm eval, fallback, and an independent judge

</details>

<details>
<summary><b><a href="https://github.com/IAnMove/jev-game-agent">IAnMove/jev-game-agent</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · IAnMove

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Experimental Jev game agent: RAM, emulator lookahead, checkpoint search and verified recordings. Bring your own ROM and BizHawk.

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-codex-plugin">integrate-your-mind/jev-codex-plugin</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · integrate-your-mind

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Open-source Codex plugin for TypeSafe Jev decision consultation, failure diagnosis, and evidence-based completion review

</details>

<details>
<summary><b><a href="https://github.com/its-panzer/jev-model-router">its-panzer/jev-model-router</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · its-panzer

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A policy router that picks the cheapest Claude model that can finish the job

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/its-panzer--jev-model-router/98819f5aaf8e6373.png" width="100%" alt="its-panzer/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcressler/fast-jev-compaction-codex">jcressler/fast-jev-compaction-codex</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · jcressler

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Task-aware Jev evidence selection and exact local recovery around native Codex compaction.

</details>

<details>
<summary><b><a href="https://github.com/jh1373/jev-search">jh1373/jev-search</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · jh1373

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Search your Obsidian vault locally and offline with no API key, then rerank the top results with Jev only after you approve exactly what gets sent. Experimental preview.

</details>

<details>
<summary><b><a href="https://github.com/jmanhype/jev-dspy-lab">jmanhype/jev-dspy-lab</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · jmanhype

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows

</details>

<details>
<summary><b><a href="https://github.com/kaijia323/dsh-plugin-jev">kaijia323/dsh-plugin-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · kaijia323

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">MahmoudAdelbghany/jev-browser</a></b> — JavaScript · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MahmoudAdelbghany

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included.

</details>

<details>
<summary><b><a href="https://github.com/maito1201/jev-harness">maito1201/jev-harness</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · maito1201

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe jev でエージェントの応答を審査し、形式的な完了を Stop hook で差し戻す Claude Code / Codex plugin

</details>

<details>
<summary><b><a href="https://github.com/max1874/jev-computer-use">max1874/jev-computer-use</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · max1874

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A macOS computer-use agent with a dynamic, indexed action space. No screenshots, no coordinates. A macOS port of browser-use/jev-ultrafast.

</details>

<details>
<summary><b><a href="https://github.com/micic-mihajlo/jev-tool-runner">micic-mihajlo/jev-tool-runner</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · micic-mihajlo

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/milanboers/jev-plays-pokemon">milanboers/jev-plays-pokemon</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · NOASSERTION · milanboers

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Playing Pokemon Red using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/minhgv/jev-mcp">minhgv/jev-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · minhgv

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe Jev MCP decision layer for coding agents and CI

</details>

<details>
<summary><b><a href="https://github.com/morcoan/JevSeek">morcoan/JevSeek</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · morcoan

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools, persistent sessions, React desktop, and documented research.

</details>

<details>
<summary><b><a href="https://github.com/MSalvalaggio/jev-reflex">MSalvalaggio/jev-reflex</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · MSalvalaggio

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision).

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-mcp">nekowasabi/jev-routing-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · nekowasabi

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/noetion/dsh-jev">noetion/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · noetion

##### Veri

Yıldız **0** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.

</details>

<details>
<summary><b><a href="https://github.com/ourines/hermes-jev">ourines/hermes-jev</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · ourines

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev decision sidekick for Hermes Agent — TypeSafe and Cloudflare, explicit tools and official skill

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-mcp-router">Pinutss/jev-mcp-router</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · Pinutss

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Select relevant MCP tools under a context-token budget, without executing them.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-mcp-router/3947a2a5cc3750c8.png" width="100%" alt="Pinutss/jev-mcp-router screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-memory-selector">Pinutss/jev-memory-selector</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · Pinutss

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-memory-selector/6b6b7efc3440b641.png" width="100%" alt="Pinutss/jev-memory-selector screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-plugins">Pinutss/jev-plugins</a></b> — inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · MIT · Pinutss

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Cursor and Hermes marketplace for the four published JEV Labs routers.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-plugins/b3fcd72ac9e61f49.jpg" width="100%" alt="Pinutss/jev-plugins screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/QuentinDanblon/pi-fast-jev-compaction">QuentinDanblon/pi-fast-jev-compaction</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · NOASSERTION · QuentinDanblon

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Verbatim context pruning for the pi coding agent, scored by TypeSafe Jev: stale tool calls and results are dropped or truncated, everything kept stays verbatim.

</details>

<details>
<summary><b><a href="https://github.com/raj8525/universal-jev">raj8525/universal-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · raj8525

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-gates">rashedInt32/jev-gates</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · MIT · rashedInt32

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/3996d0153a09b158.gif" width="100%" alt="rashedInt32/jev-gates screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/464e518e8a602a0d.gif" width="100%" alt="rashedInt32/jev-gates animation"><br><sub>hareketli kayıt · <a href="https://raw.githubusercontent.com/rashedInt32/jev-gates/main/demo/out/jev-gates.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ravi3594444/jev-agent1">ravi3594444/jev-agent1</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · ravi3594444

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/rubichandrap/hermes-jev-guard">rubichandrap/hermes-jev-guard</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · rubichandrap

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check

</details>

<details>
<summary><b><a href="https://github.com/sypherin/jev-trace-classifier">sypherin/jev-trace-classifier</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · sypherin

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next

</details>

<details>
<summary><b><a href="https://github.com/szocpaul/jev-compaction-prime">szocpaul/jev-compaction-prime</a></b> — inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · szocpaul

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Verbatim, decision-based context compaction for Prime Agent — instead of summaries, stale tool calls are scored and dropped; everything kept stays byte-for-byte intact.

</details>

<details>
<summary><b><a href="https://github.com/tgiridhar/claude-code-jev-smart-router">tgiridhar/claude-code-jev-smart-router</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · tgiridhar

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task phase and the cost of an undetected error, gated by prompt-cache arithmetic. Proof of concept.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tgiridhar--claude-code-jev-smart-router/28b9e1b2a005c7e2.png" width="100%" alt="tgiridhar/claude-code-jev-smart-router screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/themsquared/jev-benchmark">themsquared/jev-benchmark</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · Apache-2.0 · themsquared

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.

</details>

<details>
<summary><b><a href="https://github.com/thevibeworks/awesome-typesafe-jev">thevibeworks/awesome-typesafe-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · NOASSERTION · thevibeworks

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/ussyverse/hermes-jev-router">ussyverse/hermes-jev-router</a></b> — Python · inferred · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · ussyverse

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending.

</details>

<details>
<summary><b><a href="https://github.com/xucian/fbyte-jev-vs-claude">xucian/fbyte-jev-vs-claude</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · HTML · xucian

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev vs Claude — Structured Classification Benchmark. 5 tasks, 5 models, 20 cases each. Comparing Jev (via OpenRouter) against Claude Opus 4.6 and Sonnet 4.6, with and without adaptive thinking.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/watch?v=UT4bZkaxDe4"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/watch?v=UT4bZkaxDe4">İzleme yeri youtube.com</a> · oynatma kaynak sitede açılır; GitHub bunu satır içi gömemez</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/yangzhou-chaofan/awesome-jev-prompt">yangzhou-chaofan/awesome-jev-prompt</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · JavaScript · CC0-1.0 · yangzhou-chaofan

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

latest top 100 showcases for jev (keep updating) from x / github / latest sources

</details>

<details>
<summary><b><a href="https://github.com/zbloss/jev-plays-pokemon">zbloss/jev-plays-pokemon</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · Python · MIT · zbloss

##### Veri

Yıldız **0** · Fork 0 · Açık issue 2 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Like Claude Plays Pokemon, but with Jev

</details>

<details>
<summary><b><a href="https://github.com/zhangxaochen/dsh-jev">zhangxaochen/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `inferred` · TypeScript · MIT · zhangxaochen

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev (System One decision model) plugin suite for DeepSeek Harness (dsh)

</details>

<details>
<summary><b><a href="https://github.com/DevMortimer/pi-warden">DevMortimer/pi-warden</a></b> — ⭐61 · TypeScript · unverified · 0 天 · ⭐+4</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `unverified` · TypeScript · MIT · DevMortimer

##### Veri

Yıldız **61** (+4) · Fork 2 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop

> Guardrails that steer an agent before it acts. Demonstrates the gate pattern, where the decision is cheap enough to run on every step.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devmortimer--pi-warden/b8dc20ac6694613a.png" width="100%" alt="DevMortimer/pi-warden screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/3clyp50/a0-typesafe-ai">3clyp50/a0-typesafe-ai</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `unverified` · Python · MIT · 3clyp50

##### Veri

Yıldız **4** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/3clyp50--a0-typesafe-ai/9aa8ea4ef8241f14.png" width="100%" alt="3clyp50/a0-typesafe-ai screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/pi-quiet-ask">HyunjunJeon/pi-quiet-ask</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `unverified` · TypeScript · MIT · HyunjunJeon

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe Jev as the pi coding agent's quiet decision layer

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hyunjunjeon--pi-quiet-ask/7ee3a99430e853d8.png" width="100%" alt="HyunjunJeon/pi-quiet-ask screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/zoidsh/tenet">zoidsh/tenet</a></b> — ⭐3 · Go · unverified · 0 天</summary>

##### Temel bilgiler

`Ajan araçları: MCP, kancalar, geçitler ve kodlama ajanları` · Topluluk · `unverified` · Go · MIT · zoidsh

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

The review gate for code that agents write: rules in plain language, judged on every commit

</details>

<a id="routing-guardrails"></a>

## Yönlendirme, koruma kuralları ve onaylar

Üretim biçimli kullanım senaryosu — her isteği gerçekten kaldırabilecek en ucuz modele gönderin ve sonuç üzerinde deterministik bir kontrol tutun.

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐41 · Rust · observed · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `observed` · Rust · NOASSERTION · Dicklesworthstone

##### Veri

Yıldız **41** · Fork 3 · Açık issue 1 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐24 · Python · observed · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `observed` · Python · brainstormity

##### Veri

Yıldız **24** (+1) · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

<sub>Kodda kullanıldığı tespit edildi: `typesafe/__init__.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 1 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `observed` · Python · MIT · Foadsf

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `observed` · TypeScript · MIT · qddegtya

##### Veri

Yıldız **1** · Fork 0 · Açık issue 3 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Typed decisions from a System One model. An uncertain answer is a different type from a confident one — and the compiler makes you handle it.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `observed` · Python · aniruddh-krovvidi

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐18 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MIT · yusukebe

##### Veri

Yıldız **18** (+2) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐6 · JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · JavaScript · MIT · mejiasd3v

##### Veri

Yıldız **6** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · andrelandgraf

##### Veri

Yıldız **3** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐3 · Python · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · MIT · keeltrace

##### Veri

Yıldız **3** (+1) · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/jerryfane/omp-jev-compaction">jerryfane/omp-jev-compaction</a></b> — ⭐2 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MIT · jerryfane

##### Veri

Yıldız **2** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · MIT · maker-KK

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · MIT · WiktorB2004

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · MIT · Pinutss

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · MIT · prismhq

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Shashank-H

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/aaronshaf/opencode-jev-model-router">aaronshaf/opencode-jev-model-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MIT · aaronshaf

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev-based automatic per-turn model routing for OpenCode

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Jupyter · MIT · bitnovus

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/carllippert/jev-router">carllippert/jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MIT · carllippert

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Express with no routes. TypeSafe Jev picks which handler runs.

</details>

<details>
<summary><b><a href="https://github.com/cephalization/jev-triage">cephalization/jev-triage</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MIT · cephalization

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Uses typeful jev, zero sync to pull and sync large repositories for issue triage

</details>

<details>
<summary><b><a href="https://github.com/danfry1/jev-triage">danfry1/jev-triage</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MIT · danfry1

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

GitHub Action that labels, deduplicates and spam-checks issues with Jev, with calibrated confidence for every decision

</details>

<details>
<summary><b><a href="https://github.com/danielhirt/jev-lab">danielhirt/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · danielhirt

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison

</details>

<details>
<summary><b><a href="https://github.com/denikuchero/jev-chess-lab">denikuchero/jev-chess-lab</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · GPL-3.0 · denikuchero

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev chess experiments: independent decisions vs tactical and Stockfish assistance, with full traces and video replays

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/denikuchero--jev-chess-lab/93f39c2d8831bde6.gif" width="100%" alt="denikuchero/jev-chess-lab screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/denikuchero--jev-chess-lab/5b385b4d2de02637.gif" width="100%" alt="denikuchero/jev-chess-lab animation"><br><sub>hareketli kayıt · <a href="https://raw.githubusercontent.com/denikuchero/jev-chess-lab/main/docs/games/01-raw/replay.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gnoviawan/omp-jev-tools">gnoviawan/omp-jev-tools</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · NOASSERTION · gnoviawan

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation verification

</details>

<details>
<summary><b><a href="https://github.com/hugo-alves/jev-router-playground">hugo-alves/jev-router-playground</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · JavaScript · MIT · hugo-alves

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Interactive playground for testing Jev model-routing decisions against OpenRouter models

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hugo-alves--jev-router-playground/93692a5f183f12e1.jpg" width="100%" alt="hugo-alves/jev-router-playground screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iefnaf/pi-jev">iefnaf/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MIT · iefnaf

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Pi extension suite powered by Jev: selective context compaction and model routing

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-macos-loop">jcpsimmons/jev-macos-loop</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · JavaScript · AGPL-3.0 · jcpsimmons

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Native macOS computer-use loop: OmniParser CoreML, Apple Vision OCR, accessibility labels, and Jev decisions through Vercel AI Gateway.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jcpsimmons--jev-macos-loop/b368b1d9b147950e.png" width="100%" alt="jcpsimmons/jev-macos-loop screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jethrojones/hermes-jev-router">jethrojones/hermes-jev-router</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · NOASSERTION · jethrojones

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/juanegido/jev-pr-judge">juanegido/jev-pr-judge</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MIT · juanegido

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Typed verdicts on pull requests with TypeSafe System One (Jev): one parallel call, policy in code, usable as a GitHub Action

</details>

<details>
<summary><b><a href="https://github.com/kenhuangus/jev-usecases">kenhuangus/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · MIT · kenhuangus

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kenhuangus--jev-usecases/be919255190f6495.png" width="100%" alt="kenhuangus/jev-usecases screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-bot">kevin9327/jev-bot</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · MIT · kevin9327

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.

</details>

<details>
<summary><b><a href="https://github.com/makefinks/jev-feed-filter">makefinks/jev-feed-filter</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MIT · makefinks

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Smart, dynamic AI filtering for X and YouTube feeds using Jev

</details>

<details>
<summary><b><a href="https://github.com/maraichr/jev-triage">maraichr/jev-triage</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · JavaScript · MIT · maraichr

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Cross-border B2B case triage prototype using TypeSafe Jev via OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/MoonTory/pi-jev-harness">MoonTory/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · MoonTory

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards tool calls

</details>

<details>
<summary><b><a href="https://github.com/nitinnat/jev-gateway">nitinnat/jev-gateway</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · JavaScript · MIT · nitinnat

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A small local HTTP service for TypeSafe AI's Jev through Vercel

</details>

<details>
<summary><b><a href="https://github.com/rajivkuriakose/typesafe-jev-examples">rajivkuriakose/typesafe-jev-examples</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · MIT · rajivkuriakose

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/RemiCarbonne/jev-code-context-router">RemiCarbonne/jev-code-context-router</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · MIT · RemiCarbonne

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/SadiqOnGithub/jev-lab">SadiqOnGithub/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · TypeScript · SadiqOnGithub

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API

</details>

<details>
<summary><b><a href="https://github.com/stbenjam/jev-eight-ball">stbenjam/jev-eight-ball</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · JavaScript · stbenjam

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A liquid magic eight ball powered by TypeSafe Jev decisions through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/TokenTrim/jev-routing-experiment">TokenTrim/jev-routing-experiment</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · Python · Apache-2.0 · TokenTrim

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tokentrim--jev-routing-experiment/1c31bd606ebc1994.png" width="100%" alt="TokenTrim/jev-routing-experiment screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wadadanet/faq-jev-router">wadadanet/faq-jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `inferred` · JavaScript · MIT · wadadanet

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Cascade FAQ routing with TypeSafe Jev — category → FAQ or not found (GitHub Pages demo)

</details>

<details>
<summary><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">iammrduncan/typesafe-ai-benchmark</a></b> — ⭐31 · TypeScript · unverified · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `unverified` · TypeScript · MIT · iammrduncan

##### Veri

Yıldız **31** (+1) · Fork 5 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.

> A gateway that mimics the System One interface, which is what makes side-by-side benchmarking possible without rewriting the caller.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/3d66c620e48ff597.gif" width="100%" alt="iammrduncan/typesafe-ai-benchmark animation"><br><sub>hareketli kayıt · <a href="https://raw.githubusercontent.com/iammrduncan/typesafe-ai-benchmark/main/docs/media/theater-demo.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kavehmz/typesafe-playground">kavehmz/typesafe-playground</a></b> — ⭐4 · JavaScript · unverified · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `unverified` · JavaScript · kavehmz

##### Veri

Yıldız **4** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/kavehmz/typesafe-playground/main/docs/images/demo03-fable.png" width="100%" alt="kavehmz/typesafe-playground screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/raihankhan-rk/diffjury">raihankhan-rk/diffjury</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Temel bilgiler

`Yönlendirme, koruma kuralları ve onaylar` · Topluluk · `unverified` · TypeScript · raihankhan-rk

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

DiffJury — TypeSafe Jev PR risk router + code review coach

</details>

<a id="evaluation"></a>

## Değerlendirme, kalibrasyon ve kıyaslamalar

Kararların iyi olduğunu insan nereden bilsin? Kalibrasyon bu ekosistemde açık sorudur ve bunlar onu ölçen projelerdir.

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `observed` · Go · MIT · Gaurav-Gosain

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — Python · observed · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `observed` · Python · akash-kamat

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — Python · observed · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `observed` · Python · Apache-2.0 · hev

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/JoshuaSP/open-jev">JoshuaSP/open-jev</a></b> — ⭐14 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · MIT · JoshuaSP

##### Veri

Yıldız **14** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Typed JSON inference with DiffusionGemma, with Every and Jev benchmark results

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/joshuasp--open-jev/1d4a9f6368358e43.png" width="100%" alt="JoshuaSP/open-jev screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rorshopping/jev-on-a-laptop">rorshopping/jev-on-a-laptop</a></b> — ⭐14 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · NOASSERTION · rorshopping

##### Veri

Yıldız **14** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Unofficial study: Jev-style parallel typed decisions on stock 1.5B-8B models on an Apple Silicon laptop. Benchmarks, research notes, and a Hugging Face Space demo.

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐7 · Python · inferred · 1 天 · ⭐+1</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · Apache-2.0 · AbdelStark

##### Veri

Yıldız **7** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐4 · TypeScript · inferred · 2 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · TypeScript · MIT · y0usaf

##### Veri

Yıldız **4** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐3 · Python · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · NOASSERTION · Heman10x-NGU

##### Veri

Yıldız **3** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · Apache-2.0 · ikermoel

##### Veri

Yıldız **2** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Open alternative to Jev: typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with benchmarks

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · MIT · wondertwins

##### Veri

Yıldız **2** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rongxinzy/LightJev">rongxinzy/LightJev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · Apache-2.0 · rongxinzy

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Train lightweight language backbones for typed decisions and candidate probabilities. CE/Brier training, evaluation, and an offline end-to-end demo.

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · 4esv

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-eval/main/results/coverage.png" width="100%" alt="4esv/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/aieo-product/jev-gamebenchmark">aieo-product/jev-gamebenchmark</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · MIT · aieo-product

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Sandbox & benchmark: optimize how you ask Jev (TypeSafe System One) to play falling-block puzzle games, head-to-head against LLMs

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · TypeScript · MIT · Danu28

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · TeX · NOASSERTION · dnakhoa

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · eggmasonvalue

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · MIT · jujumilk3

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · JavaScript · MIT · KantaHayashiAI

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and">musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and</a></b> — HTML · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · HTML · MIT · musman550

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@automatewithmusfiraai"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@automatewithmusfiraai">İzleme yeri youtube.com</a> · oynatma kaynak sitede açılır; GitHub bunu satır içi gömemez</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/onlyoneaman/jev-eval">onlyoneaman/jev-eval</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · TypeScript · MIT · onlyoneaman

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/onlyoneaman--jev-eval/e5d471e96e134f81.png" width="100%" alt="onlyoneaman/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/robipop22/Jev-is-odd">robipop22/Jev-is-odd</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · JavaScript · MIT · robipop22

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Ask Jev by TypeSafe AI whether a number is odd. TypeScript, real token usage, and latency benchmarks.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/robipop22--jev-is-odd/5c4ddde817bd6cdc.png" width="100%" alt="robipop22/Jev-is-odd screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shunta-furukawa/jev-tick-lab">shunta-furukawa/jev-tick-lab</a></b> — inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · shunta-furukawa

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis.

</details>

<details>
<summary><b><a href="https://github.com/teyhouse/jev-secret-detection">teyhouse/jev-secret-detection</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · teyhouse

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" width="100%" alt="teyhouse/jev-secret-detection screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/uspraveen/Jev-Reranker">uspraveen/Jev-Reranker</a></b> — inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · MIT · uspraveen

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A System-1 model based memory retrieval reranked using caliberated decision space instead of embeddings

</details>

<details>
<summary><b><a href="https://github.com/zhuyansen/jev-support-pulse">zhuyansen/jev-support-pulse</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `inferred` · Python · MIT · zhuyansen

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Does a Jev-labelled support-tweet stream spike before a brand admits an outage? At equal false alarms it catches 17 vs 10 incidents (volume), ~4h ahead; a good keyword list is almost as good.

</details>

<details>
<summary><b><a href="https://github.com/Mapika/decider">Mapika/decider</a></b> — ⭐21 · Python · unverified · 0 天 · ⭐+8</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `unverified` · Python · Apache-2.0 · Mapika

##### Veri

Yıldız **21** (+8) · Fork 2 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mapika--decider/c67d355f22dcb51a.gif" width="100%" alt="Mapika/decider animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/genai-craft/openvons">genai-craft/openvons</a></b> — ⭐7 · Python · unverified · 0 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `unverified` · Python · NOASSERTION · genai-craft

##### Veri

Yıldız **7** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド

</details>

<details>
<summary><b><a href="https://github.com/mithalouni/system-one-open">mithalouni/system-one-open</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### Temel bilgiler

`Değerlendirme, kalibrasyon ve kıyaslamalar` · Topluluk · `unverified` · Python · NOASSERTION · mithalouni

##### Veri

Yıldız **4** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal)

</details>

<a id="research-models"></a>

## Açık yeniden üretimler, ağırlıklar ve mimari araştırması

Açık ağırlıklar, küçük kopyalar ve mimari çalışmaları. Bunlardan birkaçı, kalibrasyon davranışının yalnızca kamuya açık materyalden yeniden üretilememesi yüzünden var.

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐51 · Python · observed · 0 天 · ⭐+3</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `observed` · Python · MIT · kshetrajna12

##### Veri

Yıldız **51** (+3) · Fork 3 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐260 · Python · inferred · 0 天 · ⭐+22</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `inferred` · Python · MIT · TianyuCodings

##### Veri

Yıldız **260** (+22) · Fork 24 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/5055af419619e7e4.gif" width="100%" alt="TianyuCodings/NanoJev animation"><br><sub>hareketli kayıt · <a href="https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/assets/side_by_side_maze.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐16 · Python · inferred · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `inferred` · Python · MIT · r-ms

##### Veri

Yıldız **16** (+2) · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `observed`

##### Veri

İndirme 25 · Beğeni 2 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 0 天</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `observed`

##### Veri

İndirme 0 · Beğeni 0 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐119 · Python · inferred · 0 天 · ⭐+4</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `inferred` · Python · ekzhang

##### Veri

Yıldız **119** (+4) · Fork 11 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐19 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `inferred` · Python · MIT · bnsd55

##### Veri

Yıldız **19** · Fork 3 · Açık issue 4 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-nethack">integrate-your-mind/jev-nethack</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `inferred` · Python · integrate-your-mind

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev x NetHack: bounded runner, research code, and completed recording releases

</details>

<details>
<summary><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">legacybridge-tech/pi-typesafe-jev</a></b> — TypeScript · inferred · 1 天</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `inferred` · TypeScript · NOASSERTION · legacybridge-tech

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.

</details>

<details>
<summary><b><a href="https://github.com/objectgraph/jev-samegame-bench">objectgraph/jev-samegame-bench</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `inferred` · TypeScript · MIT · objectgraph

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

What should a decision model be shown to play SameGame? 21 prompt strategies for TypeSafe's Jev, 76,795 logged requests and responses, reproducible tables. MIT.

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `inferred` · Python · shellneko

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐5 · Python · unverified · 1 天</summary>

##### Temel bilgiler

`Açık yeniden üretimler, ağırlıklar ve mimari araştırması` · Topluluk · `unverified` · Python · NOASSERTION · zhihz

##### Veri

Yıldız **5** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<a id="apps-demos"></a>

## Uygulamalar, oyunlar, robotik ve etkileşimli demolar

Oyunlar, robotlar, tarayıcılar ve panolar. Gecikme ile maliyet iddialarını okunur kılan şey demolardır.

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · Python · Apache-2.0 · zadescoxp

##### Veri

Yıldız **7** · Fork 1 · Açık issue 3 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · TypeScript · daftAI2026

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · Rust · MIT · markjaquith

##### Veri

Yıldız **1** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · TypeScript · adiun

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 1 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · Dart · Bud-ro

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/sandra-arato/icon-matcher">sandra-arato/icon-matcher</a></b> — TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · TypeScript · MIT · sandra-arato

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Match a UI section title to a Hugeicons icon using TypeSafe.ai's Choice primitive — no lexical/keyword search.

</details>

<details>
<summary><b><a href="https://github.com/sandra-arato/icon-matcher-ui">sandra-arato/icon-matcher-ui</a></b> — TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · TypeScript · MIT · sandra-arato

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Browser-only UI for icon-matcher — paste a TypeSafe.ai key, match a UI title to an icon live, no backend.

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · Python · MIT · tirukovelamanoj

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/8c1b0d55baf76296.gif" width="100%" alt="tirukovelamanoj/jev-plays-doom animation"><br><sub>hareketli kayıt · <a href="https://raw.githubusercontent.com/tirukovelamanoj/jev-plays-doom/main/docs/jev-doom.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · TypeScript · wustep

##### Veri

Yıldız **0** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://x.com/tspy/status/2100864234523685146">X intent labeller</a></b> — @tspy · observed · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `observed` · [yishan](https://x.com/tspy) · @tspy · x.com

##### Veri

Görüntüleme 2364 · Beğeni 15 · Yorum 9 · Yayınlandı 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A Chrome extension that labels posts in an X timeline with their intent and probability as you scroll, drawn as a tag directly after each post's timestamp. Categories include inducement, provocation, promotion, machine-generated, persuasion, entertainment and information. A side panel reports session counts (seen, judged, correct) and cumulative token cost. The author reports near-instant responses and usable accuracy before any tuning.

<sub>Orijinal proje bağlantısı araştırılıyor.</sub>

> Worth reading as a latency argument rather than an accuracy one: labelling a timeline only works if the decision costs less than the scroll, which is the constraint a generative model cannot meet.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/0641644f12a25a45.jpg" width="100%" alt="X intent labeller screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/b80cf3173f63bdd7.gif" width="100%" alt="X intent labeller animation"><br><sub>hareketli kayıt · <a href="https://video.twimg.com/amplify_video/2100858340331200512/vid/avc1/1242x720/ex2FF5-TerVxo9xX.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐92 · Python · inferred · 0 天 · ⭐+3</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · Python · MIT · hr98w

##### Veri

Yıldız **92** (+3) · Fork 10 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐68 · TypeScript · inferred · 0 天 · ⭐+8</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · MIT · jkudish

##### Veri

Yıldız **68** (+8) · Fork 4 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/b4ae7fc04353e74c.gif" width="100%" alt="jkudish/jev-browser animation"><br><sub>hareketli kayıt · <a href="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐31 · JavaScript · inferred · 0 天 · ⭐+8</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · JavaScript · MIT · moritzkremb

##### Veri

Yıldız **31** (+8) · Fork 5 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/mizchi/jev-playground">mizchi/jev-playground</a></b> — ⭐14 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · mizchi

##### Veri

Yıldız **14** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/mario-jev">shantanugoel/mario-jev</a></b> — ⭐10 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · Python · shantanugoel

##### Veri

Yıldız **10** · Fork 2 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · emrickgarrett

##### Veri

Yıldız **5** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐5 · Python · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · Python · MIT · komorra

##### Veri

Yıldız **5** (+1) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/arielweinberger/jev-autopilot">arielweinberger/jev-autopilot</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · arielweinberger

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs $0.01.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/arielweinberger/jev-autopilot/main/docs/demo.png" width="100%" alt="arielweinberger/jev-autopilot screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐3 · JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · JavaScript · vinilana

##### Veri

Yıldız **3** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/Nainish-Rai/jev-frontend-qa">Nainish-Rai/jev-frontend-qa</a></b> — ⭐2 · Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · Python · Nainish-Rai

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Evidence-driven frontend QA built on Jev Ultrafast and Browser Harness, with a synthetic todo demo.

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · Go · MIT · paulsmith

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/reachjalil/jev-tree">reachjalil/jev-tree</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · MIT · reachjalil

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap.

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · MIT · vmendes90

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · Little-Planet-Labs

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · Python · PistachioAIHQ

##### Veri

Yıldız **1** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-mario">4esv/jev-mario</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · Python · 4esv

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe Jev plays Super Mario Bros 1-1 from a text description of the emulator RAM

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-mario/main/runs/1-1-jev-20260918-105017.gif" width="100%" alt="4esv/jev-mario screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-mario/main/runs/1-1-jev-20260918-105017.gif" width="100%" alt="4esv/jev-mario animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/bahramzada/jev-taxi-dispatch">bahramzada/jev-taxi-dispatch</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · JavaScript · MIT · bahramzada

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Real-vaxt taksi dispetçerlik simulyasiyası — TypeSafe JEV (System One) modeli ilə

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/bahramzada--jev-taxi-dispatch/e616f4168b15d3f2.png" width="100%" alt="bahramzada/jev-taxi-dispatch screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/BrendanH18/jev-lab">BrendanH18/jev-lab</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · Python · MIT · BrendanH18

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brendanh18--jev-lab/b16b9535e3744cd3.png" width="100%" alt="BrendanH18/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iluoxw/jev-vs-llm-snake">iluoxw/jev-vs-llm-snake</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · iluoxw

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev 与 LLM 同页对照的贪吃蛇

</details>

<details>
<summary><b><a href="https://github.com/jflam/jev1">jflam/jev1</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · JavaScript · jflam

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev (TypeSafe System One) proof of concept: smart-home assistant demo

</details>

<details>
<summary><b><a href="https://github.com/mttcnnng/jev-tsla-demo">mttcnnng/jev-tsla-demo</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · JavaScript · MIT · mttcnnng

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Educational vanilla JavaScript demo exploring Jev as a judgment overlay on a simple TSLA moving-average rule.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mttcnnng--jev-tsla-demo/b3b7ca7bf7d1a900.jpg" width="100%" alt="mttcnnng/jev-tsla-demo screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/pistachiopranay/jev-synergy-screening">pistachiopranay/jev-synergy-screening</a></b> — inferred · 1 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · pistachiopranay

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/rchovatiya88/cyber-breach-jev">rchovatiya88/cyber-breach-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · JavaScript · rchovatiya88

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model

</details>

<details>
<summary><b><a href="https://github.com/Spykoninho/trading-bot-jev">Spykoninho/trading-bot-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · Spykoninho

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Crypto trading bot on Binance testnet using TypeSafe (Jev) to judge news

</details>

<details>
<summary><b><a href="https://github.com/yatharth1706/jev-automation">yatharth1706/jev-automation</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · TypeScript · yatharth1706

##### Veri

Yıldız **0** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Trying automation on web browser via jev from typesafe

</details>

<details>
<summary><b><a href="https://github.com/YYK2007/jev-flappy">YYK2007/jev-flappy</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `inferred` · JavaScript · YYK2007

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev makes every flap-or-coast decision in a live game, exposing probabilities, latency, tokens, and cost.

</details>

<details>
<summary><b><a href="https://github.com/sorrycc/typesafe-snake">sorrycc/typesafe-snake</a></b> — ⭐17 · TypeScript · unverified · 1 天</summary>

##### Temel bilgiler

`Uygulamalar, oyunlar, robotik ve etkileşimli demolar` · Topluluk · `unverified` · TypeScript · sorrycc

##### Veri

Yıldız **17** · Fork 2 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code

</details>

<a id="media-discussions"></a>

## Yazılar, tartışmalar ve kardeş listeler

Lansman başlıkları, bağımsız yazılar ve bu alandaki diğer derlenmiş listeler. Bu depo tek değil ve bunu söylemek aksini varsaymaktan daha yararlı.

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐4564 · Python · observed · 0 天 · ⭐+190</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · Python · MIT · browser-use

##### Veri

Yıldız **4564** (+190) · Fork 277 · Açık issue 28 · Oluşturulma 2026-09-16 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

i. am. speed.

<sub>Kodda kullanıldığı tespit edildi: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/d3c9791c1ce6e146.gif" width="100%" alt="browser-use/jev-ultrafast animation"><br><sub>hareketli kayıt · <a href="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/demo.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1882 · observed · 2 天 · ⭐+4</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 1882 · Yorum 494 · Son push 2026-09-15 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐479 · Python · observed · 0 天 · ⭐+9</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · Python · MIT · Anil-matcha

##### Veri

Yıldız **479** (+9) · Fork 93 · Açık issue 8 · Oluşturulma 2023-05-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>Kodda kullanıldığı tespit edildi: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐192 · CSS · observed · 0 天 · ⭐+15</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · CSS · MIT · AbdelStark

##### Veri

Yıldız **192** (+15) · Fork 25 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>Kodda kullanıldığı tespit edildi: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐132 · TypeScript · observed · 0 天 · ⭐+13</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · TypeScript · dabit3

##### Veri

Yıldız **132** (+13) · Fork 13 · Açık issue 15 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

<sub>Kodda kullanıldığı tespit edildi: `jev-lint/proxy.mjs`, `jev-tower/jev-proxy.mjs`, `jev-instant-search/bench/dump.ts`, `jev-swarm/jev-proxy.mjs`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐103 · Python · observed · 0 天 · ⭐+5</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · Python · yibie

##### Veri

Yıldız **103** (+5) · Fork 9 · Açık issue 5 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐63 · observed · 0 天 · ⭐+10</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · CC0-1.0 · cobanov

##### Veri

Yıldız **63** (+10) · Fork 4 · Açık issue 3 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐50 · observed · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · CC0-1.0 · AnotiaWang

##### Veri

Yıldız **50** (+2) · Fork 13 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>Kodda kullanıldığı tespit edildi: `README.md`, `README_zh.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐40 · observed · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 40 · Yorum 9 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐28 · HTML · observed · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · HTML · CC0-1.0 · hellogumbo

##### Veri

Yıldız **28** (+2) · Fork 2 · Açık issue 5 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A community directory of projects built on Jev, TypeSafe AI's System One model.

<sub>Kodda kullanıldığı tespit edildi: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49754461">Most People on the Internet Miss What Jev Is About</a></b> — ⭐6 · observed · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 6 · Yorum 0 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49754516">Show HN: Jev vs. GPT-5.6 and Claude Haiku at Pong</a></b> — ⭐6 · observed · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 6 · Yorum 0 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 2 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 5 · Yorum 0 · Son push 2026-09-15 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 4 · Yorum 0 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐4 · Python · observed · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · Python · NOASSERTION · OmniJev

##### Veri

Yıldız **4** (+1) · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Papers, open reproductions and independent evaluations behind System One models and Jev.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 4 · Yorum 0 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 3 · Yorum 0 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49754951">Show HN: Using Jev to generate game levels in real time</a></b> — ⭐3 · observed · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 3 · Yorum 1 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 3 · Yorum 0 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### Veri

Yıldız **2** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49753667">Show HN: Explore 2D semantic space with the Jev model</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 2 · Yorum 0 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

SemanticSpace is an experiment around Jev, TypeSafe AI’s new model. It uses a Cartesian plane defined by arbitrary phrases for each axis, to map prompts onto the resulting 2D semantic space. You can edit the prompts and axes to visualize virtually any 2D relationship.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49750649">Show HN: Open-Source Alternative to TypeSafe.ai</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 2 · Yorum 1 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49744527">Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)</a></b> — ⭐2 · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 2 · Yorum 1 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Full disclosure, it was coded with AI, I don&#x27;t claim otherwise. But I wanted to test out tool calls and iterative problem solving using Jev and needed a simple library&#x2F;framework&#x2F;harness to do that.
SOKIT (System One Knowledge, Instructions and Tools) is the result

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49729945">The first (public) System One Model; Jev gives AI the properties of code</a></b> — ⭐2 · observed · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 2 · Yorum 0 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755005">Two techniques for working with System One models</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 2 · Yorum 0 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49745212">Typesafe&#x27;s Jev is the fish at the poker table</a></b> — ⭐2 · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 2 · Yorum 1 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49733647">Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step</a></b> — ⭐2 · observed · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 2 · Yorum 0 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49734345">Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD</a></b> — ⭐2 · observed · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 2 · Yorum 0 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755430">You could have built Jev</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed`

##### Veri

Puan 2 · Yorum 0 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐1 · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · NOASSERTION · aliaihub

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://github.com/ozers/jevsome-projects">ozers/jevsome-projects</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · JavaScript · MIT · ozers

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Open-source projects that provably call Jev, TypeSafe AI's System One model. Every entry links to the line of code that proves it. Refreshed daily.

</details>

<details>
<summary><b><a href="https://github.com/rhc98/awesome-jev">rhc98/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · TypeScript · NOASSERTION · rhc98

##### Veri

Yıldız **1** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself.

</details>

<details>
<summary><b><a href="https://github.com/alpibrusl/lex-judge">alpibrusl/lex-judge</a></b> — Lex · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · Lex · alpibrusl

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Typed judgments from a System One model, as a \[net\]-only Lex effect

</details>

<details>
<summary><b><a href="https://github.com/deepanwadhwa/OpenDecision">deepanwadhwa/OpenDecision</a></b> — Python · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · Python · Apache-2.0 · deepanwadhwa

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Open Type Safe System one model system

</details>

<details>
<summary><b><a href="https://github.com/gzd2032/typesafe-ai-test">gzd2032/typesafe-ai-test</a></b> — observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · gzd2032

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

a test repo for typesafe.ai

</details>

<details>
<summary><b><a href="https://github.com/hide-G/magi-system-on-jev">hide-G/magi-system-on-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · JavaScript · hide-G

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/hide-G/magi-system-on-jev/master/public/ogp.png" width="100%" alt="hide-G/magi-system-on-jev screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/JohnDotOwl/awesome-jev">JohnDotOwl/awesome-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · JavaScript · CC0-1.0 · JohnDotOwl

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A curated list of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/piyush97/focus-tube">piyush97/focus-tube</a></b> — JavaScript · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · JavaScript · MIT · piyush97

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model

</details>

<details>
<summary><b><a href="https://github.com/rbalch/typesafeai-review">rbalch/typesafeai-review</a></b> — Python · observed · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · Python · rbalch

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Using Typesafe.AI to generate diff reviews.

</details>

<details>
<summary><b><a href="https://github.com/soderlind/ai-provider-for-jev">soderlind/ai-provider-for-jev</a></b> — PHP · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · PHP · soderlind

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).

</details>

<details>
<summary><b><a href="https://github.com/TheGali/terrarium">TheGali/terrarium</a></b> — JavaScript · observed · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · JavaScript · MIT · TheGali

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.

</details>

<details>
<summary><b><a href="https://github.com/youngsemicolon/jev-lego">youngsemicolon/jev-lego</a></b> — Python · observed · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `observed` · Python · youngsemicolon

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A System One model builds Lego in 3D — code enumerates legal placements, Jev picks among them

</details>

<details>
<summary><b><a href="https://github.com/jarrodwatts/jev-trader">jarrodwatts/jev-trader</a></b> — ⭐767 · TypeScript · inferred · 1 天 · ⭐+22</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · jarrodwatts

##### Veri

Yıldız **767** (+22) · Fork 148 · Açık issue 2 · Oluşturulma 2026-09-16 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

</details>

<details>
<summary><b><a href="https://github.com/droidrun/mobile-jev">droidrun/mobile-jev</a></b> — ⭐87 · JavaScript · inferred · 1 天 · ⭐+5</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · JavaScript · MIT · droidrun

##### Veri

Yıldız **87** (+5) · Fork 16 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/superagents-lab/jev-search">superagents-lab/jev-search</a></b> — ⭐34 · TypeScript · inferred · 0 天 · ⭐+7</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · superagents-lab

##### Veri

Yıldız **34** (+7) · Fork 6 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/superagents-lab--jev-search/5a545ddfd6a52aed.png" width="100%" alt="superagents-lab/jev-search screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mrnugget/jev-shell-history">mrnugget/jev-shell-history</a></b> — ⭐26 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · mrnugget

##### Veri

Yıldız **26** (+2) · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Fish-style zsh history autosuggestions ranked by Jev (TypeSafe)

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

<sub>Yeniden dağıtım lisansı belirtilmediği için varlık üst depodan doğrudan bağlanmıştır.</sub>

</details>

<details>
<summary><b><a href="https://github.com/daseinlabs/open-jev">daseinlabs/open-jev</a></b> — ⭐25 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · daseinlabs

##### Veri

Yıldız **25** · Fork 4 · Açık issue 4 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov"><img src="" width="100%" alt="daseinlabs/open-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">IAmUnbounded/save-token-jev-clean</a></b> — ⭐25 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · IAmUnbounded

##### Veri

Yıldız **25** (+1) · Fork 6 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/hqman/JevScout">hqman/JevScout</a></b> — ⭐10 · Python · inferred · 0 天 · ⭐+6</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · hqman

##### Veri

Yıldız **10** (+6) · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4"><img src="" width="100%" alt="hqman/JevScout video"></a><br><sub><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4">Videoyu aç</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Kevthetech143/super-jev">Kevthetech143/super-jev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · Kevthetech143

##### Veri

Yıldız **5** · Fork 1 · Açık issue 2 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A small, extensible decision-to-action harness for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/danvega/hello-jev-java">danvega/hello-jev-java</a></b> — ⭐3 · Java · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Java · danvega

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/mateonunez/jod">mateonunez/jod</a></b> — ⭐3 · TypeScript · inferred · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · mateonunez

##### Veri

Yıldız **3** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers.

</details>

<details>
<summary><b><a href="https://github.com/haseeb-heaven/jev-system-one">haseeb-heaven/jev-system-one</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · MIT · haseeb-heaven

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/haseeb-heaven--jev-system-one/e41c848323b1077a.png" width="100%" alt="haseeb-heaven/jev-system-one screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/joelhooks/pi-fast-jev-compaction">joelhooks/pi-fast-jev-compaction</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · joelhooks

##### Veri

Yıldız **2** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Pi extension: verbatim context compaction with TypeSafe Jev decisions

</details>

<details>
<summary><b><a href="https://github.com/justinhe16/trade-jev">justinhe16/trade-jev</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · MIT · justinhe16

##### Veri

Yıldız **2** · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Backtest Jev (TypeSafe) as a BUY/SELL/HOLD trader on NQ L10 order-book data

</details>

<details>
<summary><b><a href="https://github.com/anxkhn/JevPlaysPokemon">anxkhn/JevPlaysPokemon</a></b> — ⭐1 · HTML · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · HTML · GPL-3.0 · anxkhn

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev plays Generation 3 Pokémon via Showdown and a real FireRed ROM.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/anxkhn--jevplayspokemon/fc9ead060d7fa36a.png" width="100%" alt="anxkhn/JevPlaysPokemon screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/jev-review-action">fatwang2/jev-review-action</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · JavaScript · MIT · fatwang2

##### Veri

Yıldız **1** · Fork 0 · Açık issue 2 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.

</details>

<details>
<summary><b><a href="https://github.com/lbotinelly/jev-little-airways">lbotinelly/jev-little-airways</a></b> — ⭐1 · HTML · inferred · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · HTML · MIT · lbotinelly

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A show-and-tell capability study for Jev, TypeSafe's System One decision model.

</details>

<details>
<summary><b><a href="https://github.com/sontakey/awesome-jev">sontakey/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · NOASSERTION · sontakey

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Unofficial list of insanely useful TypeSafe AI Jev / System One projects

</details>

<details>
<summary><b><a href="https://github.com/TanayPadar/gpt-vs-jev">TanayPadar/gpt-vs-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · TanayPadar

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Compare GPT generated language with JEV structured Noul decisions on the same input.

</details>

<details>
<summary><b><a href="https://github.com/tylerjharden/harden-jev-decides">tylerjharden/harden-jev-decides</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · tylerjharden

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.

</details>

<details>
<summary><b><a href="https://github.com/zaferayan/jev-example">zaferayan/jev-example</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · zaferayan

##### Veri

Yıldız **1** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/3l4l5/jev_test">3l4l5/jev_test</a></b> — inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · 3l4l5

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/adhamelhayek-lab/jev-connector">adhamelhayek-lab/jev-connector</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · JavaScript · adhamelhayek-lab

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/afanjul/jev-llm">afanjul/jev-llm</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · afanjul

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Fake autoregressive language model powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/aoprisan/jev-ts-repl">aoprisan/jev-ts-repl</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · aoprisan

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/Charlyhno-eng/jev-document-classification">Charlyhno-eng/jev-document-classification</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · Charlyhno-eng

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/charlyhno-eng--jev-document-classification/113bcf66f1648122.png" width="100%" alt="Charlyhno-eng/jev-document-classification screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/choxos/jev-reviewer">choxos/jev-reviewer</a></b> — inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · MIT · choxos

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/cmartinez9/jev-judge-bench">cmartinez9/jev-judge-bench</a></b> — inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · cmartinez9

##### Veri

Yıldız **0** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Binary LLM-judge bench — compare Jev (TypeSafe System One) against a frontier LLM judge on speed, cost, and agreement with human labels.

</details>

<details>
<summary><b><a href="https://github.com/Dujaydis/JevSysUno">Dujaydis/JevSysUno</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · Dujaydis

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/erhanmeydan/jev2048">erhanmeydan/jev2048</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · MIT · erhanmeydan

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

TypeSafe'in Jev karar modeli gerçek bir online 2048 sitesinde oynuyor — hamle başına tek API çağrısı, tek anahtar.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/erhanmeydan--jev2048/a2709def4f48e691.gif" width="100%" alt="erhanmeydan/jev2048 screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/erhanmeydan--jev2048/a2709def4f48e691.gif" width="100%" alt="erhanmeydan/jev2048 animation"><br><sub>hareketli kayıt</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/felixfisher/pi-jev-compaction">felixfisher/pi-jev-compaction</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · felixfisher

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Experimental Pi extension using TypeSafe Jev for auditable tool-history compaction

</details>

<details>
<summary><b><a href="https://github.com/haibt163/jev">haibt163/jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · haibt163

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/heaven-hm/jev-system-one">heaven-hm/jev-system-one</a></b> — inferred · 1 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · heaven-hm

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

</details>

<details>
<summary><b><a href="https://github.com/ilkerulusoy/pi-jev-compact">ilkerulusoy/pi-jev-compact</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · ilkerulusoy

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/JulioPeixoto/jev-decision-bench">JulioPeixoto/jev-decision-bench</a></b> — inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · JulioPeixoto

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/jun-shiromizu/mastra-jev">jun-shiromizu/mastra-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · jun-shiromizu

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/kentaro/jev-fizzbuzz">kentaro/jev-fizzbuzz</a></b> — HTML · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · HTML · kentaro

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-master">kevin9327/jev-master</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · MIT · kevin9327

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Typed System One decisions with Jev: Choice + Score + Noul composed in code.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevin9327--jev-master/cbf05c4561269075.png" width="100%" alt="kevin9327/jev-master screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kspviswa/chakravyuha-jev">kspviswa/chakravyuha-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · JavaScript · MIT · kspviswa

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kspviswa--chakravyuha-jev/4dfa22d0de9f27c1.png" width="100%" alt="kspviswa/chakravyuha-jev screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kuhung/understanding-jev">kuhung/understanding-jev</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · HTML · kuhung

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

深入解读 Jev 模型：毫秒级判定与工程边界

</details>

<details>
<summary><b><a href="https://github.com/LamplighterPaul/jev-piano">LamplighterPaul/jev-piano</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · LamplighterPaul

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev cannot generate a single note. Given a piano and the right questions, it improvises anyway.

</details>

<details>
<summary><b><a href="https://github.com/LingXuanYin/jev-chat">LingXuanYin/jev-chat</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · NOASSERTION · LingXuanYin

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Jev 聊天机：一个「只选不写」的聊天机——每个回复由逐词选择拼装，词典+分级索引+输入法式联想，由真实 Jev（TypeSafe System One）驱动。非官方实验，与 TypeSafe AI 无关联。

</details>

<details>
<summary><b><a href="https://github.com/memorysaver/jev-atari-lab">memorysaver/jev-atari-lab</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · GPL-2.0 · memorysaver

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Challenge Atari with Jev: structured decisions, value questions, and replayable experiments

</details>

<details>
<summary><b><a href="https://github.com/Nachom3/jevTrader">Nachom3/jevTrader</a></b> — Rust · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Rust · Nachom3

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

A High Frecuncy Trader made in Rust using Jev as a decision maker.

</details>

<details>
<summary><b><a href="https://github.com/narulaskaran/jev-data-questions">narulaskaran/jev-data-questions</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · narulaskaran

##### Veri

Yıldız **0** · Fork 0 · Açık issue 1 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/nishimotz/hello-jev">nishimotz/hello-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · nishimotz

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/nitro527/jev_project">nitro527/jev_project</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · nitro527

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/pavy23/jev_typesafeai_test">pavy23/jev_typesafeai_test</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · pavy23

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/ponyo877/jev-realtime-brain-scanner">ponyo877/jev-realtime-brain-scanner</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · JavaScript · ponyo877

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/rolottr/x-jev-classifier">rolottr/x-jev-classifier</a></b> — JavaScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · JavaScript · AGPL-3.0 · rolottr

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Chrome extension that stamps every X post with a type badge — alpha, shitpost, AI slop, bait — judged by Jev from Typesafe

</details>

<details>
<summary><b><a href="https://github.com/SamuelNittala/swiggy-jev-poc">SamuelNittala/swiggy-jev-poc</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · SamuelNittala

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/sueszli/qwen27b-jev">sueszli/qwen27b-jev</a></b> — inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · MIT · sueszli

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

multiple-choice questions for Qwen3.8-27B, read from logits

</details>

<details>
<summary><b><a href="https://github.com/TKY-27/JevSlop">TKY-27/JevSlop</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · TKY-27

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/TonyP-MR/jev-curation-engine">TonyP-MR/jev-curation-engine</a></b> — Python · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · Python · TonyP-MR

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions with existing LLM audit results.

</details>

<details>
<summary><b><a href="https://github.com/vava-nessa/pi-jev-compaction">vava-nessa/pi-jev-compaction</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · MIT · vava-nessa

##### Veri

Yıldız **0** · Fork 0 · Açık issue 0 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Verbatim, Jev-guided context compaction for Pi: drop stale tool calls and outputs, never summarize.

</details>

<details>
<summary><b><a href="https://github.com/Z761293629/pi-jev-helm">Z761293629/pi-jev-helm</a></b> — TypeScript · inferred · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `inferred` · TypeScript · Z761293629

##### Veri

Yıldız **0** · Fork 0 · Açık issue 10 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Üst kaynakta açıklama yayımlanmamış.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/typesafe-adblock">realZachi/typesafe-adblock</a></b> — ⭐44 · JavaScript · unverified · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `unverified` · JavaScript · MIT · realZachi

##### Veri

Yıldız **44** (+1) · Fork 3 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.

</details>

<details>
<summary><b><a href="https://github.com/devanshbatham/commit-miner">devanshbatham/commit-miner</a></b> — ⭐21 · Rust · unverified · 0 天 · ⭐+1</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `unverified` · Rust · devanshbatham

##### Veri

Yıldız **21** (+1) · Fork 5 · Açık issue 0 · Oluşturulma 2026-09-17 · Son push 2026-09-17 · İlk listelenme 2026-09-18

##### Özet

Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.

</details>

<details>
<summary><b><a href="https://github.com/phyous/tsai-sc">phyous/tsai-sc</a></b> — ⭐13 · Python · unverified · 2 天 · ⭐+1</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `unverified` · Python · MIT · phyous

##### Veri

Yıldız **13** (+1) · Fork 1 · Açık issue 0 · Oluşturulma 2026-09-16 · Son push 2026-09-16 · İlk listelenme 2026-09-18

##### Özet

TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.

<table><tr><th align="center" width="50%">Görsel</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/phyous--tsai-sc/f48a030ae92fb1fe.png" width="100%" alt="phyous/tsai-sc screenshot"></td>
<td align="center" valign="top"><sub>medya yayımlanmamış</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andysc/IBM-Q-System-One-3D-model">andysc/IBM-Q-System-One-3D-model</a></b> — ⭐12 · OpenSCAD · unverified · 2688 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `unverified` · OpenSCAD · andysc

##### Veri

Yıldız **12** · Fork 4 · Açık issue 1 · Oluşturulma 2019-03-16 · Son push 2019-05-10 · İlk listelenme 2026-09-18

##### Özet

3D-printed model of IBM Q System One

</details>

<details>
<summary><b><a href="https://github.com/razorback16/openjev">razorback16/openjev</a></b> — ⭐11 · Python · unverified · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `unverified` · Python · Apache-2.0 · razorback16

##### Veri

Yıldız **11** · Fork 2 · Açık issue 1 · Oluşturulma 2026-09-18 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Open, Jev-compatible System One decision server on DiffusionGemma

</details>

<details>
<summary><b><a href="https://github.com/zhengxuyu/litjev">zhengxuyu/litjev</a></b> — ⭐3 · Python · unverified · 0 天</summary>

##### Temel bilgiler

`Yazılar, tartışmalar ve kardeş listeler` · Topluluk · `unverified` · Python · Apache-2.0 · zhengxuyu

##### Veri

Yıldız **3** · Fork 1 · Açık issue 3 · Oluşturulma 2026-09-17 · Son push 2026-09-18 · İlk listelenme 2026-09-18

##### Özet

Turn any off-the-shelf LLM into a Jev -like decision layer

</details>

<a id="projects-by-implementation-language"></a>

## Uygulama diline göre projeler

Ekosistem Python ve TypeScript'te yoğunlaşıyor, ancak tipli istemciler başka dillerde de görünmeye devam ediyor. Bu tablo kayıtların kendisinden üretilir.

| Dil        | Kayıt | Örnekler                                                                                           |
| ---------- | ----- | -------------------------------------------------------------------------------------------------- |
| Python     | 133   | `typesafe-ai/system-one-adapter-python`, `typesafe-ai/typesafe-sdk-python`, `MrJev/awesome-jev`    |
| TypeScript | 120   | `typesafe-ai/typesafe-sdk-js`, `AntonioCoppe/jev-harness`, `opaielsheikh/typesafe-migration-guard` |
| JavaScript | 56    | `ziyu/sytem-one-sdk`, `Ying-Kai-Liao/jev-browser`, `arunav25/jev-mcp`                              |
| Rust       | 12    | `AkashPriyadarshii/jev-curate`, `abeldzan/jev-rs`, `AkashPriyadarshii/jev-git`                     |
| Go         | 11    | `Gaurav-Gosain/jev-go`, `Stumble/jev-go`, `anilsenay/jev`                                          |
| HTML       | 11    | `typesafe-ai/typesafe-ai.github.io`, `yzfly/awesome-jev-zh`, `vinilana/jev-eval-agent`             |
| PHP        | 4     | `Butochnikov/laravel-typesafe-jev`, `mzainzulifqar/jev-php-sdk`, `shanginn/jev-php`                |
| Elixir     | 3     | `nshkrdotcom/typesafe_sdk`, `typesend/typesafe_ai`, `dannote/jev`                                  |
| Java       | 3     | `Premo-Cloud/typesafe-sdk-java`, `Olti1947/jev-java`, `danvega/hello-jev-java`                     |
| Jupyter    | 2     | `jexp/neo4jev`, `bitnovus/jev-spam-eval`                                                           |
| C          | 1     | `giuliosmall/pg_typesafe`                                                                          |
| C#         | 1     | `saibimajdi/typesafeai-dotnet-sdk`                                                                 |
| CSS        | 1     | `AbdelStark/awesome-typesafe`                                                                      |
| Dart       | 1     | `Bud-ro/jev-demos`                                                                                 |
| Haskell    | 1     | `inanna-malick/jev-dsl`                                                                            |
| Lex        | 1     | `alpibrusl/lex-judge`                                                                              |
| OCaml      | 1     | `jonesmelton/verdict`                                                                              |
| OpenSCAD   | 1     | `andysc/IBM-Q-System-One-3D-model`                                                                 |
| PowerShell | 1     | `omni-/ask-jev`                                                                                    |
| Ruby       | 1     | `javiergradiche/ruby_llm-providers-typesafe`                                                       |
| TeX        | 1     | `dnakhoa/jev-deferred-crispification`                                                              |

<sub>Yalnızca dil belirten kayıtlar sayılır. Altyapı, dokümantasyon ve tartışma kayıtları bu tablonun dışında tutulur.</sub>

## Bu liste nasıl güncel kalıyor

Bu README'nin gövdesini hiçbir insan düzenlemez. Depo, zamanlanmış biçimde beş aşamalı bir iş akışı çalıştırır ve yalnızca gerçekten bir şey değiştiğinde commit eder.

<img src="assets/readme/pipeline.svg" width="100%" alt="Bu liste nasıl güncel kalıyor">

|             |                                                                                                                                                                                                                                                                                              |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **collect** | bir sorgu matrisi, resmî organizasyon, GitHub kod araması, Hacker News ve Hugging Face hub üzerinden GitHub araması.                                                                                                                                                                         |
| **curate**  | deterministik ve LLM'siz, bu yüzden aynı girdiyle art arda iki çalıştırma bayt düzeyinde aynı çıktıyı üretir. Alaka düzeyine iki sinyalli bir kural karar verir; ad çakışmaları (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD ve benzerleri) açık ve denetlenebilir bir listeyle dışlanır. |
| **media**   | her projenin kendi ekran görüntülerini ve ekran kayıtlarını toplar. Varlıklar bu depoya yalnızca proje yeniden dağıtıma uygun bir lisans beyan ettiğinde kopyalanır; aksi halde üst kaynağın URL'si doğrudan bağlanır ve kart bunu belirtir.                                                 |
| **render**  | her dil sürümünü tek bir şablondan üretir, böylece yirmi README yapı açısından asla birbirinden ayrışamaz.                                                                                                                                                                                   |
| **audit**   | bir kaydın URL'si yoksa, bir bağlantı ölüyse, iki kayıt aynı URL'yi yineliyorsa veya bir README üretilen biçiminden sapıyorsa derlemeyi başarısız kılar.                                                                                                                                     |

## Katkıda bulunma

Düzeltmeler memnuniyetle karşılanır ve bu listeyi iyileştirmenin en hızlı yoludur. Bir kayıt yanlış sınıflandırılmış, yanlış derecelendirilmiş ya da bir proje ad çakışması diye hatalı biçimde dışlanmışsa bir issue veya pull request açın — otomatik filtrelerin en çok yanılma olasılığı son kategoridedir. Ekleme yapmanın en iyi yolu README'yi düzenlemek değil, `scripts/collect.py` dosyasına bir kaynak eklemektir; çünkü README her turda yeniden üretilir.

---

<sub>Bağımsız topluluk projesi. TypeSafe AI ile bağlantılı değildir; onun tarafından onaylanmamış veya incelenmemiştir. Ürün davranışı, fiyatlandırma, sınırlar ve model takma adları bildirimsiz değişebilir; kritik her şeyi resmî belgelerle doğrulayın. Varlıklar üst projelerinin mülkiyetinde kalır ve yalnızca lisansın izin verdiği yerlerde yeniden üretilir.</sub>

<sub>Oluşturan · `render.py` · 2026-09-18T23:19:50+08:00</sub>
