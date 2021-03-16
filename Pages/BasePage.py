from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from Pages.LoginPage import LoginPage
from Pages.ProfilePage import ProfilePage
from Pages.ProductsPage import ProductsPage
from Pages.MainHeader import Header
from Pages.ConfirmGeoModal import GeoModal
from Pages.ConsturctPage import ConstructPage
from Data.All_links import Links
import os
import random
import pytest


class App:

    def __init__(self):
        self.driver = webdriver.Chrome()
        # browser_options_firefox = self.browser_options_firefox(options='web_enabled')
        # self.driver = webdriver.Firefox(firefox_options=browser_options_firefox)
        self.auth = LoginPage(self)
        self.profile = ProfilePage(self)
        self.product = ProductsPage(self)
        self.head = Header(self)
        self.geo = GeoModal(self)
        self.constructor = ConstructPage(self)
        self.links = Links()
        self.driver.implicitly_wait(10)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    # Ожидание проверки наличия элемента в DOM страницы.
    def element_expected_conditions(self, method, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((method, locator)))

    # Ожидание проверки наличия хотя бы одного элементана веб-странице.
    def visibility_element_expected_conditions(self, element):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of(element)))

    # Ожидание для проверки элемента, является ли видимым и включается так, что вы можете нажать на нее.
    def element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until((EC.element_to_be_clickable(locator)))

    def element_to_be_not_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until_not((EC.element_to_be_clickable(locator)))

    # Ожидание проверки наличия данного текста в указанном элементе.
    def wait_on_element_text(self, locator, text_):
        return WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(locator, text_))

    # Ожидание для проверки, присутствует ли данный текст в элементе
    def wait_on_element_text_value(self, locator, value):
        return WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_value(locator, value))

    # Ожидание проверки наличия элемента в DOM страницы. Это не обязательно означает, что элемент виден.
    def presence_of_element_located(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

    def visibility_of_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(locator))

    # Метод open_main_page открывает главную страницу сайта
    def open_main_page(self):
        driver = self.driver
        driver.get(self.links.page_main)

    def open_temp_mail(self):
        driver = self.driver
        driver.get(self.links.page_temp_mail)

    def open_sign_in_page(self):
        driver = self.driver
        driver.get()
        assert "signin" in driver.current_url

    def open_restore_password_page(self):
        driver = self.driver
        driver.get(self.links.page_restore_password)
        assert "restore" in driver.current_url

    def open_sign_up_page(self):
        driver = self.driver
        driver.get(self.links.page_sign_up)
        assert "signup" in driver.current_url

    def open_ad_page(self, url_products):
        driver = self.driver
        driver.get(url_products)

    # Данный метод закрывает веб-браузер и завершает процесс вебдрайвера.
    def destroy(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def execute_script_window_open(self, page):
        return self.driver.execute_script('''window.open("''' + str(page) + '''");''')

    def switch_to_window_1(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])

    @staticmethod
    def GenKey():
        array = [chr(i) for i in range(65, 91)]
        # список array = ['A', 'B', 'C' ... 'Z']
        random.shuffle(array)
        key = ""
        for i in range(5):  # length of key
            key += array.pop()
        return key

    @staticmethod
    def path():
        return os.path.abspath(os.path.dirname('D:\Projects Spacemir V2\sm-test\Tests'))

    @staticmethod
    def browser_options_chrome(option):
        chrome_options = webdriver.ChromeOptions()
        if option == 'headless':
            chrome_options.add_argument('--headless')
            return chrome_options
        elif option == 'start-maximized':
            chrome_options.add_argument('--kiosk')
            return chrome_options

    @staticmethod
    def browser_options_firefox(options):
        firefox_options = webdriver.FirefoxOptions()
        if options == 'web_enabled':
            firefox_options.set_preference('dom.webdriver.enabled', False)
            firefox_options.set_preference('dom.webnotifications.enables', False)
            firefox_options.headless = True
            return firefox_options
