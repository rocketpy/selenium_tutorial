import time
# from selenium import webdriver
from seleniumwire import webdriver
from fake_useragent import UserAgent


URL = "https://www.../"
options = webdriver.FirefoxOptions()
useragent = UserAgent()
options.set_preference("general.useragent.override", useragent.random)

# set proxy
# proxy = "123.456.78.90:8000"
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities["marionette"] = True
#
# firefox_capabilities["proxy"] = {"proxyType": "MANUAL",
#                                  "httpProxy": proxy,
#                                  "ftpProxy": proxy,
#                                  "sslProxy": proxy
#                                  }

proxy_options = {"proxy": 
                {"https": f"http://{login}:{password}@138.128.91.65:8000"}
                }

# driver = webdriver.Firefox(executable_path="//geckodriver",
#                            options=options, proxy=proxy)

driver = webdriver.Firefox(executable_path="/geckodriver",
                           seleniumwire_options=proxy_options)

# "C:\\users\\\chromedriver.exe"
# r"C:\\chromedriver.exe"

"""
from selenium import webdriver


PROXY = "<HOST:PORT>"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

with webdriver.Firefox() as driver:
    driver.get("https://...")

"""

try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    driver.save_screenshot("file_name.png")
    time.sleep(3)
    driver.get(URL)
    time.sleep(3)

    driver.refresh()
    driver.get_screenshot_as_file("file_name.png")
    driver.get(url="https://...com/")
    time.sleep(3)
    driver.save_screenshot("file_name.png")
    time.sleep(2)

    driver.get("https://2ip.ru")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
