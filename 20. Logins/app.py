from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

if __name__ == '__main__':
    # 1. Setup Kebijakan Keamanan
    # 'sosecret' adalah kunci rahasia untuk mengenkripsi cookie
    authn_policy = AuthTktAuthenticationPolicy('sosecret', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    with Configurator() as config:
        config.include('pyramid_chameleon')
        
        # 2. Pasang kebijakan ke konfigurasi
        config.set_authentication_policy(authn_policy)
        config.set_authorization_policy(authz_policy)
        
        config.add_route('home', '/')
        config.add_route('login', '/login')
        config.add_route('logout', '/logout')
        
        config.scan('views')
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()