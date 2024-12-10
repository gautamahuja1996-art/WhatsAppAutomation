'''
.text attribute get's you the visible text of the needed element or page

Before finding an element on a page, you need to make sure page is loaded properly, otherwise, it will
throw and error. So can add a wait for a specific thing to exist/load on a page by using the
WebDriverWait and expected_conditions classes

WebDriveWait class makes the browser wait for specified time.
.unitl() method checks if the expected condition is met in that time frame or not.
If the condition is met, it returns the element, else, timeout exception is raised.
We can handle all of this using try-except in python

try:
    main_element = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, "rso"))
        )
except:
    browser.quit()

Instead of By.ID, we can use By.NAME etc.

find_element --> Returns the first element which satisfies the 'id' or 'class' condition
find_elements --> Returns the list of all elements which satisfies the 'id' or 'class' condition

'''

# importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# path to chromedriver
path = r'C:/Program Files (x86)/chromedriver.exe'

# service instance
service = Service(path)

# browser instance
browser = webdriver.Chrome(service=service)

# getting google page
browser.get('https://www.google.com')

# accessing the search bar
search_bar = browser.find_element(by= By.ID, value="APjFqb")

# writing something in textbox
search_bar.send_keys("What is python?")

# hitting enter
search_bar.send_keys(Keys.RETURN)

# [Don't find the element directly]
# finding the element with id 'rso'
# main_element = browser.find_element(by=By.ID, value="rso")
# print(main_element.text)

# try-except statement
try:
    main_element = WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.ID, "rso"))
        )
    
    # printing the text content in the element if we are able to find it
    # print(main_element.text)

    # getting all the heading names within main_element
    # elements : <h3 class="LC20lb MBeuO DKV0Md">Introduction to Python</h3>
    # class: LC20lb MBeuO DKV0Md
    headings = main_element.find_elements(By.TAG_NAME, "h3")
    print(headings)

    from time import sleep
    sleep(10)

finally:
    browser.quit()