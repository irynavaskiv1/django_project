from time import sleep as explicit_wait

from ..consts import (PAGES, POHIRTSI_SPACE_TABS_LINKS,
                      POHIRTSI_SPACE_TABS_TITLES)


def test_titles_in_each_page(get_webdriver_url, get_title):
    """ test that all pages returns correct title """

    try:
        for page in PAGES:
            get_webdriver_url(page=page)
            explicit_wait(2)
            title = get_title(page=page)
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
        print('Exception in test_titles_in_each_page, ', e)