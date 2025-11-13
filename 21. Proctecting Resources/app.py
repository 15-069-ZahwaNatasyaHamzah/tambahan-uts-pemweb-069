from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, Everyone

# 1. Membuat Aturan Keamanan (ACL / Satpam)
class RootFactory(object):
    __acl__ = [
        (Allow, Everyone, 'view'),       # Semua orang boleh 'view' (lihat)
        (Allow, 'editor', 'edit'),       # HANYA user 'editor' yang boleh 'edit'
    ]

    def __init__(self, request):
        pass

if __name__ == '__main__':
    # 2. Setup Kebijakan (Sama seperti No 20)
    authn_policy = AuthTktAuthenticationPolicy('kunci_rahasia', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    with Configurator() as config:
        config.include('pyramid_chameleon')
        
        config.set_authentication_policy(authn_policy)
        config.set_authorization_policy(authz_policy)
        
        # 3. PENTING: Aktifkan Satpam (RootFactory)
        config.set_root_factory(RootFactory)
        
        config.add_route('home', '/')
        config.add_route('hello', '/hello') # Ini nanti jadi halaman rahasia
        config.add_route('login', '/login')
        config.add_route('logout', '/logout')
        
        config.scan('views')
        app = config.make_wsgi_app()
    
    print("Server berjalan di http://localhost:6543")
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()