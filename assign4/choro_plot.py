#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from geopandas import GeoSeries, GeoDataFrame

fp = "map.ai"

map_df = gpd.readfile(fp)

map_df.head()
