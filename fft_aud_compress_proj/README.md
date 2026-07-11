"fft_audio_compress.ipynb" is a notebook which loads a .wav file, performs the Fast Fourier Transform on it, filters it for a psuedo-compression at two levels, performs the Inverse Fast Fourier Transform, and returns two listenable .wav files.
"runtime_compare.py" compares the runtime of the Fast Fourier Transform and the Discrete Fourier Transform at multiple sizes.

<h3>FFT Audio Compression</h3>

First we import our libraries, read our .wav with SciPy, normalize the audio, and plot the waveform with MatPlotLib.
<img width="1226" height="475" alt="image" src="https://github.com/user-attachments/assets/d5c396d9-c476-49da-b162-23cb157753ca" />

Next, we perform the FFT on our audio, take its magnitudes, and plot it in the frequency spectrum. 
<img width="698" height="549" alt="image" src="https://github.com/user-attachments/assets/9aa9b286-d9e3-40ef-89ea-0dc8384c621f" />

The next two cells we find the top 5% and 25% loudest frequencies and set all frequencies below that threshold to 0.

The next two cells we bring our 5% and 25% filtered audios back to waveform with the IFFT, renormalize, put back into mono audio, convert and export them as .wav, and plot our new filtered/compressed waveforms.
<img width="1234" height="475" alt="image" src="https://github.com/user-attachments/assets/1de46a75-8369-49cb-a0af-1f5aace508a5" />
<img width="1228" height="469" alt="image" src="https://github.com/user-attachments/assets/11ecbea3-df5d-45d7-8ac0-aea4d3670675" />

<h3>Runtime Comparison</h3>
First we import our libraries, build a list of base 2 integers to prevent the FFT from padding, and set up two baseline variables for the runtime of each transformation.
Next, we take a loop which iterates through the list of base 2 integers and builds a random matrix of of each size. Then with the same matrix it performs the DFT and FFT and logs both of their runtimes in miliseconds.
Lastly, we calculate the overall runtime speed increase the FFT had over the DFT in percentage. 
Here is an example output:
<img width="760" height="228" alt="image" src="https://github.com/user-attachments/assets/d0046221-7162-4021-b6c1-d34ba041d1a8" />
