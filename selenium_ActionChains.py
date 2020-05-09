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
  
