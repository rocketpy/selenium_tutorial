from selenium import webdriver


service = webdriver.firefox.service.Service('geckodriver', port=1234)
driver = webdriver.Firefox(service=service)
driver.get('https://')
