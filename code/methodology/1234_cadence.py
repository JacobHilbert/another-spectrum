import matplotlib.pyplot as plt
import numpy as np


plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

t,mag,err = np.loadtxt("../data/ogle4/OCVS/lmc/cep/phot/I/OGLE-LMC-CEP-1234.dat",unpack=True)
dist = np.mod(np.diff(t)+0.5,1)-0.5
plt.hist(24*dist,np.arange(-5,12,0.5),color='k');
plt.xlabel("Hour difference between consecutive measurements")
plt.ylabel("Measurements")
plt.title("OGLE-LMC-CEP-1234")


plt.savefig("./text/img/1234_cadence.pdf")