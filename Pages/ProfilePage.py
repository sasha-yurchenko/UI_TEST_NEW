from Data.Locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


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
        self.driver.find_element(*Locators.button_profile_menu_xpath).click()

    def click_button_log_out(self):
        self.driver.find_element(*Locators.button_log_out_xpath).click()

    def check_exists_profile_elements(self):
        try:
            block = self.driver.find_element(*Locators.start_block_profile)
            top_block = self.driver.find_element(*Locators.top_block_profile)
            sider = self.driver.find_element(*Locators.sidebar_profile)
            btn_apa = self.driver.find_element(*Locators.button_apartaments)
            fav_btn = self.driver.find_element(*Locators.button_favorite_in_sidebar)
            if block and top_block and sider and btn_apa and fav_btn.is_displayed():
                return True
        except NoSuchElementException:
            print('Zero element for U!')
            self.app.destroy()
