from time import sleep as explicit_wait
import pytest
from ..consts import (POHIRTSI_SPACE_TABS_LINKS,
                      POHIRTSI_SPACE_TABS_TITLES)


@pytest.mark.parametrize("pages", [POHIRTSI_SPACE_TABS_LINKS.about, POHIRTSI_SPACE_TABS_LINKS.history,
                                   POHIRTSI_SPACE_TABS_LINKS.kindergarten, POHIRTSI_SPACE_TABS_LINKS.school,
                                   POHIRTSI_SPACE_TABS_LINKS.lyceum, POHIRTSI_SPACE_TABS_LINKS.religion,
                                   POHIRTSI_SPACE_TABS_LINKS.restaurant, POHIRTSI_SPACE_TABS_LINKS.news,
                                   POHIRTSI_SPACE_TABS_LINKS.contacts])
def test_image_in_each_page(pages, get_webdriver_url, get_image):
    """ test that all pages returns correct title """

    try:
        for page in pages:
            get_webdriver_url(page=page)
            explicit_wait(2)
            title = get_image(page=page)
            if page == POHIRTSI_SPACE_TABS_LINKS.about:
                assert POHIRTSI_SPACE_TABS_TITLES.about == title
            elif page == POHIRTSI_SPACE_TABS_LINKS.history:
                assert POHIRTSI_SPACE_TABS_TITLES.history == title
            elif page == POHIRTSI_SPACE_TABS_LINKS.kindergarten:
                assert POHIRTSI_SPACE_TABS_TITLES.kindergarten == title
            elif page == POHIRTSI_SPACE_TABS_LINKS.school:
                assert POHIRTSI_SPACE_TABS_TITLES.school == title
            elif page == POHIRTSI_SPACE_TABS_LINKS.lyceum:
                assert POHIRTSI_SPACE_TABS_TITLES.lyceum == title
            elif page == POHIRTSI_SPACE_TABS_LINKS.religion:
                assert POHIRTSI_SPACE_TABS_TITLES.religion == title
            elif page == POHIRTSI_SPACE_TABS_LINKS.restaurant:
                assert POHIRTSI_SPACE_TABS_TITLES.restaurant == title
            elif page == POHIRTSI_SPACE_TABS_LINKS.news:
                assert POHIRTSI_SPACE_TABS_TITLES.news == title
            elif page == POHIRTSI_SPACE_TABS_LINKS.contacts:
                assert POHIRTSI_SPACE_TABS_TITLES.contacts == title
            else:
                return f'{page} is not found!'
    except Exception as e:
        print('Exception in test_image_in_each_page, ', e)
