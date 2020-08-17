from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import time
import re
import pandas as pd
na='http://newsonair.com/RNU-NSD-Audio-Archive-Search.aspx'


#Set driver
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 
driver = webdriver.Chrome(chrome_options=options)


driver.get(na)
time.sleep(5)
#driver.find_element_by_link_text("RNU NSD Audio Bulletins").click()
driver.find_element_by_id("ctl00_ContentPlaceHolder1_program_type_cbl_0").click()
#radio1 = driver.findElement(By.id(""))
#radio1.click()
time.sleep(5)
# Selection of " RNU-NSD Type"		
driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddwtype']/option[text()='Regional']").click()
time.sleep(2)
# Selection of "RNU-NSD Name"
select_box = driver.find_element_by_name("ctl00$ContentPlaceHolder1$ddwrnunsdname")
options = [x for x in select_box.find_elements_by_tag_name("option")]
Name=[]

for element in options:
	Name.append(element.text)
time.sleep(2)
data_dict={}
TEMMP=[]
length=[]
Type=[]
Language=[]
Bulletin=[]
for i in range(1,len(Name)):
	TEMMP=[]
	driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddwrnunsdname']/option[text()='"+Name[i]+"']").click()
	time.sleep(2)
	select_box = driver.find_element_by_name("ctl00$ContentPlaceHolder1$ddwlanguages")
	options = [x for x in select_box.find_elements_by_tag_name("option")]
	for i1 in range(1,len(options)):
		#print(options[i1].text)
		TEMMP.append(options[i1].text)
		
		
	for i2 in TEMMP:
		driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddwlanguages']/option[text()='"+i2+"']").click()
		time.sleep(2)
		select_box = driver.find_element_by_name("ctl00$ContentPlaceHolder1$ddwrnunsd_bname")
		options1 = [x for x in select_box.find_elements_by_tag_name("option")]
		time.sleep(2)
		for i3 in range(1,len(options1)):
			Language.append(i2)
			Type.append(Name[i])
			Bulletin.append(options1[i3].text)	
			
#print(Language)
#print(Type)
#print(Bulletin)
#	print(Type)
#	print(TEMMP)
#	time.sleep(2)
#min_length=max(length)
#df = pd.DataFrame({k:pd.Series(v[:min_length]) for k,v in data_dict.items()})
#df = pd.DataFrame(wordFreqDic) 
#print(Type)
#print(TEMMP)
df = pd.DataFrame(list(zip(Type,Language,Bulletin)), columns =['Name', 'Language','Bulletin']) 
df.to_csv('filename.csv')
driver.quit()
