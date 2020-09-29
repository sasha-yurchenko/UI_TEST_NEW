from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
import pyperclip


class LoginPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.email_field_css_selector = Locators.email_field_signin
        self.password_field_css_selector = Locators.password_field_signin
        self.login_button_xpath = Locators.login_button
        self.text_fail_auth_xpath = Locators.text_fail_auth_xpath

    def auth(self, email_field, password_field):
        try:
            self.driver.find_element(By.CSS_SELECTOR, self.email_field_css_selector).clear()
            self.driver.find_element(*Locators.email_field_signin).send_keys(email_field)
            self.driver.find_element(By.CSS_SELECTOR, self.password_field_css_selector).clear()
            self.driver.find_element(*Locators.password_field_signin).send_keys(password_field)
            self.driver.find_element(*Locators.login_button).click()
            return True
        except TimeoutException:
            print('Ничего не найдено')
        return False

    def registration(self):
        try:
            self.app.open_temp_mail()
            button = self.app.element_to_be_clickable(Locators.btn_copy_mail)
            button.click()
            self.app.wait_on_element_text(Locators.copy_mail, "Скопировано")
            self.driver.execute_script("window.open('https://t-front.spacemir.com/account/signin', 'new_window')")
            self.driver.switch_to_window(self.driver.window_handles[1])
            assert "signin" in self.driver.current_url
            self.driver.find_element(*Locators.button_submit_geo_position).click()
            self.driver.find_element(*Locators.tab_signup).click()
            field_reg = self.driver.find_elements(*Locators.form_signup_field)
            for fields in field_reg:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys(pyperclip.paste())
                else:
                    fields.send_keys('123456')
            self.driver.find_element(*Locators.btn_submit_signup).click()
        except NoSuchElementException:
            return False

    def enter_password(self, password_field):
        self.driver.find_element(*Locators.password_field_signin).send_keys(password_field)
        self.driver.find_element(*Locators.password_field_signin).click()

    def check_text_fail_auth(self):
        try:
            elem = self.driver.find_element(*Locators.text_fail_auth_xpath)
            text_fail_auth = elem.text
            assert text_fail_auth == "Ошибка, пары логин пароль не существует или они не верны"
            return True
        except NoSuchElementException:
            return False and self.app.destroy()

    def assertion_page_auth(self):
        return self.driver.current_url
