import numpy as np

import wave
import struct

import matplotlib.pyplot as plt

import main

frame_rate = 48000.0
file = 'test.wav'

num_samples = 48000
wav_file = wave.open(file, 'r')

data = wav_file.readframes(num_samples)
wav_file.close

data = np.array(struct.unpack('{n}h'.format(n=num_samples), data))
frequencies = np.abs(np.fft.fft(data))
# fft returns complex numbers to get real valued numbers we need to take the abs

wave = np.array(main.generate_wav_file(1000))
wave_noise = np.array(main.generate_wav_file(50))

combined_signal = wave + wave_noise

plt.subplot(3,1,1)
plt.plot(wave[:500])
plt.title('Original Signal')

plt.subplot(3,1,2)
plt.plot(wave_noise[:4000])
plt.title('Noise')

plt.subplot(3,1,3)
plt.plot(combined_signal[:3000])
plt.title('Combined Signal')
plt.show()
