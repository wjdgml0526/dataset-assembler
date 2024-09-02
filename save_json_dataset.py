'''
Aggregates individual sample files into a unified dataset by applying a given function to each file in a directory.

Parameters:
- base_dir (str): The base directory to search for files.
- file_extension (str): The file extension to filter files by.
- processes (int): The number of parallel processes to use.
- save_path (str): The path where the aggregated dataset will be saved.
- process_function (callable): A function that processes a list of file paths and returns the processed data for each sample.

Returns:
It writes the aggregated dataset to a JSON file specified by `save_path`.
'''

import os
import multiprocessing as mp
import json

def save_dataset(base_dir, file_extension, processes, save_path, process_function):
    file_paths = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                file_paths.append(file_path)
    
    def chunkify(lst, n):
        avg = len(lst) // n
        chunks = []
        last = 0
        for i in range(n):
            next_last = last + avg + (1 if i < len(lst) % n else 0)
            chunks.append(lst[last:next_last])
            last = next_last
        return chunks
    
    chunks = chunkify(file_paths, processes)
    
    with mp.Pool(processes) as pool:
        results = pool.map(process_function, chunks)
    
    merged_results = [item for sublist in results for item in sublist]
    
    with open(save_path, 'w') as f:
        json.dump(merged_results, f, ensure_ascii = False, indent = 4)