from time import sleep as explicit_wait

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..consts import (EXECUTABLE_PATH, POHIRTSI_SPACE_BUTTONS_TITLES, TIMEOUT,
                      URL)
from ..view import BUTTONS, ID_TEXT_TITLE, POHIRTSI_SPACE_BUTTONS_IDS


@pytest.mark.parametrize("button", BUTTONS, scope="function")
def test_click_buttons(button, get_webdriver_url, get_title):
    """ test buttons click and return correct page with correct title """
    try:
        driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
        driver.get(URL)
        explicit_wait(TIMEOUT)

        driver.find_element(By.ID, button).click()
        static_title_from_page = driver.find_element(By.ID, ID_TEXT_TITLE).text

        if button == POHIRTSI_SPACE_BUTTONS_IDS.about:
            assert static_title_from_page == POHIRTSI_SPACE_BUTTONS_TITLES.about, \
                f'Page title {static_title_from_page} is not correct!'
        elif button == POHIRTSI_SPACE_BUTTONS_IDS.history:
            assert static_title_from_page == POHIRTSI_SPACE_BUTTONS_TITLES.history, \
                f'Page title {static_title_from_page} is not correct!'
        elif button == POHIRTSI_SPACE_BUTTONS_IDS.kindergarten:
            assert static_title_from_page == POHIRTSI_SPACE_BUTTONS_TITLES.kindergarten,\
                f'Page title {static_title_from_page} is not correct!'
        elif button == POHIRTSI_SPACE_BUTTONS_IDS.school:
            assert static_title_from_page == POHIRTSI_SPACE_BUTTONS_TITLES.school,\
                f'Page title {static_title_from_page} is not correct!'
        elif button == POHIRTSI_SPACE_BUTTONS_IDS.lyceum:
            assert static_title_from_page == POHIRTSI_SPACE_BUTTONS_TITLES.lyceum, \
                f'Page title {static_title_from_page} is not correct!'
        elif button == POHIRTSI_SPACE_BUTTONS_IDS.religion:
            assert static_title_from_page == POHIRTSI_SPACE_BUTTONS_TITLES.religion, \
                f'Page title {static_title_from_page} is not correct!'
        elif button == POHIRTSI_SPACE_BUTTONS_IDS.restaurant:
            assert static_title_from_page == POHIRTSI_SPACE_BUTTONS_TITLES.restaurant,\
                f'Page title {static_title_from_page} is not correct!'
        elif button == POHIRTSI_SPACE_BUTTONS_IDS.news:
            assert static_title_from_page == POHIRTSI_SPACE_BUTTONS_TITLES.news,\
                f'Page title {static_title_from_page} is not correct!'
        elif button == POHIRTSI_SPACE_BUTTONS_IDS.contacts:
            assert static_title_from_page == POHIRTSI_SPACE_BUTTONS_TITLES.contacts,\
                f'Page title {static_title_from_page} is not correct!'
    except Exception as e:
        print('Exception in test_navigation_tablet, ', e)
