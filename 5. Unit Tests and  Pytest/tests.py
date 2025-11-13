import unittest

from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_hello_world(self):
        from unit_testing import hello_world

        request = testing.DummyRequest()
        response = hello_world(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.body, b'Hello World!')

class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from unit_testing import hello_world
        with testing.setUp() as config:
            config.add_route('hello', '/')
            config.add_view(hello_world, route_name='hello')
            self.app = config.make_wsgi_app()

    def test_hello_world(self):
        from webtest import TestApp
        testapp = TestApp(self.app)
        res = testapp.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.body, b'Hello World!')