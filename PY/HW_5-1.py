import pandas as pd
import seaborn as sbn
import numpy as np
import scipy.stats as sp_st
import pylab as pl
import statsmodels.api as sm
from statsmodels.formula.api import ols


# read in the csv as a dataframe
df3 = pd.DataFrame.from_csv("C:/Users/bwoodruff/Documents/Tutoring/Data/ex0525.csv")
print df3.dtypes

# perform log-transformation on raw data
df3["Log_Income2005"] = np.log(df3.Income2005)
print df3

log_income_less12 = df3.loc[df3['Educ'] == '<12']['Log_Income2005']
log_income_12 = df3.loc[df3['Educ'] == '12']['Log_Income2005']
log_income_13_15 = df3.loc[df3['Educ'] == '13-15']['Log_Income2005']
log_income_16 = df3.loc[df3['Educ'] == '16']['Log_Income2005']
log_income_greater16 = df3.loc[df3['Educ'] == '>16']['Log_Income2005']

# Compute extra sum of squares F-Test

total_mu = np.mean(df3[(df3.Educ == '16') | (df3.Educ == '>16')]['Log_Income2005'])
mu_less12 = np.mean(log_income_less12)
mu_12 = np.mean(log_income_12)
mu_13_15 = np.mean(log_income_13_15)
mu_16 = np.mean(log_income_16)
mu_gr16 = np.mean(log_income_greater16)

reduc_resid_16 = log_income_16 - total_mu
reduc_resid_gr16 = log_income_greater16 - total_mu
full_resid_less12 = log_income_less12 - mu_less12
full_resid_12 = log_income_12 - mu_12
full_resid_13_15 = log_income_13_15 - mu_13_15
full_resid_16 = log_income_16 - mu_16
full_resid_gr16 = log_income_greater16 - mu_gr16
full = full_resid_less12.append(full_resid_12).append(full_resid_13_15).append(full_resid_16).append(full_resid_gr16)

reduc_ss = sum(reduc_resid_16 ** 2) + sum(reduc_resid_gr16 ** 2)
full_ss = sum(full ** 2)
extra_ss = abs(reduc_ss - full_ss)
extra_df = len(full) - (len(reduc_resid_16) + len(reduc_resid_gr16))
print extra_df
print len(reduc_resid_16) + len(reduc_resid_gr16)

sd_full = np.std(full)

f_stat = (extra_ss / extra_df) / sd_full
print "f stat:" and f_stat

# Given an f-statistic of .855, numerator df of 1804 and denominator df of 780, a p-value of .995 is produced.
# We fail to reject the null hypothesis with 95% confidence as our p-value is greater than our alpha level of .05.