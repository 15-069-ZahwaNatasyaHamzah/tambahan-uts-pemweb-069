# Analisis Forms and Validation

## Tujuan Tutorial
Tutorial ini mendemonstrasikan pembuatan formulir web yang aman dan terstruktur. Tujuannya adalah memahami penggunaan **Schema** untuk mendefinisikan aturan data, serta memanfaatkan pustaka eksternal (`deform`) untuk men-generate HTML formulir dan menangani validasi input secara otomatis.

---

## Komponen Utama Kode

### A. Schema Definition (`colander`)
Kita tidak memeriksa input secara manual (misal: `if request.POST['title'] == ''`). Sebaliknya, kita mendefinisikan "kontrak" data menggunakan `colander`.

1.  **`MappingSchema`:**
    Mendefinisikan struktur data yang diharapkan.
2.  **`SchemaNode`:**
    Menentukan tipe data (String, Integer) dan aturan validasi (misal: wajib diisi) untuk setiap kolom. Contoh: `title = colander.SchemaNode(colander.String())`.

### B. Form Handling (`deform`)
Library ini bekerja sebagai jembatan antara Schema dan HTML.

1.  **Rendering:**
    Perintah `form.render()` otomatis mengubah Schema menjadi kode HTML lengkap (`<input>`, `<label>`, tombol submit).
2.  **Validation:**
    Perintah `form.validate(controls)` membandingkan data yang dikirim user (POST) dengan aturan Schema.

---

## Alur Kerja (Request Lifecycle)

1.  **GET Request (Load):** User membuka halaman. Kode mendeteksi ini bukan submit, lalu menampilkan formulir kosong.
2.  **POST Request (Submit):** User mengirim data. Kode mendeteksi tombol submit ditekan.
3.  **Validation Process:**
    - Data dikirim ke `form.validate()`.
    - **Jika Valid:** Data dikembalikan sebagai dictionary bersih (`appstruct`), lalu diproses (misal: disimpan ke database).
    - **Jika Invalid:** Deform melempar `ValidationFailure`. Kode menangkap error ini dan merender ulang formulir, lengkap dengan pesan kesalahan (merah) di kolom yang bermasalah.

## Screeanshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 14 54 58_b92c5e8d](https://github.com/user-attachments/assets/c84b524a-56c2-405e-b878-a006fe6a5366)

![Gambar WhatsApp 2025-11-13 pukul 14 54 58_72fa6782](https://github.com/user-attachments/assets/7d6d63c2-f227-489b-b549-c3d33a701529)
