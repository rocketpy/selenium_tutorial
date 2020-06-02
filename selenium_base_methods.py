from time import sleep
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

#  path to webdriver
PATH = "C:\Program Files\chromedriver.exe" #  or  r"C:\Program Files\chromedriver.exe" 

# without Proxy
driver = webdriver.Chrome(path)  # or  webdriver.Chrome(executable_path=path)
driver = webdriver.Firefox(path)
driver = webdriver.Ie(path)

# maximize window
driver.maximize_window()

#  timeout for loading web_page
driver.set_page_load__timeout(10)

#  go to some URL
driver.get("https:// ... ")  

#  change URL
driver.get("https://...")

driver.get(response.url)  #  tested with scrapy or requests   
time.sleep(3)   
driver.refresh()


# checking some INFO
print(driver.title)  # title of a page
print(driver.current_url)  # check a current url

# Conditional commands
# for checking some element for exist or selected
print(elem.is_displayed())  # return True or False
print(elem.is_enabled())  # use for check_box , return True or False
print(elem.is_selected())  # status of some checkbox or radio_button , selected or not

# working with opened windows
tabs = driver.window_handles  # get a list opened tabs
driver.switch_to.window(tabs[1])  # change window to second opened tab !!!

# use INPUT field on web_page
search = driver.find_element_by_id('text')  # input id_name 
search.send_keys('some_word or text')  #  she is so cute and beautiful ))
search.send_keys(Keys.ENTER)  # ENTER , it's a button at keyboard ,  send_keys(Keys.CTRL + 'c')
search.clear()  # clean field before send a new text

# cklick on button
driver.find_element_by_id("button_id").click()
#  or
driver.find_element(By.ID, "button_id").send_keys("some_word")  # provide value into text box !!!

# use Select
#  using Select , by visible_text
elem = Select(driver.find_element_by_xpath("elem_xpath")).select_by_visible_text("some_text") 
#  or by_value
elem = Select(driver.find_element_by_xpath("elem_xpath")).select_by_value("1")


# find many same elements on page
same_elems = driver.find_elements(By.CLASS_NAME, "class_name")  # text_field  , for example

# find element by CSS selector
elem = driver.find_element_by_css_selector("input[value=some_name]")

#  ActionChains cases
# for copy img to computer memory (like  CTRL+C  buttons)
action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

#  Waits 
# wait some time for download a page or some elements
wait = WebDriverWait(driver, 5)  # Best pratice , use Explicit Wait !!!
#  or
element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Open')))
# or
#  Implicitly Wait , waits only until an item appears in the DOM !!!
driver.implicitly_wait(10) 


# scroll page down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 

# refresh web_page
driver.refresh()

# to close window
driver.quit()  
# or 
driver.close()
