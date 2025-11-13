from pyramid.view import view_config, view_defaults
from pyramid.response import Response

@view_defaults(renderer='json')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    # 1. Rute Utama
    @view_config(route_name='home')
    def home(self):
        return {'info': 'Silakan coba akses /howdy/NamaDepan/NamaBelakang'}

    # 2. Rute Dinamis (Menangkap parameter)
    @view_config(route_name='hello')
    def hello(self):
        # Mengambil data dari URL ({first} dan {last})
        first_name = self.request.matchdict['first']
        last_name = self.request.matchdict['last']
        
        return {
            'greeting': 'Hello',
            'first_name': first_name,
            'last_name': last_name
        }