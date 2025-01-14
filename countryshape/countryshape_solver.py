### import packages ###
import time
from selenium import webdriver
from datetime import date
from PIL import Image, ImageOps

### Set constants ###
# Crop pixels
LEFT = 1325 #1322
RIGHT = 1875 #1873
TOP = 170
BOTTOM = 720

# Directory
image_path = 'C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\countryshape\\screenshots\\'

### Create robot ###
browser = webdriver.Firefox()
url = "https://worldle.teuteuf.fr/"
browser.get(url)
time.sleep(5)

### get screenshot ###
current_day = date.today()
print(current_day)
browser.save_screenshot(image_path + 'worldle-'+str(current_day)+'.png')
browser.close()

### crop image ###
img = Image.open(image_path + 'worldle-'+str(current_day)+'.png')
img.save(image_path + 'raw_wordle-' + str(current_day) + '.png')
cropped_image = img.crop((LEFT, TOP, RIGHT, BOTTOM))


### Convert to black and white image ###
cropped_image_clean = cropped_image.convert("L")

### Invert to match trained model ###
inverted_cropped_image_clean = ImageOps.invert(cropped_image_clean)
inverted_cropped_image_clean.save(image_path + 'worldle-'+str(current_day)+'.png')