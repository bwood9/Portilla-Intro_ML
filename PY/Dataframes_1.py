import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print df
print df['W']
print type(df['W'])
print type(df)
# to grab for multiple cols, specify a list
print df[['W', 'Z']]
# let's create a new col
df["new"] = df['W'] + df['Y']
print df
# now let's drop this new col
df.drop("new", axis = 1)
print df
# to do permanently, use an inplace arg
df.drop("new", axis = 1, inplace = True)
print df
# now let's drop a row
df.drop('E', axis = 0, inplace = True)
print df
print df.shape
# two ways to select rows in dataframe:
print df.loc['A']
print df.iloc[0]
print df.loc['B', 'Y']
print df.iloc[1, 2]
print df.loc[['A', 'B'], ['W', 'Y']]
print df.iloc[[0, 1], [0, 2]]