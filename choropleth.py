import numpy as np 
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

#loads a shape file and plots it.

#shapefile = 'Brazil_Admin_1.shp'
#gdf = gpd.read_file(shapefile)
#print(gdf.head)
#gdf.plot()
#plt.show()

#datafile = 'amazon.csv'
#df = pd.read_csv(datafile, encoding='ISO-8859-1')

#print(df.head())

#shapefile = 'data/countries_110m/ne_110m_admin_0_countries.shp'#Read shapefile using Geopandas
#gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]#Rename columns.
#gdf.columns = ['country', 'country_code', 'geometry']
#gdf.head()

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
print(world.head())
world.plot()
plt.show()
