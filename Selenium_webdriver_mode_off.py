import time
from selenium import webdriver


# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("user-agent=...")

#  webdriver mode OFF

#  for ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# for ChromeDriver version 79.0.3945.16 or higher
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(executable_path="...",
                          options=options
                         )

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")  # checking , working or not a mode_off !
    # time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
 
