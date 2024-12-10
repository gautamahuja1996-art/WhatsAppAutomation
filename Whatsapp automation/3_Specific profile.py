'''
Opening a website in a specific profile -->

Options class helps you in changing browser settings and its behavior such as:
a) Opening specific profiles
b) Managing downloads etc

To get the chrome profile:
In a new tab, enter --> chrome://version [This has all the details of profile settings]
'''

# importing webdriver, service, by, keys, time, options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options  import Options

# path to webdriver
path = r'C:\Program Files (x86)\chromedriver.exe'

# path to chrome profile
profile_path = r'C:\Users\sunst\AppData\Local\Google\Chrome\User Data\Default'
# profile_path = r"C:\Users\sunst\AppData\Local\Google\Chrome\User Data\Profile 10"

# creating instances: service, options
service = Service(path)
chrome_options = Options()

# Adding profile
# chrome_options.add_argument(f'--user-data-dir={profile_path}')
chrome_options.add_argument(f'--user-data-dir={profile_path}')

# Creating instance of browser
chrome_browser = webdriver.Chrome(service=service, options=chrome_options)

# opening techwithtim
chrome_browser.get('https://techwithtim.net')
