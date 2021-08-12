#  Helpful tools for Selenium on Python

# PyPi:  https://pypi.org/project/seletools/
# Docs:  https://github.com/bormando/selenium-tools

# pip install seletools

# Drag & Drop

from seletools.actions import drag_and_drop


driver = webdriver.Chrome()
source = driver.find_element(By.CSS_SELECTOR, "...")
target = driver.find_element(By.CSS_SELECTOR, "...")
drag_and_drop(driver, source, target)


# Scroll

# This one helps to scroll vertically to any element on page, even if it's covered by some other element (like navbar or footer).
# If there's such obstacle - simply add that covering element into scrolling function as element2.
from seletools.actions import scroll_to_top, scroll_to_bottom

driver = webdriver.Chrome()
element1 = driver.find_element(By.CSS_SELECTOR, "...")
element2 = driver.find_element(By.CSS_SELECTOR, "...")  
# optional, used only if you have obastacle (like navbar on footer) on top of the element that you need to scroll to

scroll_to_top(driver, element1, element2)
# OR
scroll_to_top(driver, element1)

scroll_to_bottom(driver, element1, element2)
# OR
scroll_to_bottom(driver, element1)
