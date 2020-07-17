from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from Locators.locators import Locators


class ProductsPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.choice_category_in_catalog = Locators.choice_category_in_catalog
        self.choice_child_category_in_catalog = Locators.choice_child_category_in_catalog
        self.choice_filter = Locators.choice_filter
        self.open_drop_down_button = Locators.open_drop_down_button
        self.label_ads_short_card = Locators.label_ads_short_card
        self.field_search_elements = Locators.field_search_elements
        self.value_filter_label_xpath = Locators.sm_multiselect_dropdown_menu
        self.value_dropdown = Locators.value_drop_down
        self.click_on_page = Locators.click_on_page
        self.button_number = Locators.button_number
        self.button_chat = Locators.button_chat
        self.button_favorite_on_product_page = Locators.button_favorite_on_product_page
        self.main_price = Locators.main_price
        self.name_user = Locators.name_seller

    def choice_category(self):
        self.driver.find_element_by_xpath(Locators.choice_category_in_catalog).click()

    def choice_child_category(self):
        self.driver.find_element_by_xpath(Locators.choice_child_category_in_catalog).click()

    def choice_filter_marks(self):
        self.driver.find_element_by_xpath(Locators.choice_filter).click()

    def wait_for_clickable(self):
        return self.app.element_expected_conditions(By.XPATH, Locators.choice_filter)

    def tab_exist_product_page(self):
        tab_1 = self.driver.find_element_by_xpath(Locators.tab_main)
        if self.app.visibility_element_expected_conditions(tab_1):
            return True
        else:
            return False and self.app.destroy()

    def button_number_wait(self):
        element = self.driver.find_element_by_xpath(Locators.button_number)
        if self.app.visibility_element_expected_conditions(element):
            return True
        else:
            return False and self.app.destroy()

    def check_value_on_title(self):
        try:
            self.app.text_to_be_present_in_element_value((By.XPATH, Locators.label_ads_short_card), 'Nissan')
            return True
        except NoSuchElementException:
            return False and self.app.destroy()

    def click_search_element(self):
        try:
            self.driver.find_element_by_xpath(Locators.field_search_elements).click()
            return True
        except NoSuchElementException as e:
            return False

    def open_list_with_references(self):
        try:
            self.driver.find_element_by_xpath(Locators.open_drop_down_button).click()
        except ElementClickInterceptedException:
            self.app.element_to_be_clickable(Locators.open_drop_down_button)

    def void_search_marks(self, marks_auto):
        try:
            self.driver.find_element_by_xpath(Locators.field_search_elements).send_keys(marks_auto)
            return True
        except NoSuchElementException as e:
            return False

    def wait_drop_down(self):
        try:
            self.app.element_expected_conditions(By.XPATH, Locators.sm_multiselect_dropdown_menu)
            return True
        except TimeoutException:
            return False

    def check_value(self):
        self.driver.find_element_by_xpath(Locators.value_drop_down).click()

    def close_filter_drop_down(self):
        self.driver.find_element_by_xpath(Locators.click_on_page).click()

    def check_availability_elements_on_short_card(self):
        try:
            self.driver.find_element_by_xpath(Locators.button_chat)
            self.driver.find_element_by_xpath(Locators.button_favorite_on_product_page)
            self.driver.find_element_by_xpath(Locators.main_price)
            self.driver.find_element_by_xpath(Locators.name_seller)
            return True
        except TimeoutError:
            print('Ничего не найдено')
            return False
