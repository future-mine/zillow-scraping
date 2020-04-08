from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup
# options = ChromeOptions()
# options.add_argument("--start-maximized")
# driver = ChromeDriver(options)
import time
import os
import ast
import urllib.request
from requests import get
# define the name of the directory to be created
# path = os.getcwd()
# path = "/tmp/year"

# try:
#     os.mkdir(path)

def get_string(str):
    alphanumeric = ""
    for character in str:
        if character.isalnum():
            alphanumeric += character
        else:
            alphanumeric += '_'
    return alphanumeric
PINNUM = '0962'
CARDNUM = '2536871'
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
url = 'https://www.zillow.com/homedetails/2322-Poinsettia-St-Santa-Ana-CA-92706/25091186_zpid/'
driver.get(url) 
soup = BeautifulSoup(driver.page_source, 'html.parser')
item = soup.find("div", {'class': 'ds-chip'})
print(item)
Price = item.find('h3', {'class': 'ds-price'}).text

# Price, Address, Bedroom count, Bathroom count, Square footage, description, and photos

bedbathsqure = item.find_all('span', {'class': 'ds-bed-bath-living-area'})
print(bedbathsqure)
Bedroom_count = bedbathsqure[0].find('span').text
Bathroom_count = bedbathsqure[1].find('span').text
Square_footage = bedbathsqure[2].find('span').text

Address = item.find('div', {'class': 'ds-price-change-address-row'}).text
Description = soup.find('div', {'class' : 'Text-aiai24-0 sc-kafWEX jwQXdm'}).text

print(Price, Bedroom_count, Bathroom_count, Square_footage, Address, Description)

driver.execute_script('setInterval(()=>{document.querySelector(".ds-media-col-hidden-mobile").scrollTop=10000;}, 1000);')
time.sleep(4)
soup = BeautifulSoup(driver.page_source, 'html.parser')
picul = soup.find('ul', {'class':'media-stream'})
lis = picul = picul.find_all('li', {'class': 'media-stream-tile'}, recursive = False)
print(lis)
imgid = 0
for Li in lis:
    print(type(Li.find('img')))
    if Li.find('img') == None:
        continue
    imgurl = Li.find('img')['src']
    print(imgurl)

    image_name_jpg = str(imgid) + '.jpg'
    imgid += 1
    img_data = get(imgurl).content
    while True:
        if (img_data):
            break
        img_data = get(imgurl).content
    with open('images/' + image_name_jpg, 'wb') as handler:
        handler.write(img_data)
print(len(lis))