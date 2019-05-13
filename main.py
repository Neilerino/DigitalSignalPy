import numpy as np

import wave
import struct

import matplotlib.pyplot as plt

from generate_wav import generate_wav
from vertical_plot import VerticalPlot
from signal_utilities import get_frame_rate, get_frequency

frame_rate = get_frame_rate()

wave = generate_wav(1000)
wave_noise = generate_wav(50)

combined_signal = wave + wave_noise

signals = [
        [wave[:500], 'Original Signal'],
        [wave_noise[:4000], 'Noise'],
        [combined_signal[:3000], 'Combined Signal'],
]

vertical_plot = VerticalPlot(signals)
# vertical_plot.show()

print(get_frequency(wave_noise))