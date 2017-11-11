import glob
import logging
import argparse
from modelinterface import Nodelinterface
def main():
	peoplelist = glob.glob("../../voicedata/VCTK-Corpus/wav48/*")
	for person_dir in peoplelist:
		logging.info("input data dir: {}".format(person_dir))
		voicefile_list = glob.glob("{}/*".format(person_dir))

'''
def task_enroll(input_dirs, output_model):
    m = ModelInterface()
    input_dirs = [os.path.expanduser(k) for k in input_dibrs.strip().split()]
    dirs = itertools.chain(*(glob.glob(d) for d in input_dirs))
    dirs = [d for d in dirs if os.path.isdir(d)]
    files = []

    for d in dirs:
        label = os.path.basename(d.rstrip('/'))
        wavs = glob.glob(d + '/*.wav')

        print("Label {0} has files {1}".format(label, ','.join(wavs)))
        for wav in wavs:
            fs, signal = read_wav(wav)  # fs : sample rate, signal : np array
            m.enroll(label, fs, signal)

    m.train()
    m.dump(output_model) # save trained things
'''



if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	main()










'''
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input',help='data dir', required=True)
logging.basicConfig(level=logging.DEBUG)
logging.debug("디버깅용 로그~~")
logging.info("도움이 되는 정보를 남겨요~")
logging.warning("주의해야되는곳!")
logging.error("에러!!!")
logging.critical("심각한 에러!!")
'''
