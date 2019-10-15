from selenium.webdriver.common.keys import Keys

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

    def choice_category(self):
        self.driver.find_element_by_xpath(Locators.choice_category_in_catalog).click()

    def choice_child_category(self):
        self.driver.find_element_by_xpath(Locators.choice_child_category_in_catalog).click()

    def choice_filter(self):
        self.driver.find_element_by_xpath(Locators.choice_filter).click()

    def open_drop_down(self):
        self.driver.find_element_by_xpath(Locators.open_drop_down_button).click()

    def void_search_element(self, name_element):
        self.driver.find_element_by_xpath(self.field_search_elements).clean()
        self.driver.find_element_by_xpath(Locators.field_search_elements).send_keys(name_element, Keys.ARROW_DOWN)
