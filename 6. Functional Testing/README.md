# Analisis Functional Testing with WebTest

## Tujuan tutorial
Tujuan tutorial ini adalah untuk meningkatkan (refactor) integration-style test kita dari tutorial sebelumnya menjadi functional test yang lebih bersih dan efisien.

Perbedaan utamanya adalah reusabilitas. Daripada setiap fungsi tes harus membuat ulang aplikasi (TestApp) berulang kali, kita akan menggunakan pytest.fixture untuk membuat aplikasi satu kali saja dan menyuntikkannya (inject) ke setiap tes yang membutuhkannya.

---

## Komponen Utama Kode

Tutorial ini hanya memodifikasi satu file yang sudah ada. Tidak ada dependensi baru yang perlu ditambahkan di setup.py karena webtest sudah diinstal dari tutorial sebelumnya.

### A. tutorial/tests.py (Modifikasi File Test)

Kita merombak file tes kita untuk memperkenalkan fixture dan menyederhanakan fungsi tes yang ada.

```python
import pytest
from pyramid import testing
from webtest import TestApp

# --- Fixture (BARU) ---
# Ini adalah 'pabrik' untuk aplikasi tes kita
@pytest.fixture
def testapp():
    # 1. Setup: Import 'main' dan buat aplikasi WSGI
    from . import main
    settings = {}
    app = main({}, **settings)
    
    # 2. Bungkus dengan TestApp dan 'yield' (kirim) ke fungsi tes
    yield TestApp(app)
    
    # 3. (Teardown: bisa ditambahkan kode pembersihan di sini jika perlu)


# --- Test Metode 1: True Unit Test (Tidak berubah) ---

def test_default_view():
    from . import hello_world
    request = testing.DummyRequest()
    response = hello_world(request)
    assert response.text == 'Hello World!'


# --- Test Metode 2: Functional Test (DIMODIFIKASI) ---

def test_hello_view(testapp): # Minta 'testapp' fixture
    # 1. Setup: SUDAH HILANG (dikerjakan oleh fixture)
    
    # 2. Eksekusi: Langsung gunakan 'testapp'
    res = testapp.get('/', status=200)

    # 3. Validasi:
    assert res.body == b'Hello World!'
```

1. @pytest.fixture: Dekorator ini memberi tahu pytest bahwa fungsi testapp() adalah sebuah fixture (penyedia setup).
2. def testapp(): Fungsi ini berisi kode setup yang sebelumnya ada di dalam test_hello_view. Ia membuat TestApp dan memberikannya menggunakan kata kunci yield.
3. def test_hello_view(testapp): Fungsi tes ini sekarang menerima testapp sebagai parameter. pytest melihat nama parameter ini, mencocokkannya dengan fixture testapp(), dan secara otomatis menjalankan fixture tersebut terlebih dahulu, lalu menyuntikkan hasilnya ke dalam parameter testapp.
4. Kode yang Dihapus: Semua baris setup (import main, membuat app, membuat TestApp) telah dihapus dari test_hello_view, membuatnya jauh lebih bersih dan fokus pada logikanya saja.

## Alur Kerja (Eksekusi Test dengan Fixture)

1. Pengguna menjalankan pytest.
2. pytest menemukan test_hello_view dan melihat bahwa ia membutuhkan parameter bernama testapp.
3. pytest mencari fixture bernama testapp dan menemukannya (@pytest.fixture def testapp()).
4. pytest menjalankan fungsi testapp() terlebih dahulu.
5. Fungsi testapp() membuat dan yield objek TestApp.
6. pytest mengambil objek TestApp tersebut dan menyuntikkannya sebagai argumen ke test_hello_view.
7. test_hello_view(testapp) sekarang berjalan dengan testapp yang sudah siap pakai.
8. Fungsi tes test_default_view juga berjalan (ia tidak meminta fixture, jadi ia dieksekusi seperti biasa).
9. pytest melaporkan hasil "PASSED" untuk kedua tes.
