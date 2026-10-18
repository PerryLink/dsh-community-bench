# dsh-community-bench

**In-app Community Bench tab for DeepSeek Harness.** It reads the public, task-conditioned [DSH Community Bench](https://perrylink.github.io/dsh-attention-index/) registry and shows the same score everyone sees. It does **not** compute a per-user score.

[![npm](https://img.shields.io/npm/v/dsh-community-bench)](https://www.npmjs.com/package/dsh-community-bench)
[![npm downloads](https://img.shields.io/npm/dm/dsh-community-bench)](https://www.npmjs.com/package/dsh-community-bench)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![DSH plugin](https://img.shields.io/badge/dsh--plugin-✅-green)](https://github.com/topics/dsh-plugin)

## What it shows

- Top 3 per capability surface (memory, vision, Office, browser, orchestration, safety, MCP, remote, dev, voice, research, UI, desktop).
- Public score / 100 (measured) or / 60 (prior-only), with the tier, prior, bench, coverage and confidence.
- Community attention blocks and contributor reputation.
- Link to the public leaderboard and a refresh button.

The tab is a **consumer**: measurement and allocation live in the public registry, not in this plugin. If the live registry is unreachable, it falls back to the bundled snapshot and labels it.

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
