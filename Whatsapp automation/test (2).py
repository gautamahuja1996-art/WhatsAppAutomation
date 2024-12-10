import os
from appdirs import user_data_dir

# Get the default Chrome profile directory
chrome_profile_dir = os.path.join(user_data_dir('Google', 'Chrome'))

print(chrome_profile_dir)


# import os

# def find_whatsapp_web_profile():
#     # Get the default Chrome profile directory
#     chrome_profile_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Google', 'Chrome', 'User Data')

#     # Search for the WhatsApp Web profile
#     whatsapp_profile_dir = None
#     for profile in os.listdir(chrome_profile_dir):
#         if 'WhatsApp' in profile:
#             whatsapp_profile_dir = os.path.join(chrome_profile_dir, profile)
#             break

#     return whatsapp_profile_dir

# # Call the function to find the WhatsApp Web profile
# whatsapp_profile = find_whatsapp_web_profile()
# if whatsapp_profile:
#     print("WhatsApp Web profile found:", whatsapp_profile)
# else:
#     print("WhatsApp Web profile not found.")
