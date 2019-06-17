import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FirstNetworkPage(BaseAction):
    # 2g
    network_2g_button = By.XPATH, "//*[@text='2G']"

    # 3g
    network_3g_button = By.XPATH, "//*[@text='3G']"

    @allure.step(title="更多—移动网络—首选网络—点击2G")
    def click_2g(self):
        self.click(self.network_2g_button)

    @allure.step(title="更多—移动网络—首选网络—点击3G")
    def click_3g(self):
        self.click(self.network_3g_button)

