import numpy as np   
import math                 
import pandas as pd                  
import itertools
from matplotlib import pyplot as plt
import matplotlib.animation as animation
plt.style.use('seaborn-pastel')

url = 'athlete_events.csv'
data = pd.read_csv(url)
df = pd.DataFrame(data[['Year', 'Team', 'Season', "Medal"]].values)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

rows = int(df.shape[0])
cols = int(df.shape[1])

print(rows)
print(cols)
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

print(len(medals))
print(len(years))
i = 0
xs = []
ys = []
	

while(i < len(medals)):
	def animate1(i):
		plt.xlabel('Year')
		plt.ylabel('Total Medals')
		plt.title('Total Medals Per Year')

		
		xs.append(float(years[i]))
		ys.append(float(medals[i]))

		ax1.clear()
		ax1.plot(xs,ys)

		i += 1

	ani = animation.FuncAnimation(fig, animate1, interval=2500)
	plt.show()
