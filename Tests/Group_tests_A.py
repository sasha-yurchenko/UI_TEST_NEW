def test_new_registration(sm_2_fixture):
    sm_2_fixture.auth.receiving_mail_A001()
    sm_2_fixture.auth.creation_user_A001()


def test_assert_invalid_fields_on_form(sm_2_fixture):
    sm_2_fixture.auth.Invalid_field_password_A_002()
    sm_2_fixture.auth.Invalid_field_confirm_password_A_003()
    sm_2_fixture.auth.Invalid_mail_invalid_password_A_004()
    sm_2_fixture.auth.Fields_is_emprty_A_005()
    sm_2_fixture.auth.Registration_with_existing_mail_A_006()

