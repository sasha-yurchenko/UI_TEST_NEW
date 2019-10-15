from Locators.locators import Locators


class LoginPage():

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.email_field_xpath = Locators.email_field_xpath
        self.password_field_xpath = Locators.password_field_xpath
        self.login_button_xpath = Locators.login_button_xpath

    def enter_email_field(self, email_field):
        self.driver.find_element_by_xpath(self.email_field_xpath).clear()
        self.driver.find_element_by_xpath(Locators.email_field_xpath).send_keys(email_field)

    def enter_password(self, password_field):
        self.driver.find_element_by_xpath(self.password_field_xpath).clear()
        self.driver.find_element_by_xpath(Locators.password_field_xpath).send_keys(password_field)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_button_xpath).click()
