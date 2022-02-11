from pytest_django.asserts import assertTemplateUsed

from ..consts import POHIRTSI_SPACE_TABS_HTML


def test_html_main(get_webdriver_url):
    """ test that home page returns correct html"""
    EMPTY_SRT = ''

    request = get_webdriver_url(page=EMPTY_SRT)
    assertTemplateUsed(request, POHIRTSI_SPACE_TABS_HTML.about)
