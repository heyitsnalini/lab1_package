import numpy as np
import matplotlib.pyplot as plt
from numpy import log10

def plot_vpw(data,ylim1, xlim1, ylim2, xlim2, ylim3):
    '''
    Plots the voltage spectrum (real and imaginary), power spectrum, and waveform 
    '''
    vspec = np.fft.fft(data)
    pspec = np.abs(vspec)**2

    plt.style.use('default')
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (30,10))
    
    ax1.plot(np.arange(len(vspec))-1000, np.real(vspec), color = 'k', label = "Real Part")
    ax1.plot(np.arange(len(vspec))-1000, np.imag(vspec), color = 'cornflowerblue', label ="Imaginary Part")
    ax2.plot(np.arange(len(pspec))-1000, pspec, color = 'k')
    ax3.plot(np.arange(len(data)), data, color = 'k')

    ax1.set_xlim(-xlim1,xlim1)
    ax1.set_ylim(-ylim1,ylim1)
    ax2.set_xlim(-xlim2,xlim2)
    ax2.set_ylim(0,ylim2)
    ax3.set_xlim(500, 600)
    ax3.set_ylim(-ylim3,ylim3)

    ax1.set_title("Voltage Spectrum", fontsize=20)
    ax2.set_title("Power Spectrum", fontsize=20)
    ax3.set_title("Waveform", fontsize=20)

    ax1.legend()

    plt.show()