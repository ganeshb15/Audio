import unittest
import os
import AudioData

class TestAudioData(unittest.TestCase):
	def testAudioData(self):
		try:
			AudioData.AudioFile("/home/ganesh/Brainstorm/Project/AllIndiaRadio/git/Audio.git/trunk/AudioDataLength/Sample","File")
			AudioData.AudioFolder("/home/ganesh/Brainstorm/Project/AllIndiaRadio/git/Audio.git/trunk/AudioDataLength/Sample","Folder")
		

		except AssertionError as e:
			print(e)

			


if __name__ == '__main__':
	unittest.main()
