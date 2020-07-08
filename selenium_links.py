from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  read the docs : https://selenium-python.readthedocs.io/

# find_element_by_link_text  return first link !!!

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

# find link by particial text
driver.find_element_by_partial_link_text("partial").click()

# click on second href with same name
driver.find_elements_by_link_text("Secod link with same name")[1].click()

#  click on second link with same name
xpath = '//div[contains(text(), "Second")]/a[text()="Click here"]'
driver.find_element_by_xpath(xpath).click()

# when href open new window
current_url = driver.current_url

new_window_url = driver.find_element_by_link_text("Open new window").get_attribute("href")
driver.get(new_window_url)
 
driver.find_element_by_name("name").send_keys("sometext")
driver.get(current_url) # back
