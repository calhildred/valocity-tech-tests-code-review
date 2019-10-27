import pytest

from tests.base_selenium import SeleniumCase
from tests.po.objects.home_objects import HomeObjects


@pytest.mark.readonly
class HomeTest(SeleniumCase):
    """
    Test class for the Home page
    """

    def setUp(self):
        """
        Test home page set up
        """
        self.home = HomeObjects(self.browser)
        self.home.open_url()

    def test_searching_the_key_word(self):
        """
        Test word search
        """
        self.home.search_key_word('Valocity')
