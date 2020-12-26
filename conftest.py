import pytest
from Application.SpacemirApp import App
from playwright import sync_playwright


#  Создаем декоратор pytest.fixture
@pytest.fixture(scope="session")
def sm_2_fixture():
    app = App()  # Создаем из класса объект.
    yield app  # Разделяет исполняемую часть от завершающей
    app.destroy()  # Вызывает функцию, которая у нас останавливает работу браузера и вебдрайвера.


@pytest.fixture
def browser():
    pw_context = sync_playwright()
    pw = pw_context.__enter__()
    browser = getattr(pw, "chromium").connect(wsEndpoint='wss://chrome.headlesstesting.com?token=[YOUR-TOKEN]')
    browser._close = browser.close
