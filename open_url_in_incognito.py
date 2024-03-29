import webbrowser

url = 'www.blablabla.com'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
webbrowser.get(chrome_path).open_new(url)

# or
from selenium import webdriver

c = webdriver.ChromeOptions()
c.add_argument("--incognito")
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe",options=c)
driver.implicitly_wait(0.5)
driver.get("https://www.....com")


# for Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--private")
browser = webdriver.Firefox(firefox_options=firefox_options)


# for Opera
from selenium import webdriver

options =  webdriver.opera.webdriver.Options()
options.add_argument("private")
driver = webdriver.Opera(executable_path="operadriver",options=options)

# or
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options.add_argument("-private")
driver = webdriver.Firefox(options=firefox_options)
