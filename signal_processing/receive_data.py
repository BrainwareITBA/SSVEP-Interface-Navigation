import numpy as np
from pylsl import StreamInlet, resolve_stream
from utils.constants import SAMPLE_RATE

def get_inlet():
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
    inlet = StreamInlet(streams[0]) # create a new inlet to read from the stream
    return inlet

def get_chunk(inlet: StreamInlet, chunk_size: int = SAMPLE_RATE, num_channels: int = 8):
    chunk = np.zeros((chunk_size, num_channels))
    num_samples = 0
    while num_samples < chunk_size:
        sample, timestamp = inlet.pull_sample()
        if timestamp:
            chunk[num_samples] = sample
            num_samples += 1
    return chunk