from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup

import time
import re
import pandas as pd

df=pd.read_csv("Temp.csv")
CSV=df[df["Enable"]==1]

#Set driver
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome('driver/chromedriver',chrome_options=options)

# Loading the Website
Website='http://newsonair.com/RNU-NSD-Audio-Archive-Search.aspx'
driver.get(Website)
time.sleep(2)

# RNU/NSD Audio Archive Search
# Selection = RNU NSD Audio Bulletins
driver.find_element_by_id("ctl00_ContentPlaceHolder1_program_type_cbl_0").click()
time.sleep(2)

# RNU-NSD Type
# Selection =  RNU-NSD Type
driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddwtype']/option[text()='Regional']").click()
time.sleep(2)

f = open("Links.csv", "w")
f.write("Name,Language,Bulletin,Link\n")
		
for i in CSV.index:
	# RNU-NSD Name
	driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddwrnunsdname']/option[text()='"+CSV['Name'][i]+"']").click()
	time.sleep(2)

	# RNU-NSD Language Name 	
	driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddwlanguages']/option[text()='"+CSV['Language'][i]+"']").click()
	time.sleep(2)
	
	# RNU-NSD  Bulletin Name
	select = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder1$ddwrnunsd_bname'))
	select.select_by_visible_text("{:04d}".format(int(CSV['Bulletin'][i])))
	time.sleep(2)
	
	# From Date
	text_area = driver.find_element_by_id('ctl00_ContentPlaceHolder1_from_Date_txt')
	driver.find_element_by_id('ctl00_ContentPlaceHolder1_from_Date_txt').clear()
	text_area.send_keys(CSV['From'][i])
	time.sleep(2)
	
	# To Date
	text_area = driver.find_element_by_id('ctl00_ContentPlaceHolder1_to_Date_txt')
	driver.find_element_by_id('ctl00_ContentPlaceHolder1_to_Date_txt').clear()
	text_area.send_keys(CSV['To'][i]+"\n")
	time.sleep(2)


	html_source = driver.page_source
	soup = BeautifulSoup(html_source, 'html.parser')
	span = soup.find("span", id="ctl00_ContentPlaceHolder1_lblpage")
	Temp=span.text
	Temp1=Temp.split()
	PageNo=int(Temp1[-1])

	for k in range(0,PageNo):
		time.sleep(2)
		html_source = driver.page_source
		result = re.findall('<audio(.*)</audio>', html_source)
		for x in result:
			y=x.split()[0][5:-1]
			if y.endswith(".mp3") and y.startswith('http://newsonair.nic.in') :
				f.write(CSV['Name'][i]+","+CSV['Language'][i]+","+"{:04d}".format(int(CSV['Bulletin'][i]))+","+y+"\n")
		
		driver.find_element_by_link_text("Next").click()
	
		time.sleep(2)
f.close()
driver.quit()
