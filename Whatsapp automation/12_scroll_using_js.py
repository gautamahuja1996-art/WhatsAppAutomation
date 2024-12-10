'''
# Scroll the chat container until the bottom
    browser.execute_script("""
        var chatContainer = arguments[0];
        var scrollToBottom = function() {
            chatContainer.scrollTop += 10;
            if (chatContainer.scrollTop < chatContainer.scrollHeight) {
                window.requestAnimationFrame(scrollToBottom);
            }
        };
        scrollToBottom();
    """, chat_container)
'''


# importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import re
import time
import pandas as pd

# directory and profile used
chrome_directory = r'C:\Users\sunst\AppData\Local\Google\Chrome\User Data'
chrome_profile = 'Default'

# creating instances
chrome_options = Options()
chrome_options.add_experimental_option('detach', True) # keeping the chrome open even after the script ends
chrome_options.add_argument(f'--user-data-dir={chrome_directory}')
chrome_options.add_argument(f'--profile-directory={chrome_profile}')

# let's try to create the browser instance
try:

    # creating the browser instance
    browser = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    # creating a wait instance --> Timeout : 60
    wait = WebDriverWait(browser, 60)

    # let's wait for body tag to load
    wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    # opening whatsapp web
    browser.get('https://web.whatsapp.com')

    # maximizing
    browser.maximize_window()

    # getting chat-container
    chat_container = wait.until(ec.presence_of_element_located((By.ID, 'pane-side')))

    # finding chat list elements (which has all the chats, but is not a scrollable container)
    chat_list = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Chat list"]')))

    # This chat list element has an attribute 'aria-rowcount' which holds the total number of active chats.
    total_active_chats = chat_list.get_attribute('aria-rowcount')
    print(f'Total Active Chats --> {total_active_chats}') # This came out to be 507 for me

    # scrolling height / total scroll in chat container
    scroll_height = browser.execute_script('return arguments[0].scrollHeight', chat_container)
    scroll_top = browser.execute_script('return arguments[0].scrollTop', chat_container)
    print(scroll_top, scroll_height)

    # scrolling loop
    chat_titles = []
    while scroll_top <= scroll_height:

        # getting chat elements under the chat list --> 17 for my case [These will change when scrolled]
        chat_elements = chat_container.find_elements(By.CSS_SELECTOR, 'div[data-testid="cell-frame-title"]')
        for chat in chat_elements:
            chat_name = chat.text
            chat_titles.append(chat_name)

        # scroll by 10 pixels
        browser.execute_script('arguments[0].scrollTop += 1000', chat_container)

        # updating the scroll top
        scroll_top = scroll_top + 1000
        print(scroll_top)

        # to avoid stale error
        # chat_container = wait.until(ec.presence_of_element_located((By.ID, 'pane-side')))

    # printing chat_titles
    print(len(chat_titles), len(list(set(chat_titles))))

except Exception as e:
    print(str(e))