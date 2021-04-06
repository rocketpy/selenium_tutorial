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


# Options, browser arguments
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()

options.add_argument("--headless")  # open browser in headless mode. Works in both Chrome and Firefox browsers
options.add_argument("--incognito")  # open private chrome browser 
options.add_argument("--start-maximized")  # start browser maximized to screen. Requires only for Chrome browser. Firefox by default starts maximized
options.add_argument("--disable-notifications")  # disable notifications, works Only in Chrome browser


driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")

#  OR
options = Options()
options.add_argument("--incognito", "--start-maximized", "--headless")
driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")


#  go to some URL
driver.get("https://www...")  # go to page
driver.back()
driver.forward()
driver.refresh()  # update page

# get browser details
driver.title
driver.window_handles
driver.current_window_handles
driver.current_url
driver.page_source

# get some element or elements
driver.find_element_by_  #  return first element matching the given locator argument
driver.find_elements_by_  # return a list with all elements matching the given locator argument

# by id
# <input id="q" type="text" />
element = driver.find_element_by_id("q")

# by name
# <input id="q" name="search" type="text" />
element = driver.find_element_by_name("search")

# by class_name
# <div class="username" style="display: block;">…</div>
element = driver.find_element_by_class_name("username")

# cklick on checkbox with javascript
driver.execute_script("document.getElementById('personalData').checked = true")

click = driver.find_element_by_class_name('checkbox checkbox-off')
click.click()


