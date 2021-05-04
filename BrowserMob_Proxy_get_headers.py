import settings
from selenium import webdriver
from browsermobproxy import Server
from selenium.webdriver import DesiredCapabilities


config = settings.Config

server = Server(config.BROWSERMOB_PATH)
server.start()
proxy = server.create_proxy()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy.proxy)
chrome_options.add_argument('--headless')

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True
capabilities['acceptInsecureCerts'] = True

driver = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities,
                          executable_path=config.CHROME_PATH)

proxy.new_har("sahibinden", options={'captureHeaders': True})
driver.get("https://www...")

entries = proxy.har['log']["entries"]
for entry in entries:
    if 'request' in entry.keys():
        print(entry['request']['url'])
        print(entry['request']['headers'])
        print('\n')

proxy.close()
driver.quit()

