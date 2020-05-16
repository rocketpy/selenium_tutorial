import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files\chromedriver.exe"  
driver = webdriver.Chrome(PATH) 
LOGIN_FB = ""
PASSWORD_FB = ""


def auth_fb():
    try:
        driver.get("https://www.facebook.com")
        sleep(5)
        driver.find_element_by_id("email").send_keys(LOGIN_FB)
        sleep(2)
        driver.find_element_by_id("pass").send_keys(PASSWORD_FB)
        sleep(2)
        driver.find_element_by_id("u_0_b").click()
        
    
