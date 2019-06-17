from page.display_page import DisplayPage
from page.first_network_page import FirstNetworkPage
from page.mobile_network_page import MobileNetworkPage
from page.more_page import MorePage
from page.search_page import SearchPage
from page.setting_page import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def first_network(self):
        return FirstNetworkPage(self.driver)

    @property
    def mobile_network(self):
        return MobileNetworkPage(self.driver)

    @property
    def more(self):
        return MorePage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def display(self):
        return DisplayPage(self.driver)

    @property
    def search(self):
        return SearchPage(self.driver)
