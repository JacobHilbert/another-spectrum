import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.dpi"] = 120
plt.rcParams["axes.labelsize"] = 17
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12


pd_options = dict(
	sep="\s+",
	usecols=[*range(7)],
	index_col=0,
	names=["ID","I","V","P","dP","t0","ptp"],
	na_values="-"
)
base = {}
files = {}
labels = {}
tables = {}
stats = {}

base["lmc"] = "../data/ogle4/OCVS/lmc/cep/"
files["lmc"] = ["cepF.dat","cep1O.dat","cep2O.dat",
		 "cepF1O.dat","cep1O2O.dat","cepF1O2O.dat",
		 "cep1O2O3O.dat","cep1O3O.dat","cep2O3O.dat"]

base["smc"] = "../data/ogle4/OCVS/smc/cep/"
files["smc"] = ["cepF.dat","cep1O.dat","cep2O.dat",
		 "cepF1O.dat","cep1O2O.dat","cep1O2O3O.dat"]


for cloud,basepath in base.items():
	labels[cloud] = [f[3:].split(".")[0] for f in files[cloud]]
	tables[cloud] = {
		label:pd.read_table(basepath+fname,**pd_options) for fname,label in zip(files[cloud],labels[cloud])
	}
	for label,table in tables[cloud].items():
		for phot in "IV":
			table.insert(len(table.columns),"n"+phot,np.nan)
			for index in table.index:
				try:
					with open(f"{basepath}phot/{phot}/{index}.dat","r") as file:
						table.at[index,"n"+phot] = file.read().count("\n")
				except FileNotFoundError:
					pass
	all_data = pd.concat(tables[cloud]).sort_index()
	tables[cloud]["total"] = all_data
	
	local_stats = {}
	for label,table in tables[cloud].items():
		local_stats[label] = {
			"n":len(table),
			"I":sum(~table["nI"].isna()),
			"I (only)":sum(~table["nI"].isna() & table["nV"].isna()),
			"V":sum(~table["nV"].isna()),
			"V (only)":sum(table["nI"].isna() & ~table["nV"].isna()),
			"both": sum(~table["nI"].isna() & ~table["nV"].isna()),
			"none": sum(table["nI"].isna() & table["nV"].isna())
		}
	stats[cloud] = pd.DataFrame.from_dict(local_stats,orient="index")
	print(cloud,"\n",stats[cloud].to_latex())

files["selected"] = [*reversed(["cepF.dat","cep1O.dat","cep2O.dat","cepF1O.dat","cep1O2O.dat"])]
labels["selected"] = [f[3:].split(".")[0] for f in files["selected"]]
# courtesy of https://learnui.design/tools/data-color-picker.html#divergent
colors = ["#00876c","#89bd73","#ffeb8a","#f59855","#d43d51"][::-1]

##################################################################################

hist_options = dict(stacked=True,bins=70,color=colors,label=labels["selected"])
total_hist_options = dict(bins=70,histtype="step",color='k',label="total")

fig,axes = plt.subplots(nrows=2,ncols=3,figsize=(14,7),sharey="row",sharex="col")

for i,cloud in enumerate(["lmc","smc"]):
	ax = axes[i]
	#
	plt.sca(ax[0])
	plt.hist([np.log10(tables[cloud][s].P) for s in labels["selected"]], **hist_options)
	plt.hist(np.log10(tables[cloud]["total"].P), **total_hist_options)
	if i:
		plt.xlabel(r"$\log_{10}(P)$")
	plt.ylabel(fr"{cloud.upper()} star amount")
	#
	plt.sca(ax[1])
	plt.hist([tables[cloud][s].I for s in labels["selected"]], **hist_options)
	plt.hist(tables[cloud]["total"].I, **total_hist_options)
	if i:
		plt.xlabel(r"$I_{mean}$")
		plt.xlim(np.flip(plt.gca().get_xlim()))
	#	
	plt.sca(ax[2])
	plt.hist([tables[cloud][s].ptp for s in labels["selected"]], **hist_options)
	plt.hist(tables[cloud]["total"].ptp, **total_hist_options)
	if i:
		plt.xlabel(r"$\Delta I$")

sublabels = "abcdef"
for i,ax in enumerate(axes.ravel()):
	plt.sca(ax)
	plt.text(0.95, 0.1, sublabels[i]+")", fontsize=15,
			horizontalalignment='center', verticalalignment='center', 
			transform=ax.transAxes)
	
plt.sca(axes[0,0])
plt.legend(title="pulsation mode")
plt.tight_layout()

plt.savefig("./text/img/clouds_histogram_PIdI.pdf")

#############################################################################

hist_options = dict(stacked=True,bins=30,color=colors,label=labels["selected"])
total_hist_options = dict(bins=30,histtype="step",color='k',label="total")

fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(10,7),sharey="row",sharex="col")

for i,cloud in enumerate(["lmc","smc"]):
	ax = axes[i]
	
	plt.sca(ax[0])
	plt.hist([tables[cloud][s].nI for s in labels["selected"]], **hist_options)
	plt.hist(tables[cloud]["total"].nI, **total_hist_options)
	if i:
		plt.xlabel(r"$I$ points per star")
	plt.ylabel(fr"{cloud.upper()} star amount")
	
	plt.sca(ax[1])
	plt.hist([tables[cloud][s].nV for s in labels["selected"]], **hist_options)
	plt.hist(tables[cloud]["total"].nV, **total_hist_options)
	if i:
		plt.xlabel(r"$V$ points per star")

sublabels = "abcd"
for i,ax in enumerate(axes.ravel()):
	plt.sca(ax)
	plt.text(0.05, 0.9, sublabels[i]+")", fontsize=15,
			horizontalalignment='center', verticalalignment='center', 
			transform=ax.transAxes)

plt.sca(axes[1,1])
plt.legend(title="pulsation mode")
plt.tight_layout()

plt.savefig("./text/img/clouds_histogram_ns.pdf")








