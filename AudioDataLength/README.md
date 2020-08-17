[![Build Status](https://travis-ci.org/ganeshb15/Audio.svg?branch=master)](https://travis-ci.org/ganeshb15/Audio)

# **Audio Data Length** 

**Goal :** The function  gives a list of all the audio files length. And also gives the sum of all the audio file length in a folder. Works on recursively  for all the sub-folder as well. Will get the length list in a .csv file. Can be used for data analysis and assessment. Can get the amount of data to train.

## Output 
Output is the .csv file with all the list of audio file length. For folder as well as files as per the selection. The sample output is shown below.

![File](https://github.com/ganeshb15/Audio/blob/master/AudioDataLength/Output/File.png)
![Folder](https://github.com/ganeshb15/Audio/blob/master/AudioDataLength/Output/Folder.png)


## **How it works**
It is built in 3 forms. 

 1. Python
```python
import AudioData
AudioData.AudioFile("/home/travis/Sample","File")
AudioData.AudioFolder("/home/travis/Sample","Folder")
```

 2. Ubuntu 
Download this file [Link](https://raw.githubusercontent.com/ganeshb15/Audio/master/AudioDataLength/AudioDataUbntu) and run the code below in the terminal.
```sh
sudo chmod 777 AudioDataUbntu
sudo cp AudioDataUbntu /bin/AudioDataUbntu
```
 3.  Ubuntu Binary file [Same as 2 but no installation required, but can't see the code as well]

