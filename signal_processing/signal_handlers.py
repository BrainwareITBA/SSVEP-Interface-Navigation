import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

from signal_processing.receive_data import *
from utils.constants import *

channels = ["FZ", "CZ", "PZ", "P4", "P3", "OZ", "PO8", "PO7"]
colors = ('blue','green','magenta','olive','salmon','teal','maroon','orange')


def plot_signal(signal_by_channel, plot_title="EEG Signal", channels_to_use=channels):
    num_samples = signal_by_channel.shape[1]
    samples = np.linspace(0, num_samples/SAMPLE_RATE, num_samples)
    fig, axs = plt.subplots(len(channels_to_use), figsize=(10, 5), sharex=True)
    for idx in range(len(channels_to_use)):
        axs[idx].plot(samples, signal_by_channel[idx], colors[idx])
        axs[idx].set_title(channels_to_use[idx])
    fig.suptitle(plot_title, fontsize=16)
    plt.savefig(f"output/{plot_title}.png")


def plot_freqs(signal_by_channel, signal_string="Original", channels_to_use=channels):
    fig, axs = plt.subplots(len(channels_to_use), figsize=(10, 5), sharex=True)
    for idx in range(len(channels_to_use)):
        f, p = signal.periodogram(signal_by_channel[idx], SAMPLE_RATE)
        axs[idx].plot(f, p, colors[idx])
        axs[idx].set_title(channels[idx])
    fig.suptitle(f"{signal_string} signals in frequency domain", fontsize=16)
    plt.savefig(f"output/{signal_string} signals in frequency domain.png")


def signal_filtering(channels_to_use=channels):
    print("Signal filtering...")
    inlet = get_inlet()
    while True:
        chunk = get_chunk(inlet, SAMPLE_RATE)
        signal_by_channel = chunk.T
        '''
        plot_signal(signal_by_channel, channels_to_use=channels)                            # original signals
        plot_freqs(signal_by_channel, channels_to_use=channels)                             # original signals in frequency space
        '''
        sos = signal.butter(4, [6, 25], 'bandpass', fs=250, analog=False, output='sos')     # filter
        filtered_signal = signal.sosfiltfilt(sos, signal_by_channel)                        # applying filter
        '''
        plot_signal(filtered_signal, plot_title="EEG Signal", channels_to_use=channels)
        '''
        f, evoked_potentials = signal.periodogram(filtered_signal, SAMPLE_RATE)             # filtered signals in frequency space
        '''
        plot_freqs(filtered_signal, signal_string="Filtered", channels_to_use=channels)
        '''
        freq = 0
        for idx in range(len(channels_to_use)):
            freq = freq + f[evoked_potentials[idx].argmax()]
        freq /= len(channels_to_use)
        print(freq)


def write_signal_to_file():
    print("Receiving signal...")
    inlet = get_inlet()
    chunk, timestamp = inlet.pull_sample()
    if timestamp:
        with open('log.txt', 'a') as f:
            print(chunk, file=f)
