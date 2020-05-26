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

#  searching something
search = driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-header/header/div/div[2]/div[3]/form/div/div/input')
time.sleep(1) 
search.send_keys('name of object')
time.sleep(1)
# search.send_keys(Keys.ENTER)
# time.sleep(1)
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-header/header/div/div[2]/div[3]/form/button').click()


# get all notebooks
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-main-page/div/main/main-page-content/app-fat-menu-tablet/nav/ul/li[1]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/rz-super-portal/div/main/section/sp-dynamic-widgets/sp-widget-list[1]/section/ul/li[1]/sp-list-tile/div/a[2]').click()
time.sleep(3)
# here need use pagination !!!
img_xpath = "/html/body/app-root/div/div[1]/rz-category/div/main/ctg-catalog/div/div[2]/section/div/ctg-grid/ul/li[1]/app-goods-tile-default/div/div[2]/a[1]/img[2]"
name_xpath = "/html/body/app-root/div/div[1]/rz-category/div/main/ctg-catalog/div/div[2]/section/div/ctg-grid/ul/li[1]/app-goods-tile-default/div/div[2]/a[2]/span"
price_xpath = "/html/body/app-root/div/div[1]/rz-category/div/main/ctg-catalog/div/div[2]/section/div/ctg-grid/ul/li[1]/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span[1]"


