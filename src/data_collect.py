#import statements
import numpy as np
import ugradio

#We used two scripts to collect data in our lab, do_something.py for most of our data, and mixerdata.py for the mixer data
#I've copied the contents of those scripts into the following functions and cleaned them up

def mixerdata(RF, LO, fir_on, power, mixertype, real_or_imag, section):
    '''
    For getting data from mixers specifically

    Args:
    RF, LO encode the frequency of the RF and LO signals (we used strings but in retrospect should have used numbers for analysis)
    fir_on is a boolean indicating whether the FIR filters are on - True to use default settings and False to override FIR coefficients
    power is the amplitude of the inputs
    mixertype should be a string, either saying SSB or DSB
    real_or_imag indicates if you are capturing the real or imaginary output (ie I or Q)
    section is a string encoding which section of the lab this is for (added for 7.3.1, 7.3.2 and 7.3.3 only)

    Outcome: saves data as a series of npz files with different sampling rates and important information stored in both the file
    name and metadata
    '''

    sample_rates = np.arange(1e6,1e7,2e5)

    for sampling in sample_rates:
    
        if fir_on:
            test_sdr = ugradio.sdr.SDR(direct = False,sample_rate = sampling, center_freq =25e6)
        else:
            test_sdr = ugradio.sdr.SDR(direct = False,sample_rate = sampling, fir_coeffs = 
                                   np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]))
    
    
        test_data = test_sdr.capture_data(nblocks = 2)[1]
    
        np.savez(f'{section}_{real_or_imag}__{(sampling/1e6)}e6_{RF}_{LO}', data = test_data, RF_freq = RF, LO_freq = LO, mixer = mixertype, sampled_at = sampling, FIR = fir_on, power=power)
        test_sdr.__del__()
    

def generaldata(freq, fir_on, voltage, spacing):
    '''
    For getting data from one output - also used and slightly modified for our frequency resolution section

    Args:
    freq encodes the frequency of the generated signal
    fir_on is a boolean indicating whether the FIR filters are on - True to use default settings and False to override FIR coefficients
    voltage is the amplitude of the input
    spacing is an argument that was added just for the frequency resolution tests which encodes the difference between the 
    two inputs being combined

    Outcome: saves data as a series of npz files with different sampling rates and important information stored in both the file
    name and metadata
    '''

    sample_rates = np.arange(1e6, 3.2e6, 2e5)
    for i in sample_rates:
        sampling = i
    
        if fir_on:
            test_sdr = ugradio.sdr.SDR(direct = True, sample_rate = sampling)
        else:
            test_sdr = ugradio.sdr.SDR(direct = True, sample_rate = sampling, fir_coeffs = 
                                   np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2047]))
    
        test_data = test_sdr.capture_data(nblocks = 2)[1]
    
        np.savez(f'{sampling/1e6}e6_{freq}', data = test_data, frequency = freq, sampled_at = sampling, FIR = fir_on, vpp =
             voltage, freq_diff = spacing)
        test_sdr.__del__()