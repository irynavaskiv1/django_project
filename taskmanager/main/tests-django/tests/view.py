from collections import namedtuple

# menu bar buttons
ID_LOGO_IMG = ''

PohirtsiSpaceButtonsIds = namedtuple(
    "PohirtsiSpaceTabsLinks", "about history kindergarten school lyceum religion restaurant news contacts")
POHIRTSI_SPACE_BUTTONS_IDS = PohirtsiSpaceButtonsIds(about='menu_item-1', history='menu_item-2',
                                                     kindergarten='menu_item-3', school='menu_item-4',
                                                     lyceum='menu_item-5', religion='menu_item-6',
                                                     restaurant='menu_item-7', news='menu_item-8',
                                                     contacts='menu_item-9')
BUTTONS = [POHIRTSI_SPACE_BUTTONS_IDS.about, POHIRTSI_SPACE_BUTTONS_IDS.history,
           POHIRTSI_SPACE_BUTTONS_IDS.kindergarten, POHIRTSI_SPACE_BUTTONS_IDS.school,
           POHIRTSI_SPACE_BUTTONS_IDS.lyceum, POHIRTSI_SPACE_BUTTONS_IDS.religion,
           POHIRTSI_SPACE_BUTTONS_IDS.restaurant, POHIRTSI_SPACE_BUTTONS_IDS.news, POHIRTSI_SPACE_BUTTONS_IDS.contacts]

# main block
ID_TEXT_TITLE = 'text title'
