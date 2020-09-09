from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException


class LoginPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.email_field_css_selector = Locators.email_field_css_selector
        self.password_field_css_selector = Locators.password_field_css_selector
        self.login_button_xpath = Locators.login_button_xpath
        self.text_fail_auth_xpath = Locators.text_fail_auth_xpath

    def auth(self, email_field, password_field):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.email_field_css_selector).clear()
            self.driver.find_element(By.CSS_SELECTOR, Locators.email_field_css_selector).send_keys(email_field)
            self.driver.find_element(By.CSS_SELECTOR, self.password_field_css_selector).clear()
            self.driver.find_element(By.CSS_SELECTOR, Locators.password_field_css_selector).send_keys(password_field)
            self.driver.find_element(By.CSS_SELECTOR, Locators.login_button_xpath).click()
            return True
        except TimeoutException:
            print('Ничего не найдено')
        return False

    def enter_password(self, password_field):
        self.driver.find_element(By.CSS_SELECTOR, Locators.password_field_css_selector).send_keys(password_field)
        self.driver.find_element(By.CSS_SELECTOR, Locators.password_field_css_selector).click()

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.login_button_xpath).click()

    def check_text_fail_auth(self):
        try:
            elem = self.driver.find_element(By.CSS_SELECTOR, Locators.text_fail_auth_xpath)
            text_fail_auth = elem.text
            assert text_fail_auth == "Ошибка, пары логин пароль не существует или они не верны"
            return True
        except NoSuchElementException:
            return False and self.app.destroy()
