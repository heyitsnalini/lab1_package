import numpy as np
import matplotlib.pyplot as plt
from numpy import log10

def plotting_draft(data,ylim1,ylim2,ylim3):
    vspec = np.fft.fft(data)
    pspec = np.abs(vspec)**2
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (30,10))
    
    ax1.plot(np.arange(len(vspec))-1000, np.real(vspec))
    ax1.plot(np.arange(len(vspec))-1000, np.imag(vspec))
    ax2.plot(np.arange(len(pspec))-1000, pspec)
    ax3.plot(np.arange(len(data)), data)

    ax1.set_xlim(-1000,1000)
    ax1.set_ylim(-ylim1,ylim1)
    ax2.set_xlim(-1000,1000)
    ax2.set_ylim(0,ylim2)
    ax3.set_xlim(500, 600)
    ax3.set_ylim(-ylim3,ylim3)

    ax1.set_title("Voltage Spectrum")
    ax2.set_title("Power Spectrum")
    ax3.set_title("Waveform")

    plt.show()

def plotting_draft2(data,ylim1,ylim2,ylim3):
    vspec = np.fft.fft(data)
    pspec = np.abs(vspec)**2
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (30,10))
    
    ax1.plot(np.arange(len(vspec))-1000, np.real(vspec))
    ax1.plot(np.arange(len(vspec))-1000, np.imag(vspec))
    ax2.plot(np.arange(len(pspec))-1000, pspec)
    ax3.plot(np.arange(len(data)), data)

    ax1.set_xlim(-1000,1000)
    ax1.set_ylim(-ylim1,ylim1)
    ax2.set_xlim(-1000,1000)
    ax2.set_ylim(0,ylim2)
    ax3.set_xlim(500, 2000)
    ax3.set_ylim(-ylim3,ylim3)

    ax1.set_title("Voltage Spectrum")
    ax2.set_title("Power Spectrum")
    ax3.set_title("Waveform")

    plt.show()