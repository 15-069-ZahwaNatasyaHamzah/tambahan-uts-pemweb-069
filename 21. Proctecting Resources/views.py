from pyramid.view import view_config, forbidden_view_config
from pyramid.security import remember, forget
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

# Database User (Ada 2 role: editor & viewer)
USERS = {'editor': 'editor', 'viewer': 'viewer'}

class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        return {'name': 'Home View', 'logged_in': self.logged_in}

    # --- HALAMAN RAHASIA (VIP) ---
    # permission='edit' artinya HANYA user yang punya izin 'edit' yang boleh masuk
    @view_config(route_name='hello', renderer='hello.pt', permission='edit')
    def hello(self):
        return {'name': 'Halaman Rahasia'}

    # --- Login & Logout ---
    @view_config(route_name='login', renderer='login.pt')
    def login(self):
        message = ''
        login = ''
        if 'form.submitted' in self.request.params:
            login = self.request.params['login']
            password = self.request.params['password']
            if USERS.get(login) == password:
                headers = remember(self.request, login)
                return HTTPFound(location='/', headers=headers)
            message = 'Gagal Login!'

        return dict(message=message, url=self.request.route_url('login'), login=login, logged_in=self.logged_in)

    @view_config(route_name='logout')
    def logout(self):
        headers = forget(self.request)
        return HTTPFound(location='/', headers=headers)

    # Jika user ditolak (Forbidden), otomatis lempar ke halaman login
    @forbidden_view_config()
    def forbidden_view(self):
        return HTTPFound(location='/login')