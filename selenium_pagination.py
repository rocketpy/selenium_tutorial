import re
import json
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options, executable_path=r'/Users/weaabduljamac/Downloads/chromedriver')

url = 'https://services.wiltshire.gov.uk/PlanningGIS/LLPG/WeeklyList'
driver.get(url)

def getData():
  data = []
  rows = driver.find_element_by_xpath('//*[@id="form1"]/table/tbody').find_elements_by_tag_name('tr')
 for row in rows:
    app_number = row.find_elements_by_tag_name('td')[1].text
    address =  row.find_elements_by_tag_name('td')[2].text
    proposals =  row.find_elements_by_tag_name('td')[3].text
    status =  row.find_elements_by_tag_name('td')[4].text
    data.append({"CaseRef": app_number, "address": address, "proposals": proposals, "status": status})
print(data)
return data
