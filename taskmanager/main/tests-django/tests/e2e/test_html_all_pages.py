from pytest_django.asserts import assertTemplateUsed
from selenium import webdriver

from ..consts import (EXECUTABLE_PATH, HTML_EXTENSION, POHIRTSI_SPACE_TABS_LINKS,
                      URL)


def test_html_all_pages():
    """ test that home page returns correct html"""
    pages = [POHIRTSI_SPACE_TABS_LINKS.about, POHIRTSI_SPACE_TABS_LINKS.history, POHIRTSI_SPACE_TABS_LINKS.kindergarten,
             POHIRTSI_SPACE_TABS_LINKS.school, POHIRTSI_SPACE_TABS_LINKS.lyceum, POHIRTSI_SPACE_TABS_LINKS.religion,
             POHIRTSI_SPACE_TABS_LINKS.restaurant, POHIRTSI_SPACE_TABS_LINKS.news, POHIRTSI_SPACE_TABS_LINKS.contacts]
    for page in pages:
        browser = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
        result_html = page.split('/')[1] + HTML_EXTENSION
        assertTemplateUsed(browser.get(URL + page), result_html)
