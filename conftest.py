import pytest
from Application.SpacemirApp import App


#  Создаем декоратор pytest.fixture
@pytest.fixture(scope="session")
def spacemirfixture():
    app = App()  # Создаем из класса объект.
    yield app  # Разделяет исполняемую часть от завершающей
    app.destroy()  # Вызывает функцию, которая у нас останавливает работу браузера и вебдрайвера.
