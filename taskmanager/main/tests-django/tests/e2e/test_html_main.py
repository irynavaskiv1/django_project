from pytest_django.asserts import assertTemplateUsed
from selenium import webdriver


def test_html_main():
    """ test that home page returns correct html"""
    executable_path = '/Users/admin/Documents/django_project/taskmanager/main/tests-django/drivers/chromedriver'
    url = 'http://www.pohirtsi.space/'
    browser = webdriver.Chrome(executable_path=executable_path)
    responce = browser.get(url)
    assertTemplateUsed(responce, 'about.html')
