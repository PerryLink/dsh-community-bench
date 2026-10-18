# dsh-community-bench

**DeepSeek Harness 的应用内社区基准标签页，面向 `dsh-score` 公共证据层。** 它读取公开的 [dsh-score](https://perrylink.github.io/dsh-attention-index/) registry，展示所有人看到的同一份证据。它**不在本地算分**。

> **状态：参考消费者 / 维护模式。** 不再新增评分或排名功能。公共证据层是
> `dsh-score-index`（当前为 `dsh-attention-index`；repo 改名待执行）。

[![npm](https://img.shields.io/npm/v/dsh-community-bench)](https://www.npmjs.com/package/dsh-community-bench)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/dsh-community-bench)
[![GitCode](https://img.shields.io/badge/GitCode-mirror-2f6feb)](https://gitcode.com/PerryLink/dsh-community-bench)
[![DSH plugin](https://img.shields.io/badge/dsh--plugin-✅-green)](https://github.com/topics/dsh-plugin)

## 展示什么

- 每个能力面的 GOE（`E0`–`E5`）。v0.2 里所有行都是 `E0 / unrated`。
- 只有 positive measured 进入质量块；先验行是明确标注的候选，永远不是 `#1`。
- prior、bench、覆盖率和**证据完整度**（不是置信概率）。
- 社区注意力席位和贡献者声誉。
- 公共证据页链接和刷新按钮。

这个标签页只是**消费端**：证据和评级都在公共 registry 里，不在本插件里。在线 registry 不可达时回退到内置快照，并明确标注。

## 安装

```sh
dsh plugin --profile web add dsh-community-bench
```

然后打开 **Settings → Plugins → Community Bench**。

## 配置

构建时注入两个 URL（`scripts/build.mjs`）：

| 构建环境变量 | 默认值 |
|---|---|
| `BENCH_SITE_URL` | `https://perrylink.github.io/dsh-attention-index/` |
| `BENCH_REGISTRY_URL` | `https://raw.githubusercontent.com/PerryLink/dsh-attention-index/main/data/registry.json` |

如果 registry 部署在别处，用这两个变量重新构建。

## 边界

- 内置快照来自 `dsh-attention-index/data/registry.json`，是缓存，不是第二套打分。
- 在线刷新依赖 Web 应用允许出站 HTTPS；失败时停留在快照。
- 不写本地文件、不上报 telemetry、不注册工具。

## License

Apache-2.0。
