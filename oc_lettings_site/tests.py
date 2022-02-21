import pytest

from django.test import Client, TestCase
from django.urls import reverse, resolve


@pytest.mark.django_db
class TestHomeIndexPage(TestCase):
    path = reverse('index')
    client = Client()
    title_expected = '<title>Holiday Homes</title>'

    def test_url_home(self):
        self.assertEqual(self.path, '/')
        self.assertEqual(resolve(self.path).view_name, 'index')

    def test_title_view_home(self):
        response = self.client.get(self.path)

        self.assertContains(response, self.title_expected, status_code=200)
