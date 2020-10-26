from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement


options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'ua_UA'})

browser = BaseWebDriver()
browser.driver = Chrome(chrome_options=options)

browser.visit('https://www...')


#  splinter API only
from splinter import Browser
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': 'ua_UA'})

browser = Browser('chrome', options=options)

browser.visit('http://www...')
