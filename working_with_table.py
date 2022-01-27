import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www..."

class TableDataTest(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
 
    def test_get_num_rows_(self):
        driver = self.driver
        driver.get(URL)

