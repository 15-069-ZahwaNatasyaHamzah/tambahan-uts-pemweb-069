# Analisis Application Configuration with .ini Files

## Tujuan Tutorial

Tujuan dari tutorial ini adalah untuk mendemonstrasikan cara kerja file konfigurasi .ini dalam aplikasi Pyramid. Tutorial ini mengajarkan dua konsep utama:
1. Menambah Pengaturan Kustom: Cara menambahkan parameter konfigurasi Anda sendiri (di luar pengaturan standar server) ke dalam file development.ini.
2. Mengakses Pengaturan: Cara mengakses dan menggunakan nilai-nilai konfigurasi ini di dua tempat berbeda:
   - Saat startup aplikasi (di dalam fungsi factory main).
   - Saat runtime (di dalam view callable seperti hello_world).
Ini penting untuk memisahkan konfigurasi (seperti debug flags, secret keys, atau database URLs) dari logika kode aplikasi.

## Komponen Utama Kode 

Tutorial ini memodifikasi dua file yang ada dari tutorial sebelumnya (development.ini dan tutorial/__init__.py) untuk mengalirkan data konfigurasi.

### A. development.ini (File Konfigurasi)

File ini diperbarui dengan menambahkan key-value pair kustom kita sendiri di bawah bagian [app:main].

```Ini, TOML
[app:main]
use = egg:tutorial

# Pengaturan bawaan Pyramid untuk auto-reload template
pyramid.reload_templates = true

# Pengaturan kustom yang kita tambahkan
tutorial.debug = true

[server:main]
use = egg:waitress#main
host = 0.0.0.0
port = 6543
```

1. [app:main]: Bagian ini berisi pengaturan yang akan diteruskan ke aplikasi Pyramid kita.
2. tutorial.debug = true: Ini adalah pengaturan kustom yang kita ciptakan. pserve akan membaca baris ini dan menambahkannya ke dictionary pengaturan.

### B. tutorial/__init__.py (Pabrik Aplikasi & View)

File Python ini dimodifikasi untuk menerima dan menggunakan pengaturan baru.

```python
   from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.util import asbool # Utility untuk konversi string 'true'/'false'

# 1. Mengakses pengaturan saat startup (di 'main')
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # 'settings' adalah dict dari [app:main] di file .ini
    # Kita bisa periksa pengaturan di sini
    debug_mode = asbool(settings.get('tutorial.debug', False))
    # ... bisa lakukan sesuatu dengan debug_mode jika perlu ...

    # Penting: 'settings' harus diteruskan ke Configurator
    with Configurator(settings=settings) as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        return config.make_wsgi_app()

# 2. Mengakses pengaturan saat runtime (di 'view')
def hello_world(request):
    # 'request.registry.settings' adalah cara standar
    # untuk mengakses 'settings' dari dalam sebuah view.
    settings = request.registry.settings
    debug_mode = asbool(settings.get('tutorial.debug', False))

    if debug_mode:
        return Response('Hello World! (Debug Mode IS ON)')
    else:
        return Response('Hello World!')
```

1. def main(global_config, **settings): Parameter **settings secara otomatis mengumpulkan semua key-value dari bagian [app:main] ke dalam sebuah dictionary Python.
3. asbool: Menggunakan utilitas asbool adalah praktik terbaik karena nilai di file .ini selalu berupa string ("true", "false"). asbool akan mengonversinya ke Boolean Python (True, False).
3. with Configurator(settings=settings) as config: Baris ini sangat penting. Kita "menyimpan" dictionary settings ke dalam konfigurasi aplikasi.
4. request.registry.settings: Setelah disimpan di Configurator, Pyramid membuat pengaturan tersebut tersedia untuk semua view melalui request.registry.settings.

### Alur Kerja (Alur Data Konfigurasi)

Alur kerja ini menjelaskan bagaimana data dari file .ini mengalir ke view.

1. Alur Kerja Startup (Pemuatan Konfigurasi)
   
   - Pengguna menjalankan pserve development.ini.
   - pserve membaca development.ini.
   - Ia melihat [app:main] dan membuat dictionary settings, contoh: {'use':'egg:tutorial', 'pyramid.reload_templates': 'true','tutorial.debug':'true'}.
   - pserve memanggil entry point main dari tutorial (sesuai setup.py).
   - pserve menyuntikkan dictionary ini sebagai argumen **settings ke fungsi def main(...).
   - Di dalam main, dictionary settings ini diteruskan keConfigurator(settings=settings).
   - Configurator mengambil settings tersebut dan menyimpannya di lokasi sentral aplikasi yang disebut Registry.
   - Aplikasi WSGI (app) yang sudah jadi, yang kini "sadar" akan konfigurasinya, diserahkan ke server waitress.

2. Alur Kerja Request (Penggunaan Konfigurasi)
   
   - Pengguna membuka http://localhost:6543/.
   - waitress menerima permintaan dan memberikannya ke aplikasi Pyramid.
   - Pyramid mencocokkan rute / ke view hello_world.
   - Pyramid membuat objek request untuk permintaan ini. Objek request ini memiliki akses ke Registry aplikasi.
   - Pyramid memanggil hello_world(request).
   - Di dalam view, request.registry.settings dieksekusi untuk mengambil dictionary settings dari Registry.
   - Kode settings.get('tutorial.debug', False) digunakan untuk memeriksa nilai konfigurasi.
   - Karena tutorial.debug adalah true di file .ini, view mengembalikan Response('Hello World! (Debug Mode IS ON)').
