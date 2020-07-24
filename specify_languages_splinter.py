from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement


options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'de_DE'})

browser = BaseWebDriver()
browser.driver = Chrome(chrome_options=options)

browser.visit('https://www...')


