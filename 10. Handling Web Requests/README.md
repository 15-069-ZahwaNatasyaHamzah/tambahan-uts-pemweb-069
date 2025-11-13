# Analisis Handling Web Requests and Responses

## Tujuan Tutorial
Tutorial ini mendemonstrasikan interaksi dengan objek **Request** dan fleksibilitas Pyramid dalam menghasilkan berbagai jenis **Response** (HTML, Teks Mentah, dan JSON) untuk kebutuhan aplikasi modern.

---

## Komponen Utama Kode

### A. View Class (`views.py`)
Penggunaan Class (`TutorialViews`) memungkinkan pengelolaan request yang lebih terstruktur dibandingkan fungsi biasa.

1.  **Inisialisasi Request:**
    Objek `request` disuntikkan sekali pada `__init__` sehingga bisa diakses oleh semua method menggunakan `self.request` (contoh: mengambil `self.request.url`).

2.  **Variasi Response:**
    * **HTML (Standard):** Method `home` mengembalikan dictionary yang diproses oleh renderer template (`home.pt`).
    * **Plain Text (Manual):** Method `plain` mengembalikan objek `Response()` secara langsung. Ini mem-bypass template engine untuk mengirim teks mentah ke browser.
    * **JSON (API):** Method `json_view` menggunakan `renderer='json'`. Pyramid otomatis mengubah Dictionary Python menjadi format JSON yang valid untuk pertukaran data.

### B. Configurator (`app.py`)
Menggunakan `config.scan()` untuk secara otomatis mendeteksi dan menghubungkan rute (`/`, `/plain`, `/json`) dengan dekorator `@view_config` yang ada di dalam Class View.

---

## Alur Kerja (Request Lifecycle)

1.  **Akses Home (`/`):** Pyramid mengolah data via template $\rightarrow$ Browser menerima **HTML**.
2.  **Akses Plain (`/plain`):** Pyramid mengembalikan objek `Response` langsung $\rightarrow$ Browser menerima **Teks Mentah**.
3.  **Akses JSON (`/json`):** Pyramid melakukan serialisasi data via renderer JSON $\rightarrow$ Browser menerima **Data API (JSON)**.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 09 17 33_378df9e4](https://github.com/user-attachments/assets/58247ff5-700d-4a24-bfb5-bfc88039b2c1)

![Gambar WhatsApp 2025-11-13 pukul 09 17 52_f3d52068](https://github.com/user-attachments/assets/14f19ed2-6639-40fd-a0fe-630d64e82ce9)

![Gambar WhatsApp 2025-11-13 pukul 09 18 13_331ab0d0](https://github.com/user-attachments/assets/808d504f-19a0-43ad-892b-e312fbda015a)
