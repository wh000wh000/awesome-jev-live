<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>ดัชนี Jev ที่จัดเกรดตามหลักฐาน และสร้างตัวเองใหม่ทุกสองชั่วโมง</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-404-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <b>ไทย</b> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **ดัชนีสด** · ซิงค์ล่าสุด: `2026-09-18T21:49:39+08:00` (UTC+8)
> · รายการ: **404** · ใหม่ในรอบนี้: **404** · ภาษาที่ใช้พัฒนา: **22**

<sub>ทุกรายการด้านล่างถูกรวบรวม กรอง และตรวจซ้ำโดยไปป์ไลน์ในรีโพซิทอรีนี้ ตัวเลขและเวลาประทับมาจากแหล่งข้อมูล ไม่ใช่จากสแนปช็อตที่เขียนด้วยมือ</sub>

## Jev คืออะไร?

Jev คือ **System One model** ตัวแรกของ TypeSafe AI มันไม่เขียนข้อความบรรยาย แต่รับสถานะพร้อมคำถามที่คุณกำหนดชุดคำตอบไว้ล่วงหน้า แล้วคืนค่าแบบมีชนิดพร้อมการแจกแจงความน่าจะเป็นที่โค้ดของคุณใช้แยกทางได้

- **รูปแบบ:** `state + typed questions` → `constrained answers + probabilities` → `your code`
- **พื้นฐาน:** `Choice` (เลือกหนึ่งในไม่เกิน 255 ตัวเลือก), `Score` (รูบริก 2–10), `Noul` (ใช่/ไม่ใช่ เชิงความน่าจะเป็น)
- **เอนด์พอยต์:** `POST https://api.typesafe.ai/v1/systemone`, โมเดล `jev-1.13.0` / นามแฝง `jev-latest`
- **เหมาะกับ:** การจัดเส้นทาง การคัดแยก การให้คะแนน การกลั่นกรอง การตรวจสอบ และเกตความหน่วงต่ำภายในเวิร์กโฟลว์ที่มีขอบเขต
- **ข้อจำกัดที่ทราบ:** การนับไม่น่าเชื่อถือ การอ้างอิงหลายชั้นยังอ่อน และเอกสารทางการระบุความขรุขระไว้เก้าประเภท เอาต์พุตที่ถูกต้องตามสคีมาไม่เท่ากับการตัดสินใจที่ถูกต้อง — ควรคาลิเบรตกับข้อมูลของคุณเอง

## การจัดเกรดรายการ

รายการส่วนใหญ่ในสายนี้อ้างว่าทุกรายการถูกรวมไว้ ที่นี่บอกว่าตรวจสอบได้จริงมากแค่ไหน แล้วให้คุณกรองตามนั้น

| เกรด | ความหมาย |
| --- | --- |
| `official` | เผยแพร่โดย TypeSafe AI เอง |
| `observed` | ชิ้นงานสาธารณะที่เปิดอ่านได้ — ซอร์สโค้ดจริง คอนฟิกจริง หรือการประกาศ TypeSafe/Jev อย่างชัดเจนในชื่อหรือหัวข้อของรีโพซิทอรี |
| `inferred` | จับคู่ได้จากสัญญาณที่คลุมเครือบวกคำศัพท์ที่สอดคล้องกัน แต่ยังไม่ได้อ่านทีละบรรทัด |
| `unverified` | ดูเกี่ยวข้อง แต่ยังไม่มีอะไรยืนยันได้อย่างอิสระ ขึ้นรายการไว้เพื่อการค้นพบเท่านั้น |

## สารบัญ

- [SDK ทางการและเครื่องมือสำหรับนักพัฒนา](#official-sdk) — **6**
- [ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน](#community-sdk) — **70**
- [เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด](#agent-tooling) — **112**
- [การจัดเส้นทาง การ์ดเรล และการอนุมัติ](#routing-guardrails) — **40**
- [การประเมิน การคาลิเบรต และเบนช์มาร์ก](#evaluation) — **29**
- [งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม](#research-models) — **12**
- [แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ](#apps-demos) — **38**
- [บทความ การสนทนา และรายการที่เกี่ยวข้อง](#media-discussions) — **97**
- [โปรเจกต์ตามภาษาที่ใช้พัฒนา](#projects-by-implementation-language)

<a id="official-sdk"></a>

## SDK ทางการและเครื่องมือสำหรับนักพัฒนา <sub>· 6</sub>

ทุกอย่างที่ TypeSafe เผยแพร่เอง เริ่มจากตรงนี้

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐185 · official · 6 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · MIT · [typesafe-ai](https://github.com/typesafe-ai)

**ข้อมูล** · ดาว **185** · ฟอร์ก 10 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-08-24 · push ล่าสุด 2026-09-12 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐107 · TypeScript · official · 2 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · TypeScript · MIT · [typesafe-ai](https://github.com/typesafe-ai)

**ข้อมูล** · ดาว **107** · ฟอร์ก 6 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2026-09-04 · push ล่าสุด 2026-09-15 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐100 · Python · official · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · Python · MIT · [typesafe-ai](https://github.com/typesafe-ai)

**ข้อมูล** · ดาว **100** · ฟอร์ก 8 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-08-08 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>พบการใช้งานในโค้ด: `README.md`, `src/system_one_adapter/__init__.py`, `src/system_one_adapter/_response.py`, `src/system_one_adapter/_utils/error_handling.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐73 · Python · official · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · Python · MIT · [typesafe-ai](https://github.com/typesafe-ai)

**ข้อมูล** · ดาว **73** · ฟอร์ก 5 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-04 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>พบการใช้งานในโค้ด: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 105 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ทางการ · `official` · HTML · [typesafe-ai](https://github.com/typesafe-ai)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2024-05-28 · push ล่าสุด 2026-06-04 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/NicolasMontone/jev-evals">NicolasMontone/jev-evals</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `SDK ทางการและเครื่องมือสำหรับนักพัฒนา` · ชุมชน · `inferred` · TypeScript · [NicolasMontone](https://github.com/NicolasMontone)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Rubric-based eval harness cheap enough to run on every PR, powered by typesafe-ai/jev

</details>

<a id="community-sdk"></a>

## ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน <sub>· 70</sub>

ไคลเอนต์แบบมีชนิดสำหรับเอนด์พอยต์ System One ครอบคลุมภาษาต่าง ๆ เท่าที่ชุมชนทำไปถึง

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐120 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Python · NOASSERTION · [realZachi](https://github.com/realZachi)

**ข้อมูล** · ดาว **120** · ฟอร์ก 5 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

<sub>พบการใช้งานในโค้ด: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐15 · Jupyter · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Jupyter · MIT · [jexp](https://github.com/jexp)

**ข้อมูล** · ดาว **15** · ฟอร์ก 2 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · TypeScript · MIT · [AntonioCoppe](https://github.com/AntonioCoppe)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Python · CC0-1.0 · [MrJev](https://github.com/MrJev)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · TypeScript · [opaielsheikh](https://github.com/opaielsheikh)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐1 · Rust · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Rust · MIT · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐1 · Elixir · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Elixir · MIT · [nshkrdotcom](https://github.com/nshkrdotcom)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · JavaScript · MIT · [ziyu](https://github.com/ziyu)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/ehmpathy/rhachet-brains-typesafeai">ehmpathy/rhachet-brains-typesafeai</a></b> — observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · MIT · [ehmpathy](https://github.com/ehmpathy)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

rhachet brain.atom adapter for typesafe.ai classifier models

</details>

<details>
<summary><b><a href="https://github.com/ivorpad/skillranker">ivorpad/skillranker</a></b> — observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · NOASSERTION · [ivorpad](https://github.com/ivorpad)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Ruby · MIT · [javiergradiche](https://github.com/javiergradiche)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/jonesmelton/verdict">jonesmelton/verdict</a></b> — OCaml · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · OCaml · MIT · [jonesmelton](https://github.com/jonesmelton)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

ocaml sdk for typesafe.ai's jev model

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · TypeScript · [nu-sync](https://github.com/nu-sync)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — Java · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Java · MIT · [Premo-Cloud](https://github.com/Premo-Cloud)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Elixir · MIT · [typesend](https://github.com/typesend)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `observed` · Python · [xingwudao](https://github.com/xingwudao)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐20 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · [nidhi-singh02](https://github.com/nidhi-singh02)

**ข้อมูล** · ดาว **20** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">รับชมบน img.youtube.com</a> · การเล่นจะเปิดบนเว็บไซต์ต้นทาง GitHub ไม่สามารถฝังแบบอินไลน์ได้</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gamesonrblx/Jevbridge">gamesonrblx/Jevbridge</a></b> — ⭐12 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · [gamesonrblx](https://github.com/gamesonrblx)

**ข้อมูล** · ดาว **12** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

> Bridges the typed-decision layer to the agent protocols other tools already speak.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gamesonrblx--jevbridge/772995670b3e42e9.png" width="100%" alt="gamesonrblx/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐10 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · [shiftynick](https://github.com/shiftynick)

**ข้อมูล** · ดาว **10** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐9 · Elixir · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Elixir · MIT · [dannote](https://github.com/dannote)

**ข้อมูล** · ดาว **9** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐7 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · MIT · [Ying-Kai-Liao](https://github.com/Ying-Kai-Liao)

**ข้อมูล** · ดาว **7** · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐6 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [AboveColin](https://github.com/AboveColin)

**ข้อมูล** · ดาว **6** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Home Assistant integration for TypeSafe Jev. Ask a question about your house and get a probability, a choice or a score as an entity.

</details>

<details>
<summary><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">saibimajdi/typesafeai-dotnet-sdk</a></b> — ⭐5 · C# · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · C# · MIT · [saibimajdi](https://github.com/saibimajdi)

**ข้อมูล** · ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/sharziki/semdecide">sharziki/semdecide</a></b> — ⭐5 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [sharziki](https://github.com/sharziki)

**ข้อมูล** · ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.

</details>

<details>
<summary><b><a href="https://github.com/arunav25/jev-mcp">arunav25/jev-mcp</a></b> — ⭐3 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · MIT · [arunav25](https://github.com/arunav25)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.

</details>

<details>
<summary><b><a href="https://github.com/docxology/daf-jev">docxology/daf-jev</a></b> — ⭐3 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [docxology](https://github.com/docxology)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill

</details>

<details>
<summary><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Butochnikov/laravel-typesafe-jev</a></b> — ⭐2 · PHP · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · PHP · MIT · [Butochnikov](https://github.com/Butochnikov)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes.

</details>

<details>
<summary><b><a href="https://github.com/romaluev/jev-ego">romaluev/jev-ego</a></b> — ⭐2 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · NOASSERTION · [romaluev](https://github.com/romaluev)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move.

</details>

<details>
<summary><b><a href="https://github.com/tumf/jev-cli">tumf/jev-cli</a></b> — ⭐2 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [tumf](https://github.com/tumf)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Small dependency-free CLI for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/yzfly/awesome-jev-zh">yzfly/awesome-jev-zh</a></b> — ⭐2 · HTML · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · HTML · CC0-1.0 · [yzfly](https://github.com/yzfly)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/jevclient">AboveColin/jevclient</a></b> — ⭐1 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [AboveColin](https://github.com/AboveColin)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.

</details>

<details>
<summary><b><a href="https://github.com/burnigtm/jev-mcp">burnigtm/jev-mcp</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · [burnigtm](https://github.com/burnigtm)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client

</details>

<details>
<summary><b><a href="https://github.com/felpsdev/jev-classifier">felpsdev/jev-classifier</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · [felpsdev](https://github.com/felpsdev)

**ข้อมูล** · ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/felpsdev--jev-classifier/d753de26b0e6c7b6.webp" width="100%" alt="felpsdev/jev-classifier screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-go">Gaurav-Gosain/jev-go</a></b> — ⭐1 · Go · inferred · 2 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · [Gaurav-Gosain](https://github.com/Gaurav-Gosain)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/himomohi/aside-jev">himomohi/aside-jev</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [himomohi](https://github.com/himomohi)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.

</details>

<details>
<summary><b><a href="https://github.com/jtsang4/jev-cli">jtsang4/jev-cli</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · [jtsang4](https://github.com/jtsang4)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

CLI for TypeSafe AI's Jev evaluation model — typed questions in, structured JSON answers out

</details>

<details>
<summary><b><a href="https://github.com/Olti1947/jev-java">Olti1947/jev-java</a></b> — ⭐1 · Java · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Java · [Olti1947](https://github.com/Olti1947)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Idiomatic Java SDK for TypeSafe AI Jev System One decision engine

</details>

<details>
<summary><b><a href="https://github.com/StefanoITA/ts-jev-cost-calculator">StefanoITA/ts-jev-cost-calculator</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [StefanoITA](https://github.com/StefanoITA)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe.

</details>

<details>
<summary><b><a href="https://github.com/Stumble/jev-go">Stumble/jev-go</a></b> — ⭐1 · Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · [Stumble](https://github.com/Stumble)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Community Go SDK for TypeSafe AI Jev / System One

</details>

<details>
<summary><b><a href="https://github.com/tontoko/jev-browser">tontoko/jev-browser</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · Apache-2.0 · [tontoko](https://github.com/tontoko)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.

</details>

<details>
<summary><b><a href="https://github.com/abeldzan/jev-rs">abeldzan/jev-rs</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Rust · MIT · [abeldzan](https://github.com/abeldzan)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Async-first Rust SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-git">AkashPriyadarshii/jev-git</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Rust · MIT · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-scout">AkashPriyadarshii/jev-scout</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Rust · MIT · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-seo">AkashPriyadarshii/jev-seo</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Rust · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">AkashPriyadarshii/jev-superpowers</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · JavaScript · MIT · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions

</details>

<details>
<summary><b><a href="https://github.com/anilsenay/jev">anilsenay/jev</a></b> — Go · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · [anilsenay](https://github.com/anilsenay)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Unofficial Go client for TypeSafe's System One API  and its model, Jev.

</details>

<details>
<summary><b><a href="https://github.com/brnyxx/jev-ra">brnyxx/jev-ra</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [brnyxx](https://github.com/brnyxx)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7592fce4641d10.png" width="100%" alt="brnyxx/jev-ra screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7ddcd1053825a2.gif" width="100%" alt="brnyxx/jev-ra animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/david1gp/jev">david1gp/jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · [david1gp](https://github.com/david1gp)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Result-based TypeSafe System One client library and jev command-line interface.

</details>

<details>
<summary><b><a href="https://github.com/kazz187/jev-sdk-go">kazz187/jev-sdk-go</a></b> — Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · [kazz187](https://github.com/kazz187)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Go 1.27 client for TypeSafe AI's Jev (System One) API: typed questions, typed answers

</details>

<details>
<summary><b><a href="https://github.com/krw82/jev-playwright-mcp">krw82/jev-playwright-mcp</a></b> — TypeScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · [krw82](https://github.com/krw82)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.

</details>

<details>
<summary><b><a href="https://github.com/kunobi-ninja/kunobi-jev">kunobi-ninja/kunobi-jev</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Rust · Apache-2.0 · [kunobi-ninja](https://github.com/kunobi-ninja)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Rust client for the TypeSafe System One API (Jev)

</details>

<details>
<summary><b><a href="https://github.com/lhotwll217/jev-cli">lhotwll217/jev-cli</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · [lhotwll217](https://github.com/lhotwll217)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

JSON-in, typed-decisions-out CLI for the TypeSafe System One API

</details>

<details>
<summary><b><a href="https://github.com/manojlds/jev-review">manojlds/jev-review</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · [manojlds](https://github.com/manojlds)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Standalone TypeSafe Jev code-review CLI: typed decisions over a local git diff.

</details>

<details>
<summary><b><a href="https://github.com/mhmdkzr/jev">mhmdkzr/jev</a></b> — Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · [mhmdkzr](https://github.com/mhmdkzr)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

An unofficial Go client for TypeSafe's System One Jev model

</details>

<details>
<summary><b><a href="https://github.com/mzainzulifqar/jev-php-sdk">mzainzulifqar/jev-php-sdk</a></b> — PHP · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · PHP · MIT · [mzainzulifqar](https://github.com/mzainzulifqar)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

PHP SDK for TypeSafe's Jev: send text and typed questions, get typed answers with calibrated confidence. PHP 8.1+, works with any PSR-18 client, Laravel 8–13.

</details>

<details>
<summary><b><a href="https://github.com/Nasrallah-AL/jev-cli">Nasrallah-AL/jev-cli</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · TypeScript · MIT · [Nasrallah-AL](https://github.com/Nasrallah-AL)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Command-line tool for TypeSafe's Jev AI model

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-go">nekowasabi/jev-routing-go</a></b> — Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · [nekowasabi](https://github.com/nekowasabi)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.

</details>

<details>
<summary><b><a href="https://github.com/okooo5km/jev">okooo5km/jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · Apache-2.0 · [okooo5km](https://github.com/okooo5km)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed decisions from the shell: a stdlib-Python CLI and Agent Skill for TypeSafe Jev on OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch mode.

</details>

<details>
<summary><b><a href="https://github.com/phuthuycoding/jev-audit">phuthuycoding/jev-audit</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · [phuthuycoding](https://github.com/phuthuycoding)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

AI-powered pre-commit auditor backed by TypeSafe System One (Jev) — blocks secrets, vulns & low-quality code in ~300ms. 79-case test corpus at 100% accuracy.

</details>

<details>
<summary><b><a href="https://github.com/shanginn/jev-php">shanginn/jev-php</a></b> — PHP · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · PHP · MIT · [shanginn](https://github.com/shanginn)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Type-safe PHP 8.5 SDK for JEV decisions on OpenRouter: choices, scores, probabilities and typed DTOs.

</details>

<details>
<summary><b><a href="https://github.com/vayungodara/jev-lint">vayungodara/jev-lint</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [vayungodara](https://github.com/vayungodara)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Lint a Markdown knowledge base (Obsidian vault or LLM wiki) for contradictions, stale claims, unresolved markers and missing pages, using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Python · MIT · [WiktorB2004](https://github.com/WiktorB2004)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

LlamaIndex reranker and selector integrations for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/zhirschtritt/typesafe-go">zhirschtritt/typesafe-go</a></b> — Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `inferred` · Go · MIT · [zhirschtritt](https://github.com/zhirschtritt)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Idiomatic Go SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/pithings/advocaat">pithings/advocaat</a></b> — ⭐63 · TypeScript · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · TypeScript · MIT · [pithings](https://github.com/pithings)

**ข้อมูล** · ดาว **63** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/Tangerg/typesafe-sdk-go">Tangerg/typesafe-sdk-go</a></b> — ⭐7 · Go · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · Go · MIT · [Tangerg](https://github.com/Tangerg)

**ข้อมูล** · ดาว **7** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Go SDK for the TypeSafe AI API — typed questions in, probability distributions out.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/typesafe-cli">y0usaf/typesafe-cli</a></b> — ⭐4 · TypeScript · unverified · 2 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · TypeScript · MIT · [y0usaf](https://github.com/y0usaf)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose

</details>

<details>
<summary><b><a href="https://github.com/frostney/clean-code-review">frostney/clean-code-review</a></b> — ⭐3 · TypeScript · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · TypeScript · MIT · [frostney](https://github.com/frostney)

**ข้อมูล** · ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/frostney--clean-code-review/7d8a8de446e1c27b.png" width="100%" alt="frostney/clean-code-review screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/geilt/typesafe-cli">geilt/typesafe-cli</a></b> — ⭐3 · Python · unverified · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · Python · [geilt](https://github.com/geilt)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.

</details>

<details>
<summary><b><a href="https://github.com/gilljon/typesafe-ai-rs">gilljon/typesafe-ai-rs</a></b> — ⭐3 · Rust · unverified · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · Rust · MIT · [gilljon](https://github.com/gilljon)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Independent async and blocking Rust SDK for the TypeSafe AI System One API

</details>

<details>
<summary><b><a href="https://github.com/giuliosmall/pg_typesafe">giuliosmall/pg_typesafe</a></b> — ⭐3 · C · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `ไคลเอนต์ SDK และอะแดปเตอร์จากชุมชน` · ชุมชน · `unverified` · C · MIT · [giuliosmall](https://github.com/giuliosmall)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification

</details>

<a id="agent-tooling"></a>

## เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด <sub>· 112</sub>

หมวดที่โตเร็วที่สุด: ฮุก เซิร์ฟเวอร์ MCP และเกตที่วางการตัดสินใจแบบมีชนิดไว้หน้าการกระทำถัดไปของเอเจนต์

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐2375 · TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · MIT · [tamaratran](https://github.com/tamaratran)

**ข้อมูล** · ดาว **2375** · ฟอร์ก 119 · issue ที่เปิดอยู่ 38 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>พบการใช้งานในโค้ด: `src/request.ts`, `README.md`, `src/client.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐112 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [gargpratyush](https://github.com/gargpratyush)

**ข้อมูล** · ดาว **112** · ฟอร์ก 4 · issue ที่เปิดอยู่ 4 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐25 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [0xNatoshi](https://github.com/0xNatoshi)

**ข้อมูล** · ดาว **25** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐70 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · [dbreunig](https://github.com/dbreunig)

**ข้อมูล** · ดาว **70** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐11 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · [GhalebDweikat](https://github.com/GhalebDweikat)

**ข้อมูล** · ดาว **11** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · [carlaiau](https://github.com/carlaiau)

**ข้อมูล** · ดาว **7** · ฟอร์ก 1 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2026-03-13 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · [jodan-alberts](https://github.com/jodan-alberts)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · MIT · [BYK](https://github.com/BYK)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · [24601](https://github.com/24601)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · [CrowBe](https://github.com/CrowBe)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · TypeScript · MIT · [gorock007](https://github.com/gorock007)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `observed` · Python · MIT · [yousudip](https://github.com/yousudip)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐227 · TypeScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [devagrawal09](https://github.com/devagrawal09)

**ข้อมูล** · ดาว **227** · ฟอร์ก 12 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐103 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [NiazMorshed2007](https://github.com/NiazMorshed2007)

**ข้อมูล** · ดาว **103** · ฟอร์ก 9 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-eval-agent">vinilana/jev-eval-agent</a></b> — ⭐78 · HTML · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · HTML · [vinilana](https://github.com/vinilana)

**ข้อมูล** · ดาว **78** · ฟอร์ก 6 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-mcp">jkudish/jev-mcp</a></b> — ⭐65 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [jkudish](https://github.com/jkudish)

**ข้อมูล** · ดาว **65** · ฟอร์ก 8 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Proof of concept MCP for Typesafe's new Jev AI model

> An early proof of concept for exposing Jev over MCP, which is how most non-Python toolchains reach it.

</details>

<details>
<summary><b><a href="https://github.com/RomanSlack/jev-drone">RomanSlack/jev-drone</a></b> — ⭐56 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [RomanSlack](https://github.com/RomanSlack)

**ข้อมูล** · ดาว **56** · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/romanslack--jev-drone/b23ea2412f437970.png" width="100%" alt="RomanSlack/jev-drone screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/pi-jev">y0usaf/pi-jev</a></b> — ⭐38 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [y0usaf](https://github.com/y0usaf)

**ข้อมูล** · ดาว **38** · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/ask-jev-skill">shantanugoel/ask-jev-skill</a></b> — ⭐25 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [shantanugoel](https://github.com/shantanugoel)

**ข้อมูล** · ดาว **25** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Skill for Hermes, and other agents, to ask typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/supercorp-ai/supercov">supercorp-ai/supercov</a></b> — ⭐22 · Rust · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Rust · MIT · [supercorp-ai](https://github.com/supercorp-ai)

**ข้อมูล** · ดาว **22** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-08-23 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Code quality and coverage for coding agents

> Code quality and coverage verdicts produced as typed decisions rather than prose, so the result can gate a pipeline directly.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/supercorp-ai--supercov/063226e150cb8a6b.jpg" width="100%" alt="supercorp-ai/supercov screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wy-coliney/jev-browser-use">wy-coliney/jev-browser-use</a></b> — ⭐22 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [wy-coliney](https://github.com/wy-coliney)

**ข้อมูล** · ดาว **22** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wy-coliney--jev-browser-use/581fbd89fe47c952.png" width="100%" alt="wy-coliney/jev-browser-use screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/logicrw/awesome-jev-projects">logicrw/awesome-jev-projects</a></b> — ⭐16 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [logicrw](https://github.com/logicrw)

**ข้อมูล** · ดาว **16** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐9 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [fatwang2](https://github.com/fatwang2)

**ข้อมูล** · ดาว **9** · ฟอร์ก 3 · issue ที่เปิดอยู่ 5 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/compozy/yoshi">compozy/yoshi</a></b> — ⭐8 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [compozy](https://github.com/compozy)

**ข้อมูล** · ดาว **8** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/compozy--yoshi/637d8588c227f4de.png" width="100%" alt="compozy/yoshi screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">jomatsu/pi-jev-auto-mode</a></b> — ⭐8 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [jomatsu](https://github.com/jomatsu)

**ข้อมูล** · ดาว **8** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.

</details>

<details>
<summary><b><a href="https://github.com/blakestone-x/jev-mcp">blakestone-x/jev-mcp</a></b> — ⭐7 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [blakestone-x](https://github.com/blakestone-x)

**ข้อมูล** · ดาว **7** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer

</details>

<details>
<summary><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">DECRUX9812/typesafe-skill-router</a></b> — ⭐6 · Python · inferred · 2 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [DECRUX9812](https://github.com/DECRUX9812)

**ข้อมูล** · ดาว **6** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-code">devagrawal09/jev-code</a></b> — ⭐5 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [devagrawal09](https://github.com/devagrawal09)

**ข้อมูล** · ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Bounded TypeSafe Jev workflows for coding agents.

</details>

<details>
<summary><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">GodsBoy/jev-agent-skill-router</a></b> — ⭐5 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [GodsBoy](https://github.com/GodsBoy)

**ข้อมูล** · ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed, confidence-aware agent skill routing with TypeSafe Jev.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/godsboy--jev-agent-skill-router/c80293e37dcd4faf.png" width="100%" alt="GodsBoy/jev-agent-skill-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/huntedman/JevLint">huntedman/JevLint</a></b> — ⭐5 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [huntedman](https://github.com/huntedman)

**ข้อมูล** · ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.

</details>

<details>
<summary><b><a href="https://github.com/GiesN/typesafe-jev-workflow">GiesN/typesafe-jev-workflow</a></b> — ⭐4 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · [GiesN](https://github.com/GiesN)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/inanna-malick/jev-dsl">inanna-malick/jev-dsl</a></b> — ⭐4 · Haskell · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Haskell · MIT · [inanna-malick](https://github.com/inanna-malick)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels

</details>

<details>
<summary><b><a href="https://github.com/kikoncuo/jevfire">kikoncuo/jevfire</a></b> — ⭐4 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [kikoncuo](https://github.com/kikoncuo)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

JEV-inspired parallel decisions for CUDA LLMs. One context, many decisions. vLLM API, game-agent examples, and reproducible benchmarks.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kikoncuo--jevfire/2d5597bbc6b2c82e.png" width="100%" alt="kikoncuo/jevfire screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/TheoOliveira/pi-jev">TheoOliveira/pi-jev</a></b> — ⭐4 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [TheoOliveira](https://github.com/TheoOliveira)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/anpicasso/hermes-jev-approvals">anpicasso/hermes-jev-approvals</a></b> — ⭐3 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [anpicasso](https://github.com/anpicasso)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only.

</details>

<details>
<summary><b><a href="https://github.com/BillionsBobby/JevRouter">BillionsBobby/JevRouter</a></b> — ⭐3 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [BillionsBobby](https://github.com/BillionsBobby)

**ข้อมูล** · ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 5 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A lightweight Jev-powered router for models, tools, and subagents

</details>

<details>
<summary><b><a href="https://github.com/SeeAPI/awesome-jev-use-cases">SeeAPI/awesome-jev-use-cases</a></b> — ⭐3 · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · CC-BY-4.0 · [SeeAPI](https://github.com/SeeAPI)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/seeapi--awesome-jev-use-cases/33f9e684bff2514d.png" width="100%" alt="SeeAPI/awesome-jev-use-cases screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-shield">caiovicentino/jev-shield</a></b> — ⭐2 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [caiovicentino](https://github.com/caiovicentino)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check.

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/jev-judgment">HyunjunJeon/jev-judgment</a></b> — ⭐2 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [HyunjunJeon](https://github.com/HyunjunJeon)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Agent Skill: send closed coding-agent judgments to TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/molis-ai/jev-workbench">molis-ai/jev-workbench</a></b> — ⭐2 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [molis-ai](https://github.com/molis-ai)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/molis-ai--jev-workbench/00f61d8403a941cd.png" width="100%" alt="molis-ai/jev-workbench screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MongLong0214/jev-gate">MongLong0214/jev-gate</a></b> — ⭐2 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · [MongLong0214](https://github.com/MongLong0214)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 5 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.

</details>

<details>
<summary><b><a href="https://github.com/ranjan2829/AskJev">ranjan2829/AskJev</a></b> — ⭐2 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [ranjan2829](https://github.com/ranjan2829)

**ข้อมูล** · ดาว **2** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-mcp">rashedInt32/jev-mcp</a></b> — ⭐2 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [rashedInt32](https://github.com/rashedInt32)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/samtay32/jev-system-architect">samtay32/jev-system-architect</a></b> — ⭐2 · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · MIT · [samtay32](https://github.com/samtay32)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives.

</details>

<details>
<summary><b><a href="https://github.com/anandi1989/awesome-jev-usecases">anandi1989/awesome-jev-usecases</a></b> — ⭐1 · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · MIT · [anandi1989](https://github.com/anandi1989)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results

</details>

<details>
<summary><b><a href="https://github.com/bestagentkits/jev-skillful">bestagentkits/jev-skillful</a></b> — ⭐1 · TypeScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [bestagentkits](https://github.com/bestagentkits)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.

</details>

<details>
<summary><b><a href="https://github.com/buchmark/claude-jev">buchmark/claude-jev</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [buchmark](https://github.com/buchmark)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Claude Code plugin that scores review findings, debug hypotheses and design options with TypeSafe's Jev — calibrated probabilities instead of one more opinion.

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-starter">hamakyo/jev-starter</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [hamakyo](https://github.com/hamakyo)

**ข้อมูล** · ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.

</details>

<details>
<summary><b><a href="https://github.com/harrymunro/jev-first">harrymunro/jev-first</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [harrymunro](https://github.com/harrymunro)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Agent skill that spots bounded-judgment steps, tries TypeSafe's Jev first, and documents every attempt

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-model-router-demo">jcpsimmons/jev-model-router-demo</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · [jcpsimmons](https://github.com/jcpsimmons)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

</details>

<details>
<summary><b><a href="https://github.com/omni-/ask-jev">omni-/ask-jev</a></b> — ⭐1 · PowerShell · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · PowerShell · MIT · [omni-](https://github.com/omni-)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions.

</details>

<details>
<summary><b><a href="https://github.com/poponline63/hermes-jev-north-star">poponline63/hermes-jev-north-star</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [poponline63](https://github.com/poponline63)

**ข้อมูล** · ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven.

</details>

<details>
<summary><b><a href="https://github.com/Ravinder82/jev-flash-router">Ravinder82/jev-flash-router</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [Ravinder82](https://github.com/Ravinder82)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code

</details>

<details>
<summary><b><a href="https://github.com/rthomas24/jev-realtime-trading">rthomas24/jev-realtime-trading</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [rthomas24](https://github.com/rthomas24)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rthomas24--jev-realtime-trading/f27df5cca6b8e2cf.png" width="100%" alt="rthomas24/jev-realtime-trading screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/codex-jev-compaction">Wang-auspicious/codex-jev-compaction</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [Wang-auspicious](https://github.com/Wang-auspicious)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills.

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/pi-jev-compaction">Wang-auspicious/pi-jev-compaction</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [Wang-auspicious](https://github.com/Wang-auspicious)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev-powered context compaction for Pi. Keep critical instructions and tool history, prune the noise, and fall back gracefully.

</details>

<details>
<summary><b><a href="https://github.com/ably-labs/jev-pong">ably-labs/jev-pong</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · Apache-2.0 · [ably-labs](https://github.com/ably-labs)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Pong where the ball moves one step per model decision. Jev vs LLMs via Vercel AI Gateway, every player and agent on an Ably channel.

</details>

<details>
<summary><b><a href="https://github.com/aidil2105/jev-browser-pilot">aidil2105/jev-browser-pilot</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [aidil2105](https://github.com/aidil2105)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification.

</details>

<details>
<summary><b><a href="https://github.com/altregubov/jev-antigravity-mcp">altregubov/jev-antigravity-mcp</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · [altregubov](https://github.com/altregubov)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/anisselbd/jev-phishing-bench">anisselbd/jev-phishing-bench</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · [anisselbd](https://github.com/anisselbd)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.

</details>

<details>
<summary><b><a href="https://github.com/Calq-dev/ask-jev">Calq-dev/ask-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · [Calq-dev](https://github.com/Calq-dev)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Ask Jev a question about a file instead of reading it into the agent's context.

</details>

<details>
<summary><b><a href="https://github.com/cbruyndoncx/AskJev-MCP">cbruyndoncx/AskJev-MCP</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · [cbruyndoncx](https://github.com/cbruyndoncx)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence

</details>

<details>
<summary><b><a href="https://github.com/CodeAlive-AI/mastra-jev-moderation">CodeAlive-AI/mastra-jev-moderation</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [CodeAlive-AI](https://github.com/CodeAlive-AI)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Input moderation for Mastra agents on TypeSafe Jev — one file

</details>

<details>
<summary><b><a href="https://github.com/dg-coreylweathers/jev-voice-agent">dg-coreylweathers/jev-voice-agent</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [dg-coreylweathers](https://github.com/dg-coreylweathers)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A realtime voice agent with no LLM in the loop: Deepgram Flux ends the turn, TypeSafe's Jev picks the reply, Deepgram Flux TTS speaks it.

</details>

<details>
<summary><b><a href="https://github.com/doeixd/jev-pref">doeixd/jev-pref</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [doeixd](https://github.com/doeixd)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.

</details>

<details>
<summary><b><a href="https://github.com/DoGMaTiiC/hermes-jev">DoGMaTiiC/hermes-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · [DoGMaTiiC](https://github.com/DoGMaTiiC)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 7 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only.

</details>

<details>
<summary><b><a href="https://github.com/dryob/hermes-jev-context-engine">dryob/hermes-jev-context-engine</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · NOASSERTION · [dryob](https://github.com/dryob)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Lossless context compaction for Hermes Agent via the TypeSafe/Jev API — deletes or truncates stale tool calls instead of summarising. Python port of tamaratran/fast-jev-compaction.

</details>

<details>
<summary><b><a href="https://github.com/duketopceo/jev-compact">duketopceo/jev-compact</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [duketopceo](https://github.com/duketopceo)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP

</details>

<details>
<summary><b><a href="https://github.com/EliaAlberti/jev-rules">EliaAlberti/jev-rules</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [EliaAlberti](https://github.com/EliaAlberti)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev picks which of your rules apply to each prompt, so Claude only sees the ones that matter.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/eliaalberti--jev-rules/ae4048f230729427.gif" width="100%" alt="EliaAlberti/jev-rules screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/eliaalberti--jev-rules/ae4048f230729427.gif" width="100%" alt="EliaAlberti/jev-rules animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/enderzcx/spire-jev">enderzcx/spire-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [enderzcx](https://github.com/enderzcx)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Slay the Spire 2 agent controller: planner models, Jev fast decisions, and verified multi-card turn execution

</details>

<details>
<summary><b><a href="https://github.com/EtienneLescot/jev-router">EtienneLescot/jev-router</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · HTML · MIT · [EtienneLescot](https://github.com/EtienneLescot)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model tier and reasoning depth.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/etiennelescot--jev-router/96217fad0b128b3e.png" width="100%" alt="EtienneLescot/jev-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Friedjof/jev-mobile">Friedjof/jev-mobile</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [Friedjof](https://github.com/Friedjof)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Fast structured Android control loops with TypeSafe Jev and Mobile MCP

</details>

<details>
<summary><b><a href="https://github.com/gzawadzki/jev-usecases">gzawadzki/jev-usecases</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [gzawadzki](https://github.com/gzawadzki)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage

</details>

<details>
<summary><b><a href="https://github.com/hangarbay/jev.mcp">hangarbay/jev.mcp</a></b> — Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Go · MIT · [hangarbay](https://github.com/hangarbay)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/HomenShum/jev-swap">HomenShum/jev-swap</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [HomenShum](https://github.com/HomenShum)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Claude Code skill: swap System 2 LLM pipeline components for System 1 TypeSafe Jev decisions via investigation, live three-arm eval, fallback, and an independent judge

</details>

<details>
<summary><b><a href="https://github.com/IAnMove/jev-game-agent">IAnMove/jev-game-agent</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · [IAnMove](https://github.com/IAnMove)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Experimental Jev game agent: RAM, emulator lookahead, checkpoint search and verified recordings. Bring your own ROM and BizHawk.

</details>

<details>
<summary><b><a href="https://github.com/its-panzer/jev-model-router">its-panzer/jev-model-router</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [its-panzer](https://github.com/its-panzer)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A policy router that picks the cheapest Claude model that can finish the job

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/its-panzer--jev-model-router/98819f5aaf8e6373.png" width="100%" alt="its-panzer/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Jabbslad/pi-jev-tools">Jabbslad/pi-jev-tools</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [Jabbslad](https://github.com/Jabbslad)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe ranking, classification, retrieval and structured-decision tools for Pi coding agents

</details>

<details>
<summary><b><a href="https://github.com/janegbert/ask-jev">janegbert/ask-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · [janegbert](https://github.com/janegbert)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Ask Jev about a file instead of reading it. A Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/jmanhype/jev-dspy-lab">jmanhype/jev-dspy-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [jmanhype](https://github.com/jmanhype)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-harness">kevin9327/jev-harness</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [kevin9327](https://github.com/kevin9327)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

JevHarness: TypeSafe Jev agent tool-call gate. execute / confirm / reject in code.

</details>

<details>
<summary><b><a href="https://github.com/madeye/pi-jev">madeye/pi-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [madeye](https://github.com/madeye)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev-assisted file retrieval and request caching for faster Pi workflows

</details>

<details>
<summary><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">MahmoudAdelbghany/jev-browser</a></b> — JavaScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · [MahmoudAdelbghany](https://github.com/MahmoudAdelbghany)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included.

</details>

<details>
<summary><b><a href="https://github.com/milanboers/jev-plays-pokemon">milanboers/jev-plays-pokemon</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · NOASSERTION · [milanboers](https://github.com/milanboers)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Playing Pokemon Red using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/minhgv/jev-mcp">minhgv/jev-mcp</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [minhgv](https://github.com/minhgv)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe Jev MCP decision layer for coding agents and CI

</details>

<details>
<summary><b><a href="https://github.com/morcoan/JevSeek">morcoan/JevSeek</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · [morcoan](https://github.com/morcoan)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools, persistent sessions, React desktop, and documented research.

</details>

<details>
<summary><b><a href="https://github.com/MSalvalaggio/jev-reflex">MSalvalaggio/jev-reflex</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [MSalvalaggio](https://github.com/MSalvalaggio)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision).

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-mcp">nekowasabi/jev-routing-mcp</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · [nekowasabi](https://github.com/nekowasabi)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/noetion/dsh-jev">noetion/dsh-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [noetion](https://github.com/noetion)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.

</details>

<details>
<summary><b><a href="https://github.com/ourines/hermes-jev">ourines/hermes-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [ourines](https://github.com/ourines)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev decision sidekick for Hermes Agent — TypeSafe and Cloudflare, explicit tools and official skill

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-mcp-router">Pinutss/jev-mcp-router</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [Pinutss](https://github.com/Pinutss)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Select relevant MCP tools under a context-token budget, without executing them.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-mcp-router/3947a2a5cc3750c8.png" width="100%" alt="Pinutss/jev-mcp-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-memory-selector">Pinutss/jev-memory-selector</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [Pinutss](https://github.com/Pinutss)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-memory-selector/6b6b7efc3440b641.png" width="100%" alt="Pinutss/jev-memory-selector screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-plugins">Pinutss/jev-plugins</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · MIT · [Pinutss](https://github.com/Pinutss)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Cursor and Hermes marketplace for the four published JEV Labs routers.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-plugins/b3fcd72ac9e61f49.jpg" width="100%" alt="Pinutss/jev-plugins screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/QuentinDanblon/pi-fast-jev-compaction">QuentinDanblon/pi-fast-jev-compaction</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · NOASSERTION · [QuentinDanblon](https://github.com/QuentinDanblon)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Verbatim context pruning for the pi coding agent, scored by TypeSafe Jev: stale tool calls and results are dropped or truncated, everything kept stays verbatim.

</details>

<details>
<summary><b><a href="https://github.com/raj8525/universal-jev">raj8525/universal-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [raj8525](https://github.com/raj8525)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-gates">rashedInt32/jev-gates</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · MIT · [rashedInt32](https://github.com/rashedInt32)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/3996d0153a09b158.gif" width="100%" alt="rashedInt32/jev-gates screenshot"></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/d9ddd128a148385e.mp4" controls muted loop playsinline width="100%" poster="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/3996d0153a09b158.gif"><source src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/d9ddd128a148385e.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/d9ddd128a148385e.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rubichandrap/hermes-jev-guard">rubichandrap/hermes-jev-guard</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [rubichandrap](https://github.com/rubichandrap)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check

</details>

<details>
<summary><b><a href="https://github.com/sypherin/jev-trace-classifier">sypherin/jev-trace-classifier</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [sypherin](https://github.com/sypherin)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next

</details>

<details>
<summary><b><a href="https://github.com/szocpaul/jev-compaction-prime">szocpaul/jev-compaction-prime</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · [szocpaul](https://github.com/szocpaul)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Verbatim, decision-based context compaction for Prime Agent — instead of summaries, stale tool calls are scored and dropped; everything kept stays byte-for-byte intact.

</details>

<details>
<summary><b><a href="https://github.com/taisan11/jev-agent">taisan11/jev-agent</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · [taisan11](https://github.com/taisan11)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/tgiridhar/claude-code-jev-smart-router">tgiridhar/claude-code-jev-smart-router</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [tgiridhar](https://github.com/tgiridhar)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task phase and the cost of an undetected error, gated by prompt-cache arithmetic. Proof of concept.

</details>

<details>
<summary><b><a href="https://github.com/themsquared/jev-benchmark">themsquared/jev-benchmark</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · Apache-2.0 · [themsquared](https://github.com/themsquared)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.

</details>

<details>
<summary><b><a href="https://github.com/thevibeworks/awesome-typesafe-jev">thevibeworks/awesome-typesafe-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · NOASSERTION · [thevibeworks](https://github.com/thevibeworks)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/thevibeworks/awesome-typesafe-jev/main/docs/media/lab-latency.png" width="100%" alt="thevibeworks/awesome-typesafe-jev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/thevibeworks/awesome-typesafe-jev/main/docs/media/sightmap__turbo.gif" width="100%" alt="thevibeworks/awesome-typesafe-jev animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/ussyverse/hermes-jev-router">ussyverse/hermes-jev-router</a></b> — Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [ussyverse](https://github.com/ussyverse)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending.

</details>

<details>
<summary><b><a href="https://github.com/xucian/fbyte-jev-vs-claude">xucian/fbyte-jev-vs-claude</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · HTML · [xucian](https://github.com/xucian)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev vs Claude — Structured Classification Benchmark. 5 tasks, 5 models, 20 cases each. Comparing Jev (via OpenRouter) against Claude Opus 4.6 and Sonnet 4.6, with and without adaptive thinking.

</details>

<details>
<summary><b><a href="https://github.com/yangzhou-chaofan/awesome-jev-prompt">yangzhou-chaofan/awesome-jev-prompt</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · JavaScript · CC0-1.0 · [yangzhou-chaofan](https://github.com/yangzhou-chaofan)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

latest top 100 showcases for jev (keep updating) from x / github / latest sources

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yangzhou-chaofan--awesome-jev-prompt/1c01ea8fc35d81c9.webp" width="100%" alt="yangzhou-chaofan/awesome-jev-prompt screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/zbloss/jev-plays-pokemon">zbloss/jev-plays-pokemon</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · Python · MIT · [zbloss](https://github.com/zbloss)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 5 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Like Claude Plays Pokemon, but with Jev

</details>

<details>
<summary><b><a href="https://github.com/zhangxaochen/dsh-jev">zhangxaochen/dsh-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `inferred` · TypeScript · MIT · [zhangxaochen](https://github.com/zhangxaochen)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev (System One decision model) plugin suite for DeepSeek Harness (dsh)

</details>

<details>
<summary><b><a href="https://github.com/DevMortimer/pi-warden">DevMortimer/pi-warden</a></b> — ⭐57 · TypeScript · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `unverified` · TypeScript · MIT · [DevMortimer](https://github.com/DevMortimer)

**ข้อมูล** · ดาว **57** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop

> Guardrails that steer an agent before it acts. Demonstrates the gate pattern, where the decision is cheap enough to run on every step.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devmortimer--pi-warden/b8dc20ac6694613a.png" width="100%" alt="DevMortimer/pi-warden screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/3clyp50/a0-typesafe-ai">3clyp50/a0-typesafe-ai</a></b> — ⭐4 · Python · unverified · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `unverified` · Python · MIT · [3clyp50](https://github.com/3clyp50)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/3clyp50--a0-typesafe-ai/9aa8ea4ef8241f14.png" width="100%" alt="3clyp50/a0-typesafe-ai screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/pi-quiet-ask">HyunjunJeon/pi-quiet-ask</a></b> — ⭐3 · TypeScript · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `unverified` · TypeScript · MIT · [HyunjunJeon](https://github.com/HyunjunJeon)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe Jev as the pi coding agent's quiet decision layer

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hyunjunjeon--pi-quiet-ask/7ee3a99430e853d8.png" width="100%" alt="HyunjunJeon/pi-quiet-ask screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/zoidsh/tenet">zoidsh/tenet</a></b> — ⭐3 · Go · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `เครื่องมือสำหรับเอเจนต์: MCP ฮุก เกต และเอเจนต์เขียนโค้ด` · ชุมชน · `unverified` · Go · MIT · [zoidsh](https://github.com/zoidsh)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

The review gate for code that agents write: rules in plain language, judged on every commit

</details>

<a id="routing-guardrails"></a>

## การจัดเส้นทาง การ์ดเรล และการอนุมัติ <sub>· 40</sub>

กรณีใช้งานแบบงานจริง — ส่งแต่ละคำขอไปยังโมเดลที่ถูกที่สุดซึ่งรับมือได้จริง และคุมผลลัพธ์ด้วยการตรวจสอบที่แน่นอน

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐41 · Rust · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · Rust · NOASSERTION · [Dicklesworthstone](https://github.com/Dicklesworthstone)

**ข้อมูล** · ดาว **41** · ฟอร์ก 3 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐23 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · Python · [brainstormity](https://github.com/brainstormity)

**ข้อมูล** · ดาว **23** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

<sub>พบการใช้งานในโค้ด: `typesafe/__init__.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · Python · MIT · [Foadsf](https://github.com/Foadsf)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · TypeScript · MIT · [qddegtya](https://github.com/qddegtya)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed decisions from a System One model. An uncertain answer is a different type from a confident one — and the compiler makes you handle it.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `observed` · Python · [aniruddh-krovvidi](https://github.com/aniruddh-krovvidi)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐15 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · [yusukebe](https://github.com/yusukebe)

**ข้อมูล** · ดาว **15** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐5 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · MIT · [mejiasd3v](https://github.com/mejiasd3v)

**ข้อมูล** · ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · [andrelandgraf](https://github.com/andrelandgraf)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐2 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · [keeltrace](https://github.com/keeltrace)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · [maker-KK](https://github.com/maker-KK)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · [Pinutss](https://github.com/Pinutss)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐1 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · [prismhq](https://github.com/prismhq)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · [Shashank-H](https://github.com/Shashank-H)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/aaronshaf/opencode-jev-model-router">aaronshaf/opencode-jev-model-router</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · MIT · [aaronshaf](https://github.com/aaronshaf)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev-based automatic per-turn model routing for OpenCode

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Jupyter · MIT · [bitnovus](https://github.com/bitnovus)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/carllippert/jev-router">carllippert/jev-router</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · [carllippert](https://github.com/carllippert)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Express with no routes. TypeSafe Jev picks which handler runs.

</details>

<details>
<summary><b><a href="https://github.com/cephalization/jev-triage">cephalization/jev-triage</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · [cephalization](https://github.com/cephalization)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Uses typeful jev, zero sync to pull and sync large repositories for issue triage

</details>

<details>
<summary><b><a href="https://github.com/danfry1/jev-triage">danfry1/jev-triage</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · [danfry1](https://github.com/danfry1)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

GitHub Action that labels, deduplicates and spam-checks issues with Jev, with calibrated confidence for every decision

</details>

<details>
<summary><b><a href="https://github.com/danielhirt/jev-lab">danielhirt/jev-lab</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · [danielhirt](https://github.com/danielhirt)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison

</details>

<details>
<summary><b><a href="https://github.com/denikuchero/jev-chess-lab">denikuchero/jev-chess-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · GPL-3.0 · [denikuchero](https://github.com/denikuchero)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev chess experiments: independent decisions vs tactical and Stockfish assistance, with full traces and video replays

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/denikuchero--jev-chess-lab/93f39c2d8831bde6.gif" width="100%" alt="denikuchero/jev-chess-lab screenshot"></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/denikuchero--jev-chess-lab/6733e8dbce00ead3.mp4" controls muted loop playsinline width="100%" poster="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/denikuchero--jev-chess-lab/93f39c2d8831bde6.gif"><source src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/denikuchero--jev-chess-lab/6733e8dbce00ead3.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/denikuchero--jev-chess-lab/6733e8dbce00ead3.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gnoviawan/omp-jev-tools">gnoviawan/omp-jev-tools</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · NOASSERTION · [gnoviawan](https://github.com/gnoviawan)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation verification

</details>

<details>
<summary><b><a href="https://github.com/hugo-alves/jev-router-playground">hugo-alves/jev-router-playground</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · MIT · [hugo-alves](https://github.com/hugo-alves)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Interactive playground for testing Jev model-routing decisions against OpenRouter models

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hugo-alves--jev-router-playground/93692a5f183f12e1.jpg" width="100%" alt="hugo-alves/jev-router-playground screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iefnaf/pi-jev">iefnaf/pi-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · [iefnaf](https://github.com/iefnaf)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Pi extension suite powered by Jev: selective context compaction and model routing

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-macos-loop">jcpsimmons/jev-macos-loop</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · AGPL-3.0 · [jcpsimmons](https://github.com/jcpsimmons)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Native macOS computer-use loop: OmniParser CoreML, Apple Vision OCR, accessibility labels, and Jev decisions through Vercel AI Gateway.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jcpsimmons--jev-macos-loop/b368b1d9b147950e.png" width="100%" alt="jcpsimmons/jev-macos-loop screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jerryfane/omp-jev-compaction">jerryfane/omp-jev-compaction</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · [jerryfane](https://github.com/jerryfane)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/juanegido/jev-pr-judge">juanegido/jev-pr-judge</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · MIT · [juanegido](https://github.com/juanegido)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed verdicts on pull requests with TypeSafe System One (Jev): one parallel call, policy in code, usable as a GitHub Action

</details>

<details>
<summary><b><a href="https://github.com/kenhuangus/jev-usecases">kenhuangus/jev-usecases</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · [kenhuangus](https://github.com/kenhuangus)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kenhuangus--jev-usecases/be919255190f6495.png" width="100%" alt="kenhuangus/jev-usecases screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-bot">kevin9327/jev-bot</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · [kevin9327](https://github.com/kevin9327)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-code">kevin9327/jev-code</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · MIT · [kevin9327](https://github.com/kevin9327)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

JevCode: TypeSafe Jev diff merge gate. merge / comment / block in code.

</details>

<details>
<summary><b><a href="https://github.com/maraichr/jev-triage">maraichr/jev-triage</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · MIT · [maraichr](https://github.com/maraichr)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Cross-border B2B case triage prototype using TypeSafe Jev via OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/MoonTory/pi-jev-harness">MoonTory/pi-jev-harness</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · [MoonTory](https://github.com/MoonTory)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards tool calls

</details>

<details>
<summary><b><a href="https://github.com/nitinnat/jev-gateway">nitinnat/jev-gateway</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · MIT · [nitinnat](https://github.com/nitinnat)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A small local HTTP service for TypeSafe AI's Jev through Vercel

</details>

<details>
<summary><b><a href="https://github.com/SadiqOnGithub/jev-lab">SadiqOnGithub/jev-lab</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · TypeScript · [SadiqOnGithub](https://github.com/SadiqOnGithub)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API

</details>

<details>
<summary><b><a href="https://github.com/stbenjam/jev-eight-ball">stbenjam/jev-eight-ball</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · [stbenjam](https://github.com/stbenjam)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A liquid magic eight ball powered by TypeSafe Jev decisions through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/TokenTrim/jev-routing-experiment">TokenTrim/jev-routing-experiment</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · Apache-2.0 · [TokenTrim](https://github.com/TokenTrim)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tokentrim--jev-routing-experiment/1c31bd606ebc1994.png" width="100%" alt="TokenTrim/jev-routing-experiment screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/tvdavies/jev-review-lab">tvdavies/jev-review-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · Python · [tvdavies](https://github.com/tvdavies)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Read-only Jev review scouting and shared-state fan-out experiments. Shadow hints, not approval decisions.

</details>

<details>
<summary><b><a href="https://github.com/wadadanet/faq-jev-router">wadadanet/faq-jev-router</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · MIT · [wadadanet](https://github.com/wadadanet)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Cascade FAQ routing with TypeSafe Jev — category → FAQ or not found (GitHub Pages demo)

</details>

<details>
<summary><b><a href="https://github.com/Xy2002/poker-jev-test-bench">Xy2002/poker-jev-test-bench</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `inferred` · JavaScript · MIT · [Xy2002](https://github.com/Xy2002)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev test bench — Texas Hold'em edition: live-fire testing of TypeSafe's Jev evaluation model through a React poker game (Vercel AI Gateway). MIT.

</details>

<details>
<summary><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">iammrduncan/typesafe-ai-benchmark</a></b> — ⭐30 · TypeScript · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `unverified` · TypeScript · MIT · [iammrduncan](https://github.com/iammrduncan)

**ข้อมูล** · ดาว **30** · ฟอร์ก 5 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.

> A gateway that mimics the System One interface, which is what makes side-by-side benchmarking possible without rewriting the caller.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/c90c38d76d87a2fe.mp4" controls muted loop playsinline width="100%"><source src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/c90c38d76d87a2fe.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/c90c38d76d87a2fe.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/raihankhan-rk/diffjury">raihankhan-rk/diffjury</a></b> — ⭐3 · TypeScript · unverified · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การจัดเส้นทาง การ์ดเรล และการอนุมัติ` · ชุมชน · `unverified` · TypeScript · [raihankhan-rk](https://github.com/raihankhan-rk)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

DiffJury — TypeSafe Jev PR risk router + code review coach

</details>

<a id="evaluation"></a>

## การประเมิน การคาลิเบรต และเบนช์มาร์ก <sub>· 29</sub>

ใครจะรู้ได้ว่าการตัดสินใจเหล่านั้นดีพอ การคาลิเบรตเป็นคำถามเปิดในระบบนิเวศนี้ และนี่คือโปรเจกต์ที่วัดมัน

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `observed` · Go · MIT · [Gaurav-Gosain](https://github.com/Gaurav-Gosain)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `observed` · Python · [akash-kamat](https://github.com/akash-kamat)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `observed` · Python · Apache-2.0 · [hev](https://github.com/hev)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/rorshopping/jev-on-a-laptop">rorshopping/jev-on-a-laptop</a></b> — ⭐14 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · NOASSERTION · [rorshopping](https://github.com/rorshopping)

**ข้อมูล** · ดาว **14** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Unofficial study: Jev-style parallel typed decisions on stock 1.5B-8B models on an Apple Silicon laptop. Benchmarks, research notes, and a Hugging Face Space demo.

</details>

<details>
<summary><b><a href="https://github.com/JoshuaSP/open-jev">JoshuaSP/open-jev</a></b> — ⭐13 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · [JoshuaSP](https://github.com/JoshuaSP)

**ข้อมูล** · ดาว **13** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed JSON inference with DiffusionGemma, with Every and Jev benchmark results

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/joshuasp--open-jev/1d4a9f6368358e43.png" width="100%" alt="JoshuaSP/open-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐6 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · Apache-2.0 · [AbdelStark](https://github.com/AbdelStark)

**ข้อมูล** · ดาว **6** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐4 · TypeScript · inferred · 2 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · TypeScript · MIT · [y0usaf](https://github.com/y0usaf)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐2 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · NOASSERTION · [Heman10x-NGU](https://github.com/Heman10x-NGU)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · [wondertwins](https://github.com/wondertwins)

**ข้อมูล** · ดาว **2** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · Apache-2.0 · [ikermoel](https://github.com/ikermoel)

**ข้อมูล** · ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Open alternative to Jev: typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with benchmarks

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · [4esv](https://github.com/4esv)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-eval/main/results/coverage.png" width="100%" alt="4esv/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/aieo-product/jev-gamebenchmark">aieo-product/jev-gamebenchmark</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · [aieo-product](https://github.com/aieo-product)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Sandbox & benchmark: optimize how you ask Jev (TypeSafe System One) to play falling-block puzzle games, head-to-head against LLMs

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · TypeScript · MIT · [Danu28](https://github.com/Danu28)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · TeX · NOASSERTION · [dnakhoa](https://github.com/dnakhoa)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · [eggmasonvalue](https://github.com/eggmasonvalue)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · MIT · [jujumilk3](https://github.com/jujumilk3)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · JavaScript · MIT · [KantaHayashiAI](https://github.com/KantaHayashiAI)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/misaalya/snbt-jev-bench">misaalya/snbt-jev-bench</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · [misaalya](https://github.com/misaalya)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev on Indonesia's SNBT 2025 university entrance test: 159 questions, seven subtests, audited answer keys.

</details>

<details>
<summary><b><a href="https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and">musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · HTML · MIT · [musman550](https://github.com/musman550)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@automatewithmusfiraai"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@automatewithmusfiraai">รับชมบน youtube.com</a> · การเล่นจะเปิดบนเว็บไซต์ต้นทาง GitHub ไม่สามารถฝังแบบอินไลน์ได้</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/onlyoneaman/jev-eval">onlyoneaman/jev-eval</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · TypeScript · MIT · [onlyoneaman](https://github.com/onlyoneaman)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/onlyoneaman--jev-eval/e5d471e96e134f81.png" width="100%" alt="onlyoneaman/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/robipop22/Jev-is-odd">robipop22/Jev-is-odd</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · JavaScript · MIT · [robipop22](https://github.com/robipop22)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Ask Jev by TypeSafe AI whether a number is odd. TypeScript, real token usage, and latency benchmarks.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/robipop22--jev-is-odd/5c4ddde817bd6cdc.png" width="100%" alt="robipop22/Jev-is-odd screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rongxinzy/LightJev">rongxinzy/LightJev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · Apache-2.0 · [rongxinzy](https://github.com/rongxinzy)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Train lightweight language backbones for typed decisions and candidate probabilities. CE/Brier training, evaluation, and an offline end-to-end demo.

</details>

<details>
<summary><b><a href="https://github.com/shunta-furukawa/jev-tick-lab">shunta-furukawa/jev-tick-lab</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · [shunta-furukawa](https://github.com/shunta-furukawa)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis.

</details>

<details>
<summary><b><a href="https://github.com/teyhouse/jev-secret-detection">teyhouse/jev-secret-detection</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · Python · [teyhouse](https://github.com/teyhouse)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" width="100%" alt="teyhouse/jev-secret-detection screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/uspraveen/Jev-Reranker">uspraveen/Jev-Reranker</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `inferred` · MIT · [uspraveen](https://github.com/uspraveen)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A System-1 model based memory retrieval reranked using caliberated decision space instead of embeddings

</details>

<details>
<summary><b><a href="https://github.com/Mapika/decider">Mapika/decider</a></b> — ⭐12 · Python · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `unverified` · Python · [Mapika](https://github.com/Mapika)

**ข้อมูล** · ดาว **12** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Mapika/decider/main/media/montage.gif" width="100%" alt="Mapika/decider animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/genai-craft/openvons">genai-craft/openvons</a></b> — ⭐7 · Python · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `unverified` · Python · NOASSERTION · [genai-craft](https://github.com/genai-craft)

**ข้อมูล** · ดาว **7** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド

</details>

<details>
<summary><b><a href="https://github.com/aabolfazl/typesafe-local">aabolfazl/typesafe-local</a></b> — ⭐4 · Python · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `unverified` · Python · MIT · [aabolfazl](https://github.com/aabolfazl)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/aabolfazl--typesafe-local/ada59cf382af5143.png" width="100%" alt="aabolfazl/typesafe-local screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mithalouni/system-one-open">mithalouni/system-one-open</a></b> — ⭐4 · Python · unverified · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `การประเมิน การคาลิเบรต และเบนช์มาร์ก` · ชุมชน · `unverified` · Python · NOASSERTION · [mithalouni](https://github.com/mithalouni)

**ข้อมูล** · ดาว **4** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal)

</details>

<a id="research-models"></a>

## งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม <sub>· 12</sub>

เวตเปิด งานจำลองขนาดเล็ก และงานสถาปัตยกรรม หลายโปรเจกต์มีอยู่เพราะพฤติกรรมการคาลิเบรตจำลองขึ้นใหม่จากเอกสารสาธารณะเพียงอย่างเดียวไม่ได้

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐47 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `observed` · Python · MIT · [kshetrajna12](https://github.com/kshetrajna12)

**ข้อมูล** · ดาว **47** · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐224 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · MIT · [TianyuCodings](https://github.com/TianyuCodings)

**ข้อมูล** · ดาว **224** · ฟอร์ก 19 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/9ee4bfd928a28800.mp4" controls muted loop playsinline width="100%" poster="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png"><source src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/9ee4bfd928a28800.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/9ee4bfd928a28800.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐12 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · MIT · [r-ms](https://github.com/r-ms)

**ข้อมูล** · ดาว **12** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `observed`

**ข้อมูล** · ดาวน์โหลด 25 · ถูกใจ 1 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `observed`

**ข้อมูล** · ดาวน์โหลด 0 · ถูกใจ 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐114 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · [ekzhang](https://github.com/ekzhang)

**ข้อมูล** · ดาว **114** · ฟอร์ก 10 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐19 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · MIT · [bnsd55](https://github.com/bnsd55)

**ข้อมูล** · ดาว **19** · ฟอร์ก 3 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/siliconkernel/vllm-jev-decison">siliconkernel/vllm-jev-decison</a></b> — ⭐6 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · MIT · [siliconkernel](https://github.com/siliconkernel)

**ข้อมูล** · ดาว **6** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Classification-only typed decisions for vLLM: finite-schema candidate scoring, probabilities, and abstention. No generative fallback.

</details>

<details>
<summary><b><a href="https://github.com/chahero/tetris-jev">chahero/tetris-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · [chahero](https://github.com/chahero)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Watch TypeSafe Jev play Tetris. Live API vs offline heuristic, with recorded demos and reproducible runs.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/chahero/tetris-jev/main/media/jev-preview.gif" width="100%" alt="chahero/tetris-jev screenshot"></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/chahero/tetris-jev/main/media/jev.mp4" controls muted loop playsinline width="100%"><source src="https://raw.githubusercontent.com/chahero/tetris-jev/main/media/jev.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/chahero/tetris-jev/main/media/jev.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">legacybridge-tech/pi-typesafe-jev</a></b> — TypeScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · TypeScript · NOASSERTION · [legacybridge-tech](https://github.com/legacybridge-tech)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `inferred` · Python · [shellneko](https://github.com/shellneko)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐4 · Python · unverified · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `งานจำลองแบบเปิด เวต และงานวิจัยสถาปัตยกรรม` · ชุมชน · `unverified` · Python · NOASSERTION · [zhihz](https://github.com/zhihz)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<a id="apps-demos"></a>

## แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ <sub>· 38</sub>

เกม หุ่นยนต์ เบราว์เซอร์ และแดชบอร์ด เดโมคือสิ่งที่ทำให้ข้ออ้างเรื่องความหน่วงและต้นทุนอ่านออก

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐7 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · Python · Apache-2.0 · [zadescoxp](https://github.com/zadescoxp)

**ข้อมูล** · ดาว **7** · ฟอร์ก 1 · issue ที่เปิดอยู่ 3 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · TypeScript · [daftAI2026](https://github.com/daftAI2026)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · Rust · MIT · [markjaquith](https://github.com/markjaquith)

**ข้อมูล** · ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · TypeScript · [adiun](https://github.com/adiun)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · Dart · [Bud-ro](https://github.com/Bud-ro)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/sandra-arato/icon-matcher">sandra-arato/icon-matcher</a></b> — TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · TypeScript · MIT · [sandra-arato](https://github.com/sandra-arato)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Match a UI section title to a Hugeicons icon using TypeSafe.ai's Choice primitive — no lexical/keyword search.

</details>

<details>
<summary><b><a href="https://github.com/sandra-arato/icon-matcher-ui">sandra-arato/icon-matcher-ui</a></b> — TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · TypeScript · MIT · [sandra-arato](https://github.com/sandra-arato)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Browser-only UI for icon-matcher — paste a TypeSafe.ai key, match a UI title to an icon live, no backend.

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · Python · MIT · [tirukovelamanoj](https://github.com/tirukovelamanoj)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/ea0cac5593b1ef6d.mp4" controls muted loop playsinline width="100%" poster="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg"><source src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/ea0cac5593b1ef6d.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/ea0cac5593b1ef6d.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `observed` · TypeScript · [wustep](https://github.com/wustep)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐87 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · MIT · [hr98w](https://github.com/hr98w)

**ข้อมูล** · ดาว **87** · ฟอร์ก 9 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐58 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · MIT · [jkudish](https://github.com/jkudish)

**ข้อมูล** · ดาว **58** · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/23cf8f7acfef335f.mp4" controls muted loop playsinline width="100%" poster="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif"><source src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/23cf8f7acfef335f.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/23cf8f7acfef335f.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐18 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · MIT · [moritzkremb](https://github.com/moritzkremb)

**ข้อมูล** · ดาว **18** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/mizchi/jev-playground">mizchi/jev-playground</a></b> — ⭐13 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · [mizchi](https://github.com/mizchi)

**ข้อมูล** · ดาว **13** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/mario-jev">shantanugoel/mario-jev</a></b> — ⭐10 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · [shantanugoel](https://github.com/shantanugoel)

**ข้อมูล** · ดาว **10** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · [emrickgarrett](https://github.com/emrickgarrett)

**ข้อมูล** · ดาว **5** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐4 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · MIT · [komorra](https://github.com/komorra)

**ข้อมูล** · ดาว **4** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/arielweinberger/jev-autopilot">arielweinberger/jev-autopilot</a></b> — ⭐3 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · [arielweinberger](https://github.com/arielweinberger)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs $0.01.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/arielweinberger/jev-autopilot/main/docs/demo.png" width="100%" alt="arielweinberger/jev-autopilot screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐3 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · [vinilana](https://github.com/vinilana)

**ข้อมูล** · ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/Nainish-Rai/jev-frontend-qa">Nainish-Rai/jev-frontend-qa</a></b> — ⭐2 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · [Nainish-Rai](https://github.com/Nainish-Rai)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 5 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Evidence-driven frontend QA built on Jev Ultrafast and Browser Harness, with a synthetic todo demo.

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Go · MIT · [paulsmith](https://github.com/paulsmith)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/reachjalil/jev-tree">reachjalil/jev-tree</a></b> — ⭐2 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · MIT · [reachjalil](https://github.com/reachjalil)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap.

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · MIT · [vmendes90](https://github.com/vmendes90)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · [Little-Planet-Labs](https://github.com/Little-Planet-Labs)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/phureewat29/got-jev">phureewat29/got-jev</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · [phureewat29](https://github.com/phureewat29)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev (TypeSafe AI) PoC through Game of Thrones

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · [PistachioAIHQ](https://github.com/PistachioAIHQ)

**ข้อมูล** · ดาว **1** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/bahramzada/jev-taxi-dispatch">bahramzada/jev-taxi-dispatch</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · MIT · [bahramzada](https://github.com/bahramzada)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Real-vaxt taksi dispetçerlik simulyasiyası — TypeSafe JEV (System One) modeli ilə

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/bahramzada--jev-taxi-dispatch/e616f4168b15d3f2.png" width="100%" alt="bahramzada/jev-taxi-dispatch screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/bottlebrushes/jev-orb">bottlebrushes/jev-orb</a></b> — Makefile · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Makefile · [bottlebrushes](https://github.com/bottlebrushes)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Siri-style push-to-talk voice orb for autonomous browser control with Jev and Metal Whisper

</details>

<details>
<summary><b><a href="https://github.com/BrendanH18/jev-lab">BrendanH18/jev-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Python · MIT · [BrendanH18](https://github.com/BrendanH18)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brendanh18--jev-lab/b16b9535e3744cd3.png" width="100%" alt="BrendanH18/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hxutixnnn/ui-jev">hxutixnnn/ui-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · Apache-2.0 · [hxutixnnn](https://github.com/hxutixnnn)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/jflam/jev1">jflam/jev1</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · [jflam](https://github.com/jflam)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev (TypeSafe System One) proof of concept: smart-home assistant demo

</details>

<details>
<summary><b><a href="https://github.com/legostin/jev-browser">legostin/jev-browser</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · [legostin](https://github.com/legostin)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/pistachiopranay/jev-synergy-screening">pistachiopranay/jev-synergy-screening</a></b> — inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · [pistachiopranay](https://github.com/pistachiopranay)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/rchovatiya88/cyber-breach-jev">rchovatiya88/cyber-breach-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · [rchovatiya88](https://github.com/rchovatiya88)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model

</details>

<details>
<summary><b><a href="https://github.com/sightmap/jev-turbo">sightmap/jev-turbo</a></b> — Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · Go · MIT · [sightmap](https://github.com/sightmap)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev-powered semantic browser use

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/sightmap--jev-turbo/80ba196d00024a03.gif" width="100%" alt="sightmap/jev-turbo screenshot"></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/sightmap--jev-turbo/43d98ba1580eee69.mp4" controls muted loop playsinline width="100%" poster="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/sightmap--jev-turbo/80ba196d00024a03.gif"><source src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/sightmap--jev-turbo/43d98ba1580eee69.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/sightmap--jev-turbo/43d98ba1580eee69.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Spykoninho/trading-bot-jev">Spykoninho/trading-bot-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · [Spykoninho](https://github.com/Spykoninho)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Crypto trading bot on Binance testnet using TypeSafe (Jev) to judge news

</details>

<details>
<summary><b><a href="https://github.com/Tatuck/jev-boe-demo">Tatuck/jev-boe-demo</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · TypeScript · [Tatuck](https://github.com/Tatuck)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Daily demo applying TypeSafe's Jev model to Spain's official gazette (BOE).

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Tatuck/jev-boe-demo/main/docs/demo-pipeline.gif" width="100%" alt="Tatuck/jev-boe-demo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Tatuck/jev-boe-demo/main/docs/demo-web.gif" width="100%" alt="Tatuck/jev-boe-demo animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/YYK2007/jev-flappy">YYK2007/jev-flappy</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `inferred` · JavaScript · [YYK2007](https://github.com/YYK2007)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev makes every flap-or-coast decision in a live game, exposing probabilities, latency, tokens, and cost.

</details>

<details>
<summary><b><a href="https://github.com/sorrycc/typesafe-snake">sorrycc/typesafe-snake</a></b> — ⭐17 · TypeScript · unverified · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `แอปพลิเคชัน เกม หุ่นยนต์ และเดโมแบบโต้ตอบ` · ชุมชน · `unverified` · TypeScript · [sorrycc](https://github.com/sorrycc)

**ข้อมูล** · ดาว **17** · ฟอร์ก 2 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code

</details>

<a id="media-discussions"></a>

## บทความ การสนทนา และรายการที่เกี่ยวข้อง <sub>· 97</sub>

เธรดเปิดตัว บทความอิสระ และรายการคัดสรรอื่น ๆ ในสายนี้ รีโพซิทอรีนี้ไม่ใช่รายการเดียว และการพูดเช่นนั้นมีประโยชน์กว่าการแกล้งทำเป็นอย่างอื่น

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐4259 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · MIT · [browser-use](https://github.com/browser-use)

**ข้อมูล** · ดาว **4259** · ฟอร์ก 254 · issue ที่เปิดอยู่ 27 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

i. am. speed.

<sub>พบการใช้งานในโค้ด: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcc8b24fd0db56bd.mp4" controls muted loop playsinline width="100%" poster="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif"><source src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcc8b24fd0db56bd.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcc8b24fd0db56bd.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1877 · observed · 2 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 1877 · ความคิดเห็น 491 · push ล่าสุด 2026-09-15 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐465 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · MIT · [Anil-matcha](https://github.com/Anil-matcha)

**ข้อมูล** · ดาว **465** · ฟอร์ก 91 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2023-05-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>พบการใช้งานในโค้ด: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/anil-matcha--awesome-jev-by-typesafe/54dbd5521bc42664.jpg" width="100%" alt="Anil-matcha/awesome-jev-by-typesafe screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐167 · CSS · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · CSS · MIT · [AbdelStark](https://github.com/AbdelStark)

**ข้อมูล** · ดาว **167** · ฟอร์ก 21 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>พบการใช้งานในโค้ด: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐116 · TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · TypeScript · [dabit3](https://github.com/dabit3)

**ข้อมูล** · ดาว **116** · ฟอร์ก 11 · issue ที่เปิดอยู่ 16 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

<sub>พบการใช้งานในโค้ด: `nl-palette/server/jev.ts`, `jev-dispatch/vite.config.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐95 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · [yibie](https://github.com/yibie)

**ข้อมูล** · ดาว **95** · ฟอร์ก 7 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐48 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · CC0-1.0 · [cobanov](https://github.com/cobanov)

**ข้อมูล** · ดาว **48** · ฟอร์ก 2 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐47 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · CC0-1.0 · [AnotiaWang](https://github.com/AnotiaWang)

**ข้อมูล** · ดาว **47** · ฟอร์ก 11 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>พบการใช้งานในโค้ด: `README.md`, `README_zh.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐39 · observed · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 39 · ความคิดเห็น 9 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐26 · HTML · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · HTML · CC0-1.0 · [hellogumbo](https://github.com/hellogumbo)

**ข้อมูล** · ดาว **26** · ฟอร์ก 1 · issue ที่เปิดอยู่ 4 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A community directory of projects built on Jev, TypeSafe AI's System One model.

<sub>พบการใช้งานในโค้ด: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 2 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 5 · ความคิดเห็น 0 · push ล่าสุด 2026-09-15 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 4 · ความคิดเห็น 0 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 4 · ความคิดเห็น 0 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 3 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐3 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · NOASSERTION · [OmniJev](https://github.com/OmniJev)

**ข้อมูล** · ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Papers, open reproductions and independent evaluations behind System One models and Jev.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/OmniJev/awesome-jev/main/assets/cover.png" width="100%" alt="OmniJev/awesome-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49751902">Probably – a programming language for LLM workflows, powered by Jev</a></b> — ⭐3 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 3 · ความคิดเห็น 1 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 3 · ความคิดเห็น 0 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=48437732">Using Jai&#x27;s Unique and Powerful Compiler for Typesafe Units</a></b> — ⭐3 · observed · 102 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 3 · ความคิดเห็น 0 · push ล่าสุด 2026-06-07 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49752765">Ask HN: Is Jev the New Claw?</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Is it my skill&#x2F;smartness issue that I still struggle to see what Jev exactly is and what differentiates it?

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · CC0-1.0 · [hellogumbo](https://github.com/hellogumbo)

**ข้อมูล** · ดาว **2** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49744527">Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 2 · ความคิดเห็น 1 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Full disclosure, it was coded with AI, I don&#x27;t claim otherwise. But I wanted to test out tool calls and iterative problem solving using Jev and needed a simple library&#x2F;framework&#x2F;harness to do that.
SOKIT (System One Knowledge, Instructions and Tools) is the result

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=48435180">Show HN: Vithos – typesafe full-stack template for Cloudflare Workers</a></b> — ⭐2 · observed · 102 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 2 · ความคิดเห็น 1 · push ล่าสุด 2026-06-07 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49729945">The first (public) System One Model; Jev gives AI the properties of code</a></b> — ⭐2 · observed · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49745212">Typesafe&#x27;s Jev is the fish at the poker table</a></b> — ⭐2 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 2 · ความคิดเห็น 1 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49733647">Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step</a></b> — ⭐2 · observed · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49734345">Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD</a></b> — ⭐2 · observed · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed`

**ข้อมูล** · คะแนน 2 · ความคิดเห็น 0 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐1 · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · NOASSERTION · [aliaihub](https://github.com/aliaihub)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://github.com/justinhuangai/awesome-jev">justinhuangai/awesome-jev</a></b> — ⭐1 · Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · CC0-1.0 · [justinhuangai](https://github.com/justinhuangai)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A curated list of projects, tools, and resources built on Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/rhc98/awesome-jev">rhc98/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · TypeScript · NOASSERTION · [rhc98](https://github.com/rhc98)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhc98/awesome-jev/main/docs/diagrams/pipeline.png" width="100%" alt="rhc98/awesome-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/alpibrusl/lex-judge">alpibrusl/lex-judge</a></b> — Lex · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Lex · [alpibrusl](https://github.com/alpibrusl)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed judgments from a System One model, as a [net]-only Lex effect

</details>

<details>
<summary><b><a href="https://github.com/deepanwadhwa/OpenDecision">deepanwadhwa/OpenDecision</a></b> — Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · Apache-2.0 · [deepanwadhwa](https://github.com/deepanwadhwa)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Open Type Safe System one model system

</details>

<details>
<summary><b><a href="https://github.com/hide-G/magi-system-on-jev">hide-G/magi-system-on-jev</a></b> — JavaScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · [hide-G](https://github.com/hide-G)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/hide-G/magi-system-on-jev/master/public/ogp.png" width="100%" alt="hide-G/magi-system-on-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/JohnDotOwl/awesome-jev">JohnDotOwl/awesome-jev</a></b> — JavaScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · CC0-1.0 · [JohnDotOwl](https://github.com/JohnDotOwl)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A curated list of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/piyush97/focus-tube">piyush97/focus-tube</a></b> — JavaScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · MIT · [piyush97](https://github.com/piyush97)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model

</details>

<details>
<summary><b><a href="https://github.com/soderlind/ai-provider-for-jev">soderlind/ai-provider-for-jev</a></b> — PHP · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · PHP · [soderlind](https://github.com/soderlind)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).

</details>

<details>
<summary><b><a href="https://github.com/TheGali/terrarium">TheGali/terrarium</a></b> — JavaScript · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · JavaScript · MIT · [TheGali](https://github.com/TheGali)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.

</details>

<details>
<summary><b><a href="https://github.com/youngsemicolon/jev-lego">youngsemicolon/jev-lego</a></b> — Python · observed · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `observed` · Python · [youngsemicolon](https://github.com/youngsemicolon)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A System One model builds Lego in 3D — code enumerates legal placements, Jev picks among them

</details>

<details>
<summary><b><a href="https://github.com/jarrodwatts/jev-trader">jarrodwatts/jev-trader</a></b> — ⭐735 · TypeScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [jarrodwatts](https://github.com/jarrodwatts)

**ข้อมูล** · ดาว **735** · ฟอร์ก 145 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

</details>

<details>
<summary><b><a href="https://github.com/droidrun/mobile-jev">droidrun/mobile-jev</a></b> — ⭐79 · JavaScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · MIT · [droidrun](https://github.com/droidrun)

**ข้อมูล** · ดาว **79** · ฟอร์ก 15 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/daseinlabs/open-jev">daseinlabs/open-jev</a></b> — ⭐25 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · [daseinlabs](https://github.com/daseinlabs)

**ข้อมูล** · ดาว **25** · ฟอร์ก 4 · issue ที่เปิดอยู่ 4 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov" controls muted loop playsinline width="100%"><source src="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov" type="video/mp4"><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">IAmUnbounded/save-token-jev-clean</a></b> — ⭐25 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [IAmUnbounded](https://github.com/IAmUnbounded)

**ข้อมูล** · ดาว **25** · ฟอร์ก 6 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/superagents-lab/jev-search">superagents-lab/jev-search</a></b> — ⭐23 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [superagents-lab](https://github.com/superagents-lab)

**ข้อมูล** · ดาว **23** · ฟอร์ก 4 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/superagents-lab--jev-search/5a545ddfd6a52aed.png" width="100%" alt="superagents-lab/jev-search screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mrnugget/jev-shell-history">mrnugget/jev-shell-history</a></b> — ⭐19 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · [mrnugget](https://github.com/mrnugget)

**ข้อมูล** · ดาว **19** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Fish-style zsh history autosuggestions ranked by Jev (TypeSafe)

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/Dennan1221/repo-jev1iewp">Dennan1221/repo-jev1iewp</a></b> — ⭐9 · inferred · 585 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · [Dennan1221](https://github.com/Dennan1221)

**ข้อมูล** · ดาว **9** · ฟอร์ก 0 · issue ที่เปิดอยู่ 20 · สร้างเมื่อ 2025-02-10 · push ล่าสุด 2025-02-10 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Авто-генерация repo-jev1iewp

</details>

<details>
<summary><b><a href="https://github.com/jon-devlapaz/jev-me">jon-devlapaz/jev-me</a></b> — ⭐9 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · [jon-devlapaz](https://github.com/jon-devlapaz)

**ข้อมูล** · ดาว **9** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

jev-me is grill-me with jev

</details>

<details>
<summary><b><a href="https://github.com/Kevthetech143/super-jev">Kevthetech143/super-jev</a></b> — ⭐5 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [Kevthetech143](https://github.com/Kevthetech143)

**ข้อมูล** · ดาว **5** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A small, extensible decision-to-action harness for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/mateonunez/jod">mateonunez/jod</a></b> — ⭐3 · TypeScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [mateonunez](https://github.com/mateonunez)

**ข้อมูล** · ดาว **3** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers.

</details>

<details>
<summary><b><a href="https://github.com/haseeb-heaven/jev-system-one">haseeb-heaven/jev-system-one</a></b> — ⭐2 · Python · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · [haseeb-heaven](https://github.com/haseeb-heaven)

**ข้อมูล** · ดาว **2** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/haseeb-heaven--jev-system-one/e41c848323b1077a.png" width="100%" alt="haseeb-heaven/jev-system-one screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/justinhe16/trade-jev">justinhe16/trade-jev</a></b> — ⭐2 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · [justinhe16](https://github.com/justinhe16)

**ข้อมูล** · ดาว **2** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Backtest Jev (TypeSafe) as a BUY/SELL/HOLD trader on NQ L10 order-book data

</details>

<details>
<summary><b><a href="https://github.com/anxkhn/JevPlaysPokemon">anxkhn/JevPlaysPokemon</a></b> — ⭐1 · HTML · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · HTML · GPL-3.0 · [anxkhn](https://github.com/anxkhn)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev plays Generation 3 Pokémon via Showdown and a real FireRed ROM.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/anxkhn--jevplayspokemon/fc9ead060d7fa36a.png" width="100%" alt="anxkhn/JevPlaysPokemon screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/jev-review-action">fatwang2/jev-review-action</a></b> — ⭐1 · JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · MIT · [fatwang2](https://github.com/fatwang2)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.

</details>

<details>
<summary><b><a href="https://github.com/hqman/JevScout">hqman/JevScout</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · [hqman](https://github.com/hqman)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4" controls muted loop playsinline width="100%"><source src="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/joelhooks/pi-fast-jev-compaction">joelhooks/pi-fast-jev-compaction</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [joelhooks](https://github.com/joelhooks)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Pi extension: verbatim context compaction with TypeSafe Jev decisions

</details>

<details>
<summary><b><a href="https://github.com/lbotinelly/jev-little-airways">lbotinelly/jev-little-airways</a></b> — ⭐1 · HTML · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · HTML · MIT · [lbotinelly](https://github.com/lbotinelly)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A show-and-tell capability study for Jev, TypeSafe's System One decision model.

</details>

<details>
<summary><b><a href="https://github.com/sontakey/awesome-jev">sontakey/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · NOASSERTION · [sontakey](https://github.com/sontakey)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Unofficial list of insanely useful TypeSafe AI Jev / System One projects

</details>

<details>
<summary><b><a href="https://github.com/TanayPadar/gpt-vs-jev">TanayPadar/gpt-vs-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [TanayPadar](https://github.com/TanayPadar)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Compare GPT generated language with JEV structured Noul decisions on the same input.

</details>

<details>
<summary><b><a href="https://github.com/tylerjharden/harden-jev-decides">tylerjharden/harden-jev-decides</a></b> — ⭐1 · TypeScript · inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · [tylerjharden](https://github.com/tylerjharden)

**ข้อมูล** · ดาว **1** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.

</details>

<details>
<summary><b><a href="https://github.com/Amal-David/awesome-jev">Amal-David/awesome-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · NOASSERTION · [Amal-David](https://github.com/Amal-David)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/andesco/ladder-cloudflare-jev">andesco/ladder-cloudflare-jev</a></b> — Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Go · [andesco](https://github.com/andesco)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Ladderflare: Ladder as a serverless application for Cloudflare Workers

</details>

<details>
<summary><b><a href="https://github.com/Charlyhno-eng/jev-document-classification">Charlyhno-eng/jev-document-classification</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [Charlyhno-eng](https://github.com/Charlyhno-eng)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/charlyhno-eng--jev-document-classification/113bcf66f1648122.png" width="100%" alt="Charlyhno-eng/jev-document-classification screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ClemensSchartmueller/jev-guard">ClemensSchartmueller/jev-guard</a></b> — Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Go · MIT · [ClemensSchartmueller](https://github.com/ClemensSchartmueller)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/cmartinez9/jev-judge-bench">cmartinez9/jev-judge-bench</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · [cmartinez9](https://github.com/cmartinez9)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Binary LLM-judge bench — compare Jev (TypeSafe System One) against a frontier LLM judge on speed, cost, and agreement with human labels.

</details>

<details>
<summary><b><a href="https://github.com/erhanmeydan/jev2048">erhanmeydan/jev2048</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · [erhanmeydan](https://github.com/erhanmeydan)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe'in Jev karar modeli gerçek bir online 2048 sitesinde oynuyor — hamle başına tek API çağrısı, tek anahtar.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/erhanmeydan--jev2048/a2709def4f48e691.gif" width="100%" alt="erhanmeydan/jev2048 screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/erhanmeydan--jev2048/a2709def4f48e691.gif" width="100%" alt="erhanmeydan/jev2048 animation"><br><sub>บันทึกแบบเคลื่อนไหว</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/felixfisher/pi-jev-compaction">felixfisher/pi-jev-compaction</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [felixfisher](https://github.com/felixfisher)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Experimental Pi extension using TypeSafe Jev for auditable tool-history compaction

</details>

<details>
<summary><b><a href="https://github.com/havlan/jev-go">havlan/jev-go</a></b> — Go · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Go · MIT · [havlan](https://github.com/havlan)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/heaven-hm/jev-system-one">heaven-hm/jev-system-one</a></b> — inferred · 1 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · [heaven-hm](https://github.com/heaven-hm)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

</details>

<details>
<summary><b><a href="https://github.com/ilkerulusoy/pi-jev-compact">ilkerulusoy/pi-jev-compact</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · [ilkerulusoy](https://github.com/ilkerulusoy)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/jangya/jev-in-action">jangya/jev-in-action</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · MIT · [jangya](https://github.com/jangya)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jangya--jev-in-action/176ee4b2fcaaed8d.png" width="100%" alt="jangya/jev-in-action screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Jbenkang/localJev">Jbenkang/localJev</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · [Jbenkang](https://github.com/Jbenkang)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

making-jev-local

</details>

<details>
<summary><b><a href="https://github.com/jdhornsby/typesafe-jev">jdhornsby/typesafe-jev</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · [jdhornsby](https://github.com/jdhornsby)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/JulioPeixoto/jev-decision-bench">JulioPeixoto/jev-decision-bench</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · [JulioPeixoto](https://github.com/JulioPeixoto)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/kagurazakayashi/dsh-jev">kagurazakayashi/dsh-jev</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · [kagurazakayashi](https://github.com/kagurazakayashi)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

我正在探索 DeepSeek Harness 中 DeepSeek 与 Jev 的合作方式。

</details>

<details>
<summary><b><a href="https://github.com/karimatayuta/tiny-jev">karimatayuta/tiny-jev</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · HTML · [karimatayuta](https://github.com/karimatayuta)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 6 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/KaushikKC/JevScope">KaushikKC/JevScope</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [KaushikKC](https://github.com/KaushikKC)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/kentaro/jev-shogi">kentaro/jev-shogi</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · [kentaro](https://github.com/kentaro)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

判定特化モデル Jev に将棋を指させる実験（ロリポップ！AIゲートウェイ経由）

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
<td align="center" valign="top"><video src="https://raw.githubusercontent.com/kentaro/jev-shogi/main/games/20260918-214930-skill-20/game.mp4" controls muted loop playsinline width="100%"><source src="https://raw.githubusercontent.com/kentaro/jev-shogi/main/games/20260918-214930-skill-20/game.mp4" type="video/mp4"><a href="https://raw.githubusercontent.com/kentaro/jev-shogi/main/games/20260918-214930-skill-20/game.mp4">เปิดวิดีโอ</a></video></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-master">kevin9327/jev-master</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · MIT · [kevin9327](https://github.com/kevin9327)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Typed System One decisions with Jev: Choice + Score + Noul composed in code.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevin9327--jev-master/cbf05c4561269075.png" width="100%" alt="kevin9327/jev-master screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kspviswa/chakravyuha-jev">kspviswa/chakravyuha-jev</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · MIT · [kspviswa](https://github.com/kspviswa)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kspviswa--chakravyuha-jev/4dfa22d0de9f27c1.png" width="100%" alt="kspviswa/chakravyuha-jev screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/LukasCaha/jev-theme">LukasCaha/jev-theme</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · JavaScript · [LukasCaha](https://github.com/LukasCaha)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Jev powered string to color theme generator

</details>

<details>
<summary><b><a href="https://github.com/memorysaver/jev-atari-lab">memorysaver/jev-atari-lab</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · GPL-2.0 · [memorysaver](https://github.com/memorysaver)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Challenge Atari with Jev: structured decisions, value questions, and replayable experiments

</details>

<details>
<summary><b><a href="https://github.com/milanterhes/ai-column-jev">milanterhes/ai-column-jev</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · [milanterhes](https://github.com/milanterhes)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/Nachom3/jevTrader">Nachom3/jevTrader</a></b> — Rust · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Rust · [Nachom3](https://github.com/Nachom3)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A High Frecuncy Trader made in Rust using Jev as a decision maker.

</details>

<details>
<summary><b><a href="https://github.com/narulaskaran/jev-data-questions">narulaskaran/jev-data-questions</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · [narulaskaran](https://github.com/narulaskaran)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/pavy23/jev_typesafeai_test">pavy23/jev_typesafeai_test</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · [pavy23](https://github.com/pavy23)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/scottjoyner/my-jev">scottjoyner/my-jev</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · [scottjoyner](https://github.com/scottjoyner)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/semenovdv/jev_maze">semenovdv/jev_maze</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · [semenovdv](https://github.com/semenovdv)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-context-curator">Shashank-H/pi-jev-context-curator</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [Shashank-H](https://github.com/Shashank-H)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

A Jev based context curator for pi

</details>

<details>
<summary><b><a href="https://github.com/sueszli/qwen27b-jev">sueszli/qwen27b-jev</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · MIT · [sueszli](https://github.com/sueszli)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

multiple-choice questions for Qwen3.8-27B, read from logits

</details>

<details>
<summary><b><a href="https://github.com/TonyP-MR/jev-curation-engine">TonyP-MR/jev-curation-engine</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · [TonyP-MR](https://github.com/TonyP-MR)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions with existing LLM audit results.

</details>

<details>
<summary><b><a href="https://github.com/trufyrelabs/tru-jev-harness">trufyrelabs/tru-jev-harness</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · TypeScript · MIT · [trufyrelabs](https://github.com/trufyrelabs)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/Waxmell114514/jev-trade">Waxmell114514/jev-trade</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · Python · [Waxmell114514](https://github.com/Waxmell114514)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Waxmell114514/jev-trade/claude/ecstatic-bardeen-tknnox/docs/demo.png" width="100%" alt="Waxmell114514/jev-trade screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

<sub>ไฟล์ถูกดึงแบบฮอตลิงก์จากรีโพซิทอรีต้นทาง เนื่องจากไม่มีการประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ</sub>

</details>

<details>
<summary><b><a href="https://github.com/ybelatar/pokemon_jev">ybelatar/pokemon_jev</a></b> — inferred · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `inferred` · [ybelatar](https://github.com/ybelatar)

**ข้อมูล** · ดาว **0** · ฟอร์ก 0 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

_ต้นทางไม่ได้เผยแพร่คำอธิบาย_

</details>

<details>
<summary><b><a href="https://github.com/realZachi/typesafe-adblock">realZachi/typesafe-adblock</a></b> — ⭐42 · JavaScript · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · JavaScript · MIT · [realZachi](https://github.com/realZachi)

**ข้อมูล** · ดาว **42** · ฟอร์ก 3 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.

</details>

<details>
<summary><b><a href="https://github.com/devanshbatham/commit-miner">devanshbatham/commit-miner</a></b> — ⭐20 · Rust · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · Rust · [devanshbatham](https://github.com/devanshbatham)

**ข้อมูล** · ดาว **20** · ฟอร์ก 5 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-17 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.

</details>

<details>
<summary><b><a href="https://github.com/andysc/IBM-Q-System-One-3D-model">andysc/IBM-Q-System-One-3D-model</a></b> — ⭐12 · OpenSCAD · unverified · 2687 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · OpenSCAD · [andysc](https://github.com/andysc)

**ข้อมูล** · ดาว **12** · ฟอร์ก 4 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2019-03-16 · push ล่าสุด 2019-05-10 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

3D-printed model of IBM Q System One

</details>

<details>
<summary><b><a href="https://github.com/phyous/tsai-sc">phyous/tsai-sc</a></b> — ⭐12 · Python · unverified · 2 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · Python · MIT · [phyous](https://github.com/phyous)

**ข้อมูล** · ดาว **12** · ฟอร์ก 1 · issue ที่เปิดอยู่ 0 · สร้างเมื่อ 2026-09-16 · push ล่าสุด 2026-09-16 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.

<table><tr><th align="center" width="50%">รูปภาพ</th><th align="center" width="50%">วิดีโอ</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/phyous--tsai-sc/f48a030ae92fb1fe.png" width="100%" alt="phyous/tsai-sc screenshot"></td>
<td align="center" valign="top"><sub>ไม่มีสื่อที่เผยแพร่</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/razorback16/openjev">razorback16/openjev</a></b> — ⭐11 · Python · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · Python · Apache-2.0 · [razorback16](https://github.com/razorback16)

**ข้อมูล** · ดาว **11** · ฟอร์ก 0 · issue ที่เปิดอยู่ 1 · สร้างเมื่อ 2026-09-18 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Open, Jev-compatible System One decision server on DiffusionGemma

</details>

<details>
<summary><b><a href="https://github.com/zhengxuyu/litjev">zhengxuyu/litjev</a></b> — ⭐3 · Python · unverified · 0 天 · **NEW**</summary>

**ข้อมูลพื้นฐาน** · `บทความ การสนทนา และรายการที่เกี่ยวข้อง` · ชุมชน · `unverified` · Python · Apache-2.0 · [zhengxuyu](https://github.com/zhengxuyu)

**ข้อมูล** · ดาว **3** · ฟอร์ก 1 · issue ที่เปิดอยู่ 2 · สร้างเมื่อ 2026-09-17 · push ล่าสุด 2026-09-18 · ขึ้นรายการครั้งแรก 2026-09-18

**สรุป**

Turn any off-the-shelf LLM into a Jev -like decision layer

</details>

<a id="projects-by-implementation-language"></a>

## โปรเจกต์ตามภาษาที่ใช้พัฒนา

ระบบนิเวศกระจุกตัวอยู่ใน Python และ TypeScript แต่ไคลเอนต์แบบมีชนิดยังปรากฏในภาษาอื่นเรื่อย ๆ ตารางนี้สร้างจากตัวรายการเอง

| ภาษา | รายการ | ตัวอย่าง |
| --- | --- | --- |
| Python | 133 | `typesafe-ai/system-one-adapter-python`, `typesafe-ai/typesafe-sdk-python`, `realZachi/pg-jev` |
| TypeScript | 113 | `typesafe-ai/typesafe-sdk-js`, `NicolasMontone/jev-evals`, `AntonioCoppe/jev-harness` |
| JavaScript | 51 | `ziyu/sytem-one-sdk`, `Ying-Kai-Liao/jev-browser`, `arunav25/jev-mcp` |
| Go | 16 | `Gaurav-Gosain/jev-go`, `Stumble/jev-go`, `anilsenay/jev` |
| Rust | 12 | `AkashPriyadarshii/jev-curate`, `abeldzan/jev-rs`, `AkashPriyadarshii/jev-git` |
| HTML | 10 | `typesafe-ai/typesafe-ai.github.io`, `yzfly/awesome-jev-zh`, `vinilana/jev-eval-agent` |
| PHP | 4 | `Butochnikov/laravel-typesafe-jev`, `mzainzulifqar/jev-php-sdk`, `shanginn/jev-php` |
| Elixir | 3 | `nshkrdotcom/typesafe_sdk`, `typesend/typesafe_ai`, `dannote/jev` |
| Java | 2 | `Premo-Cloud/typesafe-sdk-java`, `Olti1947/jev-java` |
| Jupyter | 2 | `jexp/neo4jev`, `bitnovus/jev-spam-eval` |
| C | 1 | `giuliosmall/pg_typesafe` |
| C# | 1 | `saibimajdi/typesafeai-dotnet-sdk` |
| CSS | 1 | `AbdelStark/awesome-typesafe` |
| Dart | 1 | `Bud-ro/jev-demos` |
| Haskell | 1 | `inanna-malick/jev-dsl` |
| Lex | 1 | `alpibrusl/lex-judge` |
| Makefile | 1 | `bottlebrushes/jev-orb` |
| OCaml | 1 | `jonesmelton/verdict` |
| OpenSCAD | 1 | `andysc/IBM-Q-System-One-3D-model` |
| PowerShell | 1 | `omni-/ask-jev` |
| Ruby | 1 | `javiergradiche/ruby_llm-providers-typesafe` |
| TeX | 1 | `dnakhoa/jev-deferred-crispification` |

<sub>นับเฉพาะรายการที่ระบุภาษา ส่วนรายการที่เป็นโครงสร้างพื้นฐาน เอกสาร และการสนทนาไม่รวมอยู่ในตารางนี้</sub>

## รายการนี้เป็นปัจจุบันได้อย่างไร

ไม่มีมนุษย์แก้เนื้อหาของ README นี้ รีโพซิทอรีรันไปป์ไลน์ห้าขั้นตามกำหนดเวลา และ commit เฉพาะเมื่อมีการเปลี่ยนแปลงจริงเท่านั้น

<img src="assets/readme/pipeline.svg" width="100%" alt="รายการนี้เป็นปัจจุบันได้อย่างไร">

- **collect** — ค้นหาบน GitHub ผ่านเมทริกซ์คำค้น องค์กรทางการ การค้นหาโค้ดของ GitHub, Hacker News และฮับ HuggingFace
- **curate** — เป็นดีเทอร์มินิสติกและไม่ใช้ LLM ดังนั้นการรันสองครั้งติดกันบนอินพุตเดียวกันจึงให้ผลลัพธ์เหมือนกันทุกไบต์ กฎสองสัญญาณตัดสินความเกี่ยวข้อง ชื่อที่ชนกัน (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD และทำนองเดียวกัน) ถูกตัดออกด้วยรายการที่ชัดเจนและตรวจสอบได้
- **media** — เก็บภาพหน้าจอและบันทึกหน้าจอของแต่ละโปรเจกต์ ไฟล์จะถูกคัดลอกเข้ามาในรีโพซิทอรีนี้เฉพาะเมื่อโปรเจกต์ประกาศสัญญาอนุญาตที่เอื้อต่อการเผยแพร่ต่อ มิฉะนั้นจะฮอตลิงก์ URL ต้นทาง และการ์ดจะระบุไว้
- **render** — สร้างทุกฉบับภาษาจากเทมเพลตเดียว ดังนั้น README ทั้งยี่สิบฉบับจึงไม่มีทางต่างกันในโครงสร้าง
- **audit** — ทำให้บิลด์ล้มเหลวถ้ารายการหนึ่งไม่มี URL ถ้าลิงก์ตาย ถ้าสองรายการมี URL ซ้ำกัน หรือถ้า README เบี่ยงจากรูปแบบที่สร้างขึ้น

## การมีส่วนร่วม

ยินดีรับการแก้ไข และนั่นเป็นวิธีที่เร็วที่สุดในการปรับปรุงรายการนี้ เปิด issue หรือ pull request หากรายการถูกจัดหมวดผิด ให้เกรดผิด หรือมีโปรเจกต์ถูกตัดออกผิดเพราะเข้าใจว่าเป็นชื่อที่ชนกัน — หมวดหลังนี้คือจุดที่ตัวกรองอัตโนมัติมีโอกาสผิดมากที่สุด วิธีเพิ่มรายการที่ดีที่สุดคือเพิ่มแหล่งข้อมูลใน `scripts/collect.py` แทนการแก้ README เพราะ README ถูกสร้างใหม่ทุกรอบ

---

<sub>โปรเจกต์ชุมชนอิสระ ไม่มีความเกี่ยวข้อง ไม่ได้รับการรับรอง และไม่ได้รับการตรวจทานโดย TypeSafe AI พฤติกรรมผลิตภัณฑ์ ราคา ขีดจำกัด และนามแฝงโมเดลเปลี่ยนแปลงได้โดยไม่แจ้งล่วงหน้า โปรดตรวจสอบสิ่งที่เป็นข้อสำคัญกับเอกสารทางการ ไฟล์ต่าง ๆ ยังเป็นทรัพย์สินของโปรเจกต์ต้นทาง และถูกทำซ้ำเฉพาะเมื่อสัญญาอนุญาตเอื้อให้เท่านั้น</sub>

<sub>สร้างโดย · `render.py` · 2026-09-18T21:49:39+08:00</sub>
