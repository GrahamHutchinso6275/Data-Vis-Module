import numpy as np                    
import pandas as pd                  
import itertools
from chord import Chord

#load data

url = 'superbowl.csv'
data = pd.read_csv(url)

#for testing data was loaded correctly

#print(data.head())
#print(data.shape)
#print(pd.DataFrame(data.columns.values.tolist()))

#drop all non essential data

data = pd.DataFrame(data[['Winner', 'Loser']].values)
#print(data)

data = list(itertools.chain.from_iterable((i, i[::-1]) for i in data.values))
matrix = pd.pivot_table(pd.DataFrame(data), index=0, columns=1, aggfunc="size",fill_value=0).values.tolist()
#print(pd.DataFrame(matrix))

names = np.unique(data).tolist()
#print(pd.DataFrame(names))

colours = ["#97233F","#A71930", "#A2AAAD", "#241773", "#00338D", "#0085CA", "#C83803", "#FB4F14", "#003594", "#FB4F14", "#203731", "#002C5F", "#E31837", "#A5ACAF", "#002244", "#008E97", "#4F2683", "#002244", "#D3BC8D", "#0B2265", "#125740", "#000000", "#004C54", "#FFB612", "#002A5E", "#AA0000", "#99BE28", "#866D4B", "#D50A0A", "#0C2340", "#773141"];

Chord(matrix, names, colors=colours, wrap_labels=False).show()
