# Analisis *Pyramid Quick Tutorial - Hello World*

## Tujuan Tutorial 

Tujuan dari tutorial "Hello World" ini adalah untuk mendemonstrasikan konsep inti dan komponen minimal yang diperlukan untuk membuat aplikasi web yang berfungsi menggunakan framework Pyramid. Ini menunjukkan bagaimana Pyramid dapat memulai dari satu file Python sederhana tanpa memaksakan struktur direktori yang kompleks.

---

## 1. Komponen Utama Kode

Kode *Hello World* ini memperkenalkan **3 pilar utama Pyramid**:

---

### A. View Callable (Fungsi Logika)

```python
from pyramid.response import Response

def hello_world(request):
    return Response('Hello World!')
```
1. Sebuah view dalam Pyramid pada dasarnya adalah fungsi Python biasa (def hello_world).
2. Ia wajib menerima parameter request, yang berisi semua informasi tentang permintaan HTTP yang masuk dari browser.
3. Ia wajib mengembalikan sebuah objek Response. Di sini, pyramid.response.Response digunakan untuk mengirim respons HTTP paling sederhana: teks "Hello World!" dengan status "200 OK".

### B. Configurator (Konfigurasi dan Peta Rute)

```Python
from pyramid.config import Configurator

with Configurator() as config:
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
```
1. Configurator() adalah objek utama tempat semua pengaturan aplikasi didaftarkan.
2. config.add_route('hello', '/'): Ini adalah pendaftaran rute. Kita memberi tahu Pyramid: "Jika ada permintaan masuk ke URL root (/), berikan nama internal 'hello' pada rute ini."
3. config.add_view(hello_world, route_name='hello'): Ini adalah penghubung (mapper). Kita memberi tahu Pyramid: "Jika rute bernama 'hello' cocok, jalankan fungsi hello_world."
4. config.make_wsgi_app(): Ini adalah langkah terakhir konfigurasi. Pyramid mengambil semua rute dan view yang telah didaftarkan dan merakitnya menjadi satu aplikasi WSGI yang standar.

### C. Server (Eksekutor Aplikasi)

```Python
from wsgiref.simple_server import make_server

if __name__ == '__main__':
    # ... (kode configurator) ...
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
```
1. wsgiref.simple_server adalah server web bawaan Python. Ini hanya untuk pengembangan (development), bukan untuk produksi (production).
2. make_server(...) menginstruksikan server untuk berjalan di semua alamat IP (0.0.0.0) pada port 6543, dan memberinya aplikasi app (yang kita buat di langkah B) untuk dijalankan.
3. server.serve_forever() memulai server untuk terus berjalan dan mendengarkan permintaan.

## Alur Kerja (Request Lifecycle)
1. Analisis alur kerja dari kode di atas adalah sebagai berikut:
2. Pengguna membuka http://localhost:6543/ di browser.
3. Server (wsgiref) menerima permintaan untuk URL /.
4. Server meneruskan permintaan ke aplikasi WSGI Pyramid (app).
5. Pyramid (via Configurator) memeriksa tabel rutenya.
6. URL / cocok dengan rute yang dinamai hello.
7. Pyramid memeriksa view mana yang terhubung ke rute hello.
8. Pyramid menemukan bahwa view hello_world terhubung ke rute tersebut.
9.Pyramid menjalankan fungsi hello_world(request).
10. Fungsi mengembalikan objek Response('Hello World!').
11. Pyramid mengirimkan respons tersebut kembali ke browser.
