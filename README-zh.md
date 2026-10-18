# dsh-community-bench

**DeepSeek Harness 的应用内社区基准标签页。** 它读取公开的、按任务条件计算的 [DSH Community Bench](https://perrylink.github.io/dsh-attention-index/) registry，展示所有人看到的同一份分数。它**不在本地算分**。

[![npm](https://img.shields.io/npm/v/dsh-community-bench)](https://www.npmjs.com/package/dsh-community-bench)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/dsh-community-bench)
[![GitCode](https://img.shields.io/badge/GitCode-mirror-2f6feb)](https://gitcode.com/PerryLink/dsh-community-bench)
[![DSH plugin](https://img.shields.io/badge/dsh--plugin-✅-green)](https://github.com/topics/dsh-plugin)

## 展示什么

- 每个能力面的前 3 名（记忆、视觉、Office、浏览器、编排、安全、MCP、远程、开发、语音、研究、UI、桌面）。
- 社区分：有实测为 0–100，仅有先验为 0–60；同时展示 tier、prior、bench、覆盖率和置信度。
- 社区注意力席位和贡献者声誉。
- 公共排行榜链接和刷新按钮。

这个标签页只是**消费端**：测量和分配都在公共 registry 里，不在本插件里。在线 registry 不可达时回退到内置快照，并明确标注。

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
