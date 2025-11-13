from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

# 1. View untuk Halaman Utama (HTML)
@view_config(route_name='home', renderer='home.jinja2')
def home_view(request):
    return {}

# 2. View untuk Data JSON (API)
# renderer='json' otomatis mengubah dictionary jadi format JSON
@view_config(route_name='hello_json', renderer='json')
def hello_json(request):
    return {'message': 'Halo! Ini adalah data rahasia dari Server.'}

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_jinja2')
        
        config.add_route('home', '/')
        config.add_route('hello_json', '/howdy.json') # Kita namakan URL-nya /howdy.json
        
        config.scan()
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()