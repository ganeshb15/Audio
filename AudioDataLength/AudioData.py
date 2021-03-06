#!/usr/bin/python3
from pydub import AudioSegment
import pandas as pd 
import os



def AudioFolder(Path,OutputFileName):
	currentDirectory = os.getcwd()
	os.chdir(Path) 
	stream = os.popen("find . -type f -name \"*.mp3\"")
	Data = stream.read()
	D=Data.split()

	DLength=[]

	Temp=D[0].split('/')
	i=1
	Depth=len(Temp)
	
	ListFiles=[]
	Length=[]
	
	
	df = pd.DataFrame(D, columns = ['Path'])
	DLength=[]
	FLength=[]
	ListFolder=[]
	while i<Depth:
		PathList=df.Path.unique()
		for j in PathList:
			index=df.index[df["Path"]==j].tolist()
			temp=j.split('/')
			

			if i==1:
				df["Path"][index]=j[1:-len(temp[-1])-1]
				if Depth<len(j.split('/')):
					Depth=len(j.split('/'))
				audio = AudioSegment.from_file(Path+j[1:])
				ListFiles.append(j[1:])
				DLength.append(int(audio.duration_seconds))
			else:
				df["Path"][index]=j[:-len(temp[-1])-1]
				
				DLength.append(sum(df["Length"][index]))
				FLength.append(sum(df["Length"][index]))
				ListFolder.append(j[1:])
				ListFiles.append(j[1:])
	
	

		if i==1:
			df.insert(1,"Length",DLength,True)
			
		
			
		i=i+1
	
	F1Length=[]
	os.chdir(currentDirectory) 
	def convert(seconds): 
		min, sec = divmod(seconds, 60) 
		hour, min = divmod(min, 60) 
		return "%d:%02d:%02d" % (hour, min, sec) 
	for i in FLength:
		F1Length.append(convert(i))
	df1 =pd.DataFrame({'Path': ListFolder,'Length': F1Length})
	
	df1.to_csv(OutputFileName+'.csv')
	return ListFolder,ListFolder
	

def AudioFile(Path,OutputFileName):

	currentDirectory = os.getcwd()
	os.chdir(Path) 
	stream = os.popen("find . -type f -name \"*.mp3\"")
	Data = stream.read()
	D=Data.split()
	
	DLength=[]
	
	os.chdir(currentDirectory) 
	
	f = open(OutputFileName+'.csv', "w")
	f.write("Path,Length\n")

	
	for i in D:
		audio = AudioSegment.from_file(Path+i[1:])
		DLength.append(audio.duration_seconds)
		f.write(i[1:]+","+str(audio.duration_seconds)+"\n")
	
	f.close()
	return D,DLength




