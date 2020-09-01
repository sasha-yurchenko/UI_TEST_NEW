from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys


class ConstructPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.main_category = Locators.select_main_category
        self.nested_category = Locators.select_nested_category
        self.google_search = Locators.input_google_country

    def create_new_product(self, country):
        try:
            self.driver.find_element(By.CSS_SELECTOR, Locators.add_product_button).click()
            self.app.element_to_be_clickable((By.CSS_SELECTOR, Locators.select_main_category))
            self.driver.find_element(By.CSS_SELECTOR, Locators.select_main_category).click()
            self.driver.find_element(By.CSS_SELECTOR, Locators.select_nested_category).click()
            self.app.presence_of_element_located((By.CSS_SELECTOR, Locators.category_path))
            self.app.presence_of_element_located((By.CSS_SELECTOR, Locators.change_link))
            self.driver.find_element(By.CSS_SELECTOR, Locators.input_google_country).clear()
            self.driver.find_element(By.CSS_SELECTOR, Locators.input_google_country).send_keys(country)
            self.app.text_to_be_present_in_element((By.CSS_SELECTOR, Locators.name_contry_list), 'Бразилия')
            self.driver.find_element(By.CSS_SELECTOR, Locators.list_country).click()
            self.driver.find_element(By.CSS_SELECTOR, Locators.button_publication).click()
            return True
        except TimeoutException:
            return False and self.app.destroy()

    def choosing_value_in_select(self):
        call_select = self.driver.find_elements(By.CSS_SELECTOR, Locators.select_multiselect_wrap)
        for select in call_select:
            select.click()
            choice_value = self.driver.find_element(By.CSS_SELECTOR, Locators.value_in_dropdown_select)
            choice_value.click()



