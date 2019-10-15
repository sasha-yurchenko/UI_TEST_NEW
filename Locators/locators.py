class Locators():
    # Login page objects
    email_field_xpath = "/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[2]/sm-signin/form/div[1]/input"
    password_field_xpath = "/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[2]/sm-signin/form/div[2]/input"
    login_button_xpath = '/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[''2]/sm-signin/form/button'
    forgot_password = '/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[2]/sm-signin/form/div[3]/a'
    field_email_for_forgot_password = '/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[' \
                                      '2]/sm-restore/form/div/input '
    button_send_email_for_forgot_password = '/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[' \
                                            '2]/sm-restore/form/button '

    # Profile page objects
    button_profile_menu_xpath = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[4]/sm-avatar/div/div/img'
    button_log_out_xpath = '//div/sm-profile-dropdown-menu/div/div/div'

    # Space Main Page  objects
    submit_geo_xpath = '//div/sm-geo-for-search-modal/div[3]/button[1]'
    button_cancel_xpath = '/html/body/div[2]/div/div/sm-geo-for-search-modal/div[3]/button[2]'
    field_name_countries_xpath = '//div/sm-geo-for-search-modal/div[2]/div[1]/div[1]/input'
    button_check_counties_xpath = '//div/sm-geo-for-search-modal/div[2]/div[1]/div[2]/ul/li'
    button_check_city_xpath = '//div/sm-geo-for-search-modal/div[2]/div[2]/div[2]/ul/li[2]'
    field_name_city_xpath = '//div/sm-geo-for-search-modal/div[2]/div[2]/div[1]/input'
    search_wrap_geo_xpath = '/html/body/sm-root/sm-base-layout/sm-header/div/div/sm-global-geo/div/div/div/div/input'
    open_main_page_url = 'http://test.spacemir.com'

    # Main Headers objects
    button_login = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[3]/a[1]/button'
    button_registration = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[3]/a[2]/button'
    change_language_interface = '/html/body/sm-root/sm-base-layout/sm-header/div/div/sm-locale-select/div'
    close_language_interface = '//*[@id="sm-overlay-host-1"]/div/sm-locale-select-modal/div[2]/i'
    interface_language_list = '//*[@id="sm-overlay-host-1"]/div/sm-locale-select-modal/sm-select/div/div/i[1]'
    button_confirm = '//*[@id="sm-overlay-host-1"]/div/sm-locale-select-modal/button'
    button_main_directory = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[1]/i'
    close_main_directory = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[1]/i'
    main_logo_headers = '/html/body/sm-root/sm-base-layout/sm-header/div/div/a'
    field_search_headers = '/html/body/sm-root/sm-base-layout/sm-header/div/div/sm-global-search/div/form/input'
    drop_down_list_geo = '/html/body/sm-root/sm-base-layout/sm-header/div/div/sm-global-geo/div/div/div/div/i'

    # Products page objects
    choice_category_in_catalog = '//*[@id="sm-overlay-host-0"]/div/sm-dropdown-catalog/sm-catalog/div/div/div[3]'
    choice_child_category_in_catalog = '//*[@id="sm-overlay-host-0"]/div/sm-dropdown-catalog/sm-catalog/div/div[' \
                                       '2]/div/a '
    choice_filter = '/html/body/sm-root/sm-base-layout/div/sm-ad-findings/div/sm-desktop-ad-findings-header/div[' \
                    '2]/div/div/sm-primary-filter[1]/div '
    open_drop_down_button = '//*[@id="sm-overlay-host-9"]/div/sm-primary-filters-modal/form/div/div/sm-multiselect' \
                            '/div/div/i[1] '
    label_ads_short_card = '/html/body/sm-root/sm-base-layout/div/sm-ad-findings/div/div/div/div/ngx-masonry' \
                           '/ngxmasonryitem[1]/sm-short-product-card/div/a/div[2]/div[1] '
    field_search_elements = '//*[@id="sm-overlay-host-13"]/div/sm-primary-filters-modal/form/div/div/sm-multiselect' \
                            '/div/div/input '


