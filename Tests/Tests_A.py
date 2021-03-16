import pytest


@pytest.mark.usefixtures('bases_fixture', 'init_driver')
class Test:
    def test_A1(self, bases_fixture):
        bases_fixture.open_temp_mail()
        bases_fixture.auth.receiving_mail()
        bases_fixture.auth.creation_user()
        bases_fixture.auth.check_and_wait_welcome_modal()
        bases_fixture.auth.check_mail_on_temp_mail()
