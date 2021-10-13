# Library provides the way to automatically manage drivers for different browsers

# PyPi: https://pypi.org/project/webdriver-manager/
# Github: https://github.com/SergeyPirogov/webdriver_manager

# pip install webdriver-manager

# Before: You should download binary chromedriver, unzip it somewhere in you PC and set path to this driver like this:

webdriver.Chrome('/home/user/drivers/chromedriver')

ChromeDriverManager(path=custom_path).install()


# Use with Chrome:
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


# Use with Chromium:
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())


# Use with FireFox:
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


# Use with IE
from selenium import webdriver
from webdriver_manager.microsoft import IEDriverManager

driver = webdriver.Ie(IEDriverManager().install())

 
# Use with Edge
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())


# Use with Opera
from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager

driver = webdriver.Opera(executable_path=OperaDriverManager().install())


# If the Opera browser is installed in a location other than C:/Program Files or C:/Program Files (x86) on windows
# and /usr/bin/opera for all unix variants and mac, then use the below code,
from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager

options = webdriver.ChromeOptions()
options.add_argument('allow-elevated-browser')
options.binary_location = "C:\\Users\\USERNAME\\FOLDERLOCATION\\Opera\\VERSION\\opera.exe"
driver = webdriver.Opera(executable_path=OperaDriverManager().install(), options=options)

