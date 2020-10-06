from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException, \
    StaleElementReferenceException
import pyperclip


class LoginPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.email_field_css_selector = Locators.email_field_signin
        self.password_field_css_selector = Locators.password_field_signin
        self.login_button_xpath = Locators.login_button
        self.text_fail_auth_xpath = Locators.text_fail_auth

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

    def receiving_mail(self):
        try:
            # Получаем новую почту и регистрируемся в системе
            self.app.open_temp_mail()
            button = self.app.element_to_be_clickable(Locators.btn_copy_mail)
            button.click()
            self.app.wait_on_element_text(Locators.copy_mail, "Скопировано")
            self.driver.execute_script("window.open('https://t-front.spacemir.com/account/signin', 'new_window')")
            self.driver.execute_script("window.open('https://t-front.spacemir.com/account/signin', 'new_window')")
            self.driver.switch_to_window(self.driver.window_handles[1])
            assert "signin" in self.driver.current_url
            self.driver.find_element(*Locators.button_submit_geo_position).click()
            self.driver.find_element(*Locators.tab_signup).click()
        except NoSuchElementException:
            print("Not Found") and self.app.destroy()

    def creation_user(self):
        try:
            field_reg = self.driver.find_elements(*Locators.form_signup_field)
            for fields in field_reg:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys(pyperclip.paste())
                else:
                    fields.send_keys('123456')
            self.driver.find_element(*Locators.btn_submit_signup).click()
            # Ожидаем появления модалки приветствия и переходим к письмам
            if self.app.presence_of_element_located(Locators.welcome_modal):
                self.driver.close()
                self.driver.switch_to_window(self.driver.window_handles[0])
            else:
                print("Welcome_modal is not displayed!") and self.app.destroy()
            # Проверяем наличие писем и переходим к нему
            try:
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
                print(f"Mail activation is not found") and self.app.destroy()
        except ElementClickInterceptedException:
            self.app.destroy()

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
                    print("Activation is succesfull")
            except StaleElementReferenceException:
                print("Not Found") and self.app.destroy()

    def fill_in_reg_fields(self):
        try:
            self.app.open_sign_up_page()
            self.driver.find_element(*Locators.button_submit_geo_position).click()
            field_reg = self.driver.find_elements(*Locators.form_signup_field)
            for fields in field_reg:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys('email@mail.ru')
                else:
                    fields.send_keys('12345')
            elem = self.driver.find_elements(*Locators.text_fail_field_length)
            for error in elem:
                if error.text == 'Минимальная длина поля 6, текущая длина 5':
                    continue
            btn = self.driver.find_element(*Locators.btn_submit_signup)
            value = btn.get_attribute('disabled')
            if value == 'true':
                self.driver.refresh()
            else:
                print(value is None)
            field_reg = self.driver.find_elements(*Locators.form_signup_field)
            for fields in field_reg:
                type_field = fields.get_attribute('formcontrolname')
                if type_field == "email":
                    fields.send_keys('email@mail.ru')
                elif type_field == "password":
                    fields.send_keys('123456')
                elif type_field == "confirmPassword":
                    fields.send_keys('123')
        except ElementClickInterceptedException:
            print("ddddd")

    #     def registration(self):
    #         try:
    #             # Получаем новую почту и регистрируемся в системе
    #             self.app.open_temp_mail()
    #             button = self.app.element_to_be_clickable(Locators.btn_copy_mail)
    #             button.click()
    #             self.app.wait_on_element_text(Locators.copy_mail, "Скопировано")
    #             self.driver.execute_script("window.open('https://t-front.spacemir.com/account/signin', 'new_window')")
    #             self.driver.switch_to_window(self.driver.window_handles[1])
    #             assert "signin" in self.driver.current_url
    #             self.driver.find_element(*Locators.button_submit_geo_position).click()
    #             self.driver.find_element(*Locators.tab_signup).click()
    #             field_reg = self.driver.find_elements(*Locators.form_signup_field)
    #             for fields in field_reg:
    #                 type_field = fields.get_attribute('formcontrolname')
    #                 if type_field == "email":
    #                     fields.send_keys(pyperclip.paste())
    #                 else:
    #                     fields.send_keys('123456')
    #             self.driver.find_element(*Locators.btn_submit_signup).click()
    #             # Ожидаем появления модалки приветствия и переходим к письмам
    #             if self.app.presence_of_element_located(Locators.welcome_modal):
    #                 self.driver.close()
    #                 self.driver.switch_to_window(self.driver.window_handles[0])
    #             else:
    #                 print("Welcome_modal is not displayed!") and self.app.destroy()
    #             # Проверяем наличие писем и переходим к нему
    #             try:
    #                 if self.app.wait_on_element_text(Locators.mail_one, "Мы очень рады, что вы стали частью SPACEMIR!"):
    #                     self.driver.find_element(*Locators.mail_one).click()
    #                 elif self.app.wait_on_element_text(Locators.mail_two, "Мы очень рады, что вы стали частью SPACEMIR!"):
    #                     self.driver.find_element(*Locators.mail_one).click()
    #                 else:
    #                     self.driver.find_element(*Locators.btn_update)
    #                     self.app.wait_on_element_text(Locators.mail_one, "Мы очень рады, что вы стали частью SPACEMIR!")
    #                     self.driver.find_element(*Locators.mail_one).click()
    #             except NoSuchElementException:
    #                 print(f"Mail activation is not found") and self.app.destroy()
    #             # Проверяем наличие кнопок в письме и переходим по ним
    #             btn_on_mail = self.driver.find_elements(*Locators.btn_on_letter)
    #             for mail in btn_on_mail:
    #                 self.driver.execute_script("return arguments[0].scrollIntoView();", mail)
    #                 mail.click()
    #                 self.driver.switch_to_window(self.driver.window_handles[1])
    #                 try:
    #                     if "profile" in self.driver.current_url:
    #                         self.driver.close()
    #                         self.driver.switch_to_window(self.driver.window_handles[0])
    #                     elif "products" in self.driver.current_url:
    #                         self.driver.close()
    #                         self.driver.switch_to_window(self.driver.window_handles[0])
    #                     elif "catalog" in self.driver.current_url:
    #                         self.driver.close()
    #                         self.driver.switch_to_window(self.driver.window_handles[0])
    #                     elif "email-confirm" in self.driver.current_url:
    #                         self.app.wait_on_element_text(Locators.email_confirm,
    #                                                       "Поздравляем! Ваш аккаунт активирован, теперь вы можете публиковать свои объявления в общем доступе")
    #                         self.driver.close()
    #                         break
    #                     else:
    #                         print("Activation is succesfull")
    #                 except NoSuchElementException:
    #                     print("Not Found") and self.app.destroy()
    #         except TimeoutException:
    #             print("Not Found") and self.app.destroy()
