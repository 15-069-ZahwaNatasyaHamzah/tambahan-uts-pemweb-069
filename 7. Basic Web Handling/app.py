from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# --- VIEW FUNCTIONS (Tampilan) ---
# Fungsi ini menangani halaman utama
def hello_world(request):
    return Response('<body><h1>Hello World!</h1><p>Ini halaman depan.</p></body>')

# Fungsi ini menangani halaman profil
def hello_profile(request):
    return Response('<body><h1>Halaman Profil</h1><p>Ini adalah profil user.</p></body>')

# --- KONFIGURASI SERVER ---
if __name__ == '__main__':
    with Configurator() as config:
        # 1. Daftarkan nama rutenya (URL)
        config.add_route('home', '/')
        config.add_route('profile', '/profile')
        
        # 2. Hubungkan rute ke fungsi View
        config.add_view(hello_world, route_name='home')
        config.add_view(hello_profile, route_name='profile')
        
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()