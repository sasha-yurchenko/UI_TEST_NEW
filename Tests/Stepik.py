from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver = webdriver.Chrome()
    driver.get('http://SunInJuly.github.io/execute_script.html')
    x_elem = driver.find_element_by_id('input_value')
    x_element_treasure = x_elem.text
    x = x_element_treasure
    y = calc(x)
    answer = driver.find_element_by_css_selector('.form-group input')
    answer.send_keys(y)
    driver.find_element_by_id("robotCheckbox").click()
    button_robot = driver.find_element_by_id("robotsRule")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button_robot)
    button_robot.click()
    button_submit = driver.find_element_by_css_selector('form button')
    driver.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()
finally:
    print(x)
