# The port of the WebDriver server (i.e. geckodriver --port) is controlled by the parameter passed to the Service(port=)
from selenium import webdriver


service = webdriver.firefox.service.Service('geckodriver', port=1234)
driver = webdriver.Firefox(service=service)
driver.get('https://')

"""
driver = webdriver.Firefox(options=opts, 
service_args=["--marionette-port", "2828"])  # with Marionette port

# in terminal: geckodriver --help

OPTIONS:
  -b, --binary Path to the Firefox binary
  --log Set Gecko log level [possible values: fatal, error, warn, info, config, debug, trace]
  --marionette-host Host to use to connect to Gecko (default: 127.0.0.1)
  --marionette-port Port to use to connect to Gecko (default: system-allocated port)
  --host Host ip to use for WebDriver server (default: 127.0.0.1)
  -p, --port Port to use for WebDriver server (default: 4444)
"""
