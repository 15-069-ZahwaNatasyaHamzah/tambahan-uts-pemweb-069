from pyramid.view import view_config, forbidden_view_config
from pyramid.security import remember, forget
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

# Database User Sederhana (Username: Password)
# Di dunia nyata, ini harusnya di database terenkripsi
USERS = {'editor': 'editor', 'viewer': 'viewer'}

class TutorialViews:
    def __init__(self, request):
        self.request = request
        # Cek apakah user sedang login?
        self.logged_in = request.authenticated_userid

    # 1. Halaman Home
    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        return {'name': 'Home View', 'logged_in': self.logged_in}

    # 2. Halaman Login
    @view_config(route_name='login', renderer='login.pt')
    def login(self):
        message = ''
        login = ''
        
        if 'form.submitted' in self.request.params:
            login = self.request.params['login']
            password = self.request.params['password']
            
            # Cek apakah username dan password benar?
            if USERS.get(login) == password:
                # SUKSES: Buat cookie "Ingat Saya"
                headers = remember(self.request, login)
                # Redirect ke halaman home
                return HTTPFound(location='/', headers=headers)
            
            message = 'Gagal Login! Username/Password salah.'

        return {
            'message': message,
            'url': self.request.route_url('login'),
            'login': login,
            'logged_in': self.logged_in
        }

    # 3. Halaman Logout
    @view_config(route_name='logout')
    def logout(self):
        # Hapus cookie
        headers = forget(self.request)
        # Redirect ke home
        return HTTPFound(location='/', headers=headers)