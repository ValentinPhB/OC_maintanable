import pytest
from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.mark.django_db
class TestProfilesIndexPage(TestCase):
    path = reverse('profiles:index')
    client = Client()
    title_expected = '<title>Profiles</title>'

    def test_url_profiles_index(self):
        self.assertEqual(self.path, '/profiles/')
        self.assertEqual(resolve(self.path).view_name, 'profile:index')

    def test_title_view_profiles_index(self):
        response = self.client.get(self.path)

        self.assertContains(response, self.title_expected, status_code=200)


@pytest.mark.django_db
class TestProfilesElementPage(TestCase):
    client = Client()
    path = reverse('profiles:profile', kwargs={'username': 'ElementTestProfile'})
    title_expected = '<title>ElementTestProfile</title>'

    def setUp(self):
        user_1 = User.objects.create(username='ElementTestProfile', password='12345678AA')
        Profile.objects.create(user=user_1, favorite_city='')

    def test_title_view_profiles_element(self):
        response = self.client.get(self.path)

        self.assertContains(response, self.title_expected, status_code=200)
