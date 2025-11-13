from pyramid.view import view_config
from models import Page, DBSession
import transaction

class DatabaseViews:
    def __init__(self, request):
        self.request = request

    # View 1: Halaman Depan (Menampilkan semua data)
    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        # Query: Ambil semua data dari tabel Page
        pages = DBSession.query(Page).all()
        return {'pages': pages}

    # View 2: Tambah Data Dummy
    @view_config(route_name='add_page', renderer='string')
    def add_page(self):
        # Membuat objek baru
        new_page = Page(title="Belajar Pyramid", body="SQLAlchemy itu keren!")
        
        # Masukkan ke database
        DBSession.add(new_page)
        
        # Karena pakai pyramid_tm, kita tidak perlu 'commit()' manual.
        # Otomatis disimpan saat request selesai.
        return "Berhasil menambahkan data! Silakan kembali ke Home."