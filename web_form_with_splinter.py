from splinter import Browser
# https://splinter.readthedocs.io/en/latest/tutorial.html


FIRST_NAME = ''
LART_NAME = ''
EMAIL_ADDRESS = ''

# browser = Browser()  firefox using by default
browser = Browser('firefox')

browser.visit('https://www...')

browser.find_by_id('First Name').first.find_by_tag('input').fill(FIRST_NAME)
browser.find_by_id('Last Name').first.find_by_tag('input').fill(LAST_NAME)
browser.find_by_id('Email Address').first.find_by_tag('input').fill(EMAIL_ADDRESS)


# button = browser.find_by_name('btnK')
# button.click()

browser.find_by_js('submit').first.click()

# print(browser.url)
# print(browser.title)
# print(browser.html)

browser.quit()
