#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the dedicated README figure set for dsh-community-bench.

Outputs (docs/assets/, overwritten in place):

  dsh-community-bench-hero-{zh,en}-{light,dark}.webp   1440x576 hero banner
  dsh-community-bench-flow-v5-{light,dark}.svg         1100x660 structure figure

The two pictures are derived from the shipped package, not from a template.

  hero   The tab is a read-only window onto one public registry. The right
         panel draws that registry literally: 42 plugin rows in the bundled
         snapshot, one per cell. 41 cells are E0 / unrated, exactly one is the
         E2 provisional pilot (dsh-memento on the memory surface), and none is
         a positive measured row. The legend repeats the counts the tab's stat
         strip prints (42 / 1 / 0 / 41).

  flow   Two interchangeable lanes -> one normalization gate -> three evidence
         blocks, plus the failover edge and the upstream-authority boundary:
           - the bundled snapshot is injected at build by scripts/build.mjs;
           - the live lane is fetch(REGISTRY_URL, {cache:'no-store'});
           - a failed fetch keeps status = snapshot and shows an error string;
           - normalizeRegistry() rejects an empty surfaces[] and keeps top3
             only for goe.positive && E3-E5;
           - the render path splits into measured (E3-E5 positive, top3),
             provisional (E2 / positive=false) and candidates (unrated E0),
             each capped at 3 cards, and only measured may print a #rank;
           - the bottom band separates what this plugin never does from the
             upstream weights it only displays.

The hero is localized (en for README.md, zh for the frozen Chinese README) and
the structure figure is English with code tokens, so one light/dark pair works
for both files.

Run:  python scripts/gen-readme-assets.py
Needs: Pillow and the Windows fonts msyh.ttc / msyhbd.ttc / consola.ttf.
"""

from __future__ import annotations

import math
import os
import sys
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "assets")
NAME = "dsh-community-bench"

FONT_DIR = r"C:\Windows\Fonts"
F_REG = os.path.join(FONT_DIR, "msyh.ttc")
F_BOLD = os.path.join(FONT_DIR, "msyhbd.ttc")
F_MONO = os.path.join(FONT_DIR, "consola.ttf")
F_MONO_BOLD = os.path.join(FONT_DIR, "consolab.ttf")

for _path in (F_REG, F_BOLD, F_MONO, F_MONO_BOLD):
    if not os.path.exists(_path):
        sys.exit(f"FATAL: missing font {_path}")

_FONTS: dict[tuple[str, int], ImageFont.FreeTypeFont] = {}

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def F(path: str, size: float) -> ImageFont.FreeTypeFont:
    """Cached FreeType face."""
    key = (path, round(float(size), 2))  # type: ignore[assignment]
    if key not in _FONTS:
        _FONTS[key] = ImageFont.truetype(path, float(size))
    return _FONTS[key]


def rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def rgba(value: str, alpha: int = 255) -> tuple[int, int, int, int]:
    return rgb(value) + (alpha,)


# ---------------------------------------------------------------------------
# shared family skin
# ---------------------------------------------------------------------------
HERO_SKIN = {
    "light": dict(
        bg=("#f9f6fd", "#e4eaf8"), glow=("#4B67B4", 24),
        card="#ffffff", stroke="#d9e0ef", text="#1b2233", body="#2b3347",
        sub="#5a6275", faint="#8a93a8", accent="#4B67B4",
        accent_soft="#eef1fa", green="#15803d", amber="#b45309",
        amber_soft="#fdf3d7", cell="#f1f4fb", cell_edge="#e2e8f4",
        cell_text="#9aa3b6", shadow=(40, 60, 120, 26),
    ),
    "dark": dict(
        bg=("#131a2a", "#0c1016"), glow=("#4B67B4", 52),
        card="#1b2438", stroke="#2b3550", text="#eef2fb", body="#d7def0",
        sub="#9aa7c2", faint="#6f7c96", accent="#8496f5",
        accent_soft="#202b45", green="#4ade80", amber="#fbbf24",
        amber_soft="#3a2f12", cell="#1f2940", cell_edge="#2c3752",
        cell_text="#67748f", shadow=(0, 0, 0, 120),
    ),
}

FLOW_SKIN = {
    "light": dict(
        bg=("#f9f6fd", "#e4eaf8"), card="#ffffff", stroke="#d9e0ef",
        rowbg="#f4f7fd", text="#1b2233", body="#2b3347", sub="#5a6275",
        faint="#8a93a8", accent="#4B67B4", accent_soft="#eef1fa",
        green="#15803d", amber="#b45309", shadow="#2a3a6a", shadow_op="0.14",
    ),
    "dark": dict(
        bg=("#131a2a", "#0c1016"), card="#1b2438", stroke="#2b3550",
        rowbg="#202a41", text="#eef2fb", body="#d7def0", sub="#9aa7c2",
        faint="#6f7c96", accent="#8496f5", accent_soft="#202b45",
        green="#4ade80", amber="#fbbf24", shadow="#000000", shadow_op="0.55",
    ),
}

# ---------------------------------------------------------------------------
# hero copy
# ---------------------------------------------------------------------------
HERO = {
    "zh": dict(
        kicker="DSH 插件 · 公共证据层",
        title=[[("社区基准", "text")], [("只读消费端", "accent")]],
        value=["同一份公共 registry，所有人看同一屏。",
               "先验行只是候选，永远不挂 #1。"],
        subtitle="设置 → 插件 → 社区基准",
        meta="42 个插件 · 15 个能力面 · E0 ×41 · E2 ×1 · v0.2.6",
        footer1="github.com/PerryLink/dsh-community-bench",
        footer2="社区插件 · Apache-2.0 · 与 DeepSeek 官方无关",
        panel_title="公共 registry · 42 个插件",
        panel_sub="快照 2026-10-18 · dsh-attention/registry/v1",
        panel_chip="所有人看同一份",
        legend=[("unrated", "41 未评级"), ("provisional", "1 暂定"),
                ("zero", "0 positive measured")],
        cell_note="一个格子 = 一行插件 · 等级直接读自 registry",
        below_note="不在本地算分 · 不上报 telemetry · 不写文件 · 不注册工具",
    ),
    "en": dict(
        kicker="DSH PLUGIN · PUBLIC EVIDENCE",
        title=[[("Community", "text")], [("bench", "accent")]],
        value=["Everyone sees the same public rows.",
               "Prior-only rows stay candidates — never #1."],
        subtitle="Settings → Plugins → Community Bench",
        meta="42 plugins · 15 surfaces · E0 ×41 · E2 ×1 · v0.2.6",
        footer1="github.com/PerryLink/dsh-community-bench",
        footer2="Community plugin · Apache-2.0 · not affiliated with DeepSeek",
        panel_title="PUBLIC REGISTRY · 42 PLUGINS",
        panel_sub="snapshot 2026-10-18 · dsh-attention/registry/v1",
        panel_chip="same rows for everyone",
        legend=[("unrated", "41 unrated"), ("provisional", "1 provisional"),
                ("zero", "0 positive measured")],
        cell_note="one cell = one plugin row · grade read from the registry",
        below_note="no local score · no telemetry · no writes · no tools",
    ),
}


# ---------------------------------------------------------------------------
# Pillow helpers
# ---------------------------------------------------------------------------
def gradient(w: int, h: int, top: str, bottom: str) -> Image.Image:
    img = Image.new("RGBA", (w, h))
    draw = ImageDraw.Draw(img)
    c0, c1 = rgb(top), rgb(bottom)
    for y in range(h):
        t = y / (h - 1)
        draw.line([(0, y), (w, y)],
                  fill=tuple(int(c0[i] + (c1[i] - c0[i]) * t) for i in range(3)) + (255,))
    return img


def glow(img: Image.Image, cx: int, cy: int, rx: int, ry: int,
         color: str, alpha: int, blur: int) -> Image.Image:
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse((cx - rx, cy - ry, cx + rx, cy + ry),
                                  fill=rgba(color, alpha))
    return Image.alpha_composite(img, layer.filter(ImageFilter.GaussianBlur(blur)))


def paint_shadows(img: Image.Image, specs, color, blur: int = 18,
                  dy: int = 10) -> Image.Image:
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for box, radius in specs:
        draw.rounded_rectangle((box[0], box[1] + dy, box[2], box[3] + dy),
                               radius=radius, fill=color)
    return Image.alpha_composite(img, layer.filter(ImageFilter.GaussianBlur(blur)))


def fit(path: str, text: str, size: float, maxw: float, minsize: float,
        label: str = "") -> ImageFont.FreeTypeFont:
    """Largest face <= size that keeps `text` inside maxw."""
    while size > minsize and F(path, size).getlength(text) > maxw:
        size -= 0.5
    face = F(path, size)
    if face.getlength(text) > maxw:
        raise SystemExit(f"FATAL: {label or text[:24]!r} is "
                         f"{face.getlength(text):.0f}px wide, limit {maxw:.0f}px")
    return face


def put_runs(draw: ImageDraw.ImageDraw, x: float, baseline: float, runs,
             face, palette: dict) -> float:
    cursor = x
    for text, key in runs:
        draw.text((cursor, baseline), text, font=face, fill=palette[key],
                  anchor="ls")
        cursor += face.getlength(text)
    return cursor


def auto_face(text: str, size: float, *, mono: bool = False,
              bold: bool = False) -> ImageFont.FreeTypeFont:
    """Consolas has no CJK: drop to YaHei as soon as the string is mixed."""
    ascii_only = all(ord(ch) < 128 for ch in text)
    if mono and ascii_only:
        return F(F_MONO_BOLD if bold else F_MONO, size)
    return F(F_BOLD if bold else F_REG, size)


# ---------------------------------------------------------------------------
# hero 1440x576
# ---------------------------------------------------------------------------
def hero(lang: str, theme: str) -> Image.Image:
    L, c = HERO[lang], HERO_SKIN[theme]
    w, h = 1440, 576
    left_x, left_w = 72, 568
    card_box = (700, 56, 1372, 520)

    img = gradient(w, h, c["bg"][0], c["bg"][1])
    img = glow(img, 1140, 250, 420, 300, c["glow"][0], c["glow"][1], 170)
    img = glow(img, 150, 520, 380, 220, c["glow"][0],
               max(6, c["glow"][1] // 2), 170)
    img = paint_shadows(img, [(card_box, 22)], c["shadow"], blur=20, dy=10)
    d = ImageDraw.Draw(img)

    # left column ----------------------------------------------------------
    kicker_face = F(F_BOLD, 17)
    kicker_top = 52
    kw = int(kicker_face.getlength(L["kicker"])) + 48
    d.rounded_rectangle((left_x, kicker_top, left_x + kw, kicker_top + 44),
                        radius=22, fill=rgba(c["accent_soft"], 238),
                        outline=c["stroke"], width=1)
    d.ellipse((left_x + 18, kicker_top + 17, left_x + 30, kicker_top + 29),
              fill=c["accent"])
    d.text((left_x + 38, kicker_top + 30), L["kicker"], font=kicker_face,
           fill=c["body"], anchor="ls")

    title_face = F(F_BOLD, 80)
    title_bases = (174, 258)
    for runs, base in zip(L["title"], title_bases):
        line_w = sum(title_face.getlength(t) for t, _ in runs)
        if line_w > left_w:
            raise SystemExit(f"FATAL: {lang} title line is {line_w:.0f}px > {left_w}px")
        put_runs(d, left_x, base, runs, title_face, c)

    value_size = 30.0
    while value_size > 26 and any(
            F(F_REG, value_size).getlength(line) > left_w for line in L["value"]):
        value_size -= 0.5
    value_face = F(F_REG, value_size)
    for line, base in zip(L["value"], (322, 364)):
        if value_face.getlength(line) > left_w:
            raise SystemExit(f"FATAL: {lang} value {line[:16]!r} too wide")
        d.text((left_x, base), line, font=value_face, fill=c["body"], anchor="ls")

    sub_face = fit(F_REG, L["subtitle"], 26, left_w, 24, f"{lang} subtitle")
    d.text((left_x, 414), L["subtitle"], font=sub_face, fill=c["sub"], anchor="ls")

    meta_face = fit(F_REG, L["meta"], 20, left_w, 18, f"{lang} meta")
    d.text((left_x, 452), L["meta"], font=meta_face, fill=c["sub"], anchor="ls")

    d.line((left_x, 478, left_x + left_w, 478), fill=c["stroke"], width=1)

    foot1 = fit(F_MONO, L["footer1"], 17, left_w, 15, f"{lang} footer link")
    d.text((left_x, 502), L["footer1"], font=foot1, fill=c["sub"], anchor="ls")
    foot2 = fit(F_REG, L["footer2"], 15, left_w, 13, f"{lang} footer note")
    d.text((left_x, 526), L["footer2"], font=foot2, fill=c["faint"], anchor="ls")

    # right: the registry itself, one cell per plugin row -------------------
    cx0, cy0 = 724, 148
    cw, ch, gx, gy = 78, 40, 12, 10
    d.rounded_rectangle(card_box, radius=22, fill=c["card"],
                        outline=c["stroke"], width=1)

    panel_title = auto_face(L["panel_title"], 15, mono=True, bold=True)
    d.text((cx0, 94), L["panel_title"], font=panel_title, fill=c["accent"],
           anchor="ls")

    chip_face = auto_face(L["panel_chip"], 13)
    chip_w = int(chip_face.getlength(L["panel_chip"])) + 30
    d.rounded_rectangle((1348 - chip_w, 74, 1348, 104), radius=15,
                        fill=rgba(c["accent_soft"], 235), outline=c["stroke"],
                        width=1)
    d.text((1348 - chip_w / 2, 89), L["panel_chip"], font=chip_face,
           fill=c["sub"], anchor="mm")

    sub_face2 = auto_face(L["panel_sub"], 13, mono=True)
    d.text((cx0, 120), L["panel_sub"], font=sub_face2, fill=c["faint"],
           anchor="ls")
    d.line((cx0, 134, 1348, 134), fill=c["stroke"], width=1)

    cell_face = auto_face("E0", 12, mono=True)
    cell_face_e2 = auto_face("E2", 14, mono=True, bold=True)
    for i in range(42):
        row, col = divmod(i, 7)
        x = cx0 + col * (cw + gx)
        y = cy0 + row * (ch + gy)
        if i == 41:  # dsh-memento, the single E2 pilot
            d.rounded_rectangle((x, y, x + cw, y + ch), radius=10,
                                fill=c["amber_soft"], outline=c["amber"], width=1)
            d.rounded_rectangle((x - 3, y - 3, x + cw + 3, y + ch + 3),
                                radius=13, outline=rgba(c["amber"], 90), width=2)
            d.text((x + cw / 2, y + ch / 2), "E2", font=cell_face_e2,
                   fill=c["amber"], anchor="mm")
        else:
            d.rounded_rectangle((x, y, x + cw, y + ch), radius=10,
                                fill=c["cell"], outline=c["cell_edge"], width=1)
            d.text((x + cw / 2, y + ch / 2), "E0", font=cell_face,
                   fill=c["cell_text"], anchor="mm")

    # legend ---------------------------------------------------------------
    legend_face = auto_face("41 unrated", 14)
    lx = float(cx0)
    for kind, label in L["legend"]:
        color = {"unrated": c["cell_text"], "provisional": c["amber"],
                 "zero": c["green"]}[kind]
        box = (int(round(lx)), 456, int(round(lx)) + 11, 467)
        if kind == "zero":
            d.rounded_rectangle(box, radius=3, outline=color, width=2)
        else:
            d.rounded_rectangle(box, radius=3, fill=color)
        d.text((lx + 18, 466), label, font=legend_face, fill=c["body"],
               anchor="ls")
        lx += 18 + legend_face.getlength(label) + 32

    note_face = auto_face(L["cell_note"], 13)
    d.text((cx0, 494), L["cell_note"], font=note_face, fill=c["faint"],
           anchor="ls")

    below_face = auto_face(L["below_note"], 12.5, mono=True)
    d.text((700, 548), L["below_note"], font=below_face, fill=c["faint"],
           anchor="ls")

    return img


# ---------------------------------------------------------------------------
# structure figure 1100x660 (hand-written SVG)
# ---------------------------------------------------------------------------
def flow_svg(theme: str) -> str:
    c = FLOW_SKIN[theme]
    p: list[str] = []
    add = p.append

    def tw(text: str, size: float, mono: bool = False, bold: bool = False) -> float:
        return auto_face(text, size, mono=mono, bold=bold).getlength(text)

    def t(x, y, s, size, fill, weight=400, anchor="start", mono=False,
          spacing=None) -> str:
        family = ("'Consolas','Cascadia Mono',monospace" if mono
                  else "'Microsoft YaHei','Segoe UI',sans-serif")
        attrs = [f'x="{x}"', f'y="{y}"', f'font-size="{size}"',
                 f'fill="{fill}"', f'font-family="{family}"']
        if weight != 400:
            attrs.append(f'font-weight="{weight}"')
        if anchor != "start":
            attrs.append(f'text-anchor="{anchor}"')
        if spacing is not None:
            attrs.append(f'letter-spacing="{spacing}"')
        return f'<text {" ".join(attrs)}>{escape(s)}</text>'

    def rect(x, y, wd, ht, r, fill, stroke=None, sw=1, dashed=False,
             shadow=False) -> str:
        attrs = [f'x="{x}"', f'y="{y}"', f'width="{wd}"', f'height="{ht}"',
                 f'rx="{r}"', f'fill="{fill}"']
        if stroke:
            attrs += [f'stroke="{stroke}"', f'stroke-width="{sw}"']
        if dashed:
            attrs.append('stroke-dasharray="7 6"')
        if shadow:
            attrs.append('filter="url(#soft)"')
        return f'<rect {" ".join(attrs)}/>'

    def chip(x, y, label, size=12.5, mono=True, accent=False, h=30,
             pad=22) -> tuple[str, float]:
        wd = tw(label, size, mono=mono) + pad
        out = [rect(x, y, wd, h, 10,
                    c["accent_soft"] if accent else c["rowbg"],
                    c["stroke"], 1)]
        out.append(t(x + wd / 2, y + h / 2 + size * 0.36, label, size,
                     c["accent"] if accent else c["body"], anchor="middle",
                     mono=mono))
        return "".join(out), wd

    # shell -----------------------------------------------------------------
    add('<?xml version="1.0" encoding="UTF-8"?>')
    add('<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="660" '
        'viewBox="0 0 1100 660" role="img" aria-labelledby="fig-title">')
    add('<title id="fig-title">dsh-community-bench — two sources, one gate, '
        'three evidence tiers</title>')
    add('<defs>')
    add(f'<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{c["bg"][0]}"/>'
        f'<stop offset="1" stop-color="{c["bg"][1]}"/></linearGradient>')
    add(f'<filter id="soft" x="-25%" y="-25%" width="150%" height="150%">'
        f'<feDropShadow dx="0" dy="6" stdDeviation="10" '
        f'flood-color="{c["shadow"]}" flood-opacity="{c["shadow_op"]}"/></filter>')
    for key, color in (("acc", c["accent"]), ("amb", c["amber"]),
                       ("fnt", c["faint"])):
        add(f'<marker id="arr-{key}" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10Z" fill="{color}"/></marker>')
    add('</defs>')

    add(f'<rect width="1100" height="660" fill="url(#bg)"/>')

    # header ----------------------------------------------------------------
    add(t(48, 52, "Two sources → one gate → three evidence tiers", 22,
          c["text"], weight=700))
    add(t(1052, 52, "dsh-community-bench · v0.2.6", 13, c["faint"],
          anchor="end", mono=True))
    add(t(48, 80, "The tab renders the public registry and never scores. "
                  "Only a positive E3–E5 row may hold a quality slot.",
          13, c["sub"]))

    # sources ---------------------------------------------------------------
    add(t(48, 112, "SOURCES · 2 LANES", 12, c["faint"], weight=700,
          mono=True, spacing=1))

    add(rect(48, 122, 292, 168, 18, c["card"], c["stroke"], 1, shadow=True))
    add(t(68, 150, "BUNDLED SNAPSHOT", 14, c["accent"], weight=700, mono=True))
    add(t(68, 172, "snapshot.json", 13, c["body"], mono=True))
    add(t(68, 193, "injected at build:", 12, c["sub"]))
    add(t(68, 210, "scripts/build.mjs", 12, c["sub"], mono=True))
    add(t(68, 234, "42 plugins · 15 surfaces", 13, c["body"]))
    add(t(68, 253, "E0 41 · E2 1 · 0 positive", 13, c["body"]))
    add(f'<circle cx="72" cy="270" r="4" fill="{c["green"]}"/>')
    add(t(84, 274, "always available", 12, c["green"]))

    add(rect(48, 332, 292, 104, 18, c["card"], c["stroke"], 1, shadow=True))
    add(t(68, 358, "LIVE REGISTRY", 14, c["accent"], weight=700, mono=True))
    add(t(68, 380, "BENCH_REGISTRY_URL", 13, c["body"], mono=True))
    add(t(68, 400, "fetch(url, { cache: 'no-store' })", 13, c["sub"],
          mono=True))
    add(f'<circle cx="72" cy="416" r="4" fill="{c["amber"]}"/>')
    add(t(84, 420, "outbound HTTPS · may fail", 12, c["amber"]))

    # failover edge ----------------------------------------------------------
    add(f'<path d="M62 326V296" stroke="{c["amber"]}" stroke-width="2" '
        f'stroke-dasharray="6 5" marker-end="url(#arr-amb)"/>')
    add(t(78, 318, "fetch fails → keep snapshot", 12, c["amber"]))
    add(t(48, 458, "mount → refresh(); first paint = snapshot", 11.5,
          c["faint"], mono=True))

    # source -> gate ---------------------------------------------------------
    add(f'<path d="M340 200H380" stroke="{c["accent"]}" stroke-width="2" '
        f'marker-end="url(#arr-acc)"/>')
    add(f'<path d="M340 384C362 384 366 278 380 278" stroke="{c["accent"]}" '
        f'stroke-width="2" fill="none" marker-end="url(#arr-acc)"/>')

    # normalization gate -----------------------------------------------------
    add(rect(384, 122, 304, 178, 18, c["card"], c["stroke"], 1, shadow=True))
    add(t(404, 150, "normalizeRegistry()", 16, c["accent"], weight=700,
          mono=True))
    add(t(404, 176, "surfaces[] non-empty or throw", 13, c["body"], mono=True))
    add(t(404, 198, "leaderboard → [] if absent", 13, c["body"], mono=True))
    add(t(404, 220, "top3 = positive && E3–E5", 13, c["body"], mono=True))
    add(f'<path d="M404 238H668" stroke="{c["stroke"]}" stroke-width="1" '
        f'stroke-dasharray="4 5"/>')
    add(t(404, 258, "same gate for both lanes", 12, c["sub"]))
    add(t(404, 282, "→ normalized registry", 12, c["accent"], mono=True))

    # state label ------------------------------------------------------------
    add(rect(384, 318, 304, 118, 18, c["card"], c["stroke"], 1, shadow=True))
    add(t(404, 344, "STATE · SOURCE LABEL", 14, c["accent"], weight=700,
          mono=True))
    add(t(404, 368, "status = 'snapshot' | 'live'", 13, c["body"], mono=True))
    add(t(404, 390, "refresh() ok → live · fail → snapshot", 13, c["body"],
          mono=True))
    add(t(404, 412, "busy · error string · toolbar chip", 12, c["sub"]))

    # gate -> three evidence tiers ------------------------------------------
    add(t(728, 112, "RENDER · THREE EVIDENCE BLOCKS", 12, c["faint"],
          weight=700, mono=True, spacing=0.8))
    add(f'<path d="M688 211H708M708 172V392" stroke="{c["accent"]}" '
        f'stroke-width="2" fill="none"/>')
    for y in (172, 282, 392):
        add(f'<path d="M708 {y}H724" stroke="{c["accent"]}" stroke-width="2" '
            f'marker-end="url(#arr-acc)"/>')

    tiers = [
        (122, "MEASURED · E3–E5", c["accent"], "0",
         "goe.positive = true (top3 gate)",
         "the only block where #rank appears",
         "0 rows in this snapshot"),
        (232, "PROVISIONAL · E2", c["amber"], "1",
         "E2 or goe.positive = false",
         "no quality rank · task unreviewed",
         "max 3 cards · never #1"),
        (342, "CANDIDATES · E0", c["sub"], "41",
         "unrated = true",
         "no outcome evidence · unnumbered",
         "max 3 cards · prior-only"),
    ]
    for top, title, color, count, l1, l2, foot in tiers:
        add(rect(728, top, 324, 100, 18, c["card"], c["stroke"], 1, shadow=True))
        add(f'<circle cx="750" cy="{top + 20}" r="4" fill="{color}"/>')
        add(t(762, top + 25, title, 13.5, color, weight=700, mono=True))
        add(t(1032, top + 31, count, 24, color, weight=700, anchor="end",
              mono=True))
        add(t(748, top + 52, l1, 13, c["body"], mono=True))
        add(t(748, top + 74, l2, 13, c["body"]))
        add(t(748, top + 92, foot, 11.5, c["faint"]))

    # boundary band ----------------------------------------------------------
    add(f'<path d="M48 470H1052" stroke="{c["stroke"]}" stroke-width="1.2" '
        f'stroke-dasharray="7 6"/>')
    add(t(48, 494, "THIS PLUGIN · READ-ONLY CONSUMER", 12, c["faint"],
          weight=700, mono=True, spacing=0.8))
    add(t(568, 494, "UPSTREAM · SCORING AUTHORITY", 12, c["faint"],
          weight=700, mono=True, spacing=0.8))

    x = 48
    for label in ("no local score", "no telemetry", "no writes", "no tools"):
        svg, wd = chip(x, 504, label, 13, mono=True, h=30)
        add(svg)
        x += wd + 8
    if x - 8 > 524:
        raise SystemExit(f"FATAL: plugin chips overflow the left band ({x:.0f}px)")
    add(t(48, 558, "registers settings.plugins.tab · id community-bench", 11.5,
          c["faint"], mono=True))

    add(t(568, 520, "0.55 bench · 0.30 prior · 0.10 coverage · 0.05 community",
          13, c["body"], mono=True))
    add(t(568, 541, "prior-only cap 60 · minSamples 3 · grades E0–E5", 12,
          c["sub"]))
    add(t(568, 562, "snapshot = cache, not a second scoring path", 12,
          c["sub"]))
    add(f'<path d="M540 484V568" stroke="{c["stroke"]}" stroke-width="1.2" '
        f'stroke-dasharray="6 6"/>')

    # footer ---------------------------------------------------------------
    add(t(48, 620, "one client module · host apply() registers nothing", 11.5,
          c["faint"], mono=True))
    add(t(1052, 620, "snapshot 2026-10-18 · dsh-attention/registry/v1", 11.5,
          c["faint"], anchor="end", mono=True))

    add('</svg>')
    return "\n".join(p) + "\n"


# ---------------------------------------------------------------------------
# entry point
# ---------------------------------------------------------------------------
def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    written: list[str] = []

    for lang in ("zh", "en"):
        for theme in ("light", "dark"):
            img = hero(lang, theme)
            path = os.path.join(OUT, f"{NAME}-hero-{lang}-{theme}.webp")
            img.convert("RGB").save(path, "WEBP", quality=92, method=6)
            written.append(path)

    for theme in ("light", "dark"):
        path = os.path.join(OUT, f"{NAME}-flow-v5-{theme}.svg")
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(flow_svg(theme))
        written.append(path)

    for path in written:
        print(f"wrote {os.path.relpath(path, ROOT)} "
              f"({os.path.getsize(path) // 1024} KB)")


if __name__ == "__main__":
    main()
