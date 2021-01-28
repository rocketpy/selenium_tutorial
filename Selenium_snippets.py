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
        
       
