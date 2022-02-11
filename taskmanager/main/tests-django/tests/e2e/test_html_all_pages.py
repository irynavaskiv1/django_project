from pytest_django.asserts import assertTemplateUsed

from ..consts import HTML_EXTENSION, PAGES


def test_html_all_pages(get_webdriver_url):
    """ test that home page returns correct html """
    SPLITED_INDEX = 1

    for page in PAGES:
        request = get_webdriver_url(page=page)
        result_html = page.split('/')[SPLITED_INDEX] + HTML_EXTENSION
        assertTemplateUsed(request, result_html)
