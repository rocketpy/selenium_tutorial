import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("user-agent=...")

# for ChromeDriver version 79.0.3945.16 or over
# options.add_argument("--disable-blink-features=AutomationControlled")  #  using webdriver mode off

# headless mode's
options.add_argument("--headless")  # best practice use this one
#  OR
options.headless = True

driver = webdriver.Chrome(executable_path="PycharmProjects/selenium_python/chromedriver/chromedriver",
                          options=options
                         )
try:
    driver.get("https://www...")
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
