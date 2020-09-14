from Locators.locators import Locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    ScreenshotException
from selenium.webdriver.common.keys import Keys
import os
import autoit


class ConstructPage:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.main_category = Locators.select_main_category
        self.nested_category = Locators.select_nested_category
        self.google_search = Locators.input_google_country

    def create_new_product(self, country):
        try:
            self.driver.find_element(*Locators.add_product_button).click()
            self.app.presence_of_element_located(*Locators.select_main_category)
            self.driver.find_element(*Locators.select_main_category).click()
            self.driver.find_element(*Locators.select_nested_category).click()
            self.app.presence_of_element_located(*Locators.category_path)
            self.app.presence_of_element_located(*Locators.change_link)
            self.driver.find_element(*Locators.input_google_country).clear()
            self.driver.find_element(*Locators.input_google_country).send_keys(country)
            self.app.text_to_be_present_in_element(*Locators.name_contry_list), 'Бразилия'
            self.driver.find_element(*Locators.list_country).click()
            self.driver.find_element(*Locators.button_publication).click()
            return True
        except TimeoutException:
            return False and self.app.destroy()

    def choosing_value_in_constructor(self):
        call_select = self.driver.find_elements(*Locators.select_multiselect_wrap)
        for select in call_select:
            self.driver.execute_script("return arguments[0].scrollIntoView();", select)
            try:
                select.click()
            except ElementClickInterceptedException:
                continue
            try:
                if self.driver.find_element(*Locators.value_in_dropdown_select).is_displayed():
                    self.driver.find_element(*Locators.value_in_dropdown_select).click()
                    print("it's element select")
            except NoSuchElementException:
                self.driver.find_element(*Locators.value_in_dropdown_multi_select).click()
                select.click()
                print("it's element multi select")
        void_input = self.driver.find_elements(*Locators.input_construct)
        if len(void_input) > 0:
            for void in void_input:
                self.driver.execute_script("return arguments[0].scrollIntoView();", void)
                void.send_keys("123")
        check_box = self.driver.find_elements(*Locators.checkbox_const)
        if len(check_box) > 0:
            for value in check_box:
                self.driver.execute_script("return arguments[0].scrollIntoView();", value)
                value.click()
        radio_btn = self.driver.find_elements(*Locators.radio_btn)
        if len(radio_btn) > 0:
            for check in radio_btn:
                self.driver.execute_script("return arguments[0].scrollIntoView();", check)
                check.click()
        range_price = self.driver.find_elements(*Locators.price_range)
        if len(range_price) > 0:
            for range in range_price:
                self.driver.execute_script("return arguments[0].scrollIntoView();", range)
                range.send_keys('22')
        range_input = self.driver.find_elements(*Locators.input_range)
        if len(range_input) > 0:
            for ran in range_input:
                self.driver.execute_script("return arguments[0].scrollIntoView();", ran)
                ran.send_keys('555')
        add_photo = self.driver.find_element(*Locators.btn_photo)
        if add_photo.is_displayed():
            current_dir = self.app.path()
            file_path = os.path.join(current_dir, '4.jpg')  # добавляем к этому пути имя файла
            add_photo.send_keys(file_path)
