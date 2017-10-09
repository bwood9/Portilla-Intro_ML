import pandas as pd
from statsmodels.stats.multicomp import (pairwise_tukeyhsd as thsd, MultiComparison as mcomp)

df3 = pd.read_csv("C:/Users/bwoodruff/Documents/Tutoring/Data/handicap.csv")
df3['Handicap-Groups'] = pd.Categorical.from_array(df3.Handicap).codes
print df3

print df3['Handicap-Groups'].values

mc = mcomp(df3['Score'], df3['Handicap'])
print mc.tukeyhsd()

mc2 = thsd(df3['Score'], df3['Handicap'])
print mc2
