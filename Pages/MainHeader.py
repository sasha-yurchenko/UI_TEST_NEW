from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Header:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.button_login_header = Locators.button_login
        self.button_registration_header = Locators.button_registration
        self.button_change_language_interface = Locators.change_language_interface
        self.button_close_language_interface = Locators.close_language_interface
        self.interface_language_list = Locators.interface_language_list
        self.button_confirm_language_interface = Locators.button_confirm
        self.button_main_directory_catalog = Locators.button_main_directory
        self.button_close_main_directory = Locators.close_main_directory
        self.main_logo_headers = Locators.main_logo_headers
        self.field_search_headers = Locators.field_search_headers
        self.drop_down_list_geo = Locators.drop_down_list_geo

    def click_button_login_header(self):
        self.driver.find_element_by_xpath(Locators.button_login).click()

    def click_button_registration_header(self):
        self.driver.find_element_by_xpath(Locators.button_registration).click()

    def click_button_change_language_interface(self):
        self.driver.find_element_by_xpath(Locators.change_language_interface).click()

    def click_close_language_interface(self):
        self.driver.find_element_by_xpath(Locators.close_language_interface).click()

    def open_interface_language_list(self):
        self.driver.find_element_by_xpath(Locators.interface_language_list).click()

    def button_confirm_language_interface(self):
        self.driver.find_element_by_xpath(Locators.button_confirm).click()

    def open_main_catalog(self):
        self.driver.find_element_by_xpath(Locators.button_main_directory).click()

    def close_main_catalog(self):
        self.driver.find_element_by_xpath(Locators.close_main_directory).click()

    def click_logo_header(self):
        self.driver.find_element_by_xpath(Locators.main_logo_headers).click()

    def open_drop_down_list_geo(self):
        self.driver.find_element_by_xpath(Locators.drop_down_list_geo).click()
