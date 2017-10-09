import numpy as np
import pandas as pd
from numpy.random import randn

# dealing w/multi-level index dataframes

# index levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
print hier_index
hier_index = pd.MultiIndex.from_tuples(hier_index)
print hier_index

# Create df w/multi-level indices
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print df
print df.loc['G1'].iloc[1]

df.index.names = ['Groups', 'Nums']
print df

print df.loc['G2'].loc[2]['B']
# note diff b/t loc and iloc w/ints

# grab cross-section of data (all obs w/nums equal to 1)
print df.xs(1, level = 'Nums')
print df.xs('G1', level = 'Groups')