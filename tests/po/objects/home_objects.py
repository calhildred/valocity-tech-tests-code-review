from tests.base_page import BasePage
from tests.po.elements.ui.home_elements import HomeElements


class HomeObjects(BasePage):
    """
    Class representing the Home page
    """

    def __init__(self, browser):
        self.home = HomeElements()
        self.set_browser(browser)

    def open_url(self):
        """
        Opens set URL
        """
        self.go_to_url()
        self.home.search_button()

    # -------- logic --------#
    def search_key_word(self, key_word):
        """
        Searches for results based on a key word
        :param key_word: Key word the search will use
        """
        self.fill_search_text(key_word)
        self.click_search_button()

    # -------- page actions  --------#
    def fill_search_text(self, value=None):
        """
        Sets search box value
        :param value: Value to be entered into the search box
        """
        self.home.search_text.fill_field(value)

    def click_search_button(self):
        """
        Clicks search button
        """
        self.home.search_button.click_field(index=1)
