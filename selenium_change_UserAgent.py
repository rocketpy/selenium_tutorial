# checking a your User-Agent  !!!
agent = driver.execute_script("return navigator.userAgent")
print(agent)
print(driver.execute_script("return navigator.userAgent"))


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#  for Chrome
opts = Options()
user_agent = "any agent"
opts.add_argument("user-agent=user_agent")
driver = webdriver.Chrome(chrome_options=opts)
#  or
opts = Options()
opts.add_argument("user-agent=[user-agent string]")
# opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
driver = webdriver.Chrome(chrome_options=opts)



#  User-Agent setup in Firefox !!!
from selenium import webdriver


profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "[user-agent string]")
# profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")
driver = webdriver.Firefox(profile)



#  way to pass driver path with other details
driver = webdriver.Firefox(profile, executable_path="path to geckodriver")

driver = webdriver.Chrome(chrome_options=opts, executable_path="path to chromedriver")

