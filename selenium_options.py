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

