# comments





# importing modules
# trying to open specific profiles
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# path to chrome driver, all chrome profiles, specific profile
driver_path = r'C:\Program Files (x86)\chromedriver.exe'
profile_path = r'C:\Users\sunst\AppData\Local\Google\Chrome\User Data'
chrome_profile = 'Default'

# creating service and options instances
service = Service(driver_path)
options = Options()

# Adding path where chrome stores profiles
options.add_argument(f'--user-data-dir={profile_path}')

# Adding argument for specific profile
options.add_argument(f'--profile-directory={chrome_profile}')

# creating browser instances: If you run till here, browser opens up
browser = webdriver.Chrome(options=options, service=service)

# Chrome logo
# Google LLC
# Copyright 2023 Google LLC. All rights reserved.
# Google Chrome	113.0.5672.127 (Official Build) (64-bit) (cohort: Stable) 
# Revision	c541687b21a73452ab403e2dced7033ddc97ee9d-refs/branch-heads/5672@{#1202}
# OS	Windows 11 Version 22H2 (Build 22621.1702)
# JavaScript	V8 11.3.244.11
# User Agent	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36
# Command Line	"C:\Program Files\Google\Chrome\Application\chrome.exe" --allow-pre-commit-input --disable-background-networking --disable-backgrounding-occluded-windows --disable-client-side-phishing-detection --disable-default-apps --disable-hang-monitor --disable-popup-blocking --disable-prompt-on-repost --disable-sync --enable-automation --enable-blink-features=ShadowDOMV0 --enable-logging --log-level=0 --no-first-run --no-service-autorun --password-store=basic --remote-debugging-port=0 --test-type=webdriver --use-mock-keychain --user-data-dir="C:\Users\sunst\AppData\Local\Google\Chrome\User Data\Profile 10" --flag-switches-begin --flag-switches-end
# Executable Path	C:\Program Files\Google\Chrome\Application\chrome.exe
# Profile Path	C:\Users\sunst\AppData\Local\Google\Chrome\User Data\Profile 10\Default
# Active Variations	5e3a236d-4113a79e
