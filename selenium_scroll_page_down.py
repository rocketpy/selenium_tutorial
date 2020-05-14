from selenium import webdriver
from time import sleep


driver = webdriver.Firefox()
driver.get("https:// ...  ")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # scroll down the complete page height or a specific height !!!
time.sleep(3)
driver.close()  # driver.quit()

#  or
driver.execute_script("window.scrollTo(0, Y)")  #  Y  is a height , 1080 for example

#  or
label.sendKeys(Keys.PAGE_DOWN
               
#  or
from selenium.webdriver.common.keys import Keys

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)

#  to scroll to a page with infinite loading !!!
time_to_sroll = 0.5

# scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(time_to_scroll)
    # new scroll height , compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
               
