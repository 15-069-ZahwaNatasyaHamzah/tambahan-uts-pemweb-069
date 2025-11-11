# Analisis Basic Web Handling With Views

## Tujuan Tutorial 

Tujuan tutorial ini adalah untuk merombak (refactor) aplikasi kita agar lebih terorganisir dan bertenaga. Ini memperkenalkan dua konsep utama:

1. File views.py: Memindahkan semua fungsi view (logika) keluar dari __init__.py ke dalam file terpisah (tutorial/views.py) agar kode lebih bersih.
2. @view_config Decorator: Mengganti pendaftaran view manual (seperti config.add_view()) dengan decorator @view_config. Ini memungkinkan view itu sendiri "mengiklankan" rute mana yang terhubung dengannya.
3. config.scan(): Memperkenalkan pemindai (scanner) yang secara otomatis menemukan decorator @view_config tersebut.
4. Parameter URL Dinamis: Menunjukkan cara menangkap bagian dari URL (misalnya, nama dalam /hello/Jane) menggunakan matchdict.

---

## Komponen Utama Kode

Tutorial ini secara signifikan mengubah __init__.py, membuat file views.py baru, dan memperbarui tests.py.

### A. tutorial/views.py (File BARU)

Semua logika view sekarang tinggal di sini, dihiasi (decorated) dengan @view_config.

```python
from pyramid.response import Response
from pyramid.view import view_config

# View 1: Dihubungkan ke rute 'home'
@view_config(route_name='home')
def home_view(request):
    return Response('Hello World!')

# View 2: Dihubungkan ke rute 'hello'
@view_config(route_name='hello')
def hello_view(request):
    # Mengambil parameter 'name' dari URL
    name = request.matchdict['name']
    return Response('Hello, {}!'.format(name))
```

1. @view_config(route_name=...): Ini adalah decorator yang memberi tahu Pyramid, "Fungsi di bawahku ini adalah view yang harus dijalankan ketika rute dengan nama ... cocok."
2. request.matchdict['name']: Ini adalah cara mengambil nilai dari bagian {name} yang didefinisikan dalam rute.

3. ### B. tutorial/__init__.py (Dimodifikasi)

4. Fungsi main sekarang jauh lebih sederhana. Tugasnya hanya mendaftarkan rute (routing) dan memindai (scanning) view.

```python
   from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        # 1. Daftarkan semua rute
        config.add_route('home', '/')
        config.add_route('hello', '/hello/{name}') # Rute baru dengan parameter

        # 2. Pindai file .views untuk @view_config
        config.scan('.views')
        
    return config.make_wsgi_app()
```

1. config.add_route(...): Fungsi main sekarang bertanggung jawab penuh untuk mendefinisikan semua URL aplikasi dan memberi mereka nama (home, hello).
2. config.scan('.views'): Ini adalah perintah krusial. Ini memberi tahu Pyramid untuk mencari di modul tutorial.views (bentuk singkat dari .views) dan mendaftarkan view apa pun yang memiliki decorator @view_config.

### C. tutorial/tests.py (Dimodifikasi)

Tes diperbarui untuk memvalidasi rute baru.

```python
# ... fixture 'testapp' tetap sama ...

def test_home_view(testapp):
    # Tes ini sekarang memvalidasi rute 'home'
    res = testapp.get('/', status=200)
    assert res.body == b'Hello World!'

def test_hello_name_view(testapp):
    # Tes BARU untuk memvalidasi rute 'hello'
    res = testapp.get('/hello/Jane', status=200)
    assert res.body == b'Hello, Jane!'
```

## Alur Kerja (Startup & Request)

1. Alur Kerja Startup
   - pserve menjalankan fungsi main.
   - config.add_route('home', '/') mendaftarkan rute home.
   - config.add_route('hello', '/hello/{name}') mendaftarkan rute hello.
   - config.scan('.views') dieksekusi.
   - Pyramid membuka tutorial/views.py.
   - Ia menemukan home_view dan melihat @view_config(route_name='home'). Ia lalu membuat koneksi: Rute 'home' -> home_view.
   - Ia menemukan hello_view dan melihat @view_config(route_name='hello'). Ia membuat koneksi: Rute 'hello' -> hello_view.
   - Aplikasi yang dikonfigurasi lengkap dikembalikan ke waitress.

2. Alur Kerja Request (Contoh: /hello/Bob)
   - Browser mengirim permintaan ke /hello/Bob.
   - waitress meneruskannya ke Pyramid.
   - Router Pyramid mencocokkan /hello/Bob dengan pola /hello/{name} (rute hello).
   - Router membuat matchdict (kamus pencocokan) berisi {'name': 'Bob'}.
   - Pyramid memeriksa koneksi mana yang terkait dengan rute hello. (Dari startup, ia tahu ini adalah hello_view).
   - Pyramid memanggil hello_view(request), menyertakan matchdict di dalam request.
   - Di dalam view, request.matchdict['name'] mengambil nilai "Bob".
   - View mengembalikan Response('Hello, Bob!').
