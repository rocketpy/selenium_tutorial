# import selenium
from selenium import webdriver


# setup driver's
firefoxdriver = webdriver.Firefox(executable_path="Path to Firefox driver")
# link to driver  "https://github.com/mozilla/geckodriver/releases"

chromedriver = webdriver.Chrome(executable_path="Path to Chrome driver")
# link to driver  "https://sites.google.com/a/chromium.org/chromedriver/downloads"

iedriver = webdriver.IE(executable_path="Path to IEDriverServer.exe")
# link to driver  "http://selenium-release.storage.googleapis.com/index.html"

edgedriver = webdriver.Edge(executable_path="Path to MicrosoftWebDriver.exe")
# link to driver  "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"

operadriver = webdriver.Opera(executable_path="Path to operadriver")
# link to driver  "https://github.com/operasoftware/operachromiumdriver/releases"

#  SafariDriver now requires manual installation of the extension prior to automation !!!

