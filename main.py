import numpy as np

import wave
import struct

import matplotlib.pyplot as plt

from generate_wav import generate_wav
from vertical_plot import VerticalPlot


frame_rate = 48000.0
file = 'test.wav'

num_samples = 48000
wav_file = wave.open(file, 'r')

data = wav_file.readframes(num_samples)
wav_file.close

data = np.array(struct.unpack('{n}h'.format(n=num_samples), data))
frequencies = np.abs(np.fft.fft(data))
# fft returns complex numbers to get real valued numbers we need to take the abs

wave = np.array(generate_wav(1000))
wave_noise = np.array(generate_wav(50))

combined_signal = wave + wave_noise

signals = [
        [wave[:500], 'Original Signal'],
        [wave_noise[:4000], 'Noise'],
        [combined_signal[:3000], 'Combined Signal'],
]

vertical_plot = VerticalPlot(signals)
vertical_plot.show()