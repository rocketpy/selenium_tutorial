from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


href = driver.find_element_by_link_text("Recommend Selenium").get_attribute("href")
print(href) # recomand.html
 
id = driver.find_element_by_link_text("Recommend Selenium").get_attribute("id")
print(id) #  recommend_selenium_link
 
text = driver.find_element_by_id("recommend_selenium_link").text
print(text) # Recommend Selenium
 
tag_name = driver.find_element_by_id("recommend_selenium_link").tag_name
print(tag_name) #  a
