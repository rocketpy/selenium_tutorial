from selenium import webdriver


path = "C:\Program Files\chromedriver.exe" 
driver = webdriver.Chrome(path) 
driver.get("https://youtube.com")

search = driver.find_element_by_xpath("...")  # input field 
search.send_keys("some_word")

search_button = driver.find_element_by_xpath("...")  # button of search field
search_button.click()

driver.quit()
