import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "user_agent_name")

options.set_preference("dom.webdriver.enabled", False)  # disable webdriver mode

# using headless mode 
options.headless = True

driver = webdriver.Firefox(executable_path="PycharmProjects/selenium_python/firefoxdriver/geckodriver",
                           options=options)

try:
    driver.get("https://www...")
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()    
 
