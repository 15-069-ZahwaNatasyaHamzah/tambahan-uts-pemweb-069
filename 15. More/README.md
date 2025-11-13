# Analisis More With View Classes

## Tujuan Tutorial
Tutorial ini mendemonstrasikan pengelolaan struktur kode yang lebih efisien dengan menggabungkan beberapa view terkait ke dalam satu Class. Tujuannya adalah memahami konsep **Shared State** antar view dan cara melakukan **URL Generation** (pembuatan link otomatis) untuk navigasi antar-halaman yang aman.

---

## Komponen Utama Kode

### A. View Class Structure (`views.py`)
Kita menggunakan satu Class (`TutorialViews`) untuk menangani beberapa rute sekaligus (`home` dan `hello`).

1.  **Shared Initialization:**
    Constructor `__init__` menerima objek `request` dan menyimpannya. Ini memungkinkan semua method view di dalam class tersebut (`home`, `hello`) mengakses properti request yang sama tanpa perlu deklarasi berulang.
2.  **Method Grouping:**
    Mengelompokkan logika yang saling berhubungan (misalnya alur navigasi user) dalam satu wadah membuat kode lebih terorganisir (High Cohesion).

### B. URL Generation (`request.route_url`)
Di dalam template, kita tidak menulis link secara manual (hardcode) seperti `<a href="/hello">`, melainkan menggunakan generator.

1.  **`request.route_url('nama_rute')`:**
    Fungsi ini meminta Pyramid untuk mencari konfigurasi rute bernama `'hello'` dan membuatkan URL lengkapnya secara otomatis.
2.  **Maintainability:**
    Jika di masa depan kita mengubah *path* URL di `app.py` (misal dari `/hello` menjadi `/hi`), kita **tidak perlu** mengedit file HTML, karena link akan menyesuaikan diri secara otomatis.

---

## Alur Kerja (Request Lifecycle)

1.  **Instantiation:** Saat request masuk, Pyramid membuat *instance* baru dari class `TutorialViews` dan menyuntikkan `request`.
2.  **Rendering:** Saat merender template `home.pt`, kode `${request.route_url('hello')}` dieksekusi. Pyramid mencocokkan nama rute dan menghasilkan string URL yang valid.
3.  **Navigation:** Browser menampilkan link. Saat user mengkliknya, Pyramid kembali memproses request baru, memanggil method `hello` dari class yang sama, dan menampilkan halaman tujuan.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 14 33 48_6805ce6e](https://github.com/user-attachments/assets/2fddcf86-87cc-4144-89b7-58e7dbc593f8)

![Gambar WhatsApp 2025-11-13 pukul 14 33 48_bc1db3c9](https://github.com/user-attachments/assets/a2214652-325e-4413-926d-ab5ac6f3d755)
