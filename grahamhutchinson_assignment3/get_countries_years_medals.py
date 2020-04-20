import numpy as np   
import math                 
import pandas as pd                  
import itertools
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from numpy import savetxt
from celluloid import Camera
import time

url = 'athlete_events.csv'
data = pd.read_csv(url)
df = pd.DataFrame(data[['Year', 'NOC', "Medal"]].values)

rows = int(df.shape[0])
cols = int(df.shape[1])

years = []
countries = []

for i in range(1896, 2018, 4):	
	years.append(i)

for j in range(rows):
	if df[1][j] not in countries:
		if df[2][j] == "Gold" or df[2][j] == "Silver" or df[2][j] == "Bronze" :
			countries.append(df[1][j])

countries_len = len(countries)
years_len = len(years)

total = countries_len*years_len

df_new = pd.DataFrame(columns=list('abc'))

for i in range(total):
	code_i = i % 149
	year_i = int(i / 149)
	year = years[year_i]
	code = countries[code_i]
	df_new = df_new.append({'a': year, 'b': code, 'c': 0}, ignore_index=True)

for i in range(rows):
	if df[2][i] == "Gold" or df[2][i] == "Silver" or df[2][i] == "Bronze" :
		if df[0][i] in years:

			df_new.loc[df_new.a.isin([df[0][i]]) & df_new.b.isin([df[1][i]]), 'c'] += 1
			
df_new.to_csv(r'data_for_choro.csv', index=False)
