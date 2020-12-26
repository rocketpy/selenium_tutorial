#  Extends Selenium to give you the ability to inspect requests made by the browser.

#  PyPi:  https://pypi.org/project/selenium-wire/

#  pip install selenium-wire

#  example
from seleniumwire import webdriver 


driver = webdriver.Firefox()

driver.get('https://www.google.com')

for request in driver.requests:
    if request.response:
        print(request.url,
              request.response.status_code,
              request.response.headers['Content-Type']
              )
