from pytest_django.asserts import assertTemplateUsed
from selenium import webdriver

from consts import EXECUTABLE_PATH, POHIRTSI_SPACE_TABS_HTML, URL


def test_html_main():
    """ test that home page returns correct html"""
    browser = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
    assertTemplateUsed(browser.get(URL), POHIRTSI_SPACE_TABS_HTML.about)
