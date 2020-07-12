from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
 
  
opts = Options()
opts.set_headless()
assert opts.headless  # without grafic interface !!!
 
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('some key')
search_form.submit()

results = browser.find_elements_by_class_name('result')
# print(results[0].text)

browser.close()
quit()


# find and play some song on bandcamp.com
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


opts = Option()
opts.set_headless()  # without grafic interface !!!
 
browser = Firefox(options=opts)
browser.get('https://bandcamp.com')
browser.find_element_by_class('playbutton').click()

tracks = browser.find_elements_by_class_name('discover-item')
len(tracks)  #  quantity a tracks
tracks[3].click()  # play track number 4

# using pagination , for next 8 tracks
next_button = [i for i in browser.find_elements_by_class_name('item-page')
                   if e.text.lower().find('next') > -1]
next_button.click()

# tracks = browser.find_elements_by_class_name('discover-item')
# assert(len(tracks) == 8) 

section = self.browser.find_element_by_class_name('discover-results')
left_x = section.location['x']
right_x = left_x + section.size['width']
items = browser.find_element_by_class_name('discover_items')
 
tracks = [t for t in items
              if t.location['x'] >= left_x and t.location['x'] < right_x]
 
assert len(tracks) == 8
