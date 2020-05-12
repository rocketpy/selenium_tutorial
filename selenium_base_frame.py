import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


path = "C:\Program Files\chromedriver.exe"  # or , for PyCharm use:  r"C:\Program Files\chromedriver.exe"

#  good practice use PROXY for GOOGLE or YANDEX search !!!
proxy = "12.345.678.910:8080"
options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % proxy)
chrome = webdriver.Chrome(chrome_options=options)

driver = webdriver.Chrome(path)  # or  webdriver.Chrome(executable_path=path)
#driver.get("https:// ... ")

# add your ID and password for VK account
vk_number = ""
vk_password = ""

driver.get('https://yandex.ru')
search = driver.find_element_by_id('text')  # input id_name 
time.sleep(1)  # use sleep , for simulation user actions
search.send_keys('Kate Middleton')  #  she is so cute and beautiful ))
time.sleep(1)
search.send_keys(Keys.ENTER)  # ENTER , it's a button at keyboard
time.sleep(1)
driver.find_element_by_partial_link_text('Картинки').click()  # or  by_link_text()

#  working with opened tabs in browser
tabs = driver.window_handles  # get a list of opened tabs 

driver.switch_to.window(tabs[1])  # change window to second opened tab !!!

imgs = driver.find_elements_by_class_name('serp-item__link')  # get a list of elements
img_link = imgs[1].get_attribute('href')  # get href of img
driver.get(img_link)  # go to this link

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Открыть')))
# driver.find_element_by_partial_link_text('Открыть').click()  #  need check !!!
element.click()
tabs1 = driver.window_handles
driver.switch_to.window(tabs1[2])

action = ActionChains(driver)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# go to VK and make new post
driver.get('https://vk.com/id...')  # put your VK ID
driver.find_element_by_id('quick_email').send_keys(vk_number)
driver.find_element_by_id('quick_pass').send_keys(vk_password)
driver.find_element_by_id('quick_login_button').click()

wait = WebDriverWait(driver, 5)

elem = wait.until(EC.visibility_of_element_located((By.ID, 'post_field')))
elem.clear()
elem.send_keys('Text of message')
action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="send_post"]').click()
driver.quit()
