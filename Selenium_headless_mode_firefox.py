import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "user_agent_name")

options.set_preference("dom.webdriver.enabled", False)  # disable webdriver mode
