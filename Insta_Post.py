from instabot import Bot

# create a new bot instance
bot = Bot()
import time

time.sleep(10)

# login to your Instagram account
bot.login(username='', password='')

# define the path to your image file and caption
image_path = 'path/to/your/image'
caption = 'This post has been uploaded by an automated script designed by Aditya Late, known as the ChatBot. ' \
          'In the near future, he will be sharing a video detailing the intricacies of how this post was '\
          'uploaded using this cutting-edge software.' \
          'Thank you for your continued support of our technological advancements.'

# post the image with the caption
bot.upload_photo(image_path, caption=caption)

# logout from your Instagram account
bot.logout()
