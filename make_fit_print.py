#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime

def read_data(filename):
	f= open(filename,"r")
	date=[]; mass=[]
	lines = f.readlines()
	for line in lines[1:]:
		s = line.split(',')
		if s[11].replace('.','',1).isdigit():
			my_date = datetime.strptime(str(s[0]), '%Y-%m-%d')
			date.append(my_date)
			mass.append(float(s[11]))
	return date, mass;

def plot_date(dates, mass):
	plt.plot(date,mass)
	plt.plot(date,mass,'+')
	#plt.plot_damte(date,mass,'ro')
	plt.ylabel('Masa ciala K.Kosmider [kg]')
	plt.xlabel('Data')
	plt.grid( True)
	plt.xticks(rotation='vertical')
	plt.show()



script = sys.argv[0]
filename = sys.argv[1]

date, mass = read_data(filename)
plot_date(date,mass)
