import sys
import json
import time
import pytest
import urllib3
import warnings
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import with_tag_name


browser_capabilities = {
        "user" : "user.name",
        "accessKey" : "Access-Key",
        "build" : "[Python] - Login Page",
        "name" : "[Python] - Login Page",
        "platformName" : "OS X Mavericks",
        "browserName" : "Chrome",
        "browserVersion" : "67.0"
}
user_name = "user-name"
app_key = "access-key"

def start_todo_app():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    remote_url = "https://" + user_name + ":" + app_key + "@bm.com/wd/hub"
    web_driver = webdriver.Remote(command_executor = remote_url, desired_capabilities = browser_capabilities)
    web_driver.get('https://accounts.hey.com/login')
    web_driver.maximize_window()
    elem_label = web_driver.find_element(By.CSS_SELECTOR,".orsignup")
    elementBox = web_driver.find_elements(with_tag_name("input").below(elem_label))

    for items in elementBox:
        # print(items.get_attribute('name'))
        elem_name = items.get_attribute('name')
        if (elem_name == "email"):
            # print("Inside Email Address")
            web_driver.find_element(By.NAME, elem_name).send_keys("Email@gmail.com")
        
        if (elem_name == "password"):
            # print("Inside Password")
            web_driver.find_element(By.NAME, elem_name).send_keys("Himanshu1!")
            web_driver.find_element(By.XPATH, "//span[@class='input-group-text password-group-text']").click()
            break
    
    sleep(3)
    web_driver.find_element(By.CSS_SELECTOR, ".btn").click()
    sleep(3)
    window_title = web_driver.title
    # print(window_title)
    expected_title = "Welcome"
    if expected_title in window_title:
        print("Login successful")
    else:
        print("Login not successful")
    print("Relative Locators in Selenium 4 on LambdaTest Login Page complete")

    web_driver.quit()



# Example 2 Above
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

password_field = driver.find_element(By.ID, "password")
email_address_field = driver.find_element(locate_with(By.TAG_NAME,  "input").above(password_field))


# Example 3 Below
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
