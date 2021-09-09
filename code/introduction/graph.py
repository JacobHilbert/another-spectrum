import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

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

plt.close()


# Leavitt

Xmax,Ymax = np.loadtxt(path_prefix+"leavitt_max.tsv").T
regmax = linregress(Xmax,Ymax)
Xmin,Ymin = np.loadtxt(path_prefix+"leavitt_min.tsv").T
regmin = linregress(Xmin,Ymin)

plt.xlim([0,2.2])
plt.ylim([16.5,11])
xticks = np.arange(0,2.3,0.2)
plt.xticks(xticks)
yticks = np.arange(11,16.5,0.5)
ylabels = [str(int(i)) if round(i)==i else "" for i in yticks]
plt.yticks(yticks,ylabels)
plt.xlabel("Log P")
plt.ylabel("Photographic magnitude")
plt.grid(True)

plt.plot(Xmax,Ymax,'-ok')
plt.plot(Xmin,Ymin,'-ok')
plt.plot(xticks,regmax.slope * xticks + regmax.intercept,c="k",linestyle=(0,(5,5)))
plt.plot(xticks,regmin.slope * xticks + regmin.intercept,c="k",linestyle=(0,(5,5)))

plt.savefig("./text/img/leavitt.pdf")