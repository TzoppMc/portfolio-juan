# Portfolio Website — Najwan Amru (Juan)

> **THE DIRECTOR OF PHOTOGRAPHY — NAJWAN AMRU, EST. 2026**

A pixel-perfect portfolio website of **Najwan Amru (Juan)** — Director of Photography &
Visual Designer — rebuilt **1:1** from the original Photoshop design
`Design Porto 1.psd` (canvas **3508 × 27281 px**) via its official
*Save for Web Slices* export. No template, no redesign: visitors see exactly the
same composition, typography, colors and interactive hotspots as the PDF/PSD artwork.

---

## 🇬🇧 English

### About the artist

| | |
|---|---|
| **Name** | Najwan Amru (Juan) |
| **Role** | Director of Photography · Visual Designer · Video Editor |
| **Instagram** | [@wan_lunari](https://www.instagram.com/wan_lunari/) |
| **WhatsApp** | [+62 878-7787-9389](https://wa.link/lrpvds) |

### Featured projects (all hotspots are clickable in the site)

| Project | Platform | Link |
|---|---|---|
| Profil — FPM-ONE Short Film | YouTube | https://youtu.be/0FtWLJWL70k |
| Podcast Video Ruang 49 | YouTube | https://youtu.be/Z2BtMB00tzA |
| Review Content Electronic | YouTube | https://youtu.be/C_UndgZ5doM |
| Content production showcase #1 | YouTube | https://youtu.be/Bk_ZNLWwW70 |
| Content production showcase #2 | YouTube | https://youtu.be/LeB83VM98c4 |
| Content production showcase #3 | YouTube | https://youtu.be/21cwigQwoyw |
| Content production showcase #4 | YouTube | https://youtu.be/ToG9C8tKM30 |
| MV — The Man Who Can't Be Moved | YouTube | https://youtu.be/76OfLG3hh64 |
| DKOMPLEKS Reel — Trailer | Instagram | https://www.instagram.com/reel/DU5Rn6UEkne/ |
| DKOMPLEKS Reel 2 | Instagram | https://www.instagram.com/reel/DVTQxSWkoF7/ |
| DKOMPLEKS Reel 3 | Instagram | https://www.instagram.com/reel/DZPWFVhywD8/ |
| Video Documenter Perpisahan SMA Muhammadiyah | YouTube | https://youtu.be/M56OCl1zBw0 |
| Master Cameraman — Malam 24 @ Roemah Toegoe (Live) | YouTube Live | https://www.youtube.com/live/lGFp0znl-MM |
| WhatsApp contact | WhatsApp | https://wa.link/lrpvds |
| Instagram profile | Instagram | https://www.instagram.com/wan_lunari/ |

### How the pixel-perfect fidelity works

* `reference/Design-Porto-1-original.html` — the authoritative Photoshop
  *Save for Web Slices* table (28 columns × 24 rows).
* `tools/build_index.py` — parses that table, **asserts every geometric
  invariant** (column widths sum to 3508, row heights sum to 27281, every
  colspan/rowspan matches its slice size) and generates `index.html` using a
  **Proportional Absolute Canvas**: one wrapper with `aspect-ratio: 3508/27281`
  and every slice absolutely positioned in exact percentages.
  Result: **zero sub-pixel seams**, **zero horizontal scroll**, identical look
  on desktop, tablet and smartphone — the page is simply a proportional
  shrink/scale of the 3508-px artwork.
* A floating, hideable quick-jump navigation (Video & Film · DKOMPLEKS ·
  Live & Other · Kontak · Download PDF) overlays the design without altering it.
* SEO: semantic `<title>`, meta description, OpenGraph & Twitter cards,
  descriptive `alt` texts; decorative slices are correctly `alt=""`.

### Project structure

```
.
├── index.html                     # the website (generated, 1:1 design)
├── images/                        # 54 original PSD slices (Design-Porto-1_01…53 + trailer, etc.)
├── logo/                          # Adobe software icons (Photoshop, Illustrator, Lightroom…)
├── assets/
│   ├── png/                       # Artboard PNG exports
│   └── profile/                   # profile / support images from the Drive root
├── reference/
│   ├── Design-Porto-1-original.html   # original slice map (authoritative)
│   ├── Design-Porto-1.pdf            # official compressed design PDF (817 KB)
│   └── Design-Porto-1-FINAL.pdf      # final submission PDF (930 KB)
├── tools/
│   ├── build_index.py             # geometry-verified generator of index.html
│   ├── geometry-report.json       # computed x/y/w/h of all 53 slices
│   ├── manifest.txt               # Google Drive file IDs → repo paths
│   └── fetch_assets_locally.sh    # 1-command asset downloader (gdown)
└── .github/workflows/fetch-assets.yml  # CI that imports the Drive assets
```

### Run locally

```bash
cd portfolio-juan
python3 -m http.server 8080 --bind 0.0.0.0
# open http://localhost:8080
```

### Deploy

**GitHub Pages** — Settings → Pages → Source: *Deploy from a branch* →
select `main` / root. The site is fully static (no build step).
**Vercel / Netlify** — import the repository; framework preset *Other*;
output directory `/`.

---

## 🇮🇩 Bahasa Indonesia

Website portofolio **Najwan Amru (Juan)** — Director of Photography & Visual
Designer — dibangun **100% identik** dengan desain Photoshop asli
`Design Porto 1.psd` (kanvas **3508 × 27281 px**) menggunakan potongan resmi
(*Save for Web Slices*) hasil ekspor Photoshop. Tidak ada template atau desain
baru: tampilan, tata letak, warna, tipografi, dan seluruh 15 area klik sama
persis dengan PDF/PSD aslinya.

### Cara kerja kesetiaan visual 1:1

* Seluruh geometri (posisi & ukuran 53 potongan desain) dihitung dari tabel
  slice asli Photoshop dan **diverifikasi otomatis** oleh
  `tools/build_index.py` — setiap selisih 1 piksel pun akan menggagalkan build.
* Kanvas responsif proporsional: website adalah skala proporsional dari
  artwork 3508 px, sehingga **tanpa garis retak antar-slice**, **tanpa scroll
  horizontal**, dan tampilan Desktop/Tablet/Smartphone tetap identik dengan PDF.
* Navigasi melayang (bisa disembunyikan) untuk lompat cepat antar-bagian dan
  mengunduh PDF desain resmi.

### Menjalankan di lokal

```bash
python3 -m http.server 8080 --bind 0.0.0.0
# buka http://localhost:8080
```

### Mengunduh ulang aset dari Google Drive

Semua aset publik (*anyone with the link*) dan tercantum di
`tools/manifest.txt`:

```bash
pip install gdown
bash tools/fetch_assets_locally.sh
```

atau jalankan workflow GitHub Actions `fetch-assets.yml` (tab **Actions →
Fetch Drive assets → Run workflow**).

---

## License & credits

Design artwork © **Najwan Amru (Juan)**. Website code generated with care to
preserve the original composition 1:1.
