from time import sleep as explicit_wait

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..consts import (EXECUTABLE_PATH, MENU_BAR_STR, POHIRTSI_SPACE_TABS_LINKS,
                      TIMEOUT)
from ..view import MENU_BAR_ID


@pytest.mark.parametrize("pages", [POHIRTSI_SPACE_TABS_LINKS.about, POHIRTSI_SPACE_TABS_LINKS.history,
                                   POHIRTSI_SPACE_TABS_LINKS.kindergarten, POHIRTSI_SPACE_TABS_LINKS.school,
                                   POHIRTSI_SPACE_TABS_LINKS.lyceum, POHIRTSI_SPACE_TABS_LINKS.religion,
                                   POHIRTSI_SPACE_TABS_LINKS.restaurant, POHIRTSI_SPACE_TABS_LINKS.news,
                                   POHIRTSI_SPACE_TABS_LINKS.contacts])
def test_navigation_table(pages, get_webdriver_url, get_title):
    """
    @ID: 004
    @Category: integration
    @Description: Test that all pages returns correct navigation bar
    @tcmethod: automated

    Steps:
        1. Click to each button in main page

    Expected:
        1. In each page navigation bar return correct and all buttons
    """
    try:
        for page in pages:
            browser = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
            browser.get(page)
            explicit_wait(TIMEOUT)

            elements = browser.find_element(By.ID, MENU_BAR_ID).text
            new_elements = elements.rstrip()
            assert new_elements == MENU_BAR_STR
    except Exception as e:
        print('Exception in test_navigation_table, ', e)
