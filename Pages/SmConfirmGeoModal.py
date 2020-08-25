from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from Locators.locators import Locators
from selenium.webdriver.common.by import By


class GeoModal:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.button_cancel_xpath = Locators.button_cancel_geo_xpath
        self.submit_geo_xpath = Locators.submit_geo_xpath
        self.field_name_countries_xpath = Locators.field_name_countries_xpath
        self.field_name_city_xpath = Locators.field_name_city_xpath
        self.button_check_counties_xpath = Locators.button_check_counties_xpath
        self.button_check_city_xpath = Locators.button_check_city_xpath
        self.search_wrap_geo_xpath = Locators.search_wrap_geo_xpath
        self.button_submit_geo_position = Locators.button_submit_geo_position
        self.button_choose_another_country = Locators.button_choose_another_country
        self.modal_geo_1 = Locators.geo_modal_first

    def click_submit_geo(self):
        try:
            self.driver.find_element_by_xpath(Locators.submit_geo_xpath).click()
            return True
        except ElementClickInterceptedException:
            return False and self.app.destroy()

    def country_selection(self, country, city):
        try:
            self.driver.find_element_by_xpath(Locators.field_name_countries_xpath).send_keys(country)
            self.app.text_to_be_present_in_element((By.XPATH, Locators.button_check_counties_xpath), country)
            self.driver.find_element_by_xpath(Locators.button_check_counties_xpath).click()
            self.driver.find_element_by_xpath(Locators.field_name_city_xpath).send_keys(city)
            self.app.text_to_be_present_in_element((By.XPATH, Locators.button_check_city_xpath), city)
            self.driver.find_element_by_xpath(Locators.button_check_city_xpath).click()
            self.driver.find_element_by_xpath(Locators.submit_geo_xpath).click()

            return True
        except NoSuchElementException:
            return False and self.app.destroy()

    def assert_name_geo(self, city):
        try:
            self.app.text_to_be_present_in_element_value((By.CSS_SELECTOR, Locators.search_wrap_geo_xpath), city)
            return True
        except NoSuchElementException:
            return False and self.app.destroy()

    def assert_name_country_header(self, city):
        try:
            self.app.text_to_be_present_in_element_value((By.CSS_SELECTOR, Locators.search_wrap_geo_xpath), city)
            return True
        except TimeoutException:
            return False and self.app.destroy()

    def click_submit_geo_position(self):
        self.app.element_to_be_clickable((By.CSS_SELECTOR, Locators.button_submit_geo_position))
        self.driver.find_element_by_css_selector(Locators.button_submit_geo_position).click()

    def click_choose_another_country(self):
        self.app.element_to_be_clickable((By.CSS_SELECTOR, Locators.button_choose_another_country))
        self.driver.find_element(By.CSS_SELECTOR, Locators.button_choose_another_country).click()
