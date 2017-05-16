from django.contrib.auth.models import User
from django.test import TestCase
from . import views


user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

class TestsViews(TestCase):

    def test_index_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get("/signup/")
        self.assertEqual(response.status_code, 200)
