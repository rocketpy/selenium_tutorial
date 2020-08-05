import time
import random
from selenium import webdriver
from fake_useragent import UserAgent
from datetime import datetime as dt
# https://pypi.org/project/fake-useragent/
#  #  read the docs : https://selenium-python.readthedocs.io/

# need add function for change Proxy and UserAgent !!!

def add_random_ua():
    fake_ua = UserAgent().random
    for item in options.arguments:
        if '--user-agent=' in item:
            options.arguments.remove(item)
    options.add_argument(f'--user-agent={fake_ua}')
    print(f'User-agent: {fake_ua}')


def add_random_proxy():
    random_proxy = PROXY_LIST[random.randint(0, len(PROXY_LIST) - 1)]  # PROXY_LIST taking from .txt file
    for item in options.arguments:
        if '--proxy-server=' in item:
            options.arguments.remove(item)
    options.add_argument(f'--proxy-server={random_proxy}')
    print(f'Proxy-server: {random_proxy}')

chromedriver = 'C:\\Users\\User\\Desktop\\chromedriver\\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1024,768")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Default")
options.add_argument("--ignore-certificate-errors")

while True:  # 
    # print(f'Timestamp: {dt.now().strftime("%Y-%m-%d %H:%M:%S")}')
    add_random_ua()
    add_random_proxy()
    web = webdriver.Chrome(chromedriver, options=options)
    web.implicitly_wait(30)
    web.get(URL)

    #  testing code here ...

    web.quit()
    
    
#  change to new window by Link
# ...
LINK = 'https://...'
# ...
#driver.implicitly_wait(3)
driver.maximize_window()
driver.get('LINK')
driver.find_element_by_xpath("xpath").click()
driver.find_element_by_xpath("xpath").click()
time.sleep(2)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
driver.switch_to.window(window_name)
time.sleep(2)
t_driver = driver.current_url
