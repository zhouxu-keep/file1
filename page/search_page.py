import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):
    search_input = By.ID, "com.android.settings:id/search"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    @allure.step(title="显示—搜索—输入内容")
    def input_search(self, value):
        allure.attach("输⼊", value, allure.attach_type.TEXT)
        self.input(self.search_input, value)
        allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)

    @allure.step(title="显示—搜索—点击返回")
    def click_back(self):
        self.click(self.back_button)
