import numpy as np
import matplotlib.pyplot as plt


plt.rcParams["axes.labelsize"] = 17
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

periods = {
	"0870":1.6518538,
	"0625":3.7503413
}
colors = {
	"0870":"#006400",
	"0625":"#dc143d"
}

fig = plt.figure(figsize=(13,6))
ax = [
	plt.subplot(121),
	plt.subplot(122, projection='polar')
]
ax02 = ax[0].twiny()

plt.sca(ax[0])
plt.xlabel(r"angle $\psi = 2\pi\phi$ ")
plt.xticks(np.linspace(0,1,9),[f"{s}°" for s in np.linspace(0,360,9,dtype=int)])
plt.xlim(0,1)
plt.ylabel("radius $ = I-I_{min}$")
plt.ylim(1,0)

plt.sca(ax02)
plt.xlabel("phase $\phi$")

plt.sca(ax[1])
plt.ylim(0,1.1)
plt.yticks([0.4,0.8,1])
plt.grid(False)

for code,P in periods.items():
	t,mag,err = np.loadtxt(f"./code/theory/OGLE-LMC-CEP-{code}.dat").T
	mag -= np.min(mag)
	mag = mag/np.max(mag)
	f = 1/P
	ephemeris = t[np.argsort(mag)[1]]
	phase = np.mod((t-ephemeris)*f,1)
	angles = phase*(2*np.pi)
	F = mag*np.exp(2j*np.pi*f*(t-ephemeris))
	argmax = mag.argsort()[-3]
	
	plt.sca(ax[0])
	plt.scatter(phase,mag,s=5,color=colors[code])
	plt.plot([phase[argmax]]*2,[0,mag[argmax]],color=colors[code],alpha=0.5)
	
	plt.sca(ax[1])
	plt.scatter(angles,mag,s=5,color=colors[code])
	plt.scatter(np.angle(F.mean()),abs(F.mean()),color=colors[code],marker="*")
	plt.plot([angles[argmax]]*2,[0,mag[argmax]],color=colors[code],alpha=0.5)
	
# solid sinusoid

phase = np.linspace(0,1,500)
angles = phase*2*np.pi
mag = np.sin(angles/2)
F = mag*np.exp(2j*np.pi*phase)
plt.sca(ax[0])
plt.plot(phase,mag,c='k',alpha=0.3,zorder=-10)
plt.sca(ax[1])
plt.plot(angles,mag,c='k',alpha=0.3)
plt.scatter(np.angle(F.mean()),abs(F.mean()),color="k",alpha=0.4,marker="*")


plt.tight_layout()
plt.savefig("./text/img/complex_phase.pdf")