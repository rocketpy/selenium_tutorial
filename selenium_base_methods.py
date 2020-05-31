from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


# use PROXY
PROXY = "12.345.678.910:8080"
options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(chrome_options=options)  # Firefox()

# without Proxy
driver = webdriver.Chrome(path)  # or  webdriver.Chrome(executable_path=path)
driver.get("https:// ... ")  # go to some URL

# checking some INFO
print(driver.title)  # title of a page
print(driver.current_url)  # check a current url

# for checking some element for exist
print(elem.is_displayed())  # return True or False
print(elem.is_enabled())  # use for check_box , return True or False

# use INPUT field on web_page
search = driver.find_element_by_id('text')  # input id_name 
search.send_keys('some_word or text')  #  she is so cute and beautiful ))
search.send_keys(Keys.ENTER)  # ENTER , it's a button at keyboard
search.clear()  # clean field before send a new text


# to close window
driver.quit()  
# or 
driver.close()
