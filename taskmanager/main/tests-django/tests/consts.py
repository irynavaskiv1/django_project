from collections import namedtuple

# main consts
URL = 'http://www.pohirtsi.space'
URLS = ['https://www.pohirtsi.space/', 'https://www.pohirtsi.space/history', 'https://www.pohirtsi.space/kindergarten',
        'https://www.pohirtsi.space/school', 'https://www.pohirtsi.space/lyceum',
        'https://www.pohirtsi.space/religion', 'https://www.pohirtsi.space/restaurant',
        'https://www.pohirtsi.space/news', 'https://www.pohirtsi.space/contacts']

EXECUTABLE_PATH = '/Users/admin/Documents/django_project/taskmanager/main/tests-django/drivers/chromedriver'
TIMEOUT = 5

# html consts
HTML_EXTENSION = '.html'
PohirtsiSpaceTabs = namedtuple(
    "PohirtsiSpaceTabs", "about history kindergarten school lyceum religion restaurant news contacts")
POHIRTSI_SPACE_TABS_HTML = PohirtsiSpaceTabs(about="about.html", history="history.html",
                                             kindergarten="kindergarten.html", school="school.html",
                                             lyceum="lyceum.html", religion="religion.html",
                                             restaurant="restaurant.html", news="news.html", contacts="contacts.html")

PohirtsiSpaceTabsLinks = namedtuple(
    "PohirtsiSpaceTabsLinks", "about history kindergarten school lyceum religion restaurant news contacts")
POHIRTSI_SPACE_TABS_LINKS = PohirtsiSpaceTabsLinks(about="/about", history="/history", kindergarten="/kindergarten",
                                                   school="/school", lyceum="/lyceum", religion="/religion",
                                                   restaurant="/restaurant", news="/news", contacts="/contacts")

PAGES = [POHIRTSI_SPACE_TABS_LINKS.about, POHIRTSI_SPACE_TABS_LINKS.history, POHIRTSI_SPACE_TABS_LINKS.kindergarten,
         POHIRTSI_SPACE_TABS_LINKS.school, POHIRTSI_SPACE_TABS_LINKS.lyceum, POHIRTSI_SPACE_TABS_LINKS.religion,
         POHIRTSI_SPACE_TABS_LINKS.restaurant, POHIRTSI_SPACE_TABS_LINKS.news, POHIRTSI_SPACE_TABS_LINKS.contacts]


# ui testing
PohirtsiSpaceTabsTitles = namedtuple(
    "PohirtsiSpaceTabsTitles", "about history kindergarten school lyceum religion restaurant news contacts")
POHIRTSI_SPACE_TABS_TITLES = PohirtsiSpaceTabsTitles(about=" Про село - Погірці ", history=" Історія - Погірці ",
                                                     kindergarten=" Садок - Погірці ", school=" Школа - Погірці ",
                                                     lyceum=" Ліцей - Погірці ", religion=" Релігія - Погірці ",
                                                     restaurant=" Ресторан - Погірці ", news=" Новини - Погірці ",
                                                     contacts=" Контакти - Погірці ")

MENU_BAR_STR = 'Про нас\nІсторія\nСадок\nШкола\nЛіцей\nРелігія\nРесторан\nНовини\nКонтакти'

PohirtsiSpacePageTitles = namedtuple(
    "PohirtsiSpaceTabsTitles", "about history kindergarten school lyceum religion restaurant news contacts")
POHIRTSI_SPACE_PAGE_TITLES = PohirtsiSpacePageTitles(about="Про село Погірці", history="Історія села",
                                                     kindergarten="Садок", school="Школа", lyceum="Ліцей",
                                                     religion="Релігія", restaurant="Ресторан", news="Новини",
                                                     contacts="Контакти")
