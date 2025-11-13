from pyramid.view import view_config, view_defaults
from pyramid.response import Response

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    # Halaman Utama (HTML)
    @view_config(route_name='home')
    def home(self):
        return {'page_title': 'Home View', 'url': self.request.url}

    # Halaman Teks Polos
    @view_config(route_name='plain')
    def plain(self):
        return Response('Ini adalah teks polos (Plain Text). Tidak ada HTML disini.')

    # Halaman JSON
    @view_config(route_name='json', renderer='json')
    def json_view(self):
        return {'status': 'OK', 'message': 'Ini adalah format JSON', 'code': 200}