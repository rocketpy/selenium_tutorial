import time
import random
# from selenium import webdriver
from seleniumwire import webdriver
from fake_useragent import UserAgent


URL = "https://www...com/"

user_agents_list = []
options = webdriver.ChromeOptions()
useragent = UserAgent()

#  examples , sending u_a
# options.add_argument("user-agent=BlaBlaBla:)")
# options.add_argument("user-agent=some example u_a")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")

options.add_argument(f"user-agent={useragent.random}")

# options.add_argument("--proxy-server=123.456.78.90:8000")

proxy_options = {"proxy": 
                {"https": f"http://{login}:{password}@123.456.78.90:8000"}
                }

# driver = webdriver.Chrome(executable_path="//chromedriver",
#                           options=options
#                           )

driver = webdriver.Chrome(executable_path="/chromedriver",
                          seleniumwire_options=proxy_options
                          )

# "C:\\users\\chromedriver.exe"
# r"C:\users\chromedriver.exe"

try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    time.sleep(3)
    driver.get(url="https:www...com/")
    time.sleep(3)

    driver.refresh()
    driver.get_screenshot_as_file("file_name.png")
    driver.get(url="https://www...com/")
    time.sleep(3)
    driver.save_screenshot("file_name.png")
    time.sleep(3)

    driver.get("https://2ip.ru")
    time.sleep(3)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
