import pytest
from pages.home_page import HomePage
from pages.store_page import StorePage


url = 'https://atid.store/'

@pytest.mark.smoke
def test_user_can_access_to_home_page(browser):
    home_page = HomePage(browser, url)
    home_page.open()
    home_page.should_be_home_page()

@pytest.mark.xfail(reason="The button is not clickable in automation")
def test_user_can_click_store_button(browser):
    home_page = HomePage(browser, url)
    home_page.open()
    home_page.click_store_button()
    store_page = StorePage(home_page.browser, home_page.browser.current_url)
    store_page.should_be_store_page()
    
    
    
# @pytest.mark.home
# class TestHomePage:
    
#     url = 'https://atid.store/'
    
#     def setup_method(self, browser):
#         self.home_page = HomePage(browser, self.url)
#         self.home_page.open()
    
#     @pytest.mark.smoke
#     def test_user_can_access_to_home_page(self):
#         self.home_page.should_be_home_page()
    
#     def test_user_can_click_store_button(self):
#         self.home_page.click_store_button()
#         store_page = StorePage(self.home_page.browser, self.home_page.browser.current_url)
#         store_page.should_be_store_page()