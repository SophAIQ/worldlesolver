import time
from selenium import webdriver
from datetime import date

browser = webdriver.Firefox()
url = "https://worldle.teuteuf.fr/"
browser.get(url)
time.sleep(5)

# get screenshot
current_day = date.today()
print(current_day)
browser.save_screenshot('C:\\Users\\johnd\\Documents\\School\\Graduate School\\Computer Science\\VSCode\\countryshape\\screenshots\\wordle-'+str(current_day)+'.png')
browser.close()
