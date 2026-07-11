# fft and dft runtime comparison 

import numpy as np
import time 
from scipy import linalg

n = [16, 64, 128, 256, 1024, 2048]

total_dft_time = 0 
total_fft_time = 0

for k in n:
    signal = np.random.rand(k, k)
    
    s_time_dft = time.time()
    w = linalg.dft(k)
    x = w @ signal
    e_time_dft = (time.time() - s_time_dft)*1e3
    total_dft_time += e_time_dft
    
    s_time_fft = time.time()
    np.fft.fft(signal)
    e_time_fft = (time.time() - s_time_fft)*1e3
    total_fft_time += e_time_fft
    
    print(f"Size: {k}, DFT Runtime: {e_time_dft} ms, FFT Runtime: {e_time_fft} ms\n")

p_increase = np.round(((1-(total_fft_time/total_dft_time))*100), 2)
print(f"FFT was {p_increase}% faster")