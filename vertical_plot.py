import matplotlib.pyplot as plt
import multiprocessing
from threading import Thread

class VerticalPlot:
    def __init__(self, signals):
        self.plot = plt
        length = len(signals)
        for index, signal in enumerate(signals):
            self.plot.subplot(length, 1 , index + 1)
            self.plot.plot(signal[0])
            self.plot.title(signal[1])

    def show(self):
        self.plot.show()
