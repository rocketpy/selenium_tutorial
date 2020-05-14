import time
from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https:// ...  ")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # scroll down the complete page height or a specific height !!!

time.sleep(3)
driver.close()  # driver.quit()

#  or



#  or

from selenium.webdriver.common.keys import Keys

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
