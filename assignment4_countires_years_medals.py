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

print(rows)
print(cols)

#medals = []
years = []
countries = []

for i in range(1896, 2018, 4):	
	years.append(i)

for j in range(rows):
	if df[1][j] not in countries:
		if df[2][j] == "Gold" or df[2][j] == "Silver" or df[2][j] == "Bronze" :
			print(df[1][j])
			countries.append(df[1][j])


countries_len = len(countries)
years_len = len(years)

print('# of countries: ', countries_len)
print('# of years: ', years_len)

data_new = np.zeros((countries_len,years_len))

print('data shape: ', data_new.shape)

for i in range(rows):
	if df[2][i] == "Gold" or df[2][i] == "Silver" or df[2][i] == "Bronze" :
		if df[0][i] in years:
			index_noc = countries.index(df[1][i])
			index_year = years.index(df[0][i])
			data_new[index_noc][index_year] +=1
			
print(countries)
savetxt('years_countries_data.csv', data_new, delimiter=',')

print("Done")
	
