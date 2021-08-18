#  Extends Selenium to give you the ability to inspect requests made by the browser.

#  PyPi:  https://pypi.org/project/selenium-wire/
#  Github: https://github.com/wkeeling/selenium-wire

#  pip install selenium-wire

#  example
from seleniumwire import webdriver 


# Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors-spki-list')
chrome_options.add_argument('--ignore-ssl-errors')

options = {'proxy': {'http': 'http://myusername:password@myproxyserver.com:123456', 
                     'https': 'http://myusername:password@myproxyserver.com:123456',
                     'no_proxy': 'localhost,127.0.0.1'}}

driver== webdriver.Chrome('chromedriver', options=chrome_options, seleniumwire_options=options)

driver = webdriver.Firefox()

driver.get('https://www.google.com')

for request in driver.requests:
    if request.response:
        print(request.url,
              request.response.status_code,
              request.response.headers['Content-Type']
              )
        
