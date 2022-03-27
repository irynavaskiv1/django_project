from pytest_django.asserts import assertTemplateUsed

from ..consts import HTML_EXTENSION, PAGES


def test_html_all_pages(get_webdriver_url):
    """
    @ID: 001
    @Category: e2e
    @Description: Test that all pages return correct html
    @tcmethod: automated

    Steps:
        1. Get urls for each page

    Expected:
        1. All pages return correct HTML
    """

    SPLITED_INDEX = 1

    for page in PAGES:
        request = get_webdriver_url(page=page)
        result_html = page.split('/')[SPLITED_INDEX] + HTML_EXTENSION
        assertTemplateUsed(request, result_html)
