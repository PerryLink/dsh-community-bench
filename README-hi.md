<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-community-bench-hero-en-dark.webp">
  <img src="docs/assets/dsh-community-bench-hero-en-light.webp" width="100%" alt="dsh-community-bench: एक सार्वजनिक रजिस्ट्री पर केवल-पढ़ने वाला Community Bench टैब — 42 प्लगइन पंक्तियाँ, 41 E0 अपरिभाषित, 1 E2 प्रोविज़नल, 0 positive measured">
</picture>

# dsh-community-bench

**`dsh-score` सार्वजनिक एविडेंस लेयर के लिए ऐप के अंदर का Community Bench टैब।**

*वही सार्वजनिक रजिस्ट्री पढ़ता है जो सब देखते हैं। कोई स्थानीय स्कोरिंग नहीं, कोई टेलीमेट्री नहीं, कोई पेड रैंक नहीं।*

[English](README.md) · [简体中文](README-zh.md) · [Español](README-es.md) · [Português](README-pt.md) · [हिन्दी](README-hi.md)

> 🧊 **2026-10-31 से फ़्रोज़न, मेंटेनेंस मोड।** कोई नया स्कोरिंग या रैंकिंग फ़ीचर नहीं; पैकेज इंस्टॉल होने योग्य बना रहता है।

[![License](https://img.shields.io/badge/license-Apache--2.0-3366CC?style=flat-square&labelColor=2B3245)](LICENSE)
[![DSH](https://img.shields.io/badge/DSH-%E2%89%A50.2.1%20%3C0.3.0-4B67B4?style=flat-square&labelColor=2B3245)](#compatibility)
[![npm](https://img.shields.io/npm/v/dsh-community-bench?style=flat-square&labelColor=2B3245&color=CB3837)](https://www.npmjs.com/package/dsh-community-bench)
[![Node](https://img.shields.io/badge/node-%5E22.19%20%7C%7C%20%3E=24-339933?style=flat-square&labelColor=2B3245)](#compatibility)

[![Stars](https://img.shields.io/github/stars/PerryLink/dsh-community-bench?style=flat-square&labelColor=2B3245)](https://github.com/PerryLink/dsh-community-bench/stargazers)
[![npm downloads](https://img.shields.io/npm/dm/dsh-community-bench?style=flat-square&labelColor=2B3245&color=CB3837)](https://www.npmjs.com/package/dsh-community-bench)
[![dshfind](https://dshfind.com/api/badge/PerryLink/dsh-community-bench?metric=downloads)](https://dshfind.com/plugins/PerryLink/dsh-community-bench?ref=badge)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-C71D23?style=flat-square&labelColor=2B3245&logo=gitee)](https://gitee.com/perrylink/dsh-community-bench)

```sh
dsh plugin --profile web add dsh-community-bench
```

</div>

<sub>समुदाय का प्लगइन, DeepSeek से संबद्ध नहीं। कैनोनिकल रिपॉज़िटरी: <https://github.com/PerryLink/dsh-community-bench> (Gitee एक मिरर है)।</sub>

---

> **स्थिति: संदर्भ कंज़्यूमर / मेंटेनेंस मोड।** कोई नया स्कोरिंग या रैंकिंग फ़ीचर नहीं। सार्वजनिक एविडेंस लेयर `dsh-score-index` है (फ़िलहाल `dsh-attention-index`; repo का नाम बदलना बाकी है)।

## यह क्या दिखाता है

- प्रति सरफ़ेस GOE (`E0`–`E5`)। मौजूदा स्नैपशॉट में: 41 पंक्तियाँ `E0 / unrated` हैं, 1 पंक्ति `E2 / provisional` है (एक null pilot); कोई positive measured पंक्ति नहीं।
- positive measured पंक्तियाँ केवल क्वालिटी ब्लॉक में; prior-only पंक्तियाँ उम्मीदवार के रूप में लेबल होती हैं, कभी `#1` नहीं।
- Prior, bench, कवरेज और **एविडेंस की पूर्णता** (विश्वास की प्रायिकता नहीं)।
- समुदाय के ध्यान वाले ब्लॉक और योगदानकर्ताओं की प्रतिष्ठा।
- सार्वजनिक एविडेंस साइट का लिंक और एक रीफ़्रेश बटन।

यह टैब एक **कंज़्यूमर** है: एविडेंस और ग्रेडिंग सार्वजनिक रजिस्ट्री में रहते हैं, इस प्लगइन में नहीं। अगर लाइव रजिस्ट्री उपलब्ध न हो, तो यह बंडल किए गए स्नैपशॉट पर लौटता है और उसे लेबल करता है।

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-community-bench-flow-v5-dark.svg">
  <img src="docs/assets/dsh-community-bench-flow-v5-light.svg" width="100%" alt="dsh-community-bench संरचना: बिल्ड में इंजेक्ट किया गया स्नैपशॉट और लाइव रजिस्ट्री की लेन normalizeRegistry() पर आकर मिलती हैं, जो top3 केवल positive E3–E5 पंक्तियों के लिए रखता है; फिर रेंडर पथ measured, provisional और अपरिभाषित उम्मीदवार ब्लॉकों में बँटता है, विफल fetch स्नैपशॉट रखता है, और स्कोरिंग वेट अपस्ट्रीम ही रहते हैं">
</picture>

*संरचना: दो लेन (बिल्ड में इंजेक्ट स्नैपशॉट और लाइव रजिस्ट्री) → एक `normalizeRegistry()` गेट → तीन एविडेंस ब्लॉक; केवल positive E3–E5 पंक्ति ही क्वालिटी स्लॉट ले सकती है, विफल fetch स्नैपशॉट रखता है, और स्कोरिंग वेट अपस्ट्रीम ही रहते हैं। डायग्राम के अंदर टोकन लेबल असली पहचानकर्ता हैं, इसलिए एक ही चित्र पाँचों भाषाओं के लिए काम आता है।*

## इंस्टॉल

```sh
dsh plugin --profile web add dsh-community-bench
```

फिर **Settings → Plugins → Community Bench** खोलें।

## कॉन्फ़िगरेशन

बिल्ड दो URL इंजेक्ट करता है (`scripts/build.mjs`):

| बिल्ड के समय एनवायरनमेंट वेरिएबल | डिफ़ॉल्ट |
|---|---|
| `BENCH_SITE_URL` | `https://perrylink.github.io/dsh-attention-index/` |
| `BENCH_REGISTRY_URL` | `https://raw.githubusercontent.com/PerryLink/dsh-attention-index/main/data/registry.json` |

अगर रजिस्ट्री कहीं और होस्ट हो, तो इन वेरिएबल के साथ फिर से बिल्ड करें।

## सीमाएँ

- बंडल किया गया स्नैपशॉट `dsh-attention-index/data/registry.json` से बनता है; यह एक कैश है, दूसरा स्कोरिंग रास्ता नहीं।
- लाइव fetch इस पर निर्भर है कि होस्ट Web ऐप से आउटबाउंड HTTPS की अनुमति दे; विफल होने पर टैब स्नैपशॉट पर ही रहता है।
- कोई स्थानीय लेखन नहीं, कोई टेलीमेट्री नहीं, कोई टूल नहीं।

## मूल्यांकन

![dsh-community-bench बिल्ड और पैकेज जाँच: `node scripts/build.mjs` का असली रन, जो 89,600 बाइट का क्लाइंट बंडल लिखता है, और फिर `npm pack --dry-run` जो प्रकाशित पैकेज में README, hero/flow मीडिया और रिकॉर्ड किया गया demo gif सूचीबद्ध करता है](docs/assets/dsh-community-bench-demo.gif)

*एनिमेटेड: रिपॉज़िटरी का अपना बिल्ड स्टेप और पैकेज का dry-run, 2026-11-21 को फिर चलाया गया। टैब एक केवल-क्लाइंट व्यू है जिसका कोई CLI नहीं, इसलिए यही इसका रन है: बंडल किया गया स्नैपशॉट `client.js` में इंजेक्ट होता है और डॉक्स मीडिया npm पैकेज के साथ जाता है। कोई नेटवर्क नहीं और कोई UI कैप्चर नहीं।*

## DSH प्लगइन परिवार

| प्रोजेक्ट | भूमिका |
|---|---|
| **[dsh-aqua-input-check](https://github.com/PerryLink/dsh-aqua-input-check)** |  |
| **[dsh-archive-check](https://github.com/PerryLink/dsh-archive-check)** |  |
| **[dsh-auto-review](https://github.com/PerryLink/dsh-auto-review)** |  |
| **[dsh-bid-ca-precheck](https://github.com/PerryLink/dsh-bid-ca-precheck)** |  |
| **[dsh-bid-qual-check](https://github.com/PerryLink/dsh-bid-qual-check)** |  |
| **[dsh-check-pack](https://github.com/PerryLink/dsh-check-pack)** |  |
| **[dsh-checkpoint-rewind](https://github.com/PerryLink/dsh-checkpoint-rewind)** |  |
| **[dsh-click](https://github.com/PerryLink/dsh-click)** |  |
| **[dsh-clinic](https://github.com/PerryLink/dsh-clinic)** |  |
| **[dsh-codemod](https://github.com/PerryLink/dsh-codemod)** |  |
| **[dsh-composer-history](https://github.com/PerryLink/dsh-composer-history)** |  |
| **[dsh-contract-stance](https://github.com/PerryLink/dsh-contract-stance)** |  |
| **[dsh-customs-doc-check](https://github.com/PerryLink/dsh-customs-doc-check)** |  |
| **[dsh-data-quality](https://github.com/PerryLink/dsh-data-quality)** |  |
| **[dsh-demurrage-ledger](https://github.com/PerryLink/dsh-demurrage-ledger)** |  |
| **[dsh-dida](https://github.com/PerryLink/dsh-dida)** |  |
| **[dsh-doublecheck](https://github.com/PerryLink/dsh-doublecheck)** |  |
| **[dsh-drill-script-check](https://github.com/PerryLink/dsh-drill-script-check)** |  |
| **[dsh-eia-guide-check](https://github.com/PerryLink/dsh-eia-guide-check)** |  |
| **[dsh-emergency-plan](https://github.com/PerryLink/dsh-emergency-plan)** |  |
| **[dsh-essay-rubric-check](https://github.com/PerryLink/dsh-essay-rubric-check)** |  |
| **[dsh-evidence-check](https://github.com/PerryLink/dsh-evidence-check)** |  |
| **[dsh-export-ctl-check](https://github.com/PerryLink/dsh-export-ctl-check)** |  |
| **[dsh-fast](https://github.com/PerryLink/dsh-fast)** |  |
| **[dsh-fmea-table-check](https://github.com/PerryLink/dsh-fmea-table-check)** |  |
| **[dsh-forecast-penalty](https://github.com/PerryLink/dsh-forecast-penalty)** |  |
| **[dsh-fund-research](https://github.com/PerryLink/dsh-fund-research)** |  |
| **[dsh-github-bot](https://github.com/PerryLink/dsh-github-bot)** |  |
| **[dsh-gongwen-flow-check](https://github.com/PerryLink/dsh-gongwen-flow-check)** |  |
| **[dsh-gongwen-word-check](https://github.com/PerryLink/dsh-gongwen-word-check)** |  |
| **[dsh-guard-plan-qc](https://github.com/PerryLink/dsh-guard-plan-qc)** |  |
| **[dsh-hazchem-check](https://github.com/PerryLink/dsh-hazchem-check)** |  |
| **[dsh-hazplan-check](https://github.com/PerryLink/dsh-hazplan-check)** |  |
| **[dsh-hidden-risk-map](https://github.com/PerryLink/dsh-hidden-risk-map)** |  |
| **[dsh-hs-classify](https://github.com/PerryLink/dsh-hs-classify)** |  |
| **[dsh-icd-rule-check](https://github.com/PerryLink/dsh-icd-rule-check)** |  |
| **[dsh-industry-research](https://github.com/PerryLink/dsh-industry-research)** |  |
| **[dsh-lawcite-adapter](https://github.com/PerryLink/dsh-lawcite-adapter)** |  |
| **[dsh-laya](https://github.com/PerryLink/dsh-laya)** |  |
| **[dsh-lc-doc-check](https://github.com/PerryLink/dsh-lc-doc-check)** |  |
| **[dsh-learning-gap-check](https://github.com/PerryLink/dsh-learning-gap-check)** |  |
| **[dsh-library](https://github.com/PerryLink/dsh-library)** |  |
| **[dsh-local-ai](https://github.com/PerryLink/dsh-local-ai)** |  |
| **[dsh-lsp-actions](https://github.com/PerryLink/dsh-lsp-actions)** |  |
| **[dsh-mask](https://github.com/PerryLink/dsh-mask)** |  |
| **[dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel)** |  |
| **[dsh-medrec-qc](https://github.com/PerryLink/dsh-medrec-qc)** |  |
| **[dsh-memento](https://github.com/PerryLink/dsh-memento)** |  |
| **[dsh-nsfc-form-check](https://github.com/PerryLink/dsh-nsfc-form-check)** |  |
| **[dsh-nurse-record-check](https://github.com/PerryLink/dsh-nurse-record-check)** |  |
| **[dsh-observe](https://github.com/PerryLink/dsh-observe)** |  |
| **[dsh-origin-rvc-check](https://github.com/PerryLink/dsh-origin-rvc-check)** |  |
| **[dsh-ota-review-check](https://github.com/PerryLink/dsh-ota-review-check)** |  |
| **[dsh-output-styles](https://github.com/PerryLink/dsh-output-styles)** |  |
| **[dsh-paper-doc-adapter](https://github.com/PerryLink/dsh-paper-doc-adapter)** |  |
| **[dsh-param-repair](https://github.com/PerryLink/dsh-param-repair)** |  |
| **[dsh-permission-rules](https://github.com/PerryLink/dsh-permission-rules)** |  |
| **[dsh-permit-report-check](https://github.com/PerryLink/dsh-permit-report-check)** |  |
| **[dsh-phocinae](https://github.com/PerryLink/dsh-phocinae)** |  |
| **[dsh-phone-inbox](https://github.com/PerryLink/dsh-phone-inbox)** |  |
| **[dsh-pipeline-check](https://github.com/PerryLink/dsh-pipeline-check)** |  |
| **[dsh-pleading-draft](https://github.com/PerryLink/dsh-pleading-draft)** |  |
| **[dsh-policy-brief-draft](https://github.com/PerryLink/dsh-policy-brief-draft)** |  |
| **[dsh-power-loss-split](https://github.com/PerryLink/dsh-power-loss-split)** |  |
| **[dsh-power-ticket-check](https://github.com/PerryLink/dsh-power-ticket-check)** |  |
| **[dsh-ppap-check](https://github.com/PerryLink/dsh-ppap-check)** |  |
| **[dsh-primer](https://github.com/PerryLink/dsh-primer)** |  |
| **[dsh-protest-deadline](https://github.com/PerryLink/dsh-protest-deadline)** |  |
| **[dsh-railway-window](https://github.com/PerryLink/dsh-railway-window)** |  |
| **[dsh-repair-order-qc](https://github.com/PerryLink/dsh-repair-order-qc)** |  |
| **[dsh-research-report](https://github.com/PerryLink/dsh-research-report)** |  |
| **[dsh-review-reply-check](https://github.com/PerryLink/dsh-review-reply-check)** |  |
| **[dsh-rulefile-check](https://github.com/PerryLink/dsh-rulefile-check)** |  |
| **[dsh-safety-brief-check](https://github.com/PerryLink/dsh-safety-brief-check)** |  |
| **[dsh-scaffold](https://github.com/PerryLink/dsh-scaffold)** |  |
| **[dsh-score](https://github.com/PerryLink/dsh-score)** | पाँच आयामों वाला स्थानीय प्रायर इंस्पेक्टर |
| **[dsh-security-pack](https://github.com/PerryLink/dsh-security-pack)** |  |
| **[dsh-session-sync](https://github.com/PerryLink/dsh-session-sync)** |  |
| **[dsh-site-log-check](https://github.com/PerryLink/dsh-site-log-check)** |  |
| **[dsh-soe-decision-check](https://github.com/PerryLink/dsh-soe-decision-check)** |  |
| **[dsh-soilwater-check](https://github.com/PerryLink/dsh-soilwater-check)** |  |
| **[dsh-sop-sync-check](https://github.com/PerryLink/dsh-sop-sync-check)** |  |
| **[dsh-spc-gbt-adapter](https://github.com/PerryLink/dsh-spc-gbt-adapter)** |  |
| **[dsh-talk](https://github.com/PerryLink/dsh-talk)** |  |
| **[dsh-tender-extract](https://github.com/PerryLink/dsh-tender-extract)** |  |
| **[dsh-tender-matrix](https://github.com/PerryLink/dsh-tender-matrix)** |  |
| **[dsh-test-drive](https://github.com/PerryLink/dsh-test-drive)** |  |
| **[dsh-warranty-calc](https://github.com/PerryLink/dsh-warranty-calc)** |  |
| **[dsh-autotier](https://github.com/PerryLink/dsh-autotier)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-budget](https://github.com/PerryLink/dsh-budget)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-cert-mcp](https://github.com/PerryLink/dsh-cert-mcp)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-claude-move](https://github.com/PerryLink/dsh-claude-move)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-community-bench](https://github.com/PerryLink/dsh-community-bench)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-defend](https://github.com/PerryLink/dsh-defend)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-draw](https://github.com/PerryLink/dsh-draw)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-reach](https://github.com/PerryLink/dsh-reach)** | 🧊 फ़्रोज़न — रिपॉज़िटरी README देखें |
| **[dsh-background-agents](https://github.com/PerryLink/dsh-background-agents)** | 🚫 सेवानिवृत्त — रिपॉज़िटरी README देखें |
| **[dsh-session-pin](https://github.com/PerryLink/dsh-session-pin)** | 🚫 सेवानिवृत्त — रिपॉज़िटरी README देखें |
| **[dsh-team-rooms](https://github.com/PerryLink/dsh-team-rooms)** | 🚫 सेवानिवृत्त — रिपॉज़िटरी README देखें |

## ⭐ अगर इससे मदद मिली

यह प्लगइन [DSH प्लगइन परिवार](https://github.com/PerryLink) का हिस्सा है (40+ प्लगइन, सभी Apache-2.0)। अगर यह उपयोगी लगे, तो **एक स्टार अगले व्यक्ति को इसे खोजने में मदद करता है** — इसके पीछे कुछ भी बंद नहीं है।

## लाइसेंस

Apache-2.0.
