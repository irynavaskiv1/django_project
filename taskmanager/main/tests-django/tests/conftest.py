import pytest
from selenium import webdriver

from .consts import EXECUTABLE_PATH, URL


@pytest.fixture
def get_webdriver_url():
    def _get_webdriver_url(page):
        opened_url = None
        try:
            browser = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
            if page == '':
                opened_url = URL
                browser.get(opened_url)
            else:
                opened_url = URL + page
                browser.get(opened_url)
        except Exception as e:
            print(f'Can open {opened_url} !', e)
    return _get_webdriver_url
