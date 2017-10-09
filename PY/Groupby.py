# Groupby is a function common to SQL that allows user to group rows together
# based off of a column and perform an aggregate (e.g. sum, mean, sd, etc.) function on them.
import pandas as pd

# create dictionary containing the data
data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person':['Same', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales':[200, 120, 340, 124, 243, 350]}
# read in data as dataframe
df = pd.DataFrame(data)
print df

byComp = df.groupby('Company')
print byComp
# groupby will ignore any aggregating col that is non-numeric
print byComp.mean()
print byComp.std()

print df.groupby('Company').sum()
# separate
print ''
# groupby for only FB (count number of instances
print df.groupby('Company').count().loc['FB']
print ''
# min will print first in alphabetical order for strings
print df.groupby('Company').min().loc['GOOG']
# print various aggregation functions in one line of code
print df.groupby('Company').describe()
# transpose describe print
print df.groupby('Company').describe().transpose()
# print for only FB
print df.groupby('Company').describe().transpose()['FB']