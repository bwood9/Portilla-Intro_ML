# Series are built onto NumPy array objects and very similar to NumPy arrays
# A difference is that they can contain labels
import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

s1 = pd.Series(data = my_data)
print s1
# Now name indices
s2 = pd.Series(my_data, labels)
print s2
# Can also create series from array
s3 = pd.Series(arr, labels)
print s3
# Can also create series from just a dictionary
s4 = pd.Series(d)
print s4
# Can also create series from strings or functions
s5 = pd.Series(data = labels)
# s6 = pd.Series(data = [sum,print,len])

ser1 = pd.Series([1,2,3,4], ["USA", "Germany", "USSR", "Japan"])
print ser1
ser2 = pd.Series([1,2,5,4], ["USA", "Germany", "Italy", "Japan"])
print ser2
print ser1["USA"]
ser3 = pd.Series(data = labels)
print ser3[0]
ser4 = ser1 + ser2
print ser4