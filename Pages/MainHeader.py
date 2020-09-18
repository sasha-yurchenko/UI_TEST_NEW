from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Header:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.button_login_header = Locators.button_login
        self.button_registration_header = Locators.button_registration
        self.button_main_directory_catalog = Locators.button_main_directory
        self.main_logo_headers = Locators.main_logo_headers
        self.field_search_headers = Locators.field_search_headers
        self.drop_down_list_geo = Locators.drop_down_list_geo
        self.button_add_product = Locators.add_product_button

    def click_button_login_header(self):
        self.driver.find_element(*Locators.button_login).click()

    def click_button_registration_header(self):
        self.driver.find_element_by_xpath(*Locators.button_registration).click()

    def open_main_catalog(self):
        self.driver.find_element_by_xpath(*Locators.button_main_directory).click()

    def close_main_catalog(self):
        self.driver.find_element_by_xpath(*Locators.button_main_directory).click()

    def click_logo_header(self):
        self.driver.find_element_by_xpath(*Locators.main_logo_headers).click()

    def open_drop_down_list_geo(self):
        self.driver.find_element_by_xpath(*Locators.drop_down_list_geo).click()
