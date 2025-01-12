from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page(self):
        url = reverse('home_page')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')