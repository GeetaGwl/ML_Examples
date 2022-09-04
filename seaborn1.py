import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
sales = pd.read_csv('sale.csv')

sns.catplot(x="Months", y="Sale",hue="Years",kind="boxen",data=sales)
#print(sales.head())
plt.legend()
plt.show()