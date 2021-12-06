import os
import toolz
import json
import numpy as np
import matplotlib.pyplot as plt
from numba import njit
from scipy.signal import find_peaks
from glob import glob
from tqdm import tqdm

@njit("f8[::1](f8[::1],f8[::1],f8,f8,f8)",fastmath=True)
def fourier_incremental(t_arg,m_arg,f_ini,f_end,df):
    dF = np.exp(-2j*np.pi*t_arg*df)
    F = np.zeros_like(np.arange(f_ini,f_end,df))
    curl = m_arg * np.exp(-2j*np.pi*t_arg*f_ini)
    F[0] = np.abs(sum(curl))
    for i in range(1,len(F)):
        curl = curl*dF
        F[i] = np.abs(sum(curl))**2
    return F

# LMC

f_min, f_max, df = 0.001,4.7,1e-5 # 5e-5
fs = np.arange(f_min,f_max,df)


fnames = glob("ogle4/OCVS/lmc/cep/phot/I/*.dat")
fnames.sort()

results = {}
peaks = {}
for fname in tqdm(fnames):
    # import
    t,I,err = np.loadtxt(fname,unpack=True)
    n = len(t)
    I_mean = I.mean()
    dI_stat = 1/np.sqrt(sum(1/err**2)) # statistical error
    dI_syst = np.std(np.mean(np.random.choice(I,(n,n)),axis=1)) # systematic error
    code = os.path.basename(fname).split(".")[0]
    # prepare
    t = np.ascontiguousarray(t)
    m = np.ascontiguousarray(I) - I_mean
    F = fourier_incremental(t,m,f_min,f_max,df)
    F /= F.max()
    # process
    freq = fs[F.argmax()]
    peaks_index,props = find_peaks(F,height=0.5,width=4)
    props['freqs'] = fs[peaks_index]
    sigma_freq = df*props['widths'][props['peak_heights'].argmax()]/2
    # export
    results[code] = {
        'n':n,
        'I_mean':I_mean,
        'sigma_I_mean': np.sqrt(dI_stat**2+dI_syst**2),
        'freq':freq,
        'sigma_freq':sigma_freq,
    }
    peaks[code] = toolz.valmap(np.ndarray.tolist, props)

with open("lmc_results.json","w") as file:
    json.dump(results,file)
with open("lmc_peaks.json","w") as file:
    json.dump(peaks,file)

# SMC

fnames = glob("ogle4/OCVS/smc/cep/phot/I/*.dat")
fnames.sort()

results = {}
peaks = {}
for fname in tqdm(fnames):
    # import
    t,I,err = np.loadtxt(fname,unpack=True)
    n = len(t)
    I_mean = I.mean()
    dI_stat = 1/np.sqrt(sum(1/err**2)) # statistical error
    dI_syst = np.std(np.mean(np.random.choice(I,(n,n)),axis=1)) # systematic error
    code = os.path.basename(fname).split(".")[0]
    # prepare
    t = np.ascontiguousarray(t)
    m = np.ascontiguousarray(I) - I_mean
    F = fourier_incremental(t,m,f_min,f_max,df)
    F /= F.max()
    # process
    freq = fs[F.argmax()]
    peaks_index,props = find_peaks(F,height=0.5,width=4)
    props['freqs'] = fs[peaks_index]
    sigma_freq = df*props['widths'][props['peak_heights'].argmax()]/2
    # export
    results[code] = {
        'n':n,
        'I_mean':I_mean,
        'sigma_I_mean': np.sqrt(dI_stat**2+dI_syst**2),
        'freq':freq,
        'sigma_freq':sigma_freq,
    }
    peaks[code] = toolz.valmap(np.ndarray.tolist, props)

with open("smc_results.json","w") as file:
    json.dump(results,file)
with open("smc_peaks.json","w") as file:
    json.dump(peaks,file)
