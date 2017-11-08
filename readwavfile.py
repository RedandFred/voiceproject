import os
import wave 
import glob
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc
import pprint
from scipy import spatial
def main():

	domain = 1000	
	test = []
	folderlist = glob.glob("./data/*")
	for man in folderlist[:2]:
		voicefiles = glob.glob("{}/*".format(man))
		for wav in voicefiles[2:4]:
			print(wav)
			(rate,sig) = wavfile.read(wav)
			test.append(mfcc(sig, samplerate=rate, nfft=5000))
			
	for i in range(4):
		print(test[i][50])
	print(1 - spatial.distance.cosine(test[0][90], test[1][90]))
	print(1 - spatial.distance.cosine(test[1][90], test[2][90]))
	print(1 - spatial.distance.cosine(test[2][90], test[3][90]))
	#test = mfcc(sig, samplerate=rate, nfft=1200)
	#print(test[10])
	#test = mfcc(sig, samplerate=rate, nfft=5000)
	#print(test[10])
	#average = np.average(np.absolute(signal))
	#time = list(range(len(signal)))
	#starttime = find_start_time(signal, domain)
	#endtime = find_end_time(signal, domain)
	# find speech end time

	#plt.plot(time[starttime:], signal[starttime:], '-o')
	#plt.plot(time, signal)
	#plt.show()

# find speech start time
def find_start_time(signal, domain):
	for i in list(range(len(signal))):
		absolute = np.absolute(signal[i:i+domain])
		average = np.average(absolute)
		if average > 1000:
			starttime = i
			break
	return starttime

# find speech end time
def find_end_time(signal, domain):
	for i in list(range(len(signal))):
		absolute = np.absolute(signal[-i-domain:-i])
		average = np.average(absolute)
		if average > 1000:
			endtime = i
			break	
	return endtime

if __name__ == "__main__":
	main()
