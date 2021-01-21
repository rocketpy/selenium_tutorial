#  An iframe is used to embed HTML documents in other HTML documents
# We cannot click on elements present in iframe directly. To click on an element inside an iframe using XPath or any other locator,
# we need to switch to the frame first and then click.

# main steps:
"""
Step 1: Invoke browser and load web page
Step 2: Identify iframe using any locators
Step 3: Switch to iframe using switchTo method
Step 4: Act on elements inside iframe
Step 5: switch back to default content
"""

iframe_list =  driver.find_elements_by_tag_name("iframe")
length = len(iframe_list)
# print(length)

# we can switch to frames using 3 ways

# By using index of the frame
# By using Name or Id of the frame
# By using frame Web Element


#  switch to iframe by index

# Index is the position at which an iframe occurs in the HTML page. Using this index we can switch to it.
# Index of the iframe starts with ‘0’. Suppose if there are 100 frames in page,
# we can switch to the iframe by using index like below.

driver.switch_to().frame(0)
driver.switch_to().frame(1)

#  we can alternatively use driver.switch_to.frame() as well as driver.switch_to.default_content()

#  example
import time
from selenium import webdriver


driver = webdriver.Firefox(executable_path="/path/to/geckodriver")
driver.get("http://www...com/iframe.html")

# use any of <br> # by index of the iframe
driver.switch_to_frame(0)

# by ID of the iframe
driver.switch_to_frame("frame_name")

# by name of the iframe
driver.switch_to_frame("frame_name")

# by finding iframe as web element
frame_element = driver.find_element_by_id("id_name")
driver.switch_to_frame(frame_element)

driver.find_element_by_id("id_name").click()
time.sleep(5)
driver.switch_to_default_content()

driver.quit()

