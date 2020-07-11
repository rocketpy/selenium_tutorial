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
