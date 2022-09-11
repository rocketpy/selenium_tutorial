#  SeleniumBase is a Python framework for web automation

#  Docs:  https://github.com/seleniumbase/SeleniumBase
#  PyPi:  pip install seleniumbase

#  common SeleniumBase methods
"""
self.open(URL)  # Navigate to the web page
self.click(SELECTOR)  # Click a page element
self.type(SELECTOR, TEXT)  # Type text (Add "\n" to text for pressing enter/return.)
self.assert_element(SELECTOR)  # Assert element is visible
self.assert_text(TEXT)  # Assert text is visible (has optional SELECTOR arg)
self.assert_title(PAGE_TITLE)  # Assert page title
self.assert_no_404_errors()  # Assert no 404 errors from files on the page
self.assert_no_js_errors()  # Assert no JavaScript errors on the page (Chrome-ONLY)
self.execute_script(JAVASCRIPT)  # Execute JavaScript code
self.go_back()  # Navigate to the previous URL
self.get_text(SELECTOR)  # Get text from a selector
self.get_attribute(SELECTOR, ATTRIBUTE)  # Get a specific attribute from a selector
self.is_element_visible(SELECTOR)  # Determine if an element is visible on the page
self.is_text_visible(TEXT)  # Determine if text is visible on the page (optional SELECTOR)
self.hover_and_click(HOVER_SELECTOR, CLICK_SELECTOR)  # Mouseover element & click another
self.select_option_by_text(DROPDOWN_SELECTOR, OPTION_TEXT)  # Select a dropdown option
self.switch_to_frame(FRAME_NAME)  # Switch webdriver control to an iframe on the page
self.switch_to_default_content()  # Switch webdriver control out of the current iframe
self.switch_to_window(WINDOW_NUMBER)  # Switch to a different window/tab
self.save_screenshot(FILE_NAME)  # Save a screenshot of the current page
"""

# for reports use:
# pytest test_suite.py --html=report.html
# or
# pytest test_suite.py --dashboard --html=report.html


# find all links on the page
links = driver.find_elements_by_xpath("//a[@href]")
for link in links:
    print(elem.get_attribute("href"))
    
    
# click on the alert box
WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()


#  example , test login
from seleniumbase import BaseCase


class SwagLabsLoginTests(BaseCase):

    def login_to_swag_labs(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open("https://www.saucedemo.com/")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce")
        self.click('input[type="submit"]')

    def test_swag_labs_login(self):
        """ This test checks standard login for the Swag Labs store. """
        self.login_to_swag_labs()
        self.assert_element("div.header_label div.app_logo")
        self.assert_text("Products", "div.product_label")

        
#  here's an example where clicking a button makes a hidden element visible !
from seleniumbase import BaseCase


class VisualLayoutTest(BaseCase):

    def test_applitools_layout_change_failure(self):
        self.open('https://www...')
        
        self.check_window(name="helloworld", baseline=True)
        
        # Click a button that changes the text of an element
        self.click('...')
        
        # Click a button that makes a hidden element visible
        self.click("button")
        self.check_window(name="helloworld", level=3)

        
#  here's an example where a button is removed from a web page
from seleniumbase import BaseCase


class VisualLayoutTest(BaseCase):

    def test_python_home_layout_change_failure(self):
        self.open('https://www...')
        self.check_window(name="python_home", baseline=True)
        self.remove_element('a.button')
        self.check_window(name="python_home", level=3)        
        
       
