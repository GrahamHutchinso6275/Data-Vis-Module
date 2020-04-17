import numpy as np   
import math                 
import pandas as pd                  
import itertools
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from numpy import savetxt
plt.style.use('seaborn-pastel')

url = 'athlete_events.csv'
data = pd.read_csv(url)
df = pd.DataFrame(data[['Year', 'Team', 'Season', "Medal"]].values)

rows = int(df.shape[0])
cols = int(df.shape[1])

medals = []
years = []

for i in range(1896, 2018, 4):	
	count = 0
	for y in range(rows):
		#print(df[0][y]) #year
		#print(df[1][y]) #countries
		#print(df[2][y]) #games
		#print(df[3][y]) #medal

		if(df[0][y] == i):
			if(df[3][y] == "Gold" or df[3][y] == "Silver" or df[3][y] == "Bronze"):
				count += 1

	print(i,":",count)
	medals.append(float(count))	
	years.append(float(i))

#print(len(medals))
#print(len(years))

length1 = int(len(medals))
print(length1)

data_new = np.zeros((length1 ,2))
for i in range(len(medals)):
	data_new[i][0] = years[i]
	data_new[i][1] = medals[i]

print(data_new)
savetxt('countries_medal_data.csv', data_new, delimiter=',')
