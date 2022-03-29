from time import sleep as explicit_wait

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..consts import (EXECUTABLE_PATH, POHIRTSI_SPACE_PAGE_TITLES, TIMEOUT,
                      URL)
from ..view import BUTTONS, ID_LOGO_IMG, ID_TEXT_TITLE


@pytest.mark.skip
@pytest.mark.parametrize("button", BUTTONS, scope="function")
def test_logo(button):
    """
    @ID: 005
    @Category: ui
    @Description: Test that click to logo returns main page
    @tcmethod: automated

    Steps:
        1. Click to logo button in each page

    Expected:
        1. In each page logo button returns main page
    """

    driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
    driver.get(URL)
    explicit_wait(TIMEOUT // 2)
    driver.find_element(By.ID, button).click()
    explicit_wait(TIMEOUT // 2)

    element = driver.find_elements_by_id(ID_LOGO_IMG)
    driver.execute_script("arguments[0].click();", element)

    driver.find_element(By.ID, ID_LOGO_IMG).click()
    explicit_wait(TIMEOUT)

    update_title_from_page = driver.find_element(By.ID, ID_TEXT_TITLE).text
    print(update_title_from_page, 'update_title_from_page')
    assert update_title_from_page == POHIRTSI_SPACE_PAGE_TITLES.about, \
        f'Page title {update_title_from_page} is not correct!'
