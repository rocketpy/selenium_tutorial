# Examples

# Alert Pop-Ups
alert_popup = driver.switch_to.alert

# The accept() method - accepts the alert message
alert_popup = Alert(driver)
alert_popup.accept()

# The dismiss() method cancels the alert prompt
alert_popup = Alert(driver)
alert_popup.dismiss()

# The text() method retrieves and displays the text that is in the alert pop-up
alert_popup = Alert(driver)
# print(alert_popup.text)

# Drag and Drop Operations
from selenium.webdriver import ActionChains

action = ActionChains(driver)


# Example
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
