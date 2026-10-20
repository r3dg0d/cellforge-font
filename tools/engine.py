"""PixelForge procedural engine: pixel maps -> weighted, merged pixel outlines.

Construction model (cell = 100 units, one design pixel):
  * every ink pixel becomes a rectangle whose ink width/height depend on weight;
  * orthogonal neighbours are bridged by bars, so strokes read as continuous;
  * diagonal neighbours (no shared orthogonal neighbour) are joined by an
    explicit pixel *step* at light weights, keeping diagonals stair-stepped;
  * at heavy weights a one-pixel gap ("counter") is protected: ink may not grow
    into it beyond a fixed limit, so m, e, B, 8 ... keep open counters;
  * italics shift every pixel row by 16 units (a drawn pixel-step slant, not a
    geometric shear), so rows stay perfectly horizontal.
Every recipe emits the same primitives at every weight, so the masters are
point-compatible and can drive a variable font; static fonts are produced by
boolean union (pathops) of the same primitives.
"""
from __future__ import annotations

import os
import re

from ttcore import (BLOCK_RANGE, BOX_RANGE, COMPOSITES, POWERLINE, Glyph,
                    glyph_name, parse_box_name)

HERE = os.path.dirname(os.path.abspath(__file__))
MAPS = os.path.join(HERE, "..", "sources", "pixelmaps.txt")

CELL = 100
SLOPE = 16  # italic shift per pixel row
# weight -> (ink width of a pixel, ink height of a pixel)
INK = {100: (22, 22), 200: (40, 38), 300: (64, 60), 400: (100, 100), 500: (116, 106),
       600: (132, 112), 700: (148, 118), 800: (162, 124), 900: (176, 130)}
GAP_X, GAP_Y = 18, 15  # max growth into a protected one-pixel counter

FAMILY = {
    "name": "PixelForge", "ps": "PixelForge", "version": (1, 0), "vendor": "R3DG",
    "copyright": "Copyright 2026 Vincent Patrick Chambers (https://github.com/r3dg0d/pixelforge-font), with Reserved Font Name \"PixelForge\".",
    "designer": "Vincent Patrick Chambers", "url": "https://github.com/r3dg0d/pixelforge-font",
    "description": "PixelForge: an original pixel-grid type family for interfaces, games and terminals.",
    "upm": 1000, "italic_angle": 9.09,
    "metrics": {"ascender": 800, "descender": -200, "cap": 800, "x": 600,
                "line_ascent": 1120, "line_descent": 250, "win_ascent": 1150, "win_descent": 300,
                "underline_pos": -150, "underline_thick": 100},
}
BOX_TOP, BOX_BOTTOM = 1120, -250  # terminal cell extent for box drawing
BOX_W = 600

ACCENTS = {  # rows top-first
    "grave": ["#.", ".#"], "acute": [".#", "#."], "circumflex": [".#.", "#.#"],
    "tilde": [".#.#", "#.#."], "dieresis": ["#.#"], "ring": ["###", "#.#", "###"],
    "cedilla": [".#", "##"],
}


# ---------------------------------------------------------------- map parsing
def load_maps():
    entries = {}
    order = []
    with open(MAPS) as fh:
        blocks = re.split(r"\n\s*\n", fh.read())
    for blk in blocks:
        lines = [l for l in blk.strip().splitlines() if l and not l.startswith("# ")]
        if not lines:
            continue
        head = lines[0].split()
        name, cp, top = head[0], head[1], int(head[2])
        cp = None if cp == "-" else int(cp, 16)
        rest = head[3:]
        entries[name] = {"cp": cp, "top": top, "rows": lines[1:], "dir": rest}
        order.append(name)
    for name in order:  # resolve directives
        e = entries[name]
        if e["dir"] and e["dir"][0] == "blank":
            e["rows"] = ["." * int(e["dir"][1])]
            e["blank"] = True
        elif e["dir"]:
            op, src = e["dir"]
            s = entries[src]
            rows = s["rows"]
            if op == "=mirror":
                rows = [r[::-1] for r in rows]
            elif op == "=rot":
                rows = [r[::-1] for r in reversed(rows)]
            elif op == "=vflip":
                rows = list(reversed(rows))
            e["rows"] = list(rows)
            e["blank"] = s.get("blank", False)
    for name in order:
        rows = entries[name]["rows"]
        w = len(rows[0])
        assert all(len(r) == w for r in rows), f"ragged rows in {name}"
    return order, entries


def ink_of(rows, top, dx=0):
    return {(c + dx, top - i) for i, r in enumerate(rows) for c, ch in enumerate(r) if ch == "#"}


# ---------------------------------------------------------------- pixel pen
def draw_pixels(g, ink, weight, italic, origin):
    pw, ph = INK[weight]
    hw, hh = pw / 2, ph / 2
    slope = SLOPE if italic else 0

    def cx(c, h):
        return origin + c * CELL + CELL / 2 + h * slope

    def cy(h):
        return h * CELL + CELL / 2

    def ext(c, h, dc, dh, half, cap):
        n1, n2 = (c + dc, h + dh), (c + 2 * dc, h + 2 * dh)
        if n1 not in ink and n2 in ink:
            return min(half, CELL / 2 + cap)
        return half

    E = {}
    for (c, h) in sorted(ink):
        l, r = ext(c, h, -1, 0, hw, GAP_X), ext(c, h, 1, 0, hw, GAP_X)
        b, t = ext(c, h, 0, -1, hh, GAP_Y), ext(c, h, 0, 1, hh, GAP_Y)
        E[(c, h)] = (l, r, b, t)
        x, y = cx(c, h), cy(h)
        g.rect(x - l, y - b, x + r, y + t)
    for (c, h) in sorted(ink):
        l, r, b, t = E[(c, h)]
        if (c + 1, h) in ink:  # horizontal bridge
            b2, t2 = E[(c + 1, h)][2:]
            g.rect(cx(c, h), cy(h) - min(b, b2), cx(c + 1, h), cy(h) + min(t, t2))
        if (c, h + 1) in ink:  # vertical bridge, split at the row boundary for italics
            yb = (h + 1) * CELL
            l2, r2 = E[(c, h + 1)][:2]
            g.rect(cx(c, h) - min(l, l2), cy(h), cx(c, h) + min(r, r2), yb + 4)
            g.rect(cx(c, h + 1) - min(l, l2), yb - 4, cx(c, h + 1) + min(r, r2), cy(h + 1))
        for dc in (-1, 1):  # diagonal step
            if (c + dc, h + 1) in ink and (c + dc, h) not in ink and (c, h + 1) not in ink:
                f = 1.0 if pw < CELL else 0.0
                yb = (h + 1) * CELL
                xc = origin + (c + (1 if dc > 0 else 0)) * CELL + (h + 0.5) * slope
                x1, x2 = cx(c, h), cx(c + dc, h + 1)
                g.rect(x1, cy(h) - hh * f, xc + dc * hw * f, cy(h) + hh * f)
                g.rect(xc - hw * f, cy(h), xc + hw * f, cy(h + 1))
                g.rect(xc - dc * hw * f, cy(h + 1) - hh * f, x2, cy(h + 1) + hh * f)


def spacing(weight):
    pw, _ = INK[weight]
    return max(0, pw - CELL)


def bitmap_glyph(name, cps, rows, top, weight, italic, extra=None, blank=False):
    cols = len(rows[0])
    e = spacing(weight)
    g = Glyph(name, list(cps), (cols + 1) * CELL + e)
    if not blank:
        ink = ink_of(rows, top)
        if extra:
            ink |= extra
        draw_pixels(g, ink, weight, italic, CELL / 2 + e / 2)
    return g


# ---------------------------------------------------------------- composites
def accent_ink(base_rows, base_top, acc, upper):
    rows = ACCENTS[acc]
    cols = len(base_rows[0])
    a = len(rows[0])
    dx = (cols - a + 1) // 2
    if acc == "cedilla":
        return ink_of(rows, -1, dx)
    if acc == "ring":
        top = 10 if upper else 8
    elif acc == "dieresis":
        top = 9 if upper else 7
    else:
        top = 10 if upper else 8
    return ink_of(rows, top, dx)


# ---------------------------------------------------------------- box drawing
def box_glyph(cp, weight, italic):
    pw, ph = INK[weight]
    lt_v, lt_h = max(pw, 30), max(ph, 30)  # light line thickness
    hv_v, hv_h = min(lt_v * 2, 260), min(lt_h * 2, 260)
    g = Glyph(glyph_name(cp), [cp], BOX_W)
    midx, midy = BOX_W / 2, (BOX_TOP + BOX_BOTTOM) / 2
    spec = parse_box_name(cp)
    name = __import__("unicodedata").name(chr(cp))
    dbl = 120  # double-line spacing

    def arm(direction, w):
        if direction in ("left", "right"):
            x_end = 0 if direction == "left" else BOX_W
            th = lt_h if w == 1 else hv_h
            ext = (lt_v if w != 2 else hv_v) / 2
            if w == 3:
                for off in (-dbl / 2, dbl / 2):
                    g.rect(x_end, midy + off - lt_h / 2, midx + (dbl / 2 + lt_v / 2) * (1 if direction == "left" else -1) * -1 * -1, midy + off + lt_h / 2)
            else:
                g.rect(x_end, midy - th / 2, midx + (ext if direction == "left" else -ext), midy + th / 2)
        else:
            y_end = BOX_TOP if direction == "up" else BOX_BOTTOM
            th = lt_v if w == 1 else hv_v
            ext = (lt_h if w != 2 else hv_h) / 2
            if w == 3:
                for off in (-dbl / 2, dbl / 2):
                    g.rect(midx + off - lt_v / 2, y_end, midx + off + lt_v / 2, midy + (-(dbl / 2 + lt_h / 2) if direction == "up" else (dbl / 2 + lt_h / 2)))
            else:
                g.rect(midx - th / 2, y_end, midx + th / 2, midy + (-ext if direction == "up" else ext))

    if spec:
        for d, w in spec.items():
            arm(d, w)
    elif "DASH" in name:
        n = 2 if "DOUBLE DASH" in name else 3 if "TRIPLE" in name else 4
        heavy = "HEAVY" in name
        if "HORIZONTAL" in name:
            th = hv_h if heavy else lt_h
            seg = BOX_W / n
            for i in range(n):
                g.rect(i * seg + seg * 0.15, midy - th / 2, (i + 1) * seg - seg * 0.15, midy + th / 2)
        else:
            th = hv_v if heavy else lt_v
            seg = (BOX_TOP - BOX_BOTTOM) / n
            for i in range(n):
                g.rect(midx - th / 2, BOX_BOTTOM + i * seg + seg * 0.15, midx + th / 2, BOX_BOTTOM + (i + 1) * seg - seg * 0.15)
    elif "ARC" in name:
        # pixel-stepped rounded corner: arms stop short, a 2-step stair joins them
        dirs = {"DOWN AND RIGHT": ("down", "right"), "DOWN AND LEFT": ("down", "left"),
                "UP AND LEFT": ("up", "left"), "UP AND RIGHT": ("up", "right")}
        for k, (vd, hd) in dirs.items():
            if k in name:
                break
        sx = 1 if hd == "right" else -1
        sy = 1 if vd == "up" else -1
        r = 150
        g.rect(midx - lt_v / 2, BOX_TOP if vd == "up" else BOX_BOTTOM, midx + lt_v / 2, midy + sy * r)
        g.rect(midx + sx * r, midy - lt_h / 2, BOX_W if hd == "right" else 0, midy + lt_h / 2)
        for i in (1, 2):
            px = midx + sx * r * i / 3
            py = midy + sy * r * (3 - i) / 3
            g.rect(px - lt_v / 2 - 30, py - lt_h / 2 - 30, px + lt_v / 2 + 30, py + lt_h / 2 + 30)
    elif "DIAGONAL" in name:
        steps = 9
        hgt = BOX_TOP - BOX_BOTTOM
        diags = []
        if "UPPER RIGHT TO LOWER LEFT" in name or "CROSS" in name:
            diags.append(1)
        if "UPPER LEFT TO LOWER RIGHT" in name or "CROSS" in name:
            diags.append(-1)
        for d in diags:
            for i in range(steps):
                x0 = BOX_W * i / steps
                x1 = BOX_W * (i + 1) / steps
                yy = BOX_BOTTOM + hgt * (i / steps if d == 1 else 1 - (i + 1) / steps)
                g.rect(x0, yy, x1 + 1, yy + hgt / steps + 1)
    else:  # half lines are covered by parse; anything else: light cross fallback
        g.rect(midx - lt_v / 2, midy - lt_h / 2, midx + lt_v / 2, midy + lt_h / 2)
    if italic:
        pass  # box drawing stays upright so terminal grids keep connecting
    return g


def block_glyph(cp, weight, italic):
    g = Glyph(glyph_name(cp), [cp], BOX_W)
    T, B, W = BOX_TOP, BOX_BOTTOM, BOX_W
    H = T - B
    if 0x2581 <= cp <= 0x2588:
        g.rect(0, B, W, B + H * (cp - 0x2580) / 8)
    elif cp == 0x2580:
        g.rect(0, B + H / 2, W, T)
    elif 0x2589 <= cp <= 0x258F:
        g.rect(0, B, W * (8 - (cp - 0x2588)) / 8, T)
    elif cp == 0x2590:
        g.rect(W / 2, B, W, T)
    elif cp in (0x2591, 0x2592, 0x2593):
        # shades as a pixel dither; density from pattern, pixel size from weight
        pw, ph = INK[weight]
        step = 50
        dens = {0x2591: 1, 0x2592: 2, 0x2593: 3}[cp]
        for iy in range(int(H / step)):
            for ix in range(int(W / step)):
                on = {1: (ix % 2 == 0 and iy % 2 == 0),
                      2: (ix + iy) % 2 == 0,
                      3: not (ix % 2 == 1 and iy % 2 == 1)}[dens]
                if on:
                    g.rect(ix * step, B + iy * step, (ix + 1) * step, B + (iy + 1) * step)
    elif cp == 0x2594:
        g.rect(0, T - H / 8, W, T)
    elif cp == 0x2595:
        g.rect(W * 7 / 8, B, W, T)
    else:
        quads = {0x2596: "3", 0x2597: "4", 0x2598: "1", 0x2599: "134", 0x259A: "14",
                 0x259B: "123", 0x259C: "124", 0x259D: "2", 0x259E: "23", 0x259F: "234"}[cp]
        boxes = {"1": (0, B + H / 2, W / 2, T), "2": (W / 2, B + H / 2, W, T),
                 "3": (0, B, W / 2, B + H / 2), "4": (W / 2, B, W, B + H / 2)}
        for q in quads:
            g.rect(*boxes[q])
    return g


PL_MAPS = {
    0xE0A0: ["#...#", "#...#", "#..#.", "#.#..", "##...", "#....", "#....", "#...."],  # branch
    0xE0A1: ["#....", "#....", "#####", ".....", "#...#", "##..#", "#.#.#", "#..##"],  # LN
    0xE0A2: [".###.", "#...#", "#...#", "#####", "##.##", "##.##", "#####", "#####"],  # lock
}


def powerline_glyph(cp, weight, italic):
    if cp in PL_MAPS:
        return bitmap_glyph(glyph_name(cp), [cp], PL_MAPS[cp], 7, weight, False)
    g = Glyph(glyph_name(cp), [cp], BOX_W)
    T, B, W = BOX_TOP, BOX_BOTTOM, BOX_W
    H = T - B
    n = 27  # 50-unit pixel steps
    step = H / n
    pw, ph = INK[weight]
    for i in range(n):
        y0 = B + i * step
        frac = 1 - abs((i + 0.5) - n / 2) / (n / 2)
        x = W * frac
        if cp == 0xE0B0:
            g.rect(0, y0, x, y0 + step + 0.5)
        elif cp == 0xE0B2:
            g.rect(W - x, y0, W, y0 + step + 0.5)
        else:
            th = max(pw, 40)
            if cp == 0xE0B1:
                g.rect(max(0, x - th), y0, x, y0 + step + 0.5)
            else:
                g.rect(W - x, y0, min(W, W - x + th), y0 + step + 0.5)
    return g


# ---------------------------------------------------------------- glyph set
def notdef(weight):
    pw, ph = INK[weight]
    g = Glyph(".notdef", [], 600)
    t = max(pw, 40)
    g.rect(50, 0, 550, t)
    g.rect(50, 800 - t, 550, 800)
    g.rect(50, 0, 50 + t, 800)
    g.rect(550 - t, 0, 550, 800)
    return g


def build(weight, italic):
    order, M = load_maps()
    glyphs = [notdef(weight)]
    for name in order:
        e = M[name]
        cps = [e["cp"]] if e["cp"] is not None else []
        glyphs.append(bitmap_glyph(name, cps, e["rows"], e["top"], weight, italic, blank=e.get("blank", False)))
    by_cp = {e["cp"]: (n, e) for n, e in M.items() if e["cp"] is not None}
    for cp, (bcp, acc) in sorted(COMPOSITES.items()):
        if bcp == 0x69:
            bcp = 0x131  # accented i is built on dotless i
        bname, be = by_cp[bcp]
        upper = be["top"] >= 7 and chr(bcp).isupper()
        extra = accent_ink(be["rows"], be["top"], acc, upper)
        glyphs.append(bitmap_glyph(glyph_name(cp), [cp], be["rows"], be["top"], weight, italic, extra=extra))
    for cp in BOX_RANGE:
        glyphs.append(box_glyph(cp, weight, italic))
    for cp in BLOCK_RANGE:
        glyphs.append(block_glyph(cp, weight, italic))
    for cp in POWERLINE:
        glyphs.append(powerline_glyph(cp, weight, italic))
    return glyphs


def profiles(rows, top):
    prof = {}
    cols = len(rows[0])
    for i, r in enumerate(rows):
        if "#" in r:
            prof[top - i] = (r.index("#"), cols - 1 - r.rindex("#"))
    return prof, cols


def kerning():
    """Pixel kerning: tighten a pair by one pixel when every shared row keeps
    at least two pixels of paper between the glyphs after tightening."""
    order, M = load_maps()
    names = [n for n in order if M[n]["cp"] is not None and (chr(M[n]["cp"]).isalpha() or n in ("period", "comma"))
             and M[n]["cp"] < 0x80]
    P = {n: profiles(M[n]["rows"], M[n]["top"])[0] for n in names}
    kern = {}
    for a in names:
        for b in names:
            shared = set(P[a]) & set(P[b])
            if len(shared) < 1:
                continue
            d = min(P[a][h][1] + P[b][h][0] + 1 for h in shared)
            # rows adjacent vertically also matter for diagonal contact
            if d >= 3:
                kern[(a, b)] = -CELL
    return kern


def features():
    return """languagesystem DFLT dflt;
languagesystem latn dflt;

feature zero {
    sub zero by zero.slash;
} zero;

feature ss01 {
    featureNames { name "Dotted zero"; };
    sub zero by zero.dot;
} ss01;
"""
