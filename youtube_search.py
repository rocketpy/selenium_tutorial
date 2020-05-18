import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files\chromedriver.exe"  
PROXY = "12.345.678.910:8080"
options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(chrome_options=options)  # Firefox()
#driver = webdriver.Chrome(PATH) 
driver.get("https://youtube.com")

search = driver.find_element_by_xpath("...")  # input field 
search.send_keys("some_word")

search_button = driver.find_element_by_xpath("...")  # button of search field
search_button.click()

driver.quit()
