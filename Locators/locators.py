from typing import Tuple

from selenium.webdriver.common.by import By


class Locators(object):
    # Login page objects
    email_field_css_selector = (By.CSS_SELECTOR, "form .sm-form-field:nth-child(1) input")
    password_field_css_selector = (By.CSS_SELECTOR, "sm-signin div.sm-form-field:nth-child(2) input")
    login_button_xpath = (By.CSS_SELECTOR, 'sm-signin form button')
    forgot_password = (By.CSS_SELECTOR, 'a.link')
    field_email_for_forgot_password = (By.CSS_SELECTOR, "sm-restore input")
    button_send_email_for_forgot_password = (By.CSS_SELECTOR, 'sm-restore form button')
    text_fail_auth_xpath = (By.CSS_SELECTOR, '.sm-tabs-content p')

    # Profile page objects
    button_profile_menu_xpath = (By.CSS_SELECTOR, '.user-button img ')
    button_log_out_xpath = (By.CSS_SELECTOR, 'div.buttons :nth-child(5)')
    sidebar_profile = (By.CSS_SELECTOR, '.site-content ul')
    start_block_profile = (By.CSS_SELECTOR, "div.start-block")
    top_block_profile = (By.CSS_SELECTOR, "div.top-block")
    top_block_profile_text = (By.CSS_SELECTOR, ".top-block :nth-child(1) span")
    top_block_profile_icon = (By.CSS_SELECTOR, ".top-block :nth-child(1) i")
    button_top_block_profile = (By.CSS_SELECTOR, ".top-block :nth-child(3) a button")
    security_link = (By.CSS_SELECTOR, "div.avatar-block a")
    avatar_image = (By.CSS_SELECTOR, "div.avatar-block sm-avatar")
    button_apartaments = (By.CSS_SELECTOR, '.site-content sm-profile li:nth-child(1)')
    button_favorite_in_sidebar = (By.CSS_SELECTOR, '.site-content sm-profile li:nth-child(2)')

    # Main Headers objects
    button_login = (By.CSS_SELECTOR, 'div.auth-nav a:nth-child(1)')
    button_registration = (By.CSS_SELECTOR, 'div.auth-nav a:nth-child(1)')
    button_main_directory = (By.CSS_SELECTOR, '.catalog-button :nth-child(1)')
    main_logo_headers = (By.CSS_SELECTOR, 'a.logo.flex')
    field_search_headers = (By.CSS_SELECTOR, 'sm-global-search input')
    drop_down_list_geo = (By.CSS_SELECTOR, 'div.select-wrap i')
    button_favorite = (By.CSS_SELECTOR, '.nav-button a')
    field_geo = (By.CSS_SELECTOR, 'sm-global-geo input')

    # Products page objects
    all_primary_filters = (By.CSS_SELECTOR, '.sm-filters sm-primary-filter .content')
    open_drop_down_button = (By.CSS_SELECTOR, '.field-group .select-wrap i:nth-child(2)')
    field_search_elements = (By.CSS_SELECTOR, '.field-group .select-wrap input')
    tabs_on_is_content = (By.CSS_SELECTOR, 'div.sm-checkbox')
    value_drop_down = (By.CSS_SELECTOR, '.multi-select-dropdown-desktop div:nth-child(3)]')
    button_chat = (By.CSS_SELECTOR, 'div.nav-button .chat i')
    button_favorite_on_product_page = (By.CSS_SELECTOR, 'div.nav-button a')
    main_price = (By.CSS_SELECTOR, 'div.product-price')
    name_seller = (By.CSS_SELECTOR, 'div.user-head')

    # Geo Modal object
    button_submit_geo_position = (By.CSS_SELECTOR, '.actions :nth-child(1)')
    button_choose_another_country = (By.CSS_SELECTOR, '.actions :nth-child(2)')
    confirm_geo_modal = (By.CSS_SELECTOR, '//*[@id="sm-overlay-host-2"]/div/sm-confirm-geo-modal')
    submit_geo_xpath = (By.CSS_SELECTOR, '//div/sm-geo-for-search-modal/div[3]/button[1]')
    button_cancel_geo_xpath = (By.CSS_SELECTOR, '/html/body/div[2]/div/div/sm-geo-for-search-modal/div[3]/button[2]')
    field_name_countries_xpath = (By.CSS_SELECTOR, '//div/sm-geo-for-search-modal/div[2]/div[1]/div[1]/input')
    button_check_counties_xpath = (By.CSS_SELECTOR, '//div/sm-geo-for-search-modal/div[2]/div[1]/div[2]/ul/li')
    field_name_city_xpath = (By.CSS_SELECTOR, '//div/sm-geo-for-search-modal/div[2]/div[2]/div[1]/input')
    search_wrap_geo_xpath = (By.CSS_SELECTOR, 'sm-global-geo :nth-child(2) span')
    geo_modal_first = (By.CSS_SELECTOR, '//*[@id="sm-overlay-host-2"]/div/sm-confirm-geo-modal/span')
    button_check_city_xpath = (
        By.CSS_SELECTOR, '/html/body/div[2]/div[2]/div/sm-geo-for-search-modal/div[2]/div[2]/div[2]/ul/li[1]')

    # Main Page
    add_product_button = (By.CSS_SELECTOR, 'sm-header :nth-child(8)')
    element_top_blocks_h1 = (By.CSS_SELECTOR, '.site-content h1')
    elements_top_blocks_h3 = (By.CSS_SELECTOR, '.site-content h3')
    search_button = (By.CSS_SELECTOR, '.is-desktop:nth-child(1)>.search-button')
    input_search = (By.CSS_SELECTOR, '.ng-untouched:nth-child(1).sm-input.search-wrap')
    bottom_buttons_1 = (By.CSS_SELECTOR, 'div.bottom-buttons>button:nth-child(1)')
    bottom_buttons_2 = (By.CSS_SELECTOR, 'div.bottom-buttons>button:nth-child(2)')

    # Construct Page

    select_main_category = (By.CSS_SELECTOR, 'div.main-categories :nth-child(1)')
    select_nested_category = (By.CSS_SELECTOR, 'div.category-list :nth-child(1)')
    category_path = (By.CSS_SELECTOR, 'div.displayed-category-path span:nth-child(1)')
    change_link = (By.CSS_SELECTOR, '.displayed-category-path .r-side')
    tab_sale = (By.CSS_SELECTOR, '.sm-form-field .sm-checkbox:nth-child(1)')
    tab_sell = (By.CSS_SELECTOR, '.sm-form-field .sm-checkbox:nth-child(2)')
    input_google_country = (By.CSS_SELECTOR, 'sm-google-map input')
    list_country = (By.CSS_SELECTOR, 'div.pac-container .pac-item:nth-child(1)')
    name_contry_list = (By.CSS_SELECTOR, 'div.pac-container .pac-item:nth-child(1) span:nth-child(3)')
    button_publication = (By.CSS_SELECTOR, '.constructor-body .actions button:nth-child(2)')
    button_draft = (By.CSS_SELECTOR, 'div.constructor-body .actions button:nth-child(1)')
    select_multiselect_wrap = (
        By.CSS_SELECTOR, '.__no-padding .__attribute .form-field-item .select-wrap i:nth-child(2)')
    constructor_body = (By.CSS_SELECTOR, '.constructor-body form .product-rows .m-t-24 .__no-padding')
    value_in_dropdown_select = (By.CSS_SELECTOR, 'sm-select-dropdown-menu :nth-child(3)')
    value_in_dropdown_multi_select = (
        By.CSS_SELECTOR, 'sm-multiselect-dropdown-menu .virtual-scroll-container  div:nth-child(2)')
    input_construct = (By.CSS_SELECTOR, '.Input input')
    discription_in_const = (By.CSS_SELECTOR, 'textarea')
    price_input = (By.CSS_SELECTOR, 'sm-price input')
    input_phone_invalid = (By.CSS_SELECTOR, 'sm-phone-by-country .invalid-input')
    select_geo_phone = (By.CSS_SELECTOR, 'sm-phone-by-country sm-select i')
    price_range = (By.CSS_SELECTOR, '.price-range input')
    checkbox_const = (By.CSS_SELECTOR, 'sm-checkbox-group span:nth-child(2)')
    radio_btn = (By.CSS_SELECTOR, '.ButtonToggle .sm-form-field div:nth-child(1)')
    input_range = (By.CSS_SELECTOR, '.InputRange input')
    btn_photo = (By.CSS_SELECTOR, '.photo-loader input')
