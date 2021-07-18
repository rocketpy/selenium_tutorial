import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Test(unittest.TestCase):
    def test_move_to_element(self):
        driver = webdriver.Chrome(executable_path=r'/chromedriver.exe')
        driver.implicitly_wait(30)
        driver.get("https://www...")
        menu = driver.find_element_by_id("sub-menu")
        actions = ActionChains(driver)
        actions.move_to_element(menu)
        actions.perform()

if __name__ == "__main__":
    unittest.main()
