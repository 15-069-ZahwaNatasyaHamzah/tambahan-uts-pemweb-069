# Analisis AJAX Development With JSON Renderers

## Tujuan Tutorial
Tutorial ini mendemonstrasikan implementasi **AJAX (Asynchronous JavaScript and XML)** pada aplikasi Pyramid. Tujuannya adalah memahami cara menyajikan data mentah (JSON) dari server dan mengonsumsinya di sisi klien (Browser) menggunakan JavaScript tanpa perlu memuat ulang halaman (No Page Reload).

---

## Komponen Utama Kode

### A. JSON Renderer (`app.py`)
Pyramid mempermudah pembuatan API dengan menyediakan renderer bawaan untuk JSON.

1.  **`renderer='json'`:**
    Dekorator `@view_config(renderer='json')` secara otomatis melakukan serialisasi objek Python (Dictionary) menjadi string JSON.
2.  **Content-Type:**
    Renderer ini juga otomatis mengatur Header HTTP menjadi `application/json`, sehingga browser memahami bahwa respons yang diterima adalah data, bukan HTML.

### B. Client-Side Script (`home.jinja2`)
Di sisi tampilan, kita menggunakan JavaScript modern untuk berkomunikasi dengan server.

1.  **`fetch()` API:**
    Fungsi native JavaScript untuk melakukan request HTTP di latar belakang (background).
2.  **DOM Manipulation:**
    Setelah data JSON diterima, JavaScript memparsing data tersebut (`response.json()`) dan memperbarui elemen HTML (`innerText`) secara dinamis.

---

## Alur Kerja (Request Lifecycle)

1.  **User Action:** Pengguna mengklik tombol "Ambil Data".
2.  **Async Request:** JavaScript mengeksekusi `fetch('/howdy.json')`, mengirim request ke server tanpa mematikan halaman yang aktif.
3.  **Server Processing:** Pyramid menjalankan view `hello_json`, mengembalikan dictionary, dan `renderer='json'` mengubahnya menjadi format JSON.
4.  **Client Receive:** Browser menerima data JSON `{ "message": "Halo!..." }`.
5.  **UI Update:** JavaScript menangkap data tersebut dan menyisipkannya ke dalam kotak HTML. Hasilnya, konten halaman berubah seketika.


## Screenshoot Hasil 

![Gambar WhatsApp 2025-11-13 pukul 14 27 45_ada1bbdc](https://github.com/user-attachments/assets/0b2160da-25cd-40a0-a1e6-e27d58808de1)

![Gambar WhatsApp 2025-11-13 pukul 14 28 08_2a8364a9](https://github.com/user-attachments/assets/37e52bd1-bba0-4fbb-a3ed-b64178f6eda2)
