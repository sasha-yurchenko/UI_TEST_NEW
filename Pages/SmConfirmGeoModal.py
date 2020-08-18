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

    def void_name_city(self, name_city):
        self.driver.find_element_by_xpath(Locators.field_name_city_xpath).send_keys(name_city)

    def void_name_country(self, name_country):
        self.driver.find_element_by_xpath(Locators.field_name_countries_xpath).send_keys(name_country)

    def click_submit_geo(self):
        try:
            self.driver.find_element_by_xpath(Locators.submit_geo_xpath).click()
            return True
        except ElementClickInterceptedException:
            return False and self.app.destroy()

    def click_name_countries(self):
        self.app.text_to_be_present_in_element((By.XPATH, Locators.button_check_counties_xpath), "São Paulo")
        self.driver.find_element_by_xpath(Locators.button_check_counties_xpath).click()

    def click_name_city(self):
        self.app.text_to_be_present_in_element((By.XPATH, Locators.button_check_city_xpath), "São Paulo")
        self.driver.find_element_by_xpath(Locators.button_check_city_xpath).click()

    def wait_for_name_countries(self):
        self.app.text_to_be_present_in_element((By.XPATH, Locators.button_check_counties_xpath), "Россия")

    def assert_name_geo(self):
        try:
            self.app.text_to_be_present_in_element_value((By.XPATH, Locators.search_wrap_geo_xpath), 'São Paulo')
            return True
        except NoSuchElementException:
            return False and self.app.destroy()

    def assertion_field_geo(self):  # Проверяем что в данной строке имеются элементы
        return len(self.driver.find_elements_by_xpath \
                (
                "/html/body/sm-root/sm-base-layout/sm-header/div/div/sm-global-geo/div/div/div/div/input")) > 0

    def click_submit_geo_position(self):
        self.app.element_to_be_clickable((By.CSS_SELECTOR, Locators.button_submit_geo_position))
        self.driver.find_element_by_css_selector(Locators.button_submit_geo_position).click()

    def click_choose_another_country(self):
        self.app.element_to_be_clickable((By.XPATH, Locators.button_choose_another_country))
        self.driver.find_element_by_xpath(Locators.button_choose_another_country).click()
