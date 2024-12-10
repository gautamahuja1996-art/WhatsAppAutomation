from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Initialize the webdriver
driver = webdriver.Chrome()

# Open WhatsApp web
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code and manually log in

# Find the contact or group to send the message
contact = driver.find_element_by_xpath("//span[@title='Your Contact Name']")
contact.click()

# Locate the attachment button
attachment_button = driver.find_element_by_xpath("//div[@title='Attach']")
attachment_button.click()

# Select the image file
image_input = driver.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
image_input.send_keys("path_to_your_image_file.jpg")

# Wait for the image to upload (you may need to add a delay if required)

# [Adding some code here]
# we can check the presence of uploaded image# Wait for the image to upload
wait = WebDriverWait(driver, 10)
uploaded_image = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='message-image']/img")))

# Check if the image element is displayed
if uploaded_image.is_displayed():
    print("Image uploaded successfully!")
else:
    print("Image upload failed!")

# [Code addition ended]

# Find the send button and click it
send_button = driver.find_element_by_xpath("//span[@data-icon='send']")
send_button.click()

# Close the driver
driver.quit()
