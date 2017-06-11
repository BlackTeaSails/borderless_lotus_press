from django.contrib.auth.models import User
from django.test import TestCase
from . import views


class TestsViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    def test_login_view(self):
        response = self.client.get("/auth/login/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get("/auth/signup/")
        self.assertEqual(response.status_code, 200)

    def test_recovery_view(self):
        response = self.client.get("/auth/recovery/")
        self.assertEqual(response.status_code, 200)

    def test_profile_page(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get('/auth/profile/', follow=True)
        user = User.objects.get(username='john')
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)
