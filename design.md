# design.md — Portfolio Fiqhi Dewa Prayastama (Single Page)

## 0. Aturan utama (WAJIB dibaca dulu)

Desain portfolio ini **sudah jadi**. Dibuat oleh teman (desainer) lewat Photoshop lalu Figma, dan sudah diwujudkan menjadi `index.html` referensi. Tugas lu bukan mendesain ulang, tapi **mengimplementasikan persis sesuai desain itu**.

1. **Sumber kebenaran visual** = `index.html` referensi + folder asset (export Photoshop/Figma). Kalau design.md ini bertentangan dengan `index.html` referensi, **ikuti `index.html`**.
2. **Jangan mengarang desain sendiri.** Jangan ganti warna, font, spacing, layout, urutan section, atau gaya animasi dari referensi.
3. **Jangan tambah section atau fitur** yang tidak ada di referensi (tidak ada multi-page, tidak ada blog, tidak ada dark mode toggle kalau di referensi tidak ada).
4. **Single page only.** Satu `index.html`, navigasi pakai anchor scroll (`#about`, `#experience`, dst.), bukan halaman terpisah.
5. **Hasil akhir harus pixel-faithful** terhadap referensi di desktop. Versi mobile dibuat responsif dengan mempertahankan gaya yang sama.

## 1. Langkah kerja

1. Baca seluruh `index.html` referensi dan lihat semua file di folder asset sebelum menulis kode.
2. Catat dari referensi: struktur section, urutan, font, palet warna, ukuran heading, spacing, radius, efek hover/animasi, dan cara asset dipakai.
3. Tulis ulang/rapikan jadi proyek final tanpa mengubah tampilan: CSS dijadikan variabel (`:root`), struktur HTML semantik, asset dipanggil dari folder yang rapi.
4. Bandingkan hasil dengan referensi section per section. Perbedaan visual = bug yang harus diperbaiki.
5. Kalau ada yang tidak jelas di referensi (misal state hover tidak ada), pilih solusi paling sederhana yang konsisten dengan gaya sekitarnya dan **tandai di komentar kode** supaya gampang dicek.

## 2. Struktur folder yang diharapkan

```
/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── main.js
└── assets/
    ├── img/        (foto, ilustrasi, mockup, export PNG/JPG/WebP)
    ├── icons/      (SVG kalau tersedia)
    ├── fonts/      (kalau font dibawa lokal)
    └── cv/         (CV_FiqhiDewaPrayastama_2026.pdf untuk tombol download)
```

Aturan asset:
- Pakai asset dari teman **apa adanya**. Jangan ganti dengan stock image atau placeholder.
- Gambar boleh dikompres/dikonversi ke WebP **selama tampilan tidak berubah**; simpan nama file asli sebagai referensi.
- Semua gambar wajib punya atribut `alt` yang bermakna.
- Icon: pakai SVG dari asset kalau ada, jangan campur library icon lain.
- Kalau ada asset yang dirujuk referensi tapi file-nya tidak ada, **berhenti dan laporkan**, jangan diganti diam-diam.

## 3. Design tokens (isi dari referensi)

Ekstrak nilai ini dari `index.html` referensi / file Figma, lalu jadikan CSS variable. Jangan menebak.

```css
:root {
  /* Warna: salin dari referensi */
  --color-bg: ;
  --color-surface: ;
  --color-text: ;
  --color-text-muted: ;
  --color-accent: ;
  --color-accent-2: ;
  --color-border: ;

  /* Tipografi: salin dari referensi */
  --font-heading: ;
  --font-body: ;
  --font-mono: ;

  /* Skala ukuran, spacing, radius, shadow: salin dari referensi */
  --space-section: ;
  --radius: ;
  --shadow: ;
  --container: ;
}
```

Kalau font memakai Google Fonts, pakai yang **sama persis** dengan referensi (family + weight). Sediakan fallback stack yang wajar.

## 4. Struktur section

Urutan dan jumlah section **mengikuti referensi**. Kerangka umum yang biasanya ada di portfolio single page seperti ini (sesuaikan dengan apa yang benar-benar ada di referensi, buang yang tidak ada):

1. **Navbar** — logo/nama + link anchor ke tiap section, sticky kalau di referensi sticky.
2. **Hero** — nama, headline/role, deskripsi singkat, tombol CTA (misal Download CV, Contact), visual utama dari asset.
3. **About** — profil singkat + foto.
4. **Skills** — daftar skill.
5. **Experience** — magang dan organisasi.
6. **Education** — riwayat pendidikan.
7. **Projects / Highlights** — proyek atau pencapaian.
8. **Contact** — kontak dan footer.

## 5. Konten (data terbaru dari CV, gantikan teks dummy di referensi)

Layout dan gaya dari referensi, **teks diisi dengan data di bawah**. Data di website lama (fiqhi.my.id) sudah usang, jangan dipakai.

**Identitas**
- Nama: Fiqhi Dewa Prayastama
- Bidang: Asuransi Kerugian (general/property-casualty insurance), risk management, business development
- Website: Fiqhi.my.id

**Tentang**
- Lulusan D3 Asuransi Kerugian, STMA Trisakti.
- Tertarik pada risk management dan industri asuransi umum.
- Punya pengalaman di administrasi, operasional, dan business development.
- Aktif di organisasi dan kepanitiaan.

**Skills**
- Komunikasi
- Kerjasama tim
- Analisis
- Microsoft Office (Word, Excel, PowerPoint)
- Canva

**Pengalaman magang**
- PT Pialang Asuransi Nasional Indonesia Jaya, Magang Bagian Administrasi (sejak 1 April 2025): mengelola surat dan dokumen masuk/keluar, membuat QS (Quotation Slip) dan CS (Closing Instruction) untuk marine, motor vehicle, dan health, menangani klaim health, membangun ulang website perusahaan, membantu staf keuangan dengan Accurate 5.
- PT Focus Inservindo, Magang Bagian Operasional (1 Des 2025 – 27 Mar 2026).
- Prodigi, Business Development (13 Nov 2023 – 8 Feb 2024).

**Organisasi**
- Ketua Divisi Ekonomi Kreatif, LDK Al-Hakim STMA Trisakti (Juli 2024 – Juli 2025): mengurus kebutuhan desain, publikasi, dan dokumentasi (videografi, fotografi).

**Pendidikan**
- D3 Asuransi Kerugian, STMA Trisakti, 2023–2026, IPK 3.57
- SMKS Al-Washliyah Jakarta, jurusan Akuntansi Keuangan Lembaga, 2020–2023, nilai rata-rata 85,33

**Sertifikat dan kegiatan**
- TOEIC Listening & Reading, skor 780 (Oktober 2025)
- MarkPlus Conference 2026 (Desember 2025)
- HackerX Ethical Hacking, modul "Know the OS" (Februari 2025)

**Kontak**
- Isi email, LinkedIn, dan WhatsApp sesuai data yang gua kasih. Kalau belum ada, pakai placeholder yang jelas (`TODO`) dan jangan mengarang nomor atau alamat.

Aturan konten:
- Kalau teks dari referensi lebih panjang/pendek dari data di atas, sesuaikan panjang teks tanpa mengubah layout. Kalau ada slot di referensi yang tidak punya data, hapus slotnya dengan rapi atau tandai `TODO`, jangan isi dengan karangan.
- Bahasa konten: Indonesia, kecuali referensi memakai bahasa Inggris untuk label tertentu.

## 6. Interaksi dan animasi

- Replikasi semua animasi/transisi yang ada di referensi (scroll reveal, hover, parallax, dll.) dengan durasi dan easing yang sama.
- Kalau referensi tidak punya animasi di suatu elemen, jangan tambahkan.
- Smooth scroll untuk link anchor, dan tandai section aktif di navbar kalau referensi melakukannya.
- Hormati `prefers-reduced-motion`: matikan animasi besar untuk pengguna yang memintanya.

## 7. Responsif

- Desktop: ikuti referensi sepersis mungkin.
- Tablet dan mobile: pertahankan gaya, warna, dan font yang sama. Susun grid jadi 1 kolom, kecilkan heading secara proporsional, navbar jadi menu hamburger kalau tidak muat.
- Tidak boleh ada scroll horizontal di semua lebar layar.
- Uji minimal di lebar 360px, 768px, 1280px, dan 1920px.

## 8. Kualitas teknis

- HTML semantik (`header`, `nav`, `main`, `section`, `footer`), satu `h1`.
- Kontras teks memadai dan fokus keyboard terlihat.
- `<title>`, meta description, dan favicon diisi. Tambahkan Open Graph image kalau ada asset yang cocok.
- Gambar di bawah fold pakai `loading="lazy"`.
- Tanpa framework berat. HTML + CSS + JS biasa sudah cukup, kecuali referensi memang memakai library tertentu.
- Performa: hindari asset yang tidak terpakai dan JS yang tidak perlu.

## 9. Deploy

- Target hosting: Hostinger, domain Fiqhi.my.id.
- Output harus berupa file statis yang siap di-upload ke `public_html` (index.html + folder css, js, assets).
- Pastikan semua path asset **relatif** supaya tidak rusak di hosting.

## 10. Definition of done

- [ ] Tampilan sama dengan `index.html` referensi di semua section
- [ ] Semua asset dari teman terpakai di tempat yang benar, tidak ada yang diganti
- [ ] Konten sudah memakai data terbaru dari CV
- [ ] Single page dengan navigasi anchor berfungsi
- [ ] Responsif di mobile tanpa scroll horizontal
- [ ] Tombol Download CV mengarah ke file PDF yang benar
- [ ] Tidak ada link mati atau placeholder `TODO` yang tertinggal tanpa dilaporkan
- [ ] Ringkasan di akhir: apa yang diikuti persis, apa yang terpaksa diputuskan sendiri, dan apa yang masih kurang
