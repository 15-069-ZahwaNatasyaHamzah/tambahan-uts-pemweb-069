# Analisis Collecting Application Info With Logging

## Tujuan Tutorial
Tutorial ini mendemonstrasikan implementasi sistem **Logging** (Pencatatan) standar pada aplikasi Pyramid. Tujuannya adalah memahami cara merekam aktivitas aplikasi secara terstruktur dengan informasi waktu (timestamp) dan tingkat prioritas, menggantikan penggunaan `print()` yang terbatas.

---

## Komponen Utama Kode

### A. Logger Initialization (`app.py`)
Kita menggunakan modul bawaan Python `logging` untuk membuat objek pencatat.

1.  **`log = logging.getLogger(__name__)`:**
    Baris ini membuat *instance* logger yang terikat dengan nama modul saat ini. Ini praktik standar agar kita tahu dari file mana pesan log berasal.
2.  **`basicConfig`:**
    Konfigurasi awal untuk menentukan format output (misalnya: menampilkan jam `%(asctime)s` dan level pesan `%(levelname)s`) serta kemana log akan dicetak (ke terminal/console).

### B. Logging Levels
Di dalam fungsi view, kita mencatat pesan dengan tingkat kepentingan yang berbeda.

1.  **`log.info()`:** Digunakan untuk mencatat kejadian normal (informasi umum), seperti "User membuka halaman".
2.  **`log.warning()`:** Digunakan untuk mencatat sesuatu yang tidak diharapkan tetapi aplikasi masih bisa berjalan.
    
    Penggunaan level ini memudahkan filtering saat kita melakukan *debugging* atau audit sistem.

---

## Alur Kerja (Request Lifecycle)

1.  **Startup:** Saat server dinyalakan, `logging.basicConfig` mengaktifkan aliran output ke terminal.
2.  **Request:** Pengguna mengakses halaman Home.
3.  **Execution:** View `home` dijalankan. Kode mengeksekusi `log.info("...")`.
4.  **Output:** Sistem logging menangkap pesan tersebut, menempelkan waktu saat ini (Timestamp), dan mencetaknya ke layar terminal (Standard Output) secara real-time.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 14 42 16_fcb125a0](https://github.com/user-attachments/assets/695c8865-a047-4ce6-9269-b670930a9887)

![Gambar WhatsApp 2025-11-13 pukul 14 42 17_1a35c8a8](https://github.com/user-attachments/assets/98b22a3e-51e0-4ebd-857a-4b6778d42fe1)
