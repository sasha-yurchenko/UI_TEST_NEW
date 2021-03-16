from Data.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    ScreenshotException
from selenium.webdriver.common.keys import Keys
import os


class ConstructPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        # Селекты
        self.main_category = Locators.select_main_category
        self.nested_category = Locators.select_nested_category
        self.google_search = Locators.input_google_country
        self.category_path = Locators.category_path
        self.change_link = Locators.change_link
        self.tab_sale = Locators.tab_sale
        self.tab_sell = Locators.tab_sell
        self.input_google_country = Locators.input_google_country
        self.list_country = Locators.list_country
        self.name_contry_list = Locators.name_contry_list
        self.select_multiselect_wrap = Locators.select_multiselect_wrap
        self.constructor_body = Locators.constructor_body
        self.value_in_dropdown_select = Locators.value_in_dropdown_select
        self.value_in_dropdown_multi_select = Locators.value_in_dropdown_multi_select
        self.discription_in_const = Locators.discription_in_const
        self.select_geo_phone = Locators.select_geo_phone
        self.price_range = Locators.price_range
        self.checkbox_const = Locators.checkbox_const
        # Инпуты
        self.price_range = Locators.price_range
        self.input_google_country = Locators.input_google_country
        self.input_construct = Locators.input_construct
        self.price_input = Locators.price_input
        self.input_phone_invalid = Locators.input_phone_invalid
        self.input_range = Locators.input_range
        # Кнопки
        self.radio_btn = Locators.radio_btn
        self.btn_photo = Locators.btn_photo
        self.btn_public = Locators.button_publication
        self.btn_draft = Locators.button_draft
        self.btn_photo = Locators.btn_photo

    def create_new_product(self, country):
        try:
            self.driver.find_element(*Locators.add_product_button).click()
            self.app.presence_of_element_located(*self.main_category)
            self.driver.find_element(*self.main_category).click()
            self.driver.find_element(*self.nested_category).click()
            self.app.presence_of_element_located(*self.category_path)
            self.app.presence_of_element_located(*self.change_link)
            self.driver.find_element(*self.input_google_country).clear()
            self.driver.find_element(*self.input_google_country).send_keys(country)
            self.app.text_to_be_present_in_element(*self.name_contry_list), 'Бразилия'
            self.driver.find_element(*self.list_country).click()
            self.driver.find_element(*self.btn_public).click()
            return True
        except TimeoutException:
            return False and self.app.destroy()

    def choosing_value_in_constructor(self):
        call_select = self.driver.find_elements(*self.select_multiselect_wrap)
        for select in call_select:
            self.driver.execute_script("return arguments[0].scrollIntoView();", select)
            try:
                select.click()
            except ElementClickInterceptedException:
                continue
            try:
                if self.driver.find_element(*self.value_in_dropdown_select).is_displayed():
                    self.driver.find_element(*self.value_in_dropdown_select).click()
                    print("it's element select")
            except NoSuchElementException:
                self.driver.find_element(*self.value_in_dropdown_multi_select).click()
                select.click()
                print("it's element multi select")
        void_input = self.driver.find_elements(*self.input_construct)
        if len(void_input) > 0:
            for void in void_input:
                self.driver.execute_script("return arguments[0].scrollIntoView();", void)
                void.send_keys("123")
        check_box = self.driver.find_elements(*self.checkbox_const)
        if len(check_box) > 0:
            for value in check_box:
                self.driver.execute_script("return arguments[0].scrollIntoView();", value)
                value.click()
        radio_btn = self.driver.find_elements(*self.radio_btn)
        if len(radio_btn) > 0:
            for check in radio_btn:
                self.driver.execute_script("return arguments[0].scrollIntoView();", check)
                check.click()
        range_price = self.driver.find_elements(*self.price_range)
        if len(range_price) > 0:
            for range in range_price:
                self.driver.execute_script("return arguments[0].scrollIntoView();", range)
                range.send_keys('22')
        range_input = self.driver.find_elements(*self.input_range)
        if len(range_input) > 0:
            for ran in range_input:
                self.driver.execute_script("return arguments[0].scrollIntoView();", ran)
                ran.send_keys('555')
        add_photo = self.driver.find_element(*self.btn_photo)
        if add_photo.is_displayed():
            current_dir = self.app.path()
            file_path = os.path.join(current_dir, '4.jpg')  # добавляем к этому пути имя файла
            add_photo.send_keys(file_path)
