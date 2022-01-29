import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Important tags 
"""
 < table > – Defines an HTML table
 < th > – Contains header information in a table
 < tr > – Defines a row in a table
 < td > – Defines a column in a table
"""


URL = "https://www..."

class TableDataTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_get_num_rows_(self):
        driver = self.driver
        driver.get(URL)
       
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "")))
    nums_rows = len(driver.find_elements_by_xpath("//*[@id='']/t/tr"))
    
    def test_get_num_cols_(self):
        driver = self.driver
        driver.get(test_url)
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "...")))
        # nums_cols = len (driver.find_elements_by_xpath("//*[@id='']/tbody/tr/th"))
        nums_cols = len (driver.find_elements_by_xpath("//*[@id='']/tbody/tr[2]/td"))


