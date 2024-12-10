'''
In this example, we will use the webdriver manager (like chromedriver) in the script, we don't have to
install in manuelly.

pip install webdriver-manager --> To install the module

chromedrivermanager().install() --> This method first checks if an appropriate / compatible version 
of chromedriver is installed on your system of not. If yes, it returns the path to it, else it downloads the
compatible version and returns the path to it, which means you don't need to take care of it manuelly.
'''

# importing modules --> selenium, webdriver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# importing the ChromeDriverManager class to get the chromedriver --> chromedriver interacts with the browser
# for us.
from webdriver_manager.chrome import ChromeDriverManager

# Creating an instances
chrome_options = Options()

# we don't want chrome to close after the script has completed.
chrome_options.add_experimental_option('detach', True)

# Creating the browser isstance
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Getting website
browser.get('https://www.neuralnine.com')
browser.maximize_window() # maximizing the window by default



