# Analisis Databases Using SQLAlchemy

## Tujuan Tutorial
Tutorial ini mendemonstrasikan integrasi database SQL (SQLite) ke dalam aplikasi Pyramid menggunakan **SQLAlchemy**. Tujuannya adalah memahami konsep **ORM (Object Relational Mapping)** untuk memanipulasi data menggunakan kode Python (bukan SQL mentah) serta manajemen transaksi otomatis.

---

## Komponen Utama Kode

### A. Data Model / ORM (`models.py`)
Kita mendefinisikan struktur database menggunakan Class Python, bukan perintah SQL `CREATE TABLE`.

1.  **Declarative Base:**
    Class `Page(Base)` adalah representasi tabel. Setiap atribut (`title`, `body`) dipetakan langsung menjadi kolom di database.
2.  **Scoped Session:**
    `DBSession` dikonfigurasi sebagai *scoped session*, artinya setiap HTTP Request akan memiliki koneksi databasenya sendiri yang terisolasi (Thread-Safe).

### B. Transaction Manager (`app.py`)
Kita menggunakan pustaka `pyramid_tm` untuk mengelola siklus hidup penyimpanan data.

1.  **Automatic Commit/Rollback:**
    Kita tidak perlu menulis `session.commit()` secara manual di view.
    - Jika request sukses (return 200 OK), `pyramid_tm` otomatis menyimpan perubahan (Commit).
    - Jika terjadi error (Exception), `pyramid_tm` otomatis membatalkan perubahan (Rollback). Ini menjamin integritas data.

---

## Alur Kerja (Request Lifecycle)

1.  **Initialization:** Saat aplikasi start, `Base.metadata.create_all(engine)` mengecek dan membuat file database/tabel jika belum ada.
2.  **Request:** View `add_page` dipanggil.
3.  **Operation:** Kode mengeksekusi `DBSession.add(new_page)`. Objek baru ditambahkan ke sesi memori sementara.
4.  **Response & Commit:** View selesai dan mengembalikan response. Transaction Manager mendeteksi sukses, lalu menulis data secara permanen ke file `tutorial.sqlite`.
5.  **Query:** Pada request berikutnya, `DBSession.query(Page).all()` mengambil data tersebut dan menampilkannya di template.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 17 36 31_144ce2aa](https://github.com/user-attachments/assets/d2ecb331-4e8b-4529-ba00-e09e45c6318c)

![Gambar WhatsApp 2025-11-13 pukul 17 37 38_fd61a71f](https://github.com/user-attachments/assets/b05c6e23-ddb3-4b41-977d-e5f705263654)

![Gambar WhatsApp 2025-11-13 pukul 17 38 12_ff864a3c](https://github.com/user-attachments/assets/a1ee1eae-d778-4382-b189-2666ad1e0755)
