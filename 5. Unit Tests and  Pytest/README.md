# Analisis Unit Tests and pytest

## Tujuan Tutorial

Tujuan tutorial ini adalah untuk memperkenalkan unit testing pada aplikasi Pyramid. Tutorial ini menunjukkan dua pendekatan pengujian yang berbeda menggunakan framework pytest:
1. True Unit Test: Menguji view callable (hello_world) sebagai fungsi Python murni, terisolasi dari framework Pyramid, dengan menggunakan "request palsu" (DummyRequest).
2. Integration-style Test: Menguji view melalui framework Pyramid, di mana kita memuat konfigurasi aplikasi dan mengirim permintaan HTTP palsu ke URL (/) menggunakan library webtest

---

## Komponen Utama Kode

Tutorial ini menambahkan satu file baru (tutorial/tests.py) dan memperbarui setup.py untuk menambahkan dependensi testing.

### A. setup.py (Menambah Dependensi Test)

Kita perlu mendaftarkan pytest (test runner) dan webtest (untuk simulasi request HTTP) sebagai dependensi khusus untuk testing.

```python
# ... (kode requires dan dev_requires) ...

# Dependensi BARU khusus untuk testing
tests_require = [
    'pytest',
    'webtest',
]

setup(
    name='tutorial',
    # ...
    extras_require={
        'dev': dev_requires,
        'test': tests_require, # Mendaftarkan grup 'test'
    },
    # ...
)
```

1. tests_require: Mendefinisikan library yang hanya dibutuhkan saat menjalankan tes.
2. extras_require: Mendaftarkan grup ini agar kita bisa menginstalnya menggunakan perintah pip install -e ".[test]".

### B. tutorial/tests.py (File Test BARU)

File ini berisi semua fungsi tes kita. pytest akan secara otomatis menemukannya.

```python
from pyramid import testing

# --- Test Metode 1: True Unit Test (Menguji Fungsi) ---

def test_default_view():
    # Import view yang ingin kita tes
    from . import hello_world 

    # 1. Setup: Buat request palsu (dummy)
    request = testing.DummyRequest()

    # 2. Eksekusi: Panggil view-nya secara langsung
    response = hello_world(request)

    # 3. Validasi: Pastikan teks respons-nya benar
    assert response.text == 'Hello World!'


# --- Test Metode 2: Integration-style Test (Menguji Framework) ---

def test_hello_view():
    # Import 'main' factory dan 'webtest'
    from . import main
    from webtest import TestApp

    # 1. Setup: Buat aplikasi WSGI di memori
    settings = {}
    app = main({}, **settings)
    testapp = TestApp(app) # Bungkus app dengan TestApp

    # 2. Eksekusi: Kirim request HTTP palsu ke URL '/'
    #    Kita juga cek status 200 OK
    res = testapp.get('/', status=200)

    # 3. Validasi: Pastikan body respons-nya benar
    assert res.body == b'Hello World!'
```


1. test_default_view: Metode ini tidak peduli dengan rute atau konfigurasi. Ia hanya mengimpor fungsi hello_world dan mengujinya secara terisolasi. testing.DummyRequest() menyediakan objek request minimal agar fungsi tersebut bisa berjalan.
2. test_hello_view: Metode ini menguji keseluruhan alur Pyramid. Ia memanggil main untuk membuat aplikasi, lalu menggunakan TestApp dari webtest untuk "membuka" URL /. Tes ini memvalidasi bahwa rute / terhubung dengan benar ke view yang mengembalikan Hello World!.

## Alur Kerja (Menjalankan Test)

1. Pengguna menginstal dependensi testing (cukup sekali) dengan: pip install -e ".[test]"
2. Pengguna menjalankan test runner pytest dari direktori root proyek: pytest
3. pytest secara otomatis memindai (scan) direktori untuk mencari file bernama test_*.py atau *_test.py.
4. Ia menemukan tutorial/tests.py.
5. Ia menemukan fungsi-fungsi di dalamnya yang diawali dengan test_ (yaitu test_default_view dan test_hello_view).
6. pytest menjalankan kedua fungsi tersebut.Di dalam test_default_view, assert info.text == 'Hello World!' dievaluasi.
7. Di dalam test_hello_view, assert res.body == b'Hello World!' dievalua
8. Jika semua assert lolos (bernilai True), pytest akan melaporkan "PASSED". Jika ada yang gagal, ia akan melaporkan "FAILED" dengan detail error-nya.
