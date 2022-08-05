from hashlib import new
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sympy import subsets

df = pd.read_csv('sales_ts.csv')

df = df[['Period', 'Sales_quantity']]

df["Period"] = pd.to_datetime(df["Period"])

ax = df.plot(x='Period', y='Sales_quantity', figsize=(12,6))

xcoords = ['2015-01-01', '2015-05-01', '2016-01-01','2017-01-01', '2018-01-01', '2019-01-01', '2020-01-01']

plt.show()