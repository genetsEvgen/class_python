import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

atlas = [
    [1,100],
    [3,200],
    [10,150],
    [20, 300],
    [50, 500]
]

geography = ['time', 'value']

df = pd.DataFrame(data = atlas , columns = geography)

#df = pd.read_csv('file.csv')
#print(df.info())
#df['Time'] = df['Time'].astype('datetime64[ns]')

df.hist()

input()