from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=6, p=0.5,size=10000), hist=True, kde=False)

plt.show() 
