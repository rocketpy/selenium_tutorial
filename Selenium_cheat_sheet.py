# import selenium
from selenium import webdriver


# setup driver's
firefoxdriver = webdriver.Firefox(executable_path="Path to Firefox driver")

chromedriver = webdriver.Chrome(executable_path="Path to Chrome driver")

iedriver = webdriver.IE(executable_path="Path to IEDriverServer.exe")

edgedriver = webdriver.Edge(executable_path="Path to MicrosoftWebDriver.exe")

operadriver = webdriver.Opera(executable_path="Path to operadriver")


