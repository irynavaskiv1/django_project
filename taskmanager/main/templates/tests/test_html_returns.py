from django.test import TestCase


class AboutTest(TestCase):

    def test_pages_returns(self):
        """
        test that home page returns correct html
        """
        responce = self.content.get('http://www.pohirtsi.space/')
        self.assertTemplateUsed(responce, 'about.html')

