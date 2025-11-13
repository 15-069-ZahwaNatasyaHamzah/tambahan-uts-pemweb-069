import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
# Import modul session
from pyramid.session import SignedCookieSessionFactory

if __name__ == '__main__':
    # 1. Buat pabrik session dengan kunci rahasia
    my_session_factory = SignedCookieSessionFactory('rahasia_dapur_123')

    # Set lokasi file saat ini (biar aman)
    here = os.path.dirname(os.path.abspath(__file__))

    with Configurator() as config:
        config.include('pyramid_chameleon')
        
        # 2. Pasang session factory ke konfigurasi
        config.set_session_factory(my_session_factory)
        
        config.add_route('home', '/')
        config.scan('views')
        
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()