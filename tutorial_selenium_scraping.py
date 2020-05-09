import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


path = "C:\Program Files\chromedriver.exe"  # or any other path

driver = webdriver.Chrome(path)   # driver = webdriver.Firefox()
driver.get("https:// ... ")
# print(driver.title)  using this for test !


#  Clicking elements , like buttons or links !  for buttons need use ID ( taked from HTML )
link = driver.find_element_by_link_text("link_name")  # name on page
link.click()
try:
    some_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "some_link_text")))
    some_link.click()
    some_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ID_button")))
    somebutton.click()
    
    #  for return on previuos page use :
    driver.back()
    
    # for next page use :
    driver.forward()
    
except:
    driver.quit()
# or
finally:
    driver.quit()



# search data with input on web_page ( search field )
search = driver.find_element_by_name("some_name")  # tag name
search.send_keys("test")
# for clean serch key use :
# search.clear()
search.send_keys(Keys.RETURN)  

#  adding waits ( using for waiting a result )
try:
    some_elem = WebDriverWait(driver, 10).until(  # 10 seconds
        EC.presence_of_element_located((By.ID, "some_name"))  #  By.NAME , By.TAG_NAME , By.CLASS_NAME
    )
    # print(some_elem.text)
    articles = some_elem.find_elements_by_tag_name("tag_name")
    for article in articles:
        header = article.find_element_by_class_name("some_name")
        print(header.text)

finally:
    driver.quit()

    
# find elem by id
# some_elem = driver.find_element_by_id("some_name")
# print(some_elem.text)

#  need a few seconds for waiting a result
# time.sleep(5)

# driver.quit()  # or driver.close()
