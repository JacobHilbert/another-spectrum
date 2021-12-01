import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.labelsize"] = 17
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

code = "0625"
color = "#dc143d"
starcolor = 'k'
P = 3.7503413
t,mag,err = np.loadtxt(f"./code/theory/OGLE-LMC-CEP-{code}.dat").T
mag -= np.min(mag)
mag = mag/np.max(mag)
f = 1/P
freqs = [f,f*1.0003,f*(1-.002)]
ephemeris = t[np.argmin(mag)]

phases = [np.mod((t-ephemeris)*fi,1) for fi in freqs]
Fs = [mag*np.exp(2j*np.pi*phase) for phase in phases]

fig = plt.figure(figsize=(15,8))
ax = np.array([
	[
		plt.subplot(3,3,1),
		plt.subplot(3,3,2),
		plt.subplot(3,3,3),
	],[
		plt.subplot(3,3,(4,7), projection='polar'),
		plt.subplot(3,3,(5,8), projection='polar'),
		plt.subplot(3,3,(6,9), projection='polar'),
	]
])

for i in range(3):
	ax[0,i].xaxis.set_ticks_position("top")
	plt.sca(ax[0,i])
	plt.xlim(0,1)
	plt.ylim(1,0)
	plt.yticks([])
	plt.title(fr"phase $\phi(\nu={freqs[i]:.5f})$")
	
	plt.scatter(phases[i],mag,color=color,s=2)
	if i == 0:
		plt.yticks(np.linspace(0,1,5))
	
	
	plt.sca(ax[1,i])
	plt.scatter(np.angle(Fs[i]),abs(Fs[i]),color=color,s=3)
	plt.plot([np.angle(Fs[i].mean())]*2,[0,abs(Fs[i].mean())],c=starcolor)
	plt.scatter(np.angle(Fs[i].mean()),abs(Fs[i].mean()),c=starcolor,marker="*",s=100,zorder=100)
	
	plt.yticks([])
	plt.grid(False)

plt.tight_layout()
plt.savefig(f"./text/img/complex_phase_off.pdf")