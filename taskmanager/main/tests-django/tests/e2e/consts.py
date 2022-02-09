from collections import namedtuple

# main consts
URL = 'http://www.pohirtsi.space'
EXECUTABLE_PATH = '/Users/admin/Documents/django_project/taskmanager/main/' \
                  'tests-django/drivers/chromedriver'

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
