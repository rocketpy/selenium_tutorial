# How to interact with an existing browser session

# Start chrome with:
# chrome --remote-debugging-port=9222

# Or with optional
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
   
  
options = Options()
driver = webdriver.Chrome()

options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
path = "C:\chromedriver.exe"
driver = webdriver.Chrome(path, chrome_options=options)
driver.get('https://www...')

# print(driver.title)

"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


url = "http://localhost:4444/wd/hub"
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['platform'] = "WINDOWS"
capabilities['version'] = "10"

"""

