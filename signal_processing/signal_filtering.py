import sys

import pandas as pd
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

from signal_processing.receive_data import *
from utils.constants import SAMPLE_RATE

def signal_filtering():
    print("Signal filtering...")
    inlet = get_inlet()
    while True:
        chunk, timestamp = inlet.pull_sample()
        if timestamp:
            with open('log.txt', 'a') as f:
                print(chunk, file=f)