import numpy as np
import matplotlib.pyplot as plt
import h5py
import argparse

def main(input_file):
    # Function for tdrift extraction
    def tdrift(waveform, tp0):
        peak = np.argmax(waveform)
        tdrift = (peak-tp0) * 0.999
        tdrift50 = (peak-tp0) * 0.5
        tdrift10 = (peak-tp0) * 0.1
        return tdrift, tdrift50, tdrift10
    with h5py.File(input_file, 'r') as file:
        # Load the raw waveforms
        raw_waveform = np.array(file["raw_waveform"])
    
        # Load other labels
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
    
        # Get the random waveform
        random_waveform = raw_waveform[random_index]
    
        # Access the labels for the selected index
        energy_value = energy_label[random_index]
        psd_low_avse_value = psd_label_low_avse[random_index]
        psd_high_avse_value = psd_label_high_avse[random_index]
        psd_dcr_value = psd_label_dcr[random_index]
        psd_lq_value = psd_label_lq[random_index]
        tp0_value = tp0[random_index]
        detector_value = detector[random_index]
        run_number_value = run_number[random_index]
        id_value = id[random_index]
    
    # Extract parameter
    tdrift, tdrift50, tdrift10 = tdrift(random_waveform, tp0_value)
    
    # Visualization
    plt.figure(figsize=(10, 5))
    plt.plot(random_waveform)
    plt.title(f'Random Raw Waveform (Index: {random_index})')
    plt.xlabel('Time Index (μs)')
    plt.ylabel('ADC Counts')
    
    textstr = (
        f"Energy Label: {energy_value}\n"
        f"PSD Label Low Avse: {psd_low_avse_value}\n"
        f"PSD Label High Avse: {psd_high_avse_value}\n"
        f"PSD Label DCR: {psd_dcr_value}\n"
        f"PSD Label LQ: {psd_lq_value}\n"
        f"Start of Rising Edge: {tp0_value}\n"
        f"Detector: {detector_value}\n"
        f"Run Number: {run_number_value}\n"
        f"ID: {id_value}"
    )
    plt.gcf().text(0.45, 0.2, textstr, fontsize=10)
    plt.axvline(x=750, color='purple', linestyle='--', label='Region Start (750 μs)')
    plt.axvline(x=1250, color='purple', linestyle='--', label='Region End (1250 μs)')
    plt.axvline(x=tp0_value, color='orange', linestyle='--', label='Rising Edge (tp0)')
    plt.plot(int(tdrift50+tp0_value), random_waveform[int(tdrift50+tp0_value)], 'ro', label='tdrift50 Point')
    plt.plot(int(tdrift10+tp0_value), random_waveform[int(tdrift10+tp0_value)], 'go', label='tdrift10 Point')
    plt.plot(int(tdrift+tp0_value), random_waveform[int(tdrift+tp0_value)], 'bo', label='tdrift Point')
    
    plt.legend()
    plt.savefig("tdrift.png", format="png", dpi=300)
    print("Saved graph as tdrift.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute LFPR from waveform data using Fourier Transform.")
    parser.add_argument('--input', type=str, required=True, help="Path to the input data file (CSV)")
    
    args = parser.parse_args()
    main(args.input)







