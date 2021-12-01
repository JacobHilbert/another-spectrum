import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.labelsize"] = 17
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

periods = {
	"0870":1.6518538,
	"0625":3.7503413
}

for code,P in periods.items():
	
	t,mag,err = np.loadtxt(f"./code/theory/OGLE-LMC-CEP-{code}.dat").T
	f = 1/P
	ephemeris = t[np.argmin(mag)]
	phase = np.mod((t-ephemeris)*f,1)
	
	fig,ax = plt.subplots(ncols=2,figsize=(13,4),sharey=True)
	
	plt.sca(ax[0])
	
	plt.errorbar(t,mag,yerr=err,fmt=" ",capsize=2,c='k',alpha=.2)
	plt.scatter(t,mag,s=3,c='k')
	plt.ylim(np.flip(plt.gca().get_ylim()))
	plt.xlabel("$\\mathrm{RHJD} = \\mathrm{HJD}-2.45\\times 10^6$")
	plt.ylabel("I")
	
	plt.sca(ax[1])
	
	for i in [-1,0,1]:
		plt.errorbar(phase+i,mag,yerr=err,fmt=" ",capsize=2,c='k',alpha=.2)
		plt.scatter(phase+i,mag,s=.2,c='k')
	
	plt.xlabel("$\\phi=\\mathrm{mod}(\\mathrm{RJHD}-t_0,P)/P$")
	plt.xticks(np.arange(-0.5,1.75,0.25))
	plt.xlim(-0.5,1.5)
	
	plt.suptitle(f"OGLE-LMC-CEP-{code}",fontsize=17)
	
	plt.tight_layout()
	plt.savefig(f"./text/img/mag_phase_LMC_{code}.pdf")


