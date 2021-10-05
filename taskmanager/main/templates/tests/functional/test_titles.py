import unittest

from . import base_class
from . import const


class AllTitlesTestSuite(base_class.BaseSetUp):

    def test_about_us_page(self):
        self.browser.get(const.URL)
        self.assertIn('Про нас - Погірці', self.browser.title)

    def test_history_page(self):
        self.browser.get(const.URL + '/history')
        self.assertIn('Історія - Погірці', self.browser.title)

    def test_kindergarten_page(self):
        self.browser.get(const.URL + '/kindergarten')
        self.assertIn('Садок - Погірці', self.browser.title)

    def test_school_page(self):
        self.browser.get(const.URL + '/school')
        self.assertIn('Школа - Погірці', self.browser.title)

    def test_lyceum_page(self):
        self.browser.get(const.URL + '/lyceum')
        self.assertIn('Ліцей - Погірці', self.browser.title)

    def test_religion_page(self):
        self.browser.get(const.URL + '/religion')
        self.assertIn('Релігія - Погірці', self.browser.title)

    def test_restaurant_page(self):
        self.browser.get(const.URL + '/restaurant')
        self.assertIn('Ресторан - Погірці', self.browser.title)

    def test_contacts_page(self):
        self.browser.get(const.URL + '/contacts')
        self.assertIn('Контакти - Погірці', self.browser.title)


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
    runner.run(suite())
