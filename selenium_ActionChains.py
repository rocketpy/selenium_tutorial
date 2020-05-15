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
  

driver.get("http://www.")  
wait = WebDriverWait(driver, 40)
driver.find_element_by_css_selector("span .... ").click()
wait.until(EC.element_to_be_clickable((By.XPATH, " ... "))).click()
element = driver.find_element_by_link_text('Some_text')
actionChains = ActionChains(driver)
actionChains.move_to_element(element).perform()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Some_name"))).click()  
    
    
#  or
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()

