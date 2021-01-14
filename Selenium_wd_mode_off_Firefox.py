import time
from selenium import webdriver


options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "user-agent")

options.set_preference("dom.webdriver.enabled", False)

driver = webdriver.Firefox(executable_path="...",
                           options=options
                          )
