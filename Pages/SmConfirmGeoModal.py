from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from Locators.locators import Locators
from selenium.webdriver.common.by import By


class GeoModal:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.button_cancel = Locators.btn_cancel_geo
        self.submit_geo = Locators.submit_geo
        self.field_name_countries = Locators.field_name_country
        self.field_name_city = Locators.field_name_city
        self.check_counties = Locators.geo_list_country
        self.check_city = Locators.geo_list_city
        self.search_wrap_geo = Locators.search_wrap_geo
        self.button_submit_geo_position = Locators.button_submit_geo_position
        self.button_choose_another_country = Locators.button_choose_another_country

    def click_submit_geo(self):
        try:
            self.driver.find_element(*Locators.submit_geo).click()
            return True
        except ElementClickInterceptedException:
            return False and self.app.destroy()

    def country_selection(self, city):
        try:
            assert "Spacemir" in self.driver.title
            self.driver.find_element(*Locators.button_choose_another_country).click()
            country = self.driver.find_element(*Locators.geo_list_country)
            country.click()
            void_city = self.driver.find_element(*Locators.field_name_city)
            void_city.send_keys(city)
            self.app.text_to_be_present_in_element(*Locators.geo_list_city, city)
            self.driver.find_element(*Locators.geo_list_city).click()
            self.driver.find_element(*Locators.submit_geo).click()
            self.app.text_to_be_present_in_element(*Locators.geo_place_name, city)
        except TimeoutException:
            return False

    def assert_name_country_header(self, city):
        try:
            self.app.text_to_be_present_in_element_value((By.CSS_SELECTOR, Locators.search_wrap_geo), city)
            return True
        except TimeoutException:
            return False and self.app.destroy()

    def click_submit_geo_position(self):
        self.driver.find_element(*Locators.button_submit_geo_position).click()

