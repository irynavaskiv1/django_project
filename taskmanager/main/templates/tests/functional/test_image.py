import const
import unittest

from . import base_class


class AllTitlesTestSuite(base_class.BaseSetUp):

    def test_about_us_page(self):
        self.browser.get(const.URL)
        image = self.browser.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div/div[1]/div/div/div/div')
        is_image_exist = True if 'align-left' in image.get_attribute('class') else False
        self.assertTrue(is_image_exist)

    def test_history_page(self):
        self.browser.get(const.URL + '/history')
        image = self.browser.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div/div[1]/div/div/div/div')
        is_image_exist = True if 'align-left' in image.get_attribute('class') else False
        self.assertTrue(is_image_exist)

    def test_kindergarten_page(self):
        self.browser.get(const.URL + '/kindergarten')
        image = self.browser.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div/div[1]/div/div/div/div')
        is_image_exist = True if 'align-left' in image.get_attribute('class') else False
        self.assertTrue(is_image_exist)

    def test_school_page(self):
        self.browser.get(const.URL + '/school')
        image = self.browser.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div/div[1]/div/div/div/div')
        is_image_exist = True if 'align-left' in image.get_attribute('class') else False
        self.assertTrue(is_image_exist)

    def test_lyceum_page(self):
        self.browser.get(const.URL + '/lyceum')
        image = self.browser.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div/div[1]/div/div/div/div')
        is_image_exist = True if 'align-left' in image.get_attribute('class') else False
        self.assertTrue(is_image_exist)

    def test_religion_page(self):
        self.browser.get(const.URL + '/religion')
        image = self.browser.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div/div[1]/div/div/div/div')
        is_image_exist = True if 'align-left' in image.get_attribute('class') else False
        self.assertTrue(is_image_exist)

    def test_restaurant_page(self):
        self.browser.get(const.URL + '/restaurant')
        image = self.browser.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div/div[1]/div/div/div/div')
        is_image_exist = True if 'align-left' in image.get_attribute('class') else False
        self.assertTrue(is_image_exist)

    def test_contacts_page(self):
        self.browser.get(const.URL + '/contacts')
        image = self.browser.find_element_by_xpath('/html/body/div[3]/main/div/div[2]/div/div[1]/div/div/div/div')
        is_image_exist = True if 'align-left' in image.get_attribute('class') else False
        self.assertTrue(is_image_exist)


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
