import numpy as py

import wave
import struct

import matplotlib.pyplot as plt

def generate_wav_file(freq, file_name=None):
    num_samples = 48000
    sampling_rate = 48000.0
    amplitude = 16000

    sin_wave = [py.sin(2 * py.pi * freq * x/sampling_rate) for x in range(num_samples)]

    if file_name is not None:

        nframes = num_samples

        comptype = 'NONE'
        compname = 'not compressed'
        nchannels = 1
        sampwidth = 2

        wav_file = wave.open(file_name, 'w')
        wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

        for s in sin_wave:
            wav_file.writeframes(struct.pack('h', int(s*amplitude)))
            # the pack method converts the integter to a hexadecimal value so that the wav_file can properly maniuplate it

    return sin_wave
