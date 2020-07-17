from Locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException


class ProfilePage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.button_profile_menu_xpath = Locators.button_profile_menu_xpath
        self.button_log_out_xpath = Locators.button_log_out_xpath
        self.start_block_profile = Locators.start_block_profile
        self.sidebar_profile = Locators.sidebar_profile
        self.button_apartaments = Locators.button_apartaments
        self.button_favorite = Locators.button_favorite

    def click_button_profile(self):
        self.driver.find_element_by_xpath(Locators.button_profile_menu_xpath).click()

    def click_button_log_out(self):
        self.driver.find_element_by_xpath(Locators.button_log_out_xpath).click()

    def check_exists_profile_elements(self):
        try:
            self.driver.find_element_by_xpath(Locators.start_block_profile)
            self.driver.find_element_by_xpath(Locators.sidebar_profile)
            self.driver.find_element_by_xpath(Locators.button_apartaments)
            self.driver.find_element_by_xpath(Locators.button_favorite)
            return True
        except NoSuchElementException:
            print('Zero element for U!')
            return False
