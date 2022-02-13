import pytest
import requests
from selenium import webdriver

from .consts import EXECUTABLE_PATH, URL


# general fixtures
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


# ui testing fixtures
@pytest.fixture
def get_title():
    def _(page):
        title = None
        opened_url = URL + page
        try:
            r = requests.get(opened_url)
            al = r.text
            title = al[al.find('<title>') + 7: al.find('</title>')]
        except Exception as e:
            print(f'Can open {opened_url} in get_title fixture!', e)
        return title
    return _
