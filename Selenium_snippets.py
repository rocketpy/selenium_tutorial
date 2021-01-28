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
