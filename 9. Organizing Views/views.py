from pyramid.view import view_config, view_defaults

# @view_defaults: Settingan "borongan". 
# Semua fungsi di bawah ini otomatis pakai template 'home.pt'
@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    # View 1: Halaman Home (/)
    @view_config(route_name='home')
    def home(self):
        return {'name': 'Home View'}

    # View 2: Halaman Hello (/hello)
    @view_config(route_name='hello')
    def hello(self):
        return {'name': 'Hello View'}