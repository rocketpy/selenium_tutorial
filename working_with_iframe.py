import time
import html5lib
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get('http://...')
try:
    time.sleep(4)
    iframe = driver.find_elements_by_tag_name('iframe')[0]
    driver.switch_to_default_content()
    driver.switch_to_frame(iframe)
    driver.switch_to_default_content()
    driver.find_elements_by_tag_name('iframe')[0]
    output = driver.page_source
    print(output)

finally:
    driver.quit()
    
    
# How to switch iframe inside iframe !!!

# switch_to_default_content () will take you back to the beginning of the document.
# What was happening is that you switched to the first iframe, switched to the top of the document again,
# and then tried to find the second iframe. Selenium cannot find the second iframe because it is inside the first iframe.

# If you remove the second switch_to_default_content () 
"""
iframe = driver.find_elements_by_tag_name('iframe')[0]
driver.switch_to.default_content()

driver.switch_to.frame(iframe)
driver.find_elements_by_tag_name('iframe')[0]

"""
