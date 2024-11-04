import numpy as np
import matplotlib.pyplot as plt
import h5py
import argparse

def main(input_file):
    # Function to apply Fast Fourier Transform and normalize it
    def normalized_fourier(waveform, tp0):
        peak = np.argmax(waveform)
        frq = np.fft.fftfreq(len(waveform[tp0:peak]), d=1)
        magnitude = np.abs(np.fft.fft(waveform[tp0:peak]))
        normalized_fft = magnitude / np.max(magnitude)
        return normalized_fft, frq

    # Function to calculate Low Frequency Power Ratio (LFPR)
    def lfpr(frq_waveform, threshold=0.05):
        power_spectrum = np.abs(frq_waveform)**2
        low_frequency_power = np.sum(power_spectrum[frq_tdrift < threshold])
        return low_frequency_power / np.sum(power_spectrum)

    # Load the data from the HDF5 file
    with h5py.File(input_file, 'r') as file:
        # Load the raw waveforms and labels
        raw_waveform = np.array(file["raw_waveform"])
        energy_label = np.array(file["energy_label"])
        psd_label_low_avse = np.array(file["psd_label_low_avse"])
        psd_label_high_avse = np.array(file["psd_label_high_avse"])
        psd_label_dcr = np.array(file["psd_label_dcr"])
        psd_label_lq = np.array(file["psd_label_lq"])
        tp0 = np.array(file["tp0"])
        detector = np.array(file["detector"])
        run_number = np.array(file["run_number"])
        id = np.array(file["id"])

        # Select a random index
        random_index = np.random.choice(raw_waveform.shape[0])

        # Get the random waveform and labels
        random_waveform = raw_waveform[random_index]
        energy_value = energy_label[random_index]
        psd_low_avse_value = psd_label_low_avse[random_index]
        psd_high_avse_value = psd_label_high_avse[random_index]
        psd_dcr_value = psd_label_dcr[random_index]
        psd_lq_value = psd_label_lq[random_index]
        tp0_value = tp0[random_index]
        detector_value = detector[random_index]
        run_number_value = run_number[random_index]
        id_value = id[random_index]

    # Perform FFT and extract parameters
    fft_tdrift, frq_tdrift = normalized_fourier(random_waveform, tp0_value)
    peak = np.argmax(random_waveform)
    time_tdrift = np.arange(peak - tp0_value)

    # Visualization of waveform and FFT results
    plt.figure(figsize=(12, 6))

    # Plot the waveform in the time domain
    plt.subplot(2, 1, 1)
    plt.plot(time_tdrift, random_waveform[tp0_value:peak])
    plt.title("Random Waveform in Time Domain")
    plt.xlabel("Time (µs)")
    plt.ylabel("Amplitude")

    # Plot the magnitude of the waveform in the frequency domain
    plt.subplot(2, 1, 2)
    plt.plot(frq_tdrift[:len(frq_tdrift) // 4], np.abs(fft_tdrift)[:len(frq_tdrift) // 4])
    plt.title("Waveform in Frequency Domain")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Magnitude")

    # Save the plots as a PNG file
    plt.tight_layout()
    plt.savefig("tdrift.png", format="png", dpi=300)
    print("Saved graph as fourier_lfpr.png")

    # Calculate and print LFPR
    print(f"Low Frequency Power Ratio of the graph: {lfpr(fft_tdrift)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process waveform data and visualize Fourier Transform results.")
    parser.add_argument('--input', type=str, required=True, help="Path to the input data file (HDF5)")
    
    args = parser.parse_args()
    main(args.input)
