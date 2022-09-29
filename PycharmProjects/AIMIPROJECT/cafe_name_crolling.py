import time
import sys
import os

import pandas as pd
import numpy as np


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import warnings
warnings.filterwarnings('ignore')


search_keyword = '홍대 카페'

path = '/Users/jungmin/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get(f"https://map.naver.com/v5/search/{search_keyword}?c=14203933.7141038,4562681.4505997,10,0,0,0,dh")
driver.switch_to.frame("searchIframe")

# 가게 이름 60개 수집


title_list = []

try:
    for i in range(1, 7):
        driver.find_element_by_link_text(str(i)).click()
        try:
            for j in range(3, 70, 3):
                element = driver.find_elements_by_css_selector('.OXiLu')[j]
                ActionChains(driver).move_to_element(element).key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
        except:
            pass

        title_raw = driver.find_elements_by_css_selector(".OXiLu")
        for title in title_raw:
            title = title.text
            title_list.append(title)



except:
    pass

cafe_list=[]

for cafe_name in title_list:
    if "홍대" not in cafe_name:
        new_name = "홍대 "+cafe_name
        cafe_list.append(new_name)
    else:
        cafe_list.append(cafe_name)

print(cafe_list)

