# this module will be imported in the into your flowgraph
from gnuradio import gr
from gnuradio import iio
import numpy as np
class center_freq_block(gr.sync_block):
    def __init__(self, freq_start, freq_stop, freq_step):
        gr.sync_block.__init__(self,
            name="center_freq_block",
            in_sig=None,
            out_sig=[np.float32])
        self.freq_start = freq_start
        self.freq_stop = freq_stop
        self.freq_step = freq_step


    def work(self, input_items, output_items):
        out = output_items[0]
        while self.freq_start <= self.freq_stop:
            out = self.pluto_src.read()
            self.freq_start += self.freq_step
            self.pluto_src.set_frequency(self.freq_start)
            time.sleep(0.1)
        return len(out)

# Create an instance of the block with start frequency = 70e6, stop frequency = 5e9, and step frequency = 10e6
center_freq = center_freq_block(70e6, 5e9, 10e6)

