def test_assert_started_site(spacemirfixture):
    spacemirfixture.open_main_page()
    # Проверка есть ли строка «Spacemir» в имени страницы
    assert "Spacemir" in spacemirfixture.driver.title
    # возвращает нам текущий url-адресс в строке
    assert spacemirfixture.space.assertion_main_page() == "https://t-front.spacemir.com/"
    spacemirfixture.geo.click_submit_geo_position()
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
    assert spacemirfixture.space.assertion_main_page() == "https://t-front.spacemir.com/"
    spacemirfixture.geo.click_choose_another_country()
    spacemirfixture.geo.country_selection('Бразилия', 'São Paulo')
    assert spacemirfixture.geo.assert_name_geo('São Paulo')
    spacemirfixture.head.click_button_login_header()
    spacemirfixture.auth.auth('1@1.ru', '12345678')
    spacemirfixture.auth.check_text_fail_auth()
    print('TestPassed')


def test_auth_profile(spacemirfixture):
    spacemirfixture.open_sign_page()
    assert spacemirfixture.space.assertion_page_auth() == "https://t-front.spacemir.com/account/signin"
    spacemirfixture.geo.click_submit_geo_position()
    spacemirfixture.auth.auth('1@1.ru', '123456')
    spacemirfixture.auth.click_login()
    assert spacemirfixture.profile.check_exists_profile_elements()
    spacemirfixture.profile.click_button_profile()
    spacemirfixture.profile.click_button_log_out()
    print('TestPassed')


def test_assert_ad_page(spacemirfixture):
    spacemirfixture.open_sign_page()
    spacemirfixture.geo.click_choose_another_country()
    spacemirfixture.geo.country_selection('Бразилия', 'Rio')
    # assert spacemirfixture.geo.assert_name_country_header('')
    spacemirfixture.auth.auth('1@1.ru', '123456')
    spacemirfixture.auth.click_login()
    assert spacemirfixture.profile.check_exists_profile_elements()
    spacemirfixture.open_ad_page('https://t-front.spacemir.com/products/5c24c083384fa011c82aa0a7?countryGeoCode=BR')
    assert spacemirfixture.product.tab_exist_product_page()
    assert spacemirfixture.product.check_availability_elements_on_short_card()


def test_new_registration(spacemirfixture):
    spacemirfixture.open_main_page()
    spacemirfixture.geo.click_submit_geo_position()
    spacemirfixture.main_page.check_elements_on_main_page()
    spacemirfixture.head.click_button_login_header()
    spacemirfixture.auth.auth('1@1.ru', '123456')
    spacemirfixture.auth.click_login()
    assert spacemirfixture.profile.check_exists_profile_elements()
    spacemirfixture.constructor.create_new_product('Sao')
    spacemirfixture.constructor.choosing_value_in_select()

