### import packages ###
import time
from selenium import webdriver
from datetime import date
from PIL import Image

### Create robot ###
browser = webdriver.Firefox()
url = "https://worldle.teuteuf.fr/"
browser.get(url)
time.sleep(5)

### get screenshot ###
current_day = date.today()
print(current_day)
browser.save_screenshot('C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\countryshape\\screenshots\\wordle-'+str(current_day)+'.png')
browser.close()

### crop image ###
img = Image.open('C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\countryshape\\screenshots\\wordle-'+str(current_day)+'.png')
left = 970
top = 170
right = 2225
bottom = 720

cropped_image = img.crop((left, top, right, bottom))
cropped_image.save('C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\countryshape\\screenshots\\cropped-wordle-'+str(current_day)+'.png')
