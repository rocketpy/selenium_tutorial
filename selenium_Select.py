# https://selenium-python.readthedocs.io/navigating.html
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
# driver.maximize_window()  # fullsize_window
driver.get("https:// ... ")

driver.find_element_by_xpath("elem_xpath")

#  using Select , by visible_text
Select(driver.find_element_by_xpath("elem_xpath")).select_by_visible_text("some_text") 
#  or by_value
Select(driver.find_element_by_xpath("elem_xpath")).select_by_value("1")

# for press button
driver.find_element_by_class("name_class_button").click()

# get HTML data
data = driver.page_source
# read HTML
df = pd.read_html(data)
print(df)
# print(df[0])
time.sleep(5)
driver.quit()
