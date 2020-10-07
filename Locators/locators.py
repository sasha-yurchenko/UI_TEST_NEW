from selenium.webdriver.common.by import By


class Locators(object):
    # Login page objects
    email_field_signin = (By.CSS_SELECTOR, "form .sm-form-field:nth-child(1) input")
    password_field_signin = (By.CSS_SELECTOR, "sm-signin div.sm-form-field:nth-child(2) input")
    email_field_signup = (By.CSS_SELECTOR, "form .sm-form-field:nth-child(1) input")
    password_field_signup = (By.CSS_SELECTOR, "form .sm-form-field:nth-child(2) input")
    confirm_password_signup = (By.CSS_SELECTOR, "")
    login_button = (By.CSS_SELECTOR, 'sm-signin form button')
    forgot_password = (By.CSS_SELECTOR, 'a.link')
    field_email_for_forgot_password = (By.CSS_SELECTOR, "sm-restore input")
    button_send_email_for_forgot_password = (By.CSS_SELECTOR, 'sm-restore form button')
    text_fail_auth = (By.CSS_SELECTOR, '.sm-tabs-content p')
    text_fail_field = (By.CSS_SELECTOR, 'sm-form-field-errors li')
    text_fail_password = (By.CSS_SELECTOR, 'form .error')
    tab_signin = (By.CSS_SELECTOR, '.tabs-list li:nth-child(1)')
    tab_signup = (By.CSS_SELECTOR, '.tabs-list li:nth-child(2)')
    form_signup_field = (By.CSS_SELECTOR, 'form .sm-form-field input')
    btn_submit_signin = (By.CSS_SELECTOR, "sm-signin form button")
    btn_submit_signup = (By.CSS_SELECTOR, "sm-sign-up form button")

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
    welcome_modal = (By.CSS_SELECTOR, 'sm-welcome-modal .info-modal')

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
    submit_geo = (By.CSS_SELECTOR, '.modal-footer button:nth-child(1)')
    btn_cancel_geo = (By.CSS_SELECTOR, '.modal-footer button:nth-child(2)')
    geo_list_country = (By.CSS_SELECTOR, '.country .geo-list li')
    geo_list_city = (By.CSS_SELECTOR, '.city .geo-list li:nth-child(1)')
    field_name_country = (By.CSS_SELECTOR, '.country input')
    field_name_city = (By.CSS_SELECTOR, '.city input')
    search_wrap_geo = (By.CSS_SELECTOR, '.geo-place span')

    # Main Page
    add_product_button = (By.CSS_SELECTOR, 'sm-header :nth-child(8)')
    element_top_blocks_h1 = (By.CSS_SELECTOR, '.site-content h1')
    elements_top_blocks_h3 = (By.CSS_SELECTOR, '.site-content h3')
    search_button = (By.CSS_SELECTOR, '.is-desktop:nth-child(1)>.search-button')
    input_search = (By.CSS_SELECTOR, '.ng-untouched:nth-child(1).sm-input.search-wrap')
    bottom_buttons_1 = (By.CSS_SELECTOR, 'div.bottom-buttons>button:nth-child(1)')
    bottom_buttons_2 = (By.CSS_SELECTOR, 'div.bottom-buttons>button:nth-child(2)')
    geo_place_name = (By.CSS_SELECTOR, '.geo-place span')

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

    # Temp_Mail
    btn_copy_mail = (By.CSS_SELECTOR, '.input-box-col:nth-child(2) button')
    input_temp_mail = (By.CSS_SELECTOR, '.input-warp input')
    copy_mail = (By.CSS_SELECTOR, ".show .tooltip-inner")
    mail_one = (By.CSS_SELECTOR, ".inbox-dataList li:nth-child(2) .col-box:nth-child(2) a")
    mail_two = (By.CSS_SELECTOR, ".inbox-dataList li:nth-child(3) .col-box:nth-child(2) a")
    list_mail = (By.CSS_SELECTOR, ".inbox-dataList li .col-box:nth-child(2) a")
    btn_on_letter = (By.CSS_SELECTOR, "td a")
    btn_update = (By.ID, "click-to-refresh")

    # Page_email_confirm
    email_confirm = (By.CSS_SELECTOR, "sm-email-confirm .flex")