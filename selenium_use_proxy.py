from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


proxy = "12.345.678.910:8080"
options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % proxy)
chrome = webdriver.Chrome(chrome_options=options)
chrome.get("https://www ... ")


#  or

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "ip_addr:port"
prox.socks_proxy = "ip_addr:port"
prox.ssl_proxy = "ip_addr:port"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)


# or

from selenium import webdriver


PROXY = "12.345.678.910:8080"
webdriver.DesiredCapabilities.FIREFOX['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "autodetect":False
}
driver = webdriver.Firefox()
driver.get('http://www.whatsmyip.org/')
