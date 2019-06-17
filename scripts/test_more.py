from base.base_driver import init_driver
from page.page import Page


class TestMore:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_2g(self):
        # 设置 - 点击更多
        self.page.setting.click_more()
        # 更多 - 点击移动网络
        self.page.more.click_mobile_network()
        # 移动网络 - 点击首选网络
        self.page.mobile_network.click_first_network()
        # 首选网络 - 点击2g
        self.page.first_network.click_2g()

    def test_3g(self):
        # 设置 - 点击更多
        self.page.setting.click_more()
        # 更多 - 点击移动网络
        self.page.more.click_mobile_network()
        # 移动网络 - 点击首选网络
        self.page.mobile_network.click_first_network()
        # 首选网络 - 点击2g
        self.page.first_network.click_3g()
