from pyramid.debugtoolbar.panels import DebugPanel

_ = lambda x: x 

class HelloDebugPanel(DebugPanel):
    name = 'hello'
    has_content = True

    def __init__(self, request):
        self.data = {
            'name': request.registry.settings.get('hello.name')
        }

    def nav_title(self):
        return _('Hello')

    def title(self):
        return _('Hello')

    def url(self):
        return ''

    def content(self):
        return 'Hello, %(name)s' % self.data

def includeme(config):
    config.add_debugtoolbar_panel(HelloDebugPanel)