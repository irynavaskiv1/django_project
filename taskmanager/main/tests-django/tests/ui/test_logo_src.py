import os
from time import sleep as explicit_wait

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..consts import TIMEOUT, URL
from ..view import BUTTONS, ID_LOGO_IMG, SRC_LOGO


@pytest.mark.parametrize("button", BUTTONS, scope="function")
def test_logo_src(button):
    """
    @ID: 005
    @Category: ui
    @Description: Test that logo has correct image link in each page
    @tcmethod: automated

    Steps:
        1. Click to each button in menu bar

    Expected:
        1. In each page logo button returns correct src
    """

    path = os.path.abspath(__file__ + "/../../../")
    chrome_path_obj = os.path.join(path, 'drivers', 'chromedriver')
    chrome_path = str(chrome_path_obj)
    driver = webdriver.Chrome(executable_path=chrome_path)

    driver.get(URL)
    explicit_wait(TIMEOUT)
    driver.find_element(By.ID, button).click()
    explicit_wait(TIMEOUT)

    logo = driver.find_element(By.ID, ID_LOGO_IMG)
    src_link = logo.get_attribute("src")
    explicit_wait(TIMEOUT)

    assert src_link == SRC_LOGO, f'SRC link {src_link} is not correct!'
