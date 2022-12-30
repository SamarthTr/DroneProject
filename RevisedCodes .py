#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This block creates a spectrum for the specified centre frequency
get_ipython().system('pip install pyrtlsdr')


from pylab import *
from rtlsdr import *

sdr = RtlSdr()

sdr.sample_rate = 1.2e6
sdr.center_freq = 92.7e6
sdr.gain = 4

samples = sdr.read_samples(256*1024)
sdr.close()

psd(samples, NFFT=1024, Fs=sdr.sample_rate, Fc=sdr.center_freq)
xlabel('Frequency (MHz)')
ylabel('Relative power (dB)')
show()

x = [ele.real for ele in samples]
y = [ele.imag for ele in samples]
  
plt.scatter(x, y)
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()

#gives warning:
#Found Rafael Micro R820T tuner
#[R82XX] PLL not locked!


# In[ ]:


#This block gives multiple plots at 1 second time gap
from pylab import *
from rtlsdr import *
from time import sleep    
sdr = RtlSdr()    
sdr.sample_rate = 2.4e6
sdr.center_freq = 93.5e6
sdr.gain = 50    
while 10: # run until interrupted
    samples = sdr.read_samples(256*1024)
    psd(samples.real, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
    xlabel('Frequency (MHz)')
    ylabel('Relative power (dB)')
    show()
    sleep(1) # sleep for 1s
    clf()
sdr.close()


# In[ ]:


from pylab import *
from rtlsdr import *
import numpy
import matplotlib 

sdr = RtlSdr()

# configure device
sdr.sample_rate = 1.2e6
sdr.center_freq = 92.7e6
sdr.gain = 4

samples = sdr.read_samples(256*1024)
sdr.close()

# use matplotlib to estimate and plot the PSD
psd(samples, NFFT=1024, Fs=sdr.sample_rate, Fc=sdr.center_freq)
xlabel('Frequency (MHz)')
ylabel('Relative power (dB)')
show()


# In[ ]:


#This block creates a spectrogram for the predefined centre frequency
from pylab import *
from rtlsdr import *
import numpy


fft_size = 1024
num_rows = int(np.floor(len(samples)/fft_size))
spectrogram = np.zeros((num_rows, fft_size))
for i in range(num_rows):
    spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(samples[i*fft_size:(i+1)*fft_size])))**2)

plt.imshow(spectrogram, aspect='auto', extent = [0, sdr.sample_rate/2/1e6, 0, len(samples)/sdr.sample_rate])
plt.xlabel("Frequency [MHz]")
plt.ylabel("Time [s]")
plt.show()


# In[ ]:


#This block scans the spectrum and gives a spectrum
from pylab import *
from rtlsdr import *
import numpy
import matplotlib 

for j in range (1,2):
    for i in range(88,108):
        sdr = RtlSdr()
        # configure device
        sdr.sample_rate = 1.2e6
        sdr.center_freq = i*1e6
        sdr.gain = 4
        samples = sdr.read_samples(256*1024)
        sdr.close()
        # use matplotlib to estimate and plot the PSD
        psd(samples, NFFT=1024, Fs=sdr.sample_rate, Fc=sdr.center_freq)

xlabel('Frequency (MHz)')
ylabel('Relative power (dB)')
show()

