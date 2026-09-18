<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>प्रमाण-श्रेणीबद्ध Jev सूचकांक, जो हर दो घंटे में स्वयं को फिर से बनाता है।</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-409-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <b>हिन्दी</b> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **लाइव सूचकांक** · अंतिम सिंक: `2026-09-18T22:17:25+08:00` (UTC+8)
> · प्रविष्टियाँ: **409** · इस चक्र में नई: **27** · कार्यान्वयन भाषाएँ: **21**

<sub>नीचे दी गई हर प्रविष्टि इस रिपॉज़िटरी की पाइपलाइन द्वारा एकत्रित, फ़िल्टर और पुनः जाँची गई है। संख्याएँ और समय-चिह्न स्रोतों से आते हैं, हाथ से लिखे स्नैपशॉट से नहीं।</sub>

## Jev क्या है?

Jev, TypeSafe AI का पहला **System One मॉडल** है। यह गद्य नहीं लिखता। यह एक स्थिति और ऐसे प्रश्न लेता है जिनका उत्तर-क्षेत्र आप पहले से तय करते हैं, और टाइप्ड मान प्रायिकता वितरण के साथ लौटाता है जिन पर आपका कोड शाखा बना सकता है।

- **रूप:** `state + typed questions` → `constrained answers + probabilities` → `your code`
- **प्रिमिटिव:** `Choice` (≤255 विकल्पों में से एक चुनें), `Score` (2–10 का रूब्रिक), `Noul` (प्रायिक हाँ/नहीं)
- **एंडपॉइंट:** `POST https://api.typesafe.ai/v1/systemone`, मॉडल `jev-1.13.0` / उपनाम `jev-latest`
- **उपयुक्त:** सीमित कार्यप्रवाह के भीतर रूटिंग, ट्राइएज, स्कोरिंग, मॉडरेशन, सत्यापन और कम-विलंबता गेट
- **ज्ञात सीमाएँ:** गिनती अविश्वसनीय है, बहुस्तरीय परोक्षता कमज़ोर है, और आधिकारिक सामग्री में नौ प्रकार की असमानता बताई गई है। स्कीमा-वैध आउटपुट सही निर्णय के बराबर नहीं है — अपने ही डेटा पर कैलिब्रेट करें।

## प्रविष्टियों का दर्जा कैसे तय होता है

इस क्षेत्र की अधिकांश सूचियाँ बस समावेशन का दावा करती हैं। यह बताती है कि उसने वास्तव में कितना सत्यापित किया, और फिर आपको उसी अनुसार फ़िल्टर करने देती है।

| दर्जा | इसका क्या अर्थ है |
| --- | --- |
| `official` | TypeSafe AI द्वारा स्वयं प्रकाशित। |
| `observed` | एक सार्वजनिक कृति जिसे खोला और पढ़ा जा सकता है — वास्तविक स्रोत, वास्तविक कॉन्फ़िगरेशन, या रिपॉज़िटरी नाम या टॉपिक में स्पष्ट TypeSafe/Jev घोषणा। |
| `inferred` | एक अस्पष्ट संकेत और समर्थक शब्दावली के आधार पर मेल, पर अभी पंक्ति-दर-पंक्ति नहीं पढ़ा गया। |
| `unverified` | संबंधित लगता है, स्वतंत्र रूप से कुछ भी पुष्ट नहीं हुआ। केवल खोज के लिए सूचीबद्ध। |

## विषय-सूची

- [आधिकारिक SDK और डेवलपर उपकरण](#official-sdk) — **5**
- [समुदाय के क्लाइंट, SDK और अडैप्टर](#community-sdk) — **70**
- [एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट](#agent-tooling) — **112**
- [रूटिंग, गार्डरेल और अनुमोदन](#routing-guardrails) — **39**
- [मूल्यांकन, कैलिब्रेशन और बेंचमार्क](#evaluation) — **30**
- [खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध](#research-models) — **13**
- [अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो](#apps-demos) — **37**
- [लेखन, चर्चाएँ और समान सूचियाँ](#media-discussions) — **103**
- [कार्यान्वयन भाषा के अनुसार परियोजनाएँ](#projects-by-implementation-language)

<a id="official-sdk"></a>

## आधिकारिक SDK और डेवलपर उपकरण <sub>· 5</sub>

वह सब जो TypeSafe ने स्वयं प्रकाशित किया है। यहीं से शुरू करें।

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐190 · official · 6 天 · ⭐+5</summary>

**बुनियादी तथ्य** · `आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · MIT · [typesafe-ai](https://github.com/typesafe-ai)

**डेटा** · स्टार **190** (+5) · फ़ॉर्क 10 · खुले इश्यू 0 · बनाया गया 2026-08-24 · अंतिम पुश 2026-09-12 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐110 · TypeScript · official · 2 天 · ⭐+3</summary>

**बुनियादी तथ्य** · `आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · TypeScript · MIT · [typesafe-ai](https://github.com/typesafe-ai)

**डेटा** · स्टार **110** (+3) · फ़ॉर्क 7 · खुले इश्यू 6 · बनाया गया 2026-09-04 · अंतिम पुश 2026-09-15 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐103 · Python · official · 0 天 · ⭐+3</summary>

**बुनियादी तथ्य** · `आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · Python · MIT · [typesafe-ai](https://github.com/typesafe-ai)

**डेटा** · स्टार **103** (+3) · फ़ॉर्क 9 · खुले इश्यू 0 · बनाया गया 2026-08-08 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>कोड में प्रयुक्त पाया गया: `README.md`, `src/system_one_adapter/__init__.py`, `src/system_one_adapter/_response.py`, `src/system_one_adapter/_utils/error_handling.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐77 · Python · official · 0 天 · ⭐+4</summary>

**बुनियादी तथ्य** · `आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · Python · MIT · [typesafe-ai](https://github.com/typesafe-ai)

**डेटा** · स्टार **77** (+4) · फ़ॉर्क 6 · खुले इश्यू 1 · बनाया गया 2026-09-04 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>कोड में प्रयुक्त पाया गया: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 105 天</summary>

**बुनियादी तथ्य** · `आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · HTML · [typesafe-ai](https://github.com/typesafe-ai)

**डेटा** · स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 1 · बनाया गया 2024-05-28 · अंतिम पुश 2026-06-04 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<a id="community-sdk"></a>

## समुदाय के क्लाइंट, SDK और अडैप्टर <sub>· 70</sub>

System One एंडपॉइंट के लिए टाइप्ड क्लाइंट, उतनी भाषाओं में जितनी तक समुदाय पहुँचा है।

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐124 · Python · observed · 0 天 · ⭐+4</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Python · NOASSERTION · [realZachi](https://github.com/realZachi)

**डेटा** · स्टार **124** (+4) · फ़ॉर्क 5 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

<sub>कोड में प्रयुक्त पाया गया: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐15 · Jupyter · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Jupyter · MIT · [jexp](https://github.com/jexp)

**डेटा** · स्टार **15** · फ़ॉर्क 2 · खुले इश्यू 1 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · TypeScript · MIT · [AntonioCoppe](https://github.com/AntonioCoppe)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Python · CC0-1.0 · [MrJev](https://github.com/MrJev)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · TypeScript · [opaielsheikh](https://github.com/opaielsheikh)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐1 · Rust · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Rust · MIT · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐1 · Elixir · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Elixir · MIT · [nshkrdotcom](https://github.com/nshkrdotcom)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — ⭐1 · Java · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Java · MIT · [Premo-Cloud](https://github.com/Premo-Cloud)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · JavaScript · MIT · [ziyu](https://github.com/ziyu)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/ehmpathy/rhachet-brains-typesafeai">ehmpathy/rhachet-brains-typesafeai</a></b> — observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · MIT · [ehmpathy](https://github.com/ehmpathy)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

rhachet brain.atom adapter for typesafe.ai classifier models

</details>

<details>
<summary><b><a href="https://github.com/ivorpad/skillranker">ivorpad/skillranker</a></b> — observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · NOASSERTION · [ivorpad](https://github.com/ivorpad)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Ruby · MIT · [javiergradiche](https://github.com/javiergradiche)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/jonesmelton/verdict">jonesmelton/verdict</a></b> — OCaml · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · OCaml · MIT · [jonesmelton](https://github.com/jonesmelton)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

ocaml sdk for typesafe.ai's jev model

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · TypeScript · [nu-sync](https://github.com/nu-sync)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Elixir · MIT · [typesend](https://github.com/typesend)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Python · [xingwudao](https://github.com/xingwudao)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐22 · TypeScript · inferred · 0 天 · ⭐+2</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [nidhi-singh02](https://github.com/nidhi-singh02)

**डेटा** · स्टार **22** (+2) · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">यहाँ देखें img.youtube.com</a> · प्लेबैक होस्ट साइट पर खुलता है; GitHub इसे इनलाइन एम्बेड नहीं कर सकता</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gamesonrblx/Jevbridge">gamesonrblx/Jevbridge</a></b> — ⭐13 · TypeScript · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [gamesonrblx](https://github.com/gamesonrblx)

**डेटा** · स्टार **13** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

> Bridges the typed-decision layer to the agent protocols other tools already speak.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gamesonrblx--jevbridge/772995670b3e42e9.png" width="100%" alt="gamesonrblx/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐11 · TypeScript · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [shiftynick](https://github.com/shiftynick)

**डेटा** · स्टार **11** (+1) · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐9 · Elixir · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Elixir · MIT · [dannote](https://github.com/dannote)

**डेटा** · स्टार **9** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐7 · JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · JavaScript · MIT · [Ying-Kai-Liao](https://github.com/Ying-Kai-Liao)

**डेटा** · स्टार **7** · फ़ॉर्क 3 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐6 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · [AboveColin](https://github.com/AboveColin)

**डेटा** · स्टार **6** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Home Assistant integration for TypeSafe Jev. Ask a question about your house and get a probability, a choice or a score as an entity.

</details>

<details>
<summary><b><a href="https://github.com/saibimajdi/typesafeai-dotnet-sdk">saibimajdi/typesafeai-dotnet-sdk</a></b> — ⭐5 · C# · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · C# · MIT · [saibimajdi](https://github.com/saibimajdi)

**डेटा** · स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with structured, confidence-scored answers. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/sharziki/semdecide">sharziki/semdecide</a></b> — ⭐5 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · [sharziki](https://github.com/sharziki)

**डेटा** · स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.

</details>

<details>
<summary><b><a href="https://github.com/arunav25/jev-mcp">arunav25/jev-mcp</a></b> — ⭐3 · JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · JavaScript · MIT · [arunav25](https://github.com/arunav25)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and measurable accuracy.

</details>

<details>
<summary><b><a href="https://github.com/docxology/daf-jev">docxology/daf-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · [docxology](https://github.com/docxology)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

daf-jev: composable Python toolkit for TypeSafe's Jev (System One) decision API — question builders, confidence gates, evaluator, calibration, CLI, MCP server, agent skill

</details>

<details>
<summary><b><a href="https://github.com/frostney/clean-code-review">frostney/clean-code-review</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [frostney](https://github.com/frostney)

**डेटा** · स्टार **3** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Every code file in a pull request, judged against Uncle Bob's Clean Code by TypeSafe's Jev, then reviewed by Luna. Built on eve and Next.js.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/frostney--clean-code-review/7d8a8de446e1c27b.png" width="100%" alt="frostney/clean-code-review screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Butochnikov/laravel-typesafe-jev">Butochnikov/laravel-typesafe-jev</a></b> — ⭐2 · PHP · inferred · 1 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · PHP · MIT · [Butochnikov](https://github.com/Butochnikov)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency injection, and testing fakes.

</details>

<details>
<summary><b><a href="https://github.com/romaluev/jev-ego">romaluev/jev-ego</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · NOASSERTION · [romaluev](https://github.com/romaluev)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move.

</details>

<details>
<summary><b><a href="https://github.com/tumf/jev-cli">tumf/jev-cli</a></b> — ⭐2 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · [tumf](https://github.com/tumf)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Small dependency-free CLI for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/yzfly/awesome-jev-zh">yzfly/awesome-jev-zh</a></b> — ⭐2 · HTML · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · HTML · CC0-1.0 · [yzfly](https://github.com/yzfly)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目。

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/jevclient">AboveColin/jevclient</a></b> — ⭐1 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · [AboveColin](https://github.com/AboveColin)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.

</details>

<details>
<summary><b><a href="https://github.com/burnigtm/jev-mcp">burnigtm/jev-mcp</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [burnigtm](https://github.com/burnigtm)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client

</details>

<details>
<summary><b><a href="https://github.com/felpsdev/jev-classifier">felpsdev/jev-classifier</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [felpsdev](https://github.com/felpsdev)

**डेटा** · स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/felpsdev--jev-classifier/d753de26b0e6c7b6.webp" width="100%" alt="felpsdev/jev-classifier screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-go">Gaurav-Gosain/jev-go</a></b> — ⭐1 · Go · inferred · 2 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Go · MIT · [Gaurav-Gosain](https://github.com/Gaurav-Gosain)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Go client for TypeSafe's System One API and its model Jev: typed judgments and calibrated probabilities instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/himomohi/aside-jev">himomohi/aside-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · [himomohi](https://github.com/himomohi)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model, Aside is the browser runtime.

</details>

<details>
<summary><b><a href="https://github.com/jtsang4/jev-cli">jtsang4/jev-cli</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [jtsang4](https://github.com/jtsang4)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

CLI for TypeSafe AI's Jev evaluation model — typed questions in, structured JSON answers out

</details>

<details>
<summary><b><a href="https://github.com/Olti1947/jev-java">Olti1947/jev-java</a></b> — ⭐1 · Java · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Java · [Olti1947](https://github.com/Olti1947)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 6 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Idiomatic Java SDK for TypeSafe AI Jev System One decision engine

</details>

<details>
<summary><b><a href="https://github.com/rhighs/jev-code">rhighs/jev-code</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · [rhighs](https://github.com/rhighs)

**डेटा** · स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhighs/jev-code/main/assets/jev-code-logo.png" width="100%" alt="rhighs/jev-code screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/StefanoITA/ts-jev-cost-calculator">StefanoITA/ts-jev-cost-calculator</a></b> — ⭐1 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · [StefanoITA](https://github.com/StefanoITA)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API requests. Not affiliated with TypeSafe.

</details>

<details>
<summary><b><a href="https://github.com/Stumble/jev-go">Stumble/jev-go</a></b> — ⭐1 · Go · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Go · MIT · [Stumble](https://github.com/Stumble)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Community Go SDK for TypeSafe AI Jev / System One

</details>

<details>
<summary><b><a href="https://github.com/tontoko/jev-browser">tontoko/jev-browser</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · JavaScript · Apache-2.0 · [tontoko](https://github.com/tontoko)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 3 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations and deterministic assertions.

</details>

<details>
<summary><b><a href="https://github.com/abeldzan/jev-rs">abeldzan/jev-rs</a></b> — Rust · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Rust · MIT · [abeldzan](https://github.com/abeldzan)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Async-first Rust SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-git">AkashPriyadarshii/jev-git</a></b> — Rust · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Rust · MIT · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Sub-second Git pre-commit & pre-push semantic reflex gate powered by TypeSafe AI Jev

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-scout">AkashPriyadarshii/jev-scout</a></b> — Rust · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Rust · MIT · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-seo">AkashPriyadarshii/jev-seo</a></b> — Rust · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Rust · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

100% free ₹0 agent-first SEO & GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via DuckDuckGo and TypeSafe Jev System One

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-superpowers">AkashPriyadarshii/jev-superpowers</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · JavaScript · MIT · [AkashPriyadarshii](https://github.com/AkashPriyadarshii)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed decisions

</details>

<details>
<summary><b><a href="https://github.com/anilsenay/jev">anilsenay/jev</a></b> — Go · inferred · 1 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Go · MIT · [anilsenay](https://github.com/anilsenay)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Unofficial Go client for TypeSafe's System One API  and its model, Jev.

</details>

<details>
<summary><b><a href="https://github.com/brnyxx/jev-ra">brnyxx/jev-ra</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · [brnyxx](https://github.com/brnyxx)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 2 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every step in ~300 ms.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7592fce4641d10.png" width="100%" alt="brnyxx/jev-ra screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brnyxx--jev-ra/1f7ddcd1053825a2.gif" width="100%" alt="brnyxx/jev-ra animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/david1gp/jev">david1gp/jev</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [david1gp](https://github.com/david1gp)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Result-based TypeSafe System One client library and jev command-line interface.

</details>

<details>
<summary><b><a href="https://github.com/kazz187/jev-sdk-go">kazz187/jev-sdk-go</a></b> — Go · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Go · MIT · [kazz187](https://github.com/kazz187)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Go 1.27 client for TypeSafe AI's Jev (System One) API: typed questions, typed answers

</details>

<details>
<summary><b><a href="https://github.com/krw82/jev-playwright-mcp">krw82/jev-playwright-mcp</a></b> — TypeScript · inferred · 1 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [krw82](https://github.com/krw82)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot pruning, risky-action gating. Drop-in wrapper around @playwright/mcp for any coding agent.

</details>

<details>
<summary><b><a href="https://github.com/kunobi-ninja/kunobi-jev">kunobi-ninja/kunobi-jev</a></b> — Rust · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Rust · Apache-2.0 · [kunobi-ninja](https://github.com/kunobi-ninja)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Rust client for the TypeSafe System One API (Jev)

</details>

<details>
<summary><b><a href="https://github.com/lhotwll217/jev-cli">lhotwll217/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · [lhotwll217](https://github.com/lhotwll217)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

JSON-in, typed-decisions-out CLI for the TypeSafe System One API

</details>

<details>
<summary><b><a href="https://github.com/manojlds/jev-review">manojlds/jev-review</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · [manojlds](https://github.com/manojlds)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Standalone TypeSafe Jev code-review CLI: typed decisions over a local git diff.

</details>

<details>
<summary><b><a href="https://github.com/mhmdkzr/jev">mhmdkzr/jev</a></b> — Go · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Go · MIT · [mhmdkzr](https://github.com/mhmdkzr)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

An unofficial Go client for TypeSafe's System One Jev model

</details>

<details>
<summary><b><a href="https://github.com/mzainzulifqar/jev-php-sdk">mzainzulifqar/jev-php-sdk</a></b> — PHP · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · PHP · MIT · [mzainzulifqar](https://github.com/mzainzulifqar)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

PHP SDK for TypeSafe's Jev: send text and typed questions, get typed answers with calibrated confidence. PHP 8.1+, works with any PSR-18 client, Laravel 8–13.

</details>

<details>
<summary><b><a href="https://github.com/Nasrallah-AL/jev-cli">Nasrallah-AL/jev-cli</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · [Nasrallah-AL](https://github.com/Nasrallah-AL)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Command-line tool for TypeSafe's Jev AI model

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-go">nekowasabi/jev-routing-go</a></b> — Go · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Go · MIT · [nekowasabi](https://github.com/nekowasabi)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.

</details>

<details>
<summary><b><a href="https://github.com/okooo5km/jev">okooo5km/jev</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · Apache-2.0 · [okooo5km](https://github.com/okooo5km)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed decisions from the shell: a stdlib-Python CLI and Agent Skill for TypeSafe Jev on OpenRouter. Yes/no, choice and ordinal scores with calibrated probabilities, semantic grep and batch mode.

</details>

<details>
<summary><b><a href="https://github.com/phuthuycoding/jev-audit">phuthuycoding/jev-audit</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · [phuthuycoding](https://github.com/phuthuycoding)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

AI-powered pre-commit auditor backed by TypeSafe System One (Jev) — blocks secrets, vulns & low-quality code in ~300ms. 79-case test corpus at 100% accuracy.

</details>

<details>
<summary><b><a href="https://github.com/shanginn/jev-php">shanginn/jev-php</a></b> — PHP · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · PHP · MIT · [shanginn](https://github.com/shanginn)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Type-safe PHP 8.5 SDK for JEV decisions on OpenRouter: choices, scores, probabilities and typed DTOs.

</details>

<details>
<summary><b><a href="https://github.com/zhirschtritt/typesafe-go">zhirschtritt/typesafe-go</a></b> — Go · inferred · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Go · MIT · [zhirschtritt](https://github.com/zhirschtritt)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Idiomatic Go SDK for the TypeSafe AI API

</details>

<details>
<summary><b><a href="https://github.com/pithings/advocaat">pithings/advocaat</a></b> — ⭐63 · TypeScript · unverified · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `unverified` · TypeScript · MIT · [pithings](https://github.com/pithings)

**डेटा** · स्टार **63** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/Tangerg/typesafe-sdk-go">Tangerg/typesafe-sdk-go</a></b> — ⭐7 · Go · unverified · 0 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `unverified` · Go · MIT · [Tangerg](https://github.com/Tangerg)

**डेटा** · स्टार **7** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Go SDK for the TypeSafe AI API — typed questions in, probability distributions out.

</details>

<details>
<summary><b><a href="https://github.com/giuliosmall/pg_typesafe">giuliosmall/pg_typesafe</a></b> — ⭐5 · C · unverified · 0 天 · ⭐+2</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `unverified` · C · MIT · [giuliosmall](https://github.com/giuliosmall)

**डेटा** · स्टार **5** (+2) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/typesafe-cli">y0usaf/typesafe-cli</a></b> — ⭐4 · TypeScript · unverified · 2 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `unverified` · TypeScript · MIT · [y0usaf](https://github.com/y0usaf)

**डेटा** · स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose

</details>

<details>
<summary><b><a href="https://github.com/Brainwires/jevwire">Brainwires/jevwire</a></b> — ⭐3 · TypeScript · unverified · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `unverified` · TypeScript · MIT · [Brainwires](https://github.com/Brainwires)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code plugin (TypeSafe AI's Jev)

</details>

<details>
<summary><b><a href="https://github.com/geilt/typesafe-cli">geilt/typesafe-cli</a></b> — ⭐3 · Python · unverified · 1 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `unverified` · Python · [geilt](https://github.com/geilt)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.

</details>

<details>
<summary><b><a href="https://github.com/gilljon/typesafe-ai-rs">gilljon/typesafe-ai-rs</a></b> — ⭐3 · Rust · unverified · 1 天</summary>

**बुनियादी तथ्य** · `समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `unverified` · Rust · MIT · [gilljon](https://github.com/gilljon)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Independent async and blocking Rust SDK for the TypeSafe AI System One API

</details>

<a id="agent-tooling"></a>

## एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट <sub>· 112</sub>

सबसे तेज़ी से बढ़ती श्रेणी: हुक, MCP सर्वर और गेट, जो एजेंट की अगली कार्रवाई से पहले एक टाइप्ड निर्णय रखते हैं।

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐2451 · TypeScript · observed · 0 天 · ⭐+76</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · MIT · [tamaratran](https://github.com/tamaratran)

**डेटा** · स्टार **2451** (+76) · फ़ॉर्क 122 · खुले इश्यू 38 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>कोड में प्रयुक्त पाया गया: `src/request.ts`, `README.md`, `src/client.ts`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐114 · JavaScript · inferred · 0 天 · ⭐+2</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [gargpratyush](https://github.com/gargpratyush)

**डेटा** · स्टार **114** (+2) · फ़ॉर्क 4 · खुले इश्यू 4 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐26 · Python · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [0xNatoshi](https://github.com/0xNatoshi)

**डेटा** · स्टार **26** (+1) · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐73 · observed · 0 天 · ⭐+3</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · [dbreunig](https://github.com/dbreunig)

**डेटा** · स्टार **73** (+3) · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐12 · Python · observed · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · [GhalebDweikat](https://github.com/GhalebDweikat)

**डेटा** · स्टार **12** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · [carlaiau](https://github.com/carlaiau)

**डेटा** · स्टार **7** · फ़ॉर्क 1 · खुले इश्यू 6 · बनाया गया 2026-03-13 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · [jodan-alberts](https://github.com/jodan-alberts)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · MIT · [BYK](https://github.com/BYK)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · [24601](https://github.com/24601)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · [CrowBe](https://github.com/CrowBe)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · MIT · [gorock007](https://github.com/gorock007)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · [yousudip](https://github.com/yousudip)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐234 · TypeScript · inferred · 1 天 · ⭐+7</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [devagrawal09](https://github.com/devagrawal09)

**डेटा** · स्टार **234** (+7) · फ़ॉर्क 12 · खुले इश्यू 1 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐104 · TypeScript · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [NiazMorshed2007](https://github.com/NiazMorshed2007)

**डेटा** · स्टार **104** (+1) · फ़ॉर्क 9 · खुले इश्यू 2 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-eval-agent">vinilana/jev-eval-agent</a></b> — ⭐79 · HTML · inferred · 1 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · HTML · [vinilana](https://github.com/vinilana)

**डेटा** · स्टार **79** (+1) · फ़ॉर्क 6 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-mcp">jkudish/jev-mcp</a></b> — ⭐65 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [jkudish](https://github.com/jkudish)

**डेटा** · स्टार **65** · फ़ॉर्क 8 · खुले इश्यू 2 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Proof of concept MCP for Typesafe's new Jev AI model

> An early proof of concept for exposing Jev over MCP, which is how most non-Python toolchains reach it.

</details>

<details>
<summary><b><a href="https://github.com/RomanSlack/jev-drone">RomanSlack/jev-drone</a></b> — ⭐56 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [RomanSlack](https://github.com/RomanSlack)

**डेटा** · स्टार **56** · फ़ॉर्क 3 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/romanslack--jev-drone/b23ea2412f437970.png" width="100%" alt="RomanSlack/jev-drone screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/pi-jev">y0usaf/pi-jev</a></b> — ⭐38 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [y0usaf](https://github.com/y0usaf)

**डेटा** · स्टार **38** · फ़ॉर्क 3 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed, calibrated answers

</details>

<details>
<summary><b><a href="https://github.com/wy-coliney/jev-browser-use">wy-coliney/jev-browser-use</a></b> — ⭐26 · JavaScript · inferred · 0 天 · ⭐+4</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [wy-coliney](https://github.com/wy-coliney)

**डेटा** · स्टार **26** (+4) · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wy-coliney--jev-browser-use/581fbd89fe47c952.png" width="100%" alt="wy-coliney/jev-browser-use screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/ask-jev-skill">shantanugoel/ask-jev-skill</a></b> — ⭐25 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [shantanugoel](https://github.com/shantanugoel)

**डेटा** · स्टार **25** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Skill for Hermes, and other agents, to ask typesafe's jev

</details>

<details>
<summary><b><a href="https://github.com/supercorp-ai/supercov">supercorp-ai/supercov</a></b> — ⭐23 · Rust · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Rust · MIT · [supercorp-ai](https://github.com/supercorp-ai)

**डेटा** · स्टार **23** (+1) · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-08-23 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Code quality and coverage for coding agents

> Code quality and coverage verdicts produced as typed decisions rather than prose, so the result can gate a pipeline directly.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/supercorp-ai--supercov/063226e150cb8a6b.jpg" width="100%" alt="supercorp-ai/supercov screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐22 · JavaScript · inferred · 0 天 · ⭐+13</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [fatwang2](https://github.com/fatwang2)

**डेटा** · स्टार **22** (+13) · फ़ॉर्क 3 · खुले इश्यू 10 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/logicrw/awesome-jev-projects">logicrw/awesome-jev-projects</a></b> — ⭐17 · JavaScript · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [logicrw](https://github.com/logicrw)

**डेटा** · स्टार **17** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic GitHub sync

</details>

<details>
<summary><b><a href="https://github.com/compozy/yoshi">compozy/yoshi</a></b> — ⭐9 · TypeScript · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [compozy](https://github.com/compozy)

**डेटा** · स्टार **9** (+1) · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not claimed. POC here now, heading soon into https://github.com/compozy/compozy

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/compozy--yoshi/637d8588c227f4de.png" width="100%" alt="compozy/yoshi screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jomatsu/pi-jev-auto-mode">jomatsu/pi-jev-auto-mode</a></b> — ⭐8 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [jomatsu](https://github.com/jomatsu)

**डेटा** · स्टार **8** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write, and edit tool calls and fails closed when a decision cannot be made.

</details>

<details>
<summary><b><a href="https://github.com/blakestone-x/jev-mcp">blakestone-x/jev-mcp</a></b> — ⭐7 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [blakestone-x](https://github.com/blakestone-x)

**डेटा** · स्टार **7** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on every answer

</details>

<details>
<summary><b><a href="https://github.com/DECRUX9812/typesafe-skill-router">DECRUX9812/typesafe-skill-router</a></b> — ⭐6 · Python · inferred · 2 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [DECRUX9812](https://github.com/DECRUX9812)

**डेटा** · स्टार **6** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call. Opt-in, stdlib only, ~$0.001 per routed turn.

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-code">devagrawal09/jev-code</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [devagrawal09](https://github.com/devagrawal09)

**डेटा** · स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Bounded TypeSafe Jev workflows for coding agents.

</details>

<details>
<summary><b><a href="https://github.com/GodsBoy/jev-agent-skill-router">GodsBoy/jev-agent-skill-router</a></b> — ⭐5 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [GodsBoy](https://github.com/GodsBoy)

**डेटा** · स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed, confidence-aware agent skill routing with TypeSafe Jev.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/godsboy--jev-agent-skill-router/c80293e37dcd4faf.png" width="100%" alt="GodsBoy/jev-agent-skill-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/huntedman/JevLint">huntedman/JevLint</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [huntedman](https://github.com/huntedman)

**डेटा** · स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.

</details>

<details>
<summary><b><a href="https://github.com/GiesN/typesafe-jev-workflow">GiesN/typesafe-jev-workflow</a></b> — ⭐4 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · [GiesN](https://github.com/GiesN)

**डेटा** · स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/inanna-malick/jev-dsl">inanna-malick/jev-dsl</a></b> — ⭐4 · Haskell · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Haskell · MIT · [inanna-malick](https://github.com/inanna-malick)

**डेटा** · स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Agent-first Haskell DSL for TypeSafe's Jev judgment model: typed packets, inferred types, answers under the same labels

</details>

<details>
<summary><b><a href="https://github.com/kikoncuo/jevfire">kikoncuo/jevfire</a></b> — ⭐4 · JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [kikoncuo](https://github.com/kikoncuo)

**डेटा** · स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

JEV-inspired parallel decisions for CUDA LLMs. One context, many decisions. vLLM API, game-agent examples, and reproducible benchmarks.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kikoncuo--jevfire/2d5597bbc6b2c82e.png" width="100%" alt="kikoncuo/jevfire screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/TheoOliveira/pi-jev">TheoOliveira/pi-jev</a></b> — ⭐4 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [TheoOliveira](https://github.com/TheoOliveira)

**डेटा** · स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/anandi1989/awesome-jev-usecases">anandi1989/awesome-jev-usecases</a></b> — ⭐3 · inferred · 0 天 · ⭐+2</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · MIT · [anandi1989](https://github.com/anandi1989)

**डेटा** · स्टार **3** (+2) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos, patterns, and measured results

</details>

<details>
<summary><b><a href="https://github.com/anpicasso/hermes-jev-approvals">anpicasso/hermes-jev-approvals</a></b> — ⭐3 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [anpicasso](https://github.com/anpicasso)

**डेटा** · स्टार **3** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts, measured on 153 real commands. Approvals only.

</details>

<details>
<summary><b><a href="https://github.com/BillionsBobby/JevRouter">BillionsBobby/JevRouter</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [BillionsBobby](https://github.com/BillionsBobby)

**डेटा** · स्टार **3** · फ़ॉर्क 1 · खुले इश्यू 5 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A lightweight Jev-powered router for models, tools, and subagents

</details>

<details>
<summary><b><a href="https://github.com/SeeAPI/awesome-jev-use-cases">SeeAPI/awesome-jev-use-cases</a></b> — ⭐3 · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · CC-BY-4.0 · [SeeAPI](https://github.com/SeeAPI)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Explore real-world use cases and projects built with TypeSafe AI's Jev: content moderation, AI agents, model routing, and semantic search. Curated by SeeAPI.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/seeapi--awesome-jev-use-cases/33f9e684bff2514d.png" width="100%" alt="SeeAPI/awesome-jev-use-cases screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/caiovicentino/jev-shield">caiovicentino/jev-shield</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [caiovicentino](https://github.com/caiovicentino)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with calibrated System One verification. 94% block recall, 0 false positives, ~$0.00002/check.

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/jev-judgment">HyunjunJeon/jev-judgment</a></b> — ⭐2 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [HyunjunJeon](https://github.com/HyunjunJeon)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Agent Skill: send closed coding-agent judgments to TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/molis-ai/jev-workbench">molis-ai/jev-workbench</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [molis-ai](https://github.com/molis-ai)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Build versioned judgment functions on TypeSafe's Jev once, then call the same published version from your backend over HTTP and from coding agents over MCP. The vendor key stays on your machine.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/molis-ai--jev-workbench/00f61d8403a941cd.png" width="100%" alt="molis-ai/jev-workbench screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MongLong0214/jev-gate">MongLong0214/jev-gate</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · [MongLong0214](https://github.com/MongLong0214)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 5 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3 prototype runs today, V4 routes at the task boundary.

</details>

<details>
<summary><b><a href="https://github.com/ranjan2829/AskJev">ranjan2829/AskJev</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [ranjan2829](https://github.com/ranjan2829)

**डेटा** · स्टार **2** · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude)

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-mcp">rashedInt32/jev-mcp</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [rashedInt32](https://github.com/rashedInt32)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask. Ships as a Claude Code plugin.

</details>

<details>
<summary><b><a href="https://github.com/samtay32/jev-system-architect">samtay32/jev-system-architect</a></b> — ⭐2 · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · MIT · [samtay32](https://github.com/samtay32)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into small Choice/Score/Noul primitives.

</details>

<details>
<summary><b><a href="https://github.com/bestagentkits/jev-skillful">bestagentkits/jev-skillful</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [bestagentkits](https://github.com/bestagentkits)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands against your prompt via TypeSafe Jev, and measures whether the injection actually helps.

</details>

<details>
<summary><b><a href="https://github.com/buchmark/claude-jev">buchmark/claude-jev</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [buchmark](https://github.com/buchmark)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Claude Code plugin that scores review findings, debug hypotheses and design options with TypeSafe's Jev — calibrated probabilities instead of one more opinion.

</details>

<details>
<summary><b><a href="https://github.com/hamakyo/jev-starter">hamakyo/jev-starter</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [hamakyo](https://github.com/hamakyo)

**डेटा** · स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation, and RAG patterns for TypeScript apps.

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-model-router-demo">jcpsimmons/jev-model-router-demo</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · [jcpsimmons](https://github.com/jcpsimmons)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra

</details>

<details>
<summary><b><a href="https://github.com/omni-/ask-jev">omni-/ask-jev</a></b> — ⭐1 · PowerShell · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · PowerShell · MIT · [omni-](https://github.com/omni-)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding sessions.

</details>

<details>
<summary><b><a href="https://github.com/poponline63/hermes-jev-north-star">poponline63/hermes-jev-north-star</a></b> — ⭐1 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [poponline63](https://github.com/poponline63)

**डेटा** · स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a checkable finish line, generate the run prompt, and let Jev rank what is still unproven.

</details>

<details>
<summary><b><a href="https://github.com/Ravinder82/jev-flash-router">Ravinder82/jev-flash-router</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [Ravinder82](https://github.com/Ravinder82)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

open-sourced jev-flash-router: an MCP server for TypeSafe's new Jev model.  AI coding agents waste hundreds of reasoning tokens just deciding which file to edit, which route to pick, or whether a diff breaks tests.  Jev evaluates state and outputs calibrated probabilities.  Works with Cursor, Windsurf, & Claude Code

</details>

<details>
<summary><b><a href="https://github.com/rthomas24/jev-realtime-trading">rthomas24/jev-realtime-trading</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [rthomas24](https://github.com/rthomas24)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Paper trading agents on a live tape, decided every second by TypeSafe's Jev (System One). Electron desktop app.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rthomas24--jev-realtime-trading/f27df5cca6b8e2cf.png" width="100%" alt="rthomas24/jev-realtime-trading screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/codex-jev-compaction">Wang-auspicious/codex-jev-compaction</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [Wang-auspicious](https://github.com/Wang-auspicious)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and skills.

</details>

<details>
<summary><b><a href="https://github.com/Wang-auspicious/pi-jev-compaction">Wang-auspicious/pi-jev-compaction</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [Wang-auspicious](https://github.com/Wang-auspicious)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev-powered context compaction for Pi. Keep critical instructions and tool history, prune the noise, and fall back gracefully.

</details>

<details>
<summary><b><a href="https://github.com/ably-labs/jev-pong">ably-labs/jev-pong</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · Apache-2.0 · [ably-labs](https://github.com/ably-labs)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Pong where the ball moves one step per model decision. Jev vs LLMs via Vercel AI Gateway, every player and agent on an Ably channel.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b51a044f9d543ef0.png" width="100%" alt="ably-labs/jev-pong screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ably-labs--jev-pong/b5b9b482a58f2c01.gif" width="100%" alt="ably-labs/jev-pong animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/aidil2105/jev-browser-pilot">aidil2105/jev-browser-pilot</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [aidil2105](https://github.com/aidil2105)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A bounded decision layer for browser and desktop automation: a decision-only model picks one next step; the code owns perception, content, actuation and verification.

</details>

<details>
<summary><b><a href="https://github.com/altregubov/jev-antigravity-mcp">altregubov/jev-antigravity-mcp</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [altregubov](https://github.com/altregubov)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/anisselbd/jev-phishing-bench">anisselbd/jev-phishing-bench</a></b> — Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · [anisselbd](https://github.com/anisselbd)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost. Reproducible benchmark.

</details>

<details>
<summary><b><a href="https://github.com/cbruyndoncx/AskJev-MCP">cbruyndoncx/AskJev-MCP</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · [cbruyndoncx](https://github.com/cbruyndoncx)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

MCP server for TypeSafe's System One API (Jev): typed choice/noul/score judgments with calibrated probabilities and confidence

</details>

<details>
<summary><b><a href="https://github.com/CodeAlive-AI/mastra-jev-moderation">CodeAlive-AI/mastra-jev-moderation</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [CodeAlive-AI](https://github.com/CodeAlive-AI)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Input moderation for Mastra agents on TypeSafe Jev — one file

</details>

<details>
<summary><b><a href="https://github.com/doeixd/jev-pref">doeixd/jev-pref</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [doeixd](https://github.com/doeixd)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Turn your AGENTS.md preferences into a fast, Jev-powered AI linter.

</details>

<details>
<summary><b><a href="https://github.com/DoGMaTiiC/hermes-jev">DoGMaTiiC/hermes-jev</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · [DoGMaTiiC](https://github.com/DoGMaTiiC)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 7 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway. Fail-open, opt-in, stdlib only.

</details>

<details>
<summary><b><a href="https://github.com/dryob/hermes-jev-context-engine">dryob/hermes-jev-context-engine</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · NOASSERTION · [dryob](https://github.com/dryob)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Lossless context compaction for Hermes Agent via the TypeSafe/Jev API — deletes or truncates stale tool calls instead of summarising. Python port of tamaratran/fast-jev-compaction.

</details>

<details>
<summary><b><a href="https://github.com/duketopceo/jev-compact">duketopceo/jev-compact</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [duketopceo](https://github.com/duketopceo)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP

</details>

<details>
<summary><b><a href="https://github.com/EliaAlberti/jev-rules">EliaAlberti/jev-rules</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [EliaAlberti](https://github.com/EliaAlberti)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev picks which of your rules apply to each prompt, so Claude only sees the ones that matter.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/eliaalberti--jev-rules/f714e20b0600e246.gif" width="100%" alt="EliaAlberti/jev-rules screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/eliaalberti--jev-rules/ae4048f230729427.gif" width="100%" alt="EliaAlberti/jev-rules animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/enderzcx/spire-jev">enderzcx/spire-jev</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [enderzcx](https://github.com/enderzcx)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Slay the Spire 2 agent controller: planner models, Jev fast decisions, and verified multi-card turn execution

</details>

<details>
<summary><b><a href="https://github.com/enriquejuncorichi-create/pi-jev-assist">enriquejuncorichi-create/pi-jev-assist</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · [enriquejuncorichi-create](https://github.com/enriquejuncorichi-create)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Pi extension: checks an agent's work against observation, not against its own account of itself

</details>

<details>
<summary><b><a href="https://github.com/EtienneLescot/jev-router">EtienneLescot/jev-router</a></b> — HTML · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · HTML · MIT · [EtienneLescot](https://github.com/EtienneLescot)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model tier and reasoning depth.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/etiennelescot--jev-router/96217fad0b128b3e.png" width="100%" alt="EtienneLescot/jev-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/flaviusapop/jev-router">flaviusapop/jev-router</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [flaviusapop](https://github.com/flaviusapop)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Routes each turn in Claude Code, Codex, Grok and opencode to the cheapest model and reasoning depth that can finish it, using TypeSafe Jev

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/flaviusapop--jev-router/b7f868696d35b78b.png" width="100%" alt="flaviusapop/jev-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Friedjof/jev-mobile">Friedjof/jev-mobile</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [Friedjof](https://github.com/Friedjof)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Fast structured Android control loops with TypeSafe Jev and Mobile MCP

</details>

<details>
<summary><b><a href="https://github.com/gzawadzki/jev-usecases">gzawadzki/jev-usecases</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [gzawadzki](https://github.com/gzawadzki)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage

</details>

<details>
<summary><b><a href="https://github.com/hangarbay/jev.mcp">hangarbay/jev.mcp</a></b> — Go · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Go · MIT · [hangarbay](https://github.com/hangarbay)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

One MCP server for TypeSafe's Jev: typed, calibrated decisions instead of generated text

</details>

<details>
<summary><b><a href="https://github.com/HomenShum/jev-swap">HomenShum/jev-swap</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [HomenShum](https://github.com/HomenShum)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Claude Code skill: swap System 2 LLM pipeline components for System 1 TypeSafe Jev decisions via investigation, live three-arm eval, fallback, and an independent judge

</details>

<details>
<summary><b><a href="https://github.com/IAnMove/jev-game-agent">IAnMove/jev-game-agent</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · [IAnMove](https://github.com/IAnMove)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Experimental Jev game agent: RAM, emulator lookahead, checkpoint search and verified recordings. Bring your own ROM and BizHawk.

</details>

<details>
<summary><b><a href="https://github.com/its-panzer/jev-model-router">its-panzer/jev-model-router</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [its-panzer](https://github.com/its-panzer)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A policy router that picks the cheapest Claude model that can finish the job

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/its-panzer--jev-model-router/98819f5aaf8e6373.png" width="100%" alt="its-panzer/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jcressler/fast-jev-compaction-codex">jcressler/fast-jev-compaction-codex</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [jcressler](https://github.com/jcressler)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Codex adaptation of fast-jev-compaction: Jev-powered transcript pruning and verbatim evidence recovery around native compaction.

</details>

<details>
<summary><b><a href="https://github.com/jmanhype/jev-dspy-lab">jmanhype/jev-dspy-lab</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [jmanhype](https://github.com/jmanhype)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-harness">kevin9327/jev-harness</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [kevin9327](https://github.com/kevin9327)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

JevHarness: TypeSafe Jev agent tool-call gate. execute / confirm / reject in code.

</details>

<details>
<summary><b><a href="https://github.com/madeye/pi-jev">madeye/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [madeye](https://github.com/madeye)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev-assisted file retrieval and request caching for faster Pi workflows

</details>

<details>
<summary><b><a href="https://github.com/MahmoudAdelbghany/jev-browser">MahmoudAdelbghany/jev-browser</a></b> — JavaScript · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · [MahmoudAdelbghany](https://github.com/MahmoudAdelbghany)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright MCP included.

</details>

<details>
<summary><b><a href="https://github.com/maito1201/jev-harness">maito1201/jev-harness</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · [maito1201](https://github.com/maito1201)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe jev でエージェントの応答を審査し、形式的な完了を Stop hook で差し戻す Claude Code / Codex plugin

</details>

<details>
<summary><b><a href="https://github.com/micic-mihajlo/jev-tool-runner">micic-mihajlo/jev-tool-runner</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · [micic-mihajlo](https://github.com/micic-mihajlo)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/milanboers/jev-plays-pokemon">milanboers/jev-plays-pokemon</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · NOASSERTION · [milanboers](https://github.com/milanboers)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Playing Pokemon Red using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/minhgv/jev-mcp">minhgv/jev-mcp</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [minhgv](https://github.com/minhgv)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe Jev MCP decision layer for coding agents and CI

</details>

<details>
<summary><b><a href="https://github.com/morcoan/JevSeek">morcoan/JevSeek</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · [morcoan](https://github.com/morcoan)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools, persistent sessions, React desktop, and documented research.

</details>

<details>
<summary><b><a href="https://github.com/MSalvalaggio/jev-reflex">MSalvalaggio/jev-reflex</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [MSalvalaggio](https://github.com/MSalvalaggio)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe's Jev (~100 ms per decision).

</details>

<details>
<summary><b><a href="https://github.com/nekowasabi/jev-routing-mcp">nekowasabi/jev-routing-mcp</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · [nekowasabi](https://github.com/nekowasabi)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/noetion/dsh-jev">noetion/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [noetion](https://github.com/noetion)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.

</details>

<details>
<summary><b><a href="https://github.com/ourines/hermes-jev">ourines/hermes-jev</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [ourines](https://github.com/ourines)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev decision sidekick for Hermes Agent — TypeSafe and Cloudflare, explicit tools and official skill

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-mcp-router">Pinutss/jev-mcp-router</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [Pinutss](https://github.com/Pinutss)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Select relevant MCP tools under a context-token budget, without executing them.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-mcp-router/3947a2a5cc3750c8.png" width="100%" alt="Pinutss/jev-mcp-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-memory-selector">Pinutss/jev-memory-selector</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [Pinutss](https://github.com/Pinutss)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Filters an agent's memories to fit a token budget. Local, HTTP, MCP, Docker.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-memory-selector/6b6b7efc3440b641.png" width="100%" alt="Pinutss/jev-memory-selector screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-plugins">Pinutss/jev-plugins</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · MIT · [Pinutss](https://github.com/Pinutss)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Cursor and Hermes marketplace for the four published JEV Labs routers.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-plugins/b3fcd72ac9e61f49.jpg" width="100%" alt="Pinutss/jev-plugins screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/QuentinDanblon/pi-fast-jev-compaction">QuentinDanblon/pi-fast-jev-compaction</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · NOASSERTION · [QuentinDanblon](https://github.com/QuentinDanblon)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Verbatim context pruning for the pi coding agent, scored by TypeSafe Jev: stale tool calls and results are dropped or truncated, everything kept stays verbatim.

</details>

<details>
<summary><b><a href="https://github.com/raj8525/universal-jev">raj8525/universal-jev</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [raj8525](https://github.com/raj8525)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Universal TypeSafe Jev Runtime Plugin & MCP Server for Coding Agents

</details>

<details>
<summary><b><a href="https://github.com/rashedInt32/jev-gates">rashedInt32/jev-gates</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · [rashedInt32](https://github.com/rashedInt32)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Six calibrated gates for Claude Code, judged by TypeSafe Jev: rules, scope, intent, done, claims, and commit honesty. Each one escalates, none ever approves.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/3996d0153a09b158.gif" width="100%" alt="rashedInt32/jev-gates screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/rashedint32--jev-gates/464e518e8a602a0d.gif" width="100%" alt="rashedInt32/jev-gates animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/rashedInt32/jev-gates/main/demo/out/jev-gates.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/ravi3594444/jev-agent1">ravi3594444/jev-agent1</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · [ravi3594444](https://github.com/ravi3594444)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/rubichandrap/hermes-jev-guard">rubichandrap/hermes-jev-guard</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [rubichandrap](https://github.com/rubichandrap)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check

</details>

<details>
<summary><b><a href="https://github.com/sypherin/jev-trace-classifier">sypherin/jev-trace-classifier</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [sypherin](https://github.com/sypherin)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page authorship, head-to-head vs local Qwen3.8-Flash-Next

</details>

<details>
<summary><b><a href="https://github.com/szocpaul/jev-compaction-prime">szocpaul/jev-compaction-prime</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · [szocpaul](https://github.com/szocpaul)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Verbatim, decision-based context compaction for Prime Agent — instead of summaries, stale tool calls are scored and dropped; everything kept stays byte-for-byte intact.

</details>

<details>
<summary><b><a href="https://github.com/taisan11/jev-agent">taisan11/jev-agent</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · [taisan11](https://github.com/taisan11)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/tgiridhar/claude-code-jev-smart-router">tgiridhar/claude-code-jev-smart-router</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [tgiridhar](https://github.com/tgiridhar)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task phase and the cost of an undetected error, gated by prompt-cache arithmetic. Proof of concept.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tgiridhar--claude-code-jev-smart-router/28b9e1b2a005c7e2.png" width="100%" alt="tgiridhar/claude-code-jev-smart-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/themsquared/jev-benchmark">themsquared/jev-benchmark</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · Apache-2.0 · [themsquared](https://github.com/themsquared)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Reproducible benchmark for TypeSafe AI's Jev on agent tool-call risk classification: accuracy, latency, and whether the confidence score is worth routing on.

</details>

<details>
<summary><b><a href="https://github.com/thevibeworks/awesome-typesafe-jev">thevibeworks/awesome-typesafe-jev</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · NOASSERTION · [thevibeworks](https://github.com/thevibeworks)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Curated list of projects built on TypeSafe's Jev model, read before listed. With media and our own measurements. Not affiliated with TypeSafe AI.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/thevibeworks/awesome-typesafe-jev/main/docs/media/lab-latency.png" width="100%" alt="thevibeworks/awesome-typesafe-jev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/thevibeworks/awesome-typesafe-jev/main/docs/media/sightmap__turbo.gif" width="100%" alt="thevibeworks/awesome-typesafe-jev animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/ussyverse/hermes-jev-router">ussyverse/hermes-jev-router</a></b> — Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [ussyverse](https://github.com/ussyverse)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API access pending.

</details>

<details>
<summary><b><a href="https://github.com/yangzhou-chaofan/awesome-jev-prompt">yangzhou-chaofan/awesome-jev-prompt</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · CC0-1.0 · [yangzhou-chaofan](https://github.com/yangzhou-chaofan)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

latest top 100 showcases for jev (keep updating) from x / github / latest sources

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yangzhou-chaofan--awesome-jev-prompt/1c01ea8fc35d81c9.webp" width="100%" alt="yangzhou-chaofan/awesome-jev-prompt screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/zbloss/jev-plays-pokemon">zbloss/jev-plays-pokemon</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · [zbloss](https://github.com/zbloss)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 3 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Like Claude Plays Pokemon, but with Jev

</details>

<details>
<summary><b><a href="https://github.com/zhangxaochen/dsh-jev">zhangxaochen/dsh-jev</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · [zhangxaochen](https://github.com/zhangxaochen)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev (System One decision model) plugin suite for DeepSeek Harness (dsh)

</details>

<details>
<summary><b><a href="https://github.com/DevMortimer/pi-warden">DevMortimer/pi-warden</a></b> — ⭐57 · TypeScript · unverified · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `unverified` · TypeScript · MIT · [DevMortimer](https://github.com/DevMortimer)

**डेटा** · स्टार **57** · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges irreversible and off-task tool calls, detects stuck loops, checks unverified done claims, flags slop

> Guardrails that steer an agent before it acts. Demonstrates the gate pattern, where the decision is cheap enough to run on every step.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devmortimer--pi-warden/b8dc20ac6694613a.png" width="100%" alt="DevMortimer/pi-warden screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/3clyp50/a0-typesafe-ai">3clyp50/a0-typesafe-ai</a></b> — ⭐4 · Python · unverified · 1 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `unverified` · Python · MIT · [3clyp50](https://github.com/3clyp50)

**डेटा** · स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/3clyp50--a0-typesafe-ai/9aa8ea4ef8241f14.png" width="100%" alt="3clyp50/a0-typesafe-ai screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/HyunjunJeon/pi-quiet-ask">HyunjunJeon/pi-quiet-ask</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `unverified` · TypeScript · MIT · [HyunjunJeon](https://github.com/HyunjunJeon)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe Jev as the pi coding agent's quiet decision layer

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hyunjunjeon--pi-quiet-ask/7ee3a99430e853d8.png" width="100%" alt="HyunjunJeon/pi-quiet-ask screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/zoidsh/tenet">zoidsh/tenet</a></b> — ⭐3 · Go · unverified · 0 天</summary>

**बुनियादी तथ्य** · `एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `unverified` · Go · MIT · [zoidsh](https://github.com/zoidsh)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 2 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

The review gate for code that agents write: rules in plain language, judged on every commit

</details>

<a id="routing-guardrails"></a>

## रूटिंग, गार्डरेल और अनुमोदन <sub>· 39</sub>

प्रोडक्शन जैसा उपयोग: हर अनुरोध उसी सबसे सस्ते मॉडल को भेजें जो उसे वास्तव में संभाल सके, और परिणाम पर एक नियतात्मक जाँच बनाए रखें।

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐41 · Rust · observed · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · Rust · NOASSERTION · [Dicklesworthstone](https://github.com/Dicklesworthstone)

**डेटा** · स्टार **41** · फ़ॉर्क 3 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐23 · Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · Python · [brainstormity](https://github.com/brainstormity)

**डेटा** · स्टार **23** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

<sub>कोड में प्रयुक्त पाया गया: `typesafe/__init__.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 1 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · Python · MIT · [Foadsf](https://github.com/Foadsf)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · TypeScript · MIT · [qddegtya](https://github.com/qddegtya)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 3 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed decisions from a System One model. An uncertain answer is a different type from a confident one — and the compiler makes you handle it.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · Python · [aniruddh-krovvidi](https://github.com/aniruddh-krovvidi)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐16 · TypeScript · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · [yusukebe](https://github.com/yusukebe)

**डेटा** · स्टार **16** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐6 · JavaScript · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · MIT · [mejiasd3v](https://github.com/mejiasd3v)

**डेटा** · स्टार **6** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · [andrelandgraf](https://github.com/andrelandgraf)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · [keeltrace](https://github.com/keeltrace)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐2 · Python · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · [maker-KK](https://github.com/maker-KK)

**डेटा** · स्टार **2** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · [WiktorB2004](https://github.com/WiktorB2004)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.

</details>

<details>
<summary><b><a href="https://github.com/jerryfane/omp-jev-compaction">jerryfane/omp-jev-compaction</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · [jerryfane](https://github.com/jerryfane)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Verbatim Jev-scored context reduction for omp, over TypeSafe or OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · [Pinutss](https://github.com/Pinutss)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐1 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · [prismhq](https://github.com/prismhq)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · [Shashank-H](https://github.com/Shashank-H)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/aaronshaf/opencode-jev-model-router">aaronshaf/opencode-jev-model-router</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · [aaronshaf](https://github.com/aaronshaf)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev-based automatic per-turn model routing for OpenCode

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Jupyter · MIT · [bitnovus](https://github.com/bitnovus)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/carllippert/jev-router">carllippert/jev-router</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · [carllippert](https://github.com/carllippert)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Express with no routes. TypeSafe Jev picks which handler runs.

</details>

<details>
<summary><b><a href="https://github.com/danfry1/jev-triage">danfry1/jev-triage</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · [danfry1](https://github.com/danfry1)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

GitHub Action that labels, deduplicates and spam-checks issues with Jev, with calibrated confidence for every decision

</details>

<details>
<summary><b><a href="https://github.com/danielhirt/jev-lab">danielhirt/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · [danielhirt](https://github.com/danielhirt)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM baseline comparison

</details>

<details>
<summary><b><a href="https://github.com/denikuchero/jev-chess-lab">denikuchero/jev-chess-lab</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · GPL-3.0 · [denikuchero](https://github.com/denikuchero)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev chess experiments: independent decisions vs tactical and Stockfish assistance, with full traces and video replays

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/denikuchero--jev-chess-lab/93f39c2d8831bde6.gif" width="100%" alt="denikuchero/jev-chess-lab screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/denikuchero--jev-chess-lab/5b385b4d2de02637.gif" width="100%" alt="denikuchero/jev-chess-lab animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/denikuchero/jev-chess-lab/main/docs/games/01-raw/replay.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/gnoviawan/omp-jev-tools">gnoviawan/omp-jev-tools</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · NOASSERTION · [gnoviawan](https://github.com/gnoviawan)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation verification

</details>

<details>
<summary><b><a href="https://github.com/hugo-alves/jev-router-playground">hugo-alves/jev-router-playground</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · MIT · [hugo-alves](https://github.com/hugo-alves)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Interactive playground for testing Jev model-routing decisions against OpenRouter models

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hugo-alves--jev-router-playground/93692a5f183f12e1.jpg" width="100%" alt="hugo-alves/jev-router-playground screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/iefnaf/pi-jev">iefnaf/pi-jev</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · [iefnaf](https://github.com/iefnaf)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Pi extension suite powered by Jev: selective context compaction and model routing

</details>

<details>
<summary><b><a href="https://github.com/jcpsimmons/jev-macos-loop">jcpsimmons/jev-macos-loop</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · AGPL-3.0 · [jcpsimmons](https://github.com/jcpsimmons)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Native macOS computer-use loop: OmniParser CoreML, Apple Vision OCR, accessibility labels, and Jev decisions through Vercel AI Gateway.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jcpsimmons--jev-macos-loop/b368b1d9b147950e.png" width="100%" alt="jcpsimmons/jev-macos-loop screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/juanegido/jev-pr-judge">juanegido/jev-pr-judge</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · [juanegido](https://github.com/juanegido)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed verdicts on pull requests with TypeSafe System One (Jev): one parallel call, policy in code, usable as a GitHub Action

</details>

<details>
<summary><b><a href="https://github.com/kenhuangus/jev-usecases">kenhuangus/jev-usecases</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · [kenhuangus](https://github.com/kenhuangus)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Production TypeSafe Jev (System One) use-case harnesses with confidence-gated decision logic

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kenhuangus--jev-usecases/be919255190f6495.png" width="100%" alt="kenhuangus/jev-usecases screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-bot">kevin9327/jev-bot</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · [kevin9327](https://github.com/kevin9327)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-code">kevin9327/jev-code</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · [kevin9327](https://github.com/kevin9327)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

JevCode: TypeSafe Jev diff merge gate. merge / comment / block in code.

</details>

<details>
<summary><b><a href="https://github.com/maraichr/jev-triage">maraichr/jev-triage</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · MIT · [maraichr](https://github.com/maraichr)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Cross-border B2B case triage prototype using TypeSafe Jev via OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/MoonTory/pi-jev-harness">MoonTory/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · [MoonTory](https://github.com/MoonTory)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards tool calls

</details>

<details>
<summary><b><a href="https://github.com/nitinnat/jev-gateway">nitinnat/jev-gateway</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · MIT · [nitinnat](https://github.com/nitinnat)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A small local HTTP service for TypeSafe AI's Jev through Vercel

</details>

<details>
<summary><b><a href="https://github.com/SadiqOnGithub/jev-lab">SadiqOnGithub/jev-lab</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · [SadiqOnGithub](https://github.com/SadiqOnGithub)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Live tests for TypeSafe Jev (System One) via OpenRouter's Decisions API

</details>

<details>
<summary><b><a href="https://github.com/stbenjam/jev-eight-ball">stbenjam/jev-eight-ball</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · [stbenjam](https://github.com/stbenjam)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A liquid magic eight ball powered by TypeSafe Jev decisions through OpenRouter

</details>

<details>
<summary><b><a href="https://github.com/TokenTrim/jev-routing-experiment">TokenTrim/jev-routing-experiment</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · Apache-2.0 · [TokenTrim](https://github.com/TokenTrim)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Benchmarking TypeSafe's Jev decision model as a cost-efficient LLM router on RouterArena

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tokentrim--jev-routing-experiment/1c31bd606ebc1994.png" width="100%" alt="TokenTrim/jev-routing-experiment screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wadadanet/faq-jev-router">wadadanet/faq-jev-router</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · MIT · [wadadanet](https://github.com/wadadanet)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Cascade FAQ routing with TypeSafe Jev — category → FAQ or not found (GitHub Pages demo)

</details>

<details>
<summary><b><a href="https://github.com/Xy2002/poker-jev-test-bench">Xy2002/poker-jev-test-bench</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · MIT · [Xy2002](https://github.com/Xy2002)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev test bench — Texas Hold'em edition: live-fire testing of TypeSafe's Jev evaluation model through a React poker game (Vercel AI Gateway). MIT.

</details>

<details>
<summary><b><a href="https://github.com/iammrduncan/typesafe-ai-benchmark">iammrduncan/typesafe-ai-benchmark</a></b> — ⭐30 · TypeScript · unverified · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `unverified` · TypeScript · MIT · [iammrduncan](https://github.com/iammrduncan)

**डेटा** · स्टार **30** · फ़ॉर्क 5 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.

> A gateway that mimics the System One interface, which is what makes side-by-side benchmarking possible without rewriting the caller.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/iammrduncan--typesafe-ai-benchmark/3d66c620e48ff597.gif" width="100%" alt="iammrduncan/typesafe-ai-benchmark animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/iammrduncan/typesafe-ai-benchmark/main/docs/media/theater-demo.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/raihankhan-rk/diffjury">raihankhan-rk/diffjury</a></b> — ⭐3 · TypeScript · unverified · 0 天</summary>

**बुनियादी तथ्य** · `रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `unverified` · TypeScript · [raihankhan-rk](https://github.com/raihankhan-rk)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

DiffJury — TypeSafe Jev PR risk router + code review coach

</details>

<a id="evaluation"></a>

## मूल्यांकन, कैलिब्रेशन और बेंचमार्क <sub>· 30</sub>

किसी को कैसे पता चले कि निर्णय अच्छे हैं। कैलिब्रेशन इस पारिस्थितिकी में खुला प्रश्न है, और ये परियोजनाएँ उसे मापती हैं।

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · Go · MIT · [Gaurav-Gosain](https://github.com/Gaurav-Gosain)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · Python · [akash-kamat](https://github.com/akash-kamat)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · Python · Apache-2.0 · [hev](https://github.com/hev)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/JoshuaSP/open-jev">JoshuaSP/open-jev</a></b> — ⭐14 · Python · inferred · 1 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · [JoshuaSP](https://github.com/JoshuaSP)

**डेटा** · स्टार **14** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed JSON inference with DiffusionGemma, with Every and Jev benchmark results

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/joshuasp--open-jev/1d4a9f6368358e43.png" width="100%" alt="JoshuaSP/open-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rorshopping/jev-on-a-laptop">rorshopping/jev-on-a-laptop</a></b> — ⭐14 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · NOASSERTION · [rorshopping](https://github.com/rorshopping)

**डेटा** · स्टार **14** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Unofficial study: Jev-style parallel typed decisions on stock 1.5B-8B models on an Apple Silicon laptop. Benchmarks, research notes, and a Hugging Face Space demo.

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐6 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · Apache-2.0 · [AbdelStark](https://github.com/AbdelStark)

**डेटा** · स्टार **6** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐4 · TypeScript · inferred · 2 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · TypeScript · MIT · [y0usaf](https://github.com/y0usaf)

**डेटा** · स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · NOASSERTION · [Heman10x-NGU](https://github.com/Heman10x-NGU)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐2 · Python · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · Apache-2.0 · [ikermoel](https://github.com/ikermoel)

**डेटा** · स्टार **2** (+1) · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Open alternative to Jev: typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with benchmarks

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · [wondertwins](https://github.com/wondertwins)

**डेटा** · स्टार **2** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · [4esv](https://github.com/4esv)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-eval/main/results/coverage.png" width="100%" alt="4esv/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/aieo-product/jev-gamebenchmark">aieo-product/jev-gamebenchmark</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · [aieo-product](https://github.com/aieo-product)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Sandbox & benchmark: optimize how you ask Jev (TypeSafe System One) to play falling-block puzzle games, head-to-head against LLMs

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · TypeScript · MIT · [Danu28](https://github.com/Danu28)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · TeX · NOASSERTION · [dnakhoa](https://github.com/dnakhoa)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · [eggmasonvalue](https://github.com/eggmasonvalue)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · [jujumilk3](https://github.com/jujumilk3)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · JavaScript · MIT · [KantaHayashiAI](https://github.com/KantaHayashiAI)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/misaalya/snbt-jev-bench">misaalya/snbt-jev-bench</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · [misaalya](https://github.com/misaalya)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev on Indonesia's SNBT 2025 university entrance test: 159 questions, seven subtests, audited answer keys.

</details>

<details>
<summary><b><a href="https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and">musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and</a></b> — HTML · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · HTML · MIT · [musman550](https://github.com/musman550)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
<td align="center" valign="top"><a href="https://www.youtube.com/@automatewithmusfiraai"><img src="" width="100%" alt="video"></a><br><sub><a href="https://www.youtube.com/@automatewithmusfiraai">यहाँ देखें youtube.com</a> · प्लेबैक होस्ट साइट पर खुलता है; GitHub इसे इनलाइन एम्बेड नहीं कर सकता</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/onlyoneaman/jev-eval">onlyoneaman/jev-eval</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · TypeScript · MIT · [onlyoneaman](https://github.com/onlyoneaman)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe's Jev vs gpt-5.4-mini and gpt-5.6-luna on four public classification sets: cases, per-item answers, scoring, charts

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/onlyoneaman--jev-eval/e5d471e96e134f81.png" width="100%" alt="onlyoneaman/jev-eval screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/robipop22/Jev-is-odd">robipop22/Jev-is-odd</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · JavaScript · MIT · [robipop22](https://github.com/robipop22)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Ask Jev by TypeSafe AI whether a number is odd. TypeScript, real token usage, and latency benchmarks.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/robipop22--jev-is-odd/5c4ddde817bd6cdc.png" width="100%" alt="robipop22/Jev-is-odd screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/rongxinzy/LightJev">rongxinzy/LightJev</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · Apache-2.0 · [rongxinzy](https://github.com/rongxinzy)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Train lightweight language backbones for typed decisions and candidate probabilities. CE/Brier training, evaluation, and an offline end-to-end demo.

</details>

<details>
<summary><b><a href="https://github.com/shunta-furukawa/jev-tick-lab">shunta-furukawa/jev-tick-lab</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · [shunta-furukawa](https://github.com/shunta-furukawa)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged for calibration analysis.

</details>

<details>
<summary><b><a href="https://github.com/teyhouse/jev-secret-detection">teyhouse/jev-secret-detection</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · [teyhouse](https://github.com/teyhouse)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Measures how well TypeSafe's RLCD-Jev model spots real secret credentials in file snippets

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/teyhouse/jev-secret-detection/main/assets/screenshot.png" width="100%" alt="teyhouse/jev-secret-detection screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/uspraveen/Jev-Reranker">uspraveen/Jev-Reranker</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · MIT · [uspraveen](https://github.com/uspraveen)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A System-1 model based memory retrieval reranked using caliberated decision space instead of embeddings

</details>

<details>
<summary><b><a href="https://github.com/zhuyansen/jev-support-pulse">zhuyansen/jev-support-pulse</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · [zhuyansen](https://github.com/zhuyansen)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Does a Jev-labelled support-tweet stream spike before a brand admits an outage? At equal false alarms it catches 17 vs 10 incidents (volume), ~4h ahead; a good keyword list is almost as good.

</details>

<details>
<summary><b><a href="https://github.com/Mapika/decider">Mapika/decider</a></b> — ⭐13 · Python · unverified · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `unverified` · Python · [Mapika](https://github.com/Mapika)

**डेटा** · स्टार **13** (+1) · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Mapika/decider/main/media/montage.gif" width="100%" alt="Mapika/decider animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/genai-craft/openvons">genai-craft/openvons</a></b> — ⭐7 · Python · unverified · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `unverified` · Python · NOASSERTION · [genai-craft](https://github.com/genai-craft)

**डेटा** · स्टार **7** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド

</details>

<details>
<summary><b><a href="https://github.com/aabolfazl/typesafe-local">aabolfazl/typesafe-local</a></b> — ⭐4 · Python · unverified · 0 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `unverified` · Python · MIT · [aabolfazl](https://github.com/aabolfazl)

**डेटा** · स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text. Structured output without generation or parsing. MLX / Apple Silicon.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/aabolfazl--typesafe-local/ada59cf382af5143.png" width="100%" alt="aabolfazl/typesafe-local screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mithalouni/system-one-open">mithalouni/system-one-open</a></b> — ⭐4 · Python · unverified · 1 天</summary>

**बुनियादी तथ्य** · `मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `unverified` · Python · NOASSERTION · [mithalouni](https://github.com/mithalouni)

**डेटा** · स्टार **4** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Open replica of TypeSafe's Jev: typed calibrated decisions in one forward pass, on Gemma 4 E2B / Gemma 3 270M (Modal)

</details>

<a id="research-models"></a>

## खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध <sub>· 13</sub>

खुले वेट, छोटी प्रतिकृतियाँ और आर्किटेक्चर पर काम। इनमें से कई इसलिए हैं क्योंकि कैलिब्रेशन व्यवहार केवल सार्वजनिक सामग्री से पुनरुत्पादित नहीं होता।

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐48 · Python · observed · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `observed` · Python · MIT · [kshetrajna12](https://github.com/kshetrajna12)

**डेटा** · स्टार **48** (+1) · फ़ॉर्क 3 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐238 · Python · inferred · 0 天 · ⭐+14</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · [TianyuCodings](https://github.com/TianyuCodings)

**डेटा** · स्टार **238** (+14) · फ़ॉर्क 21 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/5055af419619e7e4.gif" width="100%" alt="TianyuCodings/NanoJev animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/assets/side_by_side_maze.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐14 · Python · inferred · 0 天 · ⭐+2</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · [r-ms](https://github.com/r-ms)

**डेटा** · स्टार **14** (+2) · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `observed`

**डेटा** · डाउनलोड 25 · लाइक 1 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 0 天</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `observed`

**डेटा** · डाउनलोड 0 · लाइक 0 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐115 · Python · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · [ekzhang](https://github.com/ekzhang)

**डेटा** · स्टार **115** (+1) · फ़ॉर्क 10 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐19 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · [bnsd55](https://github.com/bnsd55)

**डेटा** · स्टार **19** · फ़ॉर्क 3 · खुले इश्यू 4 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/siliconkernel/vllm-jev-decison">siliconkernel/vllm-jev-decison</a></b> — ⭐6 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · [siliconkernel](https://github.com/siliconkernel)

**डेटा** · स्टार **6** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Classification-only typed decisions for vLLM: finite-schema candidate scoring, probabilities, and abstention. No generative fallback.

</details>

<details>
<summary><b><a href="https://github.com/chahero/tetris-jev">chahero/tetris-jev</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · [chahero](https://github.com/chahero)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Watch TypeSafe Jev play Tetris. Live API vs offline heuristic, with recorded demos and reproducible runs.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/chahero/tetris-jev/main/media/jev-preview.gif" width="100%" alt="chahero/tetris-jev screenshot"></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/chahero/tetris-jev/main/media/jev.mp4"><img src="https://raw.githubusercontent.com/chahero/tetris-jev/main/media/jev-preview.gif" width="100%" alt="chahero/tetris-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/chahero/tetris-jev/main/media/jev.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/integrate-your-mind/jev-nethack">integrate-your-mind/jev-nethack</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · [integrate-your-mind](https://github.com/integrate-your-mind)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev x NetHack: bounded runner, research code, and completed recording releases

</details>

<details>
<summary><b><a href="https://github.com/legacybridge-tech/pi-typesafe-jev">legacybridge-tech/pi-typesafe-jev</a></b> — TypeScript · inferred · 1 天</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · TypeScript · NOASSERTION · [legacybridge-tech](https://github.com/legacybridge-tech)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A pi extension that exposes TypeSafe (Jev, System One) judgments as five pi tools, so a model can make narrow semantic judgments while your code and your users keep control of thresholds, weights, and actions.

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · [shellneko](https://github.com/shellneko)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐5 · Python · unverified · 1 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `unverified` · Python · NOASSERTION · [zhihz](https://github.com/zhihz)

**डेटा** · स्टार **5** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<a id="apps-demos"></a>

## अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो <sub>· 37</sub>

गेम, रोबोट, ब्राउज़र और डैशबोर्ड। डेमो ही वह तरीका हैं जिनसे विलंबता और लागत के दावे पढ़ने योग्य बनते हैं।

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐7 · Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · Python · Apache-2.0 · [zadescoxp](https://github.com/zadescoxp)

**डेटा** · स्टार **7** · फ़ॉर्क 1 · खुले इश्यू 3 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · TypeScript · [daftAI2026](https://github.com/daftAI2026)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · Rust · MIT · [markjaquith](https://github.com/markjaquith)

**डेटा** · स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · TypeScript · [adiun](https://github.com/adiun)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 1 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · Dart · [Bud-ro](https://github.com/Bud-ro)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/sandra-arato/icon-matcher">sandra-arato/icon-matcher</a></b> — TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · TypeScript · MIT · [sandra-arato](https://github.com/sandra-arato)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Match a UI section title to a Hugeicons icon using TypeSafe.ai's Choice primitive — no lexical/keyword search.

</details>

<details>
<summary><b><a href="https://github.com/sandra-arato/icon-matcher-ui">sandra-arato/icon-matcher-ui</a></b> — TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · TypeScript · MIT · [sandra-arato](https://github.com/sandra-arato)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Browser-only UI for icon-matcher — paste a TypeSafe.ai key, match a UI title to an icon live, no backend.

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · Python · MIT · [tirukovelamanoj](https://github.com/tirukovelamanoj)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/8c1b0d55baf76296.gif" width="100%" alt="tirukovelamanoj/jev-plays-doom animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/tirukovelamanoj/jev-plays-doom/main/docs/jev-doom.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · TypeScript · [wustep](https://github.com/wustep)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://x.com/tspy/status/2100864234523685146">X intent labeller</a></b> — @tspy · observed · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · [yishan](https://x.com/tspy) · @tspy · x.com

**डेटा** · व्यूज़ 2364 · लाइक 15 · टिप्पणियाँ 9 · पोस्ट किया गया 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A Chrome extension that labels posts in an X timeline with their intent and probability as you scroll, drawn as a tag directly after each post's timestamp. Categories include inducement, provocation, promotion, machine-generated, persuasion, entertainment and information. A side panel reports session counts (seen, judged, correct) and cumulative token cost. The author reports near-instant responses and usable accuracy before any tuning.

<sub>मूल प्रोजेक्ट का लिंक खोजा जा रहा है।</sub>

> Worth reading as a latency argument rather than an accuracy one: labelling a timeline only works if the decision costs less than the scroll, which is the constraint a generative model cannot meet.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/0641644f12a25a45.jpg" width="100%" alt="X intent labeller screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/b80cf3173f63bdd7.gif" width="100%" alt="X intent labeller animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://video.twimg.com/amplify_video/2100858340331200512/vid/avc1/1242x720/ex2FF5-TerVxo9xX.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐89 · Python · inferred · 0 天 · ⭐+2</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Python · MIT · [hr98w](https://github.com/hr98w)

**डेटा** · स्टार **89** (+2) · फ़ॉर्क 9 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐60 · TypeScript · inferred · 0 天 · ⭐+2</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · MIT · [jkudish](https://github.com/jkudish)

**डेटा** · स्टार **60** (+2) · फ़ॉर्क 3 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/b4ae7fc04353e74c.gif" width="100%" alt="jkudish/jev-browser animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐23 · JavaScript · inferred · 0 天 · ⭐+5</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · MIT · [moritzkremb](https://github.com/moritzkremb)

**डेटा** · स्टार **23** (+5) · फ़ॉर्क 3 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/mizchi/jev-playground">mizchi/jev-playground</a></b> — ⭐13 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · [mizchi](https://github.com/mizchi)

**डेटा** · स्टार **13** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mizchi/jev-playground/main/gomoku.gif" width="100%" alt="mizchi/jev-playground animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/shantanugoel/mario-jev">shantanugoel/mario-jev</a></b> — ⭐10 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Python · [shantanugoel](https://github.com/shantanugoel)

**डेटा** · स्टार **10** · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · [emrickgarrett](https://github.com/emrickgarrett)

**डेटा** · स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐4 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Python · MIT · [komorra](https://github.com/komorra)

**डेटा** · स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/arielweinberger/jev-autopilot">arielweinberger/jev-autopilot</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · [arielweinberger](https://github.com/arielweinberger)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

This demo uses Jev from TypeSafe AI to autonomously fly a drone in a random city from point A to point B, avoiding obstacles along the way. A trip costs $0.01.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/arielweinberger/jev-autopilot/main/docs/demo.png" width="100%" alt="arielweinberger/jev-autopilot screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐3 · JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · [vinilana](https://github.com/vinilana)

**डेटा** · स्टार **3** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Go · MIT · [paulsmith](https://github.com/paulsmith)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/reachjalil/jev-tree">reachjalil/jev-tree</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · MIT · [reachjalil](https://github.com/reachjalil)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Recursive Jev choice over a taxonomy. Select from more than 255 options without breaking TypeSafe Jev's choice cap.

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · MIT · [vmendes90](https://github.com/vmendes90)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · [Little-Planet-Labs](https://github.com/Little-Planet-Labs)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/phureewat29/got-jev">phureewat29/got-jev</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · [phureewat29](https://github.com/phureewat29)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev (TypeSafe AI) PoC through Game of Thrones

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Python · [PistachioAIHQ](https://github.com/PistachioAIHQ)

**डेटा** · स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/bahramzada/jev-taxi-dispatch">bahramzada/jev-taxi-dispatch</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · MIT · [bahramzada](https://github.com/bahramzada)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Real-vaxt taksi dispetçerlik simulyasiyası — TypeSafe JEV (System One) modeli ilə

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/bahramzada--jev-taxi-dispatch/e616f4168b15d3f2.png" width="100%" alt="bahramzada/jev-taxi-dispatch screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/BrendanH18/jev-lab">BrendanH18/jev-lab</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Python · MIT · [BrendanH18](https://github.com/BrendanH18)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Six small apps and a workbench that show what TypeSafe's Jev (System One) model can do

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/brendanh18--jev-lab/b16b9535e3744cd3.png" width="100%" alt="BrendanH18/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hxutixnnn/ui-jev">hxutixnnn/ui-jev</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · Apache-2.0 · [hxutixnnn](https://github.com/hxutixnnn)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/jflam/jev1">jflam/jev1</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · [jflam](https://github.com/jflam)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev (TypeSafe System One) proof of concept: smart-home assistant demo

</details>

<details>
<summary><b><a href="https://github.com/legostin/jev-browser">legostin/jev-browser</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · [legostin](https://github.com/legostin)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/pistachiopranay/jev-synergy-screening">pistachiopranay/jev-synergy-screening</a></b> — inferred · 1 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · [pistachiopranay](https://github.com/pistachiopranay)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/rchovatiya88/cyber-breach-jev">rchovatiya88/cyber-breach-jev</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · [rchovatiya88](https://github.com/rchovatiya88)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One decision model

</details>

<details>
<summary><b><a href="https://github.com/sightmap/jev-turbo">sightmap/jev-turbo</a></b> — Go · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Go · MIT · [sightmap](https://github.com/sightmap)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev-powered semantic browser use

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/sightmap--jev-turbo/80ba196d00024a03.gif" width="100%" alt="sightmap/jev-turbo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/sightmap--jev-turbo/ad7a1ccc23e034dc.gif" width="100%" alt="sightmap/jev-turbo animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/sightmap/jev-turbo/main/docs/demo.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Spykoninho/trading-bot-jev">Spykoninho/trading-bot-jev</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · [Spykoninho](https://github.com/Spykoninho)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Crypto trading bot on Binance testnet using TypeSafe (Jev) to judge news

</details>

<details>
<summary><b><a href="https://github.com/Tatuck/jev-boe-demo">Tatuck/jev-boe-demo</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · [Tatuck](https://github.com/Tatuck)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Daily demo applying TypeSafe's Jev model to Spain's official gazette (BOE).

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Tatuck/jev-boe-demo/main/docs/demo-pipeline.gif" width="100%" alt="Tatuck/jev-boe-demo screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Tatuck/jev-boe-demo/main/docs/demo-web.gif" width="100%" alt="Tatuck/jev-boe-demo animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/YYK2007/jev-flappy">YYK2007/jev-flappy</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · [YYK2007](https://github.com/YYK2007)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev makes every flap-or-coast decision in a live game, exposing probabilities, latency, tokens, and cost.

</details>

<details>
<summary><b><a href="https://github.com/sorrycc/typesafe-snake">sorrycc/typesafe-snake</a></b> — ⭐17 · TypeScript · unverified · 1 天</summary>

**बुनियादी तथ्य** · `अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `unverified` · TypeScript · [sorrycc](https://github.com/sorrycc)

**डेटा** · स्टार **17** · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Snake auto-played by TypeSafe's Jev model: one System One choice per tick, legal moves and facts generated in code

</details>

<a id="media-discussions"></a>

## लेखन, चर्चाएँ और समान सूचियाँ <sub>· 103</sub>

लॉन्च थ्रेड, स्वतंत्र लेख और इस क्षेत्र की अन्य क्यूरेटेड सूचियाँ। यह रिपॉज़िटरी अकेली नहीं है, और यह कहना अन्यथा दिखाने से अधिक उपयोगी है।

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐4374 · Python · observed · 0 天 · ⭐+115</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · MIT · [browser-use](https://github.com/browser-use)

**डेटा** · स्टार **4374** (+115) · फ़ॉर्क 260 · खुले इश्यू 28 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

i. am. speed.

<sub>कोड में प्रयुक्त पाया गया: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/d3c9791c1ce6e146.gif" width="100%" alt="browser-use/jev-ultrafast animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/demo.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1878 · observed · 2 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 1878 · टिप्पणियाँ 492 · अंतिम पुश 2026-09-15 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐470 · Python · observed · 0 天 · ⭐+5</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · MIT · [Anil-matcha](https://github.com/Anil-matcha)

**डेटा** · स्टार **470** (+5) · फ़ॉर्क 92 · खुले इश्यू 7 · बनाया गया 2023-05-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>कोड में प्रयुक्त पाया गया: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/anil-matcha--awesome-jev-by-typesafe/54dbd5521bc42664.jpg" width="100%" alt="Anil-matcha/awesome-jev-by-typesafe screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐177 · CSS · observed · 0 天 · ⭐+10</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · CSS · MIT · [AbdelStark](https://github.com/AbdelStark)

**डेटा** · स्टार **177** (+10) · फ़ॉर्क 22 · खुले इश्यू 2 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>कोड में प्रयुक्त पाया गया: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐119 · TypeScript · observed · 0 天 · ⭐+3</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · TypeScript · [dabit3](https://github.com/dabit3)

**डेटा** · स्टार **119** (+3) · फ़ॉर्क 11 · खुले इश्यू 15 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

<sub>कोड में प्रयुक्त पाया गया: `jev-lint/proxy.mjs`, `jev-tower/jev-proxy.mjs`, `jev-instant-search/bench/dump.ts`, `jev-swarm/jev-proxy.mjs`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐98 · Python · observed · 0 天 · ⭐+3</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · [yibie](https://github.com/yibie)

**डेटा** · स्टार **98** (+3) · फ़ॉर्क 8 · खुले इश्यू 7 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐53 · observed · 0 天 · ⭐+5</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · CC0-1.0 · [cobanov](https://github.com/cobanov)

**डेटा** · स्टार **53** (+5) · फ़ॉर्क 3 · खुले इश्यू 2 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐48 · observed · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · CC0-1.0 · [AnotiaWang](https://github.com/AnotiaWang)

**डेटा** · स्टार **48** (+1) · फ़ॉर्क 13 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>कोड में प्रयुक्त पाया गया: `README.md`, `README_zh.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐40 · observed · 1 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 40 · टिप्पणियाँ 9 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐26 · HTML · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · HTML · CC0-1.0 · [hellogumbo](https://github.com/hellogumbo)

**डेटा** · स्टार **26** · फ़ॉर्क 1 · खुले इश्यू 4 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A community directory of projects built on Jev, TypeSafe AI's System One model.

<sub>कोड में प्रयुक्त पाया गया: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 2 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 5 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-15 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 4 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49754461">Most People on the Internet Miss What Jev Is About</a></b> — ⭐4 · observed · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 4 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49754516">Show HN: Jev vs. GPT-5.6 and Claude Haiku at Pong</a></b> — ⭐4 · observed · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 4 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 4 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 3 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐3 · Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · NOASSERTION · [OmniJev](https://github.com/OmniJev)

**डेटा** · स्टार **3** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Papers, open reproductions and independent evaluations behind System One models and Jev.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/OmniJev/awesome-jev/main/assets/cover.png" width="100%" alt="OmniJev/awesome-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 3 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=48437732">Using Jai&#x27;s Unique and Powerful Compiler for Typesafe Units</a></b> — ⭐3 · observed · 102 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 3 · टिप्पणियाँ 0 · अंतिम पुश 2026-06-07 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49752765">Ask HN: Is Jev the New Claw?</a></b> — ⭐2 · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 2 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Is it my skill&#x2F;smartness issue that I still struggle to see what Jev exactly is and what differentiates it?

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · JavaScript · CC0-1.0 · [hellogumbo](https://github.com/hellogumbo)

**डेटा** · स्टार **2** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49744527">Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)</a></b> — ⭐2 · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 2 · टिप्पणियाँ 1 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Full disclosure, it was coded with AI, I don&#x27;t claim otherwise. But I wanted to test out tool calls and iterative problem solving using Jev and needed a simple library&#x2F;framework&#x2F;harness to do that.
SOKIT (System One Knowledge, Instructions and Tools) is the result

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=48435180">Show HN: Vithos – typesafe full-stack template for Cloudflare Workers</a></b> — ⭐2 · observed · 102 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 2 · टिप्पणियाँ 1 · अंतिम पुश 2026-06-07 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49729945">The first (public) System One Model; Jev gives AI the properties of code</a></b> — ⭐2 · observed · 1 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 2 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49745212">Typesafe&#x27;s Jev is the fish at the poker table</a></b> — ⭐2 · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 2 · टिप्पणियाँ 1 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49733647">Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step</a></b> — ⭐2 · observed · 1 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 2 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49734345">Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD</a></b> — ⭐2 · observed · 1 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

**डेटा** · अंक 2 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐1 · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · NOASSERTION · [aliaihub](https://github.com/aliaihub)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://github.com/ozers/jevsome-projects">ozers/jevsome-projects</a></b> — ⭐1 · JavaScript · observed · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · JavaScript · MIT · [ozers](https://github.com/ozers)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Open-source projects that provably call Jev, TypeSafe AI's System One model. Every entry links to the line of code that proves it. Refreshed daily.

</details>

<details>
<summary><b><a href="https://github.com/rhc98/awesome-jev">rhc98/awesome-jev</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · TypeScript · NOASSERTION · [rhc98](https://github.com/rhc98)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Projects built on Jev (TypeSafe AI's System One model), curated by Jev itself.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/rhc98/awesome-jev/main/docs/diagrams/pipeline.png" width="100%" alt="rhc98/awesome-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/alpibrusl/lex-judge">alpibrusl/lex-judge</a></b> — Lex · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Lex · [alpibrusl](https://github.com/alpibrusl)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed judgments from a System One model, as a [net]-only Lex effect

</details>

<details>
<summary><b><a href="https://github.com/deepanwadhwa/OpenDecision">deepanwadhwa/OpenDecision</a></b> — Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · Apache-2.0 · [deepanwadhwa](https://github.com/deepanwadhwa)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Open Type Safe System one model system

</details>

<details>
<summary><b><a href="https://github.com/gzd2032/typesafe-ai-test">gzd2032/typesafe-ai-test</a></b> — observed · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · [gzd2032](https://github.com/gzd2032)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

a test repo for typesafe.ai

</details>

<details>
<summary><b><a href="https://github.com/hide-G/magi-system-on-jev">hide-G/magi-system-on-jev</a></b> — JavaScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · JavaScript · [hide-G](https://github.com/hide-G)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI's System One model. 3 sages deliberate your question.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/hide-G/magi-system-on-jev/master/public/ogp.png" width="100%" alt="hide-G/magi-system-on-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/JohnDotOwl/awesome-jev">JohnDotOwl/awesome-jev</a></b> — JavaScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · JavaScript · CC0-1.0 · [JohnDotOwl](https://github.com/JohnDotOwl)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A curated list of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/piyush97/focus-tube">piyush97/focus-tube</a></b> — JavaScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · JavaScript · MIT · [piyush97](https://github.com/piyush97)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Distraction-free YouTube learning feed powered by TypeSafe AI's Jev System One model

</details>

<details>
<summary><b><a href="https://github.com/soderlind/ai-provider-for-jev">soderlind/ai-provider-for-jev</a></b> — PHP · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · PHP · [soderlind](https://github.com/soderlind)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Connect WordPress to TypeSafe's Jev System One model for structured decisions (choice, score, noul).

</details>

<details>
<summary><b><a href="https://github.com/TheGali/terrarium">TheGali/terrarium</a></b> — JavaScript · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · JavaScript · MIT · [TheGali](https://github.com/TheGali)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.

</details>

<details>
<summary><b><a href="https://github.com/youngsemicolon/jev-lego">youngsemicolon/jev-lego</a></b> — Python · observed · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · [youngsemicolon](https://github.com/youngsemicolon)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A System One model builds Lego in 3D — code enumerates legal placements, Jev picks among them

</details>

<details>
<summary><b><a href="https://github.com/jarrodwatts/jev-trader">jarrodwatts/jev-trader</a></b> — ⭐745 · TypeScript · inferred · 1 天 · ⭐+10</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [jarrodwatts](https://github.com/jarrodwatts)

**डेटा** · स्टार **745** (+10) · फ़ॉर्क 146 · खुले इश्यू 2 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

One AI trade decision every Monad block. Jev on Kuru MON-USDC.

</details>

<details>
<summary><b><a href="https://github.com/droidrun/mobile-jev">droidrun/mobile-jev</a></b> — ⭐82 · JavaScript · inferred · 1 天 · ⭐+3</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · JavaScript · MIT · [droidrun](https://github.com/droidrun)

**डेटा** · स्टार **82** (+3) · फ़ॉर्क 16 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/superagents-lab/jev-search">superagents-lab/jev-search</a></b> — ⭐27 · TypeScript · inferred · 0 天 · ⭐+4</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [superagents-lab](https://github.com/superagents-lab)

**डेटा** · स्टार **27** (+4) · फ़ॉर्क 5 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Search the web with TypeSafe's Jev: source selection, query understanding and relevance ranking. Built with Search1API.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/superagents-lab--jev-search/5a545ddfd6a52aed.png" width="100%" alt="superagents-lab/jev-search screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daseinlabs/open-jev">daseinlabs/open-jev</a></b> — ⭐25 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · [daseinlabs](https://github.com/daseinlabs)

**डेटा** · स्टार **25** · फ़ॉर्क 4 · खुले इश्यू 4 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov"><img src="" width="100%" alt="daseinlabs/open-jev video"></a><br><sub><a href="https://raw.githubusercontent.com/daseinlabs/open-jev/main/docs/media/doom-recording.mov">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/IAmUnbounded/save-token-jev-clean">IAmUnbounded/save-token-jev-clean</a></b> — ⭐24 · TypeScript · inferred · 0 天 · ⭐-1</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [IAmUnbounded](https://github.com/IAmUnbounded)

**डेटा** · स्टार **24** (-1) · फ़ॉर्क 6 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/mrnugget/jev-shell-history">mrnugget/jev-shell-history</a></b> — ⭐24 · TypeScript · inferred · 0 天 · ⭐+5</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · [mrnugget](https://github.com/mrnugget)

**डेटा** · स्टार **24** (+5) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Fish-style zsh history autosuggestions ranked by Jev (TypeSafe)

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/mrnugget/jev-shell-history/main/demo/demo.gif" width="100%" alt="mrnugget/jev-shell-history animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/Dennan1221/repo-jev1iewp">Dennan1221/repo-jev1iewp</a></b> — ⭐9 · inferred · 585 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [Dennan1221](https://github.com/Dennan1221)

**डेटा** · स्टार **9** · फ़ॉर्क 0 · खुले इश्यू 20 · बनाया गया 2025-02-10 · अंतिम पुश 2025-02-10 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Авто-генерация repo-jev1iewp

</details>

<details>
<summary><b><a href="https://github.com/jon-devlapaz/jev-me">jon-devlapaz/jev-me</a></b> — ⭐9 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · MIT · [jon-devlapaz](https://github.com/jon-devlapaz)

**डेटा** · स्टार **9** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

jev-me is grill-me with jev

</details>

<details>
<summary><b><a href="https://github.com/Kevthetech143/super-jev">Kevthetech143/super-jev</a></b> — ⭐5 · TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [Kevthetech143](https://github.com/Kevthetech143)

**डेटा** · स्टार **5** · फ़ॉर्क 1 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A small, extensible decision-to-action harness for TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/hqman/JevScout">hqman/JevScout</a></b> — ⭐4 · Python · inferred · 0 天 · ⭐+3</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · [hqman](https://github.com/hqman)

**डेटा** · स्टार **4** (+3) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4"><img src="" width="100%" alt="hqman/JevScout video"></a><br><sub><a href="https://raw.githubusercontent.com/hqman/JevScout/main/assets/jev_job.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/mateonunez/jod">mateonunez/jod</a></b> — ⭐3 · TypeScript · inferred · 1 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [mateonunez](https://github.com/mateonunez)

**डेटा** · स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Semantic schemas over TypeSafe's Jev — validate the state locally, then project typed answers.

</details>

<details>
<summary><b><a href="https://github.com/andrueandersoncs/jev-semantic-linter">andrueandersoncs/jev-semantic-linter</a></b> — ⭐2 · TypeScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · [andrueandersoncs](https://github.com/andrueandersoncs)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/haseeb-heaven/jev-system-one">haseeb-heaven/jev-system-one</a></b> — ⭐2 · Python · inferred · 1 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · MIT · [haseeb-heaven](https://github.com/haseeb-heaven)

**डेटा** · स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/haseeb-heaven--jev-system-one/e41c848323b1077a.png" width="100%" alt="haseeb-heaven/jev-system-one screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/joelhooks/pi-fast-jev-compaction">joelhooks/pi-fast-jev-compaction</a></b> — ⭐2 · TypeScript · inferred · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [joelhooks](https://github.com/joelhooks)

**डेटा** · स्टार **2** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Pi extension: verbatim context compaction with TypeSafe Jev decisions

</details>

<details>
<summary><b><a href="https://github.com/justinhe16/trade-jev">justinhe16/trade-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · MIT · [justinhe16](https://github.com/justinhe16)

**डेटा** · स्टार **2** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Backtest Jev (TypeSafe) as a BUY/SELL/HOLD trader on NQ L10 order-book data

</details>

<details>
<summary><b><a href="https://github.com/anxkhn/JevPlaysPokemon">anxkhn/JevPlaysPokemon</a></b> — ⭐1 · HTML · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · HTML · GPL-3.0 · [anxkhn](https://github.com/anxkhn)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev plays Generation 3 Pokémon via Showdown and a real FireRed ROM.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/anxkhn--jevplayspokemon/fc9ead060d7fa36a.png" width="100%" alt="anxkhn/JevPlaysPokemon screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/jev-review-action">fatwang2/jev-review-action</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · JavaScript · MIT · [fatwang2](https://github.com/fatwang2)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 2 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Configurable GitHub submission review and PR classification with TypeSafe Jev. No text-generation model.

</details>

<details>
<summary><b><a href="https://github.com/lbotinelly/jev-little-airways">lbotinelly/jev-little-airways</a></b> — ⭐1 · HTML · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · HTML · MIT · [lbotinelly](https://github.com/lbotinelly)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A show-and-tell capability study for Jev, TypeSafe's System One decision model.

</details>

<details>
<summary><b><a href="https://github.com/sontakey/awesome-jev">sontakey/awesome-jev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · NOASSERTION · [sontakey](https://github.com/sontakey)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Unofficial list of insanely useful TypeSafe AI Jev / System One projects

</details>

<details>
<summary><b><a href="https://github.com/TanayPadar/gpt-vs-jev">TanayPadar/gpt-vs-jev</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [TanayPadar](https://github.com/TanayPadar)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Compare GPT generated language with JEV structured Noul decisions on the same input.

</details>

<details>
<summary><b><a href="https://github.com/tylerjharden/harden-jev-decides">tylerjharden/harden-jev-decides</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · [tylerjharden](https://github.com/tylerjharden)

**डेटा** · स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.

</details>

<details>
<summary><b><a href="https://github.com/019ec6e2/pi-jev-compact">019ec6e2/pi-jev-compact</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · NOASSERTION · [019ec6e2](https://github.com/019ec6e2)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/adhamelhayek-lab/jev-connector">adhamelhayek-lab/jev-connector</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · JavaScript · [adhamelhayek-lab](https://github.com/adhamelhayek-lab)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/aoprisan/jev-ts-repl">aoprisan/jev-ts-repl</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [aoprisan](https://github.com/aoprisan)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/Charlyhno-eng/jev-document-classification">Charlyhno-eng/jev-document-classification</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [Charlyhno-eng](https://github.com/Charlyhno-eng)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

JEV Document Classification enables the rapid and cost-effective classification of text-based documents using AI, leveraging TypeSafe's "System One" model.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/charlyhno-eng--jev-document-classification/113bcf66f1648122.png" width="100%" alt="Charlyhno-eng/jev-document-classification screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/cmartinez9/jev-judge-bench">cmartinez9/jev-judge-bench</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [cmartinez9](https://github.com/cmartinez9)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Binary LLM-judge bench — compare Jev (TypeSafe System One) against a frontier LLM judge on speed, cost, and agreement with human labels.

</details>

<details>
<summary><b><a href="https://github.com/Dujaydis/JevSysUno">Dujaydis/JevSysUno</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · [Dujaydis](https://github.com/Dujaydis)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/erhanmeydan/jev2048">erhanmeydan/jev2048</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · MIT · [erhanmeydan](https://github.com/erhanmeydan)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe'in Jev karar modeli gerçek bir online 2048 sitesinde oynuyor — hamle başına tek API çağrısı, tek anahtar.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/erhanmeydan--jev2048/a2709def4f48e691.gif" width="100%" alt="erhanmeydan/jev2048 screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/erhanmeydan--jev2048/a2709def4f48e691.gif" width="100%" alt="erhanmeydan/jev2048 animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/felixfisher/pi-jev-compaction">felixfisher/pi-jev-compaction</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [felixfisher](https://github.com/felixfisher)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Experimental Pi extension using TypeSafe Jev for auditable tool-history compaction

</details>

<details>
<summary><b><a href="https://github.com/heaven-hm/jev-system-one">heaven-hm/jev-system-one</a></b> — inferred · 1 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [heaven-hm](https://github.com/heaven-hm)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports

</details>

<details>
<summary><b><a href="https://github.com/Jbenkang/localJev">Jbenkang/localJev</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [Jbenkang](https://github.com/Jbenkang)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

making-jev-local

</details>

<details>
<summary><b><a href="https://github.com/jdhornsby/typesafe-jev">jdhornsby/typesafe-jev</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · [jdhornsby](https://github.com/jdhornsby)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/JulioPeixoto/jev-decision-bench">JulioPeixoto/jev-decision-bench</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [JulioPeixoto](https://github.com/JulioPeixoto)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/kagurazakayashi/dsh-jev">kagurazakayashi/dsh-jev</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [kagurazakayashi](https://github.com/kagurazakayashi)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

我正在探索 DeepSeek Harness 中 DeepSeek 与 Jev 的合作方式。

</details>

<details>
<summary><b><a href="https://github.com/KamilPostrozny/pi-fast-jev-compaction">KamilPostrozny/pi-fast-jev-compaction</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [KamilPostrozny](https://github.com/KamilPostrozny)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Fast JEV compaction extension for pi

</details>

<details>
<summary><b><a href="https://github.com/KaushikKC/JevScope">KaushikKC/JevScope</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [KaushikKC](https://github.com/KaushikKC)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/kentaro/jev-fizzbuzz">kentaro/jev-fizzbuzz</a></b> — HTML · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · HTML · [kentaro](https://github.com/kentaro)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/kentaro/jev-shogi">kentaro/jev-shogi</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · [kentaro](https://github.com/kentaro)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

判定特化モデル Jev に将棋を指させる実験（ロリポップ！AIゲートウェイ経由）

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/kentaro/jev-shogi/main/games/20260918-214930-skill-20/game.mp4"><img src="" width="100%" alt="kentaro/jev-shogi video"></a><br><sub><a href="https://raw.githubusercontent.com/kentaro/jev-shogi/main/games/20260918-214930-skill-20/game.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kevin9327/jev-master">kevin9327/jev-master</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · MIT · [kevin9327](https://github.com/kevin9327)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Typed System One decisions with Jev: Choice + Score + Noul composed in code.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kevin9327--jev-master/cbf05c4561269075.png" width="100%" alt="kevin9327/jev-master screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kspviswa/chakravyuha-jev">kspviswa/chakravyuha-jev</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · JavaScript · MIT · [kspviswa](https://github.com/kspviswa)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment: the model picks each move, the walk grades it green or red, and the history page asks whether its confidence score can be trusted. BYOK, no build step.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kspviswa--chakravyuha-jev/4dfa22d0de9f27c1.png" width="100%" alt="kspviswa/chakravyuha-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/LukasCaha/jev-theme">LukasCaha/jev-theme</a></b> — JavaScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · JavaScript · [LukasCaha](https://github.com/LukasCaha)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Jev powered string to color theme generator

</details>

<details>
<summary><b><a href="https://github.com/memorysaver/jev-atari-lab">memorysaver/jev-atari-lab</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · GPL-2.0 · [memorysaver](https://github.com/memorysaver)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Challenge Atari with Jev: structured decisions, value questions, and replayable experiments

</details>

<details>
<summary><b><a href="https://github.com/muse0509/jev-preflight">muse0509/jev-preflight</a></b> — inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [muse0509](https://github.com/muse0509)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/Nachom3/jevTrader">Nachom3/jevTrader</a></b> — Rust · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Rust · [Nachom3](https://github.com/Nachom3)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A High Frecuncy Trader made in Rust using Jev as a decision maker.

</details>

<details>
<summary><b><a href="https://github.com/narulaskaran/jev-data-questions">narulaskaran/jev-data-questions</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · [narulaskaran](https://github.com/narulaskaran)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/nitro527/jev_project">nitro527/jev_project</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · [nitro527](https://github.com/nitro527)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/pavy23/jev_typesafeai_test">pavy23/jev_typesafeai_test</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · [pavy23](https://github.com/pavy23)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/rolottr/x-jev-classifier">rolottr/x-jev-classifier</a></b> — JavaScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · JavaScript · AGPL-3.0 · [rolottr](https://github.com/rolottr)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Chrome extension that stamps every X post with a type badge — alpha, shitpost, AI slop, bait — judged by Jev from Typesafe

</details>

<details>
<summary><b><a href="https://github.com/scottjoyner/my-jev">scottjoyner/my-jev</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [scottjoyner](https://github.com/scottjoyner)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/semenovdv/jev_maze">semenovdv/jev_maze</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [semenovdv](https://github.com/semenovdv)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-context-curator">Shashank-H/pi-jev-context-curator</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [Shashank-H](https://github.com/Shashank-H)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

A Jev based context curator for pi

</details>

<details>
<summary><b><a href="https://github.com/sueszli/qwen27b-jev">sueszli/qwen27b-jev</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · MIT · [sueszli](https://github.com/sueszli)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

multiple-choice questions for Qwen3.8-27B, read from logits

</details>

<details>
<summary><b><a href="https://github.com/TonyP-MR/jev-curation-engine">TonyP-MR/jev-curation-engine</a></b> — Python · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · [TonyP-MR](https://github.com/TonyP-MR)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions with existing LLM audit results.

</details>

<details>
<summary><b><a href="https://github.com/trufyrelabs/tru-jev-harness">trufyrelabs/tru-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · MIT · [trufyrelabs](https://github.com/trufyrelabs)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/wh000wh000/awesome-jev-live">wh000wh000/awesome-jev-live</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · NOASSERTION · [wh000wh000](https://github.com/wh000wh000)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Evidence-graded index of the Jev / TypeSafe System One ecosystem. Rebuilt every 2 hours in 20 languages.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/4esv/jev-eval/main/results/coverage.png" width="100%" alt="wh000wh000/awesome-jev-live screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Tatuck/jev-boe-demo/main/docs/demo-web.gif" width="100%" alt="wh000wh000/awesome-jev-live animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/ybelatar/pokemon_jev">ybelatar/pokemon_jev</a></b> — inferred · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · [ybelatar](https://github.com/ybelatar)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/Z761293629/pi-jev-helm">Z761293629/pi-jev-helm</a></b> — TypeScript · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · TypeScript · [Z761293629](https://github.com/Z761293629)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 10 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

_अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।_

</details>

<details>
<summary><b><a href="https://github.com/zhuyansen/jev-news-cold-start">zhuyansen/jev-news-cold-start</a></b> — Python · inferred · 0 天 · **NEW**</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `inferred` · Python · MIT · [zhuyansen](https://github.com/zhuyansen)

**डेटा** · स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Cross-domain check on MIND news: a zero-shot Jev headline prior is worth ~500 labelled articles, adds +0.069 ρ as features, and lifts a Thompson-sampling cold start by 25%.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/typesafe-adblock">realZachi/typesafe-adblock</a></b> — ⭐43 · JavaScript · unverified · 0 天 · ⭐+1</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `unverified` · JavaScript · MIT · [realZachi](https://github.com/realZachi)

**डेटा** · स्टार **43** (+1) · फ़ॉर्क 3 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev) "is this DOM element an ad?" and pops it off the page. BYOK, no backend, not a real ad blocker.

</details>

<details>
<summary><b><a href="https://github.com/devanshbatham/commit-miner">devanshbatham/commit-miner</a></b> — ⭐20 · Rust · unverified · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `unverified` · Rust · [devanshbatham](https://github.com/devanshbatham)

**डेटा** · स्टार **20** · फ़ॉर्क 5 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.

</details>

<details>
<summary><b><a href="https://github.com/andysc/IBM-Q-System-One-3D-model">andysc/IBM-Q-System-One-3D-model</a></b> — ⭐12 · OpenSCAD · unverified · 2688 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `unverified` · OpenSCAD · [andysc](https://github.com/andysc)

**डेटा** · स्टार **12** · फ़ॉर्क 4 · खुले इश्यू 1 · बनाया गया 2019-03-16 · अंतिम पुश 2019-05-10 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

3D-printed model of IBM Q System One

</details>

<details>
<summary><b><a href="https://github.com/phyous/tsai-sc">phyous/tsai-sc</a></b> — ⭐12 · Python · unverified · 2 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `unverified` · Python · MIT · [phyous](https://github.com/phyous)

**डेटा** · स्टार **12** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action probabilities.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/phyous--tsai-sc/f48a030ae92fb1fe.png" width="100%" alt="phyous/tsai-sc screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/razorback16/openjev">razorback16/openjev</a></b> — ⭐11 · Python · unverified · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `unverified` · Python · Apache-2.0 · [razorback16](https://github.com/razorback16)

**डेटा** · स्टार **11** · फ़ॉर्क 2 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Open, Jev-compatible System One decision server on DiffusionGemma

</details>

<details>
<summary><b><a href="https://github.com/zhengxuyu/litjev">zhengxuyu/litjev</a></b> — ⭐3 · Python · unverified · 0 天</summary>

**बुनियादी तथ्य** · `लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `unverified` · Python · Apache-2.0 · [zhengxuyu](https://github.com/zhengxuyu)

**डेटा** · स्टार **3** · फ़ॉर्क 1 · खुले इश्यू 3 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

**सारांश**

Turn any off-the-shelf LLM into a Jev -like decision layer

</details>

<a id="projects-by-implementation-language"></a>

## कार्यान्वयन भाषा के अनुसार परियोजनाएँ

यह पारिस्थितिकी मुख्यतः Python और TypeScript में केंद्रित है, पर टाइप्ड क्लाइंट अन्य भाषाओं में भी आते रहते हैं। यह तालिका स्वयं प्रविष्टियों से बनाई जाती है।

| भाषा | प्रविष्टियाँ | उदाहरण |
| --- | --- | --- |
| Python | 133 | `typesafe-ai/system-one-adapter-python`, `typesafe-ai/typesafe-sdk-python`, `realZachi/pg-jev` |
| TypeScript | 118 | `typesafe-ai/typesafe-sdk-js`, `AntonioCoppe/jev-harness`, `opaielsheikh/typesafe-migration-guard` |
| JavaScript | 54 | `ziyu/sytem-one-sdk`, `Ying-Kai-Liao/jev-browser`, `arunav25/jev-mcp` |
| Go | 13 | `Gaurav-Gosain/jev-go`, `Stumble/jev-go`, `anilsenay/jev` |
| Rust | 12 | `AkashPriyadarshii/jev-curate`, `abeldzan/jev-rs`, `AkashPriyadarshii/jev-git` |
| HTML | 9 | `typesafe-ai/typesafe-ai.github.io`, `yzfly/awesome-jev-zh`, `vinilana/jev-eval-agent` |
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
| OCaml | 1 | `jonesmelton/verdict` |
| OpenSCAD | 1 | `andysc/IBM-Q-System-One-3D-model` |
| PowerShell | 1 | `omni-/ask-jev` |
| Ruby | 1 | `javiergradiche/ruby_llm-providers-typesafe` |
| TeX | 1 | `dnakhoa/jev-deferred-crispification` |

<sub>केवल वे प्रविष्टियाँ गिनी जाती हैं जो भाषा घोषित करती हैं। अधोसंरचना, दस्तावेज़ीकरण और चर्चा वाली प्रविष्टियाँ इस तालिका से बाहर हैं।</sub>

## यह सूची अद्यतन कैसे रहती है

इस README का मुख्य भाग कोई मनुष्य संपादित नहीं करता। रिपॉज़िटरी एक निर्धारित समय-सारणी पर पाँच-चरणीय पाइपलाइन चलाती है और तभी कमिट करती है जब कुछ वास्तव में बदला हो।

<img src="assets/readme/pipeline.svg" width="100%" alt="यह सूची अद्यतन कैसे रहती है">

- **collect** — क्वेरी मैट्रिक्स, आधिकारिक संगठन, GitHub कोड खोज, Hacker News और HuggingFace हब पर GitHub खोज।
- **curate** — नियतात्मक और LLM-रहित, इसलिए एक ही इनपुट पर लगातार दो रन बाइट-दर-बाइट समान आउटपुट देते हैं। प्रासंगिकता दो-संकेत नियम तय करता है; नाम-टकराव (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD और समान) एक स्पष्ट, ऑडिट-योग्य सूची से बाहर रखे जाते हैं।
- **media** — हर परियोजना के अपने स्क्रीनशॉट और स्क्रीन रिकॉर्डिंग एकत्र करता है। संपत्तियाँ इस रिपॉज़िटरी में तभी कॉपी की जाती हैं जब परियोजना पुनर्वितरण-अनुकूल लाइसेंस घोषित करती है; अन्यथा अपस्ट्रीम URL सीधे लिंक किया जाता है और कार्ड यह बताता है।
- **render** — एक ही टेम्पलेट से हर भाषा संस्करण बनाता है, इसलिए बीस README संरचना में कभी अलग नहीं हो सकते।
- **audit** — बिल्ड तब विफल करता है जब किसी प्रविष्टि में URL न हो, कोई लिंक टूटा हो, दो प्रविष्टियाँ एक ही URL दोहराती हों, या कोई README अपने निर्मित रूप से हट जाए।

## योगदान

सुधार स्वागत-योग्य हैं और इस सूची को बेहतर बनाने का सबसे तेज़ तरीका हैं। अगर कोई प्रविष्टि गलत श्रेणी में है, गलत दर्जा पाई है, या किसी परियोजना को नाम-टकराव मानकर गलती से बाहर रखा गया है, तो issue या pull request खोलें — यही अंतिम श्रेणी है जहाँ स्वचालित फ़िल्टर के गलत होने की सबसे अधिक संभावना है। जोड़ना `scripts/collect.py` में स्रोत जोड़कर करना बेहतर है, README संपादित करके नहीं, क्योंकि README हर चक्र में फिर से बनाया जाता है।

---

<sub>स्वतंत्र समुदाय परियोजना। TypeSafe AI से संबद्ध नहीं, न ही उससे अनुमोदित या समीक्षित। उत्पाद व्यवहार, मूल्य, सीमाएँ और मॉडल उपनाम बिना सूचना के बदलते हैं; जो कुछ भी निर्णायक है उसे आधिकारिक दस्तावेज़ से सत्यापित करें। संपत्तियाँ उनकी अपस्ट्रीम परियोजनाओं की संपत्ति बनी रहती हैं और केवल वहीं पुनरुत्पादित की जाती हैं जहाँ लाइसेंस अनुमति देता है।</sub>

<sub>इनके द्वारा निर्मित · `render.py` · 2026-09-18T22:17:25+08:00</sub>
