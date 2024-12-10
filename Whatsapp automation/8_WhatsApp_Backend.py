# lhggkp7q ln8gz9je rx9719la --> Multi class names. We can access these elements using the code,
# chat_elements = pane_side.find_elements(By.CSS_SELECTOR, '.lhggkp7q.ln8gz9je.rx9719la')

# Target html elements with class '_21S-L' (single class name can be targeted using the By.CLASS_NAME)-->
'''
<div class="_21S-L" data-testid="cell-frame-title"><span dir="auto" title="Projects" aria-label="" 
class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr">Projects</span></div>
'''

# Note that: When an element is visible on a website, then only you can find it's html code

# create a different profile for WhatsApp web all together


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

# list of all groups
groups = ['DATA']

# creating service and options instance
service = Service(driver_path)
options = Options()

# Adding arguments to the options instance
options.add_argument(f'--user-data-dir={chrome_directory}')
options.add_argument(f'--profile-directory={profile}')

# Creating the browser instance
try:
    browser = webdriver.Chrome(service=service, options=options)

    # wait for body tag to load [Let's create time instance with 1 min of wait]
    wait = WebDriverWait(browser, 60)
    body_element = wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    # getting to the whatsapp web
    browser.get('https://web.whatsapp.com')

    # wait for div tag with id = pane-side to appear
    pane_side = wait.until(ec.presence_of_element_located((By.ID, 'pane-side')))

    # Finding all elements with class name : _21S-L
    chat_elements = pane_side.find_elements(By.CLASS_NAME, '_21S-L')

    # iterating over the list
    for chat in chat_elements:

        # if the text of chat element matches any names in the groups list, click on it and send the message.
        if chat.text in groups:

            # click on that element
            chat.click()

            # Getting the textbox for entering message
            # locating the textbox using it's attributes (CSS selector)
            message_box = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'div[title="Type a message"]')))

            # let's enter text into it
            message_box.send_keys('Hello')

            # let's get the send button
            # html tag --> <span data-testid="send" data-icon="send" class=""><svg viewBox="0 0 24 24" height="24" width="24" preserveAspectRatio="xMidYMid meet" class="" version="1.1" x="0px" y="0px" enable-background="new 0 0 24 24" xml:space="preserve"><path fill="currentColor" d="M1.101,21.757L23.8,12.028L1.101,2.3l0.011,7.912l13.623,1.816L1.112,13.845 L1.101,21.757z"></path></svg></span>
            send_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'span[data-icon="send"]')))

            # lets click it
            send_button.click()

            # getting the attach button
            # element --> <div aria-disabled="false" role="button" tabindex="0" class="_3ndVb" data-tab="10" title="Attach" aria-label="Attach"><span data-testid="clip" data-icon="clip" class=""><svg viewBox="0 0 24 24" height="24" width="24" preserveAspectRatio="xMidYMid meet" class="" version="1.1" x="0px" y="0px" enable-background="new 0 0 24 24" xml:space="preserve"><path fill="currentColor" d="M1.816,15.556v0.002c0,1.502,0.584,2.912,1.646,3.972s2.472,1.647,3.974,1.647 c1.501,0,2.91-0.584,3.972-1.645l9.547-9.548c0.769-0.768,1.147-1.767,1.058-2.817c-0.079-0.968-0.548-1.927-1.319-2.698 c-1.594-1.592-4.068-1.711-5.517-0.262l-7.916,7.915c-0.881,0.881-0.792,2.25,0.214,3.261c0.959,0.958,2.423,1.053,3.263,0.215 c0,0,3.817-3.818,5.511-5.512c0.28-0.28,0.267-0.722,0.053-0.936c-0.08-0.08-0.164-0.164-0.244-0.244 c-0.191-0.191-0.567-0.349-0.957,0.04c-1.699,1.699-5.506,5.506-5.506,5.506c-0.18,0.18-0.635,0.127-0.976-0.214 c-0.098-0.097-0.576-0.613-0.213-0.973l7.915-7.917c0.818-0.817,2.267-0.699,3.23,0.262c0.5,0.501,0.802,1.1,0.849,1.685 c0.051,0.573-0.156,1.111-0.589,1.543l-9.547,9.549c-0.756,0.757-1.761,1.171-2.829,1.171c-1.07,0-2.074-0.417-2.83-1.173 c-0.755-0.755-1.172-1.759-1.172-2.828l0,0c0-1.071,0.415-2.076,1.172-2.83c0,0,5.322-5.324,7.209-7.211 c0.157-0.157,0.264-0.579,0.028-0.814c-0.137-0.137-0.21-0.21-0.342-0.342c-0.2-0.2-0.553-0.263-0.834,0.018 c-1.895,1.895-7.205,7.207-7.205,7.207C2.4,12.645,1.816,14.056,1.816,15.556z"></path></svg></span></div>
            attach = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'div[title="Attach"]')))

            # clicking it
            attach.click()

            # finding the photos and videos button
            # element --> <span data-testid="attach-image" data-icon="attach-image" class="_3fV_S"><svg viewBox="0 0 53 53" height="53" width="53" preserveAspectRatio="xMidYMid meet" class="" version="1.1" x="0px" y="0px" enable-background="new 0 0 53 53" xml:space="preserve"><g><defs><circle id="image-SVGID_1_" cx="26.5" cy="26.5" r="25.5"></circle></defs><clipPath id="image-SVGID_2_"><use xlink:href="#image-SVGID_1_" overflow="visible"></use></clipPath><g clip-path="url(#image-SVGID_2_)"><path fill="#AC44CF" d="M26.5-1.1C11.9-1.1-1.1,5.6-1.1,27.6h55.2C54,8.6,41.1-1.1,26.5-1.1z"></path><path fill="#BF59CF" d="M53,26.5H-1.1c0,14.6,13,27.6,27.6,27.6s27.6-13,27.6-27.6C54.1,26.5,53,26.5,53,26.5z"></path><rect x="17" y="24.5" fill="#AC44CF" width="18" height="9"></rect></g></g><g fill="#F5F5F5"><path id="svg-image" d="M18.318 18.25 34.682 18.25C35.545 18.25 36.409 19.077 36.493 19.946L36.5 20.083 36.5 32.917C36.5 33.788 35.68 34.658 34.818 34.743L34.682 34.75 18.318 34.75C17.368 34.75 16.582 34.005 16.506 33.066L16.5 32.917 16.5 20.083C16.5 19.213 17.32 18.342 18.182 18.257L18.318 18.25 34.682 18.25ZM23.399 26.47 19.618 31.514C19.349 31.869 19.566 32.25 20.008 32.25L32.963 32.25C33.405 32.239 33.664 31.848 33.384 31.492L30.702 28.043C30.486 27.774 30.077 27.763 29.861 28.032L27.599 30.759 24.26 26.459C24.045 26.179 23.614 26.179 23.399 26.47ZM31.75 21.25C30.784 21.25 30 22.034 30 23 30 23.966 30.784 24.75 31.75 24.75 32.716 24.75 33.5 23.966 33.5 23 33.5 22.034 32.716 21.25 31.75 21.25Z"></path></g></svg></span>
            # photo_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'span[data-icon="attach-image"]')))

            # clicking on it
            # photo_button.click()

            # Once you click on the attach button, the photos and videos button will open up
            # we will have the html for that button
            # the button has an input tag where we can specify the file name to search
            # element --> <input accept="image/*,video/mp4,video/3gpp,video/quicktime" type="file" multiple="" style="display: none;">
            image_input = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'input[accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))

            # let's enter the file path in it
            image_path = r"C:\Users\sunst\OneDrive\Personal\Personal\test codes\Whatsapp automation\tech_chunauti.jpg"
            image_input.send_keys(image_path)
            sleep(2)

            # To check if image is uploaded or not, we can do a check on a canvas attribute
            # [After image upload]
            # elements --> <canvas width="642" height="160" style="padding: 0px; margin: 0px; border: 0px; background: transparent; position: absolute; top: 0px; left: 0px; width: 428px; height: 107px; display: block;"></canvas>

            # let's add a blurb
            # locating the textbox using it's attributes (CSS selector)
            message_box = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'div[title="Type a message"][data-testid="media-caption-input-container"]')))

            # let's enter text into it
            message_box.send_keys('Blurb')
            sleep(2)

            # click the send button
            send_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'span[data-icon="send"]')))
            send_button.click()

    sleep(10)
    
    # looking for all div with class name 'lhggkp7q ln8gz9je rx9719la' in side_element

except Exception as e:
    print(str(e))
finally:
    if 'browser' in locals():
        browser.quit()