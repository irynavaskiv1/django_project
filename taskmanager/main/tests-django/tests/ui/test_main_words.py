from time import sleep as explicit_wait

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..consts import (EXECUTABLE_PATH, POHIRTSI_SPACE_PAGE_TITLES,
                      POHIRTSI_SPACE_TABS_LINKS, TIMEOUT, URL, URLS)
from ..view import ID_TEXT_TITLE


@pytest.mark.parametrize('url', URLS)
def test_main_words(url):
    """
    @ID: 007
    @Category: ui
    @Description: Test that all pages returns correct main words
    @tcmethod: automated

    Steps:
        1. Click to each page in site

    Expected:
        1. In each page main words (Про нас/Історія/Садок..) is visible and correct
    """

    driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
    driver.get(url)
    explicit_wait(TIMEOUT * 2)

    title = driver.find_element(By.ID, ID_TEXT_TITLE)
    if POHIRTSI_SPACE_TABS_LINKS.about in url or url == URL:
        assert POHIRTSI_SPACE_PAGE_TITLES.about == title.text
    elif POHIRTSI_SPACE_TABS_LINKS.history in url:
        assert POHIRTSI_SPACE_PAGE_TITLES.history == title.text
    elif POHIRTSI_SPACE_TABS_LINKS.kindergarten in url:
        assert POHIRTSI_SPACE_PAGE_TITLES.kindergarten == title.text
    elif POHIRTSI_SPACE_TABS_LINKS.school in url:
        assert POHIRTSI_SPACE_PAGE_TITLES.school == title.text
    elif POHIRTSI_SPACE_TABS_LINKS.lyceum in url:
        assert POHIRTSI_SPACE_PAGE_TITLES.lyceum == title.text
    elif POHIRTSI_SPACE_TABS_LINKS.religion in url:
        assert POHIRTSI_SPACE_PAGE_TITLES.religion == title.text
    elif POHIRTSI_SPACE_TABS_LINKS.restaurant in url:
        assert POHIRTSI_SPACE_PAGE_TITLES.restaurant == title.text
    elif POHIRTSI_SPACE_TABS_LINKS.news in url:
        assert POHIRTSI_SPACE_PAGE_TITLES.news == title.text
    elif POHIRTSI_SPACE_TABS_LINKS.contacts in url:
        assert POHIRTSI_SPACE_PAGE_TITLES.contacts == title.text
    else:
        return f'{url} is not found!'
