


def test_assert_started_site(spacemirfixture):
    spacemirfixture.open_main_page()
    # Проверка есть ли строка «Spacemir» в имени страницы
    assert "Spacemir" in spacemirfixture.driver.title
    # возвращает нам текущий url-адресс в строке
    assert spacemirfixture.space.assertion_main_page() == "http://test.spacemir.com/"
    spacemirfixture.space.click_submit_geo()
    # Проверяем наличие кнопки "Войти" в шапке
    assert spacemirfixture.space.assertion_button_log_in()
    # Проверяем наличие кнопки "Регистрация" в шапке
    assert spacemirfixture.space.assertion_button_registration()
    print('TestPassed')
    spacemirfixture.destroy()


def test_assert_check_country_and_city(spacemirfixture):
    spacemirfixture.open_main_page()
    # Проверка есть ли заголовок «Spacemir» в имени страницы
    assert "Spacemir" in spacemirfixture.driver.title
    # возвращает нам текущий url-адресс в строке
    assert spacemirfixture.space.assertion_main_page() == "http://test.spacemir.com/"
    spacemirfixture.space.void_name_countries('Россия')
    spacemirfixture.space.click_name_countries()
    spacemirfixture.space.void_name_city('Москва')
    spacemirfixture.space.click_name_city()
    spacemirfixture.space.click_submit_geo()
    spacemirfixture.
    print('TestPassed')


def test_auth_profile(spacemirfixture):
    spacemirfixture.open_sign_page()
    assert spacemirfixture.space.assertion_page_auth() == "http://test.spacemir.com/account/signin"
    spacemirfixture.space.click_submit_geo()
    spacemirfixture.auth.enter_email_field('1@1.ru')
    spacemirfixture.auth.enter_password("string")
    spacemirfixture.auth.click_login()
    spacemirfixture.profile.click_button_profile()
    spacemirfixture.profile.click_button_log_out()
    assert spacemirfixture.space.assertion_page_auth() == "http://test.spacemir.com/account/signin"
    print('TestPassed')



