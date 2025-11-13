# Analisis Transient Data Using Sessions

## Tujuan Tutorial
Tutorial ini mendemonstrasikan cara mengatasi sifat *stateless* dari protokol HTTP menggunakan **Sessions**. Tujuannya adalah memahami cara menyimpan data sementara pengguna (seperti penghitung kunjungan atau isi keranjang belanja) agar tetap bertahan (persisten) meskipun halaman dimuat ulang (*refresh*).

---

## Komponen Utama Kode

### A. Session Factory (`app.py`)
Agar Pyramid bisa "mengingat", kita perlu mengaktifkan mekanisme penyimpanan sesi.

1.  **`SignedCookieSessionFactory`:**
    Kita menggunakan implementasi sesi berbasis Cookie. Data disimpan di browser pengguna, bukan di database server.
2.  **Secret Key (`'rahasia_dapur_123'`):**
    Kunci ini digunakan untuk menandatangani (sign) data secara kriptografi. Ini memastikan bahwa pengguna tidak bisa memanipulasi isi cookie secara sembarangan.

### B. Session Object (`views.py`)
Di dalam logika view, sesi diakses seperti dictionary Python biasa.

1.  **`request.session`:**
    Objek ini bertindak sebagai wadah penyimpanan.
    - **Read:** `request.session.get('counter', 0)` mengambil nilai lama.
    - **Write:** `request.session['counter'] += 1` memperbarui nilai.
    Perubahan pada objek ini otomatis disimpan kembali ke cookie di akhir request.

---

## Alur Kerja (Request Lifecycle)

1.  **Request:** Browser mengirim request ke server beserta Header `Cookie` (jika sudah pernah berkunjung).
2.  **Unpacking:** Pyramid membaca cookie tersebut, memverifikasi tanda tangan keamanannya, dan membongkarnya menjadi objek `request.session`.
3.  **Logic:** Kode view menambahkan nilai `counter` (+1).
4.  **Repacking:** Setelah view selesai, Pyramid membungkus kembali data sesi yang baru menjadi format cookie.
5.  **Response:** Server mengirim HTML beserta Header `Set-Cookie` untuk memerintahkan browser memperbarui data simpanannya.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 14 46 39_8fdc5621](https://github.com/user-attachments/assets/7fba505f-f541-403c-acb7-1bb0f64ec719)

![Gambar WhatsApp 2025-11-13 pukul 14 46 40_585f8815](https://github.com/user-attachments/assets/f41c1117-2fc7-4499-bdbb-6a085ce450ea)
