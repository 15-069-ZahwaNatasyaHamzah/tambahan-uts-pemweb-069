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

### A. Configurator (Konfigurasi dan Peta Rute)

```Python
from pyramid.config import Configurator
# ...
with Configurator() as config:
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
```
