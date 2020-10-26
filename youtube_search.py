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
from selenium.webdriver.common.proxy import Proxy, ProxyType


# PATH = r"C:\...\chromedriver.exe"  
PROXY = "134.90.229.118:39851"

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = PROXY
prox.socks_proxy = PROXY
prox.ssl_proxy = PROXY
capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

# driver = webdriver.Chrome(PATH)
# opts = Options()
# opts.add_argument("user-agent=[user-agent string]")
# opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
# driver = webdriver.Chrome(chrome_options=opts)
# options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=%s' % PROXY)
# driver = webdriver.Chrome(chrome_options=options)  # Firefox()
driver = webdriver.Chrome(desired_capabilities=capabilities)

driver.get("https://vk.com")

# search = driver.find_element_by_xpath('//*[@id="search"]')  # input field 
# search.send_keys("Prodigy")

# search_button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')  # button of search field

# search_button.click()

#driver.quit()
