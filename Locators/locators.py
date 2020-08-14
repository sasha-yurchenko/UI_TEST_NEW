class Locators:
    # Login page objects
    email_field_xpath = "/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[2]/sm-signin/form/div[1]/input"
    password_field_xpath = "/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[2]/sm-signin/form/div[2]/input"
    login_button_xpath = '/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[''2]/sm-signin/form/button'
    forgot_password = '/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[2]/sm-signin/form/div[3]/a'
    field_email_for_forgot_password = '/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[' \
                                      '2]/sm-restore/form/div/input '
    button_send_email_for_forgot_password = '/html/body/sm-root/sm-base-layout/div/sm-account/div/div/div[' \
                                            '2]/sm-restore/form/button '
    text_fail_auth_xpath = '/html/body/sm-root/sm-base-layout/div[2]/sm-account/div/div/div[2]/div'

    # Profile page objects
    button_profile_menu_xpath = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[4]/sm-avatar/div/div/img'
    button_log_out_xpath = '//div/sm-profile-dropdown-menu/div/div/div'
    tittle_block_profile = '/html/body/sm-root/sm-base-layout/div[2]/sm-profile/div[2]/div/div/sm-entry-profile-page/div/div[1]/div[1]/div[1]/span'
    sidebar_profile = '/html/body/sm-root/sm-base-layout/div[2]/sm-profile/div[1]'
    start_block_profile = '/html/body/sm-root/sm-base-layout/div[2]/sm-profile/div[2]/div/div/sm-entry-profile-page/div'
    button_apartaments = '/html/body/sm-root/sm-base-layout/div[2]/sm-profile/div[1]/div/ul/li[1]/a'
    button_favorite = '/html/body/sm-root/sm-base-layout/div[2]/sm-profile/div[1]/div/ul/li[2]/a'

    # Main Headers objects
    button_login = '//button'
    button_registration = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[3]/a[2]/button'
    change_language_interface = '/html/body/sm-root/sm-base-layout/sm-header/div/div/sm-locale-select/div'
    close_language_interface = '//*[@id="sm-overlay-host-1"]/div/sm-locale-select-modal/div[2]/i'
    interface_language_list = '//*[@id="sm-overlay-host-1"]/div/sm-locale-select-modal/sm-select/div/div/i[1]'
    button_confirm = '//*[@id="sm-overlay-host-1"]/div/sm-locale-select-modal/button'
    button_main_directory = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[1]/i'
    close_main_directory = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[1]/i'
    main_logo_headers = '/html/body/sm-root/sm-base-layout/sm-header/div/div/a'
    field_search_headers = '/html/body/sm-root/sm-base-layout/sm-header/div/div/sm-global-search/div/form/input'
    drop_down_list_geo = '//div/div/div/div/i'
    button_favorite = '/html/body/sm-root/sm-base-layout/sm-header/div/div/div[3]/a/i'
    field_geo = '/html/body/sm-root/sm-base-layout/sm-header/div/div/sm-global-geo'

    # Products page objects
    choice_category_in_catalog = '//*[@id="sm-overlay-host-0"]/div/sm-dropdown-catalog/sm-catalog/div/div/div[3]'
    choice_child_category_in_catalog = '//*[@id="sm-overlay-host-0"]/div/sm-dropdown-catalog/sm-catalog/div/div[' \
                                       '2]/div/a '
    choice_filter = '/html/body/sm-root/sm-base-layout/div/sm-ad-findings/div/sm-desktop-ad-findings-header/div[2]/div/div/sm-primary-filter[1]/div'
    open_drop_down_button = '/html/body/sm-root/sm-base-layout/div/sm-ad-findings/div/sm-desktop-ad-findings-header/div[2]/div/div/sm-primary-filter[1]/div'
    label_ads_short_card = '/html/body/sm-root/sm-base-layout/div/sm-ad-findings/div/div[2]/div/div/ngx-masonry/ngxmasonryitem/sm-short-product-card/div/a/div[2]/div[1]'
    field_search_elements = '//sm-multiselect/div/div/input'
    tab_main = '/html/body/sm-root/sm-base-layout/div[2]/sm-product-findings/div/sm-desktop-ad-findings-header/div[3]/div[1]/div/div[1]/sm-button-toggle-group/div'
    tab_child_1 = '/html/body/sm-root/sm-base-layout/div[2]/sm-product-findings/div/sm-desktop-ad-findings-header/div[3]/div[1]/div/div[1]/sm-button-toggle-group/div/div[1]'
    tab_child_2 = '/html/body/sm-root/sm-base-layout/div[2]/sm-product-findings/div/sm-desktop-ad-findings-header/div[3]/div[1]/div/div[1]/sm-button-toggle-group/div/div[2]'
    tab_child_3 = '/html/body/sm-root/sm-base-layout/div[2]/sm-product-findings/div/sm-desktop-ad-findings-header/div[3]/div[1]/div/div[1]/sm-button-toggle-group/div/div[3]'
    sm_multiselect_dropdown_menu = '//*[@id="sm-overlay-host-4"]/div/sm-multiselect-dropdown-menu'
    value_drop_down = '/html/body/div[2]/div[2]/div/sm-multiselect-dropdown-menu/div/div[3]'
    click_on_page = '//body/div[2]/div'
    button_number = '/html/body/sm-root/sm-base-layout/div/sm-ad-findings/div/div[2]/div/div/ngx-masonry/ngxmasonryitem[4]/sm-short-product-card/div/div/div[2]'
    button_chat = '/html/body/sm-root/sm-base-layout/div[2]/sm-product-findings/div/div/div/div/div/div[2]/sm-short-product-card[1]/div/div/div[2]/div'
    button_favorite_on_product_page = '/html/body/sm-root/sm-base-layout/div[2]/sm-product-findings/div/div/div/div/div/div[2]/sm-short-product-card[1]/div/a/div[1]/i'
    main_price = '/html/body/sm-root/sm-base-layout/div[2]/sm-product-findings/div/div/div/div/div/div[2]/sm-short-product-card[1]/div/a/div[1]/i'
    name_seller = '/html/body/sm-root/sm-base-layout/div[2]/sm-product-findings/div/div/div/div/div/div[2]/sm-short-product-card[1]/div/div/div[1]'

    # Geo Modal object
    button_submit_geo_position = '//div[4]/button'
    button_choose_another_country = '//div[4]/button[2]'
    confirm_geo_modal = '//*[@id="sm-overlay-host-2"]/div/sm-confirm-geo-modal'
    submit_geo_xpath = '//div/sm-geo-for-search-modal/div[3]/button[1]'
    button_cancel_geo_xpath = '/html/body/div[2]/div/div/sm-geo-for-search-modal/div[3]/button[2]'
    field_name_countries_xpath = '//div/sm-geo-for-search-modal/div[2]/div[1]/div[1]/input'
    button_check_counties_xpath = '//div/sm-geo-for-search-modal/div[2]/div[1]/div[2]/ul/li'
    field_name_city_xpath = '//div/sm-geo-for-search-modal/div[2]/div[2]/div[1]/input'
    search_wrap_geo_xpath = '/html/body/sm-root/sm-base-layout/div[2]/sm-entry-page/div/div[2]/div/div/sm-global-geo/div/div/div/div/span'
    geo_modal_first = '//*[@id="sm-overlay-host-2"]/div/sm-confirm-geo-modal/span'
    button_check_city_xpath = '/html/body/div[2]/div[2]/div/sm-geo-for-search-modal/div[2]/div[2]/div[2]/ul/li[1]'

    # Main Page
    add_product_button = '[class = "add-product-button"]'
    elements_top_blocks = '.top-blocks:nth-child(1)>.title.m-b-12'
    search_button = '.is-desktop:nth-child(1)>.search-button'
    input_search = '.ng-untouched:nth-child(1).sm-input.search-wrap'