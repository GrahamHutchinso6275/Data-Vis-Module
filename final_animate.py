import numpy as np   
import math                 
import pandas as pd                  
import itertools
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from numpy import savetxt
from celluloid import Camera
import time
plt.style.use('seaborn-pastel')

fig, axes = plt.subplots(2)
#ax1 = fig.add_subplot(1,1,1)
camera = Camera(fig)
xs = []
ys = []


def animate(i):
	url = 'countries_medal_data.csv'
	data = pd.read_csv(url)
	df = pd.DataFrame(data[['Year', 'Medals']].values)
	
	print(df[0][i])
	print(df[1][i])
	
	length = df.shape[0]	
	if(i < length):	
		#time.sleep(1)
		xs.append(df[0][i])
		ys.append(df[1][i])
	
	print(xs)
	print(ys)

	#ax1.clear()
	axes[0].plot(xs,ys, color='blue')
	axes[1].plot(xs,ys, color='red')
	camera.snap()

	plt.xlabel('Year')
	plt.ylabel('Medals')
	plt.title('Live Graph of Medals Vs. Years')
		

ani = animation.FuncAnimation(fig, animate, interval=500) 
plt.show()
