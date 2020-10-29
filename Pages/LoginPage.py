from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException, \
    StaleElementReferenceException
import pyperclip
import random
import string


class LoginPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.name = self.app.GenKey() + str('@mail.com')
        self.mail = self.name

        self.auth_mail = self.mail

        self.toast_container = Locators.toast_container
        self.email_field_signin = Locators.email_field_signin
        self.password_field_css_selector = Locators.password_field_signin
        self.login_button_xpath = Locators.login_button
        self.text_fail_auth_xpath = Locators.text_fail_auth
        self.btn_on_latter = Locators.btn_on_letter
        self.btn_submit_geo_position = Locators.button_submit_geo_position
        self.btn_recovery_mail = Locators.btn_recovery_mail
        self.email_field_signup = Locators.email_field_signup
        self.password_field_signup = Locators.password_field_signup
        self.forgot_password = Locators.forgot_password
        self.field_email_for_forgot_password = Locators.field_email_for_forgot_password
        self.input_mail_recovery = Locators.input_mail_recovery
        self.button_send_email_for_forgot_password = Locators.button_send_email_for_forgot_password
        self.text_fail_auth = Locators.text_fail_auth
        self.text_fail_field = Locators.text_fail_field
        self.text_fail_password = Locators.text_fail_password
        self.text_fail_mail = Locators.text_fail_mail
        self.tab_signin = Locators.tab_signin
        self.tab_signup = Locators.tab_signup
        self.form_signup_field = Locators.form_signup_field
        self.form_signin_fields = Locators.form_signin_fields
        self.btn_submit_signin = Locators.btn_submit_signin
        self.btn_submit_signup = Locators.btn_submit_signup
        self.btn_send_recovery_mail = Locators.btn_send_recovery_mail
        self.btn_submit_change_password = Locators.btn_submit_change_password

    def receiving_mail(self):
        try:
            # Получаем новую почту и регистрируемся в системе
            self.app.open_temp_mail()
            self.driver.refresh()
            button = self.app.element_to_be_clickable(Locators.btn_copy_mail)
            button.click()
            self.app.wait_on_element_text(Locators.copy_mail, "Скопировано")
            self.driver.execute_script("window.open('https://d-front.spacemir.com/account/signup', 'new_window')")
            self.driver.switch_to_window(self.driver.window_handles[1])
            assert "signup" in self.driver.current_url
            self.driver.find_element(*Locators.button_submit_geo_position).click()
        except ElementClickInterceptedException:
            print("Not Found") and self.app.destroy()

    def creation_user(self):
        try:
            field_reg = self.driver.find_elements(*self.form_signup_field)
            for fields in field_reg:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys(pyperclip.paste())
                else:
                    fields.send_keys('123456')
            self.driver.find_element(*self.btn_submit_signup).click()
        except NoSuchElementException:
            return False and self.app.destroy()

    def check_and_wait_welcome_modal(self):
        try:
            # Ожидаем появления модалки приветствия и переходим к письмам
            if self.app.presence_of_element_located(Locators.welcome_modal):
                self.driver.close()
                self.driver.switch_to_window(self.driver.window_handles[0])
            else:
                print("Welcome_modal is not displayed!")
        except NoSuchElementException:
            return False and self.app.destroy()

    def check_mail_on_temp_mail(self):
        # Проверяем наличие писем и переходим к нему
        try:
            self.app.presence_of_element_located(Locators.mail_one)
            mail_act = self.driver.find_element(*Locators.mail_one)
            activation = mail_act.text
            mail_gift = self.driver.find_element(*Locators.mail_two)
            gift = mail_gift.text
            if activation == "Мы очень рады, что вы стали частью SPACEMIR!":
                self.driver.find_element(*Locators.mail_one).click()
            elif gift == "Мы очень рады, что вы стали частью SPACEMIR!":
                self.driver.find_element(*Locators.mail_two).click()
            else:
                self.driver.find_element(*Locators.btn_update)
                self.app.wait_on_element_text(Locators.mail_one, "Мы очень рады, что вы стали частью SPACEMIR!")
                self.driver.find_element(*Locators.mail_one).click()
        except NoSuchElementException:
            print(f"Mail activation is not found")
        btn_on_mail = self.driver.find_elements(*Locators.btn_on_letter)
        for mail in btn_on_mail:
            self.driver.execute_script("return arguments[0].scrollIntoView();", mail)
            mail.click()
            self.driver.switch_to_window(self.driver.window_handles[1])
            try:
                if "profile" in self.driver.current_url:
                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])
                elif "products" in self.driver.current_url:
                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])
                elif "catalog" in self.driver.current_url:
                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])
                elif "email-confirm" in self.driver.current_url:
                    self.app.wait_on_element_text(Locators.email_confirm,
                                                  "Поздравляем! Ваш аккаунт активирован, теперь вы можете публиковать свои объявления в общем доступе")
                    self.driver.close()
                    break
                else:
                    self.app.refresh()
                    self.app.presence_of_element_located(Locators.top_block_profile)
                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])
                    continue
            except StaleElementReferenceException:
                continue

    def check_and_activating_user(self):
        btn_on_mail = self.driver.find_elements(*Locators.btn_on_letter)
        for mail in btn_on_mail:
            self.driver.execute_script("return arguments[0].scrollIntoView();", mail)
            mail.click()
            self.driver.switch_to_window(self.driver.window_handles[1])
            try:
                if "profile" in self.driver.current_url:
                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])
                elif "products" in self.driver.current_url:
                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])
                elif "catalog" in self.driver.current_url:
                    self.driver.close()
                    self.driver.switch_to_window(self.driver.window_handles[0])
                elif "email-confirm" in self.driver.current_url:
                    self.app.wait_on_element_text(Locators.email_confirm,
                                                  "Поздравляем! Ваш аккаунт активирован, теперь вы можете публиковать свои объявления в общем доступе")
                    self.driver.close()
                    break
                else:
                    continue
            except StaleElementReferenceException:
                print("Not Found") and self.app.destroy()

    def Invalid_field_password(self):
        # Негативный тест на проверку заполенения полей < 6
        try:
            self.driver.find_element(*self.btn_submit_geo_position).click()
            field_reg = self.driver.find_elements(*self.form_signup_field)
            for fields in field_reg:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys('email@mail.ru')
                else:
                    fields.send_keys('12345')
            elem = self.driver.find_elements(*self.text_fail_field)
            for error in elem:
                if error.text == 'Минимальная длина поля 6, текущая длина 5':
                    continue
                elif error.text == 'As senhas não correspondem':
                    continue
            btn = self.driver.find_element(*self.btn_submit_signup)
            value = btn.get_attribute('disabled')
            if value == 'true':
                self.driver.refresh()
            else:
                print(value is None)
        except TimeoutException:
            print(f"element is not found")

    def Invalid_field_confirm_password(self):
        # Негативный тест на проверку заполенения полей
        try:
            field_reg = self.driver.find_elements(*self.form_signup_field)
            for fields in field_reg:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys('email@mail.ru')
                elif type_field == "password":
                    fields.send_keys('123456')
                elif type_field == "confirmPassword":
                    fields.send_keys('123')
            elem = self.driver.find_elements(*self.text_fail_password)
            for error in elem:
                if error.text == 'Пароли не совпадают':
                    continue
                elif error.text == 'As senhas não correspondem':
                    continue
                else:
                    print(error is None)
            btn = self.driver.find_element(*self.btn_submit_signup)
            value = btn.get_attribute('disabled')
            if value == 'true':
                self.driver.refresh()
            else:
                print(value is None)
        except TimeoutException:
            print(f"element is not found")

    def Invalid_mail_invalid_password(self):
        try:
            elem = self.driver.find_elements(*self.form_signup_field)
            x = random.choice(string.ascii_letters) * 101
            for fields in elem:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys('Sf_+48,/k@#')
                elif type_field == "password":
                    fields.send_keys(x)
                elif type_field == "confirmPassword":
                    fields.send_keys(x)
            elem = self.driver.find_elements(*self.text_fail_field)
            for error in elem:
                if error.text == 'Почта должна быть в виде mail@example.com':
                    continue
                elif error.text == 'Максимальная длина поля 100, текущая длина 101':
                    continue
                else:
                    print(error is None)
            btn = self.driver.find_element(*self.btn_submit_signup)
            value = btn.get_attribute('disabled')
            if value == 'true':
                self.driver.refresh()
            else:
                print(value is None)
        except TimeoutException:
            print(f"element is not found")

    def Fields_is_emprty(self):
        try:
            elem = self.driver.find_elements(*self.form_signup_field)
            text = random.choice(string.ascii_letters)
            for fields in elem:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys(text)
                    fields.send_keys('\b')
                elif type_field == "password":
                    fields.send_keys(text)
                    fields.send_keys('\b')
                elif type_field == "confirmPassword":
                    fields.send_keys(text)
                    fields.send_keys('\b')
                else:
                    print(type_field is None)
            elem = self.driver.find_elements(*self.text_fail_field)
            for error in elem:
                if error.text == 'Поле не может быть пустым':
                    continue
                elif error.text == 'Поле не может быть пустым':
                    continue
            btn = self.driver.find_element(*self.btn_submit_signup)
            value = btn.get_attribute('disabled')
            if value == 'true':
                self.driver.refresh()
            else:
                print(value is None)
        except TimeoutException:
            print(f"element is not found")

    def check_welcom_modal_and_log_out(self):
        try:
            if self.app.presence_of_element_located(Locators.welcome_modal):
                self.driver.find_element(*Locators.close_welcome_modal).click()
                self.driver.find_element(*Locators.btn_user).click()
                self.driver.find_element(*Locators.btn_logout).click()
            else:
                self.driver.find_element(*Locators.btn_user).click()
                self.driver.find_element(*Locators.btn_logout).click()
        except NoSuchElementException:
            return False

    def reg_for_exist_mail(self):
        try:
            btn_reg_form = self.driver.find_element(*self.tab_signup)
            btn_reg_form.click()
            field_auth = self.driver.find_elements(*self.form_signup_field)
            for fields in field_auth:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys(self.mail)
                elif type_field == "password":
                    fields.send_keys('123456')
                elif type_field == "confirmPassword":
                    fields.send_keys('123456')
            self.driver.find_element(*self.btn_submit_signup).click()
            error = self.driver.find_element(*self.text_fail_mail)
            text_fail = error.get_attribute('class')
            if text_fail == "text-failure ng-star-inserted":
                print(f"{{text_fail is present}}")
            self.driver.refresh()
        except ElementClickInterceptedException:
            print("ddddd")

    def registration_new_user(self):
        try:
            field_reg = self.driver.find_elements(*self.form_signup_field)
            for fields in field_reg:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys(self.mail)
                elif type_field == "password":
                    fields.send_keys('123456')
                elif type_field == "confirmPassword":
                    fields.send_keys('123456')
            btn = self.driver.find_element(*self.btn_submit_signup)
            btn.click()
        except ElementClickInterceptedException:
            print(ElementClickInterceptedException)

    def auth(self):
        self.app.open_sign_in_page()
        field_auth = self.driver.find_elements(*self.form_signup_field)
        for fields in field_auth:
            type_field = fields.get_attribute('formcontrolname')
            if type_field == "email":
                fields.send_keys(self.auth_mail)
            elif type_field == "password":
                fields.send_keys('123456')
        self.driver.find_element(*self.btn_submit_signin).click()
        if "profile" in self.driver.current_url:
            return True
        else:
            return False and self.app.destroy()

    def auth_fake_in_app(self):
        field_auth = self.driver.find_elements(*self.form_signup_field)
        for fields in field_auth:
            type_field = fields.get_attribute('formcontrolname')
            if type_field == "email":
                fields.send_keys(self.auth_mail)
            elif type_field == "password":
                fields.send_keys('123456')
        self.driver.find_element(*self.btn_submit_signin).click()
        if self.app.presence_of_element_located(self.text_fail_mail) and self.app.presence_of_element_located(
                self.toast_container):
            ele = self.driver.find_element(*self.text_fail_mail)
            text = ele.text
            print(text)
        else:
            return False and self.app.destroy()

    def log_out(self):
        try:
            # Ожидаем появления модалки приветствия и переходим к письмам
            if self.app.presence_of_element_located(Locators.welcome_modal):
                self.driver.find_element(*Locators.close_welcome_modal).click()
                self.driver.switch_to_window(self.driver.window_handles[0])
            else:
                print("Welcome_modal is not displayed!")
        except NoSuchElementException:
            return False and self.app.destroy()

    def void_and_send_mail_for_password_recovery(self):
        try:
            self.app.presence_of_element_located(self.email_field_signin)
            self.driver.find_element(*self.btn_recovery_mail).click()
            field = self.driver.find_element(*self.input_mail_recovery)
            field.send_keys(pyperclip.paste())
            btn_send = self.driver.find_element(*self.btn_send_recovery_mail)
            btn_disable = btn_send.get_attribute('disabled')
            if btn_disable != "true":
                btn_send.click()
        except ElementClickInterceptedException:
            return False

    def check_mail_recovery_on_delivery(self):
        try:
            self.driver.switch_to_window(self.driver.window_handles[0])
            self.app.presence_of_element_located(Locators.mail_one)
            mail = self.driver.find_element(*Locators.mail_one)
            recovery_mail = mail.text
            if recovery_mail == "Восстановление пароля":
                mail.click()
                btn = self.driver.find_element(*Locators.btn_recovery_on_mail)
                self.driver.execute_script("return arguments[0].scrollIntoView();", btn)
                btn.click()
            else:
                self.driver.find_element(*Locators.btn_update).click()
                self.app.presence_of_element_located(Locators.mail_one)
                if
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            new_pass = self.driver.find_elements(*self.form_signup_field)
            for fields in new_pass:
                fields.send_keys("string")
            btn_sum = self.driver.find_element(*self.btn_submit_change_password).click()
        except ElementClickInterceptedException:
            print(btn_sum, "not clicable")




