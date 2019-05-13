from numpy import fft, argmax

# Used to keep the framerate variable which will be used anywhere in the project
def get_frame_rate():
    framerate = 48000.0
    return framerate


def get_frequency(signal):
    fourier = fft.fft(signal)
    freqs = fft.fftfreq(len(fourier))

    index = argmax(abs(fourier))
    freq = freqs[index]

    freq_hz = abs(freq * get_frame_rate())

    return freq_hz
