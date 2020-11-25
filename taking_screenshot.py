import random
from selenium import webdriver


PATH = "C:\\chromedriver.exe" 
# FILE_NAME = "first"
# or
FILE_NAME = random.randint(1, 1000000)

driver = webdriver.Chrome(PATH) 
driver.maximize_window()
driver.get("https://")
driver.get_screenshot_as_file(FILE_NAME + ".png")  # .jpg

driver.quit()
# driver.close()
