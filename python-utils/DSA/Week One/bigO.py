""""
 Create a Python script that analyzes the time complexity of different sorting algorithms by measuring execution time for various input sizes.
 
 steps:
 1. Detect start time
 2. Detect end time
 3. Calculate the difference between start time and endtime
"""

import time

def measure_time(func, arr):
    start_time = time.time()
    func(arr.copy())
    end_time = time.time()
    return end_time - start_time

