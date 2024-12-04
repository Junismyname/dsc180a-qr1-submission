import pandas as pd
import numpy as np
import h5py
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import argparse

from parameter_functions.tdrift import tdrift
from parameter_functions.rea import rea
from parameter_functions.dcr import find_dcr
from parameter_functions.peakandtailslope import extract_peak_and_tail_slope
from parameter_functions.current_amplitude import max_amplitude
from parameter_functions.fourier_lfpr import normalized_fourier, lfpr
from parameter_functions.lq80 import LQ80
from parameter_functions.agr import area_growth_rate
from parameter_functions.inflection import inflection_points
from parameter_functions.rising_edge import rising_edge_slope

def main(input_file):

    # Pre-defined variables
    windown_size = 101
    poly_order = 3

    # Specify the directory
    data_dir = "src/data/"
    file_path = data_dir + input_file

    results = []  # Initialize results for this file
    with h5py.File(file_path, 'r') as f:
        for wave_idx in range(f['raw_waveform'].shape[0]):
            # Extract waveform data
            waveform = f['raw_waveform'][wave_idx]
            tp0 = f['tp0'][wave_idx]
            id = f['id'][wave_idx]

            # Perform parameter extraction
            tdriftVal = tdrift(waveform, tp0)  # [99.9%, 50%, 10%]
            reaVal = rea(waveform, tp0)
            dcrVal = find_dcr(waveform)
            peakandtailVal = extract_peak_and_tail_slope(waveform)
            max_amp = max_amplitude(waveform)
            fft_tdrift = normalized_fourier(waveform, tp0)[0]
            lfprVal = lfpr(fft_tdrift)
            lq80 = LQ80(waveform, tp0)
            agr = area_growth_rate(waveform)
            inflectionpts = inflection_points(waveform, tp0)
            res = rising_edge_slope(waveform, tp0)

            # Append results for the current waveform
            results.append({
                'id': id,
                'tdrift': tdriftVal[0],
                'tdrift50': tdriftVal[1],
                'tdrift10': tdriftVal[2],
                'rea': reaVal,
                'dcr': dcrVal,
                'peakindex': peakandtailVal[0],
                'peakvalue': peakandtailVal[1],
                'tailslope': peakandtailVal[2],
                'currentamp': max_amp,
                'lfpr': lfprVal,
                'lq80': lq80,
                'areagrowthrate': agr,
                'inflection_points': inflectionpts,
                'risingedgeslope': res,
            })

    # Convert results to DataFrame
    df = pd.DataFrame(results)
    print("First 5 rows of features")
    print(df.head(5))
    output_filename = f"results_{input_file.replace('.hdf5', '')}.csv"
    df.to_csv("src/data/"+output_filename)
    print("File downloaded as "+output_filename+" under /data/")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract features to csv file")
    parser.add_argument('--input', type=str, required=True, help="Path to the input data file (CSV)")
    
    args = parser.parse_args()
    main(args.input)

    


