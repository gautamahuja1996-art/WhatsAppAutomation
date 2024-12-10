'''
selenium: Framework that allows you to interact with any html elements online.

Chromedriver : A tool that provides programatic control of chrome browser (helps you to control chrome
through code) [Download it: https://chromedriver.chromium.org/downloads]
Step 1: Go to google chrome settings --> About chrome (check the version of chrome)
Step 2: Go to the link above, download the same version of chromeDriver
Step 3: [Not mandatory] Move the chromeDriver application in the program files(x86) so that we can reference
it from there (a bit safe there). [File path: C:\Program Files (x86)\chromedriver.exe]

Install selenium : pip install selenium

The webdriver class of the selenium framework, interacts with your installed webdriver (chrome driver in
our case to do the browser automation.)

To close the opened tab --> driver.close()
To close the browser --> driver.quit()
'''

# getting webdriver class
from selenium import webdriver

# getting Service class to refer to our chrome driver
from selenium.webdriver.chrome.service import Service

# path to our chromedriver
path = r'C:\Program Files (x86)\chromedriver.exe'

# creating instance of Service class
service = Service(path)

# creating an instance to control our chrome
# this webdriver can interact with other browser's webdrivers as well (like firefox webdriver etc.)
driver = webdriver.Chrome(service=service)

# getting a website
driver.get('https://www.google.com')

# getting the title of the page
print(driver.title)