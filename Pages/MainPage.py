from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException


class MainPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.product_button = Locators.add_product_button
        self.element_on_top_block = Locators.elements_top_blocks
        self.button_search = Locators.search_button
        self.search_input = Locators.input_search

    def check_elements_on_main_page(self):
        try:
            self.driver.find_element_by_css_selector(Locators.add_product_button)
            self.driver.find_element_by_css_selector(Locators.elements_top_blocks)
            self.driver.find_element_by_css_selector(Locators.search_button)
            self.driver.find_element_by_css_selector(Locators.input_search)
            return True
        except TimeoutException:
            print('Ничего не найдено')
            return False
