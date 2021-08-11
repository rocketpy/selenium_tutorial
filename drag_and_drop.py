# For use drag and drop, either moving an element by a certain amount, or on to another element:
from selenium import webdriver


element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()

"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("http://")
source_element = driver.find_element_by_id('bin')
dest_element = driver.find_element_by_id('two')
ActionChains(driver).drag_and_drop(source_element, dest_element).perform()

"""
 
