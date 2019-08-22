# https://www.cnblogs.com/gczr/p/6767175.html

import matplotlib.pyplot as plt  
import seaborn as sns
import numpy as np
import pandas as pd

'''
sns.set_style("whitegrid")  
plt.plot(np.arange(10))  
plt.show()  
'''

'''
sns.set( palette="muted", color_codes=True)  
rs = np.random.RandomState(10)  
d = rs.normal(size=100)  
f, axes = plt.subplots(2, 2, figsize=(7, 7), sharex=True)  
sns.distplot(d, kde=False, color="b", ax=axes[0, 0])  
sns.distplot(d, hist=False, rug=True, color="r", ax=axes[0, 1])  
sns.distplot(d, hist=False, color="g", kde_kws={"shade": True}, ax=axes[1, 0])  
sns.distplot(d, color="m", ax=axes[1, 1])  
plt.show()  
'''
 
'''
grid=sns.FacetGrid(df,row='martial_status',col='education',palette='seismic',size=4)
grid.map(plt.scatter,'gjj_loan_balance','max_overduer_days')
grid.add_legend()
plt.show()
'''
 
# Initialize the data
x = 10 ** np.arange(1, 10)
y = x * 2
data = pd.DataFrame(data={'x': x, 'y': y})

'''
  # Create an lmplot
grid = sns.lmplot('x', 'y', data, height=7, truncate=True, scatter_kws={"s": 100})
  # Rotate the labels on x-axis
grid.set_xticklabels(rotation=90)
  # Show the plot
plt.show()
'''
g = sns.FacetGrid(data, row='y', height=4, aspect=2, xlim=(0,30))
g.map(sns.distplot, 'x', rug=False)
plt.show()

