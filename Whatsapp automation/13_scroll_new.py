from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import re
import time
import pandas as pd

chrome_directory = r'C:\Users\sunst\AppData\Local\Google\Chrome\User Data'
chrome_profile = 'Default'

chrome_options = Options()
chrome_options.add_experimental_option('detach', True) # keeping the chrome open even after the script ends
chrome_options.add_argument(f'--user-data-dir={chrome_directory}')
chrome_options.add_argument(f'--profile-directory={chrome_profile}')

try:
    browser = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(browser, 60)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))
    browser.get('https://web.whatsapp.com')
    browser.maximize_window()
    chat_container = wait.until(ec.presence_of_element_located((By.ID, 'pane-side')))
    chat_list = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Chat list"]')))
    total_active_chats = chat_list.get_attribute('aria-rowcount')
    print(f'Total Active Chats --> {total_active_chats}')
    single_chat_element = chat_list.find_element(By.CSS_SELECTOR, 'div[data-testid="list-item-0"]')
    style = single_chat_element.get_attribute('style')
    style_properties = style.split(';')

    chat_height = None
    for property in style_properties:
        if "height" in property:
            height_property = property.split(':')
            chat_height = height_property[1]
            chat_height = chat_height.strip()
            num_list = re.findall(r'\d+', chat_height)
            chat_height = int(num_list[0])
            print(f'Height of Single Chat Element: {chat_height}')

    chat_elements = chat_container.find_elements(By.CSS_SELECTOR, 'div[data-testid="cell-frame-title"]')
    total_chats_in_frame = len(chat_elements)
    print(f'Total Single Chats in a frame: {total_chats_in_frame}')
    scroll_shift_pixels = chat_height*(total_chats_in_frame)
    chat_titles = []
    scrolling_distance = 0
    container_height = browser.execute_script("return arguments[0].scrollHeight", chat_container)
    print(f'Total Height of the container/Total Scrollable distance: {container_height}', end='\n\n')

    chat_titles = []
    scrolltop = 0
    while True:
        for index, chat in enumerate(chat_elements):
            try:
                chat_name = chat.text
                if chat_name not in chat_titles:
                    chat_titles.append(chat_name)
                    print(len(chat_titles))
            except StaleElementReferenceException:
                # Handle stale element exception, e.g., print an error message
                print(f"Stale element encountered at index {index}")

        browser.execute_script(f'arguments[0].scrollTop += {chat_height}', chat_container)
        scrolltop += chat_height
        print(scrolltop, container_height)

        if scrolltop >= container_height:
            print('Broken: ', scrolltop, container_height)
            break


    print(chat_titles, len(chat_titles), len(list(set(chat_titles))))

except Exception as e:
    print(str(e))