import numpy as np
import matplotlib.pyplot as plt

#plt.rcParams["figure.dpi"] = 200
plt.rcParams["axes.labelsize"] = 17
plt.rcParams["legend.fontsize"] = 14

path_prefix = "./code/introduction/"


plt.figure(figsize=(10,4))

X,Y = np.loadtxt(path_prefix+"eta_aquilae.tsv").T
P = 7.176641 # days
X = np.concatenate((X*P,(X+1)*P,(X+2)*P))
X -= X.min()
Y = np.concatenate((Y,Y,Y))

plt.plot(X, Y ,'-ok',label=r"$\eta$ Aquilæ")
plt.ylim([4.4,3.4])
plt.xlabel("days")
plt.ylabel("V magnitude")


X,Y = np.loadtxt(path_prefix+"delta_cephei.tsv").T
P = 5.366249 # days
X = np.concatenate((X*P,(X+1)*P,(X+2)*P,(X+3)*P))
X -= X.min()
Y = np.concatenate((Y,Y,Y,Y))

plt.plot(X,Y,marker="v",color='gray',markerfacecolor="white",label=r"$\delta$ Cephei")
plt.ylim([4.4,3.4])
plt.xlabel("days")
plt.ylabel("V")
plt.xlim([0,20])

plt.legend(loc=4)
plt.tight_layout()
#plt.show()
plt.savefig("./text/img/eta_aquilae_delta_cephei_light_curves.pdf")

