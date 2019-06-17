import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestDisplay:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("search", "test_search"))
    def test_search(self, args):
        value = args["value"]
        self.page.display.click_search()
        self.page.search.input_search(value)
        self.page.search.click_back()
