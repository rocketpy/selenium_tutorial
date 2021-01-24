from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("user-agent=...")

driver = webdriver.Chrome(executable_path="/PycharmProjects/selenium_python/chromedriver/chromedriver", 
                          options=options)

try:
    driver.get("https://www...")
    # driver.implicitly_wait(5)
    # print(driver.window_handles)  # driver.window_handles - return a list with opened tabs
    # print(f"Currently URL is: {driver.current_url}")  # checking a current URL
    
    driver.switch_to.window(driver.window_handles[1])  # go to second tab
    print(f"Currently URL is: {driver.current_url}")  # checking a current URL
    
    driver.close()
    
    driver.switch_to.window(driver.window_handles[0])  # go back to first opened tab
    print(f"Currently URL is: {driver.current_url}")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

