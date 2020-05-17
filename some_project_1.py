import os
from time import sleep
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
chrome = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome(PATH) 
LOGIN_FB = ""
PASSWORD_FB = ""

"""
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
prox.http_proxy = "ip_addr:port"
prox.socks_proxy = "ip_addr:port"
prox.ssl_proxy = "ip_addr:port"
capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)
driver = webdriver.Chrome(desired_capabilities=capabilities)
"""


def auth_fb():
    try:
        driver.get("https://www.facebook.com")
        sleep(5)
        driver.find_element_by_id("email").send_keys(LOGIN_FB)
        sleep(2)
        driver.find_element_by_id("pass").send_keys(PASSWORD_FB)
        sleep(2)
        driver.find_element_by_id("u_0_b").click()
        
        if driver.find_element_by_id("pass"):
            print("Authorization not done ! , repeat again")
            auth_fb()
    except NoSuchElementException:
        print("Authorization is done !")
        
    
