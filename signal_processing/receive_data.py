from utils.constants import SAMPLE_RATE
from pylsl import StreamInlet, resolve_stream

def get_inlet():
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
    inlet = StreamInlet(streams[0]) # create a new inlet to read from the stream
    return inlet
