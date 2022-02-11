from pytest_django.asserts import assertTemplateUsed

from ..consts import HTML_EXTENSION, POHIRTSI_SPACE_TABS_LINKS


def test_html_all_pages(get_webdriver_url):
    """ test that home page returns correct html"""
    SPLITED_INDEX = 1

    pages = [POHIRTSI_SPACE_TABS_LINKS.about, POHIRTSI_SPACE_TABS_LINKS.history, POHIRTSI_SPACE_TABS_LINKS.kindergarten,
             POHIRTSI_SPACE_TABS_LINKS.school, POHIRTSI_SPACE_TABS_LINKS.lyceum, POHIRTSI_SPACE_TABS_LINKS.religion,
             POHIRTSI_SPACE_TABS_LINKS.restaurant, POHIRTSI_SPACE_TABS_LINKS.news, POHIRTSI_SPACE_TABS_LINKS.contacts]

    for page in pages:
        request = get_webdriver_url(page=page)
        result_html = page.split('/')[SPLITED_INDEX] + HTML_EXTENSION
        assertTemplateUsed(request, result_html)
