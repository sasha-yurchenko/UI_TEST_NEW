from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ConstructPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.main_category = Locators.select_main_category
        self.nested_category = Locators.select_nested_category

    def create_new_product(self, country):
        try:
            self.driver.find_element(By.CSS_SELECTOR, Locators.add_product_button).click()
            self.driver.find_element(By.CSS_SELECTOR, Locators.select_main_category).click()
            self.driver.find_element(By.CSS_SELECTOR, Locators.select_nested_category).click()
            self.app.presence_of_element_located((By.CSS_SELECTOR, Locators.category_path))
            self.app.presence_of_element_located((By.CSS_SELECTOR, Locators.change_link))
            self.driver.find_element(By.CSS_SELECTOR, Locators.input_google_country).send_keys(country)
            return True
        except NoSuchElementException:
            return False and self.app.destroy()
