import numpy as np
import pandas as pd

# read dictionary into dataframe
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print df.head()

# finding unique vals in dataframe

# find unique vals in col 2
print df['col2'].unique()
# find num of unique vals
print df['col2'].nunique()
# how many times each val occurs in col
print df['col2'].value_counts()

print df
# reminders: conditional selection
print df[df['col1'] > 2]
# combine conditions
print df[(df['col1'] > 2) & (df['col2'] == 444)]

# apply method is one of the most powerful tools in pandas
def times2(x):
    return x * 2

# apply function to each element in col 1
print df['col1'].apply(times2)

print df['col3'].apply(len)

# apply can be very useful w/lambda expressions as well
print df['col2'].apply(lambda x: x * 2) # performs same op as times2 function

# to apply own functions or lambda expressions is one of the most powerful capabilities of pandas

print df.columns
print df.index

# sort dataframe
print df.sort_values('col2')

# find nulls in dataframe
print df.isnull()

# create new dataframe
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print df

# pivot tables
print df.pivot_table(values = 'D', index = ['A', 'B'], columns = ['C'])