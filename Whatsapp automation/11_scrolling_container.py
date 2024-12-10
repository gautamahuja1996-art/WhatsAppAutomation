'''
We can execute the JavaScript code (to talk with browser) inside selenium python using the
browser.execute_script("Javascript code", "arguments") method

element with id 'pane-side' is chat container and scrollable.

waiting till container with CSS property 'aria-label="Chat list"' is located
This element has an attribute aria-rowcount=507, which is the total chats in my active chats window.
chat_container = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Chat list"]')))

getting a specific attribute
total_chats = chat_container.get_attribute('aria-rowcount')
print(total_chats) # this came out to be 507

scrolling to complete height:
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", chat_container)
arguments[0] --> Chat container

\d+ --> Finds the sequence of one number (1, 2) of more numbers (12, 2345, 564321) in the string
and returns a list of them
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

# running in headless mode
# chrome_options.add_argument('--headless')
# chrome_options.add_argument("--disable-permissions-api")  # Disable Permissions Policy header


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

    # let's get the height of the single chat container
    single_chat_element = chat_list.find_element(By.CSS_SELECTOR, 'div[data-testid="list-item-0"]')

    # let's get the style (height is listed under it) attribute of this element
    style = single_chat_element.get_attribute('style')

    # we have to parse height from it--> let's split the style string as ;
    style_properties = style.split(';')

    # let's look through each element of the list
    # let's take chat_height as none initially
    chat_height = None
    for property in style_properties:
        if "height" in property:
            
            # let's split this string at :
            # height : 72px
            height_property = property.split(':')
            
            # first element --> height, second element --> ' 72px'
            chat_height = height_property[1]

            # there is a leading space in the second element --> ' 72px'
            chat_height = chat_height.strip()

            # let's use regular expressions to get the number from our string
            num_list = re.findall(r'\d+', chat_height)
            
            # getting the first element from the list and converting it to an int
            chat_height = int(num_list[0])
            print(f'Height of Single Chat Element: {chat_height}')

    # scrolling by 17*72 = 1224 pixels
    # browser.execute_script("arguments[0].scrollTop = 1224", chat_container)

    # getting the count of single chat containers in chat list
    # getting all the visual (first 17 for me) titles of the chats
    chat_elements = chat_container.find_elements(By.CSS_SELECTOR, 'div[data-testid="cell-frame-title"]')
    total_chats_in_frame = len(chat_elements)
    print(f'Total Single Chats in a frame: {total_chats_in_frame}')

    # scrolling pixels
    scroll_shift_pixels = chat_height*(total_chats_in_frame)

    # chat name list
    chat_titles = []
    scrolling_distance = 0

    # getting the total height of chat_container
    container_height = browser.execute_script("return arguments[0].scrollHeight", chat_container)
    # scroll_top_val = browser.execute_script("return arguments[0].scrollTop", chat_container)
    print(f'Total Height of the container/Total Scrollable distance: {container_height}', end='\n\n')

    ### Test code
    scroll_top = 0
    chat_titles = []
    while scroll_top <= container_height:

        try:
        
            # noting the chat names
            for chat in chat_elements:
                chat_name = chat.text
                if chat_name not in chat_titles:
                    chat_titles.append(chat_name)

            # let's scroll the window by height pixels
            browser.execute_script(f'arguments[0].scrollTop += {chat_height}', chat_container)

            # increment the scroll top
            scroll_top += chat_height

        except Exception as e:
            print(str(e))


    print(len(chat_titles))

    ### Test code ends here


    ###new code
    # chat_test = []
    # for i in range(2):
    #     for chat in chat_elements:
    #         chat_test.append(chat.text)
    #     time.sleep(5)
    #     browser.execute_script("arguments[0].scrollTop += 1224", chat_container)

    # print(chat_test, len(chat_test), len(list(set(chat_test))))
    ### ends here

    # scrolling loop
    # while scrolling_distance <= container_height:

        # adding visible chat names to the chat titles list
        # for chat in chat_elements:
        #     chat_name = chat.text
        #     chat_titles.append(chat_name)

        # adding some wait --> Add if needed
        # time.sleep(2)

        # change the scrolling distance
        # scrolling_distance = scrolling_distance + scroll_shift_pixels

        # scrolling by scroll_pixels distance
        # browser.execute_script(f"arguments[0].scrollTop = {scrolling_distance}", chat_container)

        # Adding some wait --> Add if needed
        # time.sleep(2)


    # let's look at the chat-titles
    # print(f'Before Removing duplicates: {len(chat_titles)}')
    # print(f'After removing duplicates: {len(list(set(chat_titles)))}')

    # # # Creating a data frame from the list
    # # if chat_titles:

    # #     # giving the col name as Chat Titles
    # #     chat_df = pd.DataFrame({'Chat Titles': chat_titles})

    # #     # file name
    # #     filename = 'groups.csv'

    # #     # donwloading the file with no index numbers
    # #     chat_df.to_csv(filename, index=False)

except Exception as e:
    print(str(e))