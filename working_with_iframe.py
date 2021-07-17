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
