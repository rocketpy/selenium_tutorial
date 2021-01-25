#  1. Name the test cases and test suites appropriately.

#  2. Use ( Choose ) the best-suited Web Locators.

#  3. Avoid blocking sleep calls , use  Selenium Waits: Implicit, Explicit, Fluent, and Sleep.
#     https://selenium-python.readthedocs.io/waits.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get("https://www...")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myElement")))
finally:
    driver.quit()
    
    
#  4. Use maximize the browser window    


    
