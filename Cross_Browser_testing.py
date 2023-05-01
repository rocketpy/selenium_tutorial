import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class CrossBrowserTest(unittest.TestCase):

    def setUp(self):
        username = os.environ.get('USERNAME')
        access_key = os.environ.get('ACCESS_KEY')
        caps = webdriver.ChromeOptions()

        # self.driver = webdriver.Safari()
        # self.driver = webdriver.Edge()
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
 
    def tearDown(self):
        self.driver.quit()

    def test_sauce_labs(self):
        self.browser.get("https://www...com")
        element = self.browser.find_element(By.XPATH, '//a[text()="Platform"]')
        self.assertTrue(element.is_displayed())
        element.click()
        pricing_link = self.browser.find_element(By.XPATH, '//a[text()="Pricing"]')
        self.assertTrue(pricing_link.is_displayed())

if __name__ == '__main__':
    unittest.main(verbosity=2)
