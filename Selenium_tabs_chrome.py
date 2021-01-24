import time
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("user-agent=...")

driver = webdriver.Chrome(executable_path="/PycharmProjects/selenium_python/chromedriver/chromedriver", 
                          options=options)


