import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


path = "C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("https:// ... ")

number = ""
password = ""


