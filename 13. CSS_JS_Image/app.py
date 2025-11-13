import os  
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

@view_config(route_name='home', renderer='home.jinja2')
def home(request):
    return {}

if __name__ == '__main__':

    here = os.path.dirname(os.path.abspath(__file__))

    with Configurator() as config:
        config.include('pyramid_jinja2')
        
        config.add_static_view(name='static', path=os.path.join(here, 'static'))
        
        config.add_route('home', '/')
        config.scan()
        
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()