import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#path = "C:\..\chromedriver.exe" 
#driver = webdriver.Chrome(path)   # driver = webdriver.Firefox()
#driver.get("https:// ... ")

URL = "https://"
with requests.Session() as se:
    se.headers = {"User-Agent": "",
                 "Accept-Language": "en"
                 }
    response = se.get(URL)
soup = 

