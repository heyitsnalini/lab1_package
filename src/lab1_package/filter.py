import numpy as np
import matplotlib.pyplot as plt
from numpy import log10

def fourier_filtering_draft(data, LO, RF, ylim1, ylim2):
    vspec = np.fft.fft(data)
    new_vspec = np.empty(len(vspec), dtype=np.complex128)

    np.copyto(new_vspec, vspec, casting='same_kind')

    for i in np.arange(len(vspec)):
        if ((np.abs(vspec[i]) > LO + RF + 10) and (np.abs(vspec[i]) < LO + RF - 10)):
            print(vspec[i])
            new_vspec[i] = 0
    
    new_data = np.fft.ifft(new_vspec)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize = (20,20))

    ax1.plot(np.arange(len(data)), data)
    ax2.plot(np.arange(len(vspec))-1000, np.real(vspec))
    ax2.plot(np.arange(len(vspec))-1000, np.imag(vspec))
    ax3.plot(np.arange(len(new_data)),new_data)
    ax4.plot(np.arange(len(new_vspec))-1000, np.real(new_vspec))
    ax4.plot(np.arange(len(new_vspec))-1000, np.imag(new_vspec))
    
    ax1.set_xlim(500,2000)
    ax1.set_ylim(-ylim1,ylim1)
    ax2.set_xlim(-1000,1000)
    ax2.set_ylim(-ylim2, ylim2)
    ax3.set_xlim(500, 2000)
    ax3.set_ylim(-ylim1,ylim1)
    ax4.set_xlim(-1000,1000)
    ax4.set_ylim(-ylim2, ylim2)

    ax1.set_title("Unfiltered Waveform")
    ax2.set_title("Unfiltered Voltage Spectrum")
    ax3.set_title("Filtered Waveform")
    ax4.set_title("Filtered Voltage Spectrum")

    plt.show()

