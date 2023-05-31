from django.test import TestCase

class PrimerTestCase(TestCase):
    def test_say_shit(self):
        response = self.client.get('/say_shit/')
        self.assertEqual(response.status_code, 200) # 200 OK
        self.assertIn('shits', str(response.content))