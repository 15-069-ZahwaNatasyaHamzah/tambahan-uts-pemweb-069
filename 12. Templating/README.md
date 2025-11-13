# Analisis Templating With jinja2

## Tujuan Tutorial
Tutorial ini mendemonstrasikan cara mengganti templating engine bawaan (Chameleon) dengan **Jinja2**. Tujuannya adalah memahami cara mengintegrasikan library eksternal ke dalam konfigurasi Pyramid dan mengenali perbedaan sintaks template yang lebih populer di ekosistem Python.

---

## Komponen Utama Kode

### A. Configurator (`app.py`)
Agar Pyramid mengenali Jinja2, kita harus mendaftarkannya secara eksplisit karena ia bukan bagian dari core minimal Pyramid.

1.  **`config.include('pyramid_jinja2')`:**
    Perintah ini mengaktifkan binding Jinja2, memungkinkan aplikasi mengenali dan merender file berekstensi `.jinja2`.

### B. Template Syntax (`home.jinja2`)
Perbedaan utama terletak pada sintaks penulisan variabel di dalam file HTML.

1.  **Interpolasi Variabel:**
    Jinja2 menggunakan kurung kurawal ganda `{{ variable }}` untuk menampilkan data. Ini berbeda dengan Chameleon yang menggunakan `${variable}`.
2.  **Python-like:**
    Sintaks Jinja2 dirancang sangat mirip dengan struktur bahasa Python, membuatnya menjadi standar industri untuk framework web Python (seperti Flask dan Django).

---

## Alur Kerja (Request Lifecycle)

1.  **Setup:** Saat aplikasi dimulai, `config.include` memuat pustaka `pyramid_jinja2`.
2.  **View Execution:** View `home_view` dipanggil dan mengembalikan dictionary data (misal: `{'name': 'Zahwa'}`).
3.  **Rendering:** Pyramid mendeteksi `renderer='home.jinja2'`, lalu menyerahkan data tersebut ke mesin Jinja2.
4.  **Interpolasi:** Jinja2 mengganti placeholder `{{ name }}` dengan nilai "Zahwa" di dalam HTML.
5.  **Response:** Browser menerima HTML final yang sudah matang.

## Screenshoot Hasil

![Gambar WhatsApp 2025-11-13 pukul 14 00 51_f1d866d3](https://github.com/user-attachments/assets/eddad8a2-6434-4653-8beb-ea95eea590e0)
