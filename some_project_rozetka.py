import os
import csv
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC


#PATH = "C:\Program Files\chromedriver.exe" 
#driver = webdriver.Chrome(PATH) 

PROXY = "12.345.678.910:8080"
options = WebDriverWait.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(chrome_options=options)

driver.get("https://rozetka.com.ua/")

notebooks_pc_button = "/html/body/app-root/div/div[1]/app-rz-main-page/div/main/main-page-content/app-fat-menu-tablet/nav/ul/li[1]/a"
notebooks = "/html/body/app-root/div/div[1]/rz-super-portal/div/main/section/sp-dynamic-widgets/sp-widget-list[1]/section/ul/li[1]/sp-list-tile/div/a[2]"
smart_phones = "/html/body/app-root/div/div[1]/app-rz-main-page/div/main/main-page-content/app-fat-menu-tablet/nav/ul/li[2]/a"

#  searching something
search = driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-header/header/div/div[2]/div[3]/form/div/div/input')
time.sleep(1) 
search.send_keys('name of object')
time.sleep(1)
# search.send_keys(Keys.ENTER)
# time.sleep(1)
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-header/header/div/div[2]/div[3]/form/button').click()


# get all notebooks
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-main-page/div/main/main-page-content/app-fat-menu-tablet/nav/ul/li[1]/a').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/rz-super-portal/div/main/section/sp-dynamic-widgets/sp-widget-list[1]/section/ul/li[1]/sp-list-tile/div/a[2]').click()
time.sleep(3)

# scroll page down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(7)
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/rz-category/div/main/ctg-catalog/div/div[2]/section/div/ctg-pagination/div/a/span').click()
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(5)
nums_pages_xpath = "/html/body/app-root/div/div[1]/rz-category/div/main/ctg-catalog/div/div[2]/section/div/ctg-pagination/rz-paginator/div/ul/li[9]/a"

"""
# get  all grid with all cells
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
grids = soup.find('ul', {'class': 'catalog-grid'})
cells = grids.find_all('li')  # return a list of all li
nums_pages = soup.find('a', {'class': 'pagination__link'}).text
"""

page_nums = nums_pages_xpath

with open('result.csv', 'w') as f:
    f.write('name', 'price', 'img_url')

for i in range(1, page_nums + 1):
    page_num = (page_nums - len(str(i))) + '0' + str(i)
    url = "https://https://rozetka.com.ua/notebooks/c80004/page=" + page_num

    driver.get(url)
    
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    grids = soup.find('ul', {'class': 'catalog-grid'})
    cells = grids.find_all('li')  # return a list of all li
    nums_pages = soup.find('a', {'class': 'pagination__link'}).text
    
    #elems = driver.find_elements_by_xpath('')
    name = driver.find_elements_by_('')
    price = driver.find_elements_by_('')
    img_url = driver.find_elements_by_('')
    
    page_items = 60
    
    with open('results.csv', 'a') as f:
        for i in range(pages_items):
            f.write(name[i].text + "," + price[i].text + '\n')

      
    
"""
#  write data to csv file
def write_csv(data):
    with open('.csv', 'a') as f:
        order = ['name', 'price', 'img_href']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)
  
#  pagination 
# url = 'https:// ... '
pattern = 'https:// ... /{}.html
for i in range(1, 21):
    url = pattern.format(str(i))
"""                

# xpath's of first cell elements !!!
img_xpath = "/html/body/app-root/div/div[1]/rz-category/div/main/ctg-catalog/div/div[2]/section/div/ctg-grid/ul/li[1]/app-goods-tile-default/div/div[2]/a[1]/img[2]"
name_xpath = "/html/body/app-root/div/div[1]/rz-category/div/main/ctg-catalog/div/div[2]/section/div/ctg-grid/ul/li[1]/app-goods-tile-default/div/div[2]/a[2]/span"
price_xpath = "/html/body/app-root/div/div[1]/rz-category/div/main/ctg-catalog/div/div[2]/section/div/ctg-grid/ul/li[1]/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span[1]"

#url_img = driver.find_element_by_xpath(img_xpath).get_attribute('data-url') 
#notebook_name = driver.find_element_by_class_name("goods-tile__title").text
#notebook_price = driver.find_element_by_class_name("goods-tile__price-value").text
