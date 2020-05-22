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
