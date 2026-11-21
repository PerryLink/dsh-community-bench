<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-community-bench-hero-en-dark.webp">
  <img src="docs/assets/dsh-community-bench-hero-en-light.webp" width="100%" alt="dsh-community-bench: una pestaña Community Bench de solo lectura sobre un único registro público — 42 filas de plugins, 41 E0 sin calificar, 1 E2 provisional, 0 positive measured">
</picture>

# dsh-community-bench

**Pestaña Community Bench dentro de la app para la capa de evidencia pública de `dsh-score`.**

*Lee el mismo registro público que ve todo el mundo. Sin puntuación local, sin telemetría, sin rango pagado.*

[English](README.md) · [简体中文](README-zh.md) · [Español](README-es.md) · [Português](README-pt.md) · [हिन्दी](README-hi.md)

> 🧊 **CONGELADO — 2026-10-31. Modo de mantenimiento.** Sin nuevas funciones de puntuación ni de ranking; el paquete sigue siendo instalable.

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

<sub>Plugin de la comunidad, no afiliado a DeepSeek. Repositorio canónico: <https://github.com/PerryLink/dsh-community-bench> (Gitee es un espejo).</sub>

---

> **Estado: consumidor de referencia / modo de mantenimiento.** Sin nuevas funciones de puntuación ni de ranking. La capa de evidencia pública es `dsh-score-index` (actualmente `dsh-attention-index`; el cambio de nombre del repo está pendiente).

## Qué muestra

- GOE (`E0`–`E5`) por superficie. En la instantánea actual: 41 filas son `E0 / unrated`, 1 fila es `E2 / provisional` (un pilot nulo); ninguna fila positive measured.
- Las filas positive measured solo aparecen en el bloque de calidad; las filas prior-only se etiquetan como candidatas, nunca como `#1`.
- Prior, bench, cobertura y **completitud de la evidencia** (no una probabilidad de confianza).
- Bloques de atención de la comunidad y reputación de colaboradores.
- Enlace al sitio público de evidencia y un botón de actualización.

La pestaña es un **consumidor**: la evidencia y la calificación viven en el registro público, no en este plugin. Si el registro en vivo no es accesible, vuelve a la instantánea incluida y lo indica.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/dsh-community-bench-flow-v5-dark.svg">
  <img src="docs/assets/dsh-community-bench-flow-v5-light.svg" width="100%" alt="dsh-community-bench estructura: la instantánea inyectada en la compilación y la vía del registro en vivo convergen en normalizeRegistry(), que conserva top3 solo para filas positive E3–E5; luego la ruta de render se divide en bloques measured, provisional y candidatas sin calificar, un fetch fallido mantiene la instantánea, y los pesos de puntuación se quedan aguas arriba">
</picture>

*Estructura: dos vías (instantánea inyectada en la compilación y registro en vivo) → una puerta `normalizeRegistry()` → tres bloques de evidencia; solo una fila positive E3–E5 puede ocupar una ranura de calidad, un fetch fallido mantiene la instantánea y los pesos de puntuación se quedan aguas arriba. Las etiquetas de token dentro del diagrama son identificadores reales, así que la misma imagen sirve para los cinco idiomas.*

## Instalación

```sh
dsh plugin --profile web add dsh-community-bench
```

Luego abre **Settings → Plugins → Community Bench**.

## Configuración

La compilación inyecta dos URL (`scripts/build.mjs`):

| Variable de entorno en la compilación | Valor por defecto |
|---|---|
| `BENCH_SITE_URL` | `https://perrylink.github.io/dsh-attention-index/` |
| `BENCH_REGISTRY_URL` | `https://raw.githubusercontent.com/PerryLink/dsh-attention-index/main/data/registry.json` |

Si el registro se aloja en otro sitio, recompila con esas variables.

## Límites

- La instantánea incluida se genera a partir de `dsh-attention-index/data/registry.json`; es una caché, no una segunda vía de puntuación.
- La consulta en vivo depende de que el host permita HTTPS saliente desde la Web app; si falla, la pestaña se queda en la instantánea.
- Sin escrituras locales, sin telemetría, sin herramientas.

## Evaluación

![dsh-community-bench compilación y comprobación del paquete: una ejecución real de `node scripts/build.mjs` que escribe el bundle de cliente de 89.600 bytes, y después `npm pack --dry-run` listando el README, los medios hero/flow y el gif de demostración grabado en el paquete publicado](docs/assets/dsh-community-bench-demo.gif)

*Animado: el propio paso de compilación del repositorio y un dry-run del paquete, reejecutados el 2026-11-21. La pestaña es una vista solo de cliente sin CLI, así que esta es su ejecución: la instantánea incluida se inyecta en `client.js` y los medios de documentación viajan con el paquete npm. No hay red ni captura de UI.*

## La familia de plugins DSH

| Proyecto | Rol |
|---|---|
| **[dsh-score](https://github.com/PerryLink/dsh-score)** | Inspector local de priors de cinco dimensiones |
| **[dsh-score index](https://github.com/PerryLink/dsh-attention-index)** | Capa de evidencia pública (E0–E5, API, signals) |
| **dsh-community-bench** (este plugin) | Consumidor dentro de la app |
| **[dsh-kit](https://github.com/PerryLink/dsh-kit)** | Paquete de inicio de la familia en un comando |

## ⭐ Si te ha resultado útil

Este plugin forma parte de una [familia de plugins DSH](https://github.com/PerryLink) (40+, todos Apache-2.0). Si te resulta útil, **una estrella ayuda a que la siguiente persona lo encuentre** — nada está bloqueado detrás de ella.

## Licencia

Apache-2.0.
