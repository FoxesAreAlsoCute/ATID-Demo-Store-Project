from selenium.webdriver.common.by import By

class HomePageLocators:
    MAIN_TITLE = (By.CSS_SELECTOR, ".elementor-widget-container h1")
    
class StorePageLocators:
    CATEGORIES_LIST = (By.CSS_SELECTOR, ".product-categories li a")