# Sample Aggregation

This repository contains a Python script for aggregating and processing individual sample files into a unified dataset. The script applies a specified processing function to each file into a single JSON file.
<img width="557" alt="스크린샷 2024-09-02 오전 11 34 43" src="https://github.com/user-attachments/assets/29b1c308-ddbe-4601-acd1-7d6f724b4257">  
into:  
<img width="721" alt="스크린샷 2024-09-02 오전 11 36 14" src="https://github.com/user-attachments/assets/280a4d0d-2189-485a-b500-5b506f73b127">


## Overview

The primary function of this project is to handle a collection of sample files, each representing an individual data point. The script processes these files in parallel to efficiently create a single dataset file.

## Usage

1. **Prepare your environment**:
   - Ensure you have Python 3.x installed.
   - This project requires the following Python standard libraries, which are included with Python:
     - json
     - os
     - multiprocessing

2. **Run the script**:
   - Review the provided `example.ipynb` notebook for detailed instructions on how to use the `save_json_dataset.py` script.
