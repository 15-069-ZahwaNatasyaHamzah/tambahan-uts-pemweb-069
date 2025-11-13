from wsgiref.simple_server import make_server
from pyramid.config import Configurator

if __name__ == '__main__':
    with Configurator() as config:
        config.include('pyramid_chameleon')
        config.add_route('home', '/')
        config.add_route('plain', '/plain')
        config.add_route('json', '/json')
        config.scan('views')
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()