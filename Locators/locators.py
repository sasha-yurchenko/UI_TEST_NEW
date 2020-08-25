class Locators:
    # Login page objects
    email_field_css_selector = "form .sm-form-field:nth-child(1) input"
    password_field_css_selector = "sm-signin div.sm-form-field:nth-child(2) input"
    login_button_xpath = 'sm-signin form button'
    forgot_password = 'a.link'
    field_email_for_forgot_password = "sm-restore input"
    button_send_email_for_forgot_password = 'sm-restore form button'
    text_fail_auth_xpath = 'p.text-failure'

    # Profile page objects
    button_profile_menu_xpath = '.user-button img '
    button_log_out_xpath = 'div.buttons :nth-child(5)'
    sidebar_profile = '.site-content ul'
    start_block_profile = "div.start-block"
    top_block_profile = "div.top-block"
    top_block_profile_text = ".top-block :nth-child(1) span"
    top_block_profile_icon = ".top-block :nth-child(1) i"
    button_top_block_profile = ".top-block :nth-child(3) a button"
    security_link = "div.avatar-block a"
    avatar_image = "div.avatar-block sm-avatar"
    button_apartaments = '.site-content sm-profile li:nth-child(1)'
    button_favorite_in_sidebar = '.site-content sm-profile li:nth-child(2)'

    # Main Headers objects
    button_login = 'div.auth-nav a:nth-child(1)'
    button_registration = 'div.auth-nav a:nth-child(1)'
    change_language_interface = 'sm-locale-select :nth-child(1)'
    close_language_interface = '//*[@id="sm-overlay-host-1"]/div/sm-locale-select-modal/div[2]/i'
    interface_language_list = '//*[@id="sm-overlay-host-1"]/div/sm-locale-select-modal/sm-select/div/div/i[1]'
    button_confirm = '//*[@id="sm-overlay-host-1"]/div/sm-locale-select-modal/button'
    button_main_directory = '.catalog-button :nth-child(1)'
    main_logo_headers = 'a.logo.flex'
    field_search_headers = 'sm-global-search input'
    drop_down_list_geo = 'div.select-wrap i'
    button_favorite = '.nav-button a'
    field_geo = 'sm-global-geo input'

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
    button_submit_geo_position = '.actions :nth-child(1)'
    button_choose_another_country = '.actions :nth-child(2)'
    confirm_geo_modal = '//*[@id="sm-overlay-host-2"]/div/sm-confirm-geo-modal'
    submit_geo_xpath = '//div/sm-geo-for-search-modal/div[3]/button[1]'
    button_cancel_geo_xpath = '/html/body/div[2]/div/div/sm-geo-for-search-modal/div[3]/button[2]'
    field_name_countries_xpath = '//div/sm-geo-for-search-modal/div[2]/div[1]/div[1]/input'
    button_check_counties_xpath = '//div/sm-geo-for-search-modal/div[2]/div[1]/div[2]/ul/li'
    field_name_city_xpath = '//div/sm-geo-for-search-modal/div[2]/div[2]/div[1]/input'
    search_wrap_geo_xpath = 'sm-global-geo :nth-child(2) input'
    geo_modal_first = '//*[@id="sm-overlay-host-2"]/div/sm-confirm-geo-modal/span'
    button_check_city_xpath = '/html/body/div[2]/div[2]/div/sm-geo-for-search-modal/div[2]/div[2]/div[2]/ul/li[1]'

    # Main Page
    add_product_button = 'sm-header :nth-child(8)'
    elements_top_blocks = '.top-blocks:nth-child(1)>.title.m-b-12'
    search_button = '.is-desktop:nth-child(1)>.search-button'
    input_search = '.ng-untouched:nth-child(1).sm-input.search-wrap'
    bottom_buttons_1 = 'div.bottom-buttons>button:nth-child(1)'
    bottom_buttons_2 = 'div.bottom-buttons>button:nth-child(2)'

# Construct Page

    select_main_category = 'div.main-categories :nth-child(1)'
    select_nested_category = 'div.category-list :nth-child(1)'
    category_path = 'div.displayed-category-path span:nth-child(1)'
    change_link = '.displayed-category-path .r-side'
    tab_sale = '.sm-form-field .sm-checkbox:nth-child(1)'
    tab_sell = '.sm-form-field .sm-checkbox:nth-child(2)'
    input_google_country = 'sm-google-map input'

