from django.test import TestCase

class NegativeTest(TestCase):
    def test_get_login_disallowed(self):
        res = self.client.get('/api/v1/auth/sign-in')
        self.assertEqual(res.status_code, 405)
