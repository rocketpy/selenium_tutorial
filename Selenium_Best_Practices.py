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
    
    
#  4. Use maximize the browser window. 

#  5. Set the browser zoom level to 100 percent.

#  6. Create a browsers compatibility matrix or table for cross browser testing.   

#  7. Use design patterns and principles like Page Object Model (POM).  

#  8. Implement logging and reporting.

#  9. For parameterization use Data-Driven Testing.

#  10. Follow a uniform directory structure.

#  11. Use BDD framework with Selenium.

#  12. Come up with autonomous test case design.

#  13. Do not use a Single driver implementation.

#  14. Use assert and verify in appropriate scenarios.

#  15. Leverage parallel testing in Selenium.

#  16. Avoid code duplication (or wrap Selenium calls).


#   Worst practices for Automation testing with Selenium :

#  1. Link spidering (or crawling).
#  2. Automation of logins on Gmail, Facebook and other related platforms.
#  3. Performance testing.
#  4. Avoid test dependency.
#  5. Two-Factor authentication (2FA).
#  6. CAPTCHAS.
#  7. File downloads.

 
