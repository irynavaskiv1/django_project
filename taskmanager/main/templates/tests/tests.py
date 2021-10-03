from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from taskmanager.main.templates.main import about


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        request = HttpRequest()
        responce = about(request)
        html = responce.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
