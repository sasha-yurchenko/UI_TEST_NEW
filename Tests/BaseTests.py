def test_A001(sm_2_fixture):
    sm_2_fixture.auth.receiving_mail()
    sm_2_fixture.auth.creation_user()


def test_A002(sm_2_fixture):
    sm_2_fixture.auth.fill_in_reg_fields()
