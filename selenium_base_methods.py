from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(path)  # or  webdriver.Chrome(executable_path=path)
driver.get("https:// ... ")  # go to some URL

driver.title  # title of a page
print(driver.current_url)  # check a current url

elem.clear()  # clean field before send a new text


# to close window
driver.quit()  
# or 
driver.close()
