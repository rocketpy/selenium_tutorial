#  Using JSON
import json


def save_cookie(driver, path):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
    with open(path, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    for cookie in cookies:
        driver.add_cookie(cookie)

        
#  Using pickle
import pickle


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookie(driver, path):
     with open(path, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             driver.add_cookie(cookie)

            
#  load to file cookies            
import pickle
import selenium.webdriver 


driver = selenium.webdriver.Firefox()
driver.get("http://www...")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

#  add cookies
import pickle
import selenium.webdriver 

driver = selenium.webdriver.Firefox()
driver.get("http://www...")
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
        

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data") 
driver.get('https://www...')
time.sleep(30)  # time to enter data
driver.quit()


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('/chromedriver', options=chrome_options)
driver.get('https://www...')  # is already authenticated
time.sleep(10)
driver.quit()   
# use or this , modificated
"""
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)  # path to driver
driver.get('https://web.whatsapp.com')  # is already authenticated
time.sleep(30)
"""


#  some example        
import pickle
from selenium import webdriver


def save_cookie(driver):
    with open("cookie", 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)
        
def load_cookie(driver):
     with open("cookie", 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         for cookie in cookies:
             print(cookie)
             driver.add_cookie(cookie)

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www...'
driver.get(url)
#  first login and get cookies
load_cookie(driver) 
save_cookie(driver)
driver.quit()            
