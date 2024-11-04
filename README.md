# Project Title

## Description

This project provides a reproducible framework for analyzing waveform data to distinguish between single-site and multi-site events using various signal processing and machine learning techniques. The main objectives are:

- Extracting drift time and defining energy regions.
- Computing the Low Frequency Power Ratio (LFPR) using Fourier Transform.

---

## Prerequisites

### Data Access and Storage

**Data Location**: You must download the data in order to run all the files. It is located in https://drive.google.com/file/d/1eGyB6rB1uNR5zrQ4ZLIIjQen8gZz_Iks/view?usp=sharing. Ensure that the data is in the same directory with all the other files.
### Software Dependencies

- **Python Version**: Ensure Python 3.8+ is installed.
- **Package Requirements**: Use `requirements.txt` to install all necessary libraries. To install dependencies, run:
  
  ```bash
  pip install -r requirements.txt

## Running the Code

### tdrift
1. File: tdrift.py
2. Run this command in terminal:
   ```bash
   python tdrift.py --input MJD_Test_2.hdf5
Graph plot of tdrift will be downloaded as tdrift.png.

### Fourier and LFPR
1. File: fourier_lfpr.py
2. Run this command in terminal:
   ```bash
   python fourier_lfpr.py --input MJD_Test_2.hdf5
Graph plot of tdrift will be downloaded as fourier_lfpr.png.

### Data Exploration
1. File: data_exploration_junhwang.ipynb
2. Open the notebook in Jupyter to explore and prepare data.


















