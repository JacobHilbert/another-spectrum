import numpy as np
import matplotlib.pyplot as plt
import json
import toolz
import colorutils

plt.rcParams["axes.labelsize"] = 17
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

colors = {
	"U":"#300066",
	"B":"#6f00e9",
	"V":"#00ff00",
	"R":"#ff0000",
	"I":"#9a0000",
	"V\n(OGLE-IV)":"#006400",
	"I\n(OGLE-IV)":"#dc143d"
}

def darken(color):
	return colorutils.Color((0, 0, 0), arithmetic=colorutils.ArithmeticModel.BLEND) + color

dark_colors = toolz.valmap(
	toolz.compose(
		darken,
		colorutils.hex_to_rgb
	),
	colors
)

with open("./code/theory/filter_curves.json") as file:
	d = json.load(file)

d = toolz.keymap(lambda s: s.replace(" ","\n"),d)

johnson = {k:v for k,v in d.items() if k in "UBVRI"}

plt.figure(figsize=(10,2.5))
for name in "UBVRI":
	data = np.array(d[name])
	plt.fill_between(data[0],np.zeros_like(data[1]),data[1],color=colors[name],alpha=0.3)
	plt.text(
		x = sum(data[0]*data[1])/sum(data[1]), # x-centroid
		y = 0.25,
		s = name,
		fontsize = 25,
		color = dark_colors[name].hex,
		ha='center', va='center',
	)

for name in ['V\n(OGLE-IV)', 'I\n(OGLE-IV)']:
	data = np.array(d[name])
	plt.plot(*data,color=colors[name],linewidth=2.5)
	#plt.fill_between(data[0],np.zeros_like(data[1]),data[1],color=colors[name],alpha=0.3)
	
	plt.text(
		x = sum(data[0]*data[1])/sum(data[1]),
		y = 0.75,
		s = name,
		fontsize = 18,
		color = colors[name],
		ha='center', va='center',
	)

plt.xlim(300,930)
plt.ylim(0,1.01)

plt.xlabel(r"$\lambda$ (nm)")
plt.ylabel(r"Transmittance")

plt.tight_layout()

plt.savefig("./text/img/filters.pdf")