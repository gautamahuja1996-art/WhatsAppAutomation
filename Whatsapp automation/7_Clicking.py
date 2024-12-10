# If your link name has spaces, then use partial link name to locate the elements

# To go back, you can use, browser.back()

#  To go forward, you can use, browser.forward()

# To clear the text in search bar, you cna use, search_bar.clear()

# importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# path to chrome driver
chrome_driver = r'C:\Program Files (x86)\chromedriver.exe'

# creating service instance
service = Service(chrome_driver)

# creating broswer instance
try:
    browser = webdriver.Chrome(service=service)

    # creating wait instance
    wait = WebDriverWait(browser, 10)
    res = wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    # let's open google.com
    browser.get('https://www.google.com')

    # wait for it to load
    res = wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    # let's find search bar using NAME tag as ID might be dynamically generated
    search_bar = browser.find_element(By.NAME, 'q')

    # let's enter some text
    search_bar.send_keys('What is python?')

    # let's hit enter
    search_bar.send_keys(Keys.RETURN)

    # let's wait for the page to load properly [Let's wait till search bar appears]
    # there is a possibility that body tag appears and elements are still loading
    res = wait.until(ec.presence_of_element_located((By.NAME, 'q')))

    # let's get the element with a link
    link = browser.find_element(By.PARTIAL_LINK_TEXT, "What is Python? Executive Summary")

    # click on this link
    link.click()

    # wait for page to load
    res = wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    # click on the downloads button
    # element has link text as 'Downloads' or id as 'downloads'
    download_button = browser.find_element(By.PARTIAL_LINK_TEXT, "Downloads")
    download_button.click()

    # wait for page to load
    res = wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    # let's get back to google home page using .back method
    browser.back()
    browser.back()
    browser.back()

    # Wait for 5 sec
    time.sleep(5)

except Exception as e:
    print(str(e))
finally:
    if 'browser' in locals():
        browser.quit()