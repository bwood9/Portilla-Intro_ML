import pandas as pd
import seaborn as sbn
import numpy as np
import scipy.stats as sp_st
import pylab as pl
import statsmodels.api as sm
from statsmodels.formula.api import ols


# read in the csv as a dataframe
edu = pd.DataFrame.from_csv("C:/Users/bwoodruff/Documents/Tutoring/Data/ex0525.csv")
print edu.dtypes

income_less12 = edu.loc[edu['Educ'] == '<12']['Income2005']
income_12 = edu.loc[edu['Educ'] == '12']['Income2005']
income_13_15 = edu.loc[edu['Educ'] == '13-15']['Income2005']
income_16 = edu.loc[edu['Educ'] == '16']['Income2005']
income_greater16 = edu.loc[edu['Educ'] == '>16']['Income2005']

# check the assumptions of the raw data
sbn.boxplot(edu.Educ, edu.Income2005)
sbn.plt.show()

sp_st.probplot(income_less12, dist = 'norm', plot = pl)
pl.plt.show()
sp_st.probplot(income_12, dist = 'norm', plot = pl)
pl.plt.show()
sp_st.probplot(income_13_15, dist = 'norm', plot = pl)
pl.plt.show()
sp_st.probplot(income_16, dist = 'norm', plot = pl)
pl.plt.show()
sp_st.probplot(income_greater16, dist = 'norm', plot = pl)
pl.plt.show()

# perform log-transformation on raw data
edu["Log_Income2005"] = np.log(edu.Income2005)
print edu

log_income_less12 = edu.loc[edu['Educ'] == '<12']['Log_Income2005']
log_income_12 = edu.loc[edu['Educ'] == '12']['Log_Income2005']
log_income_13_15 = edu.loc[edu['Educ'] == '13-15']['Log_Income2005']
log_income_16 = edu.loc[edu['Educ'] == '16']['Log_Income2005']
log_income_greater16 = edu.loc[edu['Educ'] == '>16']['Log_Income2005']

# check the assumptions of the transformed data
sbn.boxplot(edu.Educ, edu.Log_Income2005)
sbn.plt.show()

sp_st.probplot(log_income_less12, dist = 'norm', plot = pl)
pl.plt.show()
sp_st.probplot(log_income_12, dist = 'norm', plot = pl)
pl.plt.show()
sp_st.probplot(log_income_13_15, dist = 'norm', plot = pl)
pl.plt.show()
sp_st.probplot(log_income_16, dist = 'norm', plot = pl)
pl.plt.show()
sp_st.probplot(log_income_greater16, dist = 'norm', plot = pl)
pl.plt.show()

# perform ANOVA on the transformed data
anova = ols('Log_Income2005 ~ Educ', data = edu).fit()
anova_table = sm.stats.anova_lm(anova, typ = 2, robust = 'hc3')
print anova_table

#print sp_st.oneway(log_income_less12, log_income_12, log_income_13_15, log_income_16, log_income_greater16, equal_var = False)


# Compute extra sum of squares F-Test

# First, subset the data
edu1 = edu.loc[edu['Educ'] == '16' & edu['Educ'] == '>16']