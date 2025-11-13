from pyramid.view import view_config, view_defaults

# Kita buat satu Class untuk menangani semua view
class TutorialViews:
    def __init__(self, request):
        self.request = request

    # View 1: Halaman Depan
    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        return {'page_title': 'Home View'}

    # View 2: Halaman Hello
    @view_config(route_name='hello', renderer='hello.pt')
    def hello(self):
        return {'page_title': 'Hello View'}