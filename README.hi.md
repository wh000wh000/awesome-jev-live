<p align="center">
  <img src="assets/readme/hero.png" width="100%" alt="Awesome Jev Live">
</p>

<h1 align="center">Awesome Jev Live</h1>

<p align="center"><b>प्रमाण-श्रेणीबद्ध Jev सूचकांक, जो हर दो घंटे में स्वयं को फिर से बनाता है।</b></p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/entries-497-0d9488" alt="entries">
  <img src="https://img.shields.io/badge/languages-20-1f6feb" alt="languages">
  <img src="https://img.shields.io/badge/refresh-every%202h-16a34a" alt="refresh">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="MIT"></a>
</p>

<p align="center"><sub><a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.es.md">Español</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.pt-BR.md">Português (Brasil)</a> · <a href="README.ru.md">Русский</a> · <a href="README.it.md">Italiano</a> · <a href="README.ar.md">العربية</a> · <b>हिन्दी</b> · <a href="README.tr.md">Türkçe</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.pl.md">Polski</a> · <a href="README.nl.md">Nederlands</a> · <a href="README.uk.md">Українська</a></sub></p>

> [!NOTE]
> **लाइव सूचकांक** · अंतिम सिंक: `2026-09-19T12:24:57+08:00` (UTC+8)
> · प्रविष्टियाँ: **497** · इस चक्र में नई: **65** · कार्यान्वयन भाषाएँ: **26**

<sub>नीचे दी गई हर प्रविष्टि इस रिपॉज़िटरी की पाइपलाइन द्वारा एकत्रित, फ़िल्टर और पुनः जाँची गई है। संख्याएँ और समय-चिह्न स्रोतों से आते हैं, हाथ से लिखे स्नैपशॉट से नहीं।</sub>

## विषय-सूची

- [Jev क्या है?](#jev-कय-ह)
- [प्रविष्टियों का दर्जा कैसे तय होता है](#परवषटय-क-दरज-कस-तय-हत-ह)
- [आधिकारिक SDK और डेवलपर उपकरण](#आधकरक-sdk-और-डवलपर-उपकरण) — **6**
- [समुदाय के क्लाइंट, SDK और अडैप्टर](#समदय-क-कलइट-sdk-और-अडपटर) — **74**
- [एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट](#एजट-उपकरण-mcp-हक-गट-और-कडग-एजट) — **147**
- [रूटिंग, गार्डरेल और अनुमोदन](#रटग-गरडरल-और-अनमदन) — **54**
- [मूल्यांकन, कैलिब्रेशन और बेंचमार्क](#मलयकन-कलबरशन-और-बचमरक) — **38**
- [खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध](#खल-पनरतपदन-वट-और-आरकटकचर-शध) — **21**
- [अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो](#अनपरयग-गम-रबटकस-और-इटरकटव-डम) — **40**
- [लेखन, चर्चाएँ और समान सूचियाँ](#लखन-चरचए-और-समन-सचय) — **117**
- [कार्यान्वयन भाषा के अनुसार परियोजनाएँ](#करयनवयन-भष-क-अनसर-परयजनए)
- [यह सूची अद्यतन कैसे रहती है](#यह-सच-अदयतन-कस-रहत-ह)

## Jev क्या है?

Jev, TypeSafe AI का पहला **System One मॉडल** है। यह गद्य नहीं लिखता। यह एक स्थिति और ऐसे प्रश्न लेता है जिनका उत्तर-क्षेत्र आप पहले से तय करते हैं, और टाइप्ड मान प्रायिकता वितरण के साथ लौटाता है जिन पर आपका कोड शाखा बना सकता है।

|                  |                                                                                                                                                                                             |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **रूप**          | `state + typed questions` → `constrained answers + probabilities` → `your code`                                                                                                             |
| **प्रिमिटिव**    | `Choice` (≤255 विकल्पों में से एक चुनें), `Score` (2–10 का रूब्रिक), `Noul` (प्रायिक हाँ/नहीं)                                                                                              |
| **एंडपॉइंट**     | `POST https://api.typesafe.ai/v1/systemone`, मॉडल `jev-1.13.0` / उपनाम `jev-latest`                                                                                                         |
| **उपयुक्त**      | सीमित कार्यप्रवाह के भीतर रूटिंग, ट्राइएज, स्कोरिंग, मॉडरेशन, सत्यापन और कम-विलंबता गेट                                                                                                     |
| **ज्ञात सीमाएँ** | गिनती अविश्वसनीय है, बहुस्तरीय परोक्षता कमज़ोर है, और आधिकारिक सामग्री में नौ प्रकार की असमानता बताई गई है। स्कीमा-वैध आउटपुट सही निर्णय के बराबर नहीं है — अपने ही डेटा पर कैलिब्रेट करें। |

## प्रविष्टियों का दर्जा कैसे तय होता है

इस क्षेत्र की अधिकांश सूचियाँ बस समावेशन का दावा करती हैं। यह बताती है कि उसने वास्तव में कितना सत्यापित किया, और फिर आपको उसी अनुसार फ़िल्टर करने देती है।

| दर्जा        | इसका क्या अर्थ है                                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `official`   | TypeSafe AI द्वारा स्वयं प्रकाशित।                                                                                                                |
| `observed`   | एक सार्वजनिक कृति जिसे खोला और पढ़ा जा सकता है — वास्तविक स्रोत, वास्तविक कॉन्फ़िगरेशन, या रिपॉज़िटरी नाम या टॉपिक में स्पष्ट TypeSafe/Jev घोषणा। |
| `inferred`   | एक अस्पष्ट संकेत और समर्थक शब्दावली के आधार पर मेल, पर अभी पंक्ति-दर-पंक्ति नहीं पढ़ा गया।                                                        |
| `unverified` | संबंधित लगता है, स्वतंत्र रूप से कुछ भी पुष्ट नहीं हुआ। केवल खोज के लिए सूचीबद्ध।                                                                 |

<a id="official-sdk"></a>

## आधिकारिक SDK और डेवलपर उपकरण

वह सब जो TypeSafe ने स्वयं प्रकाशित किया है। यहीं से शुरू करें।

<details>
<summary><b><a href="https://github.com/typesafe-ai/skills">typesafe-ai/skills</a></b> — ⭐316 · official · 6 天 · ⭐+31</summary>

##### बुनियादी तथ्य

`आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · MIT · typesafe-ai

##### डेटा

स्टार **316** (+31) · फ़ॉर्क 18 · खुले इश्यू 1 · बनाया गया 2026-08-24 · अंतिम पुश 2026-09-12 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Agent skills for building with TypeSafe's System One API

> The vendor's own agent skills. Because it is updated continuously, it is the closest thing to a specification of how TypeSafe intends Jev to be driven from an agent.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-js">typesafe-ai/typesafe-sdk-js</a></b> — ⭐135 · TypeScript · official · 3 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · TypeScript · MIT · typesafe-ai

##### डेटा

स्टार **135** (+1) · फ़ॉर्क 10 · खुले इश्यू 6 · बनाया गया 2026-09-04 · अंतिम पुश 2026-09-15 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

The official TypeScript/JavaScript library for the TypeSafe API

> TypeScript client where the answer type is inferred from the question you asked, so a mismatched return type is a compile error rather than a runtime surprise.

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/system-one-adapter-python">typesafe-ai/system-one-adapter-python</a></b> — ⭐128 · Python · official · 0 天 · ⭐+4</summary>

##### बुनियादी तथ्य

`आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · Python · MIT · typesafe-ai

##### डेटा

स्टार **128** (+4) · फ़ॉर्क 13 · खुले इश्यू 0 · बनाया गया 2026-08-08 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Drop-in TypeSafeClient replacement backed by LLM APIs

> Drop-in replacement that backs the same interface with an ordinary LLM provider. This is the honest way to A/B a typed decision against a prompt, on your own data, before committing to either.

<sub>कोड में प्रयुक्त पाया गया: `README.md`, `src/system_one_adapter/__init__.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-sdk-python">typesafe-ai/typesafe-sdk-python</a></b> — ⭐94 · Python · official · 0 天 · ⭐+2</summary>

##### बुनियादी तथ्य

`आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · Python · MIT · typesafe-ai

##### डेटा

स्टार **94** (+2) · फ़ॉर्क 8 · खुले इश्यू 2 · बनाया गया 2026-09-04 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

The official Python library for the TypeSafe API

> Synchronous and asynchronous clients. The fastest path from an API key to a typed decision, and the reference the community clients are compared against.

<sub>कोड में प्रयुक्त पाया गया: `src/typesafe_sdk/__init__.py`, `src/typesafe_sdk/_core/retry.py`, `src/typesafe_sdk/_core/config.py`, `src/typesafe_sdk/_core/logging.py`</sub>

</details>

<details>
<summary><b><a href="https://github.com/typesafe-ai/typesafe-ai.github.io">typesafe-ai/typesafe-ai.github.io</a></b> — ⭐1 · HTML · official · 106 天</summary>

##### बुनियादी तथ्य

`आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · HTML · typesafe-ai

##### डेटा

स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 1 · बनाया गया 2024-05-28 · अंतिम पुश 2026-06-04 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://github.com/TypeSafeAI/clarity-judge">TypeSafeAI/clarity-judge</a></b> — ⭐1 · TypeScript · official · 0 天</summary>

##### बुनियादी तथ्य

`आधिकारिक SDK और डेवलपर उपकरण` · आधिकारिक · `official` · TypeScript · TypeSafeAI

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Multi-axis writing quality checker powered by TypeSafe AI's Jev model. Separate named checks, each with its own verdict and confidence.

</details>

<a id="community-sdk"></a>

## समुदाय के क्लाइंट, SDK और अडैप्टर

System One एंडपॉइंट के लिए टाइप्ड क्लाइंट, उतनी भाषाओं में जितनी तक समुदाय पहुँचा है।

<details>
<summary><b><a href="https://github.com/jexp/neo4jev">jexp/neo4jev</a></b> — ⭐20 · Jupyter · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Jupyter · MIT · jexp

##### डेटा

स्टार **20** · फ़ॉर्क 5 · खुले इश्यू 1 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Typesafe.ai System One Model Jev navigating a Neo4j graph by using a classifier over neighbouring relationships

</details>

<details>
<summary><b><a href="https://github.com/AkashPriyadarshii/jev-curate">AkashPriyadarshii/jev-curate</a></b> — ⭐3 · Rust · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Rust · MIT · AkashPriyadarshii

##### डेटा

स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

High-throughput synthetic & pretraining dataset sifter powered by TypeSafe AI Jev (api.typesafe.ai). Stream, filter, and score Parquet & JSONL datasets at 1,500+ rows/sec using System One typed decisions (Choice, Score, Noul).

</details>

<details>
<summary><b><a href="https://github.com/ckaraca/awesome-jev">ckaraca/awesome-jev</a></b> — ⭐3 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Python · CC0-1.0 · ckaraca

##### डेटा

स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

A curated list of tools, integrations, and experiments built on Jev, TypeSafe AI's System One model for fast, typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/Premo-Cloud/typesafe-sdk-java">Premo-Cloud/typesafe-sdk-java</a></b> — ⭐3 · Java · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Java · MIT · Premo-Cloud

##### डेटा

स्टार **3** · फ़ॉर्क 1 · खुले इश्यू 2 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Community Java client for the TypeSafe System One API (unofficial)

</details>

<details>
<summary><b><a href="https://github.com/AntonioCoppe/jev-harness">AntonioCoppe/jev-harness</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · TypeScript · MIT · AntonioCoppe

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Decision harness for TypeSafe Jev — confidence gates, shadow mode, recipes, and evals. Claude CLI 48.9s → Jev 1.3s on the same row-filter job.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/antoniocoppe--jev-harness/aee6b175de384408.png" width="100%" alt="AntonioCoppe/jev-harness screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/MrJev/awesome-jev">MrJev/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Python · CC0-1.0 · MrJev

##### डेटा

स्टार **2** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A curated list of projects, integrations, and resources for Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/nshkrdotcom/typesafe_sdk">nshkrdotcom/typesafe_sdk</a></b> — ⭐2 · Elixir · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Elixir · MIT · nshkrdotcom

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

An idiomatic, type-safe Elixir port of the official TypeScript AI SDK (ai / ai-sdk) providing unified LLM integrations, streaming text and structured outputs, tool calling, and agentic workflows. Jev is their current flagship model and is the first System One model.

</details>

<details>
<summary><b><a href="https://github.com/opaielsheikh/typesafe-migration-guard">opaielsheikh/typesafe-migration-guard</a></b> — ⭐2 · TypeScript · observed · 1 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · TypeScript · opaielsheikh

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Automated database migration safety reviewer powered by TypeSafe AI (Jev System One model)

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://img.youtube.com/vi/4cI4r2Np7J4/maxresdefault.jpg" width="100%" alt="opaielsheikh/typesafe-migration-guard screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/xingwudao/OpenJev">xingwudao/OpenJev</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Python · xingwudao

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

OpenJev: an independent Jev-inspired System One decision API based on TypeSafe.ai concepts. Choice, score and noul primitives, local mock server, Python and TypeScript SDKs. Real inference planned; not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/ziyu/sytem-one-sdk">ziyu/sytem-one-sdk</a></b> — ⭐1 · JavaScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · JavaScript · MIT · ziyu

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Unified interface wrapper for system one models

</details>

<details>
<summary><b><a href="https://github.com/gpazo/jev-vphone-cli">gpazo/jev-vphone-cli</a></b> — Swift · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Swift · MIT · gpazo

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Jev from Typesafe.ai + vphone-cli

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gpazo--jev-vphone-cli/baa413a8104308f4.jpg" width="100%" alt="gpazo/jev-vphone-cli screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/javiergradiche/ruby_llm-providers-typesafe">javiergradiche/ruby_llm-providers-typesafe</a></b> — Ruby · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Ruby · MIT · javiergradiche

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

TypeSafe System One models (Jev) for RubyLLM: typed judgments, evaluations and reranking.

</details>

<details>
<summary><b><a href="https://github.com/kyledickey/jev-go">kyledickey/jev-go</a></b> — observed · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · MIT · kyledickey

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

TypeSafe.ai Jev Go SDK

</details>

<details>
<summary><b><a href="https://github.com/nu-sync/effect-evaluation">nu-sync/effect-evaluation</a></b> — TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · TypeScript · MIT · nu-sync

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

An Effect-native client for TypeSafe AI System One models (Jev)

</details>

<details>
<summary><b><a href="https://github.com/typesend/typesafe_ai">typesend/typesafe_ai</a></b> — Elixir · observed · 1 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `observed` · Elixir · MIT · typesend

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Typed Elixir client for TypeSafe AI and its Jev System One model, with offline test stubs, concurrent fan-out, and atom-keyed answers.

</details>

<details>
<summary><b><a href="https://github.com/realZachi/pg-jev">realZachi/pg-jev</a></b> — ⭐172 · Shell · inferred · 0 天 · ⭐+3</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Shell · NOASSERTION · realZachi

##### डेटा

स्टार **172** (+3) · फ़ॉर्क 10 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Ask your Postgres tables questions in plain language. A PostgreSQL extension powered by TypeSafe's Jev.

</details>

<details>
<summary><b><a href="https://github.com/pinecone-io/cultivar">pinecone-io/cultivar</a></b> — ⭐39 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · pinecone-io

##### डेटा

स्टार **39** · फ़ॉर्क 2 · खुले इश्यू 5 · बनाया गया 2026-06-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Use cultivar to test your Agent Skills and Docs by running them in sandboxes, and across different agents.

</details>

<details>
<summary><b><a href="https://github.com/nidhi-singh02/agent-router">nidhi-singh02/agent-router</a></b> — ⭐33 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · nidhi-singh02

##### डेटा

स्टार **33** (+1) · फ़ॉर्क 1 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

CLI that picks Cursor, Claude Code, Codex, or OpenCode + model/effort for a task, then launches it. Powered by Jev and Herdr

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="nidhi-singh02/agent-router screenshot"></td>
<td align="center" valign="top"><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/nidhi-singh02--agent-router/976e58ae0d278abd.jpg" width="100%" alt="video"></a><br><sub><a href="https://img.youtube.com/vi/7w8eRWnUUA8/maxresdefault.jpg">यहाँ देखें img.youtube.com</a> · प्लेबैक होस्ट साइट पर खुलता है; GitHub इसे इनलाइन एम्बेड नहीं कर सकता</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/tacticocc/Jevbridge">tacticocc/Jevbridge</a></b> — ⭐17 · TypeScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · tacticocc

##### डेटा

स्टार **17** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

ACP and MCP adapter that bridges TypeSafe Jev with any LLM — computer use and typed decisions alongside Codex, Claude, Grok, and OpenCode.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tacticocc--jevbridge/772995670b3e42e9.png" width="100%" alt="tacticocc/Jevbridge screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AboveColin/HA-Jev">AboveColin/HA-Jev</a></b> — ⭐15 · Python · inferred · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · AboveColin

##### डेटा

स्टार **15** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Ask your house a question, get a number back. Home Assistant integration for TypeSafe Jev: typed answers as sensors, four actions for automations, and a conversation agent for Assist.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abovecolin--ha-jev/87fa9143f6990ef1.png" width="100%" alt="AboveColin/HA-Jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/dannote/jev">dannote/jev</a></b> — ⭐13 · Elixir · inferred · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Elixir · MIT · dannote

##### डेटा

स्टार **13** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

TypeSafe Jev for OTP: reply to Jev from a GenServer and pattern match on its answer

</details>

<details>
<summary><b><a href="https://github.com/shiftynick/jev-axi">shiftynick/jev-axi</a></b> — ⭐13 · TypeScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · TypeScript · MIT · shiftynick

##### डेटा

स्टार **13** · फ़ॉर्क 1 · खुले इश्यू 4 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Agent-ergonomic CLI for TypeSafe's Jev: fast calibrated judgments (pick, rate, check, rank, triage, guard) from the shell

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shiftynick--jev-axi/e97a8238f41de3c1.gif" width="100%" alt="shiftynick/jev-axi screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/shiftynick--jev-axi/e97a8238f41de3c1.gif" width="100%" alt="shiftynick/jev-axi animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Ying-Kai-Liao/jev-browser">Ying-Kai-Liao/jev-browser</a></b> — ⭐12 · JavaScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · JavaScript · MIT · Ying-Kai-Liao

##### डेटा

स्टार **12** · फ़ॉर्क 3 · खुले इश्यू 3 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Browser automation where an LLM plans and Jev (Typesafe System One) decides. Library, CLI and MCP server.

</details>

<details>
<summary><b><a href="https://github.com/keltokhy/jgrep">keltokhy/jgrep</a></b> — ⭐9 · Python · inferred · 0 天 · ⭐+2</summary>

##### बुनियादी तथ्य

`समुदाय के क्लाइंट, SDK और अडैप्टर` · समुदाय · `inferred` · Python · MIT · keltokhy

##### डेटा

स्टार **9** (+2) · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

grep, but the pattern is a description. Filters lines by meaning with TypeSafe's Jev decision model: ~200 ms and a thousandth of a cent per line.

</details>

<details>
<summary><b>इस श्रेणी में और</b> <sub>· 50</sub></summary>

- [arunav25/jev-mcp](https://github.com/arunav25/jev-mcp) - Connect JEV to MCP clients and compare its judgments against general-purpose LLMs using shared datasets and.
- [Nasrallah-AL/jev-cli](https://github.com/Nasrallah-AL/jev-cli) - Command-line tool for TypeSafe&#x27;s Jev AI model.
- [saibimajdi/typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk) - Community .NET SDK for the TypeSafe AI System One API — typed noul, choice, and score questions with.
- [sharziki/semdecide](https://github.com/sharziki/semdecide) - Typed semantic decisions for Unix pipelines and CI, powered by TypeSafe AI Jev.
- [frostney/clean-code-review](https://github.com/frostney/clean-code-review) - Every code file in a pull request, judged against Uncle Bob&#x27;s Clean Code by TypeSafe&#x27;s Jev, then reviewed by.
- [rhighs/jev-code](https://github.com/rhighs/jev-code) - Interactive TypeScript coding CLI powered by Jev typed decisions and constrained AST generation.
- [romaluev/jev-ego](https://github.com/romaluev/jev-ego) - Fast browser agent for ego lite. One TypeSafe request per step; an agent or Jev picks the move.
- [AkashPriyadarshii/jev-seo](https://github.com/AkashPriyadarshii/jev-seo) - 100% free ₹0 agent-first SEO &amp; GEO CLI suite and MCP server in Rust replacing Semrush and OpenSEO via.
- [burnigtm/jev-mcp](https://github.com/burnigtm/jev-mcp) - MCP server that puts TypeSafe Jev on the coding loop in Cursor, Codex, and any MCP client.
- [docxology/daf-jev](https://github.com/docxology/daf-jev) - daf-jev: composable Python toolkit for TypeSafe.
- [EugeneBoondock/jevsql](https://github.com/EugeneBoondock/jevsql) - SQL with natural-language predicates, powered by TypeSafe.
- [Olti1947/jev-java](https://github.com/Olti1947/jev-java) - Idiomatic Java SDK for TypeSafe AI Jev System One decision engine.
- [tumf/jev-cli](https://github.com/tumf/jev-cli) - Small dependency-free CLI for TypeSafe Jev.
- [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh) - Jev / TypeSafe System One 中文精选列表：官方资料、SDK、爆款应用、Agent 工具、开源复现与独立评测，附中文上手指南，每日自动收录 GitHub 热门项目.
- [Butochnikov/laravel-typesafe-jev](https://github.com/Butochnikov/laravel-typesafe-jev) - Unofficial Laravel integration for TypeSafe Jev AI with typed responses, async requests, scoped dependency.
- [ddfeyes/jev-mode](https://github.com/ddfeyes/jev-mode) - I kept watching coding agents burn context on decisions that aren.
- [Gaurav-Gosain/jev-go](https://github.com/Gaurav-Gosain/jev-go) - Go client for TypeSafe.
- [ibrahemid/git-jev-stage](https://github.com/ibrahemid/git-jev-stage) - Select Git changes for staging with a plain-language description.
- [Stumble/jev-go](https://github.com/Stumble/jev-go) - Community Go SDK for TypeSafe AI Jev / System One.
- [tontoko/jev-browser](https://github.com/tontoko/jev-browser) - One grounded Jev/Playwright core: typed SDK, persistent CLI, and MCP server with native browser operations.
- [AboveColin/jevclient](https://github.com/AboveColin/jevclient) - Async Python client for TypeSafe Jev. Typed questions in, probabilities and choices out, no prose to parse.
- [AkashPriyadarshii/jev-scout](https://github.com/AkashPriyadarshii/jev-scout) - Zero-hallucination open-source repo and crate scout powered by TypeSafe AI Jev System One scoring.
- [AkashPriyadarshii/jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers) - Systematic software development framework for AI coding agents upgraded with TypeSafe Jev System One typed.
- [anilsenay/jev](https://github.com/anilsenay/jev) - Unofficial Go client for TypeSafe&#x27;s System One API and its model, Jev.
- [felpsdev/jev-classifier](https://github.com/felpsdev/jev-classifier) - Local tool-routing classifier for coding agents, with a gateway, MCP integrations, and decision logs.
- [himomohi/aside-jev](https://github.com/himomohi/aside-jev) - Aside agents decide with TypeSafe Jev (System One: Choice/Score/Noul). Not a Cua binding — Jev is the model.
- [StefanoITA/ts-jev-cost-calculator](https://github.com/StefanoITA/ts-jev-cost-calculator) - Unofficial CLI + Python estimator of tokens, cost and context limits for TypeSafe (System One / Jev) API.
- [zhirschtritt/typesafe-go](https://github.com/zhirschtritt/typesafe-go) - Idiomatic Go SDK for the TypeSafe AI API.
- [33Audits/jev-auto](https://github.com/33Audits/jev-auto) - Per-turn model routing for Claude Code. Cheapest tier that can do the job, no API key required, and it.
- [acharyaanusha/magic-jev](https://github.com/acharyaanusha/magic-jev) - A Magic Jev (8) Ball for pull requests.
- [auggie246/dsh-jev](https://github.com/auggie246/dsh-jev) - Jev integration to Deepseek harness.
- [brnyxx/jev-ra](https://github.com/brnyxx/jev-ra) - Browser use for coding agents, 3-5x faster than browser-use. MCP server + CLI; TypeSafe Jev decides every.
- [david1gp/jev](https://github.com/david1gp/jev) - Result-based TypeSafe System One client library and jev command-line interface.
- [edwardyen724-g/jev-compactor](https://github.com/edwardyen724-g/jev-compactor) - jev-compactor: deterministic context compaction + safety gating for AI agents, powered by TypeSafe.
- [krw82/jev-playwright-mcp](https://github.com/krw82/jev-playwright-mcp) - Jev-augmented Playwright MCP proxy — page-state triage, prompt-injection shielding, goal-based snapshot.
- [Kushwho/jev-codes](https://github.com/Kushwho/jev-codes) - Audit your git diff against YAML coding-standards packs using TypeSafe.
- [mhmdkzr/jev](https://github.com/mhmdkzr/jev) - An unofficial Go client for TypeSafe&#x27;s System One Jev model.
- [model-clis/jev](https://github.com/model-clis/jev) - Typed judgment CLI for the Jev model (TypeSafe System One): state + questions in, calibrated answers and exit.
- [MrDiamondBallz/jev-agent-integration](https://github.com/MrDiamondBallz/jev-agent-integration) - Provider-neutral Jev decision primitives for AI agents, with a native Hermes plugin and portable Agent Skill.
- [nandansrikrishna/jev-agent-tool](https://github.com/nandansrikrishna/jev-agent-tool) - Bring-your-own-key CLI, Python API, and MCP server for typed judgments with TypeSafe Jev.
- [nandansrikrishna/jev-go](https://github.com/nandansrikrishna/jev-go) - Standalone Go CLI and MCP server for TypeSafe Jev: typed judgments, JSONL evaluation, and resumable batches.
- [nekowasabi/jev-routing](https://github.com/nekowasabi/jev-routing) - Go Jev harness for Claude Code, Codex, and Grok Build. No npx. Not an MCP server.
- [okooo5km/jev](https://github.com/okooo5km/jev) - Typed decisions from the shell: an unofficial stdlib-Python CLI and Agent Skill for TypeSafe.
- [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) - Pre-alpha PostgreSQL extension for TypeSafe AI (Jev) categorical classification.
- [pithings/advocaat](https://github.com/pithings/advocaat) - A small, type-safe client for asking AI questions about your data, powered by TypeSafe Jev.
- [obie/ruby_decision_model](https://github.com/obie/ruby_decision_model) - Ruby client for decision models such as Typesafe Jev.
- [Brainwires/jevwire](https://github.com/Brainwires/jevwire) - Jev decision layer for agents: MCP server, embeddable DecisionModel library, and an escalate-only Claude Code.
- [y0usaf/typesafe-cli](https://github.com/y0usaf/typesafe-cli) - Ask Jev typed questions from the shell: noul, choice, and score answers as numbers, not prose.
- [geilt/typesafe-cli](https://github.com/geilt/typesafe-cli) - CLI and agent skill for TypeSafe System One (Jev): typed Choice, Score, and Noul judgments.
- [gilljon/typesafe-ai-rs](https://github.com/gilljon/typesafe-ai-rs) - Independent async and blocking Rust SDK for the TypeSafe AI System One API.

</details>

<a id="agent-tooling"></a>

## एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट

सबसे तेज़ी से बढ़ती श्रेणी: हुक, MCP सर्वर और गेट, जो एजेंट की अगली कार्रवाई से पहले एक टाइप्ड निर्णय रखते हैं।

<details>
<summary><b><a href="https://github.com/tamaratran/fast-jev-compaction">tamaratran/fast-jev-compaction</a></b> — ⭐3417 · TypeScript · observed · 0 天 · ⭐+107</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · MIT · tamaratran

##### डेटा

स्टार **3417** (+107) · फ़ॉर्क 175 · खुले इश्यू 45 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

> Replaces a coding agent's context-compaction summary with a typed decision. A clean example of swapping one LLM call in an existing pipeline rather than rebuilding the pipeline.

<sub>कोड में प्रयुक्त पाया गया: `src/request.ts`, `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/gargpratyush/jev-router">gargpratyush/jev-router</a></b> — ⭐149 · JavaScript · inferred · 0 天 · ⭐+5</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · gargpratyush

##### डेटा

स्टार **149** (+5) · फ़ॉर्क 6 · खुले इश्यू 6 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Route to the cheapest model in claude code for your task using jev-router

> Routes each turn to the cheapest model that can handle it. The canonical cost-reduction use case for a System One model.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gargpratyush--jev-router/361cf042aa7f2e59.png" width="100%" alt="gargpratyush/jev-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/0xNatoshi/jev-codex-router">0xNatoshi/jev-codex-router</a></b> — ⭐49 · Python · inferred · 1 天 · ⭐+3</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · Python · MIT · 0xNatoshi

##### डेटा

स्टार **49** (+3) · फ़ॉर्क 5 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Per-turn model & reasoning routing for Codex, driven by Jev (TypeSafe System One): picks the model, thinking depth and speed mode for every turn.

> Per-turn model and reasoning-effort routing for a coding agent, driven by typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/dbreunig/building-with-jev-skill">dbreunig/building-with-jev-skill</a></b> — ⭐105 · observed · 1 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · dbreunig

##### डेटा

स्टार **105** (+1) · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A skill for writing and improving programs that call Jev, TypeSafe's System One model

> A skill for writing programs that call Jev, rather than a program that calls Jev. The distinction matters: it encodes the design rules, not one implementation of them.

</details>

<details>
<summary><b><a href="https://github.com/GhalebDweikat/winnow">GhalebDweikat/winnow</a></b> — ⭐17 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · GhalebDweikat

##### डेटा

स्टार **17** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A calibrated context sieve for Claude Code: every tool result is judged by a System One model before it enters context.

</details>

<details>
<summary><b><a href="https://github.com/valentynkit/awesome-jev-typesafe">valentynkit/awesome-jev-typesafe</a></b> — ⭐8 · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · CC0-1.0 · valentynkit

##### डेटा

स्टार **8** · फ़ॉर्क 4 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Typed decisions with TypeSafe's Jev, the first System One model

</details>

<details>
<summary><b><a href="https://github.com/carlaiau/jev-reranking">carlaiau/jev-reranking</a></b> — ⭐7 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · carlaiau

##### डेटा

स्टार **7** · फ़ॉर्क 1 · खुले इश्यू 6 · बनाया गया 2026-03-13 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Search engine experimentation on the TREC collections. Currently focused on zero-shot reranking implementations with typesafe.ai's JEV model

</details>

<details>
<summary><b><a href="https://github.com/kraayenjon/awesome-jev">kraayenjon/awesome-jev</a></b> — ⭐7 · observed · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · NOASSERTION · kraayenjon

##### डेटा

स्टार **7** (+1) · फ़ॉर्क 1 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

A curated list of Jev use cases, projects, SDKs, and resources. Jev is TypeSafe AI's System One model for fast, typed decisions in software — Choice, Score, and Noul with calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/jodan-alberts/sokit">jodan-alberts/sokit</a></b> — ⭐2 · Python · observed · 1 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · jodan-alberts

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A harness to allow users to build agents using System One models.

</details>

<details>
<summary><b><a href="https://github.com/rajdhakad9826/routeKit">rajdhakad9826/routeKit</a></b> — ⭐2 · TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · MIT · rajdhakad9826

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Agent-native LLM model router built with JEV by TypeSafe.ai. Dynamically selects the most suitable model based on task complexity, reasoning requirements, and tool usage.

</details>

<details>
<summary><b><a href="https://github.com/BYK/jev-mcp">BYK/jev-mcp</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · MIT · BYK

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

An eval-first MCP server for TypeSafe's Jev, a System One model that returns typed judgments (noul, choice, score) with probabilities instead of generated text.

</details>

<details>
<summary><b><a href="https://github.com/emirbartu/opencode-system-one">emirbartu/opencode-system-one</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · emirbartu

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Opencode plugin using Jev (system one model) as part of software development process. Not affiliated with Opencode team.

</details>

<details>
<summary><b><a href="https://github.com/24601/Augustus">24601/Augustus</a></b> — Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · 24601

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Agent skill: design judgment-assisted systems with TypeSafe Jev (System One). Maps Choice/Score/Noul onto decision theory, reranking, and routing. Composition algebra, question design, validation gates. MIT.

</details>

<details>
<summary><b><a href="https://github.com/codaaiteam/jev-mcp">codaaiteam/jev-mcp</a></b> — JavaScript · observed · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · JavaScript · MIT · codaaiteam

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

MCP server for Jev (TypeSafe AI's System One model) — give any agent typed, calibrated decisions: classify, score, check, gate risky tool calls. Try free: jevtypesafeai.com

</details>

<details>
<summary><b><a href="https://github.com/codaaiteam/jev-typesafe-ai">codaaiteam/jev-typesafe-ai</a></b> — observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · codaaiteam

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Unofficial developer notes & examples for Jev, TypeSafe AI's System One model. Try it free: jevtypesafeai.com

</details>

<details>
<summary><b><a href="https://github.com/CrowBe/weave">CrowBe/weave</a></b> — TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · CrowBe

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Agent Harness for System One model

</details>

<details>
<summary><b><a href="https://github.com/gorock007/jev-atlas">gorock007/jev-atlas</a></b> — TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · MIT · gorock007

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

An independent, evidence-first field guide to Jev (TypeSafe AI's System One model) — for people and for coding agents. Not affiliated with TypeSafe AI.

</details>

<details>
<summary><b><a href="https://github.com/jms-dcksn/uipath-jev-guardrail-connector">jms-dcksn/uipath-jev-guardrail-connector</a></b> — JavaScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · JavaScript · jms-dcksn

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

UiPath bring-your-own-guardrail connector backed by the TypeSafe Jev System One model: plain-language agent policies enforced as calibrated probabilities.

</details>

<details>
<summary><b><a href="https://github.com/knowlet/jev-agentworld-web-simulator">knowlet/jev-agentworld-web-simulator</a></b> — TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · TypeScript · MIT · knowlet

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

An entire internet — search, pages & links — hallucinated on the fly by the System One Model.

</details>

<details>
<summary><b><a href="https://github.com/Wany-i/jev-decision-layer">Wany-i/jev-decision-layer</a></b> — Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · Wany-i

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

把决策模型（typesafe/jev-1.13，经 OpenRouter 的 decisions 端点调用）封装成业务决策工具：注册表驱动，带置信度门控与硬约束。非官方项目。

</details>

<details>
<summary><b><a href="https://github.com/yousudip/lizard-agent">yousudip/lizard-agent</a></b> — Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `observed` · Python · MIT · yousudip

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A browser agent with no LLM in the loop — deterministic code plus Jev, a System One model. ~118ms per decision, typed and auditable.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/yousudip--lizard-agent/f935c68cb397b142.png" width="100%" alt="yousudip/lizard-agent screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/devagrawal09/jev-review">devagrawal09/jev-review</a></b> — ⭐279 · TypeScript · inferred · 2 天 · ⭐+4</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · devagrawal09

##### डेटा

स्टार **279** (+4) · फ़ॉर्क 14 · खुले इश्यू 2 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A staged code-review workflow and local dashboard built with TypeSafe Jev.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/devagrawal09--jev-review/e441606238d500fd.png" width="100%" alt="devagrawal09/jev-review screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/fatwang2/awesome-jev">fatwang2/awesome-jev</a></b> — ⭐126 · JavaScript · inferred · 0 天 · ⭐+6</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · JavaScript · MIT · fatwang2

##### डेटा

स्टार **126** (+6) · फ़ॉर्क 14 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A source-backed Jev project directory with a reusable Jev-only GitHub review workflow.

</details>

<details>
<summary><b><a href="https://github.com/NiazMorshed2007/jev-review">NiazMorshed2007/jev-review</a></b> — ⭐125 · TypeScript · inferred · 1 天 · ⭐+2</summary>

##### बुनियादी तथ्य

`एजेंट उपकरण: MCP, हुक, गेट और कोडिंग एजेंट` · समुदाय · `inferred` · TypeScript · MIT · NiazMorshed2007

##### डेटा

स्टार **125** (+2) · फ़ॉर्क 9 · खुले इश्यू 2 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Local-first MCP plugin for continuous software-quality review by AI coding agents, powered by Jev.

> Local-first MCP plugin for continuous code review. Representative of the fastest-growing category in this list: a typed decision placed in front of an agent's next action.

</details>

<details>
<summary><b>इस श्रेणी में और</b> <sub>· 123</sub></summary>

- [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) - 5–10x faster browser operations: Jev clicks, Codex thinks and verifies. Built at EZCollegeApp.
- [vinilana/jev-eval-agent](https://github.com/vinilana/jev-eval-agent)
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) - Fast, cheap, typed judgments from TypeSafe&#x27;s Jev model, as MCP tools.
- [y0usaf/pi-jev](https://github.com/y0usaf/pi-jev) - TypeSafe Jev as a decision layer for the Pi coding agent: a measured tool-call gate plus jev_ask for typed.
- [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) - Camera-only autonomous drone in MuJoCo with a small judgment model (TypeSafe Jev) in the loop at 2.5Hz.
- [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) - Awesome Jev: source-backed open-source ecosystem radar, plain-language project discovery, and automatic.
- [supercorp-ai/supercov](https://github.com/supercorp-ai/supercov) - Code quality and coverage for coding agents.
- [shantanugoel/ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill) - Skill for Hermes, and other agents, to ask typesafe&#x27;s jev.
- [kbhuw/jev-sift](https://github.com/kbhuw/jev-sift) - Classify first. Read selectively. A portable agent plugin and MCP tool for batch text classification.
- [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner) - Claude Code plugin: trim long Bash output with TypeSafe Jev before the model sees it.
- [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter) - A lightweight Jev-powered router for models, tools, and subagents.
- [DanRWilloughby/snifftest](https://github.com/DanRWilloughby/snifftest) - A prose linter that sniffs out AI writing tells. Zero dependencies, countable rules plus one judgment model.
- [TheoOliveira/pi-jev](https://github.com/TheoOliveira/pi-jev) - Semantic tool routing and typed System One decisions for the Pi coding agent using TypeSafe Jev.
- [compozy/yoshi](https://github.com/compozy/yoshi) - Context-pruning proxy for Claude Code and Codex: Jev judges which history is still needed, measured not.
- [jomatsu/pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) - Jev (TypeSafe System One) backed auto mode for the Pi coding agent: semantically auto-approves bash, write.
- [blakestone-x/jev-mcp](https://github.com/blakestone-x/jev-mcp) - MCP server for TypeSafe Jev: typed classify, score, check, match and screen for any agent, with confidence on.
- [huntedman/JevLint](https://github.com/huntedman/JevLint) - Configurable semantic linting powered by Jev, with file-level NOUL judgments and a magic-strings plugin.
- [DECRUX9812/typesafe-skill-router](https://github.com/DECRUX9812/typesafe-skill-router) - TypeSafe (Jev) skill routing for Hermes Agent: names the one skill worth loading, before the model call.
- [devagrawal09/jev-code](https://github.com/devagrawal09/jev-code) - Bounded TypeSafe Jev workflows for coding agents.
- [matthewp/flue-jev-demo](https://github.com/matthewp/flue-jev-demo) - Flue agent routing with TypeSafe Jev through Cloudflare AI Gateway.
- [GodsBoy/jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router) - Typed, confidence-aware agent skill routing with TypeSafe Jev.
- [inanna-malick/jev-dsl](https://github.com/inanna-malick/jev-dsl) - Agent-first Haskell DSL for TypeSafe.
- [Zaious/jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) - Independent, evidence-based map of when TypeSafe.
- [anpicasso/hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals) - PoC: TypeSafe Jev as the reviewer for Hermes Agent smart command approvals. 8.7x faster, 4.4x fewer prompts.
- [GiesN/typesafe-jev-workflow](https://github.com/GiesN/typesafe-jev-workflow)
- [runta-dev/jot](https://github.com/runta-dev/jot) - The first general-purpose System One agent for Jev.
- [anandi1989/awesome-jev-usecases](https://github.com/anandi1989/awesome-jev-usecases) - Evidence-backed index of real-world Jev (TypeSafe AI System One) use cases, cookbook, how-to, repos.
- [rashedInt32/jev-mcp](https://github.com/rashedInt32/jev-mcp) - MCP server exposing TypeSafe Jev as typed, calibrated judgment tools: classify, score, check, batched ask.
- [SeeAPI/awesome-jev-use-cases](https://github.com/SeeAPI/awesome-jev-use-cases) - Explore real-world use cases and projects built with TypeSafe AI.
- [buluoray/JevOnly](https://github.com/buluoray/JevOnly) - Pure Jev that can &quot;type&quot; and drive towards task completion.
- [caiovicentino/jev-shield](https://github.com/caiovicentino/jev-shield) - Semantic MCP firewall powered by Jev — screens every tool call, tool result, and tool description with.
- [CrowdLinker/JevPromptCoach](https://github.com/CrowdLinker/JevPromptCoach) - Claude Code plugin that scores how well you prompt a coding agent, and shows whether your habits are.
- [jcpsimmons/jev-model-router-demo](https://github.com/jcpsimmons/jev-model-router-demo) - Throwaway Jev demo: route coding tasks to Grok Build or Codex Astra.
- [molis-ai/jev-workbench](https://github.com/molis-ai/jev-workbench) - Build versioned judgment functions on TypeSafe.
- [MongLong0214/jev-gate](https://github.com/MongLong0214/jev-gate) - Not every coding task needs your best model. Experimental Jev-powered model routing for Claude Code — V3.
- [morcoan/JevSeek](https://github.com/morcoan/JevSeek) - A local coding workspace pairing Jev action routing with DeepSeek argument generation. Native tools.
- [noetion/dsh-jev](https://github.com/noetion/dsh-jev) - DSH bundle that registers jev_ask for TypeSafe Jev noul, choice, and score answers.
- [ranjan2829/AskJev](https://github.com/ranjan2829/AskJev) - AskJev — Jev autopilot for any website + guard on irreversible clicks (TypeSafe System One, not Claude).
- [Saik0s/diffusiongemma-jev-macos](https://github.com/Saik0s/diffusiongemma-jev-macos) - Local JEV-style decisions with DiffusionGemma on Apple Silicon, with benchmarks and coding-agent examples.
- [samtay32/jev-system-architect](https://github.com/samtay32/jev-system-architect) - System-architecture skill for TypeSafe AI Jev/System One — find fuzzy semantic judgment and turn it into.
- [abhishekashokvkumar/jev-mcp-dispatcher](https://github.com/abhishekashokvkumar/jev-mcp-dispatcher) - Natural-language MCP tool dispatcher powered entirely by TypeSafe.
- [bestagentkits/jev-skillful](https://github.com/bestagentkits/jev-skillful) - Per-prompt capability router for coding agents: resolves installed skills, MCP servers, agents and commands.
- [Dharundp6/jev-carryforward](https://github.com/Dharundp6/jev-carryforward) - What your last session knew, scored against what this one is doing. MCP server: a per-project ledger written.
- [Friedjof/jev-mobile](https://github.com/Friedjof/jev-mobile) - Fast structured Android control loops with TypeSafe Jev and Mobile MCP.
- [hamakyo/jev-starter](https://github.com/hamakyo/jev-starter) - Typed, policy-driven decision workflows on top of TypeSafe AI Jev: confidence routing, fallbacks, evaluation.
- [integrate-your-mind/jev-codex-plugin](https://github.com/integrate-your-mind/jev-codex-plugin) - Open-source Codex plugin for TypeSafe Jev decision consultation, failure diagnosis, and evidence-based.
- [jcressler/fast-jev-compaction-codex](https://github.com/jcressler/fast-jev-compaction-codex) - Task-aware Jev evidence selection and exact local recovery around native Codex compaction.
- [khordoo/jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab) - Multi-drone autonomy lab demonstrating TypeSafe Jev reflex decisions with optional System 2 strategy guidance.
- [nrdz-labs/fast-jev-opencode](https://github.com/nrdz-labs/fast-jev-opencode) - Jev-scored context pruning for OpenCode: drops stale tool calls and truncates bulky results on the outgoing.
- [omni-/ask-jev](https://github.com/omni-/ask-jev) - Utilizing Jev, the RLCD-type model provided by TypeSafe AI, to independently and cheaply judge agentic coding.
- [poponline63/hermes-jev-north-star](https://github.com/poponline63/hermes-jev-north-star) - Hermes Agent skill whose north-star gate is judged by Jev (TypeSafe System One): turn an intention into a.
- [Ravinder82/jev-flash-router](https://github.com/Ravinder82/jev-flash-router) - open-sourced jev-flash-router: an MCP server for TypeSafe.
- [rthomas24/jev-realtime-trading](https://github.com/rthomas24/jev-realtime-trading) - Paper trading agents on a live tape, decided every second by TypeSafe.
- [Wang-auspicious/codex-jev-compaction](https://github.com/Wang-auspicious/codex-jev-compaction) - Jev-powered context curation for Codex. Build compact, traceable handoff context through native plugins and.
- [wotai-dev/typesafe-jev-tools](https://github.com/wotai-dev/typesafe-jev-tools) - A Claude Code hook that asks whether the decision you are writing needs a model at all. Includes a measured.
- [0x7067/claude-jev](https://github.com/0x7067/claude-jev)
- [altregubov/jev-antigravity-mcp](https://github.com/altregubov/jev-antigravity-mcp)
- [alviso/jev-precheck](https://github.com/alviso/jev-precheck) - A second signature on every write an AI agent makes into a system of record. MCP proxy: fetch the records.
- [andyholst/hermes-typesafe-jev](https://github.com/andyholst/hermes-typesafe-jev) - TypeSafe Jev MCP server for Hermes Agent — Choice, Noul, Score as first-class tools.
- [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) - Jev (TypeSafe) vs Claude Haiku 4.5 on 2 000 phishing emails: accuracy, calibration, latency, cost.
- [AntonioCoppe/openclaw-jev-harness](https://github.com/AntonioCoppe/openclaw-jev-harness) - OpenClaw plugin: jev-harness DecisionHarness as System One decide layer (policy/confidence/shadow).
- [AStheTECH/mewcp-jev](https://github.com/AStheTECH/mewcp-jev) - JEV MCP server by MewCP.
- [bidurkhatri/jev-mcp-lab](https://github.com/bidurkhatri/jev-mcp-lab)
- [buberlo/dsh-jev](https://github.com/buberlo/dsh-jev) - Jev-powered decision layer for DeepSeek Harness.
- [cbruyndoncx/AskJev-MCP](https://github.com/cbruyndoncx/AskJev-MCP) - MCP server for TypeSafe.
- [dizk/pi-jev-lens](https://github.com/dizk/pi-jev-lens) - pi extension that compresses large tool results before they reach the model: jev picks the view, full text.
- [DoGMaTiiC/hermes-jev](https://github.com/DoGMaTiiC/hermes-jev) - Hermes Agent plugin: route each turn to the one skill that fits, via TypeSafe Jev on the Vercel AI Gateway.
- [duketopceo/jev-compact](https://github.com/duketopceo/jev-compact) - Moving-highlight context compaction for agent harnesses — Jev-scored span retention, tombstone restore via MCP.
- [EtienneLescot/jev-router](https://github.com/EtienneLescot/jev-router) - Typed judgments in, control flow out: two Jev calls route a support ticket to an agent, then pick its model.
- [fast-facts/jev-mcp](https://github.com/fast-facts/jev-mcp)
- [flaviusapop/jev-router](https://github.com/flaviusapop/jev-router) - Routes each turn in Claude Code, Codex, Grok and opencode to the cheapest model and reasoning depth that can.
- [gzawadzki/jev-usecases](https://github.com/gzawadzki/jev-usecases) - TypeSafe Jev demos: Play inbox, Czajka guard, agent-card router, seed comparator, RL data triage.
- [hamakyo/jev-mahjong-bench](https://github.com/hamakyo/jev-mahjong-bench) - Reproducible riichi mahjong benchmark for Jev, GPT, Mortal, and hybrid agents using MJAI and RiichiEnv.
- [hangarbay/jev.mcp](https://github.com/hangarbay/jev.mcp) - One MCP server for TypeSafe&#x27;s Jev: typed, calibrated decisions instead of generated text.
- [its-panzer/jev-model-router](https://github.com/its-panzer/jev-model-router) - A policy router that picks the cheapest Claude model that can finish the job.
- [itsaslamopenclawdata/GrowthCompany_JevOutputs](https://github.com/itsaslamopenclawdata/GrowthCompany_JevOutputs) - Jev (TypeSafe System One) x Hermes Agent - the calibrated decision-layer playbook: 5 end-to-end use cases.
- [jh1373/jev-search](https://github.com/jh1373/jev-search) - Search your Obsidian vault locally and offline with no API key, then rerank the top results with Jev only.
- [jimmyhealer/jev-semantic-explorer](https://github.com/jimmyhealer/jev-semantic-explorer) - Stop grepping. Ask a repo where behavior is enforced. One MCP tool for coding agents.
- [jmanhype/jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab) - Reproducible calibration and selective-risk benchmarks for Jev/TypeSafe decisions in DSPy workflows.
- [jms-dcksn/jev-pii-guardrail](https://github.com/jms-dcksn/jev-pii-guardrail) - A UiPath coded agent with a custom PII detection guardrail on the LLM boundary, built on the TypeSafe Jev.
- [JoacoMarc/jev-harness-router](https://github.com/JoacoMarc/jev-harness-router) - Per-turn harness router on Jev (TypeSafe): one batched call picks the model tier, tools, skill and effort.
- [juanlentino/jev-comment-analysis](https://github.com/juanlentino/jev-comment-analysis) - Backs the WordPress AI plugin&#x27;s Comment Moderation with TypeSafe Jev, through Connector for TypeSafe Jev.
- [juanlentino/jev-connector](https://github.com/juanlentino/jev-connector) - WordPress connector for the TypeSafe System One API (Jev): typed questions, confidence-scored answers, core.
- [jxu-dev-c/jev-adaptive-thinking](https://github.com/jxu-dev-c/jev-adaptive-thinking) - CLIProxyAPI plugin for Jev-powered session model routing with local debug logs.
- [kaijia323/dsh-plugin-jev](https://github.com/kaijia323/dsh-plugin-jev) - TypeSafe Jev (System One decision model) as a native jev_decide tool plugin for DeepSeek Harness.
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) - Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents.
- [kindintelligence/jev-rust-review](https://github.com/kindintelligence/jev-rust-review) - Rust-aware code review for Claude Code and coding agents, powered by TypeSafe Jev.
- [kuldeepsinh19/jev-decision-gateway](https://github.com/kuldeepsinh19/jev-decision-gateway) - A provider-agnostic AI decision gateway using TypeSafe AI.
- [litshing/hermes-jev-plugins](https://github.com/litshing/hermes-jev-plugins) - Two Hermes Agent plugins that prune the context window and gate permanent memory with cheap System One (Jev).
- [luw2007/omp-jev-extensions](https://github.com/luw2007/omp-jev-extensions) - OMP / pi-coding-agent extensions that delegate acceptance gating and subagent routing to the Typesafe Jev.
- [MahmoudAdelbghany/jev-browser](https://github.com/MahmoudAdelbghany/jev-browser) - Jev-powered browser MCP for LLM agents — ~300ms decisions, no LLM tokens in the loop. Benchmark vs Playwright.
- [Mandrilsquad1441/jev-model-router](https://github.com/Mandrilsquad1441/jev-model-router) - Pick the best AI model and reasoning effort for any task in ~1s. Plugin for Claude Code, Claude Desktop and.
- [marcAllari/jev-mcp-router](https://github.com/marcAllari/jev-mcp-router)
- [micic-mihajlo/jev-tool-runner](https://github.com/micic-mihajlo/jev-tool-runner) - Jev selects developer tools; Codex handles code. MCP and Jev-first execution with measured benchmarks.
- [minhgv/jev-mcp](https://github.com/minhgv/jev-mcp) - TypeSafe Jev MCP decision layer for coding agents and CI.
- [mjyoke1111/jev-lab](https://github.com/mjyoke1111/jev-lab) - Real browser-agent safety evaluation: Jev versus a baseline on benign and injected tasks.
- [MSalvalaggio/jev-reflex](https://github.com/MSalvalaggio/jev-reflex) - Claude thinks, Jev reacts: an MCP server that hands browser tasks from Claude to TypeSafe.
- [nekowasabi/jev-routing-mcp](https://github.com/nekowasabi/jev-routing-mcp)
- [Nyarlathoteppppp/pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context) - Cache-neutral context trimming for the pi coding agent, powered by TypeSafe Jev: long tool output cut to.
- [Panebianco00/jev-claude](https://github.com/Panebianco00/jev-claude) - Route Claude Code.
- [pedroknigge/mcp_jev](https://github.com/pedroknigge/mcp_jev) - Open MCP server to run TypeSafe Jev (System One) packs locally — Choice / Noul / Score for Cursor &amp; agents.
- [Pinutss/jev-mcp-router](https://github.com/Pinutss/jev-mcp-router) - Select relevant MCP tools under a context-token budget, without executing them.
- [Pinutss/jev-memory-selector](https://github.com/Pinutss/jev-memory-selector) - Filters an agent&#x27;s memories to fit a token budget. Local, HTTP, MCP, Docker.
- [Pinutss/jev-plugins](https://github.com/Pinutss/jev-plugins) - Cursor and Hermes marketplace for the four published JEV Labs routers.
- [planstack-ai/jev-tetris-benchmark](https://github.com/planstack-ai/jev-tetris-benchmark) - Reproducible Tetris decision benchmark comparing TypeSafe Jev with Claude Haiku.
- [raj8525/universal-jev](https://github.com/raj8525/universal-jev) - Universal TypeSafe Jev Runtime Plugin &amp; MCP Server for Coding Agents.
- [rubichandrap/hermes-jev-guard](https://github.com/rubichandrap/hermes-jev-guard) - Hermes shell hooks: Jev-based route hint, tool-risk gate, and done-check.
- [sebastianbugal/jev](https://github.com/sebastianbugal/jev) - TypeSafe.
- [sypherin/jev-trace-classifier](https://github.com/sypherin/jev-trace-classifier) - Application of TypeSafe Jev (noul judgment primitive) on the collusion.wiki corpus: agent vs human page.
- [tgiridhar/claude-code-jev-smart-router](https://github.com/tgiridhar/claude-code-jev-smart-router) - HTTP proxy for Claude Code that selects the Claude model per request to cut cost and latency. Routes on task.
- [thanh-abaii/ud-jev-decision-workflow](https://github.com/thanh-abaii/ud-jev-decision-workflow)
- [themsquared/jev-benchmark](https://github.com/themsquared/jev-benchmark) - Reproducible benchmark for TypeSafe AI.
- [thevibeworks/awesome-typesafe-jev](https://github.com/thevibeworks/awesome-typesafe-jev) - Curated list of projects built on TypeSafe.
- [thumay9700/jev-plays](https://github.com/thumay9700/jev-plays) - Autonomous game agent powered by TypeSafe AI&#x27;s Jev (System One decision engine), starting with Pokémon Red.
- [trietphan/jev-claw](https://github.com/trietphan/jev-claw) - Typed model routing for OpenClaw agents, powered by TypeSafe Jev.
- [ussyverse/hermes-jev-router](https://github.com/ussyverse/hermes-jev-router) - Experimental Hermes plugin: Jev-assisted model routing plans with budget and capability constraints. API.
- [vinilana/jev-gateway-bench](https://github.com/vinilana/jev-gateway-bench) - Benchmark for jev-gateway: real coding agents on chess engine tasks, with Jev routing on and off.
- [yangzhou-chaofan/awesome-jev-prompt](https://github.com/yangzhou-chaofan/awesome-jev-prompt) - latest top 100 showcases for jev (keep updating) from x / github / latest sources.
- [yottayoshida/jev-sscope](https://github.com/yottayoshida/jev-sscope) - Watch a Claude Code session while it runs, scored step by step by Jev on Cloudflare Workers AI.
- [zhangxaochen/dsh-jev](https://github.com/zhangxaochen/dsh-jev) - Jev (System One decision model) plugin suite for DeepSeek Harness (dsh).
- [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden) - Guardrails for Pi built on pi-typesafe that steer the agent instead of interrupting you: Jev judges.
- [HyunjunJeon/pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask) - TypeSafe Jev as the pi coding agent&#x27;s quiet decision layer.
- [3clyp50/a0-typesafe-ai](https://github.com/3clyp50/a0-typesafe-ai) - TypeSafe AI Jev judgments for Agent Zero, with typed tools and probability cards.

</details>

<a id="routing-guardrails"></a>

## रूटिंग, गार्डरेल और अनुमोदन

प्रोडक्शन जैसा उपयोग: हर अनुरोध उसी सबसे सस्ते मॉडल को भेजें जो उसे वास्तव में संभाल सके, और परिणाम पर एक नियतात्मक जाँच बनाए रखें।

<details>
<summary><b><a href="https://github.com/Dicklesworthstone/skillranker">Dicklesworthstone/skillranker</a></b> — ⭐50 · Rust · observed · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · Rust · NOASSERTION · Dicklesworthstone

##### डेटा

स्टार **50** (+1) · फ़ॉर्क 5 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Rust CLI powered by Jev from TypeSafe.ai that ranks agent skills for the next step using live session context. Includes Claude Code hooks, structured JSON, abstention, and local feedback. Requires a TypeSafe API key.

> Ranks agent skills with a typed decision. A useful model for any 'choose among N candidates' problem that was previously a prompt.

</details>

<details>
<summary><b><a href="https://github.com/Foadsf/jev-for-engineers">Foadsf/jev-for-engineers</a></b> — ⭐2 · Python · observed · 2 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · Python · MIT · Foadsf

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Eight minimal working examples of TypeSafe's Jev (a System One model) applied to mechanical and electrical engineering: CAD/CAE/CAM routing, FEM result triage, DFM screening, BOM alignment, hallucination-proof extraction. Zero dependencies.

</details>

<details>
<summary><b><a href="https://github.com/Justmalhar/awesome-jev-apps">Justmalhar/awesome-jev-apps</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · Python · MIT · Justmalhar

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Awesome Collection of apps built with Jev - a System One model

</details>

<details>
<summary><b><a href="https://github.com/qddegtya/qualm">qddegtya/qualm</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · TypeScript · MIT · qddegtya

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 3 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Typed decisions from a System One model, where uncertainty is something you have to handle.

</details>

<details>
<summary><b><a href="https://github.com/aniruddh-krovvidi/switchboard">aniruddh-krovvidi/switchboard</a></b> — Python · observed · 1 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · Python · aniruddh-krovvidi

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Guardrail + model router for LLM gateways on TypeSafe's Jev (System One model), with an independent accuracy/calibration/latency evaluation. Stdlib Python.

</details>

<details>
<summary><b><a href="https://github.com/chy4pro/JevBrowserExt">chy4pro/JevBrowserExt</a></b> — TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · TypeScript · MIT · chy4pro

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

⚡ Ultrafast browser automation Chrome Extension (Manifest V3) powered by TypeSafe Jev (TypeSafe.ai, OpenRouter, Cloudflare)

</details>

<details>
<summary><b><a href="https://github.com/lorensation/llm-cost-optimizer-jev">lorensation/llm-cost-optimizer-jev</a></b> — observed · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `observed` · Apache-2.0 · lorensation

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

An intelligent routing layer powered by TypeSafe AI's System One model Jev that sits in front of multiple LLM providers, analyzes each incoming request’s complexity, routes it to the cheapest model capable of handling it at acceptable quality, and continuously validates that routing decisions are correct.

</details>

<details>
<summary><b><a href="https://github.com/yusukebe/hono-jev-router">yusukebe/hono-jev-router</a></b> — ⭐29 · TypeScript · inferred · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · yusukebe

##### डेटा

स्टार **29** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Route HTTP requests by meaning. A semantic router for Hono powered by Jev.

> Semantic HTTP routing for Hono. A rare example of a typed decision used for infrastructure rather than for AI plumbing.

</details>

<details>
<summary><b><a href="https://github.com/brainstormity/Jev-Moderation-Bot">brainstormity/Jev-Moderation-Bot</a></b> — ⭐25 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · brainstormity

##### डेटा

स्टार **25** · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://github.com/vinilana/jev-gateway">vinilana/jev-gateway</a></b> — ⭐15 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · vinilana

##### डेटा

स्टार **15** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://github.com/mejiasd3v/pi-jev-router">mejiasd3v/pi-jev-router</a></b> — ⭐6 · JavaScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · MIT · mejiasd3v

##### डेटा

स्टार **6** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Automatic model routing for Pi using TypeSafe's Jev through Vercel AI Gateway

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/mejiasd3v--pi-jev-router/1ed89503e472633d.png" width="100%" alt="mejiasd3v/pi-jev-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/collapseindex/dinostomp">collapseindex/dinostomp</a></b> — ⭐5 · Python · inferred · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · NOASSERTION · collapseindex

##### डेटा

स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-08-09 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

A verification layer for AI evaluations. Checks the instrument, not just the score: data, scorer, runs, numbers, claims, and itself.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/collapseindex/dinostomp/main/data/exports/readme/20260915_120000_readme_pixel-dino_architecture_1200x850_s42.png" width="100%" alt="collapseindex/dinostomp screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/collapseindex/dinostomp/main/data/exports/readme/20260915_120000_readme_pixel-dino_1200x360_s42.gif" width="100%" alt="collapseindex/dinostomp animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/andrelandgraf/safer-with-jev">andrelandgraf/safer-with-jev</a></b> — ⭐3 · TypeScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · andrelandgraf

##### डेटा

स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Neon Function proxy for the Neon AI Gateway with TypeSafe Jev routing.

</details>

<details>
<summary><b><a href="https://github.com/keeltrace/hermes-jev">keeltrace/hermes-jev</a></b> — ⭐3 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · keeltrace

##### डेटा

स्टार **3** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Typed System One decisions, ranking, verification, and an opt-in Hermes tool gate using TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/maker-KK/todo-jev">maker-KK/todo-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · maker-KK

##### डेटा

स्टार **2** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

⚡ Ultra-fast, low-cost intelligent task classifier and 3-tier routing engine powered by TypeSafe Jev (System One)

</details>

<details>
<summary><b><a href="https://github.com/prismhq/jev-router">prismhq/jev-router</a></b> — ⭐2 · Python · inferred · 2 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · prismhq

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Open-source LLM router that uses TypeSafe's Jev to pick a model, on top of LiteLLM

</details>

<details>
<summary><b><a href="https://github.com/ufec/jev-block-android-ad">ufec/jev-block-android-ad</a></b> — ⭐2 · Kotlin · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Kotlin · MIT · ufec

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

JevNoiseGate filters unwanted notifications and SMS on Android. Rather than   matching keywords, an LLM decides what's noise — and only what it explicitly   flags is blocked. Verification codes are matched on-device and never uploaded;   anything uncertain passes through.

</details>

<details>
<summary><b><a href="https://github.com/vtrivedy/jev-plays-games">vtrivedy/jev-plays-games</a></b> — ⭐2 · JavaScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · JavaScript · vtrivedy

##### डेटा

स्टार **2** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Chess, Connect Four, and a decision model. Play Jev or watch Jev play itself.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/vtrivedy/jev-plays-games/main/docs/screenshots/chess.jpg" width="100%" alt="vtrivedy/jev-plays-games screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/WiktorB2004/llama-index-jev">WiktorB2004/llama-index-jev</a></b> — ⭐2 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · WiktorB2004

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

LlamaIndex reranker + router powered by TypeSafe Jev — typed scores/choices, cheaper than LLM-as-judge.

</details>

<details>
<summary><b><a href="https://github.com/Pinutss/jev-model-router">Pinutss/jev-model-router</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Python · MIT · Pinutss

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Route among multiple LLMs and multi-model provider keys without leaking secrets.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/pinutss--jev-model-router/85881d58b893c393.png" width="100%" alt="Pinutss/jev-model-router screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/Shashank-H/pi-jev-model-router">Shashank-H/pi-jev-model-router</a></b> — ⭐1 · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Shashank-H

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Model router for pi with Jev

</details>

<details>
<summary><b><a href="https://github.com/bitnovus/jev-spam-eval">bitnovus/jev-spam-eval</a></b> — Jupyter · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Jupyter · MIT · bitnovus

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Zero-shot spam filtering with TypeSafe Jev Noul questions, compared with TF-IDF baselines

</details>

<details>
<summary><b><a href="https://github.com/buberlo/jev-pastepilot">buberlo/jev-pastepilot</a></b> — TypeScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · TypeScript · MIT · buberlo

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Explicit paste-to-action launcher that routes text to useful tools without automatic side effects.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/buberlo--jev-pastepilot/f9f8b5633a938cb0.png" width="100%" alt="buberlo/jev-pastepilot screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/buberlo--jev-pastepilot/590a0f155ae53d69.gif" width="100%" alt="buberlo/jev-pastepilot animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/buberlo/jev-pastepilot/main/docs/demo/pastepilot-core.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/buyukcerci/jev-model-router">buyukcerci/jev-model-router</a></b> — inferred · 0 天</summary>

##### बुनियादी तथ्य

`रूटिंग, गार्डरेल और अनुमोदन` · समुदाय · `inferred` · Apache-2.0 · buyukcerci

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

A multi-provider LLM and media router featuring calibrated confidence classification, dynamic policy scoring, and automated fallback management.

</details>

<details>
<summary><b>इस श्रेणी में और</b> <sub>· 30</sub></summary>

- [carllippert/jev-router](https://github.com/carllippert/jev-router) - Express with no routes. TypeSafe Jev picks which handler runs.
- [ClemannD/jev-playground](https://github.com/ClemannD/jev-playground) - Interactive playground for learning how TypeSafe&#x27;s Jev model works (via Vercel AI Gateway).
- [da-vinci-noob/pi-jev-model-router](https://github.com/da-vinci-noob/pi-jev-model-router) - Route pi prompts to task-appropriate model tiers with TypeSafe Jev typed judgments. Budget-aware, with.
- [danielhirt/jev-lab](https://github.com/danielhirt/jev-lab) - Experiments on TypeSafe Jev (System One decision model) via OpenRouter: repeatability, perturbation, and LLM.
- [devjtv/jev-gate](https://github.com/devjtv/jev-gate)
- [gnoviawan/omp-jev-tools](https://github.com/gnoviawan/omp-jev-tools) - Native omp (oh-my-pi) extension: TypeSafe Jev judgment tools — token efficiency, confidence routing, citation.
- [hugo-alves/jev-router-playground](https://github.com/hugo-alves/jev-router-playground) - Interactive playground for testing Jev model-routing decisions against OpenRouter models.
- [iefnaf/pi-jev](https://github.com/iefnaf/pi-jev) - Pi extension suite powered by Jev: selective context compaction and model routing.
- [immanuelsavio/jev-experiment](https://github.com/immanuelsavio/jev-experiment) - Benchmarking TypeSafe Jev against general-purpose LLMs on support-ticket routing, with a focus on latency.
- [jolehuit/jev-downloads-sorter](https://github.com/jolehuit/jev-downloads-sorter) - A ~/Downloads folder that sorts itself: one Jev decision per file, launchd WatchPaths, no daemon.
- [kevin9327/jev-bot](https://github.com/kevin9327/jev-bot) - JevBot: TypeSafe Jev support bot. Choice+Score+Noul in, canned reply/escalate/block out. Not a chatbot.
- [Loule95450/jev-free-router](https://github.com/Loule95450/jev-free-router) - Dynamic per-turn model router on free OpenCode Zen + Go models (fork of gargpratyush/jev-router).
- [mcgalleg/grokbot-jev-jobs](https://github.com/mcgalleg/grokbot-jev-jobs) - Scores public job postings against my resume using TypeSafe.
- [meetr1912/jev-arena](https://github.com/meetr1912/jev-arena) - A calibration arena for TypeSafe Jev: reliability, Brier/ECE, and confidence-gated risk-coverage on.
- [meetr1912/jev-sonar](https://github.com/meetr1912/jev-sonar) - TypeSafe Jev plays Battleship: one ~100-question typed fan-out per turn returns a calibrated hit-probability.
- [MoonTory/pi-jev-harness](https://github.com/MoonTory/pi-jev-harness) - Pi extension: TypeSafe Jev routes turns, pre-fetches context, trims tool results, catches loops and guards.
- [octanevz/jev-playground-openrouter](https://github.com/octanevz/jev-playground-openrouter) - Local browser playground for TypeSafe&#x27;s Jev decision model via OpenRouter. Python stdlib only.
- [perixtar/jev-e2e](https://github.com/perixtar/jev-e2e) - Natural-language end-to-end tests for web apps, powered by Jev and Playwright.
- [rajivkuriakose/typesafe-jev-examples](https://github.com/rajivkuriakose/typesafe-jev-examples) - Worked examples for TypeSafe&#x27;s Jev System One decision model, runnable today through OpenRouter.
- [ravikadam/jev-loan-triage](https://github.com/ravikadam/jev-loan-triage) - Voice loan-call triage using TypeSafe Jev: intent, info sufficiency and a lending decision from typed AI.
- [rexbuilds/jev-triage](https://github.com/rexbuilds/jev-triage)
- [ryantsai/jev-llm-router](https://github.com/ryantsai/jev-llm-router)
- [SadiqOnGithub/jev-lab](https://github.com/SadiqOnGithub/jev-lab) - Live tests for TypeSafe Jev (System One) via OpenRouter&#x27;s Decisions API.
- [shivanathd/jev-playground](https://github.com/shivanathd/jev-playground) - BYOK playground for TypeSafe Jev (System One): Choice, Score, Noul examples for production gates.
- [ThyFriendlyFox/jev-triage](https://github.com/ThyFriendlyFox/jev-triage) - Active-learning triage pipeline using TypeSafe Jev — route by confidence, log soft labels for local.
- [TokenTrim/jev-routing-experiment](https://github.com/TokenTrim/jev-routing-experiment) - Benchmarking TypeSafe&#x27;s Jev decision model as a cost-efficient LLM router on RouterArena.
- [Zumka1991/jev-telegram-admin](https://github.com/Zumka1991/jev-telegram-admin) - AI moderator for Telegram groups powered by the Jev (TypeSafe System One) decision model.
- [iammrduncan/typesafe-ai-benchmark](https://github.com/iammrduncan/typesafe-ai-benchmark) - This is a LLM Gateway that mimics typesafe ai structured output. Like an imposter Jev.
- [kavehmz/typesafe-playground](https://github.com/kavehmz/typesafe-playground) - Interactive experiments with TypeSafe Jev, from support routing to 3D driving simulations with real AI.
- [raihankhan-rk/diffjury](https://github.com/raihankhan-rk/diffjury) - DiffJury — TypeSafe Jev PR risk router + code review coach.

</details>

<a id="evaluation"></a>

## मूल्यांकन, कैलिब्रेशन और बेंचमार्क

किसी को कैसे पता चले कि निर्णय अच्छे हैं। कैलिब्रेशन इस पारिस्थितिकी में खुला प्रश्न है, और ये परियोजनाएँ उसे मापती हैं।

<details>
<summary><b><a href="https://github.com/ikermoel/open-alternative-jev">ikermoel/open-alternative-jev</a></b> — ⭐5 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · Python · Apache-2.0 · ikermoel

##### डेटा

स्टार **5** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Open-source alternative to TypeSafe's Jev: a System One style model layer that gives typed, calibrated decisions from any open-weights LLM in one forward pass (HF + vLLM), with honest benchmarks

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ikermoel--open-alternative-jev/41dab050f73a168f.png" width="100%" alt="ikermoel/open-alternative-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hev/reranker">hev/reranker</a></b> — ⭐3 · Python · observed · 1 天 · ⭐+2</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · Python · Apache-2.0 · hev

##### डेटा

स्टार **3** (+2) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Use Jev (TypeSafe's System One model) as a calibrated reranker: one call, up to 30 documents, a probability per document. Apache-2.0.

</details>

<details>
<summary><b><a href="https://github.com/akash-kamat/system-one-gemma">akash-kamat/system-one-gemma</a></b> — ⭐1 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · Python · akash-kamat

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Open-source Jev-style System One decision model. Gemma 3 270M with a scoring head — fast, calibrated decisions in a single forward pass. No text generation. Inspired by TypeSafe.ai's Jev.

</details>

<details>
<summary><b><a href="https://github.com/edgardcham/huncho">edgardcham/huncho</a></b> — ⭐1 · TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · TypeScript · MIT · edgardcham

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Decisions as code on System One models: typed questions, thresholds with hysteresis, nested decisions, journal, calibration

</details>

<details>
<summary><b><a href="https://github.com/Gaurav-Gosain/jev-sec-bench">Gaurav-Gosain/jev-sec-bench</a></b> — ⭐1 · Go · observed · 2 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · Go · MIT · Gaurav-Gosain

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Blind security benchmarks for Jev, TypeSafe's System One model: prompt injection and vulnerable code detection, built on jev-go

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/gaurav-gosain--jev-sec-bench/9fea5be47ec5a43c.png" width="100%" alt="Gaurav-Gosain/jev-sec-bench screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moguone/jev-lab">moguone/jev-lab</a></b> — JavaScript · observed · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · JavaScript · MIT · moguone

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Small apps for evaluating TypeSafe AI's System One model (Jev). Unofficial.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/moguone--jev-lab/429935d7423aabcf.jpg" width="100%" alt="moguone/jev-lab screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/nishioka-shinji/jev-edgar">nishioka-shinji/jev-edgar</a></b> — Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `observed` · Python · nishioka-shinji

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Does Jev, a System One model returning calibrated probabilities, say anything useful about an earnings release before the market prices it?

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/jev-benchmarks">AbdelStark/jev-benchmarks</a></b> — ⭐8 · Python · inferred · 1 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · Apache-2.0 · AbdelStark

##### डेटा

स्टार **8** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Probability-aware evaluation for typed decision models: calibration, selective risk, latency, and reproducible benchmarks.

</details>

<details>
<summary><b><a href="https://github.com/Heman10x-NGU/Verdict-open-jev">Heman10x-NGU/Verdict-open-jev</a></b> — ⭐7 · Python · inferred · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · NOASSERTION · Heman10x-NGU

##### डेटा

स्टार **7** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Non-autoregressive decision engine on ModernBERT (151M) with calibrated uncertainty (RLCD), TypeSafe AI Jev benchmark audit, and in-browser WebGPU playground

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Heman10x-NGU/Verdict-open-jev/main/assets/how-jev-works.png" width="100%" alt="Heman10x-NGU/Verdict-open-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/abhixhek/jevcal">abhixhek/jevcal</a></b> — ⭐5 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · abhixhek

##### डेटा

स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Stop guessing confidence thresholds: calibrate, threshold, and drift-check typed decision models (TypeSafe Jev) against an LLM teacher.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abhixhek--jevcal/3dbe2307176737c8.png" width="100%" alt="abhixhek/jevcal screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/y0usaf/jev-lm">y0usaf/jev-lm</a></b> — ⭐5 · TypeScript · inferred · 2 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · TypeScript · MIT · y0usaf

##### डेटा

स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A word-level language model whose output layer is Jev: n-gram drafter, Noul chunk verification, bits-per-token eval

</details>

<details>
<summary><b><a href="https://github.com/cablehead/jev.nu">cablehead/jev.nu</a></b> — ⭐2 · Nushell · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Nushell · MIT · cablehead

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Nushell module for the TypeSafe System One API: typed decisions with calibrated probabilities

</details>

<details>
<summary><b><a href="https://github.com/wondertwins/jev-benchmark">wondertwins/jev-benchmark</a></b> — ⭐2 · Python · inferred · 2 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · wondertwins

##### डेटा

स्टार **2** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Benchmarks and a playground for TypeSafe's Jev (System One) model: chess, and who-is-the-player-talking-to for speech-to-text game NPCs

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/wondertwins--jev-benchmark/ebe9cbadbd7e6955.gif" width="100%" alt="wondertwins/jev-benchmark animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/4esv/jev-eval">4esv/jev-eval</a></b> — Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · 4esv

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Independent eval of TypeSafe Jev vs GPT-5.6 Terra: accuracy, calibration, latency, cost

</details>

<details>
<summary><b><a href="https://github.com/carson-sweet/jev-plays-brogue">carson-sweet/jev-plays-brogue</a></b> — TypeScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · TypeScript · AGPL-3.0 · carson-sweet

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

TypeSafe's Jev model plays the roguelike Brogue live -- a hand-built expert system for System-2 reasoning, outcome-calibrated self-learning, and a web UI to watch decisions, costs, and training progress.

</details>

<details>
<summary><b><a href="https://github.com/Danu28/pi-jev-harness">Danu28/pi-jev-harness</a></b> — TypeScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · TypeScript · MIT · Danu28

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Pure Jev System-One harness for Pi — pi-model tool-based calibrate + plan + git, zero deps, no fallback

</details>

<details>
<summary><b><a href="https://github.com/dnakhoa/jev-deferred-crispification">dnakhoa/jev-deferred-crispification</a></b> — TeX · inferred · 1 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · TeX · NOASSERTION · dnakhoa

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Position paper: the Hidden-Markov and fuzzy primitives missing from TypeSafe AI's Jev and System-One decision models. Two lemmas, one principle (Deferred Crispification), one architecture (BSF-S1).

</details>

<details>
<summary><b><a href="https://github.com/eggmasonvalue/jev-takes-mauboussin">eggmasonvalue/jev-takes-mauboussin</a></b> — Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · eggmasonvalue

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Evaluating TypeSafe's Jev on Michael Mauboussin's 50-question decision calibration test

</details>

<details>
<summary><b><a href="https://github.com/ickma2311/jev-baselines-eval">ickma2311/jev-baselines-eval</a></b> — Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · ickma2311

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Pre-registered independent eval of TypeSafe Jev against a nano-class LLM, a frontier LLM, and a supervised encoder (Banking77 + CLINC150 zero-shot)

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/ickma2311--jev-baselines-eval/4cef768bc4898704.png" width="100%" alt="ickma2311/jev-baselines-eval screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jujumilk3/jev-calibration-audit">jujumilk3/jev-calibration-audit</a></b> — Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · jujumilk3

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Independent API-only calibration audit of TypeSafe AI's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/KantaHayashiAI/jev-does-not-play-dice">KantaHayashiAI/jev-does-not-play-dice</a></b> — JavaScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · JavaScript · MIT · KantaHayashiAI

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Experiments on Jev’s probability calibration, uncertainty reporting, and forecast probability preservation.

</details>

<details>
<summary><b><a href="https://github.com/laurentfabre/databricks-jev-pdf-lab">laurentfabre/databricks-jev-pdf-lab</a></b> — Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · laurentfabre

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Precision PDF extraction research: Databricks + Jev, synthetic tests, selective parsing, measured tradeoffs and negative results.

</details>

<details>
<summary><b><a href="https://github.com/llt22/jev-lab">llt22/jev-lab</a></b> — Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · llt22

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

TypeSafe Jev research, benchmarks, evaluation datasets, and reproducible experiments

</details>

<details>
<summary><b><a href="https://github.com/meetr1912/jev-bracket">meetr1912/jev-bracket</a></b> — Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`मूल्यांकन, कैलिब्रेशन और बेंचमार्क` · समुदाय · `inferred` · Python · MIT · meetr1912

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

TypeSafe Jev predicts a synthetic 32-team tournament in round fan-out: calibrated Brier vs Elo/seed/oracle plus Monte Carlo champion odds.

</details>

<details>
<summary><b>इस श्रेणी में और</b> <sub>· 14</sub></summary>

- [meetr1912/jev-vickrey](https://github.com/meetr1912/jev-vickrey) - TypeSafe Jev bids in sealed-bid auctions: threshold fan-out reconstructs a calibrated value CDF, scored by.
- [musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and](https://github.com/musman550/musfira-ai-made-the-horizontal-open-source-model-for-jev-with-rlcd-and) - Made the horizontal open-source model for Jev with RLCD, and it surpasses all the Jev benchmarks.
- [onlyoneaman/jev-eval](https://github.com/onlyoneaman/jev-eval) - TypeSafe.
- [rorshopping/jev-browser-local](https://github.com/rorshopping/jev-browser-local) - Run jev-browser on a fully local JEV-style decision engine (no cloud API). Warm-browser fork, VRAM guard.
- [SHAKULMITTAL22/jev-resume](https://github.com/SHAKULMITTAL22/jev-resume) - Folio: job-specific resume leaderboards with approved rubrics, evidence-backed AI evaluation, and human.
- [shunta-furukawa/jev-tick-lab](https://github.com/shunta-furukawa/jev-tick-lab) - A forward-only experiment: Jev (TypeSafe System One) making one-second trading judgments on bitbank, logged.
- [teyhouse/jev-secret-detection](https://github.com/teyhouse/jev-secret-detection) - Measures how well TypeSafe&#x27;s RLCD-Jev model spots real secret credentials in file snippets.
- [us/jev-local](https://github.com/us/jev-local) - Local Jev-compatible evaluation server: POST /v1/systemone with typed noul/choice/score, open weights, no.
- [yodablocks/jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) - Does ORDER BY over a Jev probability put rows in a defensible order? Independent ranking, calibration and.
- [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) - Tax document page classifier built on Jev decisions. 100% strict accuracy across 261 IRS forms, ~$0.001 per.
- [Mapika/decider](https://github.com/Mapika/decider) - One-pass typed decisions with calibrated probabilities (System One style model), fine-tuned from Qwen3.5-2B.
- [genai-craft/openvons](https://github.com/genai-craft/openvons) - openvons (open-Jev): 有限選択肢に確率で答える判断層 — テキスト / 画像 / 日本語音声コマンド.
- [aabolfazl/typesafe-local](https://github.com/aabolfazl/typesafe-local) - Inspired by TypeSafe Ai, Ask a local LLM typed questions, get calibrated probabilities instead of text.
- [mithalouni/system-one-open](https://github.com/mithalouni/system-one-open) - Open replica of TypeSafe.

</details>

<a id="research-models"></a>

## खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध

खुले वेट, छोटी प्रतिकृतियाँ और आर्किटेक्चर पर काम। इनमें से कई इसलिए हैं क्योंकि कैलिब्रेशन व्यवहार केवल सार्वजनिक सामग्री से पुनरुत्पादित नहीं होता।

<details>
<summary><b><a href="https://github.com/kshetrajna12/reflex">kshetrajna12/reflex</a></b> — ⭐64 · Python · observed · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `observed` · Python · MIT · kshetrajna12

##### डेटा

स्टार **64** (+1) · फ़ॉर्क 4 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A small open decision model: state + typed questions -> calibrated probabilities. A Jev / System One re-creation on Qwen3.5.

> An open decision model with the same state-plus-typed-question interface. Worth reading as a shape reference even if you never run it.

</details>

<details>
<summary><b><a href="https://github.com/TianyuCodings/NanoJev">TianyuCodings/NanoJev</a></b> — ⭐426 · Python · inferred · 1 天 · ⭐+31</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · TianyuCodings

##### डेटा

स्टार **426** (+31) · फ़ॉर्क 40 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A nano replica of Jev: parallel decisions, dynamic candidates, and an end-to-end training pipeline.

> A small replica of the parallel-decision shape. Useful for reading the architecture without the vendor stack, and it is how several claims about the interface first became checkable.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/f6e35d78f4661f20.png" width="100%" alt="TianyuCodings/NanoJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tianyucodings--nanojev/5055af419619e7e4.gif" width="100%" alt="TianyuCodings/NanoJev animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/TianyuCodings/NanoJev/main/assets/side_by_side_maze.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/r-ms/mini-jev">r-ms/mini-jev</a></b> — ⭐22 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · r-ms

##### डेटा

स्टार **22** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

mini-Jev: what a Jev-style typed-decision interface looks like on a frozen Qwen3-4B — read the option letter's logits instead of generating JSON. Preregistered experiment, results, teaching bench.

> The most useful independent reproduction to read: it shows the read-the-logits mechanism working, and it also warns explicitly that the share it reads out is not a calibrated probability. That warning is the single most important caveat in this ecosystem.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/r-ms--mini-jev/fe789cc568b74976.png" width="100%" alt="r-ms/mini-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/heist-one">AbdelStark/heist-one</a></b> — ⭐4 · TypeScript · observed · 1 天 · **NEW**</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `observed` · TypeScript · MIT · AbdelStark

##### डेटा

स्टार **4** · फ़ॉर्क 0 · खुले इश्यू 2 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Observable browser stealth game: Jev makes typed guard judgments while deterministic code owns the world.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/abdelstark--heist-one/af28634bc7dc0a39.png" width="100%" alt="AbdelStark/heist-one screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/imserhatdemir/jevspace">imserhatdemir/jevspace</a></b> — HTML · observed · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `observed` · HTML · imserhatdemir

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

A DarkOrbit-style space game piloted by Jev — TypeSafe's System One model. Three.js world, deterministic engine, Jev picks the targets.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/imserhatdemir/jevspace/main/docs/screenshot-win.png" width="100%" alt="imserhatdemir/jevspace screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://huggingface.co/mobarmg/jev-schema-scorer-deberta-v3-large">mobarmg/jev-schema-scorer-deberta-v3-large</a></b> — model · observed · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `observed`

##### डेटा

डाउनलोड 25 · लाइक 4 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://huggingface.co/SargeDev/jev-distill-corpus">SargeDev/jev-distill-corpus</a></b> — model · observed · 1 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `observed`

##### डेटा

डाउनलोड 0 · लाइक 0 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://github.com/ekzhang/openjev-sglang">ekzhang/openjev-sglang</a></b> — ⭐161 · Python · inferred · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · ekzhang

##### डेटा

स्टार **161** (+1) · फ़ॉर्क 12 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Jev-compatible API endpoint based on open models (prefill-only)

> A Jev-compatible endpoint served from open models, so the interface can be exercised without the hosted API.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang screenshot"></td>
<td align="center" valign="top"><img src="https://i.imgur.com/wHM3jxV.gif" width="100%" alt="ekzhang/openjev-sglang animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/featherless-ai/simple-jev">featherless-ai/simple-jev</a></b> — ⭐83 · Python · inferred · 0 天 · ⭐+13</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · featherless-ai

##### डेटा

स्टार **83** (+13) · फ़ॉर्क 7 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Turn any open model into a classifier/jev endpoint

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/featherless-ai/simple-jev/main/imgs/Simple-Jev-Logo.png" width="100%" alt="featherless-ai/simple-jev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/bnsd55/jevmlx">bnsd55/jevmlx</a></b> — ⭐26 · Python · inferred · 0 天 · ⭐+2</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · bnsd55

##### डेटा

स्टार **26** (+2) · फ़ॉर्क 3 · खुले इश्यू 6 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Jev-style parallel constrained decisions for any MLX model on Apple Silicon. Typed, schema-valid JSON in one forward pass.

> Parallel constrained decisions on Apple Silicon via MLX. Local execution removes the per-call cost argument entirely.

</details>

<details>
<summary><b><a href="https://github.com/siliconkernel/vllm-jev-decison">siliconkernel/vllm-jev-decison</a></b> — ⭐8 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · siliconkernel

##### डेटा

स्टार **8** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Classification-only typed decisions for vLLM: finite-schema candidate scoring, probabilities, and abstention. No generative fallback.

</details>

<details>
<summary><b><a href="https://github.com/wfzyx/von">wfzyx/von</a></b> — ⭐4 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · wfzyx

##### डेटा

स्टार **4** · फ़ॉर्क 1 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

The open-source System One decision model. Sub-15ms, non-autoregressive, local drop-in alternative to TypeSafe Jev.

</details>

<details>
<summary><b><a href="https://github.com/deep-diver/mini-jev">deep-diver/mini-jev</a></b> — ⭐3 · Python · inferred · 0 天 · ⭐+2</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · deep-diver

##### डेटा

स्टार **3** (+2) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://github.com/backmeupplz/jev_antispam_bot">backmeupplz/jev_antispam_bot</a></b> — ⭐1 · TypeScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · TypeScript · MIT · backmeupplz

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Minimal grammY Telegram anti-spam bot powered by TypeSafe Jev

</details>

<details>
<summary><b><a href="https://github.com/choxos/jev-reviewer">choxos/jev-reviewer</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · JavaScript · MIT · choxos

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Data extraction for systematic reviews, quoted from the papers. Ask a trial report and its supplements your extraction form or a RoB 2, ROBINS-I, QUADAS-2 or TIDieR template; Jev points at the lines, every answer is a verbatim quote with its page, you check it and export the table. Files stay in your browser.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/4a551dbca9d0c41e.jpg" width="100%" alt="choxos/jev-reviewer screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/choxos--jev-reviewer/71abea319063ce6d.gif" width="100%" alt="choxos/jev-reviewer animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/kw2828/OpenJev">kw2828/OpenJev</a></b> — ⭐1 · Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · kw2828

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Browser decision playground and reproducible experiments on memory, uncertainty, and Doom control

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/7caa9b0eff4636a1.png" width="100%" alt="kw2828/OpenJev screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/kw2828--openjev/af5371a3a94cb693.gif" width="100%" alt="kw2828/OpenJev animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/2023Anita/jev-gpt-arena">2023Anita/jev-gpt-arena</a></b> — CSS · inferred · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · CSS · 2023Anita

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Jev × GPT asynchronous AI Tetris arena with independent clocks, live score comparison, architecture diagram, and demo recording

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
<td align="center" valign="top"><a href="https://raw.githubusercontent.com/2023Anita/jev-gpt-arena/main/assets/jev-gpt-arena-demo.mp4"><img src="" width="100%" alt="2023Anita/jev-gpt-arena video"></a><br><sub><a href="https://raw.githubusercontent.com/2023Anita/jev-gpt-arena/main/assets/jev-gpt-arena-demo.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/nikotaronosuke/jev-voice-decision">nikotaronosuke/jev-voice-decision</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · MIT · nikotaronosuke

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Japanese speech → local STT → Jev typed decisions → deterministic actions.

</details>

<details>
<summary><b><a href="https://github.com/rikkooo/jev-trade">rikkooo/jev-trade</a></b> — inferred · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · rikkooo

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

A market-data trading simulator powered by auditable Jev judgments

</details>

<details>
<summary><b><a href="https://github.com/shellneko/minigrid-jev">shellneko/minigrid-jev</a></b> — Python · inferred · 0 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `inferred` · Python · shellneko

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://github.com/zhihz/openjev">zhihz/openjev</a></b> — ⭐9 · Python · unverified · 2 天</summary>

##### बुनियादी तथ्य

`खुले पुनरुत्पादन, वेट और आर्किटेक्चर शोध` · समुदाय · `unverified` · Python · NOASSERTION · zhihz

##### डेटा

स्टार **9** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Local bilingual probability decisions from context, questions, and candidate answers. Independent research preview inspired by TypeSafe Jev.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/zhihz/openjev/main/docs/images/demo-en.png" width="100%" alt="zhihz/openjev screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<a id="apps-demos"></a>

## अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो

गेम, रोबोट, ब्राउज़र और डैशबोर्ड। डेमो ही वह तरीका हैं जिनसे विलंबता और लागत के दावे पढ़ने योग्य बनते हैं।

<details>
<summary><b><a href="https://github.com/zadescoxp/Jev-Trades">zadescoxp/Jev-Trades</a></b> — ⭐10 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · Python · Apache-2.0 · zadescoxp

##### डेटा

स्टार **10** · फ़ॉर्क 1 · खुले इश्यू 3 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Trading bot with the all new TypeSafe AI's first system one model named as Jev

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/d74708c101b60531.png" width="100%" alt="zadescoxp/Jev-Trades screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/zadescoxp--jev-trades/a11bc2e9272ed726.gif" width="100%" alt="zadescoxp/Jev-Trades animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/daftAI2026/awesome-jev">daftAI2026/awesome-jev</a></b> — ⭐3 · TypeScript · observed · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · TypeScript · daftAI2026

##### डेटा

स्टार **3** (+1) · फ़ॉर्क 2 · खुले इश्यू 2 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

TypeSafe System One / Jev community directory — GitHub projects & posts around typed decisions (typesafe.ai)

</details>

<details>
<summary><b><a href="https://github.com/markjaquith/typesafe-ai-playground">markjaquith/typesafe-ai-playground</a></b> — ⭐1 · Rust · observed · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · Rust · MIT · markjaquith

##### डेटा

स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A playground for experiments around Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://github.com/adiun/clinical-trial-screener">adiun/clinical-trial-screener</a></b> — TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · TypeScript · adiun

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Testing out Jev / System One model for a health use case

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/adiun/clinical-trial-screener/main/docs/screenshots/dark.png" width="100%" alt="adiun/clinical-trial-screener screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/Bud-ro/jev-demos">Bud-ro/jev-demos</a></b> — Dart · observed · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · Dart · Bud-ro

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Demos to test the effectiveness of TypeSafe's "Jev" System One Model

</details>

<details>
<summary><b><a href="https://github.com/chris-wozniczek/jev-voice-control">chris-wozniczek/jev-voice-control</a></b> — Swift · observed · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · Swift · chris-wozniczek

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Control your Mac by voice. Speech → Jev (TypeSafe AI System One model) typed decisions → macOS actions. Menu-bar Swift app.

</details>

<details>
<summary><b><a href="https://github.com/tirukovelamanoj/jev-plays-doom">tirukovelamanoj/jev-plays-doom</a></b> — Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · Python · MIT · tirukovelamanoj

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A System One model driving the game through structured state, no pixels.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/19e3fa783e7f72e5.jpg" width="100%" alt="tirukovelamanoj/jev-plays-doom screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/tirukovelamanoj--jev-plays-doom/04e4dd3a1f6c6bae.gif" width="100%" alt="tirukovelamanoj/jev-plays-doom animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/tirukovelamanoj/jev-plays-doom/main/docs/jev-doom.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/wustep/jev-playground">wustep/jev-playground</a></b> — TypeScript · observed · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · TypeScript · wustep

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Can a System One model steer music? Jev picks the plan (enums only); code renders sheet, audio and MIDI.

</details>

<details>
<summary><b><a href="https://x.com/tspy/status/2100864234523685146">Xtags — X intent labeller</a></b> — @tspy · observed · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `observed` · [yishan](https://x.com/tspy) · @tspy · x.com

##### डेटा

व्यूज़ 9873 · लाइक 24 · टिप्पणियाँ 11 · पोस्ट किया गया 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Xtags: a Chrome extension that labels each post in an X timeline with what it is trying to get from you — inducement, provocation, promotion, machine-generated, persuasion, entertainment, information — drawn as a tag plus a probability right after the timestamp. A side panel reports session counts (seen, judged, correct) and cumulative token cost. The author reports near-instant responses and usable accuracy before any tuning.

➡️ **Original project (manifoldor/xtags)** — [https://github.com/manifoldor/xtags](https://github.com/manifoldor/xtags)

> Worth reading as a latency argument rather than an accuracy one: labelling a timeline only works if the decision costs less than the scroll, which is the constraint a generative model cannot meet.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/0641644f12a25a45.jpg" width="100%" alt="Xtags — X intent labeller screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/x--tspy--2100864234523685146/b80cf3173f63bdd7.gif" width="100%" alt="Xtags — X intent labeller animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://video.twimg.com/amplify_video/2100858340331200512/vid/avc1/1242x720/ex2FF5-TerVxo9xX.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/jkudish/jev-browser">jkudish/jev-browser</a></b> — ⭐113 · TypeScript · inferred · 0 天 · ⭐+5</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · MIT · jkudish

##### डेटा

स्टार **113** (+5) · फ़ॉर्क 6 · खुले इश्यू 2 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Browser use using Typesafe's Jev model

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/9712e94d8402c3ec.gif" width="100%" alt="jkudish/jev-browser screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/jkudish--jev-browser/d9b7631c25d7db06.gif" width="100%" alt="jkudish/jev-browser animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/jkudish/jev-browser/main/assets/github-demo.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/hr98w/jev-visual">hr98w/jev-visual</a></b> — ⭐112 · Python · inferred · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Python · MIT · hr98w

##### डेटा

स्टार **112** (+1) · फ़ॉर्क 12 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

An educational Jev-like visual inference experiment on Apple Silicon: shared context, direct candidate scoring, and local visual demos.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/hr98w--jev-visual/10390ced72c89223.png" width="100%" alt="hr98w/jev-visual screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/moritzkremb/jev-voice-browser">moritzkremb/jev-voice-browser</a></b> — ⭐80 · JavaScript · inferred · 1 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · MIT · moritzkremb

##### डेटा

स्टार **80** (+1) · फ़ॉर्क 8 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Control a real browser by voice. Jev (TypeSafe System One) decides intent + target in ~300 ms per spoken word; Playwright acts — often before you finish the sentence.

> Voice-driven browser control where the intent check is a typed decision. Shows the latency budget a gate needs to be worth running.

</details>

<details>
<summary><b><a href="https://github.com/komorra/Eugeniusz">komorra/Eugeniusz</a></b> — ⭐7 · Python · inferred · 1 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Python · MIT · komorra

##### डेटा

स्टार **7** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Local, typed AI decisions for C, C++, C#, Python, Unity and Unreal Engine.

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/b651429102df34d4.png" width="100%" alt="komorra/Eugeniusz screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/komorra--eugeniusz/38dc14fec0608a74.gif" width="100%" alt="komorra/Eugeniusz animation"><br><sub>एनिमेटेड रिकॉर्डिंग</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/vinilana/live-jev">vinilana/live-jev</a></b> — ⭐7 · JavaScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · vinilana

##### डेटा

स्टार **7** · फ़ॉर्क 5 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

2D autonomous car simulation in the browser, driven by TypeSafe's Jev decision model

</details>

<details>
<summary><b><a href="https://github.com/emrickgarrett/OneVOneJev">emrickgarrett/OneVOneJev</a></b> — ⭐5 · TypeScript · inferred · 1 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · emrickgarrett

##### डेटा

स्टार **5** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

1v1 Jev quickscope arena — Three.js + TypeSafe System One

</details>

<details>
<summary><b><a href="https://github.com/0x7067/jev-browse">0x7067/jev-browse</a></b> — ⭐2 · JavaScript · inferred · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · MIT · 0x7067

##### डेटा

स्टार **2** (+1) · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Browser automation with Jev (TypeSafe) as decision model

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/6b2906f1131adf4c.gif" width="100%" alt="0x7067/jev-browse screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/0x7067--jev-browse/3efc4d3b381ff9f5.gif" width="100%" alt="0x7067/jev-browse animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/0x7067/jev-browse/main/docs/demo.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/paulsmith/computer-use-jev">paulsmith/computer-use-jev</a></b> — ⭐2 · Go · inferred · 1 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Go · MIT · paulsmith

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

macOS computer use driven by Jev (TypeSafe System One) as the decision maker

</details>

<details>
<summary><b><a href="https://github.com/vmendes90/jev-shield">vmendes90/jev-shield</a></b> — ⭐2 · TypeScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · MIT · vmendes90

##### डेटा

स्टार **2** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Privacy-first Chrome extension that semantically blocks native ads, sponsored feed cards, and video ads using TypeSafe Jev

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/vmendes90--jev-shield/ee87b261d199a34c.jpg" width="100%" alt="vmendes90/jev-shield screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://github.com/charleeagni/JevPiano">charleeagni/JevPiano</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · charleeagni

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

@typesafeai 's Jev controls the 2 hands and each finger to play the piano in real-time.  Jev only "sees" what we see and plays this from the "note waterfall". It uses  @browser_use 's jev-ultrafast and some decision scheduling to make this happen in real-time.  Sound on 🔈🔉🔊

</details>

<details>
<summary><b><a href="https://github.com/finetuningsingh/jev-chatbot">finetuningsingh/jev-chatbot</a></b> — ⭐1 · JavaScript · inferred · 0 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · JavaScript · MIT · finetuningsingh

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Experiment: using TypeSafe Jev as a chatbot by choosing replies one letter or word at a time

</details>

<details>
<summary><b><a href="https://github.com/Little-Planet-Labs/jev-playground">Little-Planet-Labs/jev-playground</a></b> — ⭐1 · TypeScript · inferred · 1 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · Little-Planet-Labs

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A small Next.js app for experimenting with TypeSafe AI's Jev model (System One)

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/Little-Planet-Labs/jev-playground/main/docs/screenshot.png" width="100%" alt="Little-Planet-Labs/jev-playground screenshot"></td>
<td align="center" valign="top"><sub>कोई मीडिया प्रकाशित नहीं</sub></td>
</tr></table>

<sub>यह संपत्ति अपस्ट्रीम रिपॉज़िटरी से सीधे लिंक की गई है क्योंकि पुनर्वितरण की कोई लाइसेंस घोषित नहीं की गई।</sub>

</details>

<details>
<summary><b><a href="https://github.com/phureewat29/jev-got">phureewat29/jev-got</a></b> — ⭐1 · TypeScript · inferred · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · TypeScript · phureewat29

##### डेटा

स्टार **1** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Jev (TypeSafe AI) PoC through Game of Thrones

</details>

<details>
<summary><b><a href="https://github.com/PistachioAIHQ/jev-synergy-screening">PistachioAIHQ/jev-synergy-screening</a></b> — ⭐1 · Python · inferred · 2 天</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Python · PistachioAIHQ

##### डेटा

स्टार **1** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-16 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels

</details>

<details>
<summary><b><a href="https://github.com/Aben25/jev-sim">Aben25/jev-sim</a></b> — Python · inferred · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`अनुप्रयोग, गेम, रोबोटिक्स और इंटरैक्टिव डेमो` · समुदाय · `inferred` · Python · MIT · Aben25

##### डेटा

स्टार **0** · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-19 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

Fast mobile-simulator computer-use: sim-use + TypeSafe Jev (Cua jev-use pattern for iOS/Android sims)

</details>

<details>
<summary><b>इस श्रेणी में और</b> <sub>· 16</sub></summary>

- [bahramzada/jev-taxi-dispatch](https://github.com/bahramzada/jev-taxi-dispatch) - Real-vaxt taksi dispetçerlik simulyasiyası - TypeSafe JEV (System One) modeli ilə.
- [BrendanH18/jev-lab](https://github.com/BrendanH18/jev-lab) - Six small apps and a workbench that show what TypeSafe&#x27;s Jev (System One) model can do.
- [brudarko/jev-mac-voice](https://github.com/brudarko/jev-mac-voice) - English full-duplex voice control for macOS with OpenAI Realtime, native Accessibility, and Jev.
- [chahero/driving-jev](https://github.com/chahero/driving-jev) - Watch TypeSafe Jev make highway driving decisions. Includes live API and offline gameplay previews.
- [formigacamuflada/jev-computer-use](https://github.com/formigacamuflada/jev-computer-use)
- [hxutixnnn/ui-jev](https://github.com/hxutixnnn/ui-jev)
- [juanAndresArriaga/system-one-jev-demo](https://github.com/juanAndresArriaga/system-one-jev-demo) - Tiny demo of TypeSafe System One / Jev: unstructured state in → typed probabilistic decisions out.
- [JYeswak/jev_playground](https://github.com/JYeswak/jev_playground)
- [Keitark/jev-gamebook-demo](https://github.com/Keitark/jev-gamebook-demo)
- [metrox-eth/moss-jev](https://github.com/metrox-eth/moss-jev) - MOSS × Jev: a recorded-run 3D demo of the litter-picking rover choosing targets with TypeSafe.
- [n3ndor/n8n-nodes-typesafe-jev](https://github.com/n3ndor/n8n-nodes-typesafe-jev) - n8n community node for TypeSafe Jev structured AI decisions.
- [okinaaudio/live-jev](https://github.com/okinaaudio/live-jev) - Control Ableton Live with one short sentence (Japanese / English). Summon with ⌘⇧Space, type or dictate, done.
- [pistachiopranay/jev-synergy-screening](https://github.com/pistachiopranay/jev-synergy-screening) - Jev (TypeSafe System One) × ASReview SYNERGY abstract screening demo — Choice/Noul vs gold labels.
- [rchovatiya88/cyber-breach-jev](https://github.com/rchovatiya88/cyber-breach-jev) - Cyber-Breach: The Jev Protocol - A tactical cyberpunk arena combat game powered by TypeSafe AI Jev System One.
- [tanayvasishtha/Slither-Me-Jev](https://github.com/tanayvasishtha/Slither-Me-Jev) - 8 AI snakes, 1 human, 1 arena. Every snake is driven live by TypeSafe&#x27;s Jev, making all decisions in real time.
- [sorrycc/typesafe-snake](https://github.com/sorrycc/typesafe-snake) - Snake auto-played by TypeSafe.

</details>

<a id="media-discussions"></a>

## लेखन, चर्चाएँ और समान सूचियाँ

लॉन्च थ्रेड, स्वतंत्र लेख और इस क्षेत्र की अन्य क्यूरेटेड सूचियाँ। यह रिपॉज़िटरी अकेली नहीं है, और यह कहना अन्यथा दिखाने से अधिक उपयोगी है।

<details>
<summary><b><a href="https://github.com/browser-use/jev-ultrafast">browser-use/jev-ultrafast</a></b> — ⭐5847 · Python · observed · 0 天 · ⭐+176</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · MIT · browser-use

##### डेटा

स्टार **5847** (+176) · फ़ॉर्क 375 · खुले इश्यू 35 · बनाया गया 2026-09-16 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

i. am. speed.

<sub>कोड में प्रयुक्त पाया गया: `jev_ultrafast/model.py`</sub>

<table><tr><th align="center" width="50%">चित्र</th><th align="center" width="50%">वीडियो</th></tr><tr>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/3ba041d1c574f62a.gif" width="100%" alt="browser-use/jev-ultrafast screenshot"></td>
<td align="center" valign="top"><img src="https://raw.githubusercontent.com/wh000wh000/awesome-jev-live/main/media/browser-use--jev-ultrafast/dcdb919ac3afb514.gif" width="100%" alt="browser-use/jev-ultrafast animation"><br><sub>एनिमेटेड रिकॉर्डिंग · <a href="https://raw.githubusercontent.com/browser-use/jev-ultrafast/main/docs/demo.mp4">वीडियो खोलें</a></sub></td>
</tr></table>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev</a></b> — ⭐1892 · observed · 3 天 · ⭐+2</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 1892 · टिप्पणियाँ 496 · अंतिम पुश 2026-09-15 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://github.com/Anil-matcha/awesome-jev-by-typesafe">Anil-matcha/awesome-jev-by-typesafe</a></b> — ⭐536 · Python · observed · 0 天 · ⭐+7</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · MIT · Anil-matcha

##### डेटा

स्टार **536** (+7) · फ़ॉर्क 102 · खुले इश्यू 4 · बनाया गया 2023-05-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Evidence-backed use cases, patterns, prompts, and starter code for TypeSafe Jev — a System One model for fast, typed, confidence-aware decisions in software.

<sub>कोड में प्रयुक्त पाया गया: `README.md`, `examples/python/quickstart.py`, `examples/python/workflows.py`, `docs/jev-use-case-playbook.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/dabit3/jev-experiments">dabit3/jev-experiments</a></b> — ⭐247 · TypeScript · observed · 0 天 · ⭐+12</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · TypeScript · dabit3

##### डेटा

स्टार **247** (+12) · फ़ॉर्क 20 · खुले इश्यू 17 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

<sub>कोड में प्रयुक्त पाया गया: `jev-lint/proxy.mjs`</sub>

</details>

<details>
<summary><b><a href="https://github.com/AbdelStark/awesome-typesafe">AbdelStark/awesome-typesafe</a></b> — ⭐245 · CSS · observed · 0 天 · ⭐+13</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · CSS · MIT · AbdelStark

##### डेटा

स्टार **245** (+13) · फ़ॉर्क 36 · खुले इश्यू 2 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A curated list of official resources and community projects for TypeSafe, System One models, and Jev.

<sub>कोड में प्रयुक्त पाया गया: `README.md`</sub>

</details>

<details>
<summary><b><a href="https://github.com/yibie/awesome-jev">yibie/awesome-jev</a></b> — ⭐195 · Python · observed · 0 天 · ⭐+14</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · yibie

##### डेटा

स्टार **195** (+14) · फ़ॉर्क 26 · खुले इश्यू 1 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A curated list of public projects, integrations, and discussions built on Jev — TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/cobanov/awesome-jev">cobanov/awesome-jev</a></b> — ⭐125 · observed · 0 天 · ⭐+7</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · CC0-1.0 · cobanov

##### डेटा

स्टार **125** (+7) · फ़ॉर्क 13 · खुले इश्यू 1 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A curated, source-backed list of projects built with Jev, TypeSafe AI's System One model for typed decisions.

</details>

<details>
<summary><b><a href="https://github.com/AnotiaWang/awesome-jev">AnotiaWang/awesome-jev</a></b> — ⭐69 · observed · 0 天 · ⭐+2</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · CC0-1.0 · AnotiaWang

##### डेटा

स्टार **69** (+2) · फ़ॉर्क 19 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A curated list of awesome Jev / TypeSafe System One applications, libraries, and resources.

<sub>कोड में प्रयुक्त पाया गया: `README.md`, `README_zh.md`</sub>

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736660">Open-sourced jev architecture last year with model,paper and dataset</a></b> — ⭐54 · observed · 1 天 · ⭐+2</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 54 · टिप्पणियाँ 12 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Everyone now talks about the architecture  that&#x27;s not auto regressive and does lightning fast probability prediction with a json schema. I worked on this literally one year back in March 2025, published an arxiv paper, pushed the model to huggingface along with the pypi pack

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/awesome-jev">hellogumbo/awesome-jev</a></b> — ⭐42 · JavaScript · observed · 0 天 · ⭐+5</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### डेटा

स्टार **42** (+5) · फ़ॉर्क 10 · खुले इश्यू 13 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

A community directory of projects built on Jev, TypeSafe AI's System One model.

</details>

<details>
<summary><b><a href="https://github.com/OmniJev/awesome-jev">OmniJev/awesome-jev</a></b> — ⭐14 · JavaScript · observed · 0 天 · ⭐+3</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · JavaScript · NOASSERTION · OmniJev

##### डेटा

स्टार **14** (+3) · फ़ॉर्क 2 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Papers, open reproductions and independent evaluations behind System One models and Jev.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49760264">Using jev to improve product experiences is pretty crazy</a></b> — ⭐6 · observed · 0 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 6 · टिप्पणियाँ 3 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49718888">Typesafe AI</a></b> — ⭐5 · observed · 3 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 5 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-15 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49747584">Jev is about to change the AI economy</a></b> — ⭐4 · observed · 1 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 4 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49746625">Typesafe AI</a></b> — ⭐4 · observed · 1 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 4 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://github.com/aliaihub/awesome-jev-usecases">aliaihub/awesome-jev-usecases</a></b> — ⭐3 · observed · 0 天 · ⭐+1</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · NOASSERTION · aliaihub

##### डेटा

स्टार **3** (+1) · फ़ॉर्क 0 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

Evidence-backed use cases, patterns, and guidance for building with Jev, TypeSafe AI's System One model. Every claim is labeled and sourced.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49763045">Inventor of ChatGPT and RLHF Launches Typesafe.ai</a></b> — ⭐3 · observed · 0 天 · **NEW**</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 3 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-19 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49748643">Mini-Jev – typesafe&#x27;s Jev implemented on top of an LLM locally</a></b> — ⭐3 · observed · 1 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 3 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49755005">Two techniques for working with System One models</a></b> — ⭐3 · observed · 0 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 3 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49736875">Typesafe AI</a></b> — ⭐3 · observed · 1 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 3 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-17 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b><a href="https://github.com/hellogumbo/should-ai-kill-us-all">hellogumbo/should-ai-kill-us-all</a></b> — ⭐2 · JavaScript · observed · 1 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · JavaScript · CC0-1.0 · hellogumbo

##### डेटा

स्टार **2** · फ़ॉर्क 1 · खुले इश्यू 0 · बनाया गया 2026-09-17 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

We ask Jev, TypeSafe AI's System One model, whether AI should kill us all. Every ten minutes. Using the actual headlines.

</details>

<details>
<summary><b><a href="https://github.com/jtnkminimal/awesome-jev">jtnkminimal/awesome-jev</a></b> — ⭐2 · Python · observed · 0 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed` · Python · CC0-1.0 · jtnkminimal

##### डेटा

स्टार **2** · फ़ॉर्क 1 · खुले इश्यू 2 · बनाया गया 2026-09-18 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-19

##### सारांश

A curated projects built with Jev, TypeSafe's System One model.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49753667">Show HN: Explore 2D semantic space with the Jev model</a></b> — ⭐2 · observed · 0 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 2 · टिप्पणियाँ 0 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

SemanticSpace is an experiment around Jev, TypeSafe AI’s new model. It uses a Cartesian plane defined by arbitrary phrases for each axis, to map prompts onto the resulting 2D semantic space. You can edit the prompts and axes to visualize virtually any 2D relationship.

</details>

<details>
<summary><b><a href="https://news.ycombinator.com/item?id=49750649">Show HN: Open-Source Alternative to TypeSafe.ai</a></b> — ⭐2 · observed · 0 天</summary>

##### बुनियादी तथ्य

`लेखन, चर्चाएँ और समान सूचियाँ` · समुदाय · `observed`

##### डेटा

अंक 2 · टिप्पणियाँ 1 · अंतिम पुश 2026-09-18 · पहली बार सूचीबद्ध 2026-09-18

##### सारांश

अपस्ट्रीम से कोई विवरण प्रकाशित नहीं हुआ।

</details>

<details>
<summary><b>इस श्रेणी में और</b> <sub>· 93</sub></summary>

- [Show HN: Sokit – a LangChain like harness for Jev (or other System 1 models)](https://news.ycombinator.com/item?id=49744527) - Full disclosure, it was coded with AI, I don&amp;#x27;t claim otherwise. But I wanted to test out tool calls and.
- [The first (public) System One Model; Jev gives AI the properties of code](https://news.ycombinator.com/item?id=49729945)
- [TypeSafe / Jev latency-focused demos built by Devin](https://news.ycombinator.com/item?id=49757995)
- [TypeSafe AI's Jev Is Not an LLM – and That May Be the Point](https://news.ycombinator.com/item?id=49761730)
- [Typesafe's Jev is the fish at the poker table](https://news.ycombinator.com/item?id=49745212)
- [Typesafe-computer-use drives a Mac toward a goal for 1/50th of a cent per step](https://news.ycombinator.com/item?id=49733647)
- [Typesafe.ai Jev Open Source Alternative Qwen-2.5-1B-RLCD](https://news.ycombinator.com/item?id=49734345)
- [What is a System One model and why we need it?](https://news.ycombinator.com/item?id=49760138)
- [ozers/jevsome-projects](https://github.com/ozers/jevsome-projects) - Open-source projects that provably call Jev, TypeSafe AI.
- [rhc98/awesome-jev](https://github.com/rhc98/awesome-jev) - Projects built on Jev (TypeSafe AI&#x27;s System One model), curated by Jev itself.
- [soderlind/ai-provider-for-jev](https://github.com/soderlind/ai-provider-for-jev) - Connect WordPress to TypeSafe&#x27;s Jev System One model for structured decisions (choice, score, noul).
- [aamanlamba/jev-explore](https://github.com/aamanlamba/jev-explore) - An example repository for exploring Jev - the System One model.
- [alpibrusl/lex-judge](https://github.com/alpibrusl/lex-judge) - Typed judgments from a System One model, as a \[net\]-only Lex effect.
- [codaaiteam/jev-ai](https://github.com/codaaiteam/jev-ai) - Jev AI quickstart &amp; FAQ — TypeSafe AI&#x27;s System One model. Try it free: jevtypesafeai.com.
- [hide-G/magi-system-on-jev](https://github.com/hide-G/magi-system-on-jev) - MAGI system (Neon Genesis Evangelion) recreated with Jev, TypeSafe AI.
- [JohnDotOwl/awesome-jev](https://github.com/JohnDotOwl/awesome-jev) - A curated list of projects built on Jev, TypeSafe AI&#x27;s System One model.
- [piyush97/focus-tube](https://github.com/piyush97/focus-tube) - Distraction-free YouTube learning feed powered by TypeSafe AI&#x27;s Jev System One model.
- [rbalch/typesafeai-review](https://github.com/rbalch/typesafeai-review) - Using Typesafe.AI to generate diff reviews.
- [robzolkos/omarchy-issue-classifier](https://github.com/robzolkos/omarchy-issue-classifier) - Classify the Omarchy issue backlog with Jev, TypeSafe.
- [Shashank-H/jev-trader](https://github.com/Shashank-H/jev-trader) - An automated trader using SystemOne model - TypesafeAI Jev.
- [TheGali/terrarium](https://github.com/TheGali/terrarium) - A sandbox where a TypeSafe System One model presses the controls of a small creature. Code runs the world.
- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) - One AI trade decision every Monad block. Jev on Kuru MON-USDC.
- [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev)
- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) - Search the web with TypeSafe.
- [mrnugget/jev-shell-history](https://github.com/mrnugget/jev-shell-history) - Fish-style zsh history autosuggestions ranked by Jev (TypeSafe).
- [IAmUnbounded/save-token-jev-clean](https://github.com/IAmUnbounded/save-token-jev-clean)
- [daseinlabs/open-jev](https://github.com/daseinlabs/open-jev)
- [hqman/JevScout](https://github.com/hqman/JevScout)
- [jon-devlapaz/jev-me](https://github.com/jon-devlapaz/jev-me) - Grill-me with Jev optional each turn.
- [oso95/x-scanner](https://github.com/oso95/x-scanner) - Chrome extension that labels every post you scroll past on X with typed Jev judgments and a live cost counter.
- [logan-markewich/jeff](https://github.com/logan-markewich/jeff) - A self-hosted drop-in replacement for TypeSafe&#x27;s jev, powered by GliFormer.
- [manifoldor/xtags](https://github.com/manifoldor/xtags) - 在 X 的时间线上，给每条帖子标出它想让你干什么。判断来自 Jev，一个只返回概率、不生成文本的模型.
- [Kevthetech143/super-jev](https://github.com/Kevthetech143/super-jev) - A small, extensible decision-to-action harness for TypeSafe Jev.
- [joelhooks/pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction) - Pi extension: verbatim context compaction with TypeSafe Jev decisions.
- [haseeb-heaven/jev-system-one](https://github.com/haseeb-heaven/jev-system-one) - A polished OpenAI + TypeSafe Jev terminal interface for answers with transparent decision reports.
- [lbotinelly/jev-little-airways](https://github.com/lbotinelly/jev-little-airways) - A show-and-tell capability study for Jev, TypeSafe&#x27;s System One decision model.
- [1jehuang/jev-pr-labeler](https://github.com/1jehuang/jev-pr-labeler) - Semantic GitHub PR labels using Jev&#x27;s typed decisions, with conceptual scope instead of line counts.
- [amr05008/jev-sandbox](https://github.com/amr05008/jev-sandbox) - Test bench for TypeSafe&#x27;s Jev.
- [AppitStudio/awesome-jev](https://github.com/AppitStudio/awesome-jev) - Curated Jev resources and runnable examples for typed AI decisions.
- [Charlyhno-eng/jev-document-classification](https://github.com/Charlyhno-eng/jev-document-classification) - JEV Document Classification enables the rapid and cost-effective classification of text-based documents using.
- [MumuTW/awesome-jev](https://github.com/MumuTW/awesome-jev) - 快速看懂風格鮮明的 Jev：型別化決策的 System One，以及社群熱議的同類模型.
- [sontakey/awesome-jev](https://github.com/sontakey/awesome-jev) - Unofficial list of insanely useful TypeSafe AI Jev / System One projects.
- [TanayPadar/gpt-vs-jev](https://github.com/TanayPadar/gpt-vs-jev) - Compare GPT generated language with JEV structured Noul decisions on the same input.
- [tylerjharden/harden-jev-decides](https://github.com/tylerjharden/harden-jev-decides) - JEV picks which stream idea becomes the live MVP. TypeSafe System One decision board.
- [Z761293629/pi-jev-helm](https://github.com/Z761293629/pi-jev-helm)
- [agentik-os/jev-radar](https://github.com/agentik-os/jev-radar)
- [alibowbow/jev](https://github.com/alibowbow/jev)
- [amapara27/jev-pilot](https://github.com/amapara27/jev-pilot) - control your desktop smoothly. powered by typesafe&#x27;s jev.
- [ddesmond/explore-jev](https://github.com/ddesmond/explore-jev) - Exploring Jev.
- [dglazkov/jev2ui](https://github.com/dglazkov/jev2ui) - Jev + A2UI = ?
- [godspede/jev-auto-classifier](https://github.com/godspede/jev-auto-classifier) - Retired: Jev support lives in godspede/construct-auto-classifier.
- [golergka/jev-plays-starcraft-2](https://github.com/golergka/jev-plays-starcraft-2)
- [gowtam04/jev-prototypes](https://github.com/gowtam04/jev-prototypes) - Practice lab for TypeSafe Jev prototypes.
- [JulianLee1117/jev-moneyprinter](https://github.com/JulianLee1117/jev-moneyprinter)
- [kevin9327/jev-master](https://github.com/kevin9327/jev-master) - Typed System One decisions with Jev: Choice + Score + Noul composed in code.
- [kong75/jev-directory](https://github.com/kong75/jev-directory) - Copyable prompts, typed decision patterns, and practical guides for Jev by TypeSafe. Free, independent, and.
- [kspviswa/chakravyuha-jev](https://github.com/kspviswa/chakravyuha-jev) - Chakravyuha — a polar ring-maze where every move is a Jev (TypeSafe System One) decision. A fun experiment.
- [lalitsonawane/jev-one-system](https://github.com/lalitsonawane/jev-one-system)
- [LingXuanYin/jev-chat](https://github.com/LingXuanYin/jev-chat) - Jev 聊天机：一个「只选不写」的聊天机——每个回复由逐词选择拼装，词典+分级索引+输入法式联想，由真实 Jev（TypeSafe System One）驱动。非官方实验，与 TypeSafe AI 无关联.
- [logan-anderson/jev-as-a-llm](https://github.com/logan-anderson/jev-as-a-llm)
- [lookfwd/jev-fact-checker](https://github.com/lookfwd/jev-fact-checker) - Uses Typesafe AI Jev to Provide A Tweet Fact Checker.
- [meetr1912/jev-poker](https://github.com/meetr1912/jev-poker) - Watch Jev (TypeSafe) play heads-up No-Limit Hold.
- [memorysaver/jev-atari-lab](https://github.com/memorysaver/jev-atari-lab) - Challenge Atari with Jev: structured decisions, value questions, and replayable experiments.
- [mizzlelover/jev-hub](https://github.com/mizzlelover/jev-hub) - JEV HUB · X 上关于 TypeSafe AI「系统一模型」Jev 的长文与演示视频聚合（保留原链与作者）｜ 谁是专家 出品.
- [Nachom3/jevTrader](https://github.com/Nachom3/jevTrader) - A High Frecuncy Trader made in Rust using Jev as a decision maker.
- [nak1b/jev-experiments](https://github.com/nak1b/jev-experiments) - Small experiments with Jev by TypeSafe.
- [nanami-0713/dsh-jev-decide](https://github.com/nanami-0713/dsh-jev-decide)
- [nardinmarcus/pi-jev-typesafe](https://github.com/nardinmarcus/pi-jev-typesafe) - TypeSafe Jev (System One judgments) for Pi: zero-dependency jev_ask tool with question linting, model.
- [nishimotz/hello-jev](https://github.com/nishimotz/hello-jev)
- [Nolane-x/JEV-language](https://github.com/Nolane-x/JEV-language)
- [oguressive/sample-jev](https://github.com/oguressive/sample-jev)
- [OsirianLegacy/JevTactics](https://github.com/OsirianLegacy/JevTactics)
- [paritosh100/Jev-vs-LLM](https://github.com/paritosh100/Jev-vs-LLM)
- [ponyo877/jev-realtime-brain-scanner](https://github.com/ponyo877/jev-realtime-brain-scanner)
- [ponyo877/jev-telop-live](https://github.com/ponyo877/jev-telop-live)
- [s-hiraoku/jev-checkkit](https://github.com/s-hiraoku/jev-checkkit)
- [shaheersystems/jev-test](https://github.com/shaheersystems/jev-test)
- [thisisjorge/jev-control-room](https://github.com/thisisjorge/jev-control-room) - Interactive control room for fast typed AI decisions with TypeSafe Jev.
- [TonyP-MR/jev-curation-engine](https://github.com/TonyP-MR/jev-curation-engine) - Read-only TypeSafe Jev feasibility test rig for comparing structured Curation Engine classification decisions.
- [Tsagaanbayr1/jev-tetris](https://github.com/Tsagaanbayr1/jev-tetris) - Real-time Tetris versus Jev, a TypeSafe decision model — spins, garbage, B2B chains, and decisions prefetched.
- [uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep) - grep by meaning, across languages. TypeSafe Jev scores every line against a meaning; combine meanings with.
- [wakamenod/jev.el](https://github.com/wakamenod/jev.el)
- [Waxmell114514/awesome-jev-compaction](https://github.com/Waxmell114514/awesome-jev-compaction)
- [waynesutton/ask-jev-ai](https://github.com/waynesutton/ask-jev-ai) - A public wall where anyone asks a question in three to fifteen words and Jev, TypeSafe.
- [yn01/jev-stormboard](https://github.com/yn01/jev-stormboard) - 気象庁防災情報XMLをリアルタイムに取り込み、Jevで判定するStreamlitデモ(第一段階: ロガー).
- [yuki-dev26/jev-test](https://github.com/yuki-dev26/jev-test) - Javの検証用.
- [zaycruz/fast-jev-compaction-pi](https://github.com/zaycruz/fast-jev-compaction-pi) - Verbatim Jev-guided context compaction for pi — replaces the built-in compaction summary with fast-jev.
- [Zogrus/jev-technical-term](https://github.com/Zogrus/jev-technical-term) - YouTubeの解説動画やZoomのセミナーを聞きながら、出てきた技術用語のひとこと解説をリアルタイム表示するローカルツール(判定AIは TypeSafe AI の Jev).
- [realZachi/typesafe-adblock](https://github.com/realZachi/typesafe-adblock) - 🧹 Fun project: a Chrome extension that asks a tiny AI decision model (TypeSafe Jev).
- [razorback16/openjev](https://github.com/razorback16/openjev) - Open, Jev-compatible System One decision server on DiffusionGemma.
- [devanshbatham/commit-miner](https://github.com/devanshbatham/commit-miner) - Classify Git commit diffs and messages with Jev. Bug fixes, security fixes/CWEs, and change types.
- [phyous/tsai-sc](https://github.com/phyous/tsai-sc) - TypeSafe Jev controls original StarCraft shareware through keyboard and mouse with recorded action.
- [andysc/IBM-Q-System-One-3D-model](https://github.com/andysc/IBM-Q-System-One-3D-model) - 3D-printed model of IBM Q System One.

</details>

<a id="projects-by-implementation-language"></a>

## कार्यान्वयन भाषा के अनुसार परियोजनाएँ

यह पारिस्थितिकी मुख्यतः Python और TypeScript में केंद्रित है, पर टाइप्ड क्लाइंट अन्य भाषाओं में भी आते रहते हैं। यह तालिका स्वयं प्रविष्टियों से बनाई जाती है।

| भाषा       | प्रविष्टियाँ | उदाहरण                                                                                                         |
| ---------- | ------------ | -------------------------------------------------------------------------------------------------------------- |
| Python     | 162          | `typesafe-ai/system-one-adapter-python`, `typesafe-ai/typesafe-sdk-python`, `ckaraca/awesome-jev`              |
| TypeScript | 139          | `typesafe-ai/typesafe-sdk-js`, `TypeSafeAI/clarity-judge`, `AntonioCoppe/jev-harness`                          |
| JavaScript | 73           | `ziyu/sytem-one-sdk`, `Ying-Kai-Liao/jev-browser`, `arunav25/jev-mcp`                                          |
| Go         | 12           | `Gaurav-Gosain/jev-go`, `Stumble/jev-go`, `anilsenay/jev`                                                      |
| Rust       | 11           | `AkashPriyadarshii/jev-curate`, `AkashPriyadarshii/jev-seo`, `AkashPriyadarshii/jev-scout`                     |
| HTML       | 10           | `typesafe-ai/typesafe-ai.github.io`, `yzfly/awesome-jev-zh`, `vinilana/jev-eval-agent`                         |
| PHP        | 4            | `Butochnikov/laravel-typesafe-jev`, `juanlentino/jev-comment-analysis`, `juanlentino/jev-connector`            |
| CSS        | 3            | `2023Anita/jev-gpt-arena`, `AbdelStark/awesome-typesafe`, `mizzlelover/jev-hub`                                |
| Elixir     | 3            | `nshkrdotcom/typesafe_sdk`, `typesend/typesafe_ai`, `dannote/jev`                                              |
| Jupyter    | 3            | `jexp/neo4jev`, `bitnovus/jev-spam-eval`, `aamanlamba/jev-explore`                                             |
| Ruby       | 3            | `javiergradiche/ruby_llm-providers-typesafe`, `obie/ruby_decision_model`, `robzolkos/omarchy-issue-classifier` |
| Shell      | 3            | `realZachi/pg-jev`, `wotai-dev/typesafe-jev-tools`, `JYeswak/jev_playground`                                   |
| Java       | 2            | `Premo-Cloud/typesafe-sdk-java`, `Olti1947/jev-java`                                                           |
| Swift      | 2            | `gpazo/jev-vphone-cli`, `chris-wozniczek/jev-voice-control`                                                    |
| Astro      | 1            | `kong75/jev-directory`                                                                                         |
| C          | 1            | `giuliosmall/pg_typesafe`                                                                                      |
| C#         | 1            | `saibimajdi/typesafeai-dotnet-sdk`                                                                             |
| Dart       | 1            | `Bud-ro/jev-demos`                                                                                             |
| Emacs Lisp | 1            | `wakamenod/jev.el`                                                                                             |
| Haskell    | 1            | `inanna-malick/jev-dsl`                                                                                        |
| Kotlin     | 1            | `ufec/jev-block-android-ad`                                                                                    |
| Lex        | 1            | `alpibrusl/lex-judge`                                                                                          |
| Nushell    | 1            | `cablehead/jev.nu`                                                                                             |
| OpenSCAD   | 1            | `andysc/IBM-Q-System-One-3D-model`                                                                             |
| PowerShell | 1            | `omni-/ask-jev`                                                                                                |
| TeX        | 1            | `dnakhoa/jev-deferred-crispification`                                                                          |

<sub>केवल वे प्रविष्टियाँ गिनी जाती हैं जो भाषा घोषित करती हैं। अधोसंरचना, दस्तावेज़ीकरण और चर्चा वाली प्रविष्टियाँ इस तालिका से बाहर हैं।</sub>

## यह सूची अद्यतन कैसे रहती है

इस README का मुख्य भाग कोई मनुष्य संपादित नहीं करता। रिपॉज़िटरी एक निर्धारित समय-सारणी पर पाँच-चरणीय पाइपलाइन चलाती है और तभी कमिट करती है जब कुछ वास्तव में बदला हो।

<img src="assets/readme/pipeline.svg" width="100%" alt="यह सूची अद्यतन कैसे रहती है">

|             |                                                                                                                                                                                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **collect** | क्वेरी मैट्रिक्स, आधिकारिक संगठन, GitHub कोड खोज, Hacker News और Hugging Face हब पर GitHub खोज।                                                                                                                                                       |
| **curate**  | नियतात्मक और LLM-रहित, इसलिए एक ही इनपुट पर लगातार दो रन बाइट-दर-बाइट समान आउटपुट देते हैं। प्रासंगिकता दो-संकेत नियम तय करता है; नाम-टकराव (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD और समान) एक स्पष्ट, ऑडिट-योग्य सूची से बाहर रखे जाते हैं। |
| **media**   | हर परियोजना के अपने स्क्रीनशॉट और स्क्रीन रिकॉर्डिंग एकत्र करता है। संपत्तियाँ इस रिपॉज़िटरी में तभी कॉपी की जाती हैं जब परियोजना पुनर्वितरण-अनुकूल लाइसेंस घोषित करती है; अन्यथा अपस्ट्रीम URL सीधे लिंक किया जाता है और कार्ड यह बताता है।          |
| **render**  | एक ही टेम्पलेट से हर भाषा संस्करण बनाता है, इसलिए बीस README संरचना में कभी अलग नहीं हो सकते।                                                                                                                                                         |
| **audit**   | बिल्ड तब विफल करता है जब किसी प्रविष्टि में URL न हो, कोई लिंक टूटा हो, दो प्रविष्टियाँ एक ही URL दोहराती हों, या कोई README अपने निर्मित रूप से हट जाए।                                                                                              |

## योगदान

सुधार स्वागत-योग्य हैं और इस सूची को बेहतर बनाने का सबसे तेज़ तरीका हैं। अगर कोई प्रविष्टि गलत श्रेणी में है, गलत दर्जा पाई है, या किसी परियोजना को नाम-टकराव मानकर गलती से बाहर रखा गया है, तो issue या pull request खोलें — यही अंतिम श्रेणी है जहाँ स्वचालित फ़िल्टर के गलत होने की सबसे अधिक संभावना है। जोड़ना `scripts/collect.py` में स्रोत जोड़कर करना बेहतर है, README संपादित करके नहीं, क्योंकि README हर चक्र में फिर से बनाया जाता है।

---

<sub>स्वतंत्र समुदाय परियोजना। TypeSafe AI से संबद्ध नहीं, न ही उससे अनुमोदित या समीक्षित। उत्पाद व्यवहार, मूल्य, सीमाएँ और मॉडल उपनाम बिना सूचना के बदलते हैं; जो कुछ भी निर्णायक है उसे आधिकारिक दस्तावेज़ से सत्यापित करें। संपत्तियाँ उनकी अपस्ट्रीम परियोजनाओं की संपत्ति बनी रहती हैं और केवल वहीं पुनरुत्पादित की जाती हैं जहाँ लाइसेंस अनुमति देता है।</sub>

<sub>इनके द्वारा निर्मित · `render.py` · 2026-09-19T12:24:57+08:00</sub>
