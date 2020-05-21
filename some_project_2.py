import os
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#path = "C:\..\chromedriver.exe" 
#driver = webdriver.Chrome(path)   # driver = webdriver.Firefox()
#driver.get("https:// ... ")

URL = "https:// "
quant_pages = []

with requests.Session() as se:
    se.headers = {"User-Agent": " ",  # insert any User-agent !
                 "Accept-Language": "en"
                 }
    response = se.get(URL)

soup = BeautifulSoup(response.content, "html.parser")
pages = int(input("Input quants a pages : "))
category = input("Input a category : ")

for i in range(1, pages + 1):
    sleep(3)
    srt = quant_pages.append(se.get(f'https://.../{category}/?page=' + str(i)))

for srt in quant_pages:
    soup = BeautifulSoup(srt.content, "html.parser")
    
    for elem in soup.select("some_link"):
        link = elem.find("a")
        try:
            with open(f'{category}.txt' "+a") as fil):  # write data to txt file
                file.write(f'{link.get("href")}\n')
        except AttributeError as error:
            print(f'Some error {error} ,  script is runnig !')
            continue
                           
        
