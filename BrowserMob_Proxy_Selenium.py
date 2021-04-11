# BrowserMob Proxy  is a free utility to help web developers watch and manipulate network traffic from their AJAX applications.

#  Python client for the BrowserMob Proxy

# Docs:  https://browsermob-proxy-py.readthedocs.io/en/latest/
# Download BrowserMob Proxy:  https://bmp.lightbody.net/
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

"""
import time
import psutil
from browsermobproxy import Server


for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == "browsermob-proxy":
        proc.kill()

dict = {'port': 8090}
server = Server(path="./BrowserMobProxy/bin/browsermob-proxy", options=dict)
server.start()
time.sleep(1)
proxy = server.create_proxy()
time.sleep(1)
from selenium import webdriver
profile = webdriver.FirefoxProfile()
selenium_proxy = proxy.selenium_proxy()
profile.set_proxy(selenium_proxy)
driver = webdriver.Firefox(firefox_profile=profile)


proxy.new_har("file_name")
driver.get("http://www...")
print (proxy.har) # returns a HAR JSON blob

server.stop()
driver.quit()
"""

