'''
We can write the JS code as well while automating the browser using selenium.
We have to use .execute_script() function for that.
To scroll we will write JS code.
3 possibilities -->

1) Scrolling by pixels
browser.execute_script("window.scrollBy(a, b)","c") --> This function will scroll the window by 'a' pixels
in horizontal direction, 'b' pixels in the vertical direction and 'c' are additional parameters such as
duration of scrolling, transition etc.
eg --> browser.execute_script("window.scrollBy(0, 1000)", "smooth") --> Scrolling by 1000 pixels in vertical
direction, but smoothly.
eg --> browser.execute_script("window.scrollBy(0, 1000)", "duration: 2000")
'''


# importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep

# paths to driver and chrome profile
driver_path = r'C:\Program Files (x86)\chromedriver.exe'
chrome_directory = r'C:\Users\sunst\AppData\Local\Google\Chrome\User Data'
profile = 'Default'

# creating service and options instance
service = Service(driver_path)
options = Options()

# Adding arguments to the options instance
options.add_argument(f'--user-data-dir={chrome_directory}')
options.add_argument(f'--profile-directory={profile}')
options.add_experimental_option('detach', True)

# Creating the browser instance
try:
    browser = webdriver.Chrome(service=service, options=options)

    # wait for body tag to load [Let's create time instance with 1 min of wait]
    wait = WebDriverWait(browser, 60)
    body_element = wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    # maximizing
    browser.maximize_window()

    # getting to the whatsapp web
    browser.get('https://web.whatsapp.com')

    # wait for div tag with id = pane-side to appear
    pane_side = wait.until(ec.presence_of_element_located((By.ID, 'pane-side')))

    # Finding all elements with class name : _21S-L
    chat_elements = pane_side.find_elements(By.CLASS_NAME, '_21S-L')

    # scrolling by 200 pixels in a smooth manner
    # browser.execute_script("window.scrollBy(0, document.body.scrollHeight)", "")
    # Find the container element using an appropriate locator
    # container = browser.find_element_by_css_selector('.your-container-selector')

    # Scroll the container element to the bottom
    # browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", pane_side)

    # alternate approach

    # Find the container element using an appropriate locator
    # container = browser.find_element_by_css_selector('.your-container-selector')

    # Add a time delay of 2 seconds before scrolling
    sleep(2)

    # Scroll the container element to the bottom with a smooth transition
    browser.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'end' })", pane_side)



except Exception as e:
    print(str(e))