import unittest

from . import base_class
from . import const


class AllTitlesTestSuite(base_class.BaseSetUp):

    def test_titles_in_each_page(self):
        pages = ['', '/history', '/kindergarten', '/school', '/lyceum', '/religion', '/restaurant', '/contacts']
        for page in pages:
            self.browser.get(const.URL + page)
            if page == '':
                self.assertIn('Про нас - Погірці', self.browser.title)
            elif page == '/history':
                self.assertIn('Історія - Погірці', self.browser.title)
            elif page == '/kindergarten':
                self.assertIn('Садок - Погірці', self.browser.title)
            elif page == '/school':
                self.assertIn('Школа - Погірці', self.browser.title)
            elif page == '/lyceum':
                self.assertIn('Ліцей - Погірці', self.browser.title)
            elif page == '/religion':
                self.assertIn('Релігія - Погірці', self.browser.title)
            elif page == '/restaurant':
                self.assertIn('Ресторан - Погірці', self.browser.title)
            elif page == '/contacts':
                self.assertIn('Контакти - Погірці', self.browser.title)
            else:
                return f'{page} is not found!'


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
