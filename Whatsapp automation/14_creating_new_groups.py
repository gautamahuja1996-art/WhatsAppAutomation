# importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

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
    menu = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="menu"]')))

    # locating chat list
    chat_list = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Chat list"]')))

    # Creating 30 test grps
    for i in range(1, 31):
        menu.click()
        options_list = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="chatlist-header-dropdown"]')))
        new_grp = options_list.find_element(By.CSS_SELECTOR, 'li[data-testid="mi-new-group menu-item"]')
        new_grp.click()
        input_area = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="inputarea"]')))
        input_area.send_keys('Gouri')
        input_area.send_keys(Keys.ENTER)
        arrow_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="arrow-forward"]')))
        arrow_button.click()
        grp_name = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="text-input"]')))
        grp_name.send_keys(f'Test Group {i}')
        create_grp_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="create-group-btn"]')))
        create_grp_button.click()
        active_chats = chat_list.get_attribute('aria-rowcount')
        print(f'Current Active Chats:{active_chats}')

        # Instead of using sleep for 2 seconds we can write a proper algorthm where we check if the
        # group we created exists in the active chat list or not (just check if newly created grp is
        # in the first 17 elements or not)
        time.sleep(2)

except Exception as e:
    print(str(e))