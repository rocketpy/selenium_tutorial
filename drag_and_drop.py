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

# Taked from: https://www.lambdatest.com/blog/drag-and-drop-in-selenium-python/
"""
Performing Drag And Drop Using ActionChains Class

In this article, we detail the drag_and_drop(source, target) and drag_and_drop_by_offset(source, x_offset, y_offset)
functions of ActionChains class. We will cover all other ActionChains methods in another article.

    drag_and_drop(source, target)

    This method accepts two arguments: source & target. As the name goes, drag and drop ActionChains involves first locating the “source” element,
    then dragging it to the target location and dropping it. To select a source and target element, you may use XPath or CSS Selectors.
    drag_and_drop_by_offset(source, x_offset, y_offset)

    This method requires three arguments: source, x_offset, and y_offset. drag_and_drop_by_offset is an alternative to using drag_and_drop.
    It involves identifying the source element and x,y offsets of the target location. After that, it drops the selected source to the desired offset location.
    Performing chained click_and_hold(element), move_by_offset(xOffset, yOffset), pause(sec) and release() methods

    click_and_hold(argument) method simulates the “left mouse button press and hold” operation. move_by_offset(x,y) resembles moving the cursor
    by specified x and y pixels on respective axes. Pause(sec) function pauses the action for a declared number of seconds.
    Release() method frees the remotely pressed mouse button.
    Performing chained click_and_hold(element), move_to_element(target), pause(sec), move_by_offset(xOffset, yOffset) and release() methods

    move_to_element(arg) is similar to moving the cursor to the specified argument.
    In our case, we’ll use these operations for drag and drop in Selenium Python by simulating click using click_and_hold,
    then dragging by using move_to_element or move_by_offset or combo, and by finally releasing, i.e., dropping the selected element. 
"""

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

 
class DragTest(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
        
 
