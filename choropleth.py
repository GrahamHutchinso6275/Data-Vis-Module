import numpy as np 
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

shapefile = 'Brazil_Admin_1.shp'
#shapefile = 'Brasil.shx'
gdf = gpd.read_file(shapefile) #['ADMIN', 'ADM0_A3', 'geometry']
print(gdf.head())

gdf.plot()
plt.show()


#world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#print(world.head())
#world.plot()
#plt.show()
