from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.SpaceMainPage import SpaceMainHelper
from Pages.LoginPage import LoginPage
from Pages.ProfilePage import ProfilePage
from Pages.ProductsPage import ProductsPage


# инициализируем наш веб-драйвер и делаем из классов объекты страниц.
class App:

    def __init__(self):
        browser_options = self.browser_options(options='start-maximized')
        self.driver = webdriver.Chrome(chrome_options=browser_options)
        self.space = SpaceMainHelper(self)
        self.auth = LoginPage(self)
        self.profile = ProfilePage(self)
        self.product = ProductsPage(self)
        self.driver.implicitly_wait(5)

    def element_expected_conditions(self, method, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((method, locator)))

    def visibility_element_expected_conditions(self, element):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of(element))

    def element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    def text_to_be_present_in_element(self):

    # Метод open_auth_page открывает главную страницу сайта
    def open_main_page(self):
        driver = self.driver
        driver.get('http://test.spacemir.com')

    def open_sign_page(self):
        driver = self.driver
        driver.get('http://test.spacemir.com/account/signin')

    # Данный метод закрывает веб-браузер и завершает процесс вебдрайвера.
    def destroy(self):
        self.driver.quit()

    @staticmethod
    def browser_options(options):
        chrome_options = webdriver.ChromeOptions()
        if options == 'headless':
            chrome_options.add_argument('--headless')
            return chrome_options
        elif options == 'start-maximized':
            chrome_options.add_argument('--start-maximized')
            return chrome_options
