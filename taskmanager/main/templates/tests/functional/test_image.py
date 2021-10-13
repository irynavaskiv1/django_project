import unittest

from . import const
from . import base_class
from bs4 import BeautifulSoup


class AllTitlesTestSuite(base_class.BaseSetUp):
    soup = BeautifulSoup(const.URL)
    URL = soup.currentTag.contents[0]

    def test_main_image(self):
        pages = ['', '/history', '/kindergarten', '/school', '/lyceum', '/religion', '/restaurant', '/contacts']
        for page in pages:
            self.browser.get(AllTitlesTestSuite.URL + page)
            image = self.browser.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div/div[1]/div/div/div/div')
            is_image_exist = True if 'align-left' in image.get_attribute('class') else False
            self.assertTrue(is_image_exist, msg='Main image exists')

    def test_logo_image(self):
        pages = ['', '/history', '/kindergarten', '/school', '/lyceum', '/religion', '/restaurant', '/contacts']
        for page in pages:
            self.browser.get(AllTitlesTestSuite.URL + page)
            logo_image = self.browser.find_element_by_xpath('//*[@id="layoutcontainer"]/div[6]/header/div[4]/div/a/img')
            is_logo_exist = True if 'img' in logo_image.tag_name else False
            self.assertTrue(is_logo_exist, msg='Logo image exists')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AllTitlesTestSuite('test_about_us_page'))
    suite.addTest(AllTitlesTestSuite('test_history_page'))
    suite.addTest(AllTitlesTestSuite('test_kindergarten_page'))
    suite.addTest(AllTitlesTestSuite('test_school_page'))
    suite.addTest(AllTitlesTestSuite('test_lyceum_page'))
    suite.addTest(AllTitlesTestSuite('test_religion_page'))
    suite.addTest(AllTitlesTestSuite('test_restaurant_page'))
    suite.addTest(AllTitlesTestSuite('test_contacts_page'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run()
