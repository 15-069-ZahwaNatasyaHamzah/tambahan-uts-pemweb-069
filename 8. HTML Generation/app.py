from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

# @view_config adalah cara praktis menghubungkan kode ini dengan file template
@view_config(route_name='home', renderer='home.pt')
def tutorial_view(request):
    # Kita cuma kirim datanya saja, HTML-nya urusan home.pt
    return {'name': 'Zahwa'}

if __name__ == '__main__':
    with Configurator() as config:
        # PENTING: Aktifkan library templating
        config.include('pyramid_chameleon')
        
        config.add_route('home', '/')
        
        # Scan otomatis untuk menemukan @view_config di atas
        config.scan()
        
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()