<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-community-bench-hero-en-dark.webp">
  <img src="docs/assets/dsh-community-bench-hero-en-light.webp" width="100%" alt="dsh-community-bench: uma aba Community Bench somente leitura sobre um único registro público — 42 linhas de plugins, 41 E0 sem classificação, 1 E2 provisório, 0 positive measured">
</picture>

# dsh-community-bench

**Aba Community Bench dentro do app para a camada de evidência pública do `dsh-score`.**

*Lê o mesmo registro público que todo mundo vê. Sem pontuação local, sem telemetria, sem ranking pago.*

[English](README.md) · [简体中文](README-zh.md) · [Español](README-es.md) · [Português](README-pt.md) · [हिन्दी](README-hi.md)

> 🧊 **CONGELADO — 2026-10-31. Modo de manutenção.** Sem novos recursos de pontuação ou ranking; o pacote continua instalável.

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

<sub>Plugin da comunidade, não afiliado à DeepSeek. Repositório canônico: <https://github.com/PerryLink/dsh-community-bench> (o Gitee é um espelho).</sub>

---

> **Status: consumidor de referência / modo de manutenção.** Sem novos recursos de pontuação ou ranking. A camada de evidência pública é o `dsh-score-index` (atualmente `dsh-attention-index`; a renomeação do repo está pendente).

## O que mostra

- GOE (`E0`–`E5`) por superfície. No snapshot atual: 41 linhas são `E0 / unrated`, 1 linha é `E2 / provisional` (um pilot nulo); nenhuma linha positive measured.
- Linhas positive measured só no bloco de qualidade; linhas prior-only são rotuladas como candidatas, nunca como `#1`.
- Prior, bench, cobertura e **completude da evidência** (não uma probabilidade de confiança).
- Blocos de atenção da comunidade e reputação de contribuidores.
- Link para o site público de evidência e um botão de atualização.

A aba é um **consumidor**: a evidência e a classificação vivem no registro público, não neste plugin. Se o registro ao vivo estiver inacessível, ela volta ao snapshot incluído e o rotula.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-community-bench-flow-v5-dark.svg">
  <img src="docs/assets/dsh-community-bench-flow-v5-light.svg" width="100%" alt="dsh-community-bench estrutura: o snapshot injetado no build e a via do registro ao vivo convergem em normalizeRegistry(), que mantém top3 apenas para linhas positive E3–E5; o caminho de renderização então se divide em blocos measured, provisional e candidatas sem classificação, um fetch que falha mantém o snapshot, e os pesos de pontuação ficam a montante">
</picture>

*Estrutura: duas vias (snapshot injetado no build e registro ao vivo) → um portão `normalizeRegistry()` → três blocos de evidência; só uma linha positive E3–E5 pode ocupar uma vaga de qualidade, um fetch que falha mantém o snapshot, e os pesos de pontuação ficam a montante. Os rótulos de token dentro do diagrama são identificadores reais, então a mesma imagem serve aos cinco idiomas.*

## Instalação

```sh
dsh plugin --profile web add dsh-community-bench
```

Depois abra **Settings → Plugins → Community Bench**.

## Configuração

O build injeta duas URLs (`scripts/build.mjs`):

| Variável de ambiente no build | Padrão |
|---|---|
| `BENCH_SITE_URL` | `https://perrylink.github.io/dsh-attention-index/` |
| `BENCH_REGISTRY_URL` | `https://raw.githubusercontent.com/PerryLink/dsh-attention-index/main/data/registry.json` |

Se o registro for hospedado em outro lugar, rebuild com essas variáveis.

## Limites

- O snapshot incluído é gerado a partir de `dsh-attention-index/data/registry.json`; é um cache, não um segundo caminho de pontuação.
- O fetch ao vivo depende de o host permitir HTTPS de saída a partir do app Web; em caso de falha, a aba permanece no snapshot.
- Sem escritas locais, sem telemetria, sem ferramentas.

## Avaliação

![dsh-community-bench build e conferência do pacote: uma execução real de `node scripts/build.mjs` gravando o bundle de cliente de 89.600 bytes, e depois `npm pack --dry-run` listando o README, as mídias hero/flow e o gif de demonstração gravado no pacote publicado](docs/assets/dsh-community-bench-demo.gif)

*Animado: o próprio passo de build do repositório e um dry-run do pacote, reexecutados em 2026-11-21. A aba é uma visão somente de cliente sem CLI, então esta é a sua execução: o snapshot incluído é injetado em `client.js` e as mídias da documentação viajam com o pacote npm. Sem rede e sem captura de UI.*

## A família de plugins DSH

| Projeto | Papel |
|---|---|
| **[dsh-score](https://github.com/PerryLink/dsh-score)** | Inspetor local de priors de cinco dimensões |
| **[dsh-score index](https://github.com/PerryLink/dsh-attention-index)** | Camada de evidência pública (E0–E5, API, signals) |
| **dsh-community-bench** (este plugin) | Consumidor dentro do app |
| **[dsh-kit](https://github.com/PerryLink/dsh-kit)** | Pacote inicial da família em um comando |

## ⭐ Se foi útil para você

Este plugin faz parte de uma [família de plugins DSH](https://github.com/PerryLink) (40+, todos Apache-2.0). Se for útil, **uma estrela ajuda a próxima pessoa a encontrá-lo** — nada fica bloqueado atrás dela.

## Licença

Apache-2.0.
