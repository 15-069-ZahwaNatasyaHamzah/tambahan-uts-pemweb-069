from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

# Perhatikan: renderer sekarang mengarah ke file .jinja2
@view_config(route_name='home', renderer='home.jinja2')
def home_view(request):
    # Kita kirim dua data: name dan framework
    return {'name': 'Zahwa', 'framework': 'Jinja2'}

if __name__ == '__main__':
    with Configurator() as config:
        # PENTING: Aktifkan library Jinja2
        config.include('pyramid_jinja2')
        
        config.add_route('home', '/')
        config.scan()
        
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()