def test_A1(sm_2_fixture):
    sm_2_fixture.auth.receiving_mail()
    sm_2_fixture.auth.creation_user()
    sm_2_fixture.auth.check_and_wait_welcome_modal()
    sm_2_fixture.auth.check_mail_on_temp_mail()


def test_A2_A3_A4_A5_A6(sm_2_fixture):
    sm_2_fixture.open_sign_up_page()
    sm_2_fixture.auth.Invalid_field_password()
    sm_2_fixture.auth.Invalid_field_confirm_password()
    sm_2_fixture.auth.Invalid_mail_invalid_password()
    sm_2_fixture.auth.Fields_is_emprty()
    sm_2_fixture.auth.registration_new_user()
    sm_2_fixture.auth.check_welcom_modal_and_log_out()
    sm_2_fixture.auth.reg_for_exist_mail()


def test_B1(sm_2_fixture):
    sm_2_fixture.open_sign_up_page()
    sm_2_fixture.geo.click_submit_geo_position()
    sm_2_fixture.auth.registration_new_user()
    sm_2_fixture.auth.auth()


def test_B2(sm_2_fixture):
    sm_2_fixture.open_sign_in_page()
    sm_2_fixture.geo.click_submit_geo_position()
    sm_2_fixture.auth.auth_fake_in_app()


def test_C1(sm_2_fixture):
    sm_2_fixture.auth.receiving_mail()
    sm_2_fixture.auth.creation_user()
    sm_2_fixture.auth.check_welcom_modal_and_log_out()
    sm_2_fixture.auth.void_and_send_mail_for_password_recovery()
    sm_2_fixture.auth.check_mail_recovery_on_delivery()
