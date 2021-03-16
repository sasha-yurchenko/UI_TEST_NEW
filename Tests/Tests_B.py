import pytest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    browser.get(link)


def test_A2_A3_A4_A5_A6(bases_fixture):
    bases_fixture.open_sign_up_page()
    bases_fixture.geo.click_submit_geo_position()
    bases_fixture.auth.Invalid_field_password()
    bases_fixture.auth.Invalid_field_confirm_password()
    bases_fixture.auth.Invalid_mail_invalid_password()
    bases_fixture.auth.Fields_is_emprty()
    bases_fixture.auth.registration_new_user()
    bases_fixture.auth.check_welcom_modal_and_log_out()
    bases_fixture.auth.reg_for_exist_mail()


def test_B1(bases_fixture):
    bases_fixture.open_sign_up_page()
    bases_fixture.geo.click_submit_geo_position()
    bases_fixture.auth.registration_new_user()
    bases_fixture.open_sign_up_page()
    bases_fixture.auth.auth()


def test_B2(bases_fixture):
    bases_fixture.open_sign_in_page()
    bases_fixture.geo.click_submit_geo_position()
    bases_fixture.auth.auth_fake_in_app()


def test_C1(bases_fixture):
    bases_fixture.auth.receiving_mail()
    bases_fixture.auth.creation_user()
    bases_fixture.auth.check_welcom_modal_and_log_out()
    bases_fixture.auth.void_and_send_mail_for_password_recovery()
    bases_fixture.auth.check_mail_recovery_on_delivery()
    bases_fixture.auth.Fill_in_the_fields_for_password_recovery()


def test_C2(bases_fixture):
    bases_fixture.open_restore_password_page()
    bases_fixture.geo.click_submit_geo_position()
    bases_fixture.auth.checking_error_output_restore()


def test_open(bases_fixture):
    bases_fixture.open_main_page()
