from django.test import TestCase
from django.contrib.auth.models import User

class LoginAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', password='pass123!')

    def test_login_success(self):
        res = self.client.post('/api/v1/auth/sign-in', data={'username': 'user', 'password': 'pass123!'}, content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_login_fail(self):
        res = self.client.post('/api/v1/auth/sign-in', data={'username': 'user', 'password': 'salah'}, content_type='application/json')
        self.assertEqual(res.status_code, 401)
