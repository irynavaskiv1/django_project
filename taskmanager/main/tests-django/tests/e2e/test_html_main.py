from pytest_django.asserts import assertTemplateUsed

from ..consts import POHIRTSI_SPACE_TABS_HTML


def test_html_main(get_webdriver_url):
    """
    @ID: 002
    @Category: e2e
    @Description: Test that home page returns correct html
    @tcmethod: automated

    Steps:
        1. Get url for home page

    Expected:
        1. Home page returns correct HTML
    """
    EMPTY_SRT = ''

    request = get_webdriver_url(page=EMPTY_SRT)
    assertTemplateUsed(request, POHIRTSI_SPACE_TABS_HTML.about)
