# Changelog

## 0.2.5 — 2026-10-18

- Refresh snapshot to the 30-result network-isolated pilot.
- No client behavior change.

## 0.2.4 — 2026-10-18

- Render E2 provisional and unrated candidate rows; never show a rank for them.
- Refresh snapshot to the 30-result sandboxed pilot.
- Fix slot registration, package exports, icon metadata and inject edges.

## 0.2.3 — 2026-10-18

- Use absolute raw URLs for README images so npm renders them.

## 0.2.2 — 2026-10-18

- Family-style README with hero image and animated demo.
- Add `docs/assets` to the package so npm renders the README images.
- No scoring or client behavior change.

## 0.2.1 — 2026-10-18

- Snapshot the first signed E2 pilot: 41 E0/unrated + 1 E2 provisional null.
- Clarify that "no positive measured" is different from "no measured at all".
- No local scoring and no prior-only #1.

## 0.2.0 — 2026-10-18

- Brand the consumer as part of `dsh-score`.
- Show GOE (`E0`–`E5`) and `unrated`; no prior-only `#1` or quality rank.
- If a surface has no positive measured result, render "No measured evidence yet" instead of prior cards.
- Relabel confidence as evidence completeness; show the discovery score separately.

## 0.1.1 — 2026-10-18

- npm-first install docs and live registry links.
- Add Chinese README; document Gitee and GitCode mirrors.

## 0.1.0 — 2026-10-18

- Initial public release.
- Settings → Plugins → Community Bench tab.
- Reads the public `dsh-attention-index` registry; no local scoring.
- Bundled snapshot fallback when the live registry is unreachable.
