from Locators.locators import Locators
from selenium.webdriver.common.by import By


# класс для работы с главной страницей.
class SpaceMainHelper:

    # метод для инициализации фикстуры app и river через фикстуру
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.button_cancel_xpath = Locators.button_cancel_xpath
        self.submit_geo_xpath = Locators.submit_geo_xpath
        self.field_name_countries_xpath = Locators.field_name_countries_xpath
        self.field_name_city_xpath = Locators.field_name_city_xpath
        self.button_check_counties_xpath = Locators.button_check_counties_xpath
        self.button_check_city_xpath = Locators.button_check_city_xpath
        self.search_wrap_geo_xpath = Locators.search_wrap_geo_xpath

    def click_button_cancel_geo(self):
        self.app.element_to_be_clickable(By.XPATH, Locators.button_cancel_xpath)
        self.driver.find_element_by_xpath(Locators.button_cancel_xpath).click()

    def click_submit_geo(self):
        self.driver.find_element_by_xpath(Locators.submit_geo_xpath).click()

    def void_name_countries(self, name_countries):
        self.driver.find_element_by_xpath(Locators.field_name_countries_xpath).send_keys(name_countries)

    def void_name_city(self, name_city):
        self.driver.find_element_by_xpath(Locators.field_name_city_xpath).send_keys(name_city)

    def click_name_countries(self):
        self.app.text_to_be_present_in_element((By.XPATH, Locators.button_check_counties_xpath), "Россия")
        self.driver.find_element_by_xpath(Locators.button_check_counties_xpath).click()

    def click_name_city(self):
        self.app.text_to_be_present_in_element((By.XPATH, Locators.button_check_city_xpath), "Москва")
        self.driver.find_element_by_xpath(Locators.button_check_city_xpath).click()

    def wait_for_name_countries(self):
        self.app.text_to_be_present_in_element((By.XPATH, Locators.button_check_counties_xpath), "Россия")

    def assertion_button_log_in(self):  # Проверяем что в данной строке имеются элементы
        return len(self.driver.find_elements_by_xpath \
                       ("/html/body/sm-root/sm-base-layout/sm-header/div/div/div[3]/a[1]/button")) > 0

    def assertion_button_registration(self):  # Проверяем что в данной строке имеются элементы
        return len(self.driver.find_elements_by_xpath \
                       ("/html/body/sm-root/sm-base-layout/sm-header/div/div/div[3]/a[2]/button")) > 0

    def assertion_field_geo(self):  # Проверяем что в данной строке имеются элементы
        return len(self.driver.find_elements_by_xpath \
                       ("/html/body/sm-root/sm-base-layout/sm-header/div/div/sm-global-geo/div/div/div/div/input")) > 0

    def assertion_main_page(self):
        return self.driver.current_url

    def assertion_page_auth(self):
        return self.driver.current_url
