from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# using send_keys
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.UP)

# or

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
