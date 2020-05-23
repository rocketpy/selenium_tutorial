import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC


#PATH = "C:\Program Files\chromedriver.exe" 
#driver = webdriver.Chrome(PATH) 

PROXY = "12.345.678.910:8080"
options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(chrome_options=options)

driver.get("https://rozetka.com.ua/")

notebooks_pc_button = "/html/body/app-root/div/div[1]/app-rz-main-page/div/main/main-page-content/app-fat-menu-tablet/nav/ul/li[1]/a"
notebooks = "/html/body/app-root/div/div[1]/rz-super-portal/div/main/section/sp-dynamic-widgets/sp-widget-list[1]/section/ul/li[1]/sp-list-tile/div/a[2]"
smart_phones = "/html/body/app-root/div/div[1]/app-rz-main-page/div/main/main-page-content/app-fat-menu-tablet/nav/ul/li[2]/a"
