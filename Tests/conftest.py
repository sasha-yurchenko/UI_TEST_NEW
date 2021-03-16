import pytest
from selenium import webdriver
from Pages.BasePage import App
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import random


#  Создаем декоратор pytest.fixture
@pytest.fixture(scope="session")
def bases_fixture(request):
    app = App() # Создаем из класса объект.
    yield app  # Разделяет исполняемую часть от завершающей
    app.destroy()  # Вызывает функцию, которая у нас останавливает работу браузера и вебдрайвера.


@pytest.fixture(params=["chrome", "firefox"], scope='session')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.maximize_window()
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        web_driver.maximize_window()
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()


@pytest.fixture()
def GenKey():
    array = [chr(i) for i in range(65, 91)]
    # список array = ['A', 'B', 'C' ... 'Z']
    random.shuffle(array)
    key = ""
    for i in range(5):  # length of key
        key += array.pop()
    return key
