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
import pylab

#set up full canvas

fig, axs = plt.subplots(2,2, figsize=(10, 6))
fig.suptitle("Olympic Medals Per Country", fontsize=16)

#load map shapefile

shapefile = 'ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
gdf.columns = ['country', 'country_code', 'geometry']
gdf = gdf.drop(gdf.index[159])

#load and set up yearly choropleth map data

datafile = 'data_for_choro.csv'
df = pd.read_csv(datafile)
df_test = pd.DataFrame(df[['a', 'b', 'c']].values)
axs[0][0].set_title('Olympic Medals Per Country Per Year')
axs[0][0].axis('off')
medal_min = 0
medal_max = 250
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=medal_min, vmax=medal_max))
sm._A = []
cbar = fig.colorbar(sm, ax=axs[0][0])

#load total number of medals per year data

url = 'countries_medals.csv'
data = pd.read_csv(url)
df1 = pd.DataFrame(data[['Year', 'Medals']].values)
xs = []
ys = []
axs[1][0].set_xlabel('Year')
axs[1][0].set_ylabel('Medals')
axs[1][0].set_title('Live Graph of Total Medals Per Year')

#set up total medals choropleth map 

datafile1 = 'total_choro.csv'
df2 = pd.read_csv(datafile1)
df_test1 = pd.DataFrame(df2[['a', 'b', 'c']].values)
axs[0][1].set_title('Total Olympic Medals Per Country')
axs[0][1].axis('off')
total_medal_min = 0
total_medal_max = 12500
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=total_medal_min, vmax=total_medal_max))
sm._A = []
cbar = fig.colorbar(sm, ax=axs[0][1])

#set up year counter

axs[1][1].axis('off')

def animate(i):

	global cbar

	#plotting choropleth map current
	num = 1896 + (i*4)
	df_curr = df[df['a'] == num]
	merged = gdf.merge(df_curr, left_on = 'country_code', right_on = 'b')
	variable = 'c'
	merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=axs[0][0], edgecolor='0.8')

	#plotting total medals data
	
	xs.append(df1[0][i])
	ys.append(df1[1][i])
	axs[1][0].plot(xs, ys, color='blue')

	#plotting total choropleth

	num = 1896 + (i*4)
	df_curr_1 = df2[df2['a'] == num]
	merged = gdf.merge(df_curr_1, left_on = 'country_code', right_on = 'b')
	variable = 'c'
	merged.plot(column=variable, cmap='Reds', linewidth=0.8, ax=axs[0][1], edgecolor='0.8')

	#display year
	axs[1][1].clear()
	axs[1][1].axis('off')
	str_num = str(num)
	axs[1][1].text(0, 0.3, str_num, fontsize='100')
	
	filename = 'images/image' + str(num) + '.png'
	plt.savefig(filename, dpi=250)

anim = animation.FuncAnimation(fig, animate, interval=300) 
plt.show()

#anim.save('olympics_1.gif',writer='imagemagick')

