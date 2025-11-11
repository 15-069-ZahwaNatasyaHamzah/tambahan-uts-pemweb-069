# Analisis HTML Generation With Templating

## Tujuan Tutorial

Tujuan tutorial ini adalah untuk berhenti mengembalikan teks mentah (plain text) dari view kita. Sebaliknya, kita akan menggunakan sistem template (pyramid_chameleon) untuk merender file HTML yang dinamis.

View kita tidak lagi bertanggung jawab membuat HTML. Sebaliknya, view hanya akan menyiapkan data (sebagai dictionary Python), dan meneruskannya ke renderer template untuk dibuatkan HTML-nya.

---

## Komponen Utama Kode

Tutorial ini memperkenalkan dependensi baru, file template baru, dan mengubah cara kerja view kita secara fundamental.

### A. setup.py (Menambah Dependensi)

Kita perlu memberi tahu Python bahwa proyek kita sekarang memiliki dependensi runtime baru untuk menangani templating.

```python
# Dependensi utama SEKARANG TERMASUK pyramid_chameleon
requires = [
    'pyramid',
    'pyramid_chameleon', # <-- DITAMBAHKAN
    'waitress',
]
```

pyramid_chameleon: Ditambahkan ke daftar requires utama, karena ini adalah bagian inti dari aplikasi kita, bukan hanya alat development.

### B. tutorial/__init__.py (Mengaktifkan Engine)

Kita perlu memberi tahu Configurator Pyramid untuk memuat dan mengaktifkan add-on templating saat startup.

```python
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        # 1. Aktifkan pyramid_chameleon
        config.include('pyramid_chameleon') # <-- DITAMBAHKAN
        
        # 2. Daftarkan rute (tidak berubah)
        config.add_route('home', '/')
        config.add_route('hello', '/hello/{name}')

        # 3. Pindai view (tidak berubah)
        config.scan('.views')
        
    return config.make_wsgi_app()
```

config.include('pyramid_chameleon'): Memerintahkan Pyramid untuk menginisialisasi renderer template Chameleon.

### C. tutorial/templates/hello.pt (File Template BARU)

Kita membuat direktori baru (templates) dan file HTML di dalamnya. Ini adalah template Chameleon (file .pt).

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hello App</title>
</head>
<body>
    <h1>Hello, ${name}!</h1>
</body>
</html>
```

1. tutorial/templates/: Lokasi standar untuk menyimpan template.
2. ${name}: Ini adalah sintaks Chameleon untuk "substitusi variabel". Ia akan mencari key bernama name dari dictionary yang diberikan oleh view.

### D. tutorial/views.py (Modifikasi Besar)

Perubahan paling signifikan terjadi di sini. View tidak lagi mengembalikan Response!

```python
from pyramid.view import view_config

# --- View 1: home_view ---
# 'renderer' memberitahu Pyramid untuk menggunakan template
@view_config(route_name='home', renderer='tutorial:templates/home.pt')
def home_view(request):
    # View HANYA MENGEMBALIKAN DICTIONARY
    return {'name': 'World'} 

# --- View 2: hello_view ---
@view_config(route_name='hello', renderer='tutorial:templates/hello.pt')
def hello_view(request):
    name = request.matchdict['name']
    # View HANYA MENGEMBALIKAN DICTIONARY
    return {'name': name}
```

1. renderer='...': Argumen baru ini ditambahkan ke @view_config. tutorial:templates/hello.pt adalah asset specification yang menunjuk ke file template yang kita buat.
2. return {'name': ...}: Ini adalah perubahan inti. View sekarang mengembalikan dictionary Python. Pyramid akan mengambil dictionary ini dan meneruskannya ke renderer yang ditentukan.

### E. tutorial/tests.py (Dimodifikasi)

Tes sekarang harus memeriksa body HTML yang lengkap, bukan hanya teks mentah.

```python
# ... fixture 'testapp' tetap sama ...

def test_home_view(testapp):
    res = testapp.get('/', status=200)
    # Validasi bahwa HTML yang dirender berisi tag <h1> yang benar
    assert b'<h1>Hello, World!</h1>' in res.body

def test_hello_name_view(testapp):
    res = testapp.get('/hello/Jane', status=200)
    # Validasi bahwa HTML yang dirender berisi nama dinamis
    assert b'<h1>Hello, Jane!</h1>' in res.body
```

## Alur Kerja (Alur Request dengan Renderer)

1. Pengguna membuka http://localhost:6543/hello/Bob.
2. Pyramid mencocokkan rute hello dan menemukan hello_view.
3. Pyramid memanggil hello_view(request).
4. hello_view berjalan dan mengembalikan dictionary Python: {'name': 'Bob'}.
5. Pyramid melihat bahwa @view_config untuk view ini memiliki argumen renderer='tutorial:templates/hello.pt'.
6. Pyramid tidak mengirimkan dictionary itu ke browser. Sebaliknya..
7. Pyramid memuat file hello.pt
8. Ia memberikan dictionary {'name': 'Bob'} ke renderer Chameleon
9. Chameleon memproses template, mengganti ${name} dengan "Bob"
10. Renderer menghasilkan string HTML yang lengkap
11. Pyramid mengambil HTML yang sudah jadi itu, membungkusnya dalam objek Response (dengan Content-Type: text/html), dan mengirimkannya ke browser.
