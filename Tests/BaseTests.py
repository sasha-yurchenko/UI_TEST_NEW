def test_assert_check_country_and_city(sm_2_fixture):
    sm_2_fixture.open_main_page()
    # Проверка есть ли заголовок «Spacemir» в имени страницы
    assert "Spacemir" in sm_2_fixture.driver.title
    # возвращает нам текущий url-адресс в строке
    assert sm_2_fixture.main_page.assertion_main_page() == "https://t-front.spacemir.com/"
    sm_2_fixture.geo.country_selection('São Paulo')
    print('TestPassed')


def test_auth_profile(sm_2_fixture):
    sm_2_fixture.open_sign_page()
    assert sm_2_fixture.space.assertion_page_auth() == "https://t-front.spacemir.com/account/signin"
    sm_2_fixture.geo.click_submit_geo_position()
    sm_2_fixture.auth.auth('1@1.ru', '123456')
    assert sm_2_fixture.profile.check_exists_profile_elements()
    sm_2_fixture.profile.click_button_profile()
    sm_2_fixture.profile.click_button_log_out()
    print('TestPassed')


def test_assert_ad_page(sm_2_fixture):
    sm_2_fixture.open_sign_page()
    sm_2_fixture.geo.click_choose_another_country()
    sm_2_fixture.geo.country_selection('Бразилия', 'Rio')
    # assert sm_2_fixture.geo.assert_name_country_header('')
    sm_2_fixture.auth.auth('1@1.ru', '123456')
    assert sm_2_fixture.profile.check_exists_profile_elements()
    sm_2_fixture.open_ad_page('https://t-front.spacemir.com/products/5c24c083384fa011c82aa0a7?countryGeoCode=BR')
    assert sm_2_fixture.product.tab_exist_product_page()
    assert sm_2_fixture.product.check_availability_elements_on_short_card()


def test_new_registration(sm_2_fixture):
    sm_2_fixture.open_main_page()
    sm_2_fixture.geo.click_submit_geo_position()
    sm_2_fixture.main_page.check_elements_on_main_page()
    sm_2_fixture.head.click_button_login_header()
    sm_2_fixture.auth.auth('1@1.ru', '123456')
    sm_2_fixture.auth.click_login()
    assert sm_2_fixture.profile.check_exists_profile_elements()
    sm_2_fixture.constructor.create_new_product('Sao')
    sm_2_fixture.constructor.choosing_value_in_constructor()

