from Locators.locators import Locators


class Header:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        self.button_login_header = Locators.button_login
        self.button_registration_header = Locators.button_login
        self.button_change_language_interface = Locators.change_language_interface
        self.button_close_language_interface = Locators.close_language_interface
        self.interface_language_list = Locators.interface_language_list
        self.button_confirm_language_interface = Locators.button_confirm
        self.button_main_directory_catalog = Locators.button_main_directory
        self.button_close_main_directory = Locators.close_language_interface
        self.main_logo_headers = Locators.main_logo_headers
        self.field_search_headers = Locators.field_search_headers
        self.drop_down_list_geo = Locators.drop_down_list_geo

