import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print df

# conditional selection:
print df > 0
print df[df > 0]
print df['W'] > 0
print df[df['W'] > 0]
print df[df['Z'] < 0]
df_1 = df[df['W'] > 0]['X']
print df_1
df_2 = df[df['W'] > 0][['Y', 'X']]
print df_2
df_3 = df[(df['W'] > 0) & (df['Y'] > 1)]
print df_3
df_4 = df[(df['W'] > 0) | (df['Y'] > 1)]
print df_4
print df
# reset index to col then create obs col
print df.reset_index(inplace = False)
newind = 'CA NY WY OR CO'.split()
print newind
df['States'] = newind
print df
df.set_index('States')
print df
df.set_index('States', inplace = True)
print df