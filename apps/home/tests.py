from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')
    def test_get(self):
        """GET/ must return status code 200"""

        self.assertEqual(200, self.response.status_code)
        #self.assertTemplateUsed(response, 'Home.html , top_bar.html, footer.html')
