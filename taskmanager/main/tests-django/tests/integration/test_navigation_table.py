import os
from time import sleep as explicit_wait

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..consts import MENU_BAR_STR, TIMEOUT, URLS
from ..view import ID_MENU_BAR


@pytest.mark.parametrize('url', URLS)
def test_navigation_table(url):
    """
    @ID: 004
    @Category: integration
    @Description: Test that all pages returns correct navigation bar
    @tcmethod: automated

    Steps:
        1. Click to each button in main page

    Expected:
        1. In each page navigation bar returns all buttons
    """

    path = os.path.abspath(__file__ + "/../../../")
    chrome_path = os.path.join(path, 'drivers', 'chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get(url=url)
    explicit_wait(TIMEOUT * 2)

    elements = driver.find_element(By.ID, ID_MENU_BAR).text
    new_elements = elements.rstrip()
    assert new_elements == MENU_BAR_STR
