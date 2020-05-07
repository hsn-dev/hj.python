from selenium import webdriver 
from bs4 import BeautifulSoup
from datetime import datetime
import time
import os
  
'''
	How to make .exe file
	pip install pyinstaller
	pyinstaller -w -F -i [icon_file] [python_file]
'''
username = 'admin'
password = 'WXC8XLGG'

  
driver = webdriver.Chrome() 
driver.get("http://192.168.1.1")

time.sleep(3)

login_btn = driver.find_element_by_xpath('//*[@id="login"]')
login_btn.click()

time.sleep(2)

input_username = driver.find_element_by_xpath('//*[@id="username"]')
input_username.send_keys(username)

input_psword = driver.find_element_by_xpath('//*[@id="password"]')
input_psword.send_keys(password)

submit_btn = driver.find_element_by_xpath('//*[@id="BTN_Login"]')
submit_btn.click()

time.sleep(2)

conn_tab = driver.find_element_by_xpath('//*[@id="navi-connection"]')
conn_tab.click()

time.sleep(2)

page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')

tag = soup.find('font', id="used_total_traffic_data")

traffic_data = tag.string
time = datetime.now().strftime("%H:%M:%S")
date = datetime.now().date().strftime("%B %d, %Y")
data_usage_file = r'C:\Users\Hasan\Desktop\New folder\DataUsage.txt'

with open(data_usage_file, 'a') as f:
	filesize = os.path.getsize(data_usage_file)
	if filesize == 0:
		f.write("Date\t\tTime\t\tUsage\n")
	f.write(date + "\t")
	f.write(time + "\t")
	f.write(traffic_data + "\n")

driver.quit()