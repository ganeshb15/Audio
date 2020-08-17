import pandas as pd
import os

FolderSource="Source"
path=os.getcwd()+"/"+FolderSource
Link=pd.read_csv("Links.csv")
isdir = os.path.isdir(path)
if not isdir:
	os.mkdir(FolderSource)
os.chdir(path) 
  


for i in Link.index:
	isdir = os.path.isdir(path+"/"+Link['Language'][i])
	if not isdir:
		os.mkdir(Link['Language'][i])
	os.chdir(path+"/"+Link['Language'][i])
	os.system("wget "+Link['Link'][i])
	os.chdir(path)

	
