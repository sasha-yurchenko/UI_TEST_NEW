from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.SpaceMainPage import SpaceMainHelper
from Pages.LoginPage import LoginPage
from Pages.ProfilePage import ProfilePage
from Pages.ProductsPage import ProductsPage
from Pages.MainHeader import Header
from Pages.SmConfirmGeoModal import GeoModal
from Pages.MainPage import MainPage
from Pages.ConsturctPage import ConstructPage
from selenium.webdriver.common.action_chains import ActionChains


# инициализируем наш веб-драйвер и делаем из классов объекты страниц.


class App:

    def __init__(self):
        browser_options = self.browser_options(options='start-maximized')
        self.driver = webdriver.Chrome(chrome_options=browser_options)
        self.space = SpaceMainHelper(self)
        self.auth = LoginPage(self)
        self.profile = ProfilePage(self)
        self.product = ProductsPage(self)
        self.head = Header(self)
        self.geo = GeoModal(self)
        self.main_page = MainPage(self)
        self.constructor = ConstructPage(self)
        self.driver.implicitly_wait(2)

    # Методы ожидания

    # Ожидание проверки наличия элемента в DOM страницы.
    def element_expected_conditions(self, method, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((method, locator)))

    # Ожидание проверки наличия хотя бы одного элементана веб-странице.
    def visibility_element_expected_conditions(self, element):
        return WebDriverWait(self.driver, 8).until(EC.visibility_of(element))

    # Ожидание для проверки элемента, является ли видимым и включается так, что вы можете нажать на нее.
    def element_to_be_clickable(self, element):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(element))

    # Ожидание проверки наличия данного текста в указанном элементе.
    def text_to_be_present_in_element(self, locator, text_):
        return WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(locator, text_))

    # Ожидание для проверки, присутствует ли данный текст в элементе
    def text_to_be_present_in_element_value(self, locator, text_):
        return WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(locator, text_))

    # Ожидание проверки наличия элемента в DOM страницы. Это не обязательно означает, что элемент виден. Локатор - используется для поиска элемента возвращает WebElement после его нахождения
    def presence_of_element_located(self, locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    # Метод open_main_page открывает главную страницу сайта
    def open_main_page(self):
        driver = self.driver
        driver.get('https://t-front.spacemir.com/')

    def open_sign_page(self):
        driver = self.driver
        driver.get('https://t-front.spacemir.com/account/signin')

    def open_ad_page(self, url_products):
        driver = self.driver
        driver.get(url_products)

    # Данный метод закрывает веб-браузер и завершает процесс вебдрайвера.
    def destroy(self):
        self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    @staticmethod
    def browser_options(options):
        chrome_options = webdriver.ChromeOptions()
        if options == 'headless':
            chrome_options.add_argument('--headless')
            return chrome_options
        elif options == 'start-maximized':
            chrome_options.add_argument('--start-maximized')
            return chrome_options
