import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.labelsize"] = 17
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

t,mag,err = np.loadtxt("./code/theory/OGLE-LMC-CEP-0870.dat").T
P = 1.6518538
f = 1/P
ephemeris = t[np.argmin(mag)]

ptp = np.ptp(mag)
mean = np.mean(mag)
t_space = np.linspace(t[1]-.5,t[9]+.5,500)

foo = lambda t_: mean-0.5*ptp*np.cos(2*np.pi*f*(t_-ephemeris))
std = (mag-foo(t)).std()

plt.figure(figsize=(8,5))

plt.scatter(t[:11],mag[:11],c='k')
plt.errorbar(t[:11],mag[:11],yerr=err[:11],fmt=" ",capsize=2,c='k',alpha=.5)
plt.plot(t[:11],mag[:11],c='r')
plt.fill_between(t_space,foo(t_space)-std,foo(t_space)+std,color='k',alpha=0.2)
plt.ylim(np.flip(plt.gca().get_ylim()))
plt.xlim(t_space.min(),t_space.max())

plt.xlabel("$\\mathrm{RJD} = \\mathrm{HJD}-2.45\\times 10^6$")
plt.ylabel("I")

plt.title("OGLE-LMC-CEP-0870",fontsize=17)

plt.tight_layout()

plt.savefig("./text/img/interpolation_failure.pdf")