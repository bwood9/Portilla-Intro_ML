# for the sake of this lecture, we will only be concerned
# with CSV, Excel, HTML, and SQL
import pandas as pd
import sqlalchemy as alc
import lxml
import html5lib as html
# import BeautifulSoup4 as bs4

df = pd.read_csv('C:\\Users\\bwoodruff\\Documents\\Python\\Udemy-Portilla\\Data_Science\\Pandas\\Data\\example.txt')
print df

# let's write this to a .csv and not create an index:
df.to_csv('C:\\Users\\bwoodruff\\Documents\\Python\\Udemy-Portilla\\Data_Science\\Pandas\\Data\\My_Output', index = False)

df2 = pd.read_excel('C:\\Users\\bwoodruff\\Documents\\Python\\Udemy-Portilla\\Data_Science\\Pandas\\Data\\Excel_Sample.xlsx', sheetname = 'Sheet1')
print df2

# now let's read this to an Excel WB

df2.to_excel('C:\\Users\\bwoodruff\\Documents\\Python\\Udemy-Portilla\\Data_Science\\Pandas\\Data\\Excel_Sample2.xlsx', sheet_name = 'NewSheet')

df3 = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# in this case, pandas tried to find every data frame in the HTML page
print type(df3)
print df3[0]

# sqlalchemy is not the best for reading in SQL data, should use libraries specifically
# designed for the given SQL engine (e.g. psycopg2 for PostgreSQL). Still, we will explore sqlalchemy lib

from sqlalchemy import create_engine
# First, we will create our own SQL engine
engine = create_engine('sqlite:///:memory:')
# Now, we will write a dataframe to the created engine
df.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table', con = engine)
print sqldf


