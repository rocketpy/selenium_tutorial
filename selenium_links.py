from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  read the docs : https://selenium-python.readthedocs.io/


#  get attribute href
href = driver.find_element_by_link_text("some text").get_attribute("href")
print(href) # recomand.html
 
id = driver.find_element_by_link_text("some text").get_attribute("id")
print(id) #  recommend_selenium_link
 
text = driver.find_element_by_id("selenium_link").text
print(text) # Recommend Selenium
 
tag_name = driver.find_element_by_id("selenium_link").tag_name
print(tag_name) #  a

# by xpath
driver.find_element_by_xpath("//p/a[text()='some text']").click()

# click on second href with same name
driver.find_elements_by_link_text("Some second same link")[1].click()

# find_element_by_link_text  return first link !!!

#  click on second link with same name
xpath = '//div[contains(text(), "Second")]/a[text()="Click here"]'
driver.find_element_by_xpath(xpath).click()
