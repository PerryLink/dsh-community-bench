# dsh-community-bench

**In-app Community Bench tab for the `dsh-score` public evidence layer.** It reads the public [dsh-score](https://perrylink.github.io/dsh-attention-index/) registry and shows the same evidence everyone sees. It does **not** compute a per-user score.

> **Status: reference consumer / maintenance mode.** No new scoring or ranking
> features. The public evidence layer is `dsh-score-index` (currently
> `dsh-attention-index`; repo rename pending).

[![npm](https://img.shields.io/npm/v/dsh-community-bench)](https://www.npmjs.com/package/dsh-community-bench)
[![npm downloads](https://img.shields.io/npm/dm/dsh-community-bench)](https://www.npmjs.com/package/dsh-community-bench)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/dsh-community-bench)
[![GitCode](https://img.shields.io/badge/GitCode-mirror-2f6feb)](https://gitcode.com/PerryLink/dsh-community-bench)
[![DSH plugin](https://img.shields.io/badge/dsh--plugin-✅-green)](https://github.com/topics/dsh-plugin)

## What it shows

- GOE (`E0`–`E5`) per surface. At v0.2 every row is `E0 / unrated`.
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

## License

Apache-2.0.
