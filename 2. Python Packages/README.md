# Analisis Python Packages for Pyramid Applications

## Tujuan Tutorial

Tujuan dari tutorial ini adalah untuk mengubah aplikasi web "Hello World" yang sebelumnya berbentuk satu file (.py) menjadi sebuah paket Python (Python package) yang terstruktur dan dapat diinstal.

Ini adalah langkah fundamental untuk membangun aplikasi yang lebih besar dan lebih terorganisir. Tutorial ini memperkenalkan konsep-konsep kunci untuk skalabilitas :
1. Struktur Proyek: Mengubah satu file menjadi struktur direktori paket (tutorial/__init__.py).
2. Manajemen Dependensi: Menggunakan setup.py untuk mendefinisikan apa saja yang dibutuhkan oleh aplikasi (misalnya, pyramid, waitress).
3. Konfigurasi Eksternal: Menggunakan file .ini (development.ini) untuk mengelola pengaturan server dan aplikasi, alih-alih melakukan hardcoding di dalam file Python.
4. Server Produksi (Entry-level): Mengganti server bawaan Python (wsgiref) dengan server WSGI yang lebih mumpuni, yaitu waitress.
5. Entry Points: Memperkenalkan konsep entry points agar aplikasi dapat dijalankan oleh runner standar seperti pserve.

---

## Komponen Utama Kode

Tutorial ini merombak struktur file tunggal menjadi paket yang dapat diinstal. Komponen utamanya adalah tiga file baru yang bekerja bersama:

---

### A. setup.py (Manajer Paket & Dependensi)

File ini memberi tahu Python cara menginstal paket Anda dan apa saja dependensinya.

```python
from setuptools import setup

# List dependensi yang dibutuhkan
requires = [
    'pyramid',
    'waitress', # Server WSGI
]

setup(
    name='tutorial',
    install_requires=requires,
    # 'Entry points' adalah "iklan" paket Anda ke dunia luar
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main', # Menghubungkan nama 'main' ke fungsi 'main' di 'tutorial'
        ],
    },
)
```

1. requires: Mendefinisikan dependensi proyek. Sekarang kita secara eksplisit menyatakan bahwa aplikasi ini membutuhkan pyramid dan waitress.
2. entry_points: Ini adalah bagian krusial. Ini memberitahu sistem (khususnya runner pserve) bahwa jika ada yang meminta aplikasi bernama main dari paket tutorial, ia harus memanggil fungsi main yang ada di dalam modul tutorial (yaitu, file tutorial/__init__.py).

### B. development.ini (File Konfigurasi)

File ini mengontrol bagaimana aplikasi dijalankan, memisahkan konfigurasi dari logika kode.

```Ini, TOML
[app:main]
use = egg:tutorial # Gunakan 'main' entry point dari paket 'tutorial'

[server:main]
use = egg:waitress#main # Gunakan 'waitress' sebagai server
host = 0.0.0.0
port = 6543
```

1. [app:main]: Mendefinisikan aplikasi utama kita. use = egg:tutorial menginstruksikan pserve untuk menggunakan entry point main yang terkait dengan paket tutorial (yang telah kita definisikan di setup.py).
2. [server:main]: Mengonfigurasi server. use = egg:waitress#main menentukan bahwa kita ingin menggunakan server waitress. Pengaturan host dan port sekarang dikelola di sini, bukan di dalam kode Python.

### C. tutorial/__init__.py (Pabrik Aplikasi / App Factory)

Logika aplikasi dari tutorial pertama kini dipindahkan ke dalam file __init__.py dan dibungkus dalam sebuah fungsi "pabrik" (factory).

```Python
from pyramid.config import Configurator
from pyramid.response import Response

# Fungsi view tetap sama
def hello_world(request):
    return Response('Hello World!')

# Ini adalah 'App Factory'
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()
```

1. def main(...): Fungsi ini sekarang menjadi "pabrik" aplikasi kita. Ini adalah fungsi yang dipanggil oleh entry point yang kita definisikan di setup.py. Ia menerima konfigurasi global dan pengaturan khusus aplikasi (dari file .ini).
2. with Configurator(settings=settings) as config: Logika konfigurasi (menambah rute dan view) sekarang berada di dalam fungsi main ini.
3. return config.make_wsgi_app(): Fungsi main mengembalikan aplikasi WSGI yang sudah jadi, yang kemudian akan dijalankan oleh server (waitress).

## Alur Kerja (Eksekusi & Request)

Alur kerja sekarang terbagi menjadi dua fase: (1) Instalasi & Eksekusi Server, dan (2) Penanganan Request.

### 1. Fase Eksekusi Server

Ini adalah langkah-langkah untuk menjalankan server :

1. Pengguna menjalankan pip install -e . di terminal. Ini menginstal paket tutorial dalam mode "editable" dan mendaftarkan entry point nya ke sistem Python.
2. Pengguna menjalankan pserve development.ini --reload.
3. Perintah pserve membaca file development.ini.
4. Ia melihat [server:main] dan memuat server waitress.
5. Ia melihat [app:main] (use = egg:tutorial) dan mencari entry point main dari paket tutorial (yang terdaftar di setup.py).
6. pserve memanggil fungsi main di tutorial/__init__.py, menyuplai pengaturan dari file .ini.
7. Fungsi main berjalan, mengonfigurasi rute (/) dan view (hello_world), lalu mengembalikan aplikasi WSGI (app) yang sudah jadi.
8. Server waitress kini berjalan di http://0.0.0.0:6543, siap melayani app tersebut.

### 2. Fase Penanganan Request

Ini adalah apa yang terjadi ketika pengguna mengakses web :

1. Pengguna membuka http://localhost:6543/ di browser.
2. Server waitress menerima permintaan untuk URL /.
3. waitress meneruskan permintaan ke aplikasi WSGI Pyramid (app) yang dibuat oleh fungsi main.
4. Pyramid (via Configurator) memeriksa tabel rutenya.
5. URL / cocok dengan rute yang dinamai hello.
6. Pyramid memeriksa view mana yang terhubung ke rute hello.
7. Pyramid menemukan bahwa view hello_world terhubung ke rute tersebut.
8. Pyramid menjalankan fungsi hello_world(request).
9. Fungsi mengembalikan objek Response('Hello World!').
10. Pyramid (melalui waitress) mengirimkan respons tersebut kembali ke browser.
