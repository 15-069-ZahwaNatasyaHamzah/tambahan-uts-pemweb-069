from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_chameleon')
        
        # Rute ke halaman wiki
        config.add_route('wiki', '/wiki')
        
        # PENTING: Konfigurasi aset statis untuk library Deform
        config.add_static_view('deform_static', 'deform:static')
        
        config.scan('views')
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543/wiki")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()