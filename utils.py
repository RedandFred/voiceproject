#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: utils.py
# Date: Wed Dec 25 20:24:38 2013 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>

import numpy
from scipy.io import wavfile

kwd_mark = object()

def cached_func(function):
    cache = {}
    def wrapper(*args, **kwargs):
        key = args + (kwd_mark,) + tuple(sorted(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = function(*args, **kwargs)
            cache[key] = result
            return result
    return wrapper


def diff_feature(feat, nd=1):
    diff = feat[1:] - feat[:-1]
    feat = feat[1:]
    if nd == 1:
        return numpy.concatenate((feat, diff), axis=1)
    elif nd == 2:
        d2 = diff[1:] - diff[:-1]
        return numpy.concatenate((feat[1:], diff[1:], d2), axis=1)



def read_wav(fname):
    fs, signal = wavfile.read(fname)
    assert len(signal.shape) == 1, "Only Support Mono Wav File!"
    return fs, signal

def write_wav(fname, fs, signal):
    wavfile.write(fname, fs, signal)

def time_str(seconds):
    minutes = int(seconds / 60)
    sec = int(seconds % 60)
    return "{:02d}:{:02d}".format(minutes, sec)

def monophonic(signal):
    if signal.ndim > 1:
        signal = signal[:,0]
    return signal

if __name__ == "__main__":
    pass
