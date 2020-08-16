import unittest
import os
import AudioData

class TestAudioData(unittest.TestCase):
	def testAudioData(self):
		try:
			AudioData.AudioFile("/home/travis/build/ganeshb15/Audio/AudioDataLength/Sample","File")
			AudioData.AudioFolder("/home/travis/build/ganeshb15/Audio/AudioDataLength/Sample","Folder")
		

		except AssertionError as e:
			print(e)

			


if __name__ == '__main__':
	unittest.main()
