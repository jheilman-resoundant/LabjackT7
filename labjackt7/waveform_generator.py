import numpy as np
# from .core import LabjackT7

class WaveformGenerator:
    def __init__(self, labjack):
        self.labjack = labjack

    def start(self, t, V, channels = [0]):
        #disabled until resample() is restored
        # data, scanRate = self.labjack.stream.resample(V, np.max(t))
        # self.labjack.stream.configure(settling_time=0, resolution_index=0, clock_source=0)
        # self.labjack.stream.set_trigger(None)
        # self.labjack.stream.AOut(channels, data, scanRate, loop=1)
        return
