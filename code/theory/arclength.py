import numpy as np
import matplotlib.pyplot as plt

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
Fs = [mag*np.exp(2j*np.pi*phase) for phase in phases]
argsort = [p.argsort() for p in phases]

fig,ax = plt.subplots(ncols=3,figsize=(13,4),sharey=True)

for i in range(3):
	plt.sca(ax[i])
	plt.xlim(0,1)
	plt.plot(phases[i][argsort[i]],mag[argsort[i]],c='r',alpha=0.6)
	plt.scatter(phases[i][argsort[i]],mag[argsort[i]],color='k',s=2)
	if i == 0:
		plt.ylim(np.flip(plt.gca().get_ylim()))
		plt.ylabel("I")
	plt.title(fr"phase $\phi(\nu={freqs[i]:.5f})$")


plt.tight_layout()
plt.savefig(f"./text/img/offphase.pdf")