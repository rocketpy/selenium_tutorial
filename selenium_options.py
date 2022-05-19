from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()

options.add_argument("--headless")
options.add_argument("--log-level NONE")

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(chrome_options=chrome_options)


# for Firefox
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


firefox_options = Options()

firefox_options.set_headless()
driver = webdriver.Firefox(options=firefox_options)


# Selenium Wire Options
from seleniumwire import webdriver


# selenium-wire proxy settings
options = {'proxy': {'http': 'http://myusername:password@myproxyserver.com:123456', 
                     'https': 'http://myusername:password@myproxyserver.com:123456', 
                     'no_proxy': 'localhost,127.0.0.1'}}

# other chrome options
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')

driver = webdriver.Chrome('chromedriver', options=chrome_options, seleniumwire_options=options)

