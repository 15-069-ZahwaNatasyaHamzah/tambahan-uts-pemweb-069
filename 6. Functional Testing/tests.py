import unittest

class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from functional_test import hello_world
        from pyramid.config import Configurator
        
        # Setup aplikasi dummy untuk dites
        with Configurator() as config:
            config.add_route('hello', '/')
            config.add_view(hello_world, route_name='hello')
            self.app = config.make_wsgi_app()

    def test_root(self):
        from webtest import TestApp
        # Membuat browser simulasi
        testapp = TestApp(self.app)
        
        # Coba akses alamat root '/'
        res = testapp.get('/')
        
        # Cek apakah status OK (200) dan tulisan sesuai
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Hello World!', res.body)