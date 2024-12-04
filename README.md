# Majorana Neutrino Hunt
Capstone Project B10

Contributors:
- Matthew Segovia
- Jun Hwang
- Ryan Doh
- Haotian Zhu
- Ammie Xie
- Ketki Chakradeo
- Marco Sanchez
  
## Description

This project provides a reproducible framework for analyzing waveform data to distinguish between single-site and multi-site events using various signal processing and machine learning techniques. The main objectives are:

- Extracting features.
- Understanding the dataset.

---

## Prerequisites

### Installation Instructions
How to clone the repository:
``` bash
git clone https://github.com/Junismyname/dsc180a-qr1-submission.git
``` 

### Data Access and Storage

**Data Location**: You may download the data to see how the data is processed. It is located in https://drive.google.com/file/d/1eGyB6rB1uNR5zrQ4ZLIIjQen8gZz_Iks/view?usp=sharing. Ensure that the data is in `/src/data/`.
### Software Dependencies

- **Python Version**: Ensure Python 3.8+ is installed.
- **Package Requirements**: Use `requirements.txt` to install all necessary libraries. To install dependencies, run:
  
  ```bash
  pip install -r requirements.txt

## Features
This repository contains the files for all parameters functions that will be used to build and train machine learning models 

The parameters used in this investigation include:

- **Drift Time** (tdrift.py): The time taken from the initiation of charge generation to the collection at the detector's point contact at increments of 10%, 50% and 99.9%.

- **Late Charge** (lq80.py): The amount of energy being collected after 80% of the peak. 

- **Late Charge Slope** (Area Growth Rate (agr.py)): The integrated drift time of the charge collected after 80% of the waveform. 

- **Second derivative Inflection Points** (inflection.py): The amount of inflection points from 80% of our charge to the peak. 

- **Rising Edge Slope** (rising_edge.py): The slope of the charge that was recorded.

- **Rising Edge Asymmetry** (rea.py): This function measures how tilted in a direction the rising edge of the signal is.

- **Current Amplitude** (current_amplitude.py): The peak rate of charge collection, defined as I = dq/dt which means current amplitude is the derivative of charge.

- **Energy Peak** (peakandtailslope.py): The maximum analog-to-digital (ADC) count. The height of this peak correlates with the energy deposited by the particle in the detector.

- **Tail Slope** (peakandtailslope.py): The rate of charge collection over the length of the waveform’s tail. It indicates how quickly charge dissipates in the detector after the initial interaction.

- **Delayed Charge Recovery** (dcr.py): The rate of area growth in the tail slope region. This is measured by the area above the tail slope to the peak of the rise. 

- **Fourier Transform and Low Frequency Power Ratio** (fourier_lfpr.py): The Fourier Transform is a mathematical operation that transforms a time-domain signal into its frequency-domain representation. Low Frequency Power Ratio (LFPR) is used, quantifying how much of the signal’s energy is concentrated in the low-frequency threshold by the total power spectrum of the Fourier transformed waveform.  
---
## File Structure

```bash
dsc180a-qr1-submission/  
│  
├── data_exploration_junhwang.ipynb   # Main notebook for data exploration  
├── README.md                         # Project documentation  
├── requirements.txt                  # Required dependencies  
│  
├── src/                              # Source directory  
│   ├── data/                         # Contains raw data files  
│   ├── features_extracted/           # Stores CSV files of extracted features  
│   ├── parameter_functions/          # Python files for parameter extraction  
│   │   ├── agr.py                    # Area growth rate (AGR) calculation  
│   │   ├── current_amplitude.py      # Current amplitude calculations  
│   │   ├── dcr.py                    # Delayed charge recovery  
│   │   ├── fourier_lfpr.py           # Fourier transform and LFPR analysis  
│   │   ├── inflection.py             # Inflection point calculation  
│   │   ├── lq80.py                   # Late charge calculations  
│   │   ├── peakandtailslope.py       # Peak and tail slope calculations  
│   │   ├── rising_edge.py            # Rising edge slope calculation  
│   │   ├── rea.py                    # Rising edge asymmetry analysis  
│   │   ├── tdrift.py                 # Drift time calculations  
│   │  
│   ├── plots/                        # Generated plots for analysis  
│       ├── region_tdrift.png  
│       ├── rise_tdrift.png  
│       ├── rise80.png  
│       ├── time_waveform.png  
│       ├── time_waveform_region.png  
│   │  
│   └── master.py                     # Main script to execute feature extraction  
│  
└── .ipynb_checkpoints/               # Jupyter checkpoint files
```
## Running the Code  

### Running Feature Extraction with `master.py`

The `master.py` script is the main entry point for feature extraction. It orchestrates the application of various parameter functions to raw waveform data and saves the extracted features in a CSV file.

#### Steps to Use `master.py`:
1. **Ensure Input Data is Ready**:
   - Place the `.hdf5` input data file in the `/src/data/` directory.
       - You can use `MJD_Test_2.hdf5` data file downloaded from the Google Drive link above.

2. **Run the Script**:
   - Use the command below to execute the script:
     ```bash
     python src/master.py --input <filename.hdf5>
     ```
   - Replace `<filename.hdf5>` with the name of your input file.

3. **Output**:
   - The script extracts parameters such as drift times, current amplitude, late charge, Fourier LFPR, and more for each waveform in the input file.
   - Results are saved as a CSV file in the `/src/data/` directory, with the naming convention: `results_<input_filename>.csv`.

#### Parameters Extracted:
- Drift Time (10%, 50%, 99.9%)
- Rising Edge Slope
- Inflection Points
- Late Charge (LQ80)
- Fourier Low Frequency Power Ratio (LFPR)
- Current Amplitude
- Delayed Charge Recovery (DCR)
- Energy Peak and Tail Slope
- Rising Edge Asymmetry (REA)
- Area Growth Rate (AGR)

#### Example:
For an input file named `MJD_Test_2.hdf5`, the command:

```bash
python src/master.py --input MJD_Test_2.hdf5
```
will generate a file named `results_MJD_Test_2.hdf5` in the `/src/data/` directory.


### Data Exploration
1. File: data_exploration_junhwang.ipynb
2. Open the notebook in Jupyter to explore and prepare data.

## Further Reading
[Majorana Demonstrator Data Release Notes](https://arxiv.org/pdf/2308.10856)















