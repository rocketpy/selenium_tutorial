#  Python client for the BrowserMob Proxy

# Docs:  https://browsermob-proxy-py.readthedocs.io/en/latest/
# pip install browsermob-proxy

# How to use with selenium-webdriver
from browsermobproxy import Server

server = Server("path/to/browsermob-proxy")
server.start()
proxy = server.create_proxy()


from selenium import webdriver

profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)


proxy.new_har("file_name")
driver.get("http://www...")
proxy.har # returns a HAR JSON blob

server.stop()
driver.quit()

# For prevent a problems with server need use:
import psutil
import time

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == "browsermob-proxy":
        proc.kill()

# use slep before and after start server        
server.start()
time.sleep(1)
proxy = server.create_proxy()
time.sleep(1)
