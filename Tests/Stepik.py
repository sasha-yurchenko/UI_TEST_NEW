from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    btn = driver.find_element_by_css_selector('button.trollface ')
    window_before = driver.window_handles[0]
    btn.click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    x_elem = driver.find_element_by_css_selector("#input_value")
    x_element_treasure = x_elem.text
    x = x_element_treasure
    y = calc(x)
    answer = driver.find_element_by_css_selector('.form-group input')
    answer.send_keys(y)
    btn_sub = driver.find_element_by_css_selector('button.btn')
    btn_sub.click()
finally:
    print('y')
