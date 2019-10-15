from Locators.locators import Locators


class ProfilePage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.button_profile_menu_xpath = Locators.button_profile_menu_xpath
        self.button_log_out_xpath = Locators.button_log_out_xpath

    def click_button_profile(self):
        self.driver.find_element_by_xpath(Locators.button_profile_menu_xpath).click()

    def click_button_log_out(self):
        self.driver.find_element_by_xpath(Locators.button_log_out_xpath).click()
