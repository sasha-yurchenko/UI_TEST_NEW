# https://github.com/SeleniumHQ/selenium/blob/trunk/py/selenium/webdriver/support/relative_locator.py
# https://github.com/SeleniumHQ/selenium/blob/4c5b92bac07b17e223917c31caddf7035c120ea7/py/selenium/webdriver/remote/webdriver.py
from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import urllib3
import warnings
from selenium.webdriver.support.relative_locator import with_tag_name
import json
browser_capabilities = {
        "user" : "user-name",
        "accessKey" : "access-key",
        "build" : "[Python] - Relative Locators in Selenium 4",
        "name" : "[Python] - Relative Locators in Selenium 4",
        "platformName" : "Windows 10",
        "browserName" : "Chrome",
        "browserVersion" : "86.0",
        "headless" : False
}
user_name = "himanshu.sheth"
app_key = "fbI6kxucn5iRzwt5GWYiNvaPb4Olu9R8lwBsXWTSaIOebXn4x9"


def test_lambdatest_todo_app():
    sample_text = "Happy Testing at LambdaTest"
    new_item = "Cross Browser Testing at LambdaTest"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # remote_url = "https://" + user_name + ":" + app_key + "@hub.lambdatest.com/wd/hub"
    # web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = browser_capabilities)
    web_driver = webdriver.Chrome()
    web_driver.get('https://4dvanceboy.github.io/lambdatest/lambdasampleapp.html')
    web_driver.maximize_window()
     # Locate the web element li1
    elem_li1 = web_driver.find_element(By.XPATH,"//li[1]/input[@class='ng-pristine ng-untouched ng-valid']")
    # Locate the web element li5
    elem_li5 = web_driver.find_element(By.XPATH, "//li[5]/input[@class='ng-pristine ng-untouched ng-valid']")
    # Test 1 - Using the relative locators (above & below)
    # https://github.com/SeleniumHQ/selenium/blob/941dc9c6b2e2aa4f701c1b72be8de03d4b7e996a/py/selenium/webdriver/support/relative_locator.py#L41
    # https://github.com/SeleniumHQ/selenium/blob/941dc9c6b2e2aa4f701c1b72be8de03d4b7e996a/py/selenium/webdriver/support/relative_locator.py#L34
    # Use tag name and relative locators to find the web elements between them
    elementBox = web_driver.find_elements(with_tag_name("input").above(elem_li5).below(elem_li1))
    for items in elementBox:
        print()
        print(items.get_attribute('name'))
        # Use the Attribute Name to get the details of the web element
        elem_name = items.get_attribute('name')
        # Perform a click operation on the web element
        web_driver.find_element(By.NAME, elem_name).click()
    elem_add = web_driver.find_element(By.CSS_SELECTOR,"[ng-model='sampleList.sampletodoText']")
    elem_add.send_keys(sample_text)
    # Test 2 - Using the relative locator (to_right_of)
    # https://github.com/SeleniumHQ/selenium/blob/941dc9c6b2e2aa4f701c1b72be8de03d4b7e996a/py/selenium/webdriver/support/relative_locator.py#L55
    elem_submit = web_driver.find_elements(with_tag_name("input").to_right_of(elem_add))
    for items in elem_submit:
        print()
        print(items.get_attribute('id'))
        # Use the Attribute Name to get the details of the web element
        elem_name = items.get_attribute('id')
        # Add a new element in the list
        web_driver.find_element(By.ID, elem_name).click()
        break
    print()
    # Test 3 - Using the relative locator (near)
    # https://github.com/SeleniumHQ/selenium/blob/941dc9c6b2e2aa4f701c1b72be8de03d4b7e996a/py/selenium/webdriver/support/relative_locator.py#L62
    elem_add_button = web_driver.find_element(By.XPATH,"//input[@id='addbutton']")
    elem_txtbox = web_driver.find_elements(with_tag_name("input").near(elem_add_button))
    for items in elem_txtbox:
        print()
        print(items.get_attribute('id'))
        # Use the Attribute Name to get the details of the web element
        elem_name = items.get_attribute('id')
        # Add a new element in the list
        web_driver.find_element(By.ID, elem_name).send_keys(new_item + Keys.ENTER)
        break
    print()
    # Release resources held by the Selenium WebDriver
    web_driver.quit()