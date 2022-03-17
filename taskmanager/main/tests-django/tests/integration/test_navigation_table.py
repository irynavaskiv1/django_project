from time import sleep as explicit_wait

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..consts import EXECUTABLE_PATH, MENU_BAR_STR, POHIRTSI_SPACE_TABS_LINKS


@pytest.mark.parametrize("pages", [POHIRTSI_SPACE_TABS_LINKS.about, POHIRTSI_SPACE_TABS_LINKS.history,
                                   POHIRTSI_SPACE_TABS_LINKS.kindergarten, POHIRTSI_SPACE_TABS_LINKS.school,
                                   POHIRTSI_SPACE_TABS_LINKS.lyceum, POHIRTSI_SPACE_TABS_LINKS.religion,
                                   POHIRTSI_SPACE_TABS_LINKS.restaurant, POHIRTSI_SPACE_TABS_LINKS.news,
                                   POHIRTSI_SPACE_TABS_LINKS.contacts])
def test_navigation_table(pages, get_webdriver_url, get_title):
    """ test that all pages returns correct navigation bar """
    try:
        for page in pages:
            browser = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
            browser.get(page)
            explicit_wait(5)

            elements = browser.find_element(By.ID, "menu-menu").text
            new_elements = elements.rstrip()
            assert new_elements == MENU_BAR_STR
    except Exception as e:
        print('Exception in test_navigation_tablet, ', e)
