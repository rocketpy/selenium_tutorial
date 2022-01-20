#  tor-browser-selenium - A Python library to automate Tor Browser with Selenium.

# Install geckodriver from:  https://github.com/mozilla/geckodriver/releases/

# Github: https://github.com/webfp/tor-browser-selenium

# pip install tbselenium


# Usage

# Using with system tor
# tor needs to be installed (apt install tor) and running on port 9050.

from tbselenium.tbdriver import TorBrowserDriver

with TorBrowserDriver("/path/to/TorBrowserBundle/") as driver:
    driver.get('https://check.torproject.org')


