/**
 * Build the client bundle by injecting the public registry snapshot.
 *
 * The consumer never computes scores. It renders the public registry and, when
 * the live URL is reachable, refreshes to the latest one.
 */

import { readFileSync, writeFileSync } from 'node:fs'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..')
const snapshot = JSON.parse(readFileSync(join(ROOT, 'snapshot.json'), 'utf8'))
const template = readFileSync(join(ROOT, 'client.template.js'), 'utf8')
const siteUrl = process.env.BENCH_SITE_URL ?? 'https://perrylink.github.io/dsh-attention-index/'
const registryUrl = process.env.BENCH_REGISTRY_URL ?? 'https://raw.githubusercontent.com/PerryLink/dsh-attention-index/main/data/registry.json'
const client = template
  .replace('__SNAPSHOT__', JSON.stringify(snapshot))
  .replace('__SITE_URL__', JSON.stringify(siteUrl))
  .replace('__REGISTRY_URL__', JSON.stringify(registryUrl))
writeFileSync(join(ROOT, 'client.js'), client)
console.log(`wrote client.js (${client.length} bytes)`)
