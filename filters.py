import scipy.signal as sps


def HighpassFilter(arecs, fs):
    filter_stop_freq = 200  # Hz
    filter_pass_freq = 400  # Hz
    filter_order = 1001
    #
    # High-pass filter
    nyquist_rate = fs / 2.
    desired = (0, 0, 1, 1)
    bands = (0, filter_stop_freq, filter_pass_freq, nyquist_rate)
    filter_coefs = sps.firls(filter_order, bands, desired, nyq=nyquist_rate)

    # Apply high-pass filter on all 16 channels
    farecs = arecs
    for ii in range(0,16):
       print(ii)
       farec = sps.filtfilt(filter_coefs, [1], arecs[:,ii])
       farecs[:,ii] = farec[:]
    return farecs

