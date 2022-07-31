#  Selenium-stealth - Trying to make python selenium more stealthy.

# PyPi:  https://pypi.org/project/selenium-stealth/
# Github: https://github.com/diprajpatra/selenium-stealth

# pip install selenium-stealth

# Test for bots : https://bot.sannysoft.com/

# Important:  As of now selenium-stealth only support Selenium Chrome !!!

#  IMPORTANT
"""
A python package selenium-stealth to prevent detection. This programme is trying to make python selenium more stealthy.

As of now selenium-stealth only support Selenium Chrome.

After using selenium-stealth you can prevent almost all selenium detections.
There is a lot of guides on stackoverflow on How to prevent selenium detection but I can not find a single python package
for it so I am just creating one after all we can't let the cats win.
It can be seen as a re-implementation of JavaScript puppeteer-extra-plugin-stealth developed by @berstend.

Features that currently selenium-stealth can offer:
✅️ selenium-stealth with stealth passes all public bot tests.

✅️ With selenium-stealth selenium can do google account login.

✅️ selenium-stealth help with maintaining a normal reCAPTCHA v3 score
"""

#  Usage

import time
from selenium import webdriver
from selenium_stealth import stealth


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\DIPRAJ\Programming\adclick_bot\chromedriver.exe")

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

url = "https://bot.sannysoft.com/"
driver.get(url)
time.sleep(5)
driver.quit()


# automation login and get screen shot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth


options = Options()
options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
s = Service('C:\\BrowserDrivers\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )

driver.get("https://www..com")
driver.save_screenshot('file_name.png)


