import numpy as np
from pydub import AudioSegment
import matplotlib.pyplot as plt

def read_signal(file_path, normalized=True):
    sound = AudioSegment.from_file(file_path).set_channels(1)
    samples = sound.get_array_of_samples()
    arr = np.array(samples)
    if normalized:
        return sound.frame_rate, arr.astype(np.float32) / (2**15)
    return sound.frame_rate, arr


def find_avg_ampl(file_path):
    frame_rate, arr = read_signal(file_path)
    mean_ampl = np.mean(np.abs(arr))
    threshold = mean_ampl * 1.2
    return threshold, arr, frame_rate


def find_strongest_beat(file_path, window_ms=300):
    threshold, arr, frame_rate = find_avg_ampl(file_path)
    beats = np.where(np.abs(arr) > threshold)[0]

    local_maxima = []
    for i in range(1, len(beats) - 1):
        prev = beats[i - 1]
        curr = beats[i]
        next = beats[i + 1]

        if np.abs(arr[curr]) > np.abs(arr[prev]) and np.abs(arr[curr]) > np.abs(arr[next]):
            local_maxima.append(curr)

    local_maxima = np.array(local_maxima)
    window_size = int((window_ms / 1000) * frame_rate)

    selected_peaks = []
    start = 0
    while start < len(arr):
        end = start + window_size
        in_window = local_maxima[(local_maxima >= start) & (local_maxima < end)]
        if len(in_window) > 0:
            best = in_window[np.argmax(np.abs(arr[in_window]))]
            selected_peaks.append(best)
        start += window_size

    return np.array(selected_peaks), arr, frame_rate


def visualize_strongest_beat(file_path):
    local_max, arr, frame_rate = find_strongest_beat(file_path)
    time_axis = np.linspace(0, len(arr) / frame_rate, num=len(arr))

    plt.figure(figsize=(14, 5))
    plt.plot(time_axis, arr, label="Audio Signal", alpha=0.7)

    if len(local_max) > 0:
        top_20 = local_max[:2000]  # top 20 by amplitude
        times = top_20 / frame_rate
        plt.scatter(times, arr[top_20], color='red', s=50, label="Top 20 Strong Beats")

    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Waveform with Top 20 Strong Beats")
    plt.legend()
    plt.tight_layout()
    plt.show()




visualize_strongest_beat("clip44.mp3")
