<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>ดัชนี Jev ที่จัดเกรดตามหลักฐาน และสร้างตัวเองใหม่ทุกสองชั่วโมง</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-488-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <b>ไทย</b> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **ดัชนีสด** · ซิงค์ล่าสุด: `2026-09-19T10:20:34+08:00` (UTC+8)
> · รายการ: **488** · ใหม่ในรอบนี้: **71** · ภาษาที่ใช้พัฒนา: **28**

<sub>ทุกรายการด้านล่างถูกรวบรวม กรอง และตรวจซ้ำโดยไปป์ไลน์ในรีโพซิทอรีนี้ ตัวเลขและเวลาประทับมาจากแหล่งข้อมูล ไม่ใช่จากสแนปช็อตที่เขียนด้วยมือ</sub>

## สารบัญ

- [Jev คืออะไร?](#jev-คออะไร)
- [การจัดเกรดรายการ](#การจดเกรดรายการ)
- [SDK ทางการและเครื่องมือสำหรับนักพัฒนา](#sdk-ทางการและเครองมอสำหรบนกพฒนา) — **6**
- [ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน](#ไคลเอนต-sdk-และอะแดปเตอรจากชมชน) — **74**
- [เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด](#เครองมอสำหรบเอเจนต-mcp-ฮก-เกต-และเอเจนตเขยนโคด) — **144**
- [การจัดเส้นทาง การ์ดเรล และการอนุมัติ](#การจดเสนทาง-การดเรล-และการอนมต) — **48**
- [การประเมิน การคาลิเบรต และเบนช์มาร์ก](#การประเมน-การคาลเบรต-และเบนชมารก) — **39**
- [งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม](#งานจำลองแบบเปด-เวต-และงานวจยสถาปตยกรรม) — **19**
- [แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ](#แอปพลเคชน-เกม-หนยนต-และเดโมแบบโตตอบ) — **42**
- [บทความ การสนทนา และรายการที่เกี่ยวข้อง](#บทความ-การสนทนา-และรายการทเกยวของ) — **116**
- [โปรเจกต์ตามภาษาที่ใช้พัฒนา](#โปรเจกตตามภาษาทใชพฒนา)
- [รายการนี้เป็นปัจจุบันได้อย่างไร](#รายการนเปนปจจบนไดอยางไร)

## Jev คืออะไร?

Jev คือ **System One model** ตัวแรกของ TypeSafe AI มันไม่เขียนข้อความบรรยาย แต่รับสถานะพร้อมคำถามที่คุณกำหนดชุดคำตอบไว้ล่วงหน้า แล้วคืนค่าแบบมีชนิดพร้อมการแจกแจงความน่าจะเป็นที่โค้ดของคุณใช้แยกทางได้

|                     |                                                                                                                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **รูปแบบ**          | `state + typed questions` → `constrained answers + probabilities` → `your code`                                                                                                     |
| **พื้นฐาน**         | `Choice` (เลือกหนึ่งในไม่เกิน 255 ตัวเลือก), `Score` (รูบริก 2–10), `Noul` (ใช่/ไม่ใช่ เชิงความน่าจะเป็น)                                                                           |
| **เอนด์พอยต์**      | `POST https://api.typesafe.ai/v1/systemone`, โมเดล `jev-1.13.0` / นามแฝง `jev-latest`                                                                                               |
| **เหมาะกับ**        | การจัดเส้นทาง การคัดแยก การให้คะแนน การกลั่นกรอง การตรวจสอบ และเกตความหน่วงต่ำภายในเวิร์กโฟลว์ที่มีขอบเขต                                                                           |
| **ข้อจำกัดที่ทราบ** | การนับไม่น่าเชื่อถือ การอ้างอิงหลายชั้นยังอ่อน และเอกสารทางการระบุความขรุขระไว้เก้าประเภท เอาต์พุตที่ถูกต้องตามสคีมาไม่เท่ากับการตัดสินใจที่ถูกต้อง — ควรคาลิเบรตกับข้อมูลของคุณเอง |

## การจัดเกรดรายการ

รายการส่วนใหญ่ในสายนี้อ้างว่าทุกรายการถูกรวมไว้ ที่นี่บอกว่าตรวจสอบได้จริงมากแค่ไหน แล้วให้คุณกรองตามนั้น

| เกรด         | ความหมาย                                                                                                                    |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `official`   | เผยแพร่โดย TypeSafe AI เอง                                                                                                  |
| `observed`   | ชิ้นงานสาธารณะที่เปิดอ่านได้ — ซอร์สโค้ดจริง คอนฟิกจริง หรือการประกาศ TypeSafe/Jev อย่างชัดเจนในชื่อหรือหัวข้อของรีโพซิทอรี |
| `inferred`   | จับคู่ได้จากสัญญาณที่คลุมเครือบวกคำศัพท์ที่สอดคล้องกัน แต่ยังไม่ได้อ่านทีละบรรทัด                                           |
| `unverified` | ดูเกี่ยวข้อง แต่ยังไม่มีอะไรยืนยันได้อย่างอิสระ ขึ้นรายการไว้เพื่อการค้นพบเท่านั้น                                          |

<a id="official-sdk"></a>

## SDK ทางการและเครื่องมือสำหรับนักพัฒนา

ทุกอย่างที่ TypeSafe เผยแพร่เอง เริ่มจากตรงนี้

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐285 · official · 6 天 · ⭐+24</summary>

##### ข้อมูลพื้นฐาน

`SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · MIT · typesafe-ai

##### ข้อมูล

ดาว **285** (+24) · ฟอร์ก 17 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-08-24 · push ล่าสุด 2026-09-12 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐134 · TypeScript · official · 3 天 · ⭐+6</summary>

##### ข้อมูลพื้นฐาน

`SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · TypeScript · MIT · typesafe-ai

##### ข้อมูล

ดาว **134** (+6) · ฟอร์ก 10 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2026-09-04 · push ล่าสุด 2026-09-15 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐124 · Python · official · 0 天 · ⭐+3</summary>

##### ข้อมูลพื้นฐาน

`SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · Python · MIT · typesafe-ai

##### ข้อมูล

ดาว **124** (+3) · ฟอร์ก 13 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-08-08 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>พบการใช้งานในโค้ด: `README.md`, `src/system_one_adapter/__init__.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐92 · Python · official · 0 天 · ⭐+8</summary>

##### ข้อมูลพื้นฐาน

`SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · Python · MIT · typesafe-ai

##### ข้อมูล

ดาว **92** (+8) · ฟอร์ก 9 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-04 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>พบการใช้งานในโค้ด: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 106 天</summary>

##### ข้อมูลพื้นฐาน

`SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · HTML · typesafe-ai

##### ข้อมูล

ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2024-05-28 · push ล่าสุด 2026-06-04 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/TypeSafeAI/clarity-judge">TypeSafeAI/clarity-judge</a></b> — ⭐1 · TypeScript · official · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · TypeScript · TypeSafeAI

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Multi-axis writing quality checker powered by TypeSafe AI's Jev model. Separate named checks, each with its own verdict and confidence.

</details>

<a id="community-sdk"></a>

## ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน

ไคลเอนต์แบบมีชนิดสำหรับเอนด์พอยต์ System One ครอบคลุมภาษาต่าง ๆ เท่าที่ชุมชนทำไปถึง

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐20 · Jupyter · observed · 0 天 · ⭐+3</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Jupyter · MIT · jexp

##### ข้อมูล

ดาว **20** (+3) · ฟอร์ก 5 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐3 · Rust · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Rust · MIT · AkashPriyadarshii

##### ข้อมูล

ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/ckaraca/awesome-jev">ckaraca/awesome-jev</a></b> — ⭐3 · Python · observed · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Python · CC0-1.0 · ckaraca

##### ข้อมูล

ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A curated list of tools, integrations, and experiments built on Jev, TypeSafe AI's System One model for fast, typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — ⭐3 · Java · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Java · MIT · Premo-Cloud

##### ข้อมูล

ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · TypeScript · MIT · AntonioCoppe

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Python · CC0-1.0 · MrJev

##### ข้อมูล

ดาว **2** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐2 · Elixir · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Elixir · MIT · nshkrdotcom

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · TypeScript · opaielsheikh

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Python · xingwudao

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · JavaScript · MIT · ziyu

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/gpazo/jev-vphone-cli">gpazo/jev-vphone-cli</a></b> — Swift · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Swift · MIT · gpazo

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Jev from Typesafe.ai + vphone-cli

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gpazo--jev-vphone-cli/baa413a8104308f4.jpg" width="100%" alt="gpazo/jev-vphone-cli screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Ruby · MIT · javiergradiche

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · TypeScript · MIT · nu-sync

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/RadixILS-Dev/typesafe-sdk-go">RadixILS-Dev/typesafe-sdk-go</a></b> — Go · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Go · MIT · RadixILS-Dev

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A typesafe.ai client written in golang

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Elixir · MIT · typesend

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐169 · Shell · inferred · 0 天 · ⭐+5</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Shell · NOASSERTION · realZachi

##### ข้อมูล

ดาว **169** (+5) · ฟอร์ก 10 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pinecone-io/cultivar">pinecone-io/cultivar</a></b> — ⭐39 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · pinecone-io

##### ข้อมูล

ดาว **39** · ฟอร์ก 2 · issue ที่เปิดอยู่ 5 · สร้างเมื่อ 2026-06-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐32 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · nidhi-singh02

##### ข้อมูล

ดาว **32** (+1) · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">รับชมบน img.youtube.com</a> · การเล่นจะเปิดบนเว็บไซต์ต้นทาง GitHub ไม่สามารถฝังแบบอินไลน์ได้</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/tacticocc/Jevbridge">tacticocc/Jevbridge</a></b> — ⭐17 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · tacticocc

##### ข้อมูล

ดาว **17** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tacticocc--jevbridge/772995670b3e42e9.png" width="100%" alt="tacticocc/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐14 · Python · inferred · 0 天 · ⭐+4</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · AboveColin

##### ข้อมูล

ดาว **14** (+4) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Ask your house a question, get a number back. Home Assistant integration for TypeSafe Jev: typed answers as sensors, four actions for automations, and a conversation agent for Assist.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abovecolin--ha-jev/87fa9143f6990ef1.png" width="100%" alt="AboveColin/HA-Jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐13 · Elixir · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Elixir · MIT · dannote

##### ข้อมูล

ดาว **13** (+1) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐13 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · shiftynick

##### ข้อมูล

ดาว **13** · ฟอร์ก 1 · issue ที่เปิดอยู่ 4 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shiftynick--jev-axi/e97a8238f41de3c1.gif" width="100%" alt="shiftynick/jev-axi screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shiftynick--jev-axi/e97a8238f41de3c1.gif" width="100%" alt="shiftynick/jev-axi animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐12 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · MIT · Ying-Kai-Liao

##### ข้อมูล

ดาว **12** (+1) · ฟอร์ก 3 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/keltokhy/jgrep">keltokhy/jgrep</a></b> — ⭐7 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · keltokhy

##### ข้อมูล

ดาว **7** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.

</details>

<details>
<summary><b><a href="https://github.com/arunav25/jev-mcp">arunav25/jev-mcp</a></b> — ⭐5 · JavaScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · MIT · arunav25

##### ข้อมูล

ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.

</details>

<details>
<summary><b><a href="https://github.com/Nasrallah-AL/jev-cli">Nasrallah-AL/jev-cli</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · Nasrallah-AL

##### ข้อมูล

ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Command-line tool for TypeSafe's Jev AI model

</details>

<details>
<summary><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">saibimajdi/typesafeai-dotnet-sdk</a></b> — ⭐5 · C# · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · C# · MIT · saibimajdi

##### ข้อมูล

ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/sharziki/semdecide">sharziki/semdecide</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · sharziki

##### ข้อมูล

ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.

</details>

<details>
<summary><b><a href="https://github.com/frostney/clean-code-review">frostney/clean-code-review</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · frostney

##### ข้อมูล

ดาว **4** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/frostney--clean-code-review/7d8a8de446e1c27b.png" width="100%" alt="frostney/clean-code-review screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rhighs/jev-code">rhighs/jev-code</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · rhighs

##### ข้อมูล

ดาว **4** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/assets/jev-code-logo.png" width="100%" alt="rhighs/jev-code screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/docs/media/session.gif" width="100%" alt="rhighs/jev-code animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/romaluev/jev-ego">romaluev/jev-ego</a></b> — ⭐4 · TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · NOASSERTION · romaluev

##### ข้อมูล

ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-seo">AkashPriyadarshii/jev-seo</a></b> — ⭐3 · Rust · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Rust · AkashPriyadarshii

##### ข้อมูล

ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One

</details>

<details>
<summary><b><a href="https://github.com/docxology/daf-jev">docxology/daf-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · docxology

##### ข้อมูล

ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill

</details>

<details>
<summary><b><a href="https://github.com/EugeneBoondock/jevsql">EugeneBoondock/jevsql</a></b> — ⭐3 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · MIT · EugeneBoondock

##### ข้อมูล

ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

SQL with natural-language predicates, powered by TypeSafe's Jev. Filter, rank, classify and score rows by meaning — batched, cached and cost-guarded.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/eugeneboondock--jevsql/d6bbe6cf6a2d2e8c.png" width="100%" alt="EugeneBoondock/jevsql screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Olti1947/jev-java">Olti1947/jev-java</a></b> — ⭐3 · Java · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Java · Olti1947

##### ข้อมูล

ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 8 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Idiomatic Java SDK for TypeSafe AI Jev System One decision engine

</details>

<details>
<summary><b><a href="https://github.com/burnigtm/jev-mcp">burnigtm/jev-mcp</a></b> — ⭐2 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · burnigtm

##### ข้อมูล

ดาว **2** (+1) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client

</details>

<details>
<summary><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Butochnikov/laravel-typesafe-jev</a></b> — ⭐2 · PHP · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · PHP · MIT · Butochnikov

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes.

</details>

<details>
<summary><b><a href="https://github.com/ddfeyes/jev-mode">ddfeyes/jev-mode</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · ddfeyes

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

I kept watching coding agents burn context on decisions that aren't hard - triage 400 tickets, tag 600 files, route to one of six teams. jev-mode moves those verdicts to a typed-judgment model. I A/B'd it: 78% fewer tokens, 16x less work-attributable input, accuracy 96.1% vs 93.7%. Python, no deps, MIT.

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-go">Gaurav-Gosain/jev-go</a></b> — ⭐2 · Go · inferred · 2 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · Gaurav-Gosain

##### ข้อมูล

ดาว **2** (+1) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/ibrahemid/git-jev-stage">ibrahemid/git-jev-stage</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · ibrahemid

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Select Git changes for staging with a plain-language description.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ibrahemid--git-jev-stage/f8c136a32610d69a.gif" width="100%" alt="ibrahemid/git-jev-stage animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Stumble/jev-go">Stumble/jev-go</a></b> — ⭐2 · Go · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · Stumble

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Community Go SDK for TypeSafe AI Jev / System One

</details>

<details>
<summary><b><a href="https://github.com/tontoko/jev-browser">tontoko/jev-browser</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · Apache-2.0 · tontoko

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.

</details>

<details>
<summary><b><a href="https://github.com/tumf/jev-cli">tumf/jev-cli</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · tumf

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Small dependency-free CLI for TypeSafe Jev

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tumf--jev-cli/f90f005044872607.png" width="100%" alt="tumf/jev-cli screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tumf--jev-cli/f69b319352312892.gif" width="100%" alt="tumf/jev-cli animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://raw.githubusercontent.com/tumf/jev-cli/main/assets/jev-cli-terminal-demo.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/yzfly/awesome-jev-zh">yzfly/awesome-jev-zh</a></b> — ⭐2 · HTML · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · HTML · CC0-1.0 · yzfly

##### ข้อมูล

ดาว **2** · ฟอร์ก 3 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/jevclient">AboveColin/jevclient</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · AboveColin

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-scout">AkashPriyadarshii/jev-scout</a></b> — ⭐1 · Rust · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Rust · MIT · AkashPriyadarshii

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring

</details>

<details>
<summary><b><a href="https://github.com/anilsenay/jev">anilsenay/jev</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · anilsenay

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Unofficial Go client for TypeSafe's System One API  and its model, Jev.

</details>

<details>
<summary><b><a href="https://github.com/felpsdev/jev-classifier">felpsdev/jev-classifier</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · felpsdev

##### ข้อมูล

ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/felpsdev--jev-classifier/d753de26b0e6c7b6.webp" width="100%" alt="felpsdev/jev-classifier screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gmaxxxie/jev-cli">gmaxxxie/jev-cli</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · gmaxxxie

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/himomohi/aside-jev">himomohi/aside-jev</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · himomohi

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.

</details>

<details>
<summary><b><a href="https://github.com/StefanoITA/ts-jev-cost-calculator">StefanoITA/ts-jev-cost-calculator</a></b> — ⭐1 · Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · StefanoITA

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe.

</details>

<details>
<summary><b><a href="https://github.com/zhirschtritt/typesafe-go">zhirschtritt/typesafe-go</a></b> — ⭐1 · Go · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · zhirschtritt

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Idiomatic Go SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/33Audits/jev-auto">33Audits/jev-auto</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · MIT · 33Audits

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Per-turn model routing for Claude Code. Cheapest tier that can do the job, no API key required, and it calibrates itself from what actually happened.

</details>

<details>
<summary><b><a href="https://github.com/acharyaanusha/magic-jev">acharyaanusha/magic-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · acharyaanusha

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A Magic Jev (8) Ball for pull requests.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/acharyaanusha--magic-jev/f58dfd5f54b0ae6c.gif" width="100%" alt="acharyaanusha/magic-jev animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">AkashPriyadarshii/jev-superpowers</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · MIT · AkashPriyadarshii

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions

</details>

<details>
<summary><b><a href="https://github.com/brnyxx/jev-ra">brnyxx/jev-ra</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · brnyxx

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7592fce4641d10.png" width="100%" alt="brnyxx/jev-ra screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7ddcd1053825a2.gif" width="100%" alt="brnyxx/jev-ra animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/david1gp/jev">david1gp/jev</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · david1gp

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Result-based TypeSafe System One client library and jev command-line interface.

</details>

<details>
<summary><b><a href="https://github.com/egma-ai/jev-reviewer">egma-ai/jev-reviewer</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · MIT · egma-ai

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Review behavior, not just diffs. Jev prioritizes human attention; OpenAI explains the changes. Local CLI + agent skill + GitHub extension.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/egma-ai--jev-reviewer/db97b1dd85958e4d.png" width="100%" alt="egma-ai/jev-reviewer screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/krw82/jev-playwright-mcp">krw82/jev-playwright-mcp</a></b> — TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · krw82

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.

</details>

<details>
<summary><b><a href="https://github.com/Kushwho/jev-codes">Kushwho/jev-codes</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · Kushwho

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Audit your git diff against YAML coding-standards packs using TypeSafe's Jev model, from a CLI or your AI agent's command/skill.

</details>

<details>
<summary><b><a href="https://github.com/lhotwll217/jev-cli">lhotwll217/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · lhotwll217

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

JSON-in, typed-decisions-out CLI for the TypeSafe System One API

</details>

<details>
<summary><b><a href="https://github.com/mhmdkzr/jev">mhmdkzr/jev</a></b> — Go · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · mhmdkzr

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

An unofficial Go client for TypeSafe's System One Jev model

</details>

<details>
<summary><b><a href="https://github.com/model-clis/jev">model-clis/jev</a></b> — Rust · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Rust · MIT · model-clis

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Typed judgment CLI for the Jev model (TypeSafe System One): state + questions in, calibrated answers and exit codes out

</details>

<details>
<summary><b><a href="https://github.com/nandansrikrishna/jev-agent-tool">nandansrikrishna/jev-agent-tool</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · nandansrikrishna

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Bring-your-own-key CLI, Python API, and MCP server for typed judgments with TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing">nekowasabi/jev-routing</a></b> — Go · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · nekowasabi

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.

</details>

<details>
<summary><b><a href="https://github.com/SAGAR-TAMANG/sarvam-jev">SAGAR-TAMANG/sarvam-jev</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · SAGAR-TAMANG

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Generation-free typed decisions on Indic LLMs. An open Jev-style inference engine on sarvam-1: constrained logit readout instead of autoregressive JSON. Runs client-side in the browser.

</details>

<details>
<summary><b><a href="https://github.com/yannip1234/codex-jev">yannip1234/codex-jev</a></b> — Rust · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Rust · Apache-2.0 · yannip1234

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 11 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Experimental Jev compression for Codex, with a macOS menu bar launcher, desktop bridge, and native client.

</details>

<details>
<summary><b><a href="https://github.com/giuliosmall/pg_typesafe">giuliosmall/pg_typesafe</a></b> — ⭐76 · C · unverified · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · C · MIT · giuliosmall

##### ข้อมูล

ดาว **76** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification

</details>

<details>
<summary><b><a href="https://github.com/pithings/advocaat">pithings/advocaat</a></b> — ⭐74 · TypeScript · unverified · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · TypeScript · MIT · pithings

##### ข้อมูล

ดาว **74** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/obie/ruby_decision_model">obie/ruby_decision_model</a></b> — ⭐34 · Ruby · unverified · 0 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · Ruby · MIT · obie

##### ข้อมูล

ดาว **34** (+2) · ฟอร์ก 2 · issue ที่เปิดอยู่ 18 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Ruby client for decision models such as Typesafe Jev

</details>

<details>
<summary><b><a href="https://github.com/Brainwires/jevwire">Brainwires/jevwire</a></b> — ⭐5 · TypeScript · unverified · 0 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · TypeScript · MIT · Brainwires

##### ข้อมูล

ดาว **5** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/typesafe-cli">y0usaf/typesafe-cli</a></b> — ⭐4 · TypeScript · unverified · 2 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · TypeScript · MIT · y0usaf

##### ข้อมูล

ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose

</details>

<details>
<summary><b><a href="https://github.com/geilt/typesafe-cli">geilt/typesafe-cli</a></b> — ⭐3 · Python · unverified · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · Python · geilt

##### ข้อมูล

ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.

</details>

<details>
<summary><b><a href="https://github.com/gilljon/typesafe-ai-rs">gilljon/typesafe-ai-rs</a></b> — ⭐3 · Rust · unverified · 1 天</summary>

##### ข้อมูลพื้นฐาน

`ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · Rust · MIT · gilljon

##### ข้อมูล

ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Independent async and blocking Rust SDK for the TypeSafe AI System One API

</details>

<a id="agent-tooling"></a>

## เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด

หมวดที่โตเร็วที่สุด: ฮุก เซิร์ฟเวอร์ MCP และเกตที่วางการตัดสินใจแบบมีชนิดไว้หน้าการกระทำถัดไปของเอเจนต์

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐3310 · TypeScript · observed · 0 天 · ⭐+114</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · MIT · tamaratran

##### ข้อมูล

ดาว **3310** (+114) · ฟอร์ก 166 · issue ที่เปิดอยู่ 45 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>พบการใช้งานในโค้ด: `src/request.ts`, `README.md`, `src/client.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐144 · JavaScript · inferred · 0 天 · ⭐+6</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · gargpratyush

##### ข้อมูล

ดาว **144** (+6) · ฟอร์ก 5 · issue ที่เปิดอยู่ 5 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐46 · Python · inferred · 1 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · 0xNatoshi

##### ข้อมูล

ดาว **46** (+2) · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐104 · observed · 1 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · dbreunig

##### ข้อมูล

ดาว **104** (+1) · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐17 · Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · GhalebDweikat

##### ข้อมูล

ดาว **17** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/valentynkit/awesome-jev-typesafe">valentynkit/awesome-jev-typesafe</a></b> — ⭐8 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · CC0-1.0 · valentynkit

##### ข้อมูล

ดาว **8** · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Typed decisions with TypeSafe's Jev, the first System One model

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · carlaiau

##### ข้อมูล

ดาว **7** · ฟอร์ก 1 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2026-03-13 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/kraayenjon/awesome-jev">kraayenjon/awesome-jev</a></b> — ⭐6 · observed · 0 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · NOASSERTION · kraayenjon

##### ข้อมูล

ดาว **6** (+2) · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · jodan-alberts

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/rajdhakad9826/routeKit">rajdhakad9826/routeKit</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · MIT · rajdhakad9826

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Agent-native LLM model router built with JEV by TypeSafe.ai. Dynamically selects the most suitable model based on task complexity, reasoning requirements, and tool usage.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · MIT · BYK

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/emirbartu/opencode-system-one">emirbartu/opencode-system-one</a></b> — ⭐1 · TypeScript · observed · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · emirbartu

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Opencode plugin using Jev (system one model) as part of software development process. Not affiliated with Opencode team.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · 24601

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/codaaiteam/jev-typesafe-ai">codaaiteam/jev-typesafe-ai</a></b> — observed · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · codaaiteam

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Unofficial developer notes & examples for Jev, TypeSafe AI's System One model. Try it free: jevtypesafeai.com

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · CrowBe

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · MIT · gorock007

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/uipath-jev-guardrail-connector">jms-dcksn/uipath-jev-guardrail-connector</a></b> — JavaScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · JavaScript · jms-dcksn

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

UiPath bring-your-own-guardrail connector backed by the TypeSafe Jev System One model: plain-language agent policies enforced as calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/knowlet/jev-agentworld-web-simulator">knowlet/jev-agentworld-web-simulator</a></b> — TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · MIT · knowlet

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

An entire internet — search, pages & links — hallucinated on the fly by the System One Model.

</details>

<details>
<summary><b><a href="https://github.com/Wany-i/jev-decision-layer">Wany-i/jev-decision-layer</a></b> — Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · Wany-i

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

把决策模型（typesafe/jev-1.13，经 OpenRouter 的 decisions 端点调用）封装成业务决策工具：注册表驱动，带置信度门控与硬约束。非官方项目。

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · yousudip

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐275 · TypeScript · inferred · 2 天 · ⭐+8</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · devagrawal09

##### ข้อมูล

ดาว **275** (+8) · ฟอร์ก 14 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐123 · TypeScript · inferred · 1 天 · ⭐+4</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · NiazMorshed2007

##### ข้อมูล

ดาว **123** (+4) · ฟอร์ก 9 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐120 · JavaScript · inferred · 0 天 · ⭐+11</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · fatwang2

##### ข้อมูล

ดาว **120** (+11) · ฟอร์ก 14 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/wy-coliney/jev-browser-use">wy-coliney/jev-browser-use</a></b> — ⭐109 · JavaScript · inferred · 0 天 · ⭐+15</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · wy-coliney

##### ข้อมูล

ดาว **109** (+15) · ฟอร์ก 4 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wy-coliney--jev-browser-use/581fbd89fe47c952.png" width="100%" alt="wy-coliney/jev-browser-use screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-eval-agent">vinilana/jev-eval-agent</a></b> — ⭐86 · HTML · inferred · 1 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · HTML · vinilana

##### ข้อมูล

ดาว **86** (+2) · ฟอร์ก 8 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-mcp">jkudish/jev-mcp</a></b> — ⭐73 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · jkudish

##### ข้อมูล

ดาว **73** · ฟอร์ก 10 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Fast, cheap, typed judgments from TypeSafe's Jev model, as MCP tools.

> An early proof of concept for exposing Jev over MCP, which is how most non-Python toolchains reach it.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/pi-jev">y0usaf/pi-jev</a></b> — ⭐68 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · y0usaf

##### ข้อมูล

ดาว **68** (+1) · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers

</details>

<details>
<summary><b><a href="https://github.com/RomanSlack/jev-drone">RomanSlack/jev-drone</a></b> — ⭐63 · Python · inferred · 2 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · RomanSlack

##### ข้อมูล

ดาว **63** (+2) · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/romanslack--jev-drone/b23ea2412f437970.png" width="100%" alt="RomanSlack/jev-drone screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/supercorp-ai/supercov">supercorp-ai/supercov</a></b> — ⭐35 · Rust · inferred · 0 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Rust · MIT · supercorp-ai

##### ข้อมูล

ดาว **35** (+2) · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-08-23 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Code quality and coverage for coding agents

> Code quality and coverage verdicts produced as typed decisions rather than prose, so the result can gate a pipeline directly.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/supercorp-ai--supercov/063226e150cb8a6b.jpg" width="100%" alt="supercorp-ai/supercov screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/logicrw/awesome-jev-projects">logicrw/awesome-jev-projects</a></b> — ⭐33 · JavaScript · inferred · 0 天 · ⭐+4</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · logicrw

##### ข้อมูล

ดาว **33** (+4) · ฟอร์ก 8 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/ask-jev-skill">shantanugoel/ask-jev-skill</a></b> — ⭐30 · Python · inferred · 1 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · shantanugoel

##### ข้อมูล

ดาว **30** (+1) · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Skill for Hermes, and other agents, to ask typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/tamaratran/jev-pruner">tamaratran/jev-pruner</a></b> — ⭐15 · TypeScript · inferred · 0 天 · ⭐+5</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · tamaratran

##### ข้อมูล

ดาว **15** (+5) · ฟอร์ก 1 · issue ที่เปิดอยู่ 7 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Claude Code plugin: trim long Bash output with TypeSafe Jev before the model sees it

</details>

<details>
<summary><b><a href="https://github.com/DanRWilloughby/snifftest">DanRWilloughby/snifftest</a></b> — ⭐14 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · DanRWilloughby

##### ข้อมูล

ดาว **14** · ฟอร์ก 0 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/danrwilloughby--snifftest/39b2a26b93d5f1ec.gif" width="100%" alt="DanRWilloughby/snifftest animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/TheoOliveira/pi-jev">TheoOliveira/pi-jev</a></b> — ⭐14 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · TheoOliveira

##### ข้อมูล

ดาว **14** (+1) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/kbhuw/jev-sift">kbhuw/jev-sift</a></b> — ⭐13 · JavaScript · inferred · 0 天 · ⭐+9</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · kbhuw

##### ข้อมูล

ดาว **13** (+9) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification.

</details>

<details>
<summary><b><a href="https://github.com/compozy/yoshi">compozy/yoshi</a></b> — ⭐12 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · compozy

##### ข้อมูล

ดาว **12** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/compozy--yoshi/637d8588c227f4de.png" width="100%" alt="compozy/yoshi screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">jomatsu/pi-jev-auto-mode</a></b> — ⭐12 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · jomatsu

##### ข้อมูล

ดาว **12** (+1) · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.

</details>

<details>
<summary><b><a href="https://github.com/BillionsBobby/JevRouter">BillionsBobby/JevRouter</a></b> — ⭐11 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · BillionsBobby

##### ข้อมูล

ดาว **11** (+4) · ฟอร์ก 1 · issue ที่เปิดอยู่ 4 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A lightweight Jev-powered router for models, tools, and subagents

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/billionsbobby--jevrouter/f0e638219505d5da.png" width="100%" alt="BillionsBobby/JevRouter screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/blakestone-x/jev-mcp">blakestone-x/jev-mcp</a></b> — ⭐9 · Python · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · blakestone-x

##### ข้อมูล

ดาว **9** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer

</details>

<details>
<summary><b><a href="https://github.com/huntedman/JevLint">huntedman/JevLint</a></b> — ⭐9 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · huntedman

##### ข้อมูล

ดาว **9** (+1) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.

</details>

<details>
<summary><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">DECRUX9812/typesafe-skill-router</a></b> — ⭐7 · Python · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · DECRUX9812

##### ข้อมูล

ดาว **7** · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-code">devagrawal09/jev-code</a></b> — ⭐6 · TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · devagrawal09

##### ข้อมูล

ดาว **6** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Bounded TypeSafe Jev workflows for coding agents.

</details>

<details>
<summary><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">GodsBoy/jev-agent-skill-router</a></b> — ⭐5 · Python · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · GodsBoy

##### ข้อมูล

ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typed, confidence-aware agent skill routing with TypeSafe Jev.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/godsboy--jev-agent-skill-router/c80293e37dcd4faf.png" width="100%" alt="GodsBoy/jev-agent-skill-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/inanna-malick/jev-dsl">inanna-malick/jev-dsl</a></b> — ⭐5 · Haskell · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Haskell · MIT · inanna-malick

##### ข้อมูล

ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels

</details>

<details>
<summary><b><a href="https://github.com/matthewp/flue-jev-demo">matthewp/flue-jev-demo</a></b> — ⭐5 · TypeScript · inferred · 0 天 · ⭐+3</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · matthewp

##### ข้อมูล

ดาว **5** (+3) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Flue agent routing with TypeSafe Jev through Cloudflare AI Gateway

</details>

<details>
<summary><b><a href="https://github.com/anpicasso/hermes-jev-approvals">anpicasso/hermes-jev-approvals</a></b> — ⭐4 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · anpicasso

##### ข้อมูล

ดาว **4** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only.

</details>

<details>
<summary><b><a href="https://github.com/GiesN/typesafe-jev-workflow">GiesN/typesafe-jev-workflow</a></b> — ⭐4 · Python · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · GiesN

##### ข้อมูล

ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/runta-dev/jot">runta-dev/jot</a></b> — ⭐4 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · runta-dev

##### ข้อมูล

ดาว **4** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

The first general-purpose System One agent for Jev

</details>

<details>
<summary><b><a href="https://github.com/anandi1989/awesome-jev-usecases">anandi1989/awesome-jev-usecases</a></b> — ⭐3 · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · MIT · anandi1989

##### ข้อมูล

ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-mcp">rashedInt32/jev-mcp</a></b> — ⭐3 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · rashedInt32

##### ข้อมูล

ดาว **3** (+1) · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/SeeAPI/awesome-jev-use-cases">SeeAPI/awesome-jev-use-cases</a></b> — ⭐3 · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · CC-BY-4.0 · SeeAPI

##### ข้อมูล

ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-align">caiovicentino/jev-align</a></b> — ⭐2 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · caiovicentino

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Calibrated alignment verifier for LLM responses and agent plans — powered by Jev

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-shield">caiovicentino/jev-shield</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · caiovicentino

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check.

</details>

<details>
<summary><b><a href="https://github.com/doeixd/jev-pref">doeixd/jev-pref</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · doeixd

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/doeixd--jev-pref/ddb9009a54eedbbd.gif" width="100%" alt="doeixd/jev-pref animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-model-router-demo">jcpsimmons/jev-model-router-demo</a></b> — ⭐2 · JavaScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · jcpsimmons

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

</details>

<details>
<summary><b><a href="https://github.com/molis-ai/jev-workbench">molis-ai/jev-workbench</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · molis-ai

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/molis-ai--jev-workbench/00f61d8403a941cd.png" width="100%" alt="molis-ai/jev-workbench screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MongLong0214/jev-gate">MongLong0214/jev-gate</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MongLong0214

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 5 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.

</details>

<details>
<summary><b><a href="https://github.com/morcoan/JevSeek">morcoan/JevSeek</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · morcoan

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools, persistent sessions, React desktop, and documented research.

</details>

<details>
<summary><b><a href="https://github.com/noetion/dsh-jev">noetion/dsh-jev</a></b> — ⭐2 · TypeScript · inferred · 1 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · noetion

##### ข้อมูล

ดาว **2** (+1) · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.

</details>

<details>
<summary><b><a href="https://github.com/ranjan2829/AskJev">ranjan2829/AskJev</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · ranjan2829

##### ข้อมูล

ดาว **2** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)

</details>

<details>
<summary><b><a href="https://github.com/samtay32/jev-system-architect">samtay32/jev-system-architect</a></b> — ⭐2 · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · MIT · samtay32

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives.

</details>

<details>
<summary><b><a href="https://github.com/Zaious/jev-capability-atlas">Zaious/jev-capability-atlas</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · NOASSERTION · Zaious

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Independent, evidence-based map of when TypeSafe's Jev actually holds up vs. breaks down — real API-call receipts, not a leaderboard. 中文為主的雙語 repo。

</details>

<details>
<summary><b><a href="https://github.com/abhishekashokvkumar/jev-mcp-dispatcher">abhishekashokvkumar/jev-mcp-dispatcher</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · abhishekashokvkumar

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Natural-language MCP tool dispatcher powered entirely by TypeSafe's Jev — no general-purpose LLM. Discovers a simple MCP server's tool signatures at runtime and uses Jev's typed primitives (Choice/Noul) to pick the right tool and extract its arguments straight out of the sentence.

</details>

<details>
<summary><b><a href="https://github.com/bestagentkits/jev-skillful">bestagentkits/jev-skillful</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · bestagentkits

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.

</details>

<details>
<summary><b><a href="https://github.com/cephalization/jev-oxlint">cephalization/jev-oxlint</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · cephalization

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Digest your skills into oxlint rules powered by jev

</details>

<details>
<summary><b><a href="https://github.com/CrowdLinker/JevPromptCoach">CrowdLinker/JevPromptCoach</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · CrowdLinker

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Claude Code plugin that scores how well you prompt a coding agent, and shows whether your habits are improving. Runs on TypeSafe's Jev model. Zero added latency.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/crowdlinker--jevpromptcoach/5340815130cd47ba.png" width="100%" alt="CrowdLinker/JevPromptCoach screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Dharundp6/jev-carryforward">Dharundp6/jev-carryforward</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · Dharundp6

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written as things happen, recalled per task with TypeSafe's Jev evaluation model via Vercel AI Gateway.

</details>

<details>
<summary><b><a href="https://github.com/Friedjof/jev-mobile">Friedjof/jev-mobile</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · Friedjof

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Fast structured Android control loops with TypeSafe Jev and Mobile MCP

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-starter">hamakyo/jev-starter</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · hamakyo

##### ข้อมูล

ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-codex-plugin">integrate-your-mind/jev-codex-plugin</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · integrate-your-mind

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Open-source Codex plugin for TypeSafe Jev decision consultation, failure diagnosis, and evidence-based completion review

</details>

<details>
<summary><b><a href="https://github.com/jcressler/fast-jev-compaction-codex">jcressler/fast-jev-compaction-codex</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · jcressler

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Task-aware Jev evidence selection and exact local recovery around native Codex compaction.

</details>

<details>
<summary><b><a href="https://github.com/khordoo/jev-reflex-autonomy-lab">khordoo/jev-reflex-autonomy-lab</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · khordoo

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/khordoo/jev-reflex-autonomy-lab/main/docs/media/reflex-dashboard.png" width="100%" alt="khordoo/jev-reflex-autonomy-lab screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/omni-/ask-jev">omni-/ask-jev</a></b> — ⭐1 · PowerShell · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · PowerShell · MIT · omni-

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions.

</details>

<details>
<summary><b><a href="https://github.com/poponline63/hermes-jev-north-star">poponline63/hermes-jev-north-star</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · poponline63

##### ข้อมูล

ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven.

</details>

<details>
<summary><b><a href="https://github.com/RahulBalakavi/claude-code-jev">RahulBalakavi/claude-code-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · RahulBalakavi

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Experimental Jev permission gate for Claude Code via OpenRouter, with reproducible latency and cost benchmarks

</details>

<details>
<summary><b><a href="https://github.com/Ravinder82/jev-flash-router">Ravinder82/jev-flash-router</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · Ravinder82

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code

</details>

<details>
<summary><b><a href="https://github.com/rthomas24/jev-realtime-trading">rthomas24/jev-realtime-trading</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · rthomas24

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rthomas24--jev-realtime-trading/f27df5cca6b8e2cf.png" width="100%" alt="rthomas24/jev-realtime-trading screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Saik0s/diffusiongemma-jev-macos">Saik0s/diffusiongemma-jev-macos</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · Saik0s

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Local JEV-style decisions with DiffusionGemma on Apple Silicon, with benchmarks and coding-agent examples.

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/codex-jev-compaction">Wang-auspicious/codex-jev-compaction</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · Wang-auspicious

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills.

</details>

<details>
<summary><b><a href="https://github.com/wotai-dev/typesafe-jev-tools">wotai-dev/typesafe-jev-tools</a></b> — ⭐1 · Shell · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Shell · MIT · wotai-dev

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured 149-row comparison of TypeSafe Jev against Claude Haiku 4.5.

</details>

<details>
<summary><b><a href="https://github.com/altregubov/jev-antigravity-mcp">altregubov/jev-antigravity-mcp</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · altregubov

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/alviso/jev-precheck">alviso/jev-precheck</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · alviso

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A second signature on every write an AI agent makes into a system of record. MCP proxy: fetch the records, derive in code, Jev judges. 98.6% recall, 0 false holds on 288 cases.

</details>

<details>
<summary><b><a href="https://github.com/andyholst/hermes-typesafe-jev">andyholst/hermes-typesafe-jev</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · NOASSERTION · andyholst

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

TypeSafe Jev MCP server for Hermes Agent — Choice, Noul, Score as first-class tools

</details>

<details>
<summary><b><a href="https://github.com/anisselbd/jev-phishing-bench">anisselbd/jev-phishing-bench</a></b> — Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · anisselbd

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/openclaw-jev-harness">AntonioCoppe/openclaw-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · AntonioCoppe

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

OpenClaw plugin: jev-harness DecisionHarness as System One decide layer (policy/confidence/shadow)

</details>

<details>
<summary><b><a href="https://github.com/AStheTECH/mewcp-jev">AStheTECH/mewcp-jev</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · Apache-2.0 · AStheTECH

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

JEV MCP server by MewCP

</details>

<details>
<summary><b><a href="https://github.com/bidurkhatri/jev-mcp-lab">bidurkhatri/jev-mcp-lab</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · Apache-2.0 · bidurkhatri

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/buberlo/dsh-jev">buberlo/dsh-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · buberlo

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Jev-powered decision layer for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/cbruyndoncx/AskJev-MCP">cbruyndoncx/AskJev-MCP</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · cbruyndoncx

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence

</details>

<details>
<summary><b><a href="https://github.com/de-niji/jev-hermes">de-niji/jev-hermes</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · de-niji

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Jev for Hermes: cheap intent gates + verbatim tool compaction on OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/dizk/pi-jev-lens">dizk/pi-jev-lens</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · dizk

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

pi extension that compresses large tool results before they reach the model: jev picks the view, full text stays recallable

</details>

<details>
<summary><b><a href="https://github.com/DoGMaTiiC/hermes-jev">DoGMaTiiC/hermes-jev</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · DoGMaTiiC

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 7 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only.

</details>

<details>
<summary><b><a href="https://github.com/droid-Q/jev-skill-router">droid-Q/jev-skill-router</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · droid-Q

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/droid-Q/jev-skill-router/main/docs/images/dashboard-en.png" width="100%" alt="droid-Q/jev-skill-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/duketopceo/jev-compact">duketopceo/jev-compact</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · duketopceo

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP

</details>

<details>
<summary><b><a href="https://github.com/EtienneLescot/jev-router">EtienneLescot/jev-router</a></b> — HTML · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · HTML · MIT · EtienneLescot

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model tier and reasoning depth.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/etiennelescot--jev-router/96217fad0b128b3e.png" width="100%" alt="EtienneLescot/jev-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fast-facts/jev-mcp">fast-facts/jev-mcp</a></b> — Go · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Go · MIT · fast-facts

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/flaviusapop/jev-router">flaviusapop/jev-router</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · flaviusapop

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Routes each turn in Claude Code, Codex, Grok and opencode to the cheapest model and reasoning depth that can finish it, using TypeSafe Jev

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/flaviusapop--jev-router/b7f868696d35b78b.png" width="100%" alt="flaviusapop/jev-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gzawadzki/jev-usecases">gzawadzki/jev-usecases</a></b> — Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · gzawadzki

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage

</details>

<details>
<summary><b><a href="https://github.com/hangarbay/jev.mcp">hangarbay/jev.mcp</a></b> — Go · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Go · MIT · hangarbay

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/its-panzer/jev-model-router">its-panzer/jev-model-router</a></b> — Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · its-panzer

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A policy router that picks the cheapest Claude model that can finish the job

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/its-panzer--jev-model-router/98819f5aaf8e6373.png" width="100%" alt="its-panzer/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jh1373/jev-search">jh1373/jev-search</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · jh1373

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Search your Obsidian vault locally and offline with no API key, then rerank the top results with Jev only after you approve exactly what gets sent. Experimental preview.

</details>

<details>
<summary><b><a href="https://github.com/jmanhype/jev-dspy-lab">jmanhype/jev-dspy-lab</a></b> — Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · jmanhype

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/jev-pii-guardrail">jms-dcksn/jev-pii-guardrail</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · jms-dcksn

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A UiPath coded agent with a custom PII detection guardrail on the LLM boundary, built on the TypeSafe Jev model as a LangChain awrap_model_call middleware.

</details>

<details>
<summary><b><a href="https://github.com/JoacoMarc/jev-harness-router">JoacoMarc/jev-harness-router</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · JoacoMarc

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Per-turn harness router on Jev (TypeSafe): one batched call picks the model tier, tools, skill and effort budget for an agent turn, behind a hard latency deadline.

</details>

<details>
<summary><b><a href="https://github.com/juanlentino/jev-connector">juanlentino/jev-connector</a></b> — PHP · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · PHP · GPL-2.0 · juanlentino

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

WordPress connector for the TypeSafe System One API (Jev): typed questions, confidence-scored answers, core Connectors API key management

</details>

<details>
<summary><b><a href="https://github.com/jxu-dev-c/jev-adaptive-thinking">jxu-dev-c/jev-adaptive-thinking</a></b> — Go · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Go · jxu-dev-c

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

CLIProxyAPI plugin for Jev-powered session model routing with local debug logs

</details>

<details>
<summary><b><a href="https://github.com/kaijia323/dsh-plugin-jev">kaijia323/dsh-plugin-jev</a></b> — HTML · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · HTML · MIT · kaijia323

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness

</details>

<details>
<summary><b><a href="https://github.com/kerpopule/hermes-jev-skills">kerpopule/hermes-jev-skills</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · kerpopule

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (also Claude Code and Codex)

</details>

<details>
<summary><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">MahmoudAdelbghany/jev-browser</a></b> — JavaScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MahmoudAdelbghany

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included.

</details>

<details>
<summary><b><a href="https://github.com/Mandrilsquad1441/jev-model-router">Mandrilsquad1441/jev-model-router</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · Mandrilsquad1441

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Pick the best AI model and reasoning effort for any task in ~1s. Plugin for Claude Code, Claude Desktop and Codex, powered by TypeSafe's Jev decision model and live OpenRouter pricing. Balance intelligence, speed and cost, or choose your priority.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mandrilsquad1441--jev-model-router/6187e7fb04b04c08.png" width="100%" alt="Mandrilsquad1441/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/marcAllari/jev-mcp-router">marcAllari/jev-mcp-router</a></b> — inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · marcAllari

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/micic-mihajlo/jev-tool-runner">micic-mihajlo/jev-tool-runner</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · micic-mihajlo

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/minhgv/jev-mcp">minhgv/jev-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · minhgv

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe Jev MCP decision layer for coding agents and CI

</details>

<details>
<summary><b><a href="https://github.com/mjyoke1111/jev-agent-safety-arena">mjyoke1111/jev-agent-safety-arena</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · mjyoke1111

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Real browser-agent safety evaluation: Jev versus a baseline on benign and injected tasks

</details>

<details>
<summary><b><a href="https://github.com/MSalvalaggio/jev-reflex">MSalvalaggio/jev-reflex</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · MSalvalaggio

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision).

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-mcp">nekowasabi/jev-routing-mcp</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · nekowasabi

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/Nyarlathoteppppp/pi-jev-context">Nyarlathoteppppp/pi-jev-context</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · Nyarlathoteppppp

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Cache-neutral context trimming for the pi coding agent, powered by TypeSafe Jev: long tool output cut to verbatim key lines before it enters context, with lossless recall. Measured, with pre-registered benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Panebianco00/jev-claude">Panebianco00/jev-claude</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · Panebianco00

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Route Claude Code's coding decisions through TypeSafe Jev: typed choices with probabilities, enforced at plan approval, questions, and risky commands.

</details>

<details>
<summary><b><a href="https://github.com/pedroknigge/mcp_jev">pedroknigge/mcp_jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · pedroknigge

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Open MCP server to run TypeSafe Jev (System One) packs locally — Choice / Noul / Score for Cursor & agents

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-mcp-router">Pinutss/jev-mcp-router</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · Pinutss

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Select relevant MCP tools under a context-token budget, without executing them.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-mcp-router/3947a2a5cc3750c8.png" width="100%" alt="Pinutss/jev-mcp-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-memory-selector">Pinutss/jev-memory-selector</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · Pinutss

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-plugins">Pinutss/jev-plugins</a></b> — inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · MIT · Pinutss

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Cursor and Hermes marketplace for the four published JEV Labs routers.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-plugins/b3fcd72ac9e61f49.jpg" width="100%" alt="Pinutss/jev-plugins screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/planstack-ai/jev-tetris-benchmark">planstack-ai/jev-tetris-benchmark</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · planstack-ai

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Reproducible Tetris decision benchmark comparing TypeSafe Jev with Claude Haiku

</details>

<details>
<summary><b><a href="https://github.com/raj8525/universal-jev">raj8525/universal-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · raj8525

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents

</details>

<details>
<summary><b><a href="https://github.com/robbyczgw-cla/hermes-plugin-jev">robbyczgw-cla/hermes-plugin-jev</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · robbyczgw-cla

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

TypeSafe/Jev decision signals for Hermes: turn classification, conservative tool shaping, approvals, and coding verification.

</details>

<details>
<summary><b><a href="https://github.com/rubichandrap/hermes-jev-guard">rubichandrap/hermes-jev-guard</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · rubichandrap

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check

</details>

<details>
<summary><b><a href="https://github.com/sebastianbugal/jev">sebastianbugal/jev</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · sebastianbugal

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

TypeSafe's Jev decision model in Claude Code. Ask in plain language, get a typed answer with a calibrated probability.

</details>

<details>
<summary><b><a href="https://github.com/skeptrunedev/jev-recruiter">skeptrunedev/jev-recruiter</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · skeptrunedev

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A Jev powered LinkedIn recruiting agent. Watch it browse relevant profiles, save links, and review evidence against your hiring brief.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/skeptrunedev--jev-recruiter/d87f759cfd3422af.png" width="100%" alt="skeptrunedev/jev-recruiter screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/stoopid-computers/jev-bot">stoopid-computers/jev-bot</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · stoopid-computers

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Computer Use Agent developed with Jev

</details>

<details>
<summary><b><a href="https://github.com/sypherin/jev-trace-classifier">sypherin/jev-trace-classifier</a></b> — Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · sypherin

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next

</details>

<details>
<summary><b><a href="https://github.com/tgiridhar/claude-code-jev-smart-router">tgiridhar/claude-code-jev-smart-router</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · tgiridhar

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task phase and the cost of an undetected error, gated by prompt-cache arithmetic. Proof of concept.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tgiridhar--claude-code-jev-smart-router/28b9e1b2a005c7e2.png" width="100%" alt="tgiridhar/claude-code-jev-smart-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/thanh-abaii/ud-jev-decision-workflow">thanh-abaii/ud-jev-decision-workflow</a></b> — inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · MIT · thanh-abaii

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/themsquared/jev-benchmark">themsquared/jev-benchmark</a></b> — Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · Apache-2.0 · themsquared

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.

</details>

<details>
<summary><b><a href="https://github.com/thevibeworks/awesome-typesafe-jev">thevibeworks/awesome-typesafe-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · NOASSERTION · thevibeworks

##### ข้อมูล

ดาว **0** · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/thumay9700/jev-plays">thumay9700/jev-plays</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · thumay9700

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Autonomous game agent powered by TypeSafe AI's Jev (System One decision engine), starting with Pokémon Red.

</details>

<details>
<summary><b><a href="https://github.com/trietphan/jev-claw">trietphan/jev-claw</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · trietphan

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Typed model routing for OpenClaw agents, powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/ussyverse/hermes-jev-router">ussyverse/hermes-jev-router</a></b> — Python · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · ussyverse

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-gateway-bench">vinilana/jev-gateway-bench</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · vinilana

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Benchmark for jev-gateway: real coding agents on chess engine tasks, with Jev routing on and off

</details>

<details>
<summary><b><a href="https://github.com/yangzhou-chaofan/awesome-jev-prompt">yangzhou-chaofan/awesome-jev-prompt</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · CC0-1.0 · yangzhou-chaofan

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

latest top 100 showcases for jev (keep updating) from x / github / latest sources

</details>

<details>
<summary><b><a href="https://github.com/zbloss/jev-plays-pokemon">zbloss/jev-plays-pokemon</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · zbloss

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Like Claude Plays Pokemon, but with Jev

</details>

<details>
<summary><b><a href="https://github.com/zhangxaochen/dsh-jev">zhangxaochen/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · zhangxaochen

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev (System One decision model) plugin suite for DeepSeek Harness (dsh)

</details>

<details>
<summary><b><a href="https://github.com/DevMortimer/pi-warden">DevMortimer/pi-warden</a></b> — ⭐64 · TypeScript · unverified · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `unverified` · TypeScript · MIT · DevMortimer

##### ข้อมูล

ดาว **64** (+1) · ฟอร์ก 5 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop

> Guardrails that steer an agent before it acts. Demonstrates the gate pattern, where the decision is cheap enough to run on every step.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devmortimer--pi-warden/b8dc20ac6694613a.png" width="100%" alt="DevMortimer/pi-warden screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/pi-quiet-ask">HyunjunJeon/pi-quiet-ask</a></b> — ⭐5 · TypeScript · unverified · 1 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `unverified` · TypeScript · MIT · HyunjunJeon

##### ข้อมูล

ดาว **5** (+2) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe Jev as the pi coding agent's quiet decision layer

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hyunjunjeon--pi-quiet-ask/7ee3a99430e853d8.png" width="100%" alt="HyunjunJeon/pi-quiet-ask screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/3clyp50/a0-typesafe-ai">3clyp50/a0-typesafe-ai</a></b> — ⭐4 · Python · unverified · 2 天</summary>

##### ข้อมูลพื้นฐาน

`เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `unverified` · Python · MIT · 3clyp50

##### ข้อมูล

ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/3clyp50--a0-typesafe-ai/9aa8ea4ef8241f14.png" width="100%" alt="3clyp50/a0-typesafe-ai screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<a id="routing-guardrails"></a>

## การจัดเส้นทาง การ์ดเรล และการอนุมัติ

กรณีใช้งานแบบงานจริง — ส่งแต่ละคำขอไปยังโมเดลที่ถูกที่สุดซึ่งรับมือได้จริง และคุมผลลัพธ์ด้วยการตรวจสอบที่แน่นอน

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐49 · Rust · observed · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · Rust · NOASSERTION · Dicklesworthstone

##### ข้อมูล

ดาว **49** (+1) · ฟอร์ก 5 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 2 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · Python · MIT · Foadsf

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/Justmalhar/awesome-jev-apps">Justmalhar/awesome-jev-apps</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · Python · MIT · Justmalhar

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Awesome Collection of apps built with Jev - a System One model

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · TypeScript · MIT · qddegtya

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typed decisions from a System One model, where uncertainty is something you have to handle.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · Python · aniruddh-krovvidi

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/chy4pro/JevBrowserExt">chy4pro/JevBrowserExt</a></b> — TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · TypeScript · MIT · chy4pro

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

⚡ Ultrafast browser automation Chrome Extension (Manifest V3) powered by TypeSafe Jev (TypeSafe.ai, OpenRouter, Cloudflare)

</details>

<details>
<summary><b><a href="https://github.com/lorensation/llm-cost-optimizer-jev">lorensation/llm-cost-optimizer-jev</a></b> — observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · Apache-2.0 · lorensation

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

An intelligent routing layer powered by TypeSafe AI's System One model Jev that sits in front of multiple LLM providers, analyzes each incoming request’s complexity, routes it to the cheapest model capable of handling it at acceptable quality, and continuously validates that routing decisions are correct.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐28 · TypeScript · inferred · 0 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · yusukebe

##### ข้อมูล

ดาว **28** (+2) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐25 · Python · inferred · 0 天 · ⭐-1</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · brainstormity

##### ข้อมูล

ดาว **25** (-1) · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐6 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · MIT · mejiasd3v

##### ข้อมูล

ดาว **6** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · andrelandgraf

##### ข้อมูล

ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · keeltrace

##### ข้อมูล

ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · maker-KK

##### ข้อมูล

ดาว **2** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐2 · Python · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · prismhq

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/vtrivedy/jev-plays-games">vtrivedy/jev-plays-games</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · vtrivedy

##### ข้อมูล

ดาว **2** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Chess, Connect Four, and a decision model. Play Jev or watch Jev play itself.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/vtrivedy/jev-plays-games/main/docs/screenshots/chess.jpg" width="100%" alt="vtrivedy/jev-plays-games screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · WiktorB2004

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · Pinutss

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Shashank-H

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Jupyter · MIT · bitnovus

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/buberlo/jev-pastepilot">buberlo/jev-pastepilot</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · buberlo

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Explicit paste-to-action launcher that routes text to useful tools without automatic side effects.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/buberlo--jev-pastepilot/f9f8b5633a938cb0.png" width="100%" alt="buberlo/jev-pastepilot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/buberlo--jev-pastepilot/590a0f155ae53d69.gif" width="100%" alt="buberlo/jev-pastepilot animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://raw.githubusercontent.com/buberlo/jev-pastepilot/main/docs/demo/pastepilot-core.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/buyukcerci/jev-model-router">buyukcerci/jev-model-router</a></b> — inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Apache-2.0 · buyukcerci

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A multi-provider LLM and media router featuring calibrated confidence classification, dynamic policy scoring, and automated fallback management.

</details>

<details>
<summary><b><a href="https://github.com/carllippert/jev-router">carllippert/jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · carllippert

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Express with no routes. TypeSafe Jev picks which handler runs.

</details>

<details>
<summary><b><a href="https://github.com/danielhirt/jev-lab">danielhirt/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · danielhirt

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison

</details>

<details>
<summary><b><a href="https://github.com/gnoviawan/omp-jev-tools">gnoviawan/omp-jev-tools</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · NOASSERTION · gnoviawan

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation verification

</details>

<details>
<summary><b><a href="https://github.com/hugo-alves/jev-router-playground">hugo-alves/jev-router-playground</a></b> — JavaScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · MIT · hugo-alves

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Interactive playground for testing Jev model-routing decisions against OpenRouter models

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hugo-alves--jev-router-playground/93692a5f183f12e1.jpg" width="100%" alt="hugo-alves/jev-router-playground screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iefnaf/pi-jev">iefnaf/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · iefnaf

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Pi extension suite powered by Jev: selective context compaction and model routing

</details>

<details>
<summary><b><a href="https://github.com/immanuelsavio/jev-experiment">immanuelsavio/jev-experiment</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · immanuelsavio

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Benchmarking TypeSafe Jev against general-purpose LLMs on support-ticket routing, with a focus on latency, accuracy, and confidence.

</details>

<details>
<summary><b><a href="https://github.com/jolehuit/jev-downloads-sorter">jolehuit/jev-downloads-sorter</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · jolehuit

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A ~/Downloads folder that sorts itself: one Jev decision per file, launchd WatchPaths, no daemon

</details>

<details>
<summary><b><a href="https://github.com/kenhuangus/jev-usecases">kenhuangus/jev-usecases</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · kenhuangus

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kenhuangus--jev-usecases/be919255190f6495.png" width="100%" alt="kenhuangus/jev-usecases screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-bot">kevin9327/jev-bot</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · kevin9327

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.

</details>

<details>
<summary><b><a href="https://github.com/Loule95450/jev-free-router">Loule95450/jev-free-router</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · MIT · Loule95450

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Dynamic per-turn model router on free OpenCode Zen + Go models (fork of gargpratyush/jev-router)

</details>

<details>
<summary><b><a href="https://github.com/makefinks/jev-feed-filter">makefinks/jev-feed-filter</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · makefinks

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Smart, dynamic AI filtering for X and YouTube feeds using Jev

</details>

<details>
<summary><b><a href="https://github.com/mcgalleg/grokbot-jev-jobs">mcgalleg/grokbot-jev-jobs</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · mcgalleg

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Scores public job postings against my resume using TypeSafe's jev via the Vercel AI Gateway. Daily Vercel cron.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-arena">meetr1912/jev-arena</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · meetr1912

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A calibration arena for TypeSafe Jev: reliability, Brier/ECE, and confidence-gated risk-coverage on analytically-known random worlds.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-sonar">meetr1912/jev-sonar</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · meetr1912

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

TypeSafe Jev plays Battleship: one ~100-question typed fan-out per turn returns a calibrated hit-probability heatmap that is also the move policy.

</details>

<details>
<summary><b><a href="https://github.com/MoonTory/pi-jev-harness">MoonTory/pi-jev-harness</a></b> — TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MoonTory

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards tool calls

</details>

<details>
<summary><b><a href="https://github.com/perixtar/jev-e2e">perixtar/jev-e2e</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · perixtar

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Natural-language end-to-end tests for web apps, powered by Jev and Playwright.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/perixtar--jev-e2e/81a240435b11d6f2.gif" width="100%" alt="perixtar/jev-e2e animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://raw.githubusercontent.com/perixtar/jev-e2e/main/docs/assets/ebay-benchmark.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rajivkuriakose/typesafe-jev-examples">rajivkuriakose/typesafe-jev-examples</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · rajivkuriakose

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Worked examples for TypeSafe's Jev System One decision model, runnable today through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/ravikadam/jev-loan-triage">ravikadam/jev-loan-triage</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · ravikadam

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Voice loan-call triage using TypeSafe Jev: intent, info sufficiency and a lending decision from typed AI judgments

</details>

<details>
<summary><b><a href="https://github.com/SadiqOnGithub/jev-lab">SadiqOnGithub/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · SadiqOnGithub

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API

</details>

<details>
<summary><b><a href="https://github.com/SDTakeuchi/jev-api-router">SDTakeuchi/jev-api-router</a></b> — Go · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Go · SDTakeuchi

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/TokenTrim/jev-routing-experiment">TokenTrim/jev-routing-experiment</a></b> — Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · Apache-2.0 · TokenTrim

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tokentrim--jev-routing-experiment/1c31bd606ebc1994.png" width="100%" alt="TokenTrim/jev-routing-experiment screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ufec/jev-block-android-ad">ufec/jev-block-android-ad</a></b> — Kotlin · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Kotlin · MIT · ufec

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

JevNoiseGate filters unwanted notifications and SMS on Android. Rather than   matching keywords, an LLM decides what's noise — and only what it explicitly   flags is blocked. Verification codes are matched on-device and never uploaded;   anything uncertain passes through.

</details>

<details>
<summary><b><a href="https://github.com/viniciosrab/pi-jev-router">viniciosrab/pi-jev-router</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · viniciosrab

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/Zumka1991/jev-telegram-admin">Zumka1991/jev-telegram-admin</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · Zumka1991

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

AI moderator for Telegram groups powered by the Jev (TypeSafe System One) decision model

</details>

<details>
<summary><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">iammrduncan/typesafe-ai-benchmark</a></b> — ⭐32 · TypeScript · unverified · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `unverified` · TypeScript · MIT · iammrduncan

##### ข้อมูล

ดาว **32** · ฟอร์ก 5 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.

> A gateway that mimics the System One interface, which is what makes side-by-side benchmarking possible without rewriting the caller.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/80d6baf37faa23fb.gif" width="100%" alt="iammrduncan/typesafe-ai-benchmark animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://raw.githubusercontent.com/iammrduncan/typesafe-ai-benchmark/main/docs/media/theater-demo.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kavehmz/typesafe-playground">kavehmz/typesafe-playground</a></b> — ⭐9 · JavaScript · unverified · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `unverified` · JavaScript · kavehmz

##### ข้อมูล

ดาว **9** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI decisions and visible sensor inputs.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/kavehmz/typesafe-playground/main/docs/images/demo03-fable.png" width="100%" alt="kavehmz/typesafe-playground screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/raihankhan-rk/diffjury">raihankhan-rk/diffjury</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `unverified` · TypeScript · raihankhan-rk

##### ข้อมูล

ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

DiffJury — TypeSafe Jev PR risk router + code review coach

</details>

<a id="evaluation"></a>

## การประเมิน การคาลิเบรต และเบนช์มาร์ก

ใครจะรู้ได้ว่าการตัดสินใจเหล่านั้นดีพอ การคาลิเบรตเป็นคำถามเปิดในระบบนิเวศนี้ และนี่คือโปรเจกต์ที่วัดมัน

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐5 · Python · observed · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `observed` · Python · Apache-2.0 · ikermoel

##### ข้อมูล

ดาว **5** (+1) · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Open-source alternative to TypeSafe's Jev: a System One style model layer that gives typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with honest benchmarks

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `observed` · Python · akash-kamat

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/edgardcham/huncho">edgardcham/huncho</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `observed` · TypeScript · MIT · edgardcham

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Decisions as code on System One models: typed questions, thresholds with hysteresis, nested decisions, journal, calibration

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `observed` · Go · MIT · Gaurav-Gosain

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — ⭐1 · Python · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `observed` · Python · Apache-2.0 · hev

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/nishioka-shinji/jev-edgar">nishioka-shinji/jev-edgar</a></b> — Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `observed` · Python · nishioka-shinji

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Does Jev, a System One model returning calibrated probabilities, say anything useful about an earnings release before the market prices it?

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐8 · Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · Apache-2.0 · AbdelStark

##### ข้อมูล

ดาว **8** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐6 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · NOASSERTION · Heman10x-NGU

##### ข้อมูล

ดาว **6** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/abhixhek/jevcal">abhixhek/jevcal</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · abhixhek

##### ข้อมูล

ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abhixhek--jevcal/3dbe2307176737c8.png" width="100%" alt="abhixhek/jevcal screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐5 · TypeScript · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · TypeScript · MIT · y0usaf

##### ข้อมูล

ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/cablehead/jev.nu">cablehead/jev.nu</a></b> — ⭐2 · Nushell · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Nushell · MIT · cablehead

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Nushell module for the TypeSafe System One API: typed decisions with calibrated probabilities

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · wondertwins

##### ข้อมูล

ดาว **2** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · 4esv

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

</details>

<details>
<summary><b><a href="https://github.com/carson-sweet/jev-plays-brogue">carson-sweet/jev-plays-brogue</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · TypeScript · AGPL-3.0 · carson-sweet

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

TypeSafe's Jev model plays the roguelike Brogue live -- a hand-built expert system for System-2 reasoning, outcome-calibrated self-learning, and a web UI to watch decisions, costs, and training progress.

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · TypeScript · MIT · Danu28

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · TeX · NOASSERTION · dnakhoa

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · eggmasonvalue

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/ickma2311/jev-baselines-eval">ickma2311/jev-baselines-eval</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · ickma2311

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Pre-registered independent eval of TypeSafe Jev against a nano-class LLM, a frontier LLM, and a supervised encoder (Banking77 + CLINC150 zero-shot)

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ickma2311--jev-baselines-eval/4cef768bc4898704.png" width="100%" alt="ickma2311/jev-baselines-eval screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · jujumilk3

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · JavaScript · MIT · KantaHayashiAI

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/KiishiAD/jev-loan-identity-benchmark">KiishiAD/jev-loan-identity-benchmark</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · KiishiAD

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Reproducible synthetic benchmark for temporal loan identity resolution with TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/laurentfabre/databricks-jev-pdf-lab">laurentfabre/databricks-jev-pdf-lab</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · laurentfabre

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Precision PDF extraction research: Databricks + Jev, synthetic tests, selective parsing, measured tradeoffs and negative results.

</details>

<details>
<summary><b><a href="https://github.com/llt22/jev-lab">llt22/jev-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · llt22

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

TypeSafe Jev research, benchmarks, evaluation datasets, and reproducible experiments

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-bracket">meetr1912/jev-bracket</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · meetr1912

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

TypeSafe Jev predicts a synthetic 32-team tournament in round fan-out: calibrated Brier vs Elo/seed/oracle plus Monte Carlo champion odds.

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-vickrey">meetr1912/jev-vickrey</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · meetr1912

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

TypeSafe Jev bids in sealed-bid auctions: threshold fan-out reconstructs a calibrated value CDF, scored by regret and truthfulness.

</details>

<details>
<summary><b><a href="https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and">musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and</a></b> — HTML · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · HTML · MIT · musman550

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@automatewithmusfiraai"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@automatewithmusfiraai">รับชมบน youtube.com</a> · การเล่นจะเปิดบนเว็บไซต์ต้นทาง GitHub ไม่สามารถฝังแบบอินไลน์ได้</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/onlyoneaman/jev-eval">onlyoneaman/jev-eval</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · TypeScript · MIT · onlyoneaman

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/onlyoneaman--jev-eval/e5d471e96e134f81.png" width="100%" alt="onlyoneaman/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rorshopping/jev-browser-local">rorshopping/jev-browser-local</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · NOASSERTION · rorshopping

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Run jev-browser on a fully local JEV-style decision engine (no cloud API). Warm-browser fork, VRAM guard, measured benchmarks, run traces.

</details>

<details>
<summary><b><a href="https://github.com/SHAKULMITTAL22/jev-resume">SHAKULMITTAL22/jev-resume</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · AGPL-3.0 · SHAKULMITTAL22

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Folio: job-specific resume leaderboards with approved rubrics, evidence-backed AI evaluation, and human hiring decisions.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shakulmittal22--jev-resume/e653593f3a00df9d.png" width="100%" alt="SHAKULMITTAL22/jev-resume screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shunta-furukawa/jev-tick-lab">shunta-furukawa/jev-tick-lab</a></b> — inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · shunta-furukawa

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis.

</details>

<details>
<summary><b><a href="https://github.com/teyhouse/jev-secret-detection">teyhouse/jev-secret-detection</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · teyhouse

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" width="100%" alt="teyhouse/jev-secret-detection screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/thisisandreeeee/jev-benchmarks">thisisandreeeee/jev-benchmarks</a></b> — inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · MIT · thisisandreeeee

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/us/jev-local">us/jev-local</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · us

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Local Jev-compatible evaluation server: POST /v1/systemone with typed noul/choice/score, open weights, no waitlist

</details>

<details>
<summary><b><a href="https://github.com/yodablocks/jev-orderby-bench">yodablocks/jev-orderby-bench</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · yodablocks

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and invariant measurements of TypeSafe AI's Jev.

</details>

<details>
<summary><b><a href="https://github.com/kyotofin/tax-doc-classifier">kyotofin/tax-doc-classifier</a></b> — ⭐130 · TypeScript · unverified · 0 天 · ⭐+17</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `unverified` · TypeScript · Apache-2.0 · kyotofin

##### ข้อมูล

ดาว **130** (+17) · ฟอร์ก 12 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per page.

</details>

<details>
<summary><b><a href="https://github.com/Mapika/decider">Mapika/decider</a></b> — ⭐25 · Python · unverified · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `unverified` · Python · Apache-2.0 · Mapika

##### ข้อมูล

ดาว **25** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mapika--decider/c67d355f22dcb51a.gif" width="100%" alt="Mapika/decider animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/genai-craft/openvons">genai-craft/openvons</a></b> — ⭐7 · Python · unverified · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `unverified` · Python · NOASSERTION · genai-craft

##### ข้อมูล

ดาว **7** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド

</details>

<details>
<summary><b><a href="https://github.com/aabolfazl/typesafe-local">aabolfazl/typesafe-local</a></b> — ⭐6 · Python · unverified · 0 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `unverified` · Python · MIT · aabolfazl

##### ข้อมูล

ดาว **6** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/aabolfazl--typesafe-local/ada59cf382af5143.png" width="100%" alt="aabolfazl/typesafe-local screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mithalouni/system-one-open">mithalouni/system-one-open</a></b> — ⭐4 · Python · unverified · 1 天</summary>

##### ข้อมูลพื้นฐาน

`การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `unverified` · Python · NOASSERTION · mithalouni

##### ข้อมูล

ดาว **4** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal)

</details>

<a id="research-models"></a>

## งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม

เวตเปิด งานจำลองขนาดเล็ก และงานสถาปัตยกรรม หลายโปรเจกต์มีอยู่เพราะพฤติกรรมการคาลิเบรตจำลองขึ้นใหม่จากเอกสารสาธารณะเพียงอย่างเดียวไม่ได้

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐63 · Python · observed · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `observed` · Python · MIT · kshetrajna12

##### ข้อมูล

ดาว **63** (+1) · ฟอร์ก 4 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐395 · Python · inferred · 1 天 · ⭐+25</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · MIT · TianyuCodings

##### ข้อมูล

ดาว **395** (+25) · ฟอร์ก 37 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/5055af419619e7e4.gif" width="100%" alt="TianyuCodings/NanoJev animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/assets/side_by_side_maze.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐22 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · MIT · r-ms

##### ข้อมูล

ดาว **22** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/imserhatdemir/jevspace">imserhatdemir/jevspace</a></b> — HTML · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `observed` · HTML · imserhatdemir

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A DarkOrbit-style space game piloted by Jev — TypeSafe's System One model. Three.js world, deterministic engine, Jev picks the targets.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/imserhatdemir/jevspace/main/docs/screenshot-win.png" width="100%" alt="imserhatdemir/jevspace screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `observed`

##### ข้อมูล

ดาวน์โหลด 25 · ถูกใจ 4 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `observed`

##### ข้อมูล

ดาวน์โหลด 0 · ถูกใจ 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐160 · Python · inferred · 0 天 · ⭐+6</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · ekzhang

##### ข้อมูล

ดาว **160** (+6) · ฟอร์ก 12 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/featherless-ai/simple-jev">featherless-ai/simple-jev</a></b> — ⭐70 · Python · inferred · 0 天 · ⭐+13</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · featherless-ai

##### ข้อมูล

ดาว **70** (+13) · ฟอร์ก 6 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Turn any open model into a classifier/jev endpoint

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/featherless-ai/simple-jev/main/imgs/Simple-Jev-Logo.png" width="100%" alt="featherless-ai/simple-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐24 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · MIT · bnsd55

##### ข้อมูล

ดาว **24** · ฟอร์ก 3 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/siliconkernel/vllm-jev-decison">siliconkernel/vllm-jev-decison</a></b> — ⭐8 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · MIT · siliconkernel

##### ข้อมูล

ดาว **8** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Classification-only typed decisions for vLLM: finite-schema candidate scoring, probabilities, and abstention. No generative fallback.

</details>

<details>
<summary><b><a href="https://github.com/wfzyx/von">wfzyx/von</a></b> — ⭐4 · Python · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · wfzyx

##### ข้อมูล

ดาว **4** (+1) · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/choxos/jev-reviewer">choxos/jev-reviewer</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · JavaScript · MIT · choxos

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay in your browser.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/4a551dbca9d0c41e.jpg" width="100%" alt="choxos/jev-reviewer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/71abea319063ce6d.gif" width="100%" alt="choxos/jev-reviewer animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/deep-diver/mini-jev">deep-diver/mini-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · deep-diver

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/kw2828/OpenJev">kw2828/OpenJev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · MIT · kw2828

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Browser decision playground and reproducible experiments on memory, uncertainty, and Doom control

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/7caa9b0eff4636a1.png" width="100%" alt="kw2828/OpenJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/af5371a3a94cb693.gif" width="100%" alt="kw2828/OpenJev animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/backmeupplz/jev_antispam_bot">backmeupplz/jev_antispam_bot</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · TypeScript · MIT · backmeupplz

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">legacybridge-tech/pi-typesafe-jev</a></b> — TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · TypeScript · NOASSERTION · legacybridge-tech

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.

</details>

<details>
<summary><b><a href="https://github.com/NeU-dev/reddit-jev-sentiment-analyzer">NeU-dev/reddit-jev-sentiment-analyzer</a></b> — inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · NeU-dev

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A non-commercial personal research prototype for numerical sentiment analysis of public Reddit technology discussions using JEV.

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · shellneko

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐9 · Python · unverified · 2 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `unverified` · Python · NOASSERTION · zhihz

##### ข้อมูล

ดาว **9** (+1) · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<a id="apps-demos"></a>

## แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ

เกม หุ่นยนต์ เบราว์เซอร์ และแดชบอร์ด เดโมคือสิ่งที่ทำให้ข้ออ้างเรื่องความหน่วงและต้นทุนอ่านออก

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐10 · Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · Python · Apache-2.0 · zadescoxp

##### ข้อมูล

ดาว **10** · ฟอร์ก 1 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · TypeScript · daftAI2026

##### ข้อมูล

ดาว **2** · ฟอร์ก 2 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · Rust · MIT · markjaquith

##### ข้อมูล

ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · TypeScript · adiun

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · Dart · Bud-ro

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/chris-wozniczek/jev-voice-control">chris-wozniczek/jev-voice-control</a></b> — Swift · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · Swift · chris-wozniczek

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-bar Swift app.

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · Python · MIT · tirukovelamanoj

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/04e4dd3a1f6c6bae.gif" width="100%" alt="tirukovelamanoj/jev-plays-doom animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://raw.githubusercontent.com/tirukovelamanoj/jev-plays-doom/main/docs/jev-doom.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · TypeScript · wustep

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://x.com/tspy/status/2100864234523685146">X intent labeller</a></b> — @tspy · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · [yishan](https://x.com/tspy) · @tspy · x.com

##### ข้อมูล

จำนวนดู 2364 · ถูกใจ 15 · ความคิดเห็น 9 · เผยแพร่เมื่อ 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A Chrome extension that labels posts in an X timeline with their intent and probability as you scroll, drawn as a tag directly after each post's timestamp. Categories include inducement, provocation, promotion, machine-generated, persuasion, entertainment and information. A side panel reports session counts (seen, judged, correct) and cumulative token cost. The author reports near-instant responses and usable accuracy before any tuning.

<sub>กำลังตรวจสอบลิงก์โครงการต้นฉบับ</sub>

> Worth reading as a latency argument rather than an accuracy one: labelling a timeline only works if the decision costs less than the scroll, which is the constraint a generative model cannot meet.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/0641644f12a25a45.jpg" width="100%" alt="X intent labeller screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/b80cf3173f63bdd7.gif" width="100%" alt="X intent labeller animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://video.twimg.com/amplify_video/2100858340331200512/vid/avc1/1242x720/ex2FF5-TerVxo9xX.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐111 · Python · inferred · 0 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · MIT · hr98w

##### ข้อมูล

ดาว **111** (+2) · ฟอร์ก 12 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐108 · TypeScript · inferred · 0 天 · ⭐+4</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · MIT · jkudish

##### ข้อมูล

ดาว **108** (+4) · ฟอร์ก 5 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/d9b7631c25d7db06.gif" width="100%" alt="jkudish/jev-browser animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐79 · JavaScript · inferred · 1 天 · ⭐+8</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · MIT · moritzkremb

##### ข้อมูล

ดาว **79** (+8) · ฟอร์ก 8 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/mizchi/jev-playground">mizchi/jev-playground</a></b> — ⭐15 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · mizchi

##### ข้อมูล

ดาว **15** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐7 · Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · MIT · komorra

##### ข้อมูล

ดาว **7** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐7 · JavaScript · inferred · 0 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · vinilana

##### ข้อมูล

ดาว **7** (+2) · ฟอร์ก 5 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · emrickgarrett

##### ข้อมูล

ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Go · MIT · paulsmith

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · MIT · vmendes90

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/vmendes90--jev-shield/ee87b261d199a34c.jpg" width="100%" alt="vmendes90/jev-shield screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0x7067/jev-browse">0x7067/jev-browse</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · MIT · 0x7067

##### ข้อมูล

ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Browser automation with Jev (TypeSafe) as decision model

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/6b2906f1131adf4c.gif" width="100%" alt="0x7067/jev-browse screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/3efc4d3b381ff9f5.gif" width="100%" alt="0x7067/jev-browse animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://raw.githubusercontent.com/0x7067/jev-browse/main/docs/demo.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/charleeagni/JevPiano">charleeagni/JevPiano</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · charleeagni

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

@typesafeai 's Jev controls the 2 hands and each finger to play the piano in real-time.  Jev only "sees" what we see and plays this from the "note waterfall". It uses  @browser_use 's jev-ultrafast and some decision scheduling to make this happen in real-time.  Sound on 🔈🔉🔊

</details>

<details>
<summary><b><a href="https://github.com/finetuningsingh/jev-chatbot">finetuningsingh/jev-chatbot</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · MIT · finetuningsingh

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Experiment: using TypeSafe Jev as a chatbot by choosing replies one letter or word at a time

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · Little-Planet-Labs

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · PistachioAIHQ

##### ข้อมูล

ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/acharyaanusha/magic-jev-demo">acharyaanusha/magic-jev-demo</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · acharyaanusha

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Sample pull requests for demoing Magic Jev. The code is filler.

</details>

<details>
<summary><b><a href="https://github.com/bahramzada/jev-taxi-dispatch">bahramzada/jev-taxi-dispatch</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · MIT · bahramzada

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Real-vaxt taksi dispetçerlik simulyasiyası - TypeSafe JEV (System One) modeli ilə

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/bahramzada--jev-taxi-dispatch/e616f4168b15d3f2.png" width="100%" alt="bahramzada/jev-taxi-dispatch screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/BrendanH18/jev-lab">BrendanH18/jev-lab</a></b> — Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · MIT · BrendanH18

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brendanh18--jev-lab/b16b9535e3744cd3.png" width="100%" alt="BrendanH18/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/chahero/driving-jev">chahero/driving-jev</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · chahero

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Watch TypeSafe Jev make highway driving decisions. Includes live API and offline gameplay previews.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev-preview.gif" width="100%" alt="chahero/driving-jev screenshot"></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev.mp4"><img src="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev-preview.gif" width="100%" alt="chahero/driving-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/chahero/driving-jev/master/media/jev.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/ethereumdegen/jev-discord-bot">ethereumdegen/jev-discord-bot</a></b> — Rust · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Rust · MIT · ethereumdegen

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/formigacamuflada/jev-computer-use">formigacamuflada/jev-computer-use</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · formigacamuflada

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/gua-project/gua-sample-jev-racinggame">gua-project/gua-sample-jev-racinggame</a></b> — inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · gua-project

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/JYeswak/jev_playground">JYeswak/jev_playground</a></b> — Shell · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Shell · MIT · JYeswak

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jyeswak--jev_playground/b6414da07c9c5aa8.jpg" width="100%" alt="JYeswak/jev_playground screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Keitark/jev-gamebook-demo">Keitark/jev-gamebook-demo</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · Keitark

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/metrox-eth/moss-jev">metrox-eth/moss-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · metrox-eth

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

MOSS × Jev: a recorded-run 3D demo of the litter-picking rover choosing targets with TypeSafe's Jev decision model.

</details>

<details>
<summary><b><a href="https://github.com/n3ndor/n8n-nodes-typesafe-jev">n3ndor/n8n-nodes-typesafe-jev</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · MIT · n3ndor

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

n8n community node for TypeSafe Jev structured AI decisions

</details>

<details>
<summary><b><a href="https://github.com/parzivale/jev-bot">parzivale/jev-bot</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Rust · parzivale

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Discord bot that scores how likely a statement is to be true, using TypeSafe's jev model

</details>

<details>
<summary><b><a href="https://github.com/PierrunoYT/JevFlow">PierrunoYT/JevFlow</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · PierrunoYT

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A trading bot powered by TypeSafe AI's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pistachiopranay/jev-synergy-screening">pistachiopranay/jev-synergy-screening</a></b> — inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · pistachiopranay

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/rchovatiya88/cyber-breach-jev">rchovatiya88/cyber-breach-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · rchovatiya88

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model

</details>

<details>
<summary><b><a href="https://github.com/rikkooo/jev-trade">rikkooo/jev-trade</a></b> — inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · rikkooo

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A market-data trading simulator powered by auditable Jev judgments

</details>

<details>
<summary><b><a href="https://github.com/SuryaManavalan/JevNash">SuryaManavalan/JevNash</a></b> — inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · SuryaManavalan

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Jev harness for playing or working, agnostic of the game or workstream.

</details>

<details>
<summary><b><a href="https://github.com/tanayvasishtha/Slither-Me-Jev">tanayvasishtha/Slither-Me-Jev</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · tanayvasishtha

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

8 AI snakes, 1 human, 1 arena. Every snake is driven live by TypeSafe's Jev, making all decisions in real time

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/tanayvasishtha/Slither-Me-Jev/main/menu-screenshot.png" width="100%" alt="tanayvasishtha/Slither-Me-Jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/sorrycc/typesafe-snake">sorrycc/typesafe-snake</a></b> — ⭐17 · TypeScript · unverified · 1 天</summary>

##### ข้อมูลพื้นฐาน

`แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `unverified` · TypeScript · sorrycc

##### ข้อมูล

ดาว **17** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code

</details>

<a id="media-discussions"></a>

## บทความ การสนทนา และรายการที่เกี่ยวข้อง

เธรดเปิดตัว บทความอิสระ และรายการคัดสรรอื่น ๆ ในสายนี้ รีโพซิทอรีนี้ไม่ใช่รายการเดียว และการพูดเช่นนั้นมีประโยชน์กว่าการแกล้งทำเป็นอย่างอื่น

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐5671 · Python · observed · 0 天 · ⭐+200</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · MIT · browser-use

##### ข้อมูล

ดาว **5671** (+200) · ฟอร์ก 361 · issue ที่เปิดอยู่ 34 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

i. am. speed.

<sub>พบการใช้งานในโค้ด: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcdb919ac3afb514.gif" width="100%" alt="browser-use/jev-ultrafast animation"><br><sub>บันทึกแบบเคลื่อนไหว · <a href="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/demo.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1890 · observed · 3 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 1890 · ความคิดเห็น 496 · push ล่าสุด 2026-09-15 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐529 · Python · observed · 0 天 · ⭐+9</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · MIT · Anil-matcha

##### ข้อมูล

ดาว **529** (+9) · ฟอร์ก 102 · issue ที่เปิดอยู่ 4 · สร้างเมื่อ 2023-05-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>พบการใช้งานในโค้ด: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐235 · TypeScript · observed · 0 天 · ⭐+16</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · TypeScript · dabit3

##### ข้อมูล

ดาว **235** (+16) · ฟอร์ก 20 · issue ที่เปิดอยู่ 17 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

<sub>พบการใช้งานในโค้ด: `jev-lint/proxy.mjs`</sub>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐232 · CSS · observed · 0 天 · ⭐+8</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · CSS · MIT · AbdelStark

##### ข้อมูล

ดาว **232** (+8) · ฟอร์ก 34 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>พบการใช้งานในโค้ด: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐181 · Python · observed · 0 天 · ⭐+16</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · yibie

##### ข้อมูล

ดาว **181** (+16) · ฟอร์ก 25 · issue ที่เปิดอยู่ 13 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐118 · observed · 0 天 · ⭐+5</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · CC0-1.0 · cobanov

##### ข้อมูล

ดาว **118** (+5) · ฟอร์ก 12 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐67 · observed · 0 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · CC0-1.0 · AnotiaWang

##### ข้อมูล

ดาว **67** (+2) · ฟอร์ก 19 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>พบการใช้งานในโค้ด: `README.md`, `README_zh.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐52 · observed · 1 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 52 · ความคิดเห็น 12 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐37 · JavaScript · observed · 0 天 · ⭐+4</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### ข้อมูล

ดาว **37** (+4) · ฟอร์ก 10 · issue ที่เปิดอยู่ 10 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A community directory of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐11 · JavaScript · observed · 0 天 · ⭐+2</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · NOASSERTION · OmniJev

##### ข้อมูล

ดาว **11** (+2) · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Papers, open reproductions and independent evaluations behind System One models and Jev.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49760264">Using jev to improve product experiences is pretty crazy</a></b> — ⭐6 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 6 · ความคิดเห็น 3 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 3 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 5 · ความคิดเห็น 0 · push ล่าสุด 2026-09-15 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 4 · ความคิดเห็น 0 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 4 · ความคิดเห็น 0 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 3 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755005">Two techniques for working with System One models</a></b> — ⭐3 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 3 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 3 · ความคิดเห็น 0 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐2 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · NOASSERTION · aliaihub

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### ข้อมูล

ดาว **2** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49759706">I used Jev to control a swarm of 15 simulated drones in real time</a></b> — ⭐2 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49759999">Jev&#x27;s Architecture Unmasked</a></b> — ⭐2 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/jtnkminimal/awesome-jev">jtnkminimal/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · CC0-1.0 · jtnkminimal

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A curated projects built with Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49753667">Show HN: Explore 2D semantic space with the Jev model</a></b> — ⭐2 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

SemanticSpace is an experiment around Jev, TypeSafe AI’s new model. It uses a Cartesian plane defined by arbitrary phrases for each axis, to map prompts onto the resulting 2D semantic space. You can edit the prompts and axes to visualize virtually any 2D relationship.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49750649">Show HN: Open-Source Alternative to TypeSafe.ai</a></b> — ⭐2 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 1 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49744527">Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)</a></b> — ⭐2 · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 1 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Full disclosure, it was coded with AI, I don&#x27;t claim otherwise. But I wanted to test out tool calls and iterative problem solving using Jev and needed a simple library&#x2F;framework&#x2F;harness to do that.
SOKIT (System One Knowledge, Instructions and Tools) is the result

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49729945">The first (public) System One Model; Jev gives AI the properties of code</a></b> — ⭐2 · observed · 2 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49757995">TypeSafe / Jev latency-focused demos built by Devin</a></b> — ⭐2 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49761730">TypeSafe AI&#x27;s Jev Is Not an LLM – and That May Be the Point</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49745212">Typesafe&#x27;s Jev is the fish at the poker table</a></b> — ⭐2 · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 1 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49733647">Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step</a></b> — ⭐2 · observed · 2 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49734345">Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD</a></b> — ⭐2 · observed · 2 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49760138">What is a System One model and why we need it?</a></b> — ⭐2 · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

##### ข้อมูล

คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/ozers/jevsome-projects">ozers/jevsome-projects</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · MIT · ozers

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Open-source projects that provably call Jev, TypeSafe AI's System One model. Every entry links to the line of code that proves it. Refreshed daily.

</details>

<details>
<summary><b><a href="https://github.com/rhc98/awesome-jev">rhc98/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · TypeScript · NOASSERTION · rhc98

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself.

</details>

<details>
<summary><b><a href="https://github.com/soderlind/ai-provider-for-jev">soderlind/ai-provider-for-jev</a></b> — ⭐1 · PHP · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · PHP · soderlind

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).

</details>

<details>
<summary><b><a href="https://github.com/aamanlamba/jev-explore">aamanlamba/jev-explore</a></b> — Jupyter · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Jupyter · aamanlamba

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

An example repository for exploring Jev - the System One model

</details>

<details>
<summary><b><a href="https://github.com/alpibrusl/lex-judge">alpibrusl/lex-judge</a></b> — Lex · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Lex · alpibrusl

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typed judgments from a System One model, as a \[net\]-only Lex effect

</details>

<details>
<summary><b><a href="https://github.com/codaaiteam/jev-ai">codaaiteam/jev-ai</a></b> — observed · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · codaaiteam

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Jev AI quickstart & FAQ — TypeSafe AI's System One model. Try it free: jevtypesafeai.com

</details>

<details>
<summary><b><a href="https://github.com/hide-G/magi-system-on-jev">hide-G/magi-system-on-jev</a></b> — JavaScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · hide-G

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/hide-G/magi-system-on-jev/master/public/ogp.png" width="100%" alt="hide-G/magi-system-on-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/JohnDotOwl/awesome-jev">JohnDotOwl/awesome-jev</a></b> — JavaScript · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · CC0-1.0 · JohnDotOwl

##### ข้อมูล

ดาว **0** · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A curated list of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/piyush97/focus-tube">piyush97/focus-tube</a></b> — JavaScript · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · MIT · piyush97

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model

</details>

<details>
<summary><b><a href="https://github.com/rbalch/typesafeai-review">rbalch/typesafeai-review</a></b> — Python · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · rbalch

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Using Typesafe.AI to generate diff reviews.

</details>

<details>
<summary><b><a href="https://github.com/robzolkos/omarchy-issue-classifier">robzolkos/omarchy-issue-classifier</a></b> — Ruby · observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Ruby · robzolkos

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Classify the Omarchy issue backlog with Jev, TypeSafe's System One model. Ten typed questions per issue in one request, for a hundredth of a cent each.

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/jev-trader">Shashank-H/jev-trader</a></b> — observed · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · AGPL-3.0 · Shashank-H

##### ข้อมูล

ดาว **0** · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

An automated trader using SystemOne model - TypesafeAI Jev

</details>

<details>
<summary><b><a href="https://github.com/TheGali/terrarium">TheGali/terrarium</a></b> — JavaScript · observed · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · MIT · TheGali

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.

</details>

<details>
<summary><b><a href="https://github.com/jarrodwatts/jev-trader">jarrodwatts/jev-trader</a></b> — ⭐888 · TypeScript · inferred · 1 天 · ⭐+23</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · jarrodwatts

##### ข้อมูล

ดาว **888** (+23) · ฟอร์ก 170 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

</details>

<details>
<summary><b><a href="https://github.com/droidrun/mobile-jev">droidrun/mobile-jev</a></b> — ⭐144 · JavaScript · inferred · 1 天 · ⭐+9</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · MIT · droidrun

##### ข้อมูล

ดาว **144** (+9) · ฟอร์ก 22 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/superagents-lab/jev-search">superagents-lab/jev-search</a></b> — ⭐123 · TypeScript · inferred · 0 天 · ⭐+19</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · superagents-lab

##### ข้อมูล

ดาว **123** (+19) · ฟอร์ก 20 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/superagents-lab--jev-search/5a545ddfd6a52aed.png" width="100%" alt="superagents-lab/jev-search screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mrnugget/jev-shell-history">mrnugget/jev-shell-history</a></b> — ⭐44 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · mrnugget

##### ข้อมูล

ดาว **44** (+1) · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Fish-style zsh history autosuggestions ranked by Jev (TypeSafe)

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">IAmUnbounded/save-token-jev-clean</a></b> — ⭐40 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · IAmUnbounded

##### ข้อมูล

ดาว **40** · ฟอร์ก 9 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/daseinlabs/open-jev">daseinlabs/open-jev</a></b> — ⭐32 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · daseinlabs

##### ข้อมูล

ดาว **32** · ฟอร์ก 5 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov"><img src="" width="100%" alt="daseinlabs/open-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hqman/JevScout">hqman/JevScout</a></b> — ⭐18 · Python · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · hqman

##### ข้อมูล

ดาว **18** (+1) · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4"><img src="" width="100%" alt="hqman/JevScout video"></a><br><sub><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4">เปิดวิดีโอ</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/oso95/x-scanner">oso95/x-scanner</a></b> — ⭐8 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · oso95

##### ข้อมูล

ดาว **8** (+1) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter

</details>

<details>
<summary><b><a href="https://github.com/Kevthetech143/super-jev">Kevthetech143/super-jev</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · Kevthetech143

##### ข้อมูล

ดาว **5** · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A small, extensible decision-to-action harness for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/joelhooks/pi-fast-jev-compaction">joelhooks/pi-fast-jev-compaction</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · joelhooks

##### ข้อมูล

ดาว **4** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Pi extension: verbatim context compaction with TypeSafe Jev decisions

</details>

<details>
<summary><b><a href="https://github.com/haseeb-heaven/jev-system-one">haseeb-heaven/jev-system-one</a></b> — ⭐2 · Python · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · haseeb-heaven

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/haseeb-heaven--jev-system-one/e41c848323b1077a.png" width="100%" alt="haseeb-heaven/jev-system-one screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevinpita/pi-jev-context">kevinpita/pi-jev-context</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · kevinpita

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Reversible context pruning for Pi, powered by TypeSafe Jev. Keep useful context without deleting session history.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevinpita--pi-jev-context/9f40314df01e39d4.png" width="100%" alt="kevinpita/pi-jev-context screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/lbotinelly/jev-little-airways">lbotinelly/jev-little-airways</a></b> — ⭐2 · HTML · inferred · 1 天 · ⭐+1</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · HTML · MIT · lbotinelly

##### ข้อมูล

ดาว **2** (+1) · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A show-and-tell capability study for Jev, TypeSafe's System One decision model.

</details>

<details>
<summary><b><a href="https://github.com/oxwen11/awesome-jev">oxwen11/awesome-jev</a></b> — ⭐2 · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · CC0-1.0 · oxwen11

##### ข้อมูล

ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A curated list of what people built with Jev

</details>

<details>
<summary><b><a href="https://github.com/1jehuang/jev-pr-labeler">1jehuang/jev-pr-labeler</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · 1jehuang

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Semantic GitHub PR labels using Jev's typed decisions, with conceptual scope instead of line counts

</details>

<details>
<summary><b><a href="https://github.com/AppitStudio/awesome-jev">AppitStudio/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · NOASSERTION · AppitStudio

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 4 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Curated Jev resources and runnable examples for typed AI decisions.

</details>

<details>
<summary><b><a href="https://github.com/Charlyhno-eng/jev-document-classification">Charlyhno-eng/jev-document-classification</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · Charlyhno-eng

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/charlyhno-eng--jev-document-classification/113bcf66f1648122.png" width="100%" alt="Charlyhno-eng/jev-document-classification screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/jev-review-action">fatwang2/jev-review-action</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · MIT · fatwang2

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.

</details>

<details>
<summary><b><a href="https://github.com/kazuhideoki/jev-search">kazuhideoki/jev-search</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · kazuhideoki

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Recursive semantic file search using TypeSafe Jev and fzf

</details>

<details>
<summary><b><a href="https://github.com/MumuTW/awesome-jev">MumuTW/awesome-jev</a></b> — ⭐1 · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · CC0-1.0 · MumuTW

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

快速看懂風格鮮明的 Jev：型別化決策的 System One，以及社群熱議的同類模型。

</details>

<details>
<summary><b><a href="https://github.com/sontakey/awesome-jev">sontakey/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · NOASSERTION · sontakey

##### ข้อมูล

ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Unofficial list of insanely useful TypeSafe AI Jev / System One projects

</details>

<details>
<summary><b><a href="https://github.com/TanayPadar/gpt-vs-jev">TanayPadar/gpt-vs-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · TanayPadar

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Compare GPT generated language with JEV structured Noul decisions on the same input.

</details>

<details>
<summary><b><a href="https://github.com/tylerjharden/harden-jev-decides">tylerjharden/harden-jev-decides</a></b> — ⭐1 · TypeScript · inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · tylerjharden

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.

</details>

<details>
<summary><b><a href="https://github.com/X0EF/jev_projects">X0EF/jev_projects</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · MIT · X0EF

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

list of projects that use typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/Z761293629/pi-jev-helm">Z761293629/pi-jev-helm</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · Z761293629

##### ข้อมูล

ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/agentik-os/jev-radar">agentik-os/jev-radar</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · agentik-os

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/amansoory/JEV2048">amansoory/JEV2048</a></b> — C++ · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · C++ · amansoory

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/amr05008/jev-sandbox">amr05008/jev-sandbox</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · amr05008

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Test bench for TypeSafe's Jev: small, repeatable experiments on where a decision model beats prompt-and-parse

</details>

<details>
<summary><b><a href="https://github.com/Btheriot83/jev-academy">Btheriot83/jev-academy</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · Btheriot83

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Public Jev / TypeSafe academy — zero-to-hero walkthrough for Brandon Theriot

</details>

<details>
<summary><b><a href="https://github.com/caio0452/jev_search">caio0452/jev_search</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · caio0452

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/divo12/jev-v-llm">divo12/jev-v-llm</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · divo12

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/doroper98/Jev_Pendulum">doroper98/Jev_Pendulum</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · doroper98

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/EdwardHong0627/jev-poc">EdwardHong0627/jev-poc</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · EdwardHong0627

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/getvoicify/jev-reviewer">getvoicify/jev-reviewer</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · getvoicify

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/golergka/jev-plays-starcraft-2">golergka/jev-plays-starcraft-2</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · golergka

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/heaven-hm/jev-system-one">heaven-hm/jev-system-one</a></b> — inferred · 2 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · heaven-hm

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

</details>

<details>
<summary><b><a href="https://github.com/jamesward/jev-llm-c4">jamesward/jev-llm-c4</a></b> — Scala · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Scala · jamesward

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/jdhornsby/typesafe-jev">jdhornsby/typesafe-jev</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · jdhornsby

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-master">kevin9327/jev-master</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · kevin9327

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Typed System One decisions with Jev: Choice + Score + Noul composed in code.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevin9327--jev-master/cbf05c4561269075.png" width="100%" alt="kevin9327/jev-master screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kong75/jev-directory">kong75/jev-directory</a></b> — Astro · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Astro · kong75

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A curated directory of Jev projects, examples, and patterns.

</details>

<details>
<summary><b><a href="https://github.com/kspviswa/chakravyuha-jev">kspviswa/chakravyuha-jev</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · MIT · kspviswa

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kspviswa--chakravyuha-jev/4dfa22d0de9f27c1.png" width="100%" alt="kspviswa/chakravyuha-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/lalitsonawane/jev-one-system">lalitsonawane/jev-one-system</a></b> — inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · lalitsonawane

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/LingXuanYin/jev-chat">LingXuanYin/jev-chat</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · NOASSERTION · LingXuanYin

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Jev 聊天机：一个「只选不写」的聊天机——每个回复由逐词选择拼装，词典+分级索引+输入法式联想，由真实 Jev（TypeSafe System One）驱动。非官方实验，与 TypeSafe AI 无关联。

</details>

<details>
<summary><b><a href="https://github.com/lookfwd/jev-fact-checker">lookfwd/jev-fact-checker</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · lookfwd

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Uses Typesafe AI Jev to Provide A Tweet Fact Checker

</details>

<details>
<summary><b><a href="https://github.com/manikanda-kumar/jev-dspy-control-plane">manikanda-kumar/jev-dspy-control-plane</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · manikanda-kumar

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-poker">meetr1912/jev-poker</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · meetr1912

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 4 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Watch Jev (TypeSafe) play heads-up No-Limit Hold'em, with decision probabilities on the side panel. Money/points scoreboard, offline CI, no secrets.

</details>

<details>
<summary><b><a href="https://github.com/memorysaver/jev-atari-lab">memorysaver/jev-atari-lab</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · GPL-2.0 · memorysaver

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Challenge Atari with Jev: structured decisions, value questions, and replayable experiments

</details>

<details>
<summary><b><a href="https://github.com/MrDesjardins/jev-send-guard">MrDesjardins/jev-send-guard</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MrDesjardins

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/Nachom3/jevTrader">Nachom3/jevTrader</a></b> — Rust · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Rust · Nachom3

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A High Frecuncy Trader made in Rust using Jev as a decision maker.

</details>

<details>
<summary><b><a href="https://github.com/nardinmarcus/pi-jev-typesafe">nardinmarcus/pi-jev-typesafe</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · nardinmarcus

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model discovery, and budget caps

</details>

<details>
<summary><b><a href="https://github.com/Nolane-x/JEV-language">Nolane-x/JEV-language</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · Nolane-x

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/oguressive/sample-jev">oguressive/sample-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · oguressive

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/silverzzzzz/jev-binaryoption">silverzzzzz/jev-binaryoption</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · MIT · silverzzzzz

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/sperictao/dsh-auto-review-jev">sperictao/dsh-auto-review-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · sperictao

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/thisisjorge/jev-control-room">thisisjorge/jev-control-room</a></b> — TypeScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · thisisjorge

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Interactive control room for fast typed AI decisions with TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/TonyP-MR/jev-curation-engine">TonyP-MR/jev-curation-engine</a></b> — Python · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · TonyP-MR

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions with existing LLM audit results.

</details>

<details>
<summary><b><a href="https://github.com/toshitoshi-creator/jev-chat-site">toshitoshi-creator/jev-chat-site</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · toshitoshi-creator

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/trungdq88/jev-tetris">trungdq88/jev-tetris</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · trungdq88

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Jev play Tetris in real-time against other AI models

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/trungdq88/jev-tetris/main/docs/screenshot.png" width="100%" alt="trungdq88/jev-tetris screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/Tsagaanbayr1/jev-tetris">Tsagaanbayr1/jev-tetris</a></b> — JavaScript · inferred · 0 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · Tsagaanbayr1

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Real-time Tetris versus Jev, a TypeSafe decision model — spins, garbage, B2B chains, and decisions prefetched a piece ahead

</details>

<details>
<summary><b><a href="https://github.com/TurboGuo/jev-fedspeech">TurboGuo/jev-fedspeech</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · TurboGuo

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Real-time hawk-or-dove analysis of Fed press conferences with TypeSafe's Jev vs chat models. Live at fedspeech.pages.dev

</details>

<details>
<summary><b><a href="https://github.com/wakamenod/jev.el">wakamenod/jev.el</a></b> — Emacs Lisp · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Emacs Lisp · GPL-3.0 · wakamenod

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/waynesutton/ask-jev-ai">waynesutton/ask-jev-ai</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · waynesutton

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

A public wall where anyone asks a question in three to fifteen words and Jev, TypeSafe's judgment model, answers yes, no, or it depends in about 100 milliseconds. Every judged ask lands on the wall in realtime, with a running count toward one million, showing cost.

</details>

<details>
<summary><b><a href="https://github.com/yuki-dev26/jev-test">yuki-dev26/jev-test</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · yuki-dev26

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

ต้นทางไม่ได้เผยแพร่คำอธิบาย

</details>

<details>
<summary><b><a href="https://github.com/zaycruz/fast-jev-compaction-pi">zaycruz/fast-jev-compaction-pi</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · zaycruz

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

Verbatim Jev-guided context compaction for pi — replaces the built-in compaction summary with fast-jev decisions; stale tool calls/results dropped, everything kept stays verbatim.

</details>

<details>
<summary><b><a href="https://github.com/Zogrus/jev-technical-term">Zogrus/jev-technical-term</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · Zogrus

##### ข้อมูล

ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-19 · push ล่าสุด 2026-09-19 · ขึ้นรายการครั้งแรก 2026-09-19

##### สรุป

YouTubeの解説動画やZoomのセミナーを聞きながら、出てきた技術用語のひとこと解説をリアルタイム表示するローカルツール(判定AIは TypeSafe AI の Jev)

</details>

<details>
<summary><b><a href="https://github.com/realZachi/typesafe-adblock">realZachi/typesafe-adblock</a></b> — ⭐49 · JavaScript · unverified · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · JavaScript · MIT · realZachi

##### ข้อมูล

ดาว **49** · ฟอร์ก 4 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.

</details>

<details>
<summary><b><a href="https://github.com/razorback16/openjev">razorback16/openjev</a></b> — ⭐42 · Python · unverified · 0 天 · ⭐+6</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · Python · Apache-2.0 · razorback16

##### ข้อมูล

ดาว **42** (+6) · ฟอร์ก 6 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Open, Jev-compatible System One decision server on DiffusionGemma

</details>

<details>
<summary><b><a href="https://github.com/devanshbatham/commit-miner">devanshbatham/commit-miner</a></b> — ⭐22 · Rust · unverified · 1 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · Rust · devanshbatham

##### ข้อมูล

ดาว **22** · ฟอร์ก 5 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.

</details>

<details>
<summary><b><a href="https://github.com/phyous/tsai-sc">phyous/tsai-sc</a></b> — ⭐15 · Python · unverified · 2 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · Python · MIT · phyous

##### ข้อมูล

ดาว **15** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/phyous--tsai-sc/f48a030ae92fb1fe.png" width="100%" alt="phyous/tsai-sc screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andysc/IBM-Q-System-One-3D-model">andysc/IBM-Q-System-One-3D-model</a></b> — ⭐12 · OpenSCAD · unverified · 2688 天</summary>

##### ข้อมูลพื้นฐาน

`บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · OpenSCAD · andysc

##### ข้อมูล

ดาว **12** · ฟอร์ก 4 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2019-03-16 · push ล่าสุด 2019-05-10 · ขึ้นรายการครั้งแรก 2026-09-18

##### สรุป

3D-printed model of IBM Q System One

</details>

<a id="projects-by-implementation-language"></a>

## โปรเจกต์ตามภาษาที่ใช้พัฒนา

ระบบนิเวศกระจุกตัวอยู่ใน Python และ TypeScript แต่ไคลเอนต์แบบมีชนิดยังปรากฏในภาษาอื่นเรื่อย ๆ ตารางนี้สร้างจากตัวรายการเอง

| ภาษา       | รายการ | ตัวอย่าง                                                                                                       |
| ---------- | ------ | -------------------------------------------------------------------------------------------------------------- |
| Python     | 157    | `typesafe-ai/system-one-adapter-python`, `typesafe-ai/typesafe-sdk-python`, `ckaraca/awesome-jev`              |
| TypeScript | 136    | `typesafe-ai/typesafe-sdk-js`, `TypeSafeAI/clarity-judge`, `AntonioCoppe/jev-harness`                          |
| JavaScript | 73     | `ziyu/sytem-one-sdk`, `Ying-Kai-Liao/jev-browser`, `arunav25/jev-mcp`                                          |
| Go         | 13     | `RadixILS-Dev/typesafe-sdk-go`, `Gaurav-Gosain/jev-go`, `Stumble/jev-go`                                       |
| Rust       | 13     | `AkashPriyadarshii/jev-curate`, `AkashPriyadarshii/jev-seo`, `AkashPriyadarshii/jev-scout`                     |
| HTML       | 8      | `typesafe-ai/typesafe-ai.github.io`, `yzfly/awesome-jev-zh`, `vinilana/jev-eval-agent`                         |
| Elixir     | 3      | `nshkrdotcom/typesafe_sdk`, `typesend/typesafe_ai`, `dannote/jev`                                              |
| Jupyter    | 3      | `jexp/neo4jev`, `bitnovus/jev-spam-eval`, `aamanlamba/jev-explore`                                             |
| PHP        | 3      | `Butochnikov/laravel-typesafe-jev`, `juanlentino/jev-connector`, `soderlind/ai-provider-for-jev`               |
| Ruby       | 3      | `javiergradiche/ruby_llm-providers-typesafe`, `obie/ruby_decision_model`, `robzolkos/omarchy-issue-classifier` |
| Shell      | 3      | `realZachi/pg-jev`, `wotai-dev/typesafe-jev-tools`, `JYeswak/jev_playground`                                   |
| Java       | 2      | `Premo-Cloud/typesafe-sdk-java`, `Olti1947/jev-java`                                                           |
| Swift      | 2      | `gpazo/jev-vphone-cli`, `chris-wozniczek/jev-voice-control`                                                    |
| Astro      | 1      | `kong75/jev-directory`                                                                                         |
| C          | 1      | `giuliosmall/pg_typesafe`                                                                                      |
| C#         | 1      | `saibimajdi/typesafeai-dotnet-sdk`                                                                             |
| C++        | 1      | `amansoory/JEV2048`                                                                                            |
| CSS        | 1      | `AbdelStark/awesome-typesafe`                                                                                  |
| Dart       | 1      | `Bud-ro/jev-demos`                                                                                             |
| Emacs Lisp | 1      | `wakamenod/jev.el`                                                                                             |
| Haskell    | 1      | `inanna-malick/jev-dsl`                                                                                        |
| Kotlin     | 1      | `ufec/jev-block-android-ad`                                                                                    |
| Lex        | 1      | `alpibrusl/lex-judge`                                                                                          |
| Nushell    | 1      | `cablehead/jev.nu`                                                                                             |
| OpenSCAD   | 1      | `andysc/IBM-Q-System-One-3D-model`                                                                             |
| PowerShell | 1      | `omni-/ask-jev`                                                                                                |
| Scala      | 1      | `jamesward/jev-llm-c4`                                                                                         |
| TeX        | 1      | `dnakhoa/jev-deferred-crispification`                                                                          |

<sub>นับเฉพาะรายการที่ระบุภาษา ส่วนรายการที่เป็นโครงสร้างพื้นฐาน เอกสาร และการสนทนาไม่รวมอยู่ในตารางนี้</sub>

## รายการนี้เป็นปัจจุบันได้อย่างไร

ไม่มีมนุษย์แก้เนื้อหาของ README นี้ รีโพซิทอรีรันไปป์ไลน์ห้าขั้นตามกำหนดเวลา และ commit เฉพาะเมื่อมีการเปลี่ยนแปลงจริงเท่านั้น

<img src="assets/readme/pipeline.svg" width="100%" alt="รายการนี้เป็นปัจจุบันได้อย่างไร">

|             |                                                                                                                                                                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **collect** | ค้นหาบน GitHub ผ่านเมทริกซ์คำค้น องค์กรทางการ การค้นหาโค้ดของ GitHub, Hacker News และฮับ Hugging Face                                                                                                                                                              |
| **curate**  | เป็นดีเทอร์มินิสติกและไม่ใช้ LLM ดังนั้นการรันสองครั้งติดกันบนอินพุตเดียวกันจึงให้ผลลัพธ์เหมือนกันทุกไบต์ กฎสองสัญญาณตัดสินความเกี่ยวข้อง ชื่อที่ชนกัน (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD และทำนองเดียวกัน) ถูกตัดออกด้วยรายการที่ชัดเจนและตรวจสอบได้ |
| **media**   | เก็บภาพหน้าจอและบันทึกหน้าจอของแต่ละโปรเจกต์ ไฟล์จะถูกคัดลอกเข้ามาในรีโพซิทอรีนี้เฉพาะเมื่อโปรเจกต์ประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ มิฉะนั้นจะฮอตลิงก์ URL ต้นทาง และการ์ดจะระบุไว้                                                                       |
| **render**  | สร้างทุกฉบับภาษาจากเทมเพลตเดียว ดังนั้น README ทั้งยี่สิบฉบับจึงไม่มีทางต่างกันในโครงสร้าง                                                                                                                                                                         |
| **audit**   | ทำให้บิลด์ล้มเหลวถ้ารายการหนึ่งไม่มี URL ถ้าลิงก์ตาย ถ้าสองรายการมี URL ซ้ำกัน หรือถ้า README เบี่ยงจากรูปแบบที่สร้างขึ้น                                                                                                                                          |

## การมีส่วนร่วม

ยินดีรับการแก้ไข และนั่นเป็นวิธีที่เร็วที่สุดในการปรับปรุงรายการนี้ เปิด issue หรือ pull request หากรายการถูกจัดหมวดผิด ให้เกรดผิด หรือมีโปรเจกต์ถูกตัดออกผิดเพราะเข้าใจว่าเป็นชื่อที่ชนกัน — หมวดหลังนี้คือจุดที่ตัวกรองอัตโนมัติมีโอกาสผิดมากที่สุด วิธีเพิ่มรายการที่ดีที่สุดคือเพิ่มแหล่งข้อมูลใน `scripts/collect.py` แทนการแก้ README เพราะ README ถูกสร้างใหม่ทุกรอบ

---

<sub>โปรเจกต์ชุมชนอิสระ ไม่มีความเกี่ยวข้อง ไม่ได้รับการรับรอง และไม่ได้รับการตรวจทานโดย TypeSafe AI พฤติกรรมผลิตภัณฑ์ ราคา ขีดจำกัด และนามแฝงโมเดลเปลี่ยนแปลงได้โดยไม่แจ้งล่วงหน้า โปรดตรวจสอบสิ่งที่เป็นข้อสำคัญกับเอกสารทางการ ไฟล์ต่าง ๆ ยังเป็นทรัพย์สินของโปรเจกต์ต้นทาง และถูกทำซ้ำเฉพาะเมื่อสัญญาอนุญาตเอื้อให้เท่านั้น</sub>

<sub>สร้างโดย · `render.py` · 2026-09-19T10:20:34+08:00</sub>
