'''
common module --> This module is a common place for commonly used classes like Keys, By
by class --> To locate elements
Keys class --> To enter text of hit keys over elements
driver.page_source --> Gives you the source code of the page
'''

# To communicate with the webdriver installed
from selenium import webdriver

# to specify the path, let's import service object
from selenium.webdriver.chrome.service import Service

# importing By class which is used to locate elements
from selenium.webdriver.common.by import By

# importing keys class
from selenium.webdriver.common.keys import Keys

# path to chromedriver
path = r'C:\Program Files (x86)\chromedriver.exe'

# Creating service isntance
service = Service(path)

# creating instance
driver = webdriver.Chrome(service=service)

# getting google.com
driver.get('https://www.google.com')

# getting the search bar by id
# find_element_by_id searches through the id and returns the object
search_box = driver.find_element(By.ID, "APjFqb")

# writing something in the search bar
search_box.send_keys("What is google?")

# Hitting enter
search_box.send_keys(Keys.RETURN)

# waiting for 2 seconds
from time import sleep
sleep(2)

# closing the tab
driver.close()