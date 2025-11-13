# Analisis Protecting Resources With Authorization

## Tujuan Tutorial
Tutorial ini mendemonstrasikan implementasi **Authorization** (Hak Akses) menggunakan sistem **ACL (Access Control List)**. Tujuannya adalah membedakan antara *Authentication* (Siapa Anda?) dan *Authorization* (Apa yang boleh Anda lakukan?), serta melindungi halaman sensitif agar hanya bisa diakses oleh pengguna dengan privilese tertentu.

---

## Komponen Utama Kode

### A. Context Factory / ACL (`app.py`)
Kita mendefinisikan aturan keamanan terpusat pada Class `RootFactory`.

1.  **`__acl__` (Access Control List):**
    Adalah daftar tuple yang mendefinisikan hak akses.
    - `(Allow, Everyone, 'view')`: Memberikan izin 'view' kepada semua pengunjung.
    - `(Allow, 'editor', 'edit')`: Memberikan izin khusus 'edit' **hanya** kepada user dengan ID 'editor'. User lain tidak akan mendapatkan izin ini.

### B. View Permission (`views.py`)
Kita memasang "gembok" pada fungsi view tertentu menggunakan parameter `permission`.

1.  **`permission='edit'`:**
    Dekorator `@view_config(..., permission='edit')` menginstruksikan Pyramid untuk memverifikasi apakah user yang sedang login memiliki hak 'edit' sebelum menjalankan fungsi view tersebut.

---

## Alur Kerja (Request Lifecycle)

1.  **Request:** User mengakses URL `/hello` (Halaman Rahasia).
2.  **Authentication:** Sistem mengecek cookie dan menentukan identitas User (misal: `viewer` atau `editor`).
3.  **Context Lookup:** Pyramid memanggil `RootFactory` untuk mengambil daftar aturan ACL.
4.  **Authorization Check:**
    - View target membutuhkan izin `'edit'`.
    - Jika User adalah `editor`: ACL menemukan aturan yang cocok. **Akses Diberikan**.
    - Jika User adalah `viewer`: Tidak ada aturan ACL yang memberikan hak 'edit' ke viewer. **Akses Ditolak**.
5.  **Forbidden Handling:** Jika akses ditolak, Pyramid memicu `HTTPForbidden`. Kode `@forbidden_view_config` menangkap error ini dan mengarahkan user kembali ke halaman Login secara otomatis.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 18 23 31_df03530d](https://github.com/user-attachments/assets/5bcde44e-0f65-469b-bd02-d64482b357a8)

![Gambar WhatsApp 2025-11-13 pukul 18 23 31_7e2798e8](https://github.com/user-attachments/assets/12258990-8b55-4ea4-9db4-371d7e375bd9)

![Gambar WhatsApp 2025-11-13 pukul 18 23 32_7428e71d](https://github.com/user-attachments/assets/58a424ba-e958-49d3-a637-e8055fddbf2e)

![Gambar WhatsApp 2025-11-13 pukul 18 23 32_2f66439b](https://github.com/user-attachments/assets/07c6f37e-4e2a-44ea-9fb0-d2b4d9184500)
