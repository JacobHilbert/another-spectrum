import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import argsort

plt.rcParams["axes.labelsize"] = 17
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

code = "0625"
P = 3.7503413
t,mag,err = np.loadtxt(f"./code/theory/OGLE-LMC-CEP-{code}.dat").T
f = 1/P
freqs = [f,f*1.0003,f*(1-.002)]
ephemeris = t[np.argmin(mag)]

phases = [np.mod((t-ephemeris)*fi,1) for fi in freqs]

fig,ax = plt.subplots(ncols=3,figsize=(13,4),sharey=True)

xbins = np.linspace(0,1,30)
ybins = np.linspace(mag.min(),mag.max(),30)
for i in range(3):
	plt.sca(ax[i])
	plt.xlim(0,1.1)
	plt.xticks(np.linspace(0,1,5))
	plt.hist2d(phases[i],mag,(xbins,ybins),cmap='binary')
	if i == 0:
		plt.ylim(np.flip(plt.gca().get_ylim()))
		plt.ylabel("I")
	plt.title(fr"phase $\phi(\nu={freqs[i]:.5f})$")

plt.tight_layout()
plt.savefig(f"./text/img/offhist2d.pdf")