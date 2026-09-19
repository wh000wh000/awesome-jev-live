<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>Chỉ mục Jev có phân hạng bằng chứng, tự dựng lại sau mỗi hai giờ.</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-477-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <b>Tiếng Việt</b> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **Chỉ mục trực tiếp** · Đồng bộ lần cuối: `2026-09-19T08:12:36+08:00` (UTC+8)
> · Mục: **477** · Mới trong lượt này: **54** · Ngôn ngữ triển khai: **27**

<sub>Mọi mục bên dưới đều do pipeline trong kho lưu trữ này thu thập, lọc và kiểm tra lại. Các con số và mốc thời gian đến từ nguồn, không phải từ một ảnh chụp viết tay.</sub>

## Nội dung

- [Jev là gì?](#jev-là-gì)
- [Cách các mục được phân hạng](#cách-các-mục-được-phân-hạng)
- [SDK chính thức và công cụ cho nhà phát triển](#sdk-chính-thức-và-công-cụ-cho-nhà-phát-triển) — **5**
- [Client, SDK và adapter do cộng đồng phát triển](#client-sdk-và-adapter-do-cộng-đồng-phát-triển) — **75**
- [Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã](#công-cụ-cho-agent-mcp-hook-cổng-chặn-và-agent-viết-mã) — **132**
- [Định tuyến, rào chắn và phê duyệt](#định-tuyến-rào-chắn-và-phê-duyệt) — **45**
- [Đánh giá, hiệu chỉnh và benchmark](#đánh-giá-hiệu-chỉnh-và-benchmark) — **38**
- [Bản tái tạo mở, trọng số và nghiên cứu kiến trúc](#bản-tái-tạo-mở-trọng-số-và-nghiên-cứu-kiến-trúc) — **20**
- [Ứng dụng, trò chơi, robot và demo tương tác](#ứng-dụng-trò-chơi-robot-và-demo-tương-tác) — **41**
- [Bài viết, thảo luận và các danh sách cùng chủ đề](#bài-viết-thảo-luận-và-các-danh-sách-cùng-chủ-đề) — **121**
- [Dự án theo ngôn ngữ triển khai](#dự-án-theo-ngôn-ngữ-triển-khai)
- [Danh sách này được giữ mới như thế nào](#danh-sách-này-được-giữ-mới-như-thế-nào)

## Jev là gì?

Jev là **System One model** đầu tiên của TypeSafe AI. Nó không viết văn xuôi. Nó nhận một trạng thái cùng những câu hỏi mà không gian trả lời do bạn định trước, rồi trả về các giá trị có kiểu kèm phân phối xác suất để mã của bạn rẽ nhánh.

|                      |                                                                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Hình dạng**        | `state + typed questions` → `constrained answers + probabilities` → `your code`                                                                                                                                          |
| **Nguyên thủy**      | `Choice` (chọn một trong ≤255 lựa chọn), `Score` (thang điểm 2–10), `Noul` (có/không theo xác suất)                                                                                                                      |
| **Endpoint**         | `POST https://api.typesafe.ai/v1/systemone`, model `jev-1.13.0` / bí danh `jev-latest`                                                                                                                                   |
| **Phù hợp**          | định tuyến, phân loại, chấm điểm, kiểm duyệt, xác minh và các cổng chặn độ trễ thấp trong một quy trình có giới hạn                                                                                                      |
| **Giới hạn đã biết** | việc đếm không đáng tin, suy luận nhiều tầng còn yếu, và tài liệu chính thức nêu chín nhóm khiếm khuyết. Đầu ra hợp lệ theo schema không đồng nghĩa với một quyết định đúng — hãy hiệu chỉnh trên dữ liệu của chính bạn. |

## Cách các mục được phân hạng

Phần lớn danh sách trong lĩnh vực này khẳng định là đã bao gồm. Danh sách này nói rõ nó thực sự đã xác minh đến đâu, rồi để bạn lọc theo đó.

| Hạng         | Ý nghĩa                                                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `official`   | Do chính TypeSafe AI công bố.                                                                                                                           |
| `observed`   | Một hiện vật công khai có thể mở ra và đọc — mã nguồn thật, cấu hình thật, hoặc một tuyên bố TypeSafe/Jev rõ ràng trong tên hay chủ đề của kho lưu trữ. |
| `inferred`   | Khớp nhờ một tín hiệu mơ hồ cùng vốn từ bổ trợ, nhưng chưa được đọc từng dòng.                                                                          |
| `unverified` | Có vẻ liên quan, chưa có gì được xác nhận độc lập. Chỉ được liệt kê để khám phá.                                                                        |

<a id="official-sdk"></a>

## SDK chính thức và công cụ cho nhà phát triển

Mọi thứ do chính TypeSafe công bố. Hãy bắt đầu từ đây.

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐261 · official · 6 天 · ⭐+23</summary>

##### Thông tin cơ bản

`SDK chính thức và công cụ cho nhà phát triển` · Chính thức · `official` · MIT · typesafe-ai

##### Dữ liệu

Sao **261** (+23) · Fork 14 · Issue đang mở 1 · Ngày tạo 2026-08-24 · Lần push cuối 2026-09-12 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐128 · TypeScript · official · 3 天 · ⭐+3</summary>

##### Thông tin cơ bản

`SDK chính thức và công cụ cho nhà phát triển` · Chính thức · `official` · TypeScript · MIT · typesafe-ai

##### Dữ liệu

Sao **128** (+3) · Fork 9 · Issue đang mở 6 · Ngày tạo 2026-09-04 · Lần push cuối 2026-09-15 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐121 · Python · official · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`SDK chính thức và công cụ cho nhà phát triển` · Chính thức · `official` · Python · MIT · typesafe-ai

##### Dữ liệu

Sao **121** (+2) · Fork 12 · Issue đang mở 0 · Ngày tạo 2026-08-08 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>Được tìm thấy trong mã nguồn: `README.md`, `src/system_one_adapter/__init__.py`, `src/system_one_adapter/_response.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐84 · Python · official · 0 天</summary>

##### Thông tin cơ bản

`SDK chính thức và công cụ cho nhà phát triển` · Chính thức · `official` · Python · MIT · typesafe-ai

##### Dữ liệu

Sao **84** · Fork 7 · Issue đang mở 2 · Ngày tạo 2026-09-04 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>Được tìm thấy trong mã nguồn: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 106 天</summary>

##### Thông tin cơ bản

`SDK chính thức và công cụ cho nhà phát triển` · Chính thức · `official` · HTML · typesafe-ai

##### Dữ liệu

Sao **1** · Fork 1 · Issue đang mở 1 · Ngày tạo 2024-05-28 · Lần push cuối 2026-06-04 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<a id="community-sdk"></a>

## Client, SDK và adapter do cộng đồng phát triển

Các client có kiểu cho endpoint System One, trải rộng trên bao nhiêu ngôn ngữ mà cộng đồng đã làm tới.

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐17 · Jupyter · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Jupyter · MIT · jexp

##### Dữ liệu

Sao **17** · Fork 3 · Issue đang mở 1 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐3 · Rust · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Rust · MIT · AkashPriyadarshii

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — ⭐3 · Java · observed · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Java · MIT · Premo-Cloud

##### Dữ liệu

Sao **3** (+1) · Fork 1 · Issue đang mở 2 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · TypeScript · MIT · AntonioCoppe

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Python · CC0-1.0 · MrJev

##### Dữ liệu

Sao **2** · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐2 · Elixir · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Elixir · MIT · nshkrdotcom

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · TypeScript · opaielsheikh

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Python · xingwudao

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · JavaScript · MIT · ziyu

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/gpazo/jev-vphone-cli">gpazo/jev-vphone-cli</a></b> — Swift · observed · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Swift · MIT · gpazo

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Jev from Typesafe.ai + vphone-cli

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gpazo--jev-vphone-cli/baa413a8104308f4.jpg" width="100%" alt="gpazo/jev-vphone-cli screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Ruby · MIT · javiergradiche

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/jonesmelton/verdict">jonesmelton/verdict</a></b> — OCaml · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · OCaml · MIT · jonesmelton

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

ocaml sdk for typesafe.ai's jev model

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · TypeScript · MIT · nu-sync

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/RadixILS-Dev/typesafe-sdk-go">RadixILS-Dev/typesafe-sdk-go</a></b> — Go · observed · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Go · MIT · RadixILS-Dev

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A typesafe.ai client written in golang

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `observed` · Elixir · MIT · typesend

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐164 · Shell · inferred · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Shell · NOASSERTION · realZachi

##### Dữ liệu

Sao **164** (+2) · Fork 9 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pinecone-io/cultivar">pinecone-io/cultivar</a></b> — ⭐39 · Python · inferred · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · pinecone-io

##### Dữ liệu

Sao **39** (+2) · Fork 2 · Issue đang mở 5 · Ngày tạo 2026-06-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐31 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · nidhi-singh02

##### Dữ liệu

Sao **31** (+1) · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">Xem trên img.youtube.com</a> · trình phát mở trên trang gốc; GitHub không thể nhúng trực tiếp</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/tacticocc/Jevbridge">tacticocc/Jevbridge</a></b> — ⭐17 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · tacticocc

##### Dữ liệu

Sao **17** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tacticocc--jevbridge/772995670b3e42e9.png" width="100%" alt="tacticocc/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐13 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · shiftynick

##### Dữ liệu

Sao **13** · Fork 1 · Issue đang mở 2 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐12 · Elixir · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Elixir · MIT · dannote

##### Dữ liệu

Sao **12** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐11 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · JavaScript · MIT · Ying-Kai-Liao

##### Dữ liệu

Sao **11** · Fork 3 · Issue đang mở 3 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐10 · Python · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · AboveColin

##### Dữ liệu

Sao **10** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Ask your house a question, get a number back. Home Assistant integration for TypeSafe Jev: typed answers as sensors, four actions for automations, and a conversation agent for Assist.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abovecolin--ha-jev/87fa9143f6990ef1.png" width="100%" alt="AboveColin/HA-Jev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/keltokhy/jgrep">keltokhy/jgrep</a></b> — ⭐7 · Python · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · keltokhy

##### Dữ liệu

Sao **7** (+1) · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.

</details>

<details>
<summary><b><a href="https://github.com/arunav25/jev-mcp">arunav25/jev-mcp</a></b> — ⭐5 · JavaScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · JavaScript · MIT · arunav25

##### Dữ liệu

Sao **5** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.

</details>

<details>
<summary><b><a href="https://github.com/Nasrallah-AL/jev-cli">Nasrallah-AL/jev-cli</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · Nasrallah-AL

##### Dữ liệu

Sao **5** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Command-line tool for TypeSafe's Jev AI model

</details>

<details>
<summary><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">saibimajdi/typesafeai-dotnet-sdk</a></b> — ⭐5 · C# · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · C# · MIT · saibimajdi

##### Dữ liệu

Sao **5** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/sharziki/semdecide">sharziki/semdecide</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · sharziki

##### Dữ liệu

Sao **5** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.

</details>

<details>
<summary><b><a href="https://github.com/frostney/clean-code-review">frostney/clean-code-review</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · frostney

##### Dữ liệu

Sao **4** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/frostney--clean-code-review/7d8a8de446e1c27b.png" width="100%" alt="frostney/clean-code-review screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rhighs/jev-code">rhighs/jev-code</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · rhighs

##### Dữ liệu

Sao **4** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/assets/jev-code-logo.png" width="100%" alt="rhighs/jev-code screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/docs/media/session.gif" width="100%" alt="rhighs/jev-code animation"><br><sub>bản ghi động</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/romaluev/jev-ego">romaluev/jev-ego</a></b> — ⭐4 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · NOASSERTION · romaluev

##### Dữ liệu

Sao **4** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-seo">AkashPriyadarshii/jev-seo</a></b> — ⭐3 · Rust · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Rust · AkashPriyadarshii

##### Dữ liệu

Sao **3** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One

</details>

<details>
<summary><b><a href="https://github.com/docxology/daf-jev">docxology/daf-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · docxology

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill

</details>

<details>
<summary><b><a href="https://github.com/Olti1947/jev-java">Olti1947/jev-java</a></b> — ⭐3 · Java · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Java · Olti1947

##### Dữ liệu

Sao **3** · Fork 1 · Issue đang mở 7 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Idiomatic Java SDK for TypeSafe AI Jev System One decision engine

</details>

<details>
<summary><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Butochnikov/laravel-typesafe-jev</a></b> — ⭐2 · PHP · inferred · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · PHP · MIT · Butochnikov

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes.

</details>

<details>
<summary><b><a href="https://github.com/ddfeyes/jev-mode">ddfeyes/jev-mode</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · ddfeyes

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no deps, MIT.

</details>

<details>
<summary><b><a href="https://github.com/ibrahemid/git-jev-stage">ibrahemid/git-jev-stage</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · ibrahemid

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Select Git changes for staging with a plain-language description.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Stumble/jev-go">Stumble/jev-go</a></b> — ⭐2 · Go · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Go · MIT · Stumble

##### Dữ liệu

Sao **2** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Community Go SDK for TypeSafe AI Jev / System One

</details>

<details>
<summary><b><a href="https://github.com/tontoko/jev-browser">tontoko/jev-browser</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · JavaScript · Apache-2.0 · tontoko

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 4 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.

</details>

<details>
<summary><b><a href="https://github.com/tumf/jev-cli">tumf/jev-cli</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · tumf

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Small dependency-free CLI for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/yzfly/awesome-jev-zh">yzfly/awesome-jev-zh</a></b> — ⭐2 · HTML · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · HTML · CC0-1.0 · yzfly

##### Dữ liệu

Sao **2** · Fork 3 · Issue đang mở 3 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/jevclient">AboveColin/jevclient</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · AboveColin

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-scout">AkashPriyadarshii/jev-scout</a></b> — ⭐1 · Rust · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Rust · MIT · AkashPriyadarshii

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring

</details>

<details>
<summary><b><a href="https://github.com/anilsenay/jev">anilsenay/jev</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Go · MIT · anilsenay

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Unofficial Go client for TypeSafe's System One API  and its model, Jev.

</details>

<details>
<summary><b><a href="https://github.com/burnigtm/jev-mcp">burnigtm/jev-mcp</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · burnigtm

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client

</details>

<details>
<summary><b><a href="https://github.com/felpsdev/jev-classifier">felpsdev/jev-classifier</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · felpsdev

##### Dữ liệu

Sao **1** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/felpsdev--jev-classifier/d753de26b0e6c7b6.webp" width="100%" alt="felpsdev/jev-classifier screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-go">Gaurav-Gosain/jev-go</a></b> — ⭐1 · Go · inferred · 2 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Go · MIT · Gaurav-Gosain

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/himomohi/aside-jev">himomohi/aside-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · himomohi

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.

</details>

<details>
<summary><b><a href="https://github.com/mzainzulifqar/jev-php-sdk">mzainzulifqar/jev-php-sdk</a></b> — ⭐1 · PHP · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · PHP · MIT · mzainzulifqar

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

PHP SDK for TypeSafe's Jev: send text and typed questions, get typed answers with calibrated confidence. PHP 8.1+, works with any PSR-18 client, Laravel 8–13.

</details>

<details>
<summary><b><a href="https://github.com/socai-io/jev-social">socai-io/jev-social</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · JavaScript · MIT · socai-io

##### Dữ liệu

Sao **1** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Jev-powered social media research through the socai CLI

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/socai-io--jev-social/b95803491d0f55c3.png" width="100%" alt="socai-io/jev-social screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/socai-io--jev-social/0a9e1e30f2fa0829.gif" width="100%" alt="socai-io/jev-social animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/StefanoITA/ts-jev-cost-calculator">StefanoITA/ts-jev-cost-calculator</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · StefanoITA

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe.

</details>

<details>
<summary><b><a href="https://github.com/zhirschtritt/typesafe-go">zhirschtritt/typesafe-go</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Go · MIT · zhirschtritt

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Idiomatic Go SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/33Audits/jev-auto">33Audits/jev-auto</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · JavaScript · MIT · 33Audits

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Per-turn model routing for Claude Code. Cheapest tier that can do the job, no API key required, and it calibrates itself from what actually happened.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">AkashPriyadarshii/jev-superpowers</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · JavaScript · MIT · AkashPriyadarshii

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions

</details>

<details>
<summary><b><a href="https://github.com/brnyxx/jev-ra">brnyxx/jev-ra</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · MIT · brnyxx

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 2 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7592fce4641d10.png" width="100%" alt="brnyxx/jev-ra screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7ddcd1053825a2.gif" width="100%" alt="brnyxx/jev-ra animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/david1gp/jev">david1gp/jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · david1gp

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Result-based TypeSafe System One client library and jev command-line interface.

</details>

<details>
<summary><b><a href="https://github.com/krw82/jev-playwright-mcp">krw82/jev-playwright-mcp</a></b> — TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · MIT · krw82

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.

</details>

<details>
<summary><b><a href="https://github.com/kunobi-ninja/kunobi-jev">kunobi-ninja/kunobi-jev</a></b> — Rust · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Rust · Apache-2.0 · kunobi-ninja

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Rust client for the TypeSafe System One API (Jev)

</details>

<details>
<summary><b><a href="https://github.com/lhotwll217/jev-cli">lhotwll217/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · lhotwll217

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

JSON-in, typed-decisions-out CLI for the TypeSafe System One API

</details>

<details>
<summary><b><a href="https://github.com/manojlds/jev-review">manojlds/jev-review</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · TypeScript · manojlds

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Standalone TypeSafe Jev code-review CLI: typed decisions over a local git diff.

</details>

<details>
<summary><b><a href="https://github.com/mhmdkzr/jev">mhmdkzr/jev</a></b> — Go · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Go · MIT · mhmdkzr

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

An unofficial Go client for TypeSafe's System One Jev model

</details>

<details>
<summary><b><a href="https://github.com/model-clis/jev">model-clis/jev</a></b> — Rust · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Rust · MIT · model-clis

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Typed judgment CLI for the Jev model (TypeSafe System One): state + questions in, calibrated answers and exit codes out

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing">nekowasabi/jev-routing</a></b> — Go · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Go · MIT · nekowasabi

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.

</details>

<details>
<summary><b><a href="https://github.com/okooo5km/jev">okooo5km/jev</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · Apache-2.0 · okooo5km

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed decisions from the shell: a stdlib-Python CLI and Agent Skill for TypeSafe Jev on OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch mode.

</details>

<details>
<summary><b><a href="https://github.com/phuthuycoding/jev-audit">phuthuycoding/jev-audit</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · phuthuycoding

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

AI-powered pre-commit auditor backed by TypeSafe System One (Jev) — blocks secrets, vulns & low-quality code in ~300ms. 79-case test corpus at 100% accuracy.

</details>

<details>
<summary><b><a href="https://github.com/SAGAR-TAMANG/sarvam-jev">SAGAR-TAMANG/sarvam-jev</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · SAGAR-TAMANG

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Generation-free typed decisions on Indic LLMs. An open Jev-style inference engine on sarvam-1: constrained logit readout instead of autoregressive JSON. Runs client-side in the browser.

</details>

<details>
<summary><b><a href="https://github.com/yannip1234/ask-jev">yannip1234/ask-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Python · yannip1234

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Continuous AskJev CLI checks throughout Astra work, plus the standalone AskJev skill

</details>

<details>
<summary><b><a href="https://github.com/yannip1234/codex-jev">yannip1234/codex-jev</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `inferred` · Rust · Apache-2.0 · yannip1234

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 11 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Experimental Jev compression for Codex, with a macOS menu bar launcher, desktop bridge, and native client.

</details>

<details>
<summary><b><a href="https://github.com/giuliosmall/pg_typesafe">giuliosmall/pg_typesafe</a></b> — ⭐76 · C · unverified · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `unverified` · C · MIT · giuliosmall

##### Dữ liệu

Sao **76** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification

</details>

<details>
<summary><b><a href="https://github.com/pithings/advocaat">pithings/advocaat</a></b> — ⭐74 · TypeScript · unverified · 0 天 · ⭐+4</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `unverified` · TypeScript · MIT · pithings

##### Dữ liệu

Sao **74** (+4) · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/obie/ruby_decision_model">obie/ruby_decision_model</a></b> — ⭐32 · Ruby · unverified · 0 天 · ⭐+6</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `unverified` · Ruby · MIT · obie

##### Dữ liệu

Sao **32** (+6) · Fork 2 · Issue đang mở 18 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Ruby client for decision models such as Typesafe Jev

</details>

<details>
<summary><b><a href="https://github.com/Brainwires/jevwire">Brainwires/jevwire</a></b> — ⭐5 · TypeScript · unverified · 0 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `unverified` · TypeScript · MIT · Brainwires

##### Dữ liệu

Sao **5** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/typesafe-cli">y0usaf/typesafe-cli</a></b> — ⭐4 · TypeScript · unverified · 2 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `unverified` · TypeScript · MIT · y0usaf

##### Dữ liệu

Sao **4** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose

</details>

<details>
<summary><b><a href="https://github.com/geilt/typesafe-cli">geilt/typesafe-cli</a></b> — ⭐3 · Python · unverified · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `unverified` · Python · geilt

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.

</details>

<details>
<summary><b><a href="https://github.com/gilljon/typesafe-ai-rs">gilljon/typesafe-ai-rs</a></b> — ⭐3 · Rust · unverified · 1 天</summary>

##### Thông tin cơ bản

`Client, SDK và adapter do cộng đồng phát triển` · Cộng đồng · `unverified` · Rust · MIT · gilljon

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Independent async and blocking Rust SDK for the TypeSafe AI System One API

</details>

<a id="agent-tooling"></a>

## Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã

Danh mục tăng nhanh nhất: hook, máy chủ MCP và cổng chặn đặt một quyết định có kiểu trước hành động kế tiếp của agent.

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐3196 · TypeScript · observed · 0 天 · ⭐+113</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · TypeScript · MIT · tamaratran

##### Dữ liệu

Sao **3196** (+113) · Fork 159 · Issue đang mở 44 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>Được tìm thấy trong mã nguồn: `src/request.ts`, `README.md`, `src/client.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐138 · JavaScript · inferred · 0 天 · ⭐+6</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · gargpratyush

##### Dữ liệu

Sao **138** (+6) · Fork 5 · Issue đang mở 4 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐44 · Python · inferred · 1 天 · ⭐+6</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · 0xNatoshi

##### Dữ liệu

Sao **44** (+6) · Fork 3 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐103 · observed · 1 天 · ⭐+4</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · dbreunig

##### Dữ liệu

Sao **103** (+4) · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐17 · Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · Python · MIT · GhalebDweikat

##### Dữ liệu

Sao **17** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/valentynkit/awesome-jev-typesafe">valentynkit/awesome-jev-typesafe</a></b> — ⭐8 · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · CC0-1.0 · valentynkit

##### Dữ liệu

Sao **8** · Fork 3 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Typed decisions with TypeSafe's Jev, the first System One model

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · Python · MIT · carlaiau

##### Dữ liệu

Sao **7** · Fork 1 · Issue đang mở 6 · Ngày tạo 2026-03-13 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/kraayenjon/awesome-jev">kraayenjon/awesome-jev</a></b> — ⭐4 · observed · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · NOASSERTION · kraayenjon

##### Dữ liệu

Sao **4** (+2) · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · Python · MIT · jodan-alberts

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/rajdhakad9826/routeKit">rajdhakad9826/routeKit</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · TypeScript · MIT · rajdhakad9826

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Agent-native LLM model router built with JEV by TypeSafe.ai. Dynamically selects the most suitable model based on task complexity, reasoning requirements, and tool usage.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · TypeScript · MIT · BYK

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · Python · MIT · 24601

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · TypeScript · CrowBe

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · TypeScript · MIT · gorock007

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/uipath-jev-guardrail-connector">jms-dcksn/uipath-jev-guardrail-connector</a></b> — JavaScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · JavaScript · jms-dcksn

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

UiPath bring-your-own-guardrail connector backed by the TypeSafe Jev System One model: plain-language agent policies enforced as calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/knowlet/jev-agentworld-web-simulator">knowlet/jev-agentworld-web-simulator</a></b> — TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · TypeScript · MIT · knowlet

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

An entire internet — search, pages & links — hallucinated on the fly by the System One Model.

</details>

<details>
<summary><b><a href="https://github.com/Wany-i/jev-decision-layer">Wany-i/jev-decision-layer</a></b> — Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · Python · MIT · Wany-i

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

把决策模型（typesafe/jev-1.13，经 OpenRouter 的 decisions 端点调用）封装成业务决策工具：注册表驱动，带置信度门控与硬约束。非官方项目。

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `observed` · Python · MIT · yousudip

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐267 · TypeScript · inferred · 1 天 · ⭐+4</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · devagrawal09

##### Dữ liệu

Sao **267** (+4) · Fork 13 · Issue đang mở 1 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐119 · TypeScript · inferred · 1 天 · ⭐+3</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · NiazMorshed2007

##### Dữ liệu

Sao **119** (+3) · Fork 9 · Issue đang mở 2 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐109 · JavaScript · inferred · 0 天 · ⭐+9</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · fatwang2

##### Dữ liệu

Sao **109** (+9) · Fork 12 · Issue đang mở 3 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/wy-coliney/jev-browser-use">wy-coliney/jev-browser-use</a></b> — ⭐94 · JavaScript · inferred · 0 天 · ⭐+16</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · wy-coliney

##### Dữ liệu

Sao **94** (+16) · Fork 3 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wy-coliney--jev-browser-use/581fbd89fe47c952.png" width="100%" alt="wy-coliney/jev-browser-use screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-eval-agent">vinilana/jev-eval-agent</a></b> — ⭐84 · HTML · inferred · 1 天 · ⭐+3</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · HTML · vinilana

##### Dữ liệu

Sao **84** (+3) · Fork 8 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-mcp">jkudish/jev-mcp</a></b> — ⭐73 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · jkudish

##### Dữ liệu

Sao **73** (+1) · Fork 9 · Issue đang mở 2 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools.

> An early proof of concept for exposing Jev over MCP, which is how most non-Python toolchains reach it.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/pi-jev">y0usaf/pi-jev</a></b> — ⭐67 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · y0usaf

##### Dữ liệu

Sao **67** · Fork 3 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers

</details>

<details>
<summary><b><a href="https://github.com/RomanSlack/jev-drone">RomanSlack/jev-drone</a></b> — ⭐61 · Python · inferred · 1 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · RomanSlack

##### Dữ liệu

Sao **61** (+2) · Fork 3 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/romanslack--jev-drone/b23ea2412f437970.png" width="100%" alt="RomanSlack/jev-drone screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/supercorp-ai/supercov">supercorp-ai/supercov</a></b> — ⭐33 · Rust · inferred · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Rust · MIT · supercorp-ai

##### Dữ liệu

Sao **33** (+2) · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-08-23 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Code quality and coverage for coding agents

> Code quality and coverage verdicts produced as typed decisions rather than prose, so the result can gate a pipeline directly.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/supercorp-ai--supercov/063226e150cb8a6b.jpg" width="100%" alt="supercorp-ai/supercov screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/logicrw/awesome-jev-projects">logicrw/awesome-jev-projects</a></b> — ⭐29 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · logicrw

##### Dữ liệu

Sao **29** · Fork 7 · Issue đang mở 4 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/ask-jev-skill">shantanugoel/ask-jev-skill</a></b> — ⭐29 · Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · shantanugoel

##### Dữ liệu

Sao **29** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Skill for Hermes, and other agents, to ask typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/DanRWilloughby/snifftest">DanRWilloughby/snifftest</a></b> — ⭐14 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · DanRWilloughby

##### Dữ liệu

Sao **14** (+1) · Fork 0 · Issue đang mở 3 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/TheoOliveira/pi-jev">TheoOliveira/pi-jev</a></b> — ⭐13 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · TheoOliveira

##### Dữ liệu

Sao **13** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/compozy/yoshi">compozy/yoshi</a></b> — ⭐12 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · compozy

##### Dữ liệu

Sao **12** (+1) · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/compozy--yoshi/637d8588c227f4de.png" width="100%" alt="compozy/yoshi screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">jomatsu/pi-jev-auto-mode</a></b> — ⭐11 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · jomatsu

##### Dữ liệu

Sao **11** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.

</details>

<details>
<summary><b><a href="https://github.com/tamaratran/jev-pruner">tamaratran/jev-pruner</a></b> — ⭐10 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · tamaratran

##### Dữ liệu

Sao **10** · Fork 1 · Issue đang mở 7 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Claude Code plugin: trim long Bash output with TypeSafe Jev before the model sees it

</details>

<details>
<summary><b><a href="https://github.com/blakestone-x/jev-mcp">blakestone-x/jev-mcp</a></b> — ⭐9 · Python · inferred · 2 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · blakestone-x

##### Dữ liệu

Sao **9** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer

</details>

<details>
<summary><b><a href="https://github.com/huntedman/JevLint">huntedman/JevLint</a></b> — ⭐8 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · huntedman

##### Dữ liệu

Sao **8** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.

</details>

<details>
<summary><b><a href="https://github.com/BillionsBobby/JevRouter">BillionsBobby/JevRouter</a></b> — ⭐7 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · BillionsBobby

##### Dữ liệu

Sao **7** (+2) · Fork 1 · Issue đang mở 4 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A lightweight Jev-powered router for models, tools, and subagents

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/billionsbobby--jevrouter/f0e638219505d5da.png" width="100%" alt="BillionsBobby/JevRouter screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">DECRUX9812/typesafe-skill-router</a></b> — ⭐7 · Python · inferred · 2 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · DECRUX9812

##### Dữ liệu

Sao **7** (+1) · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-code">devagrawal09/jev-code</a></b> — ⭐6 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · devagrawal09

##### Dữ liệu

Sao **6** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Bounded TypeSafe Jev workflows for coding agents.

</details>

<details>
<summary><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">GodsBoy/jev-agent-skill-router</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · GodsBoy

##### Dữ liệu

Sao **5** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed, confidence-aware agent skill routing with TypeSafe Jev.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/godsboy--jev-agent-skill-router/c80293e37dcd4faf.png" width="100%" alt="GodsBoy/jev-agent-skill-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/inanna-malick/jev-dsl">inanna-malick/jev-dsl</a></b> — ⭐5 · Haskell · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Haskell · MIT · inanna-malick

##### Dữ liệu

Sao **5** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels

</details>

<details>
<summary><b><a href="https://github.com/anpicasso/hermes-jev-approvals">anpicasso/hermes-jev-approvals</a></b> — ⭐4 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · anpicasso

##### Dữ liệu

Sao **4** · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only.

</details>

<details>
<summary><b><a href="https://github.com/GiesN/typesafe-jev-workflow">GiesN/typesafe-jev-workflow</a></b> — ⭐4 · Python · inferred · 2 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · GiesN

##### Dữ liệu

Sao **4** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/kbhuw/jev-sift">kbhuw/jev-sift</a></b> — ⭐4 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · kbhuw

##### Dữ liệu

Sao **4** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification.

</details>

<details>
<summary><b><a href="https://github.com/anandi1989/awesome-jev-usecases">anandi1989/awesome-jev-usecases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · MIT · anandi1989

##### Dữ liệu

Sao **3** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results

</details>

<details>
<summary><b><a href="https://github.com/SeeAPI/awesome-jev-use-cases">SeeAPI/awesome-jev-use-cases</a></b> — ⭐3 · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · CC-BY-4.0 · SeeAPI

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-shield">caiovicentino/jev-shield</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · caiovicentino

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check.

</details>

<details>
<summary><b><a href="https://github.com/doeixd/jev-pref">doeixd/jev-pref</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · doeixd

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-macos-loop">jcpsimmons/jev-macos-loop</a></b> — ⭐2 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · AGPL-3.0 · jcpsimmons

##### Dữ liệu

Sao **2** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Open-source macOS AI computer use and native GUI automation on Apple silicon. Jev + OmniParser CoreML + Apple Vision OCR. Bring your own OpenRouter, Vercel AI Gateway, or TypesafeAI token.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jcpsimmons--jev-macos-loop/19bcb6c0f1788073.gif" width="100%" alt="jcpsimmons/jev-macos-loop screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jcpsimmons--jev-macos-loop/c99113da6464b245.gif" width="100%" alt="jcpsimmons/jev-macos-loop animation"><br><sub>bản ghi động · <a href="https://raw.githubusercontent.com/jcpsimmons/jev-macos-loop/master/docs/media/jev-finder-batch-demo.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-model-router-demo">jcpsimmons/jev-model-router-demo</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · jcpsimmons

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

</details>

<details>
<summary><b><a href="https://github.com/matthewp/flue-jev-demo">matthewp/flue-jev-demo</a></b> — ⭐2 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · matthewp

##### Dữ liệu

Sao **2** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Flue agent routing with TypeSafe Jev through Cloudflare AI Gateway

</details>

<details>
<summary><b><a href="https://github.com/molis-ai/jev-workbench">molis-ai/jev-workbench</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · molis-ai

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/molis-ai--jev-workbench/00f61d8403a941cd.png" width="100%" alt="molis-ai/jev-workbench screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MongLong0214/jev-gate">MongLong0214/jev-gate</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MongLong0214

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 5 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.

</details>

<details>
<summary><b><a href="https://github.com/morcoan/JevSeek">morcoan/JevSeek</a></b> — ⭐2 · Python · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · morcoan

##### Dữ liệu

Sao **2** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools, persistent sessions, React desktop, and documented research.

</details>

<details>
<summary><b><a href="https://github.com/ranjan2829/AskJev">ranjan2829/AskJev</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · ranjan2829

##### Dữ liệu

Sao **2** · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-mcp">rashedInt32/jev-mcp</a></b> — ⭐2 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · rashedInt32

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/samtay32/jev-system-architect">samtay32/jev-system-architect</a></b> — ⭐2 · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · MIT · samtay32

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives.

</details>

<details>
<summary><b><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher">abhishekashokvkumar/jev-mcp-dispatcher</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · abhishekashokvkumar

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Natural-language MCP tool dispatcher powered entirely by TypeSafe's Jev — no general-purpose LLM. Discovers a simple MCP server's tool signatures at runtime and uses Jev's typed primitives (Choice/Noul) to pick the right tool and extract its arguments straight out of the sentence.

</details>

<details>
<summary><b><a href="https://github.com/bestagentkits/jev-skillful">bestagentkits/jev-skillful</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · bestagentkits

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.

</details>

<details>
<summary><b><a href="https://github.com/Dharundp6/jev-carryforward">Dharundp6/jev-carryforward</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · Dharundp6

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written as things happen, recalled per task with TypeSafe's Jev evaluation model via Vercel AI Gateway.

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-starter">hamakyo/jev-starter</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · hamakyo

##### Dữ liệu

Sao **1** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-codex-plugin">integrate-your-mind/jev-codex-plugin</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · integrate-your-mind

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Open-source Codex plugin for TypeSafe Jev decision consultation, failure diagnosis, and evidence-based completion review

</details>

<details>
<summary><b><a href="https://github.com/khordoo/jev-reflex-autonomy-lab">khordoo/jev-reflex-autonomy-lab</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · khordoo

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/khordoo/jev-reflex-autonomy-lab/main/docs/media/reflex-dashboard.png" width="100%" alt="khordoo/jev-reflex-autonomy-lab screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/noetion/dsh-jev">noetion/dsh-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · noetion

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.

</details>

<details>
<summary><b><a href="https://github.com/omni-/ask-jev">omni-/ask-jev</a></b> — ⭐1 · PowerShell · inferred · 2 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · PowerShell · MIT · omni-

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions.

</details>

<details>
<summary><b><a href="https://github.com/poponline63/hermes-jev-north-star">poponline63/hermes-jev-north-star</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · poponline63

##### Dữ liệu

Sao **1** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven.

</details>

<details>
<summary><b><a href="https://github.com/RahulBalakavi/claude-code-jev">RahulBalakavi/claude-code-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · RahulBalakavi

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Experimental Jev permission gate for Claude Code via OpenRouter, with reproducible latency and cost benchmarks

</details>

<details>
<summary><b><a href="https://github.com/Ravinder82/jev-flash-router">Ravinder82/jev-flash-router</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · Ravinder82

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code

</details>

<details>
<summary><b><a href="https://github.com/rthomas24/jev-realtime-trading">rthomas24/jev-realtime-trading</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · rthomas24

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rthomas24--jev-realtime-trading/f27df5cca6b8e2cf.png" width="100%" alt="rthomas24/jev-realtime-trading screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Saik0s/diffusiongemma-jev-macos">Saik0s/diffusiongemma-jev-macos</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · Saik0s

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Local JEV-style decisions with DiffusionGemma on Apple Silicon, with benchmarks and coding-agent examples.

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/codex-jev-compaction">Wang-auspicious/codex-jev-compaction</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · Wang-auspicious

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills.

</details>

<details>
<summary><b><a href="https://github.com/ably-labs/jev-pong">ably-labs/jev-pong</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · Apache-2.0 · ably-labs

##### Dữ liệu

Sao **0** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Pong where the ball moves one step per model decision. Jev vs LLMs via Vercel AI Gateway, every player and agent on an Ably channel.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b51a044f9d543ef0.png" width="100%" alt="ably-labs/jev-pong screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b5b9b482a58f2c01.gif" width="100%" alt="ably-labs/jev-pong animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/altregubov/jev-antigravity-mcp">altregubov/jev-antigravity-mcp</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · altregubov

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/alviso/jev-precheck">alviso/jev-precheck</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · alviso

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A second signature on every write an AI agent makes into a system of record. MCP proxy: fetch the records, derive in code, Jev judges. 98.6% recall, 0 false holds on 288 cases.

</details>

<details>
<summary><b><a href="https://github.com/andyholst/hermes-typesafe-jev">andyholst/hermes-typesafe-jev</a></b> — inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · andyholst

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-19 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

TypeSafe Jev MCP server for Hermes Agent — Choice, Noul, Score as first-class tools

</details>

<details>
<summary><b><a href="https://github.com/anisselbd/jev-phishing-bench">anisselbd/jev-phishing-bench</a></b> — Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · anisselbd

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/openclaw-jev-harness">AntonioCoppe/openclaw-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · AntonioCoppe

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

OpenClaw plugin: jev-harness DecisionHarness as System One decide layer (policy/confidence/shadow)

</details>

<details>
<summary><b><a href="https://github.com/AStheTECH/mewcp-jev">AStheTECH/mewcp-jev</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · Apache-2.0 · AStheTECH

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

JEV MCP server by MewCP

</details>

<details>
<summary><b><a href="https://github.com/cbruyndoncx/AskJev-MCP">cbruyndoncx/AskJev-MCP</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · cbruyndoncx

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence

</details>

<details>
<summary><b><a href="https://github.com/CrowdLinker/JevPromptCoach">CrowdLinker/JevPromptCoach</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · CrowdLinker

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Claude Code plugin that scores how well you prompt a coding agent, and shows whether your habits are improving. Runs on TypeSafe's Jev model. Zero added latency.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/crowdlinker--jevpromptcoach/5340815130cd47ba.png" width="100%" alt="CrowdLinker/JevPromptCoach screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/de-niji/jev-hermes">de-niji/jev-hermes</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · de-niji

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Jev for Hermes: cheap intent gates + verbatim tool compaction on OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/dizk/pi-jev-lens">dizk/pi-jev-lens</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · dizk

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

pi extension that compresses large tool results before they reach the model: jev picks the view, full text stays recallable

</details>

<details>
<summary><b><a href="https://github.com/DoGMaTiiC/hermes-jev">DoGMaTiiC/hermes-jev</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · DoGMaTiiC

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 7 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only.

</details>

<details>
<summary><b><a href="https://github.com/duketopceo/jev-compact">duketopceo/jev-compact</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · duketopceo

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP

</details>

<details>
<summary><b><a href="https://github.com/EtienneLescot/jev-router">EtienneLescot/jev-router</a></b> — HTML · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · HTML · MIT · EtienneLescot

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model tier and reasoning depth.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/etiennelescot--jev-router/96217fad0b128b3e.png" width="100%" alt="EtienneLescot/jev-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fast-facts/jev-mcp">fast-facts/jev-mcp</a></b> — Go · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Go · MIT · fast-facts

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/flaviomartil/herdr-jev">flaviomartil/herdr-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · flaviomartil

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Jev-driven multi-model triage and Triad orchestration plugin for Herdr and AI-Harness

</details>

<details>
<summary><b><a href="https://github.com/flaviusapop/jev-router">flaviusapop/jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · flaviusapop

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Routes each turn in Claude Code, Codex, Grok and opencode to the cheapest model and reasoning depth that can finish it, using TypeSafe Jev

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/flaviusapop--jev-router/b7f868696d35b78b.png" width="100%" alt="flaviusapop/jev-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Friedjof/jev-mobile">Friedjof/jev-mobile</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · Friedjof

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Fast structured Android control loops with TypeSafe Jev and Mobile MCP

</details>

<details>
<summary><b><a href="https://github.com/gzawadzki/jev-usecases">gzawadzki/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · gzawadzki

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage

</details>

<details>
<summary><b><a href="https://github.com/hangarbay/jev.mcp">hangarbay/jev.mcp</a></b> — Go · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Go · MIT · hangarbay

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/its-panzer/jev-model-router">its-panzer/jev-model-router</a></b> — Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · its-panzer

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A policy router that picks the cheapest Claude model that can finish the job

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/its-panzer--jev-model-router/98819f5aaf8e6373.png" width="100%" alt="its-panzer/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jmanhype/jev-dspy-lab">jmanhype/jev-dspy-lab</a></b> — Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · jmanhype

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/jev-pii-guardrail">jms-dcksn/jev-pii-guardrail</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · jms-dcksn

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A UiPath coded agent with a custom PII detection guardrail on the LLM boundary, built on the TypeSafe Jev model as a LangChain awrap_model_call middleware.

</details>

<details>
<summary><b><a href="https://github.com/JoacoMarc/jev-harness-router">JoacoMarc/jev-harness-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · JoacoMarc

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Per-turn harness router on Jev (TypeSafe): one batched call picks the model tier, tools, skill and effort budget for an agent turn, behind a hard latency deadline.

</details>

<details>
<summary><b><a href="https://github.com/juanlentino/jev-connector">juanlentino/jev-connector</a></b> — PHP · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · PHP · GPL-2.0 · juanlentino

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

WordPress connector for the TypeSafe System One API (Jev): typed questions, confidence-scored answers, core Connectors API key management

</details>

<details>
<summary><b><a href="https://github.com/kaijia323/dsh-plugin-jev">kaijia323/dsh-plugin-jev</a></b> — HTML · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · HTML · MIT · kaijia323

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/Korbeil/opencode-jev-plugin">Korbeil/opencode-jev-plugin</a></b> — inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Korbeil

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/madeye/pi-jev">madeye/pi-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · madeye

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Jev-assisted file retrieval and request caching for faster Pi workflows

</details>

<details>
<summary><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">MahmoudAdelbghany/jev-browser</a></b> — JavaScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MahmoudAdelbghany

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included.

</details>

<details>
<summary><b><a href="https://github.com/Mandrilsquad1441/jev-model-router">Mandrilsquad1441/jev-model-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · Mandrilsquad1441

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Pick the best AI model and reasoning effort for any task in ~1s. Plugin for Claude Code, Claude Desktop and Codex, powered by TypeSafe's Jev decision model and live OpenRouter pricing. Balance intelligence, speed and cost, or choose your priority.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mandrilsquad1441--jev-model-router/6187e7fb04b04c08.png" width="100%" alt="Mandrilsquad1441/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/marcAllari/jev-mcp-router">marcAllari/jev-mcp-router</a></b> — inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · marcAllari

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/micic-mihajlo/jev-tool-runner">micic-mihajlo/jev-tool-runner</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · micic-mihajlo

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/minhgv/jev-mcp">minhgv/jev-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · minhgv

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe Jev MCP decision layer for coding agents and CI

</details>

<details>
<summary><b><a href="https://github.com/MSalvalaggio/jev-reflex">MSalvalaggio/jev-reflex</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · MSalvalaggio

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision).

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-mcp">nekowasabi/jev-routing-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · nekowasabi

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/Nyarlathoteppppp/pi-jev-context">Nyarlathoteppppp/pi-jev-context</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · Nyarlathoteppppp

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Cache-neutral context trimming for the pi coding agent, powered by TypeSafe Jev: long tool output cut to verbatim key lines before it enters context, with lossless recall. Measured, with pre-registered benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Panebianco00/jev-claude">Panebianco00/jev-claude</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · Panebianco00

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Route Claude Code's coding decisions through TypeSafe Jev: typed choices with probabilities, enforced at plan approval, questions, and risky commands.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-mcp-router">Pinutss/jev-mcp-router</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · Pinutss

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Select relevant MCP tools under a context-token budget, without executing them.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-mcp-router/3947a2a5cc3750c8.png" width="100%" alt="Pinutss/jev-mcp-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-memory-selector">Pinutss/jev-memory-selector</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · Pinutss

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-plugins">Pinutss/jev-plugins</a></b> — inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · MIT · Pinutss

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Cursor and Hermes marketplace for the four published JEV Labs routers.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-plugins/b3fcd72ac9e61f49.jpg" width="100%" alt="Pinutss/jev-plugins screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/raj8525/universal-jev">raj8525/universal-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · raj8525

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents

</details>

<details>
<summary><b><a href="https://github.com/riposta/pi-jev">riposta/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · riposta

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

a Jev classification layer for the Pi coding agent

</details>

<details>
<summary><b><a href="https://github.com/robbyczgw-cla/hermes-plugin-jev">robbyczgw-cla/hermes-plugin-jev</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · robbyczgw-cla

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

TypeSafe/Jev decision signals for Hermes: turn classification, conservative tool shaping, approvals, and coding verification.

</details>

<details>
<summary><b><a href="https://github.com/rubichandrap/hermes-jev-guard">rubichandrap/hermes-jev-guard</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · rubichandrap

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check

</details>

<details>
<summary><b><a href="https://github.com/sebastianbugal/jev">sebastianbugal/jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · sebastianbugal

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

TypeSafe's Jev decision model in Claude Code. Ask in plain language, get a typed answer with a calibrated probability.

</details>

<details>
<summary><b><a href="https://github.com/sypherin/jev-trace-classifier">sypherin/jev-trace-classifier</a></b> — Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · sypherin

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next

</details>

<details>
<summary><b><a href="https://github.com/tgiridhar/claude-code-jev-smart-router">tgiridhar/claude-code-jev-smart-router</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · tgiridhar

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task phase and the cost of an undetected error, gated by prompt-cache arithmetic. Proof of concept.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tgiridhar--claude-code-jev-smart-router/28b9e1b2a005c7e2.png" width="100%" alt="tgiridhar/claude-code-jev-smart-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/themsquared/jev-benchmark">themsquared/jev-benchmark</a></b> — Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · Apache-2.0 · themsquared

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.

</details>

<details>
<summary><b><a href="https://github.com/thevibeworks/awesome-typesafe-jev">thevibeworks/awesome-typesafe-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · NOASSERTION · thevibeworks

##### Dữ liệu

Sao **0** · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/thumay9700/jev-plays">thumay9700/jev-plays</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · thumay9700

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Autonomous game agent powered by TypeSafe AI's Jev (System One decision engine), starting with Pokémon Red.

</details>

<details>
<summary><b><a href="https://github.com/trietphan/jev-claw">trietphan/jev-claw</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · trietphan

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Typed model routing for OpenClaw agents, powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/ussyverse/hermes-jev-router">ussyverse/hermes-jev-router</a></b> — Python · inferred · 2 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · MIT · ussyverse

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-gateway-bench">vinilana/jev-gateway-bench</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · MIT · vinilana

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Benchmark for jev-gateway: real coding agents on chess engine tasks, with Jev routing on and off

</details>

<details>
<summary><b><a href="https://github.com/wotai-dev/typesafe-jev-tools">wotai-dev/typesafe-jev-tools</a></b> — Shell · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Shell · MIT · wotai-dev

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 149-row comparison of TypeSafe Jev against Claude Haiku 4.5.

</details>

<details>
<summary><b><a href="https://github.com/yangzhou-chaofan/awesome-jev-prompt">yangzhou-chaofan/awesome-jev-prompt</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · JavaScript · CC0-1.0 · yangzhou-chaofan

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

latest top 100 showcases for jev (keep updating) from x / github / latest sources

</details>

<details>
<summary><b><a href="https://github.com/Zaious/jev-capability-atlas">Zaious/jev-capability-atlas</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · Python · NOASSERTION · Zaious

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。

</details>

<details>
<summary><b><a href="https://github.com/zhangxaochen/dsh-jev">zhangxaochen/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `inferred` · TypeScript · MIT · zhangxaochen

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev (System One decision model) plugin suite for DeepSeek Harness (dsh)

</details>

<details>
<summary><b><a href="https://github.com/DevMortimer/pi-warden">DevMortimer/pi-warden</a></b> — ⭐63 · TypeScript · unverified · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `unverified` · TypeScript · MIT · DevMortimer

##### Dữ liệu

Sao **63** (+1) · Fork 5 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop

> Guardrails that steer an agent before it acts. Demonstrates the gate pattern, where the decision is cheap enough to run on every step.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devmortimer--pi-warden/b8dc20ac6694613a.png" width="100%" alt="DevMortimer/pi-warden screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/3clyp50/a0-typesafe-ai">3clyp50/a0-typesafe-ai</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `unverified` · Python · MIT · 3clyp50

##### Dữ liệu

Sao **4** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/3clyp50--a0-typesafe-ai/9aa8ea4ef8241f14.png" width="100%" alt="3clyp50/a0-typesafe-ai screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/zoidsh/tenet">zoidsh/tenet</a></b> — ⭐4 · Go · unverified · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `unverified` · Go · MIT · zoidsh

##### Dữ liệu

Sao **4** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

The review gate for code that agents write: rules in plain language, judged on every commit

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/pi-quiet-ask">HyunjunJeon/pi-quiet-ask</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Thông tin cơ bản

`Công cụ cho agent: MCP, hook, cổng chặn và agent viết mã` · Cộng đồng · `unverified` · TypeScript · MIT · HyunjunJeon

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe Jev as the pi coding agent's quiet decision layer

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hyunjunjeon--pi-quiet-ask/7ee3a99430e853d8.png" width="100%" alt="HyunjunJeon/pi-quiet-ask screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<a id="routing-guardrails"></a>

## Định tuyến, rào chắn và phê duyệt

Trường hợp dùng mang dáng dấp sản xuất — gửi mỗi yêu cầu tới mô hình rẻ nhất thực sự xử lý được, và giữ một phép kiểm tra tất định trên kết quả.

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐48 · Rust · observed · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `observed` · Rust · NOASSERTION · Dicklesworthstone

##### Dữ liệu

Sao **48** (+1) · Fork 4 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 2 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `observed` · Python · MIT · Foadsf

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `observed` · TypeScript · MIT · qddegtya

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 3 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed decisions from a System One model. An uncertain answer is a different type from a confident one — and the compiler makes you handle it.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `observed` · Python · aniruddh-krovvidi

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/chy4pro/JevBrowserExt">chy4pro/JevBrowserExt</a></b> — TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `observed` · TypeScript · MIT · chy4pro

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

⚡ Ultrafast browser automation Chrome Extension (Manifest V3) powered by TypeSafe Jev (TypeSafe.ai, OpenRouter, Cloudflare)

</details>

<details>
<summary><b><a href="https://github.com/lorensation/llm-cost-optimizer-jev">lorensation/llm-cost-optimizer-jev</a></b> — observed · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `observed` · Apache-2.0 · lorensation

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

An intelligent routing layer powered by TypeSafe AI's System One model Jev that sits in front of multiple LLM providers, analyzes each incoming request’s complexity, routes it to the cheapest model capable of handling it at acceptable quality, and continuously validates that routing decisions are correct.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐26 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · brainstormity

##### Dữ liệu

Sao **26** · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐26 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · MIT · yusukebe

##### Dữ liệu

Sao **26** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐6 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · JavaScript · MIT · mejiasd3v

##### Dữ liệu

Sao **6** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · andrelandgraf

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · MIT · keeltrace

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/sysadarsh/zerosweep">sysadarsh/zerosweep</a></b> — ⭐3 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · sysadarsh

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Autonomous System-One Triage Engine & Benchmark powered by TypeSafe AI (Jev). 75ms inference, $0 output tokens, and RLCD epistemic safety gates.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-gateway">vinilana/jev-gateway</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · MIT · vinilana

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · MIT · maker-KK

##### Dữ liệu

Sao **2** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · MIT · prismhq

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/vtrivedy/jev-plays-games">vtrivedy/jev-plays-games</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · JavaScript · vtrivedy

##### Dữ liệu

Sao **2** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Chess, Connect Four, and a decision model. Play Jev or watch Jev play itself.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/vtrivedy/jev-plays-games/main/docs/screenshots/chess.jpg" width="100%" alt="vtrivedy/jev-plays-games screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · MIT · WiktorB2004

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · MIT · Pinutss

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Shashank-H

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Jupyter · MIT · bitnovus

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/buyukcerci/jev-model-router">buyukcerci/jev-model-router</a></b> — inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Apache-2.0 · buyukcerci

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A multi-provider LLM and media router featuring calibrated confidence classification, dynamic policy scoring, and automated fallback management.

</details>

<details>
<summary><b><a href="https://github.com/carllippert/jev-router">carllippert/jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · MIT · carllippert

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Express with no routes. TypeSafe Jev picks which handler runs.

</details>

<details>
<summary><b><a href="https://github.com/danielhirt/jev-lab">danielhirt/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · danielhirt

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison

</details>

<details>
<summary><b><a href="https://github.com/gnoviawan/omp-jev-tools">gnoviawan/omp-jev-tools</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · NOASSERTION · gnoviawan

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation verification

</details>

<details>
<summary><b><a href="https://github.com/hugo-alves/jev-router-playground">hugo-alves/jev-router-playground</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · JavaScript · MIT · hugo-alves

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Interactive playground for testing Jev model-routing decisions against OpenRouter models

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hugo-alves--jev-router-playground/93692a5f183f12e1.jpg" width="100%" alt="hugo-alves/jev-router-playground screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iefnaf/pi-jev">iefnaf/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · MIT · iefnaf

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Pi extension suite powered by Jev: selective context compaction and model routing

</details>

<details>
<summary><b><a href="https://github.com/jolehuit/jev-downloads-sorter">jolehuit/jev-downloads-sorter</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · MIT · jolehuit

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A ~/Downloads folder that sorts itself: one Jev decision per file, launchd WatchPaths, no daemon

</details>

<details>
<summary><b><a href="https://github.com/kenhuangus/jev-usecases">kenhuangus/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · MIT · kenhuangus

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kenhuangus--jev-usecases/be919255190f6495.png" width="100%" alt="kenhuangus/jev-usecases screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-bot">kevin9327/jev-bot</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · MIT · kevin9327

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.

</details>

<details>
<summary><b><a href="https://github.com/LightningK0ala/jev-marshal">LightningK0ala/jev-marshal</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · MIT · LightningK0ala

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Semantic PR policy checks powered by Jev.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/lightningk0ala--jev-marshal/e47e7ce8f0057d1f.png" width="100%" alt="LightningK0ala/jev-marshal screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Loule95450/jev-free-router">Loule95450/jev-free-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · JavaScript · MIT · Loule95450

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Dynamic per-turn model router on free OpenCode Zen + Go models (fork of gargpratyush/jev-router)

</details>

<details>
<summary><b><a href="https://github.com/makefinks/jev-feed-filter">makefinks/jev-feed-filter</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · MIT · makefinks

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Smart, dynamic AI filtering for X and YouTube feeds using Jev

</details>

<details>
<summary><b><a href="https://github.com/mcgalleg/grokbot-jev-jobs">mcgalleg/grokbot-jev-jobs</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · mcgalleg

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Scores public job postings against my resume using TypeSafe's jev via the Vercel AI Gateway. Daily Vercel cron.

</details>

<details>
<summary><b><a href="https://github.com/MoonTory/pi-jev-harness">MoonTory/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · MoonTory

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards tool calls

</details>

<details>
<summary><b><a href="https://github.com/perixtar/jev-e2e">perixtar/jev-e2e</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · MIT · perixtar

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Natural-language end-to-end tests for web apps, powered by Jev and Playwright.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>không công bố media</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/perixtar--jev-e2e/81a240435b11d6f2.gif" width="100%" alt="perixtar/jev-e2e animation"><br><sub>bản ghi động · <a href="https://raw.githubusercontent.com/perixtar/jev-e2e/main/docs/assets/ebay-benchmark.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rajivkuriakose/typesafe-jev-examples">rajivkuriakose/typesafe-jev-examples</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · MIT · rajivkuriakose

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/SadiqOnGithub/jev-lab">SadiqOnGithub/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · TypeScript · SadiqOnGithub

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API

</details>

<details>
<summary><b><a href="https://github.com/TokenTrim/jev-routing-experiment">TokenTrim/jev-routing-experiment</a></b> — Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · Apache-2.0 · TokenTrim

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tokentrim--jev-routing-experiment/1c31bd606ebc1994.png" width="100%" alt="TokenTrim/jev-routing-experiment screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ufec/jev-block-android-ad">ufec/jev-block-android-ad</a></b> — Kotlin · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Kotlin · MIT · ufec

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

JevNoiseGate filters unwanted notifications and SMS on Android. Rather than   matching keywords, an LLM decides what's noise — and only what it explicitly   flags is blocked. Verification codes are matched on-device and never uploaded;   anything uncertain passes through.

</details>

<details>
<summary><b><a href="https://github.com/viniciosrab/pi-jev-router">viniciosrab/pi-jev-router</a></b> — inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · viniciosrab

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-19 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/wadadanet/faq-jev-router">wadadanet/faq-jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · JavaScript · MIT · wadadanet

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Cascade FAQ routing with TypeSafe Jev — category → FAQ or not found (GitHub Pages demo)

</details>

<details>
<summary><b><a href="https://github.com/Zumka1991/jev-telegram-admin">Zumka1991/jev-telegram-admin</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `inferred` · Python · Zumka1991

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

AI moderator for Telegram groups powered by the Jev (TypeSafe System One) decision model

</details>

<details>
<summary><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">iammrduncan/typesafe-ai-benchmark</a></b> — ⭐32 · TypeScript · unverified · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `unverified` · TypeScript · MIT · iammrduncan

##### Dữ liệu

Sao **32** · Fork 5 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.

> A gateway that mimics the System One interface, which is what makes side-by-side benchmarking possible without rewriting the caller.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>không công bố media</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/80d6baf37faa23fb.gif" width="100%" alt="iammrduncan/typesafe-ai-benchmark animation"><br><sub>bản ghi động · <a href="https://raw.githubusercontent.com/iammrduncan/typesafe-ai-benchmark/main/docs/media/theater-demo.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kavehmz/typesafe-playground">kavehmz/typesafe-playground</a></b> — ⭐9 · JavaScript · unverified · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `unverified` · JavaScript · kavehmz

##### Dữ liệu

Sao **9** (+1) · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/kavehmz/typesafe-playground/main/docs/images/demo03-fable.png" width="100%" alt="kavehmz/typesafe-playground screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/raihankhan-rk/diffjury">raihankhan-rk/diffjury</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### Thông tin cơ bản

`Định tuyến, rào chắn và phê duyệt` · Cộng đồng · `unverified` · TypeScript · raihankhan-rk

##### Dữ liệu

Sao **3** · Fork 1 · Issue đang mở 2 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

DiffJury — TypeSafe Jev PR risk router + code review coach

</details>

<a id="evaluation"></a>

## Đánh giá, hiệu chỉnh và benchmark

Làm sao biết các quyết định là tốt? Hiệu chỉnh là câu hỏi mở trong hệ sinh thái này, và đây là những dự án đang đo lường nó.

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐4 · Python · observed · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `observed` · Python · Apache-2.0 · ikermoel

##### Dữ liệu

Sao **4** (+1) · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Open-source alternative to TypeSafe's Jev: a System One style model layer that gives typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with honest benchmarks

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/edgardcham/huncho">edgardcham/huncho</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `observed` · TypeScript · MIT · edgardcham

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Decisions as code on System One models: typed questions, thresholds with hysteresis, nested decisions, journal, calibration

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `observed` · Go · MIT · Gaurav-Gosain

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — ⭐1 · Python · observed · 1 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `observed` · Python · Apache-2.0 · hev

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `observed` · Python · akash-kamat

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/nishioka-shinji/jev-edgar">nishioka-shinji/jev-edgar</a></b> — Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `observed` · Python · nishioka-shinji

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Does Jev, a System One model returning calibrated probabilities, say anything useful about an earnings release before the market prices it?

</details>

<details>
<summary><b><a href="https://github.com/JoshuaSP/open-jev">JoshuaSP/open-jev</a></b> — ⭐14 · Python · inferred · 2 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · MIT · JoshuaSP

##### Dữ liệu

Sao **14** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed JSON inference with DiffusionGemma, with Every and Jev benchmark results

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/joshuasp--open-jev/1d4a9f6368358e43.png" width="100%" alt="JoshuaSP/open-jev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐8 · Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · Apache-2.0 · AbdelStark

##### Dữ liệu

Sao **8** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐6 · Python · inferred · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · NOASSERTION · Heman10x-NGU

##### Dữ liệu

Sao **6** (+2) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/abhixhek/jevcal">abhixhek/jevcal</a></b> — ⭐5 · Python · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · MIT · abhixhek

##### Dữ liệu

Sao **5** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abhixhek--jevcal/3dbe2307176737c8.png" width="100%" alt="abhixhek/jevcal screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐5 · TypeScript · inferred · 2 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · TypeScript · MIT · y0usaf

##### Dữ liệu

Sao **5** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/cablehead/jev.nu">cablehead/jev.nu</a></b> — ⭐2 · Nushell · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Nushell · MIT · cablehead

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nushell module for the TypeSafe System One API: typed decisions with calibrated probabilities

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 2 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · MIT · wondertwins

##### Dữ liệu

Sao **2** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rongxinzy/LightJev">rongxinzy/LightJev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · Apache-2.0 · rongxinzy

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Train lightweight language backbones for typed decisions and candidate probabilities. CE/Brier training, evaluation, and an offline end-to-end demo.

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · 4esv

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

</details>

<details>
<summary><b><a href="https://github.com/carson-sweet/jev-plays-brogue">carson-sweet/jev-plays-brogue</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · TypeScript · AGPL-3.0 · carson-sweet

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

TypeSafe's Jev model plays the roguelike Brogue live -- a hand-built expert system for System-2 reasoning, outcome-calibrated self-learning, and a web UI to watch decisions, costs, and training progress.

</details>

<details>
<summary><b><a href="https://github.com/danielgshea/jev-as-a-judge">danielgshea/jev-as-a-judge</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · danielgshea

##### Dữ liệu

Sao **0** · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Using Jev as an evaluator.

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · TypeScript · MIT · Danu28

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · TeX · NOASSERTION · dnakhoa

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · eggmasonvalue

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/ickma2311/jev-baselines-eval">ickma2311/jev-baselines-eval</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · MIT · ickma2311

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Pre-registered independent eval of TypeSafe Jev against a nano-class LLM, a frontier LLM, and a supervised encoder (Banking77 + CLINC150 zero-shot)

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ickma2311--jev-baselines-eval/4cef768bc4898704.png" width="100%" alt="ickma2311/jev-baselines-eval screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · MIT · jujumilk3

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · JavaScript · MIT · KantaHayashiAI

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/KiishiAD/jev-loan-identity-benchmark">KiishiAD/jev-loan-identity-benchmark</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · KiishiAD

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Reproducible synthetic benchmark for temporal loan identity resolution with TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/laurentfabre/databricks-jev-pdf-lab">laurentfabre/databricks-jev-pdf-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · laurentfabre

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Precision PDF extraction research: Databricks + Jev, synthetic tests, selective parsing, measured tradeoffs and negative results.

</details>

<details>
<summary><b><a href="https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and">musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and</a></b> — HTML · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · HTML · MIT · musman550

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>không công bố media</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@automatewithmusfiraai"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@automatewithmusfiraai">Xem trên youtube.com</a> · trình phát mở trên trang gốc; GitHub không thể nhúng trực tiếp</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/onlyoneaman/jev-eval">onlyoneaman/jev-eval</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · TypeScript · MIT · onlyoneaman

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/onlyoneaman--jev-eval/e5d471e96e134f81.png" width="100%" alt="onlyoneaman/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rorshopping/jev-browser-local">rorshopping/jev-browser-local</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · NOASSERTION · rorshopping

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Run jev-browser on a fully local JEV-style decision engine (no cloud API). Warm-browser fork, VRAM guard, measured benchmarks, run traces.

</details>

<details>
<summary><b><a href="https://github.com/SHAKULMITTAL22/jev-resume">SHAKULMITTAL22/jev-resume</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · AGPL-3.0 · SHAKULMITTAL22

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Folio: job-specific resume leaderboards with approved rubrics, evidence-backed AI evaluation, and human hiring decisions.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shakulmittal22--jev-resume/e653593f3a00df9d.png" width="100%" alt="SHAKULMITTAL22/jev-resume screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shunta-furukawa/jev-tick-lab">shunta-furukawa/jev-tick-lab</a></b> — inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · shunta-furukawa

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis.

</details>

<details>
<summary><b><a href="https://github.com/simonmesmith/jev-banking77-experiment">simonmesmith/jev-banking77-experiment</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · simonmesmith

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Jev on BANKING77: reproducible classification evaluation, published BERT comparison, costs and latency.

</details>

<details>
<summary><b><a href="https://github.com/teyhouse/jev-secret-detection">teyhouse/jev-secret-detection</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · teyhouse

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" width="100%" alt="teyhouse/jev-secret-detection screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/us/jev-local">us/jev-local</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `inferred` · Python · us

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Local Jev-compatible evaluation server: POST /v1/systemone with typed noul/choice/score, open weights, no waitlist

</details>

<details>
<summary><b><a href="https://github.com/kyotofin/tax-doc-classifier">kyotofin/tax-doc-classifier</a></b> — ⭐113 · TypeScript · unverified · 0 天 · ⭐+19</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `unverified` · TypeScript · Apache-2.0 · kyotofin

##### Dữ liệu

Sao **113** (+19) · Fork 10 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.

</details>

<details>
<summary><b><a href="https://github.com/Mapika/decider">Mapika/decider</a></b> — ⭐25 · Python · unverified · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `unverified` · Python · Apache-2.0 · Mapika

##### Dữ liệu

Sao **25** · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>không công bố media</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mapika--decider/c67d355f22dcb51a.gif" width="100%" alt="Mapika/decider animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/genai-craft/openvons">genai-craft/openvons</a></b> — ⭐7 · Python · unverified · 0 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `unverified` · Python · NOASSERTION · genai-craft

##### Dữ liệu

Sao **7** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド

</details>

<details>
<summary><b><a href="https://github.com/aabolfazl/typesafe-local">aabolfazl/typesafe-local</a></b> — ⭐6 · Python · unverified · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `unverified` · Python · MIT · aabolfazl

##### Dữ liệu

Sao **6** (+1) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/aabolfazl--typesafe-local/ada59cf382af5143.png" width="100%" alt="aabolfazl/typesafe-local screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mithalouni/system-one-open">mithalouni/system-one-open</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### Thông tin cơ bản

`Đánh giá, hiệu chỉnh và benchmark` · Cộng đồng · `unverified` · Python · NOASSERTION · mithalouni

##### Dữ liệu

Sao **4** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal)

</details>

<a id="research-models"></a>

## Bản tái tạo mở, trọng số và nghiên cứu kiến trúc

Trọng số mở, bản sao nhỏ và công trình kiến trúc. Một số dự án tồn tại vì hành vi hiệu chỉnh không thể tái tạo chỉ từ tài liệu công khai.

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐62 · Python · observed · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `observed` · Python · MIT · kshetrajna12

##### Dữ liệu

Sao **62** (+1) · Fork 4 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐370 · Python · inferred · 1 天 · ⭐+16</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · MIT · TianyuCodings

##### Dữ liệu

Sao **370** (+16) · Fork 33 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/5055af419619e7e4.gif" width="100%" alt="TianyuCodings/NanoJev animation"><br><sub>bản ghi động · <a href="https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/assets/side_by_side_maze.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐22 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · MIT · r-ms

##### Dữ liệu

Sao **22** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/imserhatdemir/jevspace">imserhatdemir/jevspace</a></b> — HTML · observed · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `observed` · HTML · imserhatdemir

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A DarkOrbit-style space game piloted by Jev — TypeSafe's System One model. Three.js world, deterministic engine, Jev picks the targets.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/imserhatdemir/jevspace/main/docs/screenshot-win.png" width="100%" alt="imserhatdemir/jevspace screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `observed`

##### Dữ liệu

Lượt tải 25 · Lượt thích 4 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `observed`

##### Dữ liệu

Lượt tải 0 · Lượt thích 0 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐154 · Python · inferred · 0 天 · ⭐+4</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · ekzhang

##### Dữ liệu

Sao **154** (+4) · Fork 12 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>bản ghi động</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/featherless-ai/simple-jev">featherless-ai/simple-jev</a></b> — ⭐57 · Python · inferred · 0 天 · ⭐+23</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · featherless-ai

##### Dữ liệu

Sao **57** (+23) · Fork 5 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Turn any open model into a classifier/jev endpoint

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/featherless-ai/simple-jev/main/imgs/Simple-Jev-Logo.png" width="100%" alt="featherless-ai/simple-jev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐24 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · MIT · bnsd55

##### Dữ liệu

Sao **24** · Fork 3 · Issue đang mở 6 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/siliconkernel/vllm-jev-decison">siliconkernel/vllm-jev-decison</a></b> — ⭐8 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · MIT · siliconkernel

##### Dữ liệu

Sao **8** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Classification-only typed decisions for vLLM: finite-schema candidate scoring, probabilities, and abstention. No generative fallback.

</details>

<details>
<summary><b><a href="https://github.com/wfzyx/von">wfzyx/von</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · wfzyx

##### Dữ liệu

Sao **3** · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/choxos/jev-reviewer">choxos/jev-reviewer</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · JavaScript · MIT · choxos

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay in your browser.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/4a551dbca9d0c41e.jpg" width="100%" alt="choxos/jev-reviewer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/71abea319063ce6d.gif" width="100%" alt="choxos/jev-reviewer animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kw2828/OpenJev">kw2828/OpenJev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · MIT · kw2828

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Browser decision playground and reproducible experiments on memory, uncertainty, and Doom control

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/7caa9b0eff4636a1.png" width="100%" alt="kw2828/OpenJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/af5371a3a94cb693.gif" width="100%" alt="kw2828/OpenJev animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/backmeupplz/jev_antispam_bot">backmeupplz/jev_antispam_bot</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · TypeScript · MIT · backmeupplz

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/deep-diver/mini-jev">deep-diver/mini-jev</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · deep-diver

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">legacybridge-tech/pi-typesafe-jev</a></b> — TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · TypeScript · NOASSERTION · legacybridge-tech

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.

</details>

<details>
<summary><b><a href="https://github.com/liuup/jev-research">liuup/jev-research</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · liuup

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

📊 The third-party research implementation of jev.

</details>

<details>
<summary><b><a href="https://github.com/objectgraph/jev-samegame-bench">objectgraph/jev-samegame-bench</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · TypeScript · MIT · objectgraph

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

What should a decision model be shown to play SameGame? 21 prompt strategies for TypeSafe's Jev, 76,795 logged requests and responses, reproducible tables. MIT.

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `inferred` · Python · shellneko

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐8 · Python · unverified · 2 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Bản tái tạo mở, trọng số và nghiên cứu kiến trúc` · Cộng đồng · `unverified` · Python · NOASSERTION · zhihz

##### Dữ liệu

Sao **8** (+1) · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<a id="apps-demos"></a>

## Ứng dụng, trò chơi, robot và demo tương tác

Trò chơi, robot, trình duyệt và bảng điều khiển. Demo là cách khiến các tuyên bố về độ trễ và chi phí trở nên dễ hiểu.

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐10 · Python · observed · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `observed` · Python · Apache-2.0 · zadescoxp

##### Dữ liệu

Sao **10** (+1) · Fork 1 · Issue đang mở 3 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `observed` · TypeScript · daftAI2026

##### Dữ liệu

Sao **2** · Fork 2 · Issue đang mở 2 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `observed` · Rust · MIT · markjaquith

##### Dữ liệu

Sao **1** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `observed` · TypeScript · adiun

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `observed` · Dart · Bud-ro

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/chris-wozniczek/jev-voice-control">chris-wozniczek/jev-voice-control</a></b> — Swift · observed · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `observed` · Swift · chris-wozniczek

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-bar Swift app.

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 1 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `observed` · Python · MIT · tirukovelamanoj

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/8c1b0d55baf76296.gif" width="100%" alt="tirukovelamanoj/jev-plays-doom animation"><br><sub>bản ghi động · <a href="https://raw.githubusercontent.com/tirukovelamanoj/jev-plays-doom/main/docs/jev-doom.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `observed` · TypeScript · wustep

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://x.com/tspy/status/2100864234523685146">X intent labeller</a></b> — @tspy · observed · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `observed` · [yishan](https://x.com/tspy) · @tspy · x.com

##### Dữ liệu

Lượt xem 2364 · Lượt thích 15 · Bình luận 9 · Đã đăng 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A Chrome extension that labels posts in an X timeline with their intent and probability as you scroll, drawn as a tag directly after each post's timestamp. Categories include inducement, provocation, promotion, machine-generated, persuasion, entertainment and information. A side panel reports session counts (seen, judged, correct) and cumulative token cost. The author reports near-instant responses and usable accuracy before any tuning.

<sub>Đang xác minh liên kết dự án gốc.</sub>

> Worth reading as a latency argument rather than an accuracy one: labelling a timeline only works if the decision costs less than the scroll, which is the constraint a generative model cannot meet.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/0641644f12a25a45.jpg" width="100%" alt="X intent labeller screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/b80cf3173f63bdd7.gif" width="100%" alt="X intent labeller animation"><br><sub>bản ghi động · <a href="https://video.twimg.com/amplify_video/2100858340331200512/vid/avc1/1242x720/ex2FF5-TerVxo9xX.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐109 · Python · inferred · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Python · MIT · hr98w

##### Dữ liệu

Sao **109** (+2) · Fork 12 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐104 · TypeScript · inferred · 0 天 · ⭐+7</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · TypeScript · MIT · jkudish

##### Dữ liệu

Sao **104** (+7) · Fork 5 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/d9b7631c25d7db06.gif" width="100%" alt="jkudish/jev-browser animation"><br><sub>bản ghi động · <a href="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐71 · JavaScript · inferred · 1 天 · ⭐+10</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · MIT · moritzkremb

##### Dữ liệu

Sao **71** (+10) · Fork 8 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/mizchi/jev-playground">mizchi/jev-playground</a></b> — ⭐15 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · TypeScript · mizchi

##### Dữ liệu

Sao **15** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground animation"><br><sub>bản ghi động</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐7 · Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Python · MIT · komorra

##### Dữ liệu

Sao **7** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · TypeScript · emrickgarrett

##### Dữ liệu

Sao **5** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐5 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · vinilana

##### Dữ liệu

Sao **5** · Fork 5 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/arielweinberger/jev-autopilot">arielweinberger/jev-autopilot</a></b> — ⭐3 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · TypeScript · arielweinberger

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs $0.01.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/arielweinberger/jev-autopilot/main/docs/demo.png" width="100%" alt="arielweinberger/jev-autopilot screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 1 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Go · MIT · paulsmith

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · TypeScript · MIT · vmendes90

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/vmendes90--jev-shield/ee87b261d199a34c.jpg" width="100%" alt="vmendes90/jev-shield screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0x7067/jev-browse">0x7067/jev-browse</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · MIT · 0x7067

##### Dữ liệu

Sao **1** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Browser automation with Jev (TypeSafe) as decision model

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/6b2906f1131adf4c.gif" width="100%" alt="0x7067/jev-browse screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/3efc4d3b381ff9f5.gif" width="100%" alt="0x7067/jev-browse animation"><br><sub>bản ghi động · <a href="https://raw.githubusercontent.com/0x7067/jev-browse/main/docs/demo.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-mario">4esv/jev-mario</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Python · 4esv

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe Jev plays Super Mario Bros from a text description of emulator RAM

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-mario/main/runs/1-1-branch-jev-20260918-170421.gif" width="100%" alt="4esv/jev-mario screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-mario/main/runs/1-1-branch-jev-20260918-170421.gif" width="100%" alt="4esv/jev-mario animation"><br><sub>bản ghi động</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/charleeagni/JevPiano">charleeagni/JevPiano</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · charleeagni

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

@typesafeai 's Jev controls the 2 hands and each finger to play the piano in real-time.  Jev only "sees" what we see and plays this from the "note waterfall". It uses  @browser_use 's jev-ultrafast and some decision scheduling to make this happen in real-time.  Sound on 🔈🔉🔊

</details>

<details>
<summary><b><a href="https://github.com/finetuningsingh/jev-chatbot">finetuningsingh/jev-chatbot</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · MIT · finetuningsingh

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Experiment: using TypeSafe Jev as a chatbot by choosing replies one letter or word at a time

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · TypeScript · Little-Planet-Labs

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 2 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Python · PistachioAIHQ

##### Dữ liệu

Sao **1** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/bahramzada/jev-taxi-dispatch">bahramzada/jev-taxi-dispatch</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · MIT · bahramzada

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Real-vaxt taksi dispetçerlik simulyasiyası - TypeSafe JEV (System One) modeli ilə

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/bahramzada--jev-taxi-dispatch/e616f4168b15d3f2.png" width="100%" alt="bahramzada/jev-taxi-dispatch screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/beto11-gif/jev-trading-backend">beto11-gif/jev-trading-backend</a></b> — inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · beto11-gif

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/BrendanH18/jev-lab">BrendanH18/jev-lab</a></b> — Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Python · MIT · BrendanH18

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brendanh18--jev-lab/b16b9535e3744cd3.png" width="100%" alt="BrendanH18/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/chahero/driving-jev">chahero/driving-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Python · chahero

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Watch TypeSafe Jev make highway driving decisions. Includes live API and offline gameplay previews.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev-preview.gif" width="100%" alt="chahero/driving-jev screenshot"></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev.mp4"><img src="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev-preview.gif" width="100%" alt="chahero/driving-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev.mp4">Mở video</a></sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/ethereumdegen/jev-discord-bot">ethereumdegen/jev-discord-bot</a></b> — Rust · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Rust · MIT · ethereumdegen

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/JYeswak/jev_playground">JYeswak/jev_playground</a></b> — Shell · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Shell · MIT · JYeswak

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jyeswak--jev_playground/b6414da07c9c5aa8.jpg" width="100%" alt="JYeswak/jev_playground screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevinbadi/jev-voice">kevinbadi/jev-voice</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · Python · MIT · kevinbadi

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Talk to your Mac. Local whisper.cpp + one Jev (TypeSafe) call per command + macOS automation.

</details>

<details>
<summary><b><a href="https://github.com/LakshyaChaudhry/jev-label-desk">LakshyaChaudhry/jev-label-desk</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · TypeScript · LakshyaChaudhry

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

weekend project using Jev to automate trace / data labeling for a provided labeling taxonomy.

</details>

<details>
<summary><b><a href="https://github.com/marcelomar21/demo-tetris-jev">marcelomar21/demo-tetris-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · marcelomar21

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Tetris arcade jogado pelo Jev da TypeSafe AI, com decisões em JSON, antecipação de jogadas e custo por partida.

</details>

<details>
<summary><b><a href="https://github.com/metrox-eth/moss-jev">metrox-eth/moss-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · metrox-eth

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

MOSS × Jev: a recorded-run 3D demo of the litter-picking rover choosing targets with TypeSafe's Jev decision model.

</details>

<details>
<summary><b><a href="https://github.com/n3ndor/n8n-nodes-typesafe-jev">n3ndor/n8n-nodes-typesafe-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · TypeScript · MIT · n3ndor

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

n8n community node for TypeSafe Jev structured AI decisions

</details>

<details>
<summary><b><a href="https://github.com/PierrunoYT/JevFlow">PierrunoYT/JevFlow</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · TypeScript · PierrunoYT

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A trading bot powered by TypeSafe AI's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pistachiopranay/jev-synergy-screening">pistachiopranay/jev-synergy-screening</a></b> — inferred · 2 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · pistachiopranay

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/rchovatiya88/cyber-breach-jev">rchovatiya88/cyber-breach-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · rchovatiya88

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model

</details>

<details>
<summary><b><a href="https://github.com/tanayvasishtha/Slither-Me-Jev">tanayvasishtha/Slither-Me-Jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `inferred` · JavaScript · tanayvasishtha

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

8 AI snakes, 1 human, 1 arena. Every snake is driven live by TypeSafe's Jev, making all decisions in real time

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/tanayvasishtha/Slither-Me-Jev/main/menu-screenshot.png" width="100%" alt="tanayvasishtha/Slither-Me-Jev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/sorrycc/typesafe-snake">sorrycc/typesafe-snake</a></b> — ⭐17 · TypeScript · unverified · 1 天</summary>

##### Thông tin cơ bản

`Ứng dụng, trò chơi, robot và demo tương tác` · Cộng đồng · `unverified` · TypeScript · sorrycc

##### Dữ liệu

Sao **17** · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code

</details>

<a id="media-discussions"></a>

## Bài viết, thảo luận và các danh sách cùng chủ đề

Các thread ra mắt, bài viết độc lập và những danh sách tuyển chọn khác trong lĩnh vực này. Kho lưu trữ này không phải là duy nhất, và nói ra điều đó hữu ích hơn là giả vờ ngược lại.

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐5471 · Python · observed · 0 天 · ⭐+159</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · Python · MIT · browser-use

##### Dữ liệu

Sao **5471** (+159) · Fork 342 · Issue đang mở 32 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

i. am. speed.

<sub>Được tìm thấy trong mã nguồn: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcdb919ac3afb514.gif" width="100%" alt="browser-use/jev-ultrafast animation"><br><sub>bản ghi động · <a href="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/demo.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1890 · observed · 3 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 1890 · Bình luận 496 · Lần push cuối 2026-09-15 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐520 · Python · observed · 0 天 · ⭐+9</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · Python · MIT · Anil-matcha

##### Dữ liệu

Sao **520** (+9) · Fork 100 · Issue đang mở 4 · Ngày tạo 2023-05-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>Được tìm thấy trong mã nguồn: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐224 · CSS · observed · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · CSS · MIT · AbdelStark

##### Dữ liệu

Sao **224** (+1) · Fork 32 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>Được tìm thấy trong mã nguồn: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐219 · TypeScript · observed · 0 天 · ⭐+11</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · TypeScript · dabit3

##### Dữ liệu

Sao **219** (+11) · Fork 19 · Issue đang mở 17 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

<sub>Được tìm thấy trong mã nguồn: `jev-lint/proxy.mjs`, `jev-tower/jev-proxy.mjs`, `nl-palette/server/jev.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐165 · Python · observed · 0 天 · ⭐+12</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · Python · yibie

##### Dữ liệu

Sao **165** (+12) · Fork 24 · Issue đang mở 12 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐113 · observed · 0 天 · ⭐+10</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · CC0-1.0 · cobanov

##### Dữ liệu

Sao **113** (+10) · Fork 10 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐65 · observed · 0 天 · ⭐+5</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · CC0-1.0 · AnotiaWang

##### Dữ liệu

Sao **65** (+5) · Fork 18 · Issue đang mở 3 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>Được tìm thấy trong mã nguồn: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐51 · observed · 1 天 · ⭐+5</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 51 · Bình luận 11 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐33 · JavaScript · observed · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### Dữ liệu

Sao **33** (+1) · Fork 10 · Issue đang mở 9 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A community directory of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐9 · JavaScript · observed · 0 天 · ⭐+3</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · JavaScript · NOASSERTION · OmniJev

##### Dữ liệu

Sao **9** (+3) · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Papers, open reproductions and independent evaluations behind System One models and Jev.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49760264">Using jev to improve product experiences is pretty crazy</a></b> — ⭐6 · observed · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 6 · Bình luận 3 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 3 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 5 · Bình luận 0 · Lần push cuối 2026-09-15 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 4 · Bình luận 0 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 4 · Bình luận 0 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 3 · Bình luận 0 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755005">Two techniques for working with System One models</a></b> — ⭐3 · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 3 · Bình luận 0 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 3 · Bình luận 0 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐2 · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · NOASSERTION · aliaihub

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### Dữ liệu

Sao **2** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49759706">I used Jev to control a swarm of 15 simulated drones in real time</a></b> — ⭐2 · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 0 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49759999">Jev&#x27;s Architecture Unmasked</a></b> — ⭐2 · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 0 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49753667">Show HN: Explore 2D semantic space with the Jev model</a></b> — ⭐2 · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 0 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

SemanticSpace is an experiment around Jev, TypeSafe AI’s new model. It uses a Cartesian plane defined by arbitrary phrases for each axis, to map prompts onto the resulting 2D semantic space. You can edit the prompts and axes to visualize virtually any 2D relationship.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49750649">Show HN: Open-Source Alternative to TypeSafe.ai</a></b> — ⭐2 · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 1 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49744527">Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)</a></b> — ⭐2 · observed · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 1 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Full disclosure, it was coded with AI, I don&#x27;t claim otherwise. But I wanted to test out tool calls and iterative problem solving using Jev and needed a simple library&#x2F;framework&#x2F;harness to do that.
SOKIT (System One Knowledge, Instructions and Tools) is the result

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49729945">The first (public) System One Model; Jev gives AI the properties of code</a></b> — ⭐2 · observed · 2 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 0 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49757995">TypeSafe / Jev latency-focused demos built by Devin</a></b> — ⭐2 · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 0 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49745212">Typesafe&#x27;s Jev is the fish at the poker table</a></b> — ⭐2 · observed · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 1 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49733647">Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step</a></b> — ⭐2 · observed · 2 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 0 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49734345">Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD</a></b> — ⭐2 · observed · 2 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 0 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49760138">What is a System One model and why we need it?</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed`

##### Dữ liệu

Điểm 2 · Bình luận 0 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/ozers/jevsome-projects">ozers/jevsome-projects</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · JavaScript · MIT · ozers

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Open-source projects that provably call Jev, TypeSafe AI's System One model. Every entry links to the line of code that proves it. Refreshed daily.

</details>

<details>
<summary><b><a href="https://github.com/rhc98/awesome-jev">rhc98/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · TypeScript · NOASSERTION · rhc98

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself.

</details>

<details>
<summary><b><a href="https://github.com/soderlind/ai-provider-for-jev">soderlind/ai-provider-for-jev</a></b> — ⭐1 · PHP · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · PHP · soderlind

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).

</details>

<details>
<summary><b><a href="https://github.com/aamanlamba/jev-explore">aamanlamba/jev-explore</a></b> — Jupyter · observed · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · Jupyter · aamanlamba

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

An example repository for exploring Jev - the System One model

</details>

<details>
<summary><b><a href="https://github.com/alpibrusl/lex-judge">alpibrusl/lex-judge</a></b> — Lex · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · Lex · alpibrusl

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed judgments from a System One model, as a \[net\]-only Lex effect

</details>

<details>
<summary><b><a href="https://github.com/hide-G/magi-system-on-jev">hide-G/magi-system-on-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · JavaScript · hide-G

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/hide-G/magi-system-on-jev/master/public/ogp.png" width="100%" alt="hide-G/magi-system-on-jev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/ImXforever/typesafe-jev-1.13">ImXforever/typesafe-jev-1.13</a></b> — Python · observed · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · Python · MIT · ImXforever

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

JEV

</details>

<details>
<summary><b><a href="https://github.com/JohnDotOwl/awesome-jev">JohnDotOwl/awesome-jev</a></b> — JavaScript · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · JavaScript · CC0-1.0 · JohnDotOwl

##### Dữ liệu

Sao **0** · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A curated list of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/jtnkminimal/awesome-jev">jtnkminimal/awesome-jev</a></b> — Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · Python · CC0-1.0 · jtnkminimal

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A curated projects built with Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/piyush97/focus-tube">piyush97/focus-tube</a></b> — JavaScript · observed · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · JavaScript · MIT · piyush97

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model

</details>

<details>
<summary><b><a href="https://github.com/rbalch/typesafeai-review">rbalch/typesafeai-review</a></b> — Python · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · Python · rbalch

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Using Typesafe.AI to generate diff reviews.

</details>

<details>
<summary><b><a href="https://github.com/robzolkos/omarchy-issue-classifier">robzolkos/omarchy-issue-classifier</a></b> — Ruby · observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · Ruby · robzolkos

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Classify the Omarchy issue backlog with Jev, TypeSafe's System One model. Ten typed questions per issue in one request, for a hundredth of a cent each.

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/jev-trader">Shashank-H/jev-trader</a></b> — observed · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · AGPL-3.0 · Shashank-H

##### Dữ liệu

Sao **0** · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

An automated trader using SystemOne model - TypesafeAI Jev

</details>

<details>
<summary><b><a href="https://github.com/TheGali/terrarium">TheGali/terrarium</a></b> — JavaScript · observed · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `observed` · JavaScript · MIT · TheGali

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.

</details>

<details>
<summary><b><a href="https://github.com/jarrodwatts/jev-trader">jarrodwatts/jev-trader</a></b> — ⭐865 · TypeScript · inferred · 1 天 · ⭐+17</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · jarrodwatts

##### Dữ liệu

Sao **865** (+17) · Fork 162 · Issue đang mở 3 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

</details>

<details>
<summary><b><a href="https://github.com/droidrun/mobile-jev">droidrun/mobile-jev</a></b> — ⭐135 · JavaScript · inferred · 1 天 · ⭐+9</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · JavaScript · MIT · droidrun

##### Dữ liệu

Sao **135** (+9) · Fork 22 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/superagents-lab/jev-search">superagents-lab/jev-search</a></b> — ⭐104 · TypeScript · inferred · 0 天 · ⭐+11</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · superagents-lab

##### Dữ liệu

Sao **104** (+11) · Fork 17 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/superagents-lab--jev-search/5a545ddfd6a52aed.png" width="100%" alt="superagents-lab/jev-search screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mrnugget/jev-shell-history">mrnugget/jev-shell-history</a></b> — ⭐43 · TypeScript · inferred · 0 天 · ⭐+3</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · mrnugget

##### Dữ liệu

Sao **43** (+3) · Fork 3 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Fish-style zsh history autosuggestions ranked by Jev (TypeSafe)

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history animation"><br><sub>bản ghi động</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">IAmUnbounded/save-token-jev-clean</a></b> — ⭐40 · TypeScript · inferred · 0 天 · ⭐+3</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · IAmUnbounded

##### Dữ liệu

Sao **40** (+3) · Fork 9 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/daseinlabs/open-jev">daseinlabs/open-jev</a></b> — ⭐32 · Python · inferred · 0 天 · ⭐+1</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · daseinlabs

##### Dữ liệu

Sao **32** (+1) · Fork 5 · Issue đang mở 2 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>không công bố media</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov"><img src="" width="100%" alt="daseinlabs/open-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hqman/JevScout">hqman/JevScout</a></b> — ⭐17 · Python · inferred · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · hqman

##### Dữ liệu

Sao **17** (+2) · Fork 2 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>không công bố media</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4"><img src="" width="100%" alt="hqman/JevScout video"></a><br><sub><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jon-devlapaz/jev-me">jon-devlapaz/jev-me</a></b> — ⭐9 · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · MIT · jon-devlapaz

##### Dữ liệu

Sao **9** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Grill-me with Jev optional each turn

</details>

<details>
<summary><b><a href="https://github.com/oso95/x-scanner">oso95/x-scanner</a></b> — ⭐7 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · oso95

##### Dữ liệu

Sao **7** (+2) · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter

</details>

<details>
<summary><b><a href="https://github.com/JackZeng/Jev_apps">JackZeng/Jev_apps</a></b> — ⭐6 · Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · JackZeng

##### Dữ liệu

Sao **6** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

看看 Jev 能做什么：用中英文讲清热门应用、工作原理和各自优缺点。Explore Jev apps with plain-language examples, explanations, and comparisons.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://pbs.twimg.com/amplify_video_thumb/2100410607807918080/img/lNfcykqoOvLoZHWa.jpg" width="100%" alt="JackZeng/Jev_apps screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Kevthetech143/super-jev">Kevthetech143/super-jev</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · MIT · Kevthetech143

##### Dữ liệu

Sao **5** · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A small, extensible decision-to-action harness for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/joelhooks/pi-fast-jev-compaction">joelhooks/pi-fast-jev-compaction</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · joelhooks

##### Dữ liệu

Sao **4** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Pi extension: verbatim context compaction with TypeSafe Jev decisions

</details>

<details>
<summary><b><a href="https://github.com/mateonunez/jod">mateonunez/jod</a></b> — ⭐3 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · mateonunez

##### Dữ liệu

Sao **3** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers.

</details>

<details>
<summary><b><a href="https://github.com/haseeb-heaven/jev-system-one">haseeb-heaven/jev-system-one</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · MIT · haseeb-heaven

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/haseeb-heaven--jev-system-one/e41c848323b1077a.png" width="100%" alt="haseeb-heaven/jev-system-one screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevinpita/pi-jev-context">kevinpita/pi-jev-context</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · kevinpita

##### Dữ liệu

Sao **2** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Reversible context pruning for Pi, powered by TypeSafe Jev. Keep useful context without deleting session history.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevinpita--pi-jev-context/9f40314df01e39d4.png" width="100%" alt="kevinpita/pi-jev-context screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Charlyhno-eng/jev-document-classification">Charlyhno-eng/jev-document-classification</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · Charlyhno-eng

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/charlyhno-eng--jev-document-classification/113bcf66f1648122.png" width="100%" alt="Charlyhno-eng/jev-document-classification screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/everyai-com/jev-directory">everyai-com/jev-directory</a></b> — ⭐1 · HTML · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · HTML · MIT · everyai-com

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/jev-review-action">fatwang2/jev-review-action</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · JavaScript · MIT · fatwang2

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 2 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.

</details>

<details>
<summary><b><a href="https://github.com/lbotinelly/jev-little-airways">lbotinelly/jev-little-airways</a></b> — ⭐1 · HTML · inferred · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · HTML · MIT · lbotinelly

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A show-and-tell capability study for Jev, TypeSafe's System One decision model.

</details>

<details>
<summary><b><a href="https://github.com/MumuTW/awesome-jev">MumuTW/awesome-jev</a></b> — ⭐1 · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · CC0-1.0 · MumuTW

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

快速看懂風格鮮明的 Jev：型別化決策的 System One，以及社群熱議的同類模型。

</details>

<details>
<summary><b><a href="https://github.com/sontakey/awesome-jev">sontakey/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · NOASSERTION · sontakey

##### Dữ liệu

Sao **1** · Fork 1 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Unofficial list of insanely useful TypeSafe AI Jev / System One projects

</details>

<details>
<summary><b><a href="https://github.com/TanayPadar/gpt-vs-jev">TanayPadar/gpt-vs-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · TanayPadar

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Compare GPT generated language with JEV structured Noul decisions on the same input.

</details>

<details>
<summary><b><a href="https://github.com/tylerjharden/harden-jev-decides">tylerjharden/harden-jev-decides</a></b> — ⭐1 · TypeScript · inferred · 2 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · tylerjharden

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.

</details>

<details>
<summary><b><a href="https://github.com/Z761293629/pi-jev-helm">Z761293629/pi-jev-helm</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · Z761293629

##### Dữ liệu

Sao **1** · Fork 0 · Issue đang mở 3 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-joust">4esv/jev-joust</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · 4esv

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

TypeSafe Jev vs Jev in NES Joust, bring your own ROM

</details>

<details>
<summary><b><a href="https://github.com/adhamelhayek-lab/jev-connector">adhamelhayek-lab/jev-connector</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · JavaScript · adhamelhayek-lab

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/agentik-os/jev-radar">agentik-os/jev-radar</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · JavaScript · agentik-os

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/amansoory/JEV2048">amansoory/JEV2048</a></b> — inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · amansoory

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/aoi-yoneda/haikyuBattleJev">aoi-yoneda/haikyuBattleJev</a></b> — HTML · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · HTML · aoi-yoneda

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev (TypeSafe AI) が打者を判断する配球バトル野球シミュレーション — 9回制・パワプロ風

</details>

<details>
<summary><b><a href="https://github.com/AppitStudio/awesome-jev">AppitStudio/awesome-jev</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · NOASSERTION · AppitStudio

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 4 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Curated Jev resources and runnable examples for typed AI decisions.

</details>

<details>
<summary><b><a href="https://github.com/Btheriot83/jev-academy">Btheriot83/jev-academy</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · Btheriot83

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Public Jev / TypeSafe academy — zero-to-hero walkthrough for Brandon Theriot

</details>

<details>
<summary><b><a href="https://github.com/enuminous/JEV-EFMW-Syncretic-Layer">enuminous/JEV-EFMW-Syncretic-Layer</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · NOASSERTION · enuminous

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/golergka/jev-plays-starcraft-2">golergka/jev-plays-starcraft-2</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · golergka

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/heaven-hm/jev-system-one">heaven-hm/jev-system-one</a></b> — inferred · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · heaven-hm

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

</details>

<details>
<summary><b><a href="https://github.com/jdhornsby/typesafe-jev">jdhornsby/typesafe-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · jdhornsby

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/jsherman999/jev_local_web_seatch-">jsherman999/jev_local_web_seatch-</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · jsherman999

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/julianarchila/jev-experiments">julianarchila/jev-experiments</a></b> — inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · julianarchila

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/Justmalhar/awesome-jev-apps">Justmalhar/awesome-jev-apps</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · MIT · Justmalhar

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/kazuhideoki/jev-search">kazuhideoki/jev-search</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · kazuhideoki

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Recursive semantic file search using TypeSafe Jev and fzf

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-master">kevin9327/jev-master</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · MIT · kevin9327

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Typed System One decisions with Jev: Choice + Score + Noul composed in code.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevin9327--jev-master/cbf05c4561269075.png" width="100%" alt="kevin9327/jev-master screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/KhaiStimpson/JevGen">KhaiStimpson/JevGen</a></b> — C# · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · C# · KhaiStimpson

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/kimgh06/jev">kimgh06/jev</a></b> — inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · kimgh06

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

what's jev

</details>

<details>
<summary><b><a href="https://github.com/kspviswa/chakravyuha-jev">kspviswa/chakravyuha-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · JavaScript · MIT · kspviswa

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kspviswa--chakravyuha-jev/4dfa22d0de9f27c1.png" width="100%" alt="kspviswa/chakravyuha-jev screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Kushwho/jev-codes">Kushwho/jev-codes</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · Kushwho

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Jev

</details>

<details>
<summary><b><a href="https://github.com/lalitsonawane/jev-one-system">lalitsonawane/jev-one-system</a></b> — inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · lalitsonawane

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/LingXuanYin/jev-chat">LingXuanYin/jev-chat</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · NOASSERTION · LingXuanYin

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jev 聊天机：一个「只选不写」的聊天机——每个回复由逐词选择拼装，词典+分级索引+输入法式联想，由真实 Jev（TypeSafe System One）驱动。非官方实验，与 TypeSafe AI 无关联。

</details>

<details>
<summary><b><a href="https://github.com/llmer/jev-goldwrong">llmer/jev-goldwrong</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · llmer

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Hunting label errors in popular text-classification datasets with TypeSafe Jev

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/llmer/jev-goldwrong/main/docs/diagrams/main.png" width="100%" alt="llmer/jev-goldwrong screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/lookfwd/jev-fact-checker">lookfwd/jev-fact-checker</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · lookfwd

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Uses Typesafe AI Jev to Provide A Tweet Fact Checker

</details>

<details>
<summary><b><a href="https://github.com/LukasCaha/jev-profanity">LukasCaha/jev-profanity</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · JavaScript · LukasCaha

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Jev based detector and rewrite engine to censor profanity, rudeness and hate speech.

</details>

<details>
<summary><b><a href="https://github.com/marcoss/jev-assistant">marcoss/jev-assistant</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · marcoss

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/memorysaver/jev-atari-lab">memorysaver/jev-atari-lab</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · GPL-2.0 · memorysaver

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Challenge Atari with Jev: structured decisions, value questions, and replayable experiments

</details>

<details>
<summary><b><a href="https://github.com/miguelaeh/jev-microduck">miguelaeh/jev-microduck</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · miguelaeh

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Make Microduck autonomous controlled in a loop by Jev.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><sub>không công bố media</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/miguelaeh/jev-microduck/main/duck/videos/jev_camera_head.mp4"><img src="" width="100%" alt="miguelaeh/jev-microduck video"></a><br><sub><a href="https://raw.githubusercontent.com/miguelaeh/jev-microduck/main/duck/videos/jev_camera_head.mp4">Mở video</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moto-taka/jev-orchestrator">moto-taka/jev-orchestrator</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · moto-taka

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/MrDesjardins/jev-send-guard">MrDesjardins/jev-send-guard</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · MrDesjardins

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/myokoym/misereru-slide-jev">myokoym/misereru-slide-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · JavaScript · myokoym

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/Nachom3/jevTrader">Nachom3/jevTrader</a></b> — Rust · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Rust · Nachom3

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

A High Frecuncy Trader made in Rust using Jev as a decision maker.

</details>

<details>
<summary><b><a href="https://github.com/nardinmarcus/pi-jev-typesafe">nardinmarcus/pi-jev-typesafe</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · nardinmarcus

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model discovery, and budget caps

</details>

<details>
<summary><b><a href="https://github.com/narulaskaran/jev-data-questions">narulaskaran/jev-data-questions</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · narulaskaran

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 1 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/oldmoldycake/jev_vampire_survivors">oldmoldycake/jev_vampire_survivors</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · MIT · oldmoldycake

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/OsirianLegacy/JevTactics">OsirianLegacy/JevTactics</a></b> — CMake · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · CMake · OsirianLegacy

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/pedrorau/feedback-radar-jev">pedrorau/feedback-radar-jev</a></b> — Astro · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Astro · MIT · pedrorau

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-19 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/rahiseko-alt/jev-test1">rahiseko-alt/jev-test1</a></b> — Shell · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Shell · rahiseko-alt

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/robzilla1738/Jev-DeepSWE">robzilla1738/Jev-DeepSWE</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · robzilla1738

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Nguồn gốc không công bố mô tả nào.

</details>

<details>
<summary><b><a href="https://github.com/thisisjorge/jev-control-room">thisisjorge/jev-control-room</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · thisisjorge

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Interactive control room for fast typed AI decisions with TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/TKY-27/JevSlop">TKY-27/JevSlop</a></b> — TypeScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TypeScript · MIT · TKY-27

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Jevによるnote記事のAI Slop判定サイト

</details>

<details>
<summary><b><a href="https://github.com/TonyP-MR/jev-curation-engine">TonyP-MR/jev-curation-engine</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · TonyP-MR

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions with existing LLM audit results.

</details>

<details>
<summary><b><a href="https://github.com/TreeCityWes/jev_x1">TreeCityWes/jev_x1</a></b> — inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · TreeCityWes

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

x1.xyz transaction classifier

</details>

<details>
<summary><b><a href="https://github.com/trungdq88/jev-tetris">trungdq88/jev-tetris</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · JavaScript · trungdq88

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Jev play Tetris in real-time against other AI models

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/trungdq88/jev-tetris/main/docs/screenshot.png" width="100%" alt="trungdq88/jev-tetris screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

<sub>Tài nguyên được dẫn trực tiếp từ kho lưu trữ gốc vì dự án không khai báo giấy phép cho phép tái phân phối.</sub>

</details>

<details>
<summary><b><a href="https://github.com/Tsagaanbayr1/jev-tetris">Tsagaanbayr1/jev-tetris</a></b> — JavaScript · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · JavaScript · Tsagaanbayr1

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

Real-time Tetris versus Jev, a TypeSafe decision model — spins, garbage, B2B chains, and decisions prefetched a piece ahead

</details>

<details>
<summary><b><a href="https://github.com/yaredtekile/jev-2048">yaredtekile/jev-2048</a></b> — Python · inferred · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `inferred` · Python · MIT · yaredtekile

##### Dữ liệu

Sao **0** · Fork 0 · Issue đang mở 0 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-19

##### Tóm tắt

TypeSafe Jev plays live 2048. It doesn’t see pixels or write text, it only picks the swipe.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yaredtekile--jev-2048/2b37ce94a3eae275.gif" width="100%" alt="yaredtekile/jev-2048 screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yaredtekile--jev-2048/2b37ce94a3eae275.gif" width="100%" alt="yaredtekile/jev-2048 animation"><br><sub>bản ghi động</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/realZachi/typesafe-adblock">realZachi/typesafe-adblock</a></b> — ⭐49 · JavaScript · unverified · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `unverified` · JavaScript · MIT · realZachi

##### Dữ liệu

Sao **49** · Fork 4 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.

</details>

<details>
<summary><b><a href="https://github.com/razorback16/openjev">razorback16/openjev</a></b> — ⭐36 · Python · unverified · 0 天 · ⭐+5</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `unverified` · Python · Apache-2.0 · razorback16

##### Dữ liệu

Sao **36** (+5) · Fork 4 · Issue đang mở 1 · Ngày tạo 2026-09-18 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Open, Jev-compatible System One decision server on DiffusionGemma

</details>

<details>
<summary><b><a href="https://github.com/devanshbatham/commit-miner">devanshbatham/commit-miner</a></b> — ⭐22 · Rust · unverified · 1 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `unverified` · Rust · devanshbatham

##### Dữ liệu

Sao **22** · Fork 5 · Issue đang mở 0 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-17 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.

</details>

<details>
<summary><b><a href="https://github.com/phyous/tsai-sc">phyous/tsai-sc</a></b> — ⭐15 · Python · unverified · 2 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `unverified` · Python · MIT · phyous

##### Dữ liệu

Sao **15** · Fork 1 · Issue đang mở 0 · Ngày tạo 2026-09-16 · Lần push cuối 2026-09-16 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.

<table><tr><th align="center" width="50%">Hình ảnh</th><th align="center" width="50%">Video</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/phyous--tsai-sc/f48a030ae92fb1fe.png" width="100%" alt="phyous/tsai-sc screenshot"></td>
<td align="center" valign="top"><sub>không công bố media</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andysc/IBM-Q-System-One-3D-model">andysc/IBM-Q-System-One-3D-model</a></b> — ⭐12 · OpenSCAD · unverified · 2688 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `unverified` · OpenSCAD · andysc

##### Dữ liệu

Sao **12** · Fork 4 · Issue đang mở 1 · Ngày tạo 2019-03-16 · Lần push cuối 2019-05-10 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

3D-printed model of IBM Q System One

</details>

<details>
<summary><b><a href="https://github.com/zhengxuyu/litjev">zhengxuyu/litjev</a></b> — ⭐4 · Python · unverified · 0 天</summary>

##### Thông tin cơ bản

`Bài viết, thảo luận và các danh sách cùng chủ đề` · Cộng đồng · `unverified` · Python · Apache-2.0 · zhengxuyu

##### Dữ liệu

Sao **4** · Fork 1 · Issue đang mở 3 · Ngày tạo 2026-09-17 · Lần push cuối 2026-09-18 · Lần đầu được liệt kê 2026-09-18

##### Tóm tắt

Turn any off-the-shelf LLM into a Jev -like decision layer

</details>

<a id="projects-by-implementation-language"></a>

## Dự án theo ngôn ngữ triển khai

Hệ sinh thái tập trung vào Python và TypeScript, nhưng các client có kiểu vẫn tiếp tục xuất hiện ở những ngôn ngữ khác. Bảng này được tạo từ chính các mục trong danh sách.

| Ngôn ngữ   | Mục | Ví dụ                                                                                                          |
| ---------- | --- | -------------------------------------------------------------------------------------------------------------- |
| Python     | 157 | `typesafe-ai/system-one-adapter-python`, `typesafe-ai/typesafe-sdk-python`, `MrJev/awesome-jev`                |
| TypeScript | 131 | `typesafe-ai/typesafe-sdk-js`, `AntonioCoppe/jev-harness`, `opaielsheikh/typesafe-migration-guard`             |
| JavaScript | 65  | `ziyu/sytem-one-sdk`, `Ying-Kai-Liao/jev-browser`, `arunav25/jev-mcp`                                          |
| Rust       | 13  | `AkashPriyadarshii/jev-curate`, `AkashPriyadarshii/jev-seo`, `AkashPriyadarshii/jev-scout`                     |
| Go         | 12  | `RadixILS-Dev/typesafe-sdk-go`, `Stumble/jev-go`, `anilsenay/jev`                                              |
| HTML       | 10  | `typesafe-ai/typesafe-ai.github.io`, `yzfly/awesome-jev-zh`, `vinilana/jev-eval-agent`                         |
| PHP        | 4   | `Butochnikov/laravel-typesafe-jev`, `mzainzulifqar/jev-php-sdk`, `juanlentino/jev-connector`                   |
| Shell      | 4   | `realZachi/pg-jev`, `wotai-dev/typesafe-jev-tools`, `JYeswak/jev_playground`                                   |
| Elixir     | 3   | `nshkrdotcom/typesafe_sdk`, `typesend/typesafe_ai`, `dannote/jev`                                              |
| Jupyter    | 3   | `jexp/neo4jev`, `bitnovus/jev-spam-eval`, `aamanlamba/jev-explore`                                             |
| Ruby       | 3   | `javiergradiche/ruby_llm-providers-typesafe`, `obie/ruby_decision_model`, `robzolkos/omarchy-issue-classifier` |
| C#         | 2   | `saibimajdi/typesafeai-dotnet-sdk`, `KhaiStimpson/JevGen`                                                      |
| Java       | 2   | `Premo-Cloud/typesafe-sdk-java`, `Olti1947/jev-java`                                                           |
| Swift      | 2   | `gpazo/jev-vphone-cli`, `chris-wozniczek/jev-voice-control`                                                    |
| Astro      | 1   | `pedrorau/feedback-radar-jev`                                                                                  |
| C          | 1   | `giuliosmall/pg_typesafe`                                                                                      |
| CMake      | 1   | `OsirianLegacy/JevTactics`                                                                                     |
| CSS        | 1   | `AbdelStark/awesome-typesafe`                                                                                  |
| Dart       | 1   | `Bud-ro/jev-demos`                                                                                             |
| Haskell    | 1   | `inanna-malick/jev-dsl`                                                                                        |
| Kotlin     | 1   | `ufec/jev-block-android-ad`                                                                                    |
| Lex        | 1   | `alpibrusl/lex-judge`                                                                                          |
| Nushell    | 1   | `cablehead/jev.nu`                                                                                             |
| OCaml      | 1   | `jonesmelton/verdict`                                                                                          |
| OpenSCAD   | 1   | `andysc/IBM-Q-System-One-3D-model`                                                                             |
| PowerShell | 1   | `omni-/ask-jev`                                                                                                |
| TeX        | 1   | `dnakhoa/jev-deferred-crispification`                                                                          |

<sub>Chỉ những mục khai báo ngôn ngữ mới được tính. Các mục về hạ tầng, tài liệu và thảo luận bị loại khỏi bảng này.</sub>

## Danh sách này được giữ mới như thế nào

Không ai chỉnh sửa phần thân của README này bằng tay. Kho lưu trữ chạy một pipeline năm giai đoạn theo lịch và chỉ commit khi thực sự có thay đổi.

<img src="assets/readme/pipeline.svg" width="100%" alt="Danh sách này được giữ mới như thế nào">

|             |                                                                                                                                                                                                                                                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **collect** | tìm kiếm trên GitHub theo một ma trận truy vấn, tổ chức chính thức, tìm kiếm mã trên GitHub, Hacker News và hub Hugging Face.                                                                                                                                                                                    |
| **curate**  | tất định và không dùng LLM, nên hai lần chạy liên tiếp trên cùng đầu vào cho ra kết quả giống hệt nhau từng byte. Một quy tắc hai tín hiệu quyết định mức liên quan; các trường hợp trùng tên (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD và tương tự) bị loại bằng một danh sách rõ ràng, có thể kiểm toán. |
| **media**   | thu thập ảnh chụp màn hình và bản ghi màn hình của từng dự án. Tài nguyên chỉ được sao chép vào kho lưu trữ này khi dự án khai báo giấy phép cho phép tái phân phối; nếu không, URL gốc được dẫn trực tiếp và thẻ ghi rõ điều đó.                                                                                |
| **render**  | tạo mọi phiên bản ngôn ngữ từ một template duy nhất, nên hai mươi README không thể lệch nhau về cấu trúc.                                                                                                                                                                                                        |
| **audit**   | làm build thất bại nếu một mục thiếu URL, nếu một liên kết đã chết, nếu hai mục trùng URL, hoặc nếu một README lệch khỏi dạng được tạo ra.                                                                                                                                                                       |

## Đóng góp

Mọi đính chính đều được hoan nghênh và là cách nhanh nhất để cải thiện danh sách này. Hãy mở một issue hoặc pull request nếu một mục bị xếp sai danh mục, chấm sai hạng, hoặc nếu một dự án bị loại nhầm vì trùng tên — nhóm cuối cùng là nơi bộ lọc tự động dễ sai nhất. Cách thêm mục tốt nhất là thêm một nguồn vào `scripts/collect.py` thay vì sửa README, vì README được tạo lại mỗi lượt.

---

<sub>Dự án cộng đồng độc lập. Không liên kết, không được TypeSafe AI bảo trợ hay thẩm định. Hành vi sản phẩm, giá, giới hạn và bí danh model có thể thay đổi mà không báo trước; hãy kiểm chứng mọi thứ quan trọng với tài liệu chính thức. Tài nguyên vẫn thuộc quyền sở hữu của các dự án gốc và chỉ được tái tạo khi giấy phép cho phép.</sub>

<sub>Tạo bởi · `render.py` · 2026-09-19T08:12:36+08:00</sub>
