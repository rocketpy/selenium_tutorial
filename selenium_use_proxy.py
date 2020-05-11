from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


proxy = "12.345.678.910:8080"

options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % proxy)

chrome = webdriver.Chrome(chrome_options=options)
chrome.get("https://www ... ")
