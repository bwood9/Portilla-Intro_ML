import numpy as np
import pandas as pd

# create df out of dictionary
d = {'A':[1, 2, np.nan], 'B':[5, np.nan, np.nan], 'C':[1, 2, 3]}
df = pd.DataFrame(d)
print df

# defaults to dropping any rows w/nulls
print df.dropna()
# drop any cols w/nulls
print df.dropna(axis = 1)
# now set threshold to keep any rows w/2+ filled vals
print df.dropna(thresh = 2)

# lets fill the NAs
print df.fillna(value = 0)
print df['A'].fillna(value = df['A'].mean())
