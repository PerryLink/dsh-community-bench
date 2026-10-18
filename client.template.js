window.__ModuleLoader__.load({
  id: 'dsh-community-bench',
  factory(require) {
    const React = require('react')
    const h = React.createElement

    const NS = 'dsh-community-bench'
    const SNAPSHOT = __SNAPSHOT__
    const SITE_URL = __SITE_URL__
    const REGISTRY_URL = __REGISTRY_URL__

    const en = {
      tab: 'Community Bench',
      title: 'dsh-score',
      subtitle: 'Public evidence. Prior-only rows are unrated; no local scoring. Same registry for everyone.',
      live: 'live registry',
      snapshot: 'bundled snapshot',
      refresh: 'Refresh',
      refreshing: 'Refreshing…',
      surface: 'Capability',
      score: 'GOE',
      tier: 'Tier',
      prior: 'prior',
      measured: 'measured',
      unrated: 'unrated',
      bench: 'bench',
      coverage: 'coverage',
      confidence: 'evidence completeness',
      contributors: 'Contributors',
      noContributors: 'No public contribution receipts yet.',
      noMeasured: 'No positive measured evidence yet. Prior rows are candidates, not a quality rank.',
      openSite: 'Open public evidence',
      generated: 'Generated',
      error: 'Could not refresh the public registry; showing the bundled snapshot.',
      note: 'This tab only reads the public registry. It does not compute a per-user score.',
      top: 'Candidates',
    }
    const zh = {
      tab: '社区基准',
      title: 'dsh-score',
      subtitle: '公开证据。先验行未评级；不在本地算分。所有人看同一份 registry。',
      live: '在线 registry',
      snapshot: '内置快照',
      refresh: '刷新',
      refreshing: '刷新中…',
      surface: '能力面',
      score: 'GOE',
      tier: '证据',
      prior: '先验',
      measured: '实测',
      unrated: '未评级',
      bench: '实测分',
      coverage: '覆盖',
      confidence: '证据完整度',
      contributors: '贡献者',
      noContributors: '还没有公开贡献记录。',
      noMeasured: '还没有 positive measured 证据。先验行只是候选，不是质量排名。',
      openSite: '打开公共证据页',
      generated: '生成时间',
      error: '刷新公共 registry 失败，显示内置快照。',
      note: '本标签页只读公共 registry，不计算个人分数。',
      top: '候选',
    }

    function normalizeRegistry(input) {
      const surfaces = Array.isArray(input?.surfaces) ? input.surfaces.map(surface => ({
        ...surface,
        top3: Array.isArray(surface.top3) ? surface.top3 : (Array.isArray(surface.leaderboard) ? surface.leaderboard.slice(0, 3) : []),
      })) : []
      return { ...input, surfaces }
    }

    const styles = {
      root: { display: 'flex', flexDirection: 'column', gap: '14px', minWidth: 0, color: 'var(--dsw-alias-label-primary)' },
      header: { display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '16px', flexWrap: 'wrap' },
      title: { margin: 0, fontSize: '18px', lineHeight: '26px', fontWeight: 700 },
      subtitle: { margin: '4px 0 0', color: 'var(--dsw-alias-label-secondary)', fontSize: '12px', lineHeight: '18px' },
      toolbar: { display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' },
      button: { font: 'inherit', fontSize: '12px', padding: '4px 10px', borderRadius: '6px', border: '1px solid var(--dsw-alias-border-l3)', background: 'var(--dsw-alias-bg-layer-1)', color: 'var(--dsw-alias-label-primary)', cursor: 'pointer' },
      stats: { display: 'grid', gridTemplateColumns: 'repeat(4, minmax(0, 1fr))', gap: '8px' },
      stat: { border: '1px solid var(--dsw-alias-border-l3)', borderRadius: '8px', padding: '8px 10px', background: 'var(--dsw-alias-bg-layer-1)' },
      statValue: { fontSize: '18px', fontWeight: 700, lineHeight: '24px' },
      statLabel: { color: 'var(--dsw-alias-label-secondary)', fontSize: '11px' },
      tabs: { display: 'flex', flexWrap: 'wrap', gap: '4px', borderBottom: '1px solid var(--dsw-alias-border-l3)', paddingBottom: '8px' },
      tab: { font: 'inherit', fontSize: '12px', padding: '4px 8px', borderRadius: '6px', border: '1px solid transparent', background: 'transparent', color: 'var(--dsw-alias-label-secondary)', cursor: 'pointer' },
      tabActive: { background: 'var(--dsw-alias-bg-layer-2)', borderColor: 'var(--dsw-alias-border-l3)', color: 'var(--dsw-alias-label-primary)', fontWeight: 600 },
      note: { margin: 0, padding: '8px 10px', borderRadius: '6px', background: 'var(--dsw-alias-bg-layer-2)', color: 'var(--dsw-alias-label-secondary)', fontSize: '12px', lineHeight: '18px' },
      cards: { display: 'grid', gridTemplateColumns: 'repeat(3, minmax(0, 1fr))', gap: '8px' },
      card: { border: '1px solid var(--dsw-alias-border-l3)', borderRadius: '8px', padding: '10px', background: 'var(--dsw-alias-bg-layer-1)', minWidth: 0 },
      cardTop: { display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '6px' },
      rank: { color: 'var(--dsw-alias-label-secondary)', fontSize: '11px', fontWeight: 700 },
      chip: { fontSize: '10px', padding: '1px 6px', borderRadius: '999px', background: 'var(--dsw-alias-bg-layer-2)', color: 'var(--dsw-alias-label-secondary)' },
      chipMeasured: { fontSize: '10px', padding: '1px 6px', borderRadius: '999px', background: 'color-mix(in srgb, #16845b 14%, transparent)', color: '#16845b' },
      name: { margin: '6px 0 0', fontSize: '13px', fontWeight: 700, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' },
      author: { color: 'var(--dsw-alias-label-secondary)', fontSize: '11px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' },
      score: { margin: '8px 0 2px', fontSize: '22px', lineHeight: '28px', fontWeight: 800 },
      small: { fontSize: '11px', fontWeight: 500, color: 'var(--dsw-alias-label-secondary)' },
      meta: { color: 'var(--dsw-alias-label-secondary)', fontSize: '11px', lineHeight: '17px' },
      link: { color: 'var(--dsw-alias-brand-primary)', textDecoration: 'none', fontSize: '11px' },
      contributors: { display: 'flex', flexDirection: 'column', gap: '4px' },
      contributor: { display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: '8px', padding: '6px 8px', border: '1px solid var(--dsw-alias-border-l3)', borderRadius: '6px', fontSize: '12px' },
    }

    function formatPct(value) {
      return `${Math.round((Number(value) || 0) * 100)}%`
    }

    function scoreOf(row) {
      if (row?.unrated === true || row?.evidenceGrade === 'E0') return 'E0 · unrated'
      const scale = row.scoreScale ?? (row.tier === 'measured' ? 100 : 60)
      return `${Number(row.score ?? 0).toFixed(1)}/${scale}`
    }

    function CommunityBenchTab(props) {
      const t = typeof props.t === 'function' ? props.t : (key) => zh[key] ?? en[key] ?? key
      const [data, setData] = React.useState(() => normalizeRegistry(SNAPSHOT))
      const [status, setStatus] = React.useState('snapshot')
      const [surfaceId, setSurfaceId] = React.useState(() => data.surfaces[0]?.id ?? 'memory')
      const [error, setError] = React.useState('')
      const [busy, setBusy] = React.useState(false)

      const refresh = React.useCallback(async () => {
        setBusy(true)
        setError('')
        try {
          const response = await fetch(REGISTRY_URL, { cache: 'no-store' })
          if (!response.ok) throw new Error(`HTTP ${response.status}`)
          const live = normalizeRegistry(await response.json())
          setData(live)
          setStatus('live')
        } catch (failure) {
          setStatus('snapshot')
          setError(String(failure instanceof Error ? failure.message : failure))
        } finally {
          setBusy(false)
        }
      }, [])

      React.useEffect(() => { void refresh() }, [refresh])

      const surface = data.surfaces.find(item => item.id === surfaceId) ?? data.surfaces[0]
      const measured = surface?.top3?.filter(row => row.tier === 'measured').length ?? 0
      const measuredTotal = data.stats?.measuredPlugins ?? 0

      return h('div', { 'data-dsh-community-bench': '', style: styles.root },
        h('div', { style: styles.header },
          h('div', { style: { minWidth: 0 } },
            h('h2', { style: styles.title }, t('title')),
            h('p', { style: styles.subtitle }, t('subtitle')),
          ),
          h('div', { style: styles.toolbar },
            h('span', { style: styles.chip }, status === 'live' ? t('live') : t('snapshot')),
            h('button', { type: 'button', style: styles.button, onClick: () => { void refresh() }, disabled: busy }, busy ? t('refreshing') : t('refresh')),
            h('a', { style: { ...styles.button, textDecoration: 'none' }, href: SITE_URL, target: '_blank', rel: 'noreferrer' }, t('openSite')),
          ),
        ),
        h('div', { style: styles.stats },
          h('div', { style: styles.stat }, h('div', { style: styles.statValue }, String(data.stats?.plugins ?? 0)), h('div', { style: styles.statLabel }, 'plugins')),
          h('div', { style: styles.stat }, h('div', { style: styles.statValue }, String(measuredTotal)), h('div', { style: styles.statLabel }, t('measured'))),
          h('div', { style: styles.stat }, h('div', { style: styles.statValue }, String(data.stats?.unratedPlugins ?? Math.max(0, (data.stats?.plugins ?? 0) - measuredTotal))), h('div', { style: styles.statLabel }, t('unrated'))),
          h('div', { style: styles.stat }, h('div', { style: styles.statValue }, String(data.stats?.surfaces ?? 0)), h('div', { style: styles.statLabel }, t('surface'))),
        ),
        h('div', { style: styles.tabs }, (data.surfaces ?? []).map(item => h('button', {
          key: item.id,
          type: 'button',
          style: { ...styles.tab, ...(item.id === surface?.id ? styles.tabActive : {}) },
          onClick: () => setSurfaceId(item.id),
        }, item.zh ?? item.label ?? item.id))),
        h('p', { style: styles.note }, `${t('note')} ${surface?.note ?? ''}`),
        error.length > 0 ? h('p', { style: { ...styles.note, color: 'var(--dsw-alias-label-secondary)' } }, `${t('error')} (${error})`) : null,
        (surface?.top3 ?? []).length === 0
          ? h('p', { style: styles.note }, t('noMeasured'))
          : h('div', { style: styles.cards }, (surface?.top3 ?? []).map(row => h('div', { key: row.pluginId, style: styles.card },
              h('div', { style: styles.cardTop },
                h('span', { style: styles.rank }, row.rank === null || row.rank === undefined ? '—' : `#${row.rank}`),
                h('span', { style: row.unrated ? styles.chip : styles.chipMeasured }, row.unrated ? t('unrated') : t('measured')),
              ),
              h('div', { style: styles.name, title: row.name }, row.name),
              h('div', { style: styles.author }, row.author),
              h('div', { style: styles.score }, scoreOf(row), h('span', { style: styles.small }, ` ${t('score')}`)),
              h('div', { style: styles.meta }, `GOE ${row.evidenceGrade ?? 'E0'} · ${t('prior')} ${Number(row.prior ?? 0).toFixed(1)} · ${t('bench')} ${row.bench === null || row.bench === undefined ? '—' : Number(row.bench).toFixed(1)}`),
              h('div', { style: styles.meta }, `${t('coverage')} ${formatPct(row.coverage)} · ${t('confidence')} ${formatPct(row.confidence)}`),
              h('a', { style: styles.link, href: row.repo, target: '_blank', rel: 'noreferrer' }, 'repo ↗'),
            ))),
        h('div', null,
          h('div', { style: { ...styles.subtitle, marginBottom: '6px' } }, t('contributors')),
          (data.contributors ?? []).length === 0
            ? h('p', { style: styles.note }, t('noContributors'))
            : h('div', { style: styles.contributors }, data.contributors.slice(0, 5).map(row => h('div', { key: row.contributor, style: styles.contributor },
                h('span', null, row.contributor, ' ', h('span', { style: styles.small }, row.badge)),
                h('span', { style: styles.small }, `${row.credits} credits · ${row.count} contributions`),
              ))),
        ),
        h('div', { style: styles.meta }, `${t('generated')}: ${data.generatedAt ?? '—'} · ${data.schema ?? ''}`),
      )
    }

    function apply(ctx) {
      ctx.effect(() => ctx.locale.register(NS, { en, zh }), 'dsh-community-bench: dictionaries')
      const t = ctx.locale.bind(NS)
      ctx.inject(['slots'], (scope) => {
        scope.effect(() => scope.slots.register({
          name: 'settings.plugins.tab',
          id: 'community-bench',
          order: 40,
          label: () => t('tab'),
          locale: NS,
        }, CommunityBenchTab), 'dsh-community-bench: settings tab')
      })
    }

    return { name: 'dsh-community-bench', inject: ['slots', 'locale'], NS, apply }
  },
})
