import time
from selenium import webdriver


# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"


options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "user-agent")

options.set_preference("dom.webdriver.enabled", False)

driver = webdriver.Firefox(executable_path="...",
                           options=options
                          )
try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")  # checking , mode off or not !
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

    
