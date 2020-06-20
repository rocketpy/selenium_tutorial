import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# PATH = r"C:\...\chromedriver.exe"  
PROXY = "12.345.678.910:8080"
# driver = webdriver.Chrome(PATH)
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(chrome_options=options)  # Firefox()

driver.get("https://youtube.com")

search = driver.find_element_by_xpath('//*[@id="search"]')  # input field 
search.send_keys("Prodigy")

search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')  # button of search field

search_button.click()

#driver.quit()
