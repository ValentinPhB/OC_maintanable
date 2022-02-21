import pytest

from django.test import Client, TestCase
from django.urls import reverse, resolve

from lettings.models import Letting
from oc_lettings_site.models import Address


@pytest.mark.django_db
class TestLettingsIndexPage(TestCase):
    path = reverse('lettings:index')
    client = Client()
    title_expected = '<title>Lettings</title>'

    def test_url_lettings_index(self):
        self.assertEqual(self.path, '/lettings/')
        self.assertEqual(resolve(self.path).view_name, 'letting:index')

    def test_title_view_lettings_index(self):
        response = self.client.get(self.path)

        self.assertContains(response, self.title_expected)


@pytest.mark.django_db
class TestLettingsElementPage(TestCase):
    client = Client()
    path = reverse('lettings:letting', kwargs={'letting_id': 1})
    title_expected = '<title>ELEMENT TEST LETTINGS</title>'

    def setUp(self):
        address_1 = Address.objects.create(number=1, street='TEST', city='TEST',
                                           state='FR', zip_code=1, country_iso_code='111')
        Letting.objects.create(title='ELEMENT TEST LETTINGS', address=address_1)

    def test_title_view_lettings_element(self):
        response = self.client.get(self.path)

        self.assertContains(response, self.title_expected)
