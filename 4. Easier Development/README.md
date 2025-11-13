# Analisis asier Development with debugtoolbar

## Tujuan Tutorial

Tujuan tutorial ini adalah untuk menginstal dan mengaktifkan pyramid_debugtoolbar, sebuah add-on (pengaya) yang sangat berguna untuk development.

Toolbar ini akan muncul di browser dan memberikan informasi debugging secara real-time (seperti request, logs, dan pengaturan) serta menampilkan traceback yang interaktif jika terjadi error.

---

## Komponen Utama Kode

Untuk mengaktifkan add-on ini, kita hanya perlu memodifikasi 2 file konfigurasi. Kita tidak perlu mengubah file logika tutorial/_init_.py.

---

### A. setup.py (Menambah Dependensi)

Kita perlu memberi tahu Python bahwa proyek kita sekarang memiliki dependensi baru yang khusus untuk development.

```python
# ... (kode setup.py lainnya) ...

# Dependensi utama
requires = [
    'pyramid',
    'waitress',
]

# Dependensi khusus untuk development
dev_requires = [
    'pyramid_debugtoolbar',
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires, # Mendaftarkan 'dev' requirements
    },
    # ... (kode entry_points lainnya) ...
)
```

1. dev_requires: Kita menambahkan pyramid_debugtoolbar ke daftar terpisah.
2. extras_require={'dev': ...}: Ini memungkinkan kita menginstalnya dengan perintah khusus pip install -e ".[dev]".

### B. development.ini (Mengaktifkan Add-on)

Setelah terinstal, kita perlu memberi tahu aplikasi Pyramid untuk "memuat" atau "meng-include" add-on ini saat aplikasi dijalankan.

```Ini, TOML
   [app:main]
use = egg:tutorial

# BARIS INI DITAMBAHKAN
pyramid.includes =
    pyramid_debugtoolbar

# ... (pengaturan .ini lainnya) ...

[server:main]
# ... (server config) ...
```

## Alur Kerja (Bagaimana Toolbar Muncul)

1. Pengguna menginstal dependensi development dengan pip install -e ".[dev]".
2. Pengguna menjalankan pserve development.ini --reload.
3. pserve memuat aplikasi main dari tutorial.
4. Saat Configurator di dalam main dijalankan, ia membaca development.ini.
5. Configurator melihat pengaturan pyramid.includes = pyramid_debugtoolbar.
6. Pyramid secara otomatis memuat add-on tersebut, yang "membungkus" aplikasi kita.
7. Saat browser meminta halaman (http://localhost:6543/), aplikasi Pyramid merender response "Hello World!".
8. Sebelum mengirimkannya ke browser, pyramid_debugtoolbar menyuntikkan (inject) HTML, CSS, dan JavaScript-nya sendiri ke dalam response tersebut.
9. Hasilnya, browser menampilkan "Hello World!" dan juga logo/panel debug toolbar di sisi halaman.
