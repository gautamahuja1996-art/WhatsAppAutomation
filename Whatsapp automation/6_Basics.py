# Comments --> 

# As soon as you create the browser instance and run the code, your browser should open up and close
# instantly. To keep it open, you have to add further commands for browser

# There is a possibility that your browser might not open due to some unknown error or exceptions. It's
# good practice to open it using the try-except-finally statement.

# locals() method returns the directory of variables created in local namespace.

# To maximize window, driver.maximize_window()

# [IMPORTANT: TO BE DEALT LATER] If different profiles are already opened and you are trying to open 
# a specific profile, an error might occur. Also, this error does not occur if you just trying to open 
# chrome (no options parameter) and not a specific profile, with other profiles opened -->
# [ERROR] --> Opening in existing browser session.
# Message: unknown error: Chrome failed to start: exited normally.
#   (unknown error: DevToolsActivePort file doesn't exist)
#   (The process started from chrome location C:\Program Files\Google\Chrome\Application\chrome.exe is no longer running, so ChromeDriver is assuming that Chrome has crashed.)
# Stacktrace:
# Backtrace:
#         GetHandleVerifier [0x00D38893+48451]
#         (No symbol) [0x00CCB8A1]
#         (No symbol) [0x00BD5058]
#         (No symbol) [0x00BF3211]
#         (No symbol) [0x00BF0019]
#         (No symbol) [0x00C20798]
#         (No symbol) [0x00C2047C]
#         (No symbol) [0x00C1A0B6]
#         (No symbol) [0x00BF7E08]
#         (No symbol) [0x00BF8F2D]
#         GetHandleVerifier [0x00F98E3A+2540266]
#         GetHandleVerifier [0x00FD8959+2801161]
#         GetHandleVerifier [0x00FD295C+2776588]
#         GetHandleVerifier [0x00DC2280+612144]
#         (No symbol) [0x00CD4F6C]
#         (No symbol) [0x00CD11D8]
#         (No symbol) [0x00CD12BB]
#         (No symbol) [0x00CC4857]
#         BaseThreadInitThunk [0x75C97D59+25]
#         RtlInitializeExceptionChain [0x7706B74B+107]
#         RtlClearBits [0x7706B6CF+191]

# In oder to wait in your browser till a specific condition is met, you can go through the following steps-->

# a) Create an instance of WebDriverWait class, as 'wait = WebDriverWait(driver, 10)' --> This will create
# a timer of 10 seconds.

# b) Next, use one of the methods of the WebDriverWait class as 'until', 'until_no' etc, such as, 
# 'element = wait.until(expected_conditions.presence_of_element_located(('By.TAG_NAME', 'body')))' 
# to check if a specific condition is met or not in that timespan or not.

# c) Note that, if the condition is met, the unti() method returns the 'element' (whose tag name is body),
# else, it returns a 'timeout-exception'.

# Error is element is not located within the given time -->
# Message: 
# Stacktrace:
# Backtrace:
#         GetHandleVerifier [0x00568893+48451]
#         (No symbol) [0x004FB8A1]
#         (No symbol) [0x00405058]
#         (No symbol) [0x00430467]
#         (No symbol) [0x0043069B]
#         (No symbol) [0x0045DD92]
#         (No symbol) [0x0044A304]
#         (No symbol) [0x0045C482]
#         (No symbol) [0x0044A0B6]
#         (No symbol) [0x00427E08]
#         (No symbol) [0x00428F2D]
#         GetHandleVerifier [0x007C8E3A+2540266]
#         GetHandleVerifier [0x00808959+2801161]
#         GetHandleVerifier [0x0080295C+2776588]
#         GetHandleVerifier [0x005F2280+612144]
#         (No symbol) [0x00504F6C]
#         (No symbol) [0x005011D8]
#         (No symbol) [0x005012BB]
#         (No symbol) [0x004F4857]
#         BaseThreadInitThunk [0x75C97D59+25]
#         RtlInitializeExceptionChain [0x7706B74B+107]
#         RtlClearBits [0x7706B6CF+191]

# Getting all the headings in the page
# <h3 class="LC20lb MBeuO DKV0Md">What is Python? Executive Summary</h3>
# Also we can find elements within other elements as -->
# element = browser.find_element(By.ID, 'rso')
# headings = element.find_elements(By.TAG_NAME, 'h3')
# for heading in headings:
#     print(heading.text)

# making imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  # To create timeout instance
from selenium.webdriver.support import expected_conditions as ec  # To create conditions

# path to chrome driver, directory where chrome stores all profiles
driver_path = r'C:\Program Files (x86)\chromedriver.exe'
directory_path = r'C:\Users\sunst\AppData\Local\Google\Chrome\User Data'

# specific profile we want to open
profile = "Default"

# url to open
website = 'https://www.google.com'

# creating service and options instance
service = Service(driver_path)
options = Options()

# Adding arguments
options.add_argument(f'--user-data-dir={directory_path}')
options.add_argument(f'--profile-directory={profile}')

# Opening the browser
try:
    browser = webdriver.Chrome(service=service, options=options)     # Add the options parameter later

    # checking is page is loaded successfully or not [Locating body tag in HTML DOM]
    # The until method will look for body tag in the DOM. If found within 10 seconds, it will
    # return the element, else it will return a timeout exception
    wait = WebDriverWait(browser, 10)
    result = wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))

    # print(result)

    # Let's load google.com
    browser.get("https://www.google.com")

    # wait to check if it's loaded or not [Looking for body tag again]
    res = wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))
    # print(res)

    # finding search bar
    search_bar = browser.find_element(By.ID, 'APjFqb')

    # enterting text in it
    search_bar.send_keys('What is python?')

    # hitting enter
    search_bar.send_keys(Keys.RETURN)

    # waiting until body tag is loaded
    r = wait.until(ec.presence_of_element_located((By.TAG_NAME, 'body')))
    # print(r)

    # let's get all the titles of search results
    headings = browser.find_elements(By.TAG_NAME, 'h3')

    # headings is a list
    for heading in headings:
        print(heading.text)


except Exception as e:
    print(str(e))
finally:
    # 'broswer' will exist in directory of local variables, if it's created in 'try' part with no exception.
    if 'broswer' in locals():
        browser.quit()
