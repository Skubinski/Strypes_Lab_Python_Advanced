from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

def read_signal(file_path, normalized = True):
    sound = AudioSegment.from_file(file_path).set_channels(1)

    samples = sound.get_array_of_samples()

    arr = np.array(samples)

    if normalized:
        return sound.frame_rate, arr.astype(np.float32) / (2**15)
    return sound.frame_rate, arr

def frames(file_path, frame_size):
    frame_rate, arr = read_signal(file_path)

    num_frames = len(arr) // frame_size

    arr = arr[:num_frames * frame_size]

    return np.reshape(arr, (num_frames, frame_size)), frame_rate

def short_term_energy(file_path, frame_size):
    frames_arr, frame_rate= frames(file_path, frame_size)

    energies = np.sum(frames_arr ** 2, axis=1)


    return energies, frame_rate

def beat_detections(file_path, frame_size, spike):
    energies, frame_rate = short_term_energy(file_path, frame_size)

    threshold = np.mean(energies) * spike

    beat_frames = np.where(energies > threshold)[0]

    return beat_frames, energies, frame_rate

def visualize_beats(file_path, frame_size=1024, spike=1.5):
    beat_frames, energies, frame_rate = beat_detections(file_path, frame_size, spike)
    time_axis = np.arange(len(energies)) * (frame_size / frame_rate)

    plt.figure(figsize=(14, 5))
    plt.plot(time_axis, energies, label='Short-Term Energy')
    plt.scatter(time_axis[beat_frames], energies[beat_frames], color='red', label='Detected Beats')
    plt.xlabel('Time (s)')
    plt.ylabel('Energy')
    plt.title('Beat Detection using Short-Term Energy')
    plt.legend()
    plt.tight_layout()
    plt.show()

def visualize_signal_with_beats(file_path, frame_size=1024):
    frame_rate, signal = read_signal(file_path)
    energies, _ = short_term_energy(file_path, frame_size)

    time_axis = np.linspace(0, len(signal) / frame_rate, num=len(signal))
    energy_time = np.arange(len(energies)) * (frame_size / frame_rate)

    # Find peaks (local max) and valleys (local min)
    peaks = []
    valleys = []
    for i in range(1, len(energies) - 1):
        if energies[i] > energies[i-1] and energies[i] > energies[i+1]:
            peaks.append(i)
        elif energies[i] < energies[i-1] and energies[i] < energies[i+1]:
            valleys.append(i)

    peak_times = np.array(peaks) * frame_size / frame_rate
    valley_times = np.array(valleys) * frame_size / frame_rate

    # Plot signal
    plt.figure(figsize=(14, 5))
    plt.plot(time_axis, signal, label='Audio Signal', alpha=0.6)

    # Plot red dots for peaks
    plt.scatter(peak_times, np.zeros_like(peak_times), color='red', label='Peaks (Beats)', zorder=5)

    # Plot blue dots for valleys
    plt.scatter(valley_times, np.zeros_like(valley_times), color='blue', label='Valleys', zorder=5)

    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Audio Signal with Peak and Valley Detection')
    plt.legend()
    plt.tight_layout()
    plt.show()



visualize_signal_with_beats('clip44.mp3', frame_size=1024)







