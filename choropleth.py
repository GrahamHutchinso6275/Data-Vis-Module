import numpy as np 
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#shapefile = 'Brazil_Admin_1.shp'

#gdf = gpd.readfile(shapefile)['ADMIN', 'ADM0_A3', 'geometry']

#gdf.head()

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
print(world.head())

world.plot()
plt.show()
