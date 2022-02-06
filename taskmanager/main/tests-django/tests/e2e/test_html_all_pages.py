from pytest_django.asserts import assertTemplateUsed
from selenium import webdriver


def test_html_all_pages():
    """ test that home page returns correct html"""
    executable_path = '/Users/admin/Documents/django_project/taskmanager/main/tests-django/drivers/chromedriver'
    url = 'http://www.pohirtsi.space'
    pages = ['/history', '/kindergarten', '/school', '/lyceum', '/religion', '/restaurant', '/contacts']
    for page in pages:
        browser = webdriver.Chrome(executable_path=executable_path)
        responce = browser.get(url + page)
        result_html = page.split('/')[1] + '.html'
        assertTemplateUsed(responce, result_html)
