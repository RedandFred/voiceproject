import glob
import logging
import argparse
from modelinterface import ModelInterface
from utils import read_wav
import os
import itertools
def main():
    print(1)
    task_enroll("../../Downloads/VCTK-Corpus/wav48/", './test.txt')
    #task_predict("../../voicedata/VCTK-Corpus/wav48/p225/", "./VCTC_Learned.txt")

def task_enroll(input_dirs, output_model):
    m = ModelInterface()
    dirs = glob.glob(input_dirs + "*")
    files = []
    print(dirs)  
    for d in dirs:
        label = os.path.basename(d.rstrip('/'))
        print(label)
        wavs = glob.glob(d + '/*.wav')
        #print(wavs)

        #print("Label {} has files {}".format(label, ','.join(wavs)))
        if len(wavs) < 150:
            asdf = len(wavs)
        else: 
            asdf = 150
        for wav in wavs[:asdf]:
            print(wav)
            fs, signal = read_wav(wav)  # fs : sample rate, signal : np array
            m.enroll(label, fs, signal)

    m.train()
    m.dump(output_model) # save trained things


def task_predict(input_files, input_model):
    m = ModelInterface.load(input_model)
    fls = glob.glob(input_files+'*')[120:140]
    fls.append('../../voicedata/VCTK-Corpus/wav48/p228/p228_001.wav')
    for f in fls:
        fs, signal = read_wav(f)
        label = m.predict(fs, signal)
        print(f, '->', label)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()










'''
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input',help='data dir', required=True)
logging.basicConfig(level=logging.DEBUG)
logging.debug("")
logging.info("")
logging.warning("")
logging.error()
logging.critical()
'''
