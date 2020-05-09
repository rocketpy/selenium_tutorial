import pandas as pd
from selenium import webdriver
from BeautifulSoup import BeautifulSoup


driver = webdriver.Chrome("path to chromedriver")  # example "/user/libs/chromium-browser/chromedriver" 

products = [] 
prices = [] 
ratings = [] 
driver.get("<a href="https://www.blabla.com/">https://www.blabla.com/laptops/</a>")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class':''}):
    name = a.find('div', attrs={'class':''})
    price = a.find('div', attrs={'class':''})
    rating = a.find('div', attrs={'class':''})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 
    
#  run  code

#  write data to CSV file
df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')    
    
