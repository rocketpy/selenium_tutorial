#  Test Automation Project

# Github: https://github.com/startrug/selenium-python-framework

# Project Features
"""
1. framework follows page object pattern
2. data-driven tests - in most tests the option of loading data from an xlsx file has been implemented
3. logger has been implemented in each step of test cases, e.g.
"""
@allure.step("Setting destination to '{1}'")
    def set_destination(self, destination):
        self.logger.info(f"Setting destination: {destination}")
        self.driver.find_element(*SearchHotelsFormLocators.destination_inactive).click()

