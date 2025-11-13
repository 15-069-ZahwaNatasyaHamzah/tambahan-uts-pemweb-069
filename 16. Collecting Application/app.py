import logging
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# 1. Siapkan pencatat (Logger)
log = logging.getLogger(__name__)

def home(request):
    # 2. Ini cara mencatat pesan ke terminal
    log.info("Seseorang baru saja membuka halaman HOME!")
    log.warning("Ini adalah contoh pesan peringatan (Warning).")
    
    return Response('Cek terminal kamu (Layar Hitam), ada log yang tercatat disana.')

if __name__ == '__main__':
    # 3. Konfigurasi dasar agar Log muncul di layar
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    with Configurator() as config:
        config.add_route('home', '/')
        config.add_view(home, route_name='home')
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()