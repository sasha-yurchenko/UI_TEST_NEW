
def test_assert_started_site(spacemirfixture):
    spacemirfixture.open_main_page()
    # Проверка есть ли строка «Spacemir» в имени страницы
    assert "Spacemir" in spacemirfixture.driver.title
    # возвращает нам текущий url-адресс в строке
    assert spacemirfixture.space.assertion_main_page() == "http://test.spacemir.com/"
    spacemirfixture.geo.click_submit_geo()
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
    assert spacemirfixture.space.assertion_main_page() == "https://test.spacemir.com/"
    spacemirfixture.geo.void_name_countries('Россия')
    spacemirfixture.geo.click_name_countries()
    spacemirfixture.geo.void_name_city('Москва')
    spacemirfixture.geo.click_name_city()
    spacemirfixture.geo.click_submit_geo()
    spacemirfixture.geo.assert_name_geo()
    spacemirfixture.head.click_button_login_header()
    spacemirfixture.auth.enter_email_field('1@1.ru')
    spacemirfixture.auth.enter_password("string")
    spacemirfixture.auth.click_login()
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
    print('TestPassed')


def test_assert_ad_page(spacemirfixture):
    spacemirfixture.open_ad_page()
    spacemirfixture.space.click_submit_geo()
    # Проверка наличия таба на странице выдачи "Продать"
    spacemirfixture.product.tab_for_sale()
    # Првоерка наличия кнопки "Показать телефон"
    spacemirfixture.product.button_number_wait()
    spacemirfixture.product.choice_filter_marks()
    spacemirfixture.product.click_search_element()
    spacemirfixture.product.void_search_marks('niss')
    spacemirfixture.product.check_value()
    spacemirfixture.product.close_filter_drop_down()
    # Проверка марки машины в заголовке объявления
    spacemirfixture.product.check_value_on_title()

