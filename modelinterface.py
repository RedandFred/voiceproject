#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: interface.py
# Date: Thu Sep 14 14:56:58 2017 -0700
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

import time
import os
import sys
from collections import defaultdict
from scipy.io import wavfile
import numpy as np
#import cPickle as pickle
import pickle
import traceback as tb

#from feature import mix_feature
import MFCC
import LPC
from skgmm import GMMSet
from sklearn.mixture import GaussianMixture as GMM
#from feature import mix_feature
#from filters.VAD import VAD
import pickle
#try:
#    from gmmset import GMMSetPyGMM as GMMSet
#    from gmmset import GMM
#except:
#    print >> sys.stderr, "Warning: failed to import fast-gmm, use gmm from scikit-learn instead"


CHECK_ACTIVE_INTERVAL = 1       # seconds

class ModelInterface(object):
    #from feature.LPC import extract2
    #from feature.MFCC import extract
    UBM_MODEL_FILE = None

    def __init__(self):
        self.features = defaultdict(list)
        self.gmmset = GMMSet()
        #self.vad = VAD()
    '''
    def mix_feature(self, tup):
        mfcc = MFCC.extract(tup)
        lpc = LPC.extract(tup)
        if len(mfcc) == 0:
            print(sys.stderr, "ERROR.. failed to extract mfcc feature:", len(tup[1]))
        return np.concatenate((mfcc, lpc), axis=1)
    '''
    def enroll(self, name, fs, signal):
        """
        add the signal to this person's training dataset
        name: person's name
        """
        mfcc = MFCC.extract((fs, signal))
        lpc = LPC.extract2((fs, signal))
        feat = np.concatenate((mfcc, lpc), axis=1) # output : np.array of a wave file, ""[mfcc, lpc]"",
        self.features[name].extend(feat) # label : name of a person, feature : defaultdict

    def _get_gmm_set(self):
        return GMMSet()

    def train(self):
        self.gmmset = self._get_gmm_set() #gmmset.GMMSet()
        start = time.time()
        print("Start training...")
        for name, feats in self.features.iteritems():
            print(name)
            self.gmmset.fit_new(feats, name)
        print(time.time() - start, " seconds")
        for i in range(len(self.gmmset.y)):
            with open("./pickled/{}".format(self.gmmset.y[i]), 'wb') as ff:
                pickle.dump((self.gmmset.y[i], self.gmmset.x[i]),ff)
        sys.exit(1)
    def predict(self, fs, signal):
        """
        return a label (name)
        """
        #try:
        mfcc = MFCC.extract((fs, signal))
        lpc = LPC.extract2((fs, signal))
        feat = np.concatenate((mfcc, lpc), axis=1)
        #feat = mix_feature((fs, signal)) # feat : np.concatenate((mfcc, lpc), axis=1)
        #except:
        #    pass
        return self.gmmset.predict_one(feat)

    def dump(self, fname):
        """ dump all models to file"""
        self.gmmset.before_pickle()
        with open(fname, 'w') as f:
            pickle.dump(self, f, -1)
        self.gmmset.after_pickle()

    @staticmethod
    def load(fname):
        """ load from a dumped model file"""
        with open(fname, 'r') as f:
            R = pickle.load(f)
            R.gmmset.after_pickle()
            return R



if __name__ == "__main__":
    """ some testing"""
    m = ModelInterface()
    fs, signal = wavfile.read("../corpus.silence-removed/Style_Reading/f_001_03.wav")
    m.enroll('h', fs, signal[:80000])
    fs, signal = wavfile.read("../corpus.silence-removed/Style_Reading/f_003_03.wav")
    m.enroll('a', fs, signal[:80000])
    m.train()
