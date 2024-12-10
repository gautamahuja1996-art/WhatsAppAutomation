'''
To pack/grid a widget when needed, use .pack() or .grid() to pack, else use .grid_forget() or .pack_forget()
to temporarily remove a widget.
'''

# importing modules
import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageTk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# some global variables
file_path = ''
image_tk = None
image = None
link = ''
blurb = ''
final_text = ''

# list of all groups
groups = ['DATA']

# Callback functions
# upload image function
def upload_image():

    global file_path, image, image_tk

    # open dialog box
    file_path = filedialog.askopenfilename(filetypes=(('Png Files', '*.png'), 
                                                      ('Jpeg files', '*.jpg *.jpeg')))

    # Checking if it's a valid file path
    if os.path.exists(file_path):

        # let's open the image
        image = Image.open(file_path)
        # print(image.size)

        # resizing image
        resized_image = image.resize((400, 225)) # 16:9 aspect ratio maintained

        # converting to tk image
        image_tk = ImageTk.PhotoImage(resized_image)

        # if valid image
        if resized_image:

            # putting it on the label
            image_viewer.config(text='', image=image_tk)

# add link + blurb function
def add_both():

    global link, blurb, final_text
    
    # getting the text
    link = entry.get()
    blurb = textarea.get('1.0', tk.END)

    final_text = blurb + '\n' + link

    # Update the label
    text_view.config(text=final_text)

    # clear the widget and variables
    entry.delete(0, tk.END)
    textarea.delete(1.0, tk.END)

# send comms function
def send_comms():

    global final_text

    # are you sure message box
    user_input = messagebox.askokcancel(title='Send Comms', message='Are you sure you want to send the comms?')

    # if user pressed yes
    if user_input:

        # let's try to create a browser instance
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

                    # getting the attach button
                    # element --> <div aria-disabled="false" role="button" tabindex="0" class="_3ndVb" data-tab="10" title="Attach" aria-label="Attach"><span data-testid="clip" data-icon="clip" class=""><svg viewBox="0 0 24 24" height="24" width="24" preserveAspectRatio="xMidYMid meet" class="" version="1.1" x="0px" y="0px" enable-background="new 0 0 24 24" xml:space="preserve"><path fill="currentColor" d="M1.816,15.556v0.002c0,1.502,0.584,2.912,1.646,3.972s2.472,1.647,3.974,1.647 c1.501,0,2.91-0.584,3.972-1.645l9.547-9.548c0.769-0.768,1.147-1.767,1.058-2.817c-0.079-0.968-0.548-1.927-1.319-2.698 c-1.594-1.592-4.068-1.711-5.517-0.262l-7.916,7.915c-0.881,0.881-0.792,2.25,0.214,3.261c0.959,0.958,2.423,1.053,3.263,0.215 c0,0,3.817-3.818,5.511-5.512c0.28-0.28,0.267-0.722,0.053-0.936c-0.08-0.08-0.164-0.164-0.244-0.244 c-0.191-0.191-0.567-0.349-0.957,0.04c-1.699,1.699-5.506,5.506-5.506,5.506c-0.18,0.18-0.635,0.127-0.976-0.214 c-0.098-0.097-0.576-0.613-0.213-0.973l7.915-7.917c0.818-0.817,2.267-0.699,3.23,0.262c0.5,0.501,0.802,1.1,0.849,1.685 c0.051,0.573-0.156,1.111-0.589,1.543l-9.547,9.549c-0.756,0.757-1.761,1.171-2.829,1.171c-1.07,0-2.074-0.417-2.83-1.173 c-0.755-0.755-1.172-1.759-1.172-2.828l0,0c0-1.071,0.415-2.076,1.172-2.83c0,0,5.322-5.324,7.209-7.211 c0.157-0.157,0.264-0.579,0.028-0.814c-0.137-0.137-0.21-0.21-0.342-0.342c-0.2-0.2-0.553-0.263-0.834,0.018 c-1.895,1.895-7.205,7.207-7.205,7.207C2.4,12.645,1.816,14.056,1.816,15.556z"></path></svg></span></div>
                    attach = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'div[title="Attach"]')))

                    # clicking it
                    attach.click()

                    # Once you click on the attach button, the photos and videos button will open up
                    # we will have the html for that button
                    # the button has an input tag where we can specify the file name to search
                    # element --> <input accept="image/*,video/mp4,video/3gpp,video/quicktime" type="file" multiple="" style="display: none;">
                    image_input = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'input[accept="image/*,video/mp4,video/3gpp,video/quicktime"]')))

                    # let's enter the file path in it
                    image_input.send_keys(file_path)

                    # let's add the text message
                    # locating the textbox using it's attributes (CSS selector)
                    message_box = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'div[data-testid="media-caption-input-container"]')))

                    # let's enter text into it
                    message_box.send_keys(final_text)
                    print(f'final blurb: {final_text}')
                    time.sleep(2)

                    # click the send button
                    send_button = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR ,'span[data-icon="send"]')))
                    send_button.click()

                    time.sleep(5)

        except Exception as e:
            print(str(e))
        finally:
            if 'browser' in locals():
                browser.quit()
            


# Creating instances and variables
driver_path = r"C:\Program Files (x86)\chromedriver.exe"
directory_path = r'C:\Users\sunst\AppData\Local\Google\Chrome\User Data'
profile = 'Default'
service = Service(driver_path)
options = Options()
options.add_argument(f'--user-data-dir={directory_path}')
options.add_argument(f'--profile-directory={profile}')

# root gui --> main gui
root = tk.Tk()

# properties of root gui
root.title('Communication Scheduler')
root.geometry('800x600')
root.resizable(width=False, height=False)
# root.iconbitmap('scheduler.ico')

# Adding widgets
# Label --> To display 'Whatsapp scheduler'
label = tk.Label(root, text='WhatsApp Scheduler')
label.pack()

# Frame + image picker button + display label
image_frame = tk.Frame(root)
image_frame.pack()
image_picker = tk.Button(image_frame, text='Upload Image', command=upload_image)
image_viewer = tk.Label(image_frame, text='No Image')
image_picker.grid(row=0, column=0)
image_viewer.grid(row=0, column=1)

# Frame + entry widget + text area + button + label to display
data_frame = tk.Frame(root)
data_frame.pack()
entry = tk.Entry(data_frame, width=100)
entry.grid(row=0, column=0)
textarea = tk.Text(data_frame, width=75, height=5)
textarea.grid(row=1, column=0)
add_blurb_btn = tk.Button(data_frame, text='Add Both', command=add_both)
add_blurb_btn.grid(row=2, column=0)
text_view = tk.Label(data_frame, text='No Link and blurb')
text_view.grid(row=3, column=0)

# send button
s_btn = tk.Button(root, text='Send comms', command=send_comms)
s_btn.pack()

# mainloop
root.mainloop()