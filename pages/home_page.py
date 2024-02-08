from .base_page import BasePage
from ._locators import HomePageLocators

class HomePage(BasePage):
    expected_text="ATID Demo Store"
    
    def should_be_home_page(self):
        assert self.element_is_not_visible(HomePageLocators.MAIN_TITLE), "Main title is not visible"
        text = self.get_visible_text(HomePageLocators.MAIN_TITLE)
        assert text == self.expected_text, "Text of main title is not as expected"