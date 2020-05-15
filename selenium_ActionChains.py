import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


path = "C:\Program Files\chromedriver.exe" 
driver = webdriver.Chrome(path)   
driver.get("https:// ... ")

driver.implicitly_wait(5)  # waiting a 5 sec for loading a web_page

some_elem = driver.find_element_by_id("id_name")
some_elem_count = driver.find_element_by_id("id_name")

actions = ActionChains(driver)
actions.click(some_elem)

for i in range(1000):  # 1000 times
    actions.perform()
  
driver.quit()

#  or

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
  
