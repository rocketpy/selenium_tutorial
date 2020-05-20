#  Test  Case
#  https://selenium-python.readthedocs.io/page-objects.html
import page
import unittest
from selenium import webdriver


# PATH = "C:\Program Files\chromedriver.exe"  

class Search(unittest.TestCase):
    
    def set_up(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver = .get("https"// ... ")

    def test_case(self):
        print("Some message")
        assert True
    
    def tear_down():
        self.driver.close()
          
                                               
if __name__=="__maun__":
    unittest.main()
