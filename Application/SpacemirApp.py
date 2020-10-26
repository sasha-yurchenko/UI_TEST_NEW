from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

from Pages.LoginPage import LoginPage
from Pages.ProfilePage import ProfilePage
from Pages.ProductsPage import ProductsPage
from Pages.MainHeader import Header
from Pages.SmConfirmGeoModal import GeoModal
from Pages.MainPage import MainPage
from Pages.ConsturctPage import ConstructPage
from selenium.webdriver.common.action_chains import ActionChains
import os
import random


# инициализируем наш веб-драйвер и делаем из классов объекты страниц.


class App:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.auth = LoginPage(self)
        self.profile = ProfilePage(self)
        self.product = ProductsPage(self)
        self.head = Header(self)
        self.geo = GeoModal(self)
        self.main_page = MainPage(self)
        self.constructor = ConstructPage(self)
        self.driver.implicitly_wait(20)

    # Методы ожидания

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
        driver.get('https://t-front.spacemir.com/')

    def open_temp_mail(self):
        driver = self.driver
        driver.get('https://temp-mail.org/ru')

    def open_sign_page(self):
        driver = self.driver
        driver.get('https://t-front.spacemir.com/account/signin')
        assert "signin" in driver.current_url

    def open_sign_up_page(self):
        driver = self.driver
        driver.get('https://t-front.spacemir.com/account/signup')
        assert "signup" in driver.current_url

    def open_ad_page(self, url_products):
        driver = self.driver
        driver.get(url_products)

    # Данный метод закрывает веб-браузер и завершает процесс вебдрайвера.
    def destroy(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

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
    def browser_options(options):
        chrome_options = webdriver.ChromeOptions()
        if options == 'headless':
            chrome_options.add_argument('--headless')
            return chrome_options
        elif options == 'start-maximized':
            chrome_options.add_argument('--kiosk')
            return chrome_options
