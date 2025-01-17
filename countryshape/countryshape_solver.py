### import packages ###
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date
from pathlib import Path
from PIL import Image, ImageOps
import predict

### Set constants ###
# Crop pixels
LEFT = 1325 #1322
RIGHT = 1875 #1873
TOP = 170
BOTTOM = 720

### Functions
# def type_in_word(word):
#     for i in word:
#             interactable.send_keys(i)
#             time.sleep(0.2)
#     time.sleep(1)
#     play_button.click()
#     time.sleep(3)
#     return 0

# Directory
image_path = Path(r'C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\countryshape\\screenshots\\')

### Create robot ###
browser = webdriver.Firefox()
url = "https://worldle.teuteuf.fr/"
browser.get(url)
time.sleep(5)

# ### get screenshot ###
# current_day = date.today()
# file_name = f'worldle-{str(current_day)}.png'
# browser.save_screenshot(image_path / file_name)

# ### crop image ###
# img = Image.open(image_path / file_name)
# img.save(image_path / file_name)
# cropped_image = img.crop((LEFT, TOP, RIGHT, BOTTOM))

# ### Convert to black and white image ###
# cropped_image_clean = cropped_image.convert("L")

# ### Invert to match trained model ###
# inverted_cropped_image_clean = ImageOps.invert(cropped_image_clean)
# inverted_cropped_image_clean.save(image_path / file_name)
# print(image_path / file_name)

### Make prediction
# prediction = predict.predict64(image_path / file_name)

### Type in prediction
# play_button = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[2]/form/div/button')
# interactable = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[2]/form/div/div/input')
# type_in_word(prediction)
print("starting 15 sec timer")
time.sleep(15)

### See if answer is correct or not

### If incorrect, gather feedback
# Distance
distance = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]')
print(distance.get_attribute('innerHTML'))

# # Direction
direction = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div[3]/span/img')
print(direction.get_attribute('src'))
# north = 'https://cdnjs.cloudflare.com/ajax/libs/twemoji/12.0.4/2/72x72/2b06.png'
# ne = 'https://cdnjs.cloudflare.com/ajax/libs/twemoji/12.0.4/2/72x72/2197.png'
# east = 'https://cdnjs.cloudflare.com/ajax/libs/twemoji/12.0.4/2/72x72/27a1.png'
# se = 'https://cdnjs.cloudflare.com/ajax/libs/twemoji/12.0.4/2/72x72/2198.png'
# south = 'https://cdnjs.cloudflare.com/ajax/libs/twemoji/12.0.4/2/72x72/2b07.png'
# sw = 'https://cdnjs.cloudflare.com/ajax/libs/twemoji/12.0.4/2/72x72/2199.png'
# west = 'https://cdnjs.cloudflare.com/ajax/libs/twemoji/12.0.4/2/72x72/2b05.png'
# nw = 'https://cdnjs.cloudflare.com/ajax/libs/twemoji/12.0.4/2/72x72/2196.png'
