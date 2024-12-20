
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# phone = "917501138448"
group_id = "H7MsCPjYoGXDFdFHZvZEYA"

message = 'Hi there! This is a test message from a Python script.'

BASE_URL = "https://web.whatsapp.com/"
CHAT_URL ="https://web.whatsapp.com/send?id={group_id}&text={message}&type=id&app_absent=1"


chrome_options = Options()
chrome_options.add_argument("start-maximized")
user_data_dir = ''.join(random.choices(string.ascii_letters, k=8))
chrome_options.add_argument("--user-data-dir=/tmp/chrome-data/" + user_data_dir)
chrome_options.add_argument("--incognito")


browser = webdriver.Chrome(ChromeDriverManager().install(),  options=chrome_options,)

browser.get(BASE_URL)
browser.maximize_window()



# phone = "917501138448"
# message = 'Hi There,  This is a test message from Python Script'



browser.get(CHAT_URL.format(group_id=group_id, message=message))
time.sleep(10)


inp_xpath = (
    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
)
input_box = WebDriverWait(browser, 60).until(
    expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
)
input_box.send_keys(message)
input_box.send_keys(Keys.ENTER)

time.sleep(10)






















