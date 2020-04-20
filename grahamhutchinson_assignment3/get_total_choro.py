import numpy as np   
import math                 
import pandas as pd                  
import itertools
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from numpy import savetxt
from celluloid import Camera
import time
import geopandas as gpd

datafile = 'data_for_choro.csv'
df = pd.read_csv(datafile)
df_test = pd.DataFrame(df[['a', 'b', 'c']].values)

df2 = pd.DataFrame(columns=list('abc'))
for i in range(4619):
	year = 1896 + (4 * int(i/149))
	country = df_test[1][i]
	medals = 0
	df2 = df2.append({'a': year, 'b': country, 'c': medals}, ignore_index=True)

print(df2)

totals = []

for i in range(149):
	totals.append(0)

for j in range(4619):
	curr = j % 149
	#curr1 = int(j / 149)
	#year = 1896 + (4 * curr1)
	year = df_test[0][j]
	country = df_test[1][j]
	num1 = df_test[2][j]

	if(j>=149):	
		df2.loc[df2.a.isin([year]) & df2.b.isin([country]), 'c'] += (num1 + totals[curr])
	else:
		df2.loc[df2.a.isin([year]) & df2.b.isin([country]), 'c'] += num1 

	totals[curr] += num1
	
print(df2)
df2.to_csv(r'total_choro.csv', index=False)
