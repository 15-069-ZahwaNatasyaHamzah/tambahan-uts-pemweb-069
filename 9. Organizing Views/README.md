# Analisis Organizing Views With View Classes

## Tujuan Tutorial

Tujuan tutorial ini adalah untuk melakukan refactoring (perombakan) kode di views.py. Daripada memiliki banyak fungsi view yang berdiri sendiri, kita akan mengelompokkan semua view yang terkait ke dalam satu Class (Kelas) Python.
Manfaat utamanya adalah:

1. Organisasi: Kode menjadi lebih rapi karena semua view yang berhubungan (misalnya, semua view untuk "user") ada di dalam satu class.
2. Reusable Logic: Memudahkan untuk berbagi properti atau helper method di antara view di dalam class yang sama (misalnya, self.db_conn atau self.current_user).

---

## Komponen Utama Kode

Perubahan utama terjadi hanya di tutorial/views.py. File __init__.py dan tests.py tidak perlu diubah sama sekali.

### A. tutorial/views.py (Modifikasi Besar)

Semua fungsi view diubah menjadi method di dalam sebuah class baru.

```python
from pyramid.view import view_config

# 'Response' tidak lagi di-import, karena kita hanya mengembalikan dictionary
# untuk renderer

class TutorialViews:
    # 1. 'request' disuntikkan (inject) saat class dibuat
    #    dan disimpan di self.request
    def __init__(self, request):
        self.request = request

    # 2. 'home_view' diubah menjadi method 'home(self)'
    #    @view_config diletakkan di atas method
    @view_config(route_name='home', renderer='tutorial:templates/home.pt')
    def home(self):
        return {'name': 'World'}

    # 3. 'hello_view' diubah menjadi method 'hello(self)'
    @view_config(route_name='hello', renderer='tutorial:templates/hello.pt')
    def hello(self):
        # 4. 'request' sekarang diakses melalui 'self.request'
        name = self.request.matchdict['name']
        return {'name': name}
```

Perubahaan :
1. class TutorialViews: Sebuah class baru dibuat untuk menampung semua view.
2. def __init__(self, request): Kita mendefinisikan constructor (__init__) untuk class ini. Pyramid akan secara otomatis mengirimkan objek request ke constructor ini setiap kali view dipanggil. Kita menyimpannya di self.request agar bisa diakses oleh method lain.
3. def home(self) & def hello(self): Fungsi view diubah menjadi method (fungsi di dalam class). Mereka tidak lagi menerima request sebagai parameter, karena request sudah tersedia melalui self.request.
4. self.request.matchdict: Kita sekarang mengakses matchdict dari self.request yang sudah disimpan.

### B. tutorial/__init__.py (Tidak Berubah)

File main (pabrik aplikasi) tidak perlu diubah.

Perintah config.scan('.views') cukup pintar untuk memindai file views.py dan menemukan decorator @view_config baik yang ada di fungsi (seperti sebelumnya) maupun yang ada di method class (seperti sekarang).

### C. tutorial/tests.py (Tidak Berubah)

File tes juga tidak perlu diubah. Refactoring ini hanya mengubah implementasi internal view. Dari luar (dari sudut pandang webtest yang mengakses URL), aplikasi kita berperilaku identik: URL / masih mengembalikan HTML "Hello, World!" dan URL /hello/Jane masih mengembalikan "Hello, Jane!". Ini adalah tanda refactoring yang baik.

## Alur Kerja (Request dengan View Class)

Alur kerja startup (pemindaian) hampir sama, tetapi alur kerja request sedikit berbeda:
1. Pengguna membuka http://localhost:6543/hello/Bob.
2. Pyramid menerima request dan mencocokkannya dengan rute hello.
3. Pyramid melihat dari hasil scan bahwa rute hello terhubung ke method hello dari class TutorialViews.
4. Langkah Kunci: Pyramid membuat sebuah instance (objek) dari class tersebut, sambil menyuntikkan request ke constructor-nya. view_instance = TutorialViews(request)
5. Setelah instance dibuat, Pyramid memanggil method spesifik yang terkait dengan rute tersebut: result_dict = view_instance.hello()
6. Method hello berjalan, mengakses self.request.matchdict['name'] ("Bob"), dan mengembalikan dictionary {'name': 'Bob'}.
7. Pyramid melihat renderer yang terdaftar untuk view ini, mengambil dictionary tersebut, merendernya dengan template hello.pt, dan mengirimkan HTML-nya ke browser.
