import json

def get_freqs():
    with open('config.json', 'r') as f:
        input = json.load(f)
    if input['use_freq']:
        return input['frequencies']
    refresh_rate = input['monitor_refresh_rate']
    freqs = list(map(lambda n_frame: refresh_rate/n_frame, input['frame_rates']))
    return freqs

def get_periods():
    periods = list(map(lambda f: 1/f, get_freqs()))
    return periods

def get_delays():
    delays = list(map(lambda p: p * 1000 / 2, get_periods()))
    return delays