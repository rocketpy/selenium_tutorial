import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files\chromedriver.exe"  
driver = webdriver.Chrome(PATH)   


def auth_fb():
    try:
        driver.get('https://www.facebook.com')
        
    
