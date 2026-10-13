#!/usr/bin/env python3
"""
build_index.py — Pixel-perfect index.html generator for the
"Najwan Amru — Design Porto 1" portfolio website.

Parses the authoritative Photoshop "Save for Web Slices" table
(reference/Design-Porto-1-original.html, canvas 3508 x 27281 px),
verifies every geometric invariant (column widths, row heights,
colspan/rowspan consistency), and emits a responsive index.html that
uses a Proportional Absolute Canvas:

  * one wrapper div with a fixed aspect-ratio (3508 / 27281)
  * every slice absolutely positioned with exact percentage geometry
  * zero sub-pixel seams, zero horizontal scroll at any viewport width

The visual design, section order, images and 15 interactive links are
1:1 with Design Porto 1.pdf / Design Porto 1.psd — nothing is
redesigned.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "reference" / "Design-Porto-1-original.html"
OUT = ROOT / "index.html"
REPORT = ROOT / "tools" / "geometry-report.json"

CANVAS_W = 3508

# ----------------------------------------------------------------------------
# Content metadata: descriptive alt text for content slices.
# Decorative margin/background slices get alt="" (correct accessibility
# practice: they carry no information). Section wording follows the
# wording used inside the design itself.
# ----------------------------------------------------------------------------
ALTS = {
    "Design-Porto-1_01.gif":
        "Sampul portofolio: THE DIRECTOR OF PHOTOGRAPHY — NAJWAN AMRU EST 2026, "
        "beserta bagian Hi / Intro, Contact, Experience, Education, dan Software "
        "(Adobe Photoshop, Illustrator, Lightroom, Premiere Pro, After Effects)",
    "Design-Porto-1_03.gif":
        "Tonton di YouTube: Profil — FPM-ONE Short Film",
    "Design-Porto-1_03-06.gif":
        "Tonton di YouTube: Podcast Video Ruang 49",
    "Design-Porto-1_07.gif":
        "Keterangan proyek FPM-ONE Short Film: peran, peralatan, dan deskripsi produksi",
    "Design-Porto-1_08.gif":
        "Keterangan proyek Podcast Ruang 49: peran, peralatan, dan deskripsi produksi",
    "Design-Porto-1_10.jpg":
        "Tonton di YouTube: Review Content Electronic",
    "Design-Porto-1_12.gif":
        "Keterangan proyek Review Content Electronic dan daftar video di bawahnya",
    "Design-Porto-1_10.gif":
        "Tonton di YouTube: video produksi konten (showcase proyek)",
    "Design-Porto-1_10-17.gif":
        "Tonton di YouTube: video produksi konten (showcase proyek)",
    "Design-Porto-1_18.gif":
        "Judul video showcase proyek (baris teks)",
    "Design-Porto-1_19.gif":
        "Judul video showcase proyek (baris teks)",
    "Design-Porto-1_16.gif":
        "Tonton di YouTube: video showcase proyek",
    "Design-Porto-1_10-23.gif":
        "Tonton di YouTube: video showcase proyek",
    "Design-Porto-1_24.gif":
        "Keterangan video showcase proyek (blok teks)",
    "Design-Porto-1_25.gif":
        "Keterangan video showcase proyek (blok teks)",
    "Design-Porto-1_10-28.gif":
        "Tonton di YouTube: Music Video — The Man Who Can't Be Moved",
    "Design-Porto-1_29.gif":
        "Keterangan proyek Music Video The Man Who Can't Be Moved",
    "trailer.gif":
        "Lihat di Instagram: DKOMPLEKS Reel — Trailer (instagram.com/reel/DU5Rn6UEkne)",
    "Design-Porto-1_11-34.gif":
        "Lihat di Instagram: DKOMPLEKS Reel (instagram.com/reel/DVTQxSWkoF7)",
    "Design-Porto-1_13-36.gif":
        "Lihat di Instagram: DKOMPLEKS Reel (instagram.com/reel/DZPWFVhywD8)",
    "Design-Porto-1_37.gif":
        "Keterangan konten Instagram DKOMPLEKS (blok teks)",
    "Design-Porto-1_39.gif":
        "Keterangan konten Instagram DKOMPLEKS (blok teks)",
    "video-documenter.gif":
        "Tonton di YouTube: Video Documenter Perpisahan SMA Muhammadiyah",
    "KERONCONG-TUGU.gif":
        "Tonton livestream YouTube: Master Cameraman — Malam 24 di Roemah Toegoe (Keroncong Tugu)",
    "Design-Porto-1_46.gif":
        "Galeri Other's Content: karya dan konten pendukung lainnya",
    "Design-Porto-1_47.gif":
        "Bagian footer: identitas kontak",
    "Design-Porto-1_48.gif":
        "Hubungi via WhatsApp +62 878-7787-9389 (wa.link/lrpvds)",
    "Design-Porto-1_50.gif":
        "Informasi kontak footer (blok teks)",
    "Design-Porto-1_51.gif":
        "Kunjungi Instagram @wan_lunari",
    "Design-Porto-1_53.gif":
        "Footer portofolio — penutup desain",
}

SITE_URL = "https://tzoppmc.github.io/portfolio-juan/"
PAGE_TITLE = "Najwan Amru — Director of Photography & Visual Designer Portfolio"
PAGE_DESC = (
    "Portofolio resmi Najwan Amru (Juan) — Director of Photography & Visual Designer. "
    "Showcase film pendek, podcast, music video, konten Instagram DKOMPLEKS, "
    "livestream, dan dokumentasi. Est. 2026."
)

# Section anchors: (id, reference slice whose y is used, label)
SECTIONS = [
    ("showcase", "Design-Porto-1_03.gif", "Video & Film"),
    ("dkompleks", "trailer.gif", "DKOMPLEKS"),
    ("live", "video-documenter.gif", "Live & Other"),
    ("kontak", "Design-Porto-1_48.gif", "Kontak"),
]


def parse(html: str):
    html = html.replace("\r\n", "\n")
    rows_html = re.findall(r"<tr>(.*?)</tr>", html, re.S)
    rows = []
    for row_html in rows_html:
        cells = []
        for attrs, inner in re.findall(r"<td([^>]*)>(.*?)</td>", row_html, re.S):
            cs = int((re.search(r'colspan="(\d+)"', attrs) or [None, "1"])[1])
            rs = int((re.search(r'rowspan="(\d+)"', attrs) or [None, "1"])[1])
            img = re.search(r'<img src="([^"]+)" width="(\d+)" height="(\d+)"', inner)
            href = re.search(r'<a href="([^"]+)"', inner)
            cells.append({
                "colspan": cs,
                "rowspan": rs,
                "src": img.group(1) if img else None,
                "w": int(img.group(2)) if img else None,
                "h": int(img.group(3)) if img else None,
                "href": href.group(1) if href else None,
            })
        rows.append(cells)

    # ---- column widths (last row: one spacer img per column) ----
    col_widths = [c["w"] for c in rows[-1] if c["w"]]
    col_widths.append(1)  # final empty <td> = the 1 px edge column
    total_w = sum(col_widths)
    assert total_w == CANVAS_W, f"column widths sum {total_w} != {CANVAS_W}"

    # ---- row heights (each row's width-1 spacer defines the height) ----
    row_heights = []
    for cells in rows[:-1]:
        spacers = [c["h"] for c in cells if c["src"] and c["src"].endswith("spacer.gif") and c["w"] == 1]
        assert len(spacers) == 1, f"expected exactly 1 row spacer, got {len(spacers)}"
        row_heights.append(spacers[0])
    row_heights.append(1)  # the column-definition row itself
    total_h = sum(row_heights)

    # ---- grid placement ----
    occupied = {}
    slices = []
    n_rows = len(rows)
    for r, cells in enumerate(rows):
        col = 0
        for cell in cells:
            while occupied.get((r, col)):
                col += 1
            cs, rs = cell["colspan"], cell["rowspan"]
            for rr in range(r, r + rs):
                for cc in range(col, col + cs):
                    assert (rr, cc) not in occupied, f"overlap at {rr},{cc}"
                    occupied[(rr, cc)] = True
            cell["col"], cell["row"] = col, r
            cell["x"] = sum(col_widths[:col])
            cell["y"] = sum(row_heights[:r])
            cell["w_grid"] = sum(col_widths[col:col + cs])
            cell["h_grid"] = sum(row_heights[r:r + rs])
            if cell["src"] and not cell["src"].endswith("spacer.gif"):
                slices.append(cell)
            col += cs

    # ---- invariants: pixel-perfect proof ----
    for s in slices:
        assert s["w"] == s["w_grid"], (
            f"{s['src']}: declared width {s['w']} != grid width {s['w_grid']}")
        assert s["h"] == s["h_grid"], (
            f"{s['src']}: declared height {s['h']} != grid height {s['h_grid']}")
        assert s["x"] + s["w"] <= CANVAS_W
        assert s["y"] + s["h"] <= total_h

    return col_widths, row_heights, slices, total_w, total_h


def pct(v, base):
    return f"{v / base * 100:.6f}%"


def build(slices, total_w, total_h):
    y_of = {Path(s["src"]).name: s["y"] for s in slices}
    anchors = [(sid, pct(y_of[ref], total_h), label) for sid, ref, label in SECTIONS]

    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{PAGE_TITLE}</title>
<meta name="description" content="{PAGE_DESC}">
<meta name="author" content="Najwan Amru (Juan)">
<meta name="theme-color" content="#000000">
<link rel="canonical" href="{SITE_URL}">
<!-- OpenGraph -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Najwan Amru — Portfolio">
<meta property="og:title" content="{PAGE_TITLE}">
<meta property="og:description" content="{PAGE_DESC}">
<meta property="og:url" content="{SITE_URL}">
<meta property="og:image" content="{SITE_URL}images/Design-Porto-1_01.gif">
<meta property="og:locale" content="id_ID">
<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{PAGE_TITLE}">
<meta name="twitter:description" content="{PAGE_DESC}">
<meta name="twitter:image" content="{SITE_URL}images/Design-Porto-1_01.gif">
<link rel="preload" as="image" href="images/Design-Porto-1_01.gif">
<link rel="icon" type="image/png" href="assets/png/Artboard 1.png">
<style>
  :root {{ --page-bg: #ffffff; }}
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  html, body {{ margin: 0; padding: 0; background: var(--page-bg); }}
  body {{ -webkit-text-size-adjust: 100%; }}

  .sr-only {{
    position: absolute; width: 1px; height: 1px; margin: -1px;
    padding: 0; border: 0; clip: rect(0 0 0 0); overflow: hidden; white-space: nowrap;
  }}

  /* ===== Proportional Absolute Canvas — geometry 1:1 with the PSD ===== */
  .canvas {{
    position: relative;
    width: 100%;
    max-width: {total_w}px;
    margin: 0 auto;
    aspect-ratio: {total_w} / {total_h};
    background: var(--page-bg);
    overflow: hidden;
  }}
  .canvas a, .canvas img {{ display: block; border: 0; padding: 0; margin: 0; }}
  .slice {{
    position: absolute;
    object-fit: fill;
    width: 100%; height: 100%;
  }}
  a.slice {{ z-index: 2; }}
  a.slice img {{
    width: 100%; height: 100%;
    transition: filter .25s ease, transform .25s ease;
    will-change: filter;
  }}
  a.slice:hover img, a.slice:focus-visible img {{
    filter: brightness(1.12) saturate(1.06);
  }}
  a.slice:focus-visible {{
    outline: 3px solid #4da3ff; outline-offset: -3px; border-radius: 4px;
  }}
  .anchor {{ position: absolute; width: 1px; height: 1px; }}
  @media (prefers-reduced-motion: reduce) {{
    html {{ scroll-behavior: auto; }}
    a.slice img {{ transition: none; }}
  }}

  /* ===== Floating quick-jump navigation (overlay only — never alters design) ===== */
  #quicknav {{
    position: fixed; right: max(14px, env(safe-area-inset-right)); bottom: max(14px, env(safe-area-inset-bottom));
    z-index: 50; display: flex; flex-direction: column; align-items: flex-end; gap: 8px;
    font: 600 13px/1.2 system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  }}
  #qn-items {{
    display: flex; flex-direction: column; gap: 6px;
    background: rgba(16,16,20,.92); color: #fff;
    border: 1px solid rgba(255,255,255,.14); border-radius: 14px;
    padding: 10px; box-shadow: 0 8px 28px rgba(0,0,0,.35);
    backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  }}
  #quicknav.collapsed #qn-items {{ display: none; }}
  #qn-items a {{
    color: #fff; text-decoration: none; padding: 7px 12px; border-radius: 9px;
    white-space: nowrap; transition: background .2s ease;
  }}
  #qn-items a:hover {{ background: rgba(255,255,255,.16); }}
  #qn-items a.pdf {{ color: #9ed0ff; }}
  #qn-toggle {{
    width: 44px; height: 44px; border-radius: 50%;
    border: 1px solid rgba(255,255,255,.2); background: rgba(16,16,20,.92); color: #fff;
    font-size: 19px; cursor: pointer; box-shadow: 0 6px 20px rgba(0,0,0,.35);
  }}
  #qn-toggle:focus-visible, #qn-items a:focus-visible {{ outline: 2px solid #4da3ff; outline-offset: 2px; }}
</style>
</head>
<body>
<h1 class="sr-only">Najwan Amru — Director of Photography &amp; Visual Designer (Est. 2026). Portofolio karya: film pendek, podcast, music video, konten Instagram DKOMPLEKS, livestream, dan dokumentasi.</h1>

<main class="canvas" id="top" aria-label="Portofolio Najwan Amru — desain 1:1 Design Porto 1">
""")

    # anchors
    for sid, y, _label in anchors:
        parts.append(f'  <span class="anchor" id="{sid}" style="top:{y}" aria-hidden="true"></span>\n')

    for s in slices:
        name = Path(s["src"]).name
        # +0.02% right/bottom expansion guarantees no sub-pixel white seams
        left = pct(s["x"], total_w)
        top = pct(s["y"], total_h)
        width = f"calc({pct(s['w'], total_w)} + 0.02%)"
        height = f"calc({pct(s['h'], total_h)} + 0.02%)"
        alt = ALTS.get(name, "")
        alt_attr = f'alt="{alt}"' if alt else 'alt="" aria-hidden="true"'
        lazy = ' loading="lazy" decoding="async"' if s["y"] > 8000 else ' decoding="async"'
        img = (f'<img class="slice" src="{s["src"]}" {alt_attr}{lazy} '
               f'width="{s["w"]}" height="{s["h"]}" '
               f'style="left:{left};top:{top};width:{width};height:{height}">')
        if s["href"]:
            img = (f'<a class="slice" href="{s["href"]}" target="_blank" rel="noopener noreferrer" '
                   f'aria-label="{alt if alt else name}">{img}</a>')
        parts.append(f"  {img}\n")

    parts.append(f"""</main>

<nav id="quicknav" aria-label="Navigasi cepat">
  <div id="qn-items">
    <a href="#top">&#8593; Ke Atas</a>
    <a href="#showcase">Video &amp; Film</a>
    <a href="#dkompleks">DKOMPLEKS</a>
    <a href="#live">Live &amp; Other</a>
    <a href="#kontak">Kontak</a>
    <a class="pdf" href="reference/Design-Porto-1.pdf" download="Design Porto 1.pdf">&#11015; Unduh PDF Desain</a>
  </div>
  <button id="qn-toggle" type="button" aria-expanded="true" aria-controls="qn-items" title="Sembunyikan / tampilkan navigasi">&#9776;</button>
</nav>

<script>
(function () {{
  var nav = document.getElementById('quicknav');
  var btn = document.getElementById('qn-toggle');
  btn.addEventListener('click', function () {{
    var collapsed = nav.classList.toggle('collapsed');
    btn.setAttribute('aria-expanded', String(!collapsed));
  }});
}})();
</script>
</body>
</html>
""")
    return "".join(parts)


def main():
    html = SRC.read_text(encoding="utf-8")
    col_widths, row_heights, slices, total_w, total_h = parse(html)

    links = [s for s in slices if s["href"]]
    print(f"Canvas          : {total_w} x {total_h} px")
    print(f"Columns         : {len(col_widths)} (sum {sum(col_widths)})")
    print(f"Rows            : {len(row_heights)} (sum {sum(row_heights)})")
    print(f"Content slices  : {len(slices)}")
    print(f"Unique images   : {len(set(s['src'] for s in slices))}")
    print(f"Interactive link: {len(links)}")
    for s in links:
        print(f"  - {Path(s['src']).name:<32} -> {s['href']}")

    assert len(links) == 15, f"expected 15 interactive links, found {len(links)}"
    assert len(set(s["src"] for s in slices)) == 53, "expected 53 unique content images (54 files incl. spacer)"

    OUT.write_text(build(slices, total_w, total_h), encoding="utf-8")
    REPORT.write_text(json.dumps({
        "canvas": [total_w, total_h],
        "slices": [
            {"src": s["src"], "x": s["x"], "y": s["y"], "w": s["w"], "h": s["h"],
             "href": s["href"]} for s in slices
        ],
    }, indent=2), encoding="utf-8")
    print(f"\nOK wrote {OUT} ({OUT.stat().st_size} bytes) and {REPORT}")


if __name__ == "__main__":
    sys.exit(main())
