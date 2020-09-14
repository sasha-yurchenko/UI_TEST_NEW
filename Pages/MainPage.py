from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
import math


class MainPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.product_button = Locators.add_product_button
        self.element_h1 = Locators.element_top_blocks_h1
        self.element_h3 = Locators.elements_top_blocks_h3
        self.button_search = Locators.search_button
        self.search_input = Locators.input_search
        self.user_button = Locators.bottom_buttons_1
        self.business_button = Locators.bottom_buttons_2

    def check_elements_on_main_page(self):
        try:
            self.driver.find_element(*Locators.add_product_button)
            text_h1 = self.driver.find_element(*Locators.element_top_blocks_h1)
            h1 = text_h1.text
            assert h1 == "Сайт бесплатных объявлений"
            self.driver.find_elements(*Locators.elements_top_blocks_h3)
            self.driver.find_element(*Locators.search_button)
            self.driver.find_element(*Locators.input_search)
            self.driver.find_element(*Locators.bottom_buttons_1)
            self.driver.find_element(*Locators.bottom_buttons_2)
            return True
        except NoSuchElementException:
            print('Ничего не найдено')


