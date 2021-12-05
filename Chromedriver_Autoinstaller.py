# chromedriver-autoinstaller - Automatically download and install chromedriver that supports the currently installed version of chrome.

# Github - https://github.com/yeongbin-jo/python-chromedriver-autoinstaller

# pip install chromedriver-autoinstaller

# Driver - https://chromedriver.chromium.org/

# Example

from selenium import webdriver
import chromedriver_autoinstaller


# Check if the current version of chromedriver exists and if it doesn't exist, download it automatically,
# then add chromedriver to path
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

