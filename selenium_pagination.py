import re
import json
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')  # disable infobar in Chrome browser
driver=webdriver.Chrome(chrome_options=options, executable_path=r'/Users/.../chromedriver')

#  pagination use URL
url = 'https:// ... '
pattern = 'https:// ... /{}.html'  # use method format for add a number of page
for i in range(1, 21):  # 21 pages
    url = pattern.format(str(i))
    
    
driver.get(url)

def main():
    all_data = []
    select = Select(driver.find_element_by_xpath("... and @id='...']"))
    list_options = select.options

    for item in range(len(list_options)):
        select = Select(driver.find_element_by_xpath(""))
        select.select_by_index(str(item))
        driver.find_element_by_css_selector("").click()
        number_of_pages = int(driver.find_element_by_xpath("").text)  # get numbers of all pages
        for j in range(number_of_pages - 1):  # loop for all pages
            all_data.extend(getData())
            driver.find_element_by_xpath("//a[contains(text(),'Next')]").click()
            time.sleep(1)
        driver.get(url)

 with open( 'filename.json', 'w+' ) as f:
     json.dump( all_data, f )
        
 def get_data():
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
        
    
 driver.quit()


if __name__ == "__main__":
    main()
