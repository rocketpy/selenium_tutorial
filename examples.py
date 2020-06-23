# need add function for change Proxy and UserAgent !!!
from selenium import webdriver
import time
import random
from fake_useragent import UserAgent
from datetime import datetime as dt


def add_random_ua():
    # Generate a random user-agent useing fake_useragent library
    fake_ua = UserAgent().random
    # If there is already a "user-agent" argument in options delete it
    for item in options.arguments:
        if '--user-agent=' in item:
            options.arguments.remove(item)
    # Add generated user-agent to options
    options.add_argument(f'--user-agent={fake_ua}')
    print(f'User-agent: {fake_ua}')


def add_random_proxy():
    # Same logic as with add_random_ua
    # PROXY_LIST is just a list read from .txt file
    random_proxy = PROXY_LIST[random.randint(0, len(PROXY_LIST) - 1)]
    for item in options.arguments:
        if '--proxy-server=' in item:
            options.arguments.remove(item)
    options.add_argument(f'--proxy-server={random_proxy}')
    print(f'Proxy-server: {random_proxy}')

chromedriver = 'C:\\Users\\User\\Desktop\\chromedriver\\chromedriver.exe'
# Initial chromedriver options
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1024,768")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Default")
options.add_argument("--ignore-certificate-errors")

while True:
    print(f'Timestamp: {dt.now().strftime("%Y-%m-%d %H:%M:%S")}')
    add_random_ua()
    add_random_proxy()
    web = webdriver.Chrome(chromedriver, options=options)
    web.implicitly_wait(30)
    web.get(URL)

    # Some testing code...

    web.quit()



