# Analisis CSS/JS/Images Files With Static Assets

## Tujuan Tutorial
Tutorial ini mendemonstrasikan cara menyajikan **Static Files** (aset tetap seperti CSS, JavaScript, dan Gambar). Tujuannya adalah memahami konfigurasi `add_static_view` untuk membuka akses folder publik dan cara menghasilkan URL aset yang benar di dalam template.

---

## Komponen Utama Kode

### A. Configurator (`app.py`)
Agar browser bisa mengakses file di dalam folder komputer, kita harus membuka jalur aksesnya secara eksplisit.

1.  **`config.add_static_view(name='static', path='static')`:**
    Perintah ini memetakan URL prefix `/static` ke folder fisik bernama `static` di direktori proyek. Tanpa ini, Pyramid akan menganggap semua request sebagai rute view biasa dan mengembalikan 404.

### B. Template Helper (`home.jinja2`)
Di sisi tampilan, kita tidak menulis jalur file secara manual (hardcode), melainkan menggunakan helper function.

1.  **`request.static_url()`:**
    Kode `{{ request.static_url('static/theme.css') }}` digunakan untuk menghasilkan URL absolut yang menuju ke file aset. Ini memastikan link tetap valid meskipun struktur aplikasi atau domain berubah.

---

## Alur Kerja (Request Lifecycle)

1.  **Setup:** `app.py` mendaftarkan folder `static` agar bisa diakses publik.
2.  **Rendering:** Saat merender HTML, `request.static_url` mengubah path relatif menjadi URL lengkap (misal: `http://localhost:6543/static/theme.css`).
3.  **Browser Parsing:** Browser membaca HTML, menemukan tag `<link>`, dan mengirim request terpisah ke server untuk mengambil file CSS.
4.  **Serving File:** Pyramid menerima request `/static/...`, langsung mencari file di folder yang sesuai, dan mengirimkannya ke browser untuk diterapkan pada tampilan.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 14 21 03_ac4e61c9](https://github.com/user-attachments/assets/95b01851-7d18-4364-b946-b6df1c6717a9)
