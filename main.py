from selenium import webdriver
import pandas as pd
#import requests
from bs4 import BeautifulSoup
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

url = 'https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.p_selectsubject'

wd = webdriver.Chrome('chromedriver', options=options)
wd.get(url)
status = wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[11]/td[1]/input").is_selected()
print(status)

wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[11]/td[1]/input").click()

status = wd.find_element_by_xpath("/html/body/div[3]/form/table/tbody/tr[11]/td[1]/input").is_selected()
print(status)

wd.find_element_by_xpath("/html/body/div[3]/form/input").click()
wd.implicitly_wait(3)
html = wd.page_source
file1=open("t.txt","w")
file1.write(html)
file1.close()
#print(html)
