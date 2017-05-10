from django.test import TestCase
from . import views

class MyTests(TestCase):

    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
