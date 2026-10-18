<div align="center">

# 🧪 dsh-community-bench

**In-app Community Bench tab for the `dsh-score` public evidence layer.**

*Reads the same public registry everyone sees. No local scoring, no telemetry, no paid rank.*

[![npm](https://img.shields.io/npm/v/dsh-community-bench)](https://www.npmjs.com/package/dsh-community-bench)
[![npm downloads](https://img.shields.io/npm/dm/dsh-community-bench)](https://www.npmjs.com/package/dsh-community-bench)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/dsh-community-bench)
[![GitCode](https://img.shields.io/badge/GitCode-mirror-2f6feb)](https://gitcode.com/PerryLink/dsh-community-bench)
[![DSH plugin](https://img.shields.io/badge/dsh--plugin-✅-green)](https://github.com/topics/dsh-plugin)

[English](README.md) · [简体中文](README-zh.md)

```sh
dsh plugin --profile web add dsh-community-bench
```

</div>

---

<img src="docs/assets/dsh-score-hero.png" width="100%" alt="dsh-score public evidence: E0 unrated, E2 provisional, no quality #1" />

<img src="docs/assets/dsh-score-demo.gif" width="100%" alt="Animated dsh-score demo" />

> **Status: reference consumer / maintenance mode.** No new scoring or ranking
> features. The public evidence layer is `dsh-score-index` (currently
> `dsh-attention-index`; repo rename pending).

## What it shows

- GOE (`E0`–`E5`) per surface. At 0.2.1: 41 rows are `E0 / unrated`, 1 row is `E2 / provisional` (a null pilot); no positive measured row.
- Positive measured rows only in the quality block; prior-only rows are labelled candidates, never `#1`.
- Prior, bench, coverage and **evidence completeness** (not a confidence probability).
- Community attention blocks and contributor reputation.
- Link to the public evidence site and a refresh button.

The tab is a **consumer**: evidence and grading live in the public registry, not in this plugin. If the live registry is unreachable, it falls back to the bundled snapshot and labels it.

## Install

```sh
dsh plugin --profile web add dsh-community-bench
```

Then open **Settings → Plugins → Community Bench**.

## Configuration

The build injects two URLs (`scripts/build.mjs`):

| Env at build time | Default |
|---|---|
| `BENCH_SITE_URL` | `https://perrylink.github.io/dsh-attention-index/` |
| `BENCH_REGISTRY_URL` | `https://raw.githubusercontent.com/PerryLink/dsh-attention-index/main/data/registry.json` |

If the registry is hosted elsewhere, rebuild with those variables.

## Limits

- The bundled snapshot is generated from `dsh-attention-index/data/registry.json`; it is a cache, not a second scoring path.
- The live fetch depends on the host allowing outbound HTTPS from the Web app; on failure the tab stays on the snapshot.
- No local writes, no telemetry, no tools.

## DSH plugin family

| Project | Role |
|---|---|
| **[dsh-score](https://github.com/PerryLink/dsh-score)** | Local five-dimension prior inspector |
| **[dsh-score index](https://github.com/PerryLink/dsh-attention-index)** | Public evidence layer (E0–E5, API, signals) |
| **dsh-community-bench** (this plugin) | In-app consumer |
| **[dsh-kit](https://github.com/PerryLink/dsh-kit)** | One-command family starter |

## ⭐ 如果它帮到了你

这个插件是 [DSH 插件家族](https://github.com/PerryLink)的一员（40+ 个，全部 Apache-2.0）。如果你在用，**给个 star** —— 它不会解锁任何功能，但会让下一个人在搜索里更容易找到它。

## License

Apache-2.0.
