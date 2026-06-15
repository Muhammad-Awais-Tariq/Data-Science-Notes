import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

yield_apples = [0.895 , 0.91 , 0.919 , 0.926 , 0.929 , 0.931]
yield_oranges = [0.925, 0.921, 0.900, 0.895, 0.890, 0.885]
years = [2010, 2011 , 2012 , 2013 , 2014 , 2016]
plt.plot(years , yield_apples , "xb")
plt.plot(years , yield_oranges , "or")
plt.xlabel("Years")
plt.ylabel("Yield")
plt.title("Crop yields in pakistan")
plt.legend(["Oranges","Apples"])
plt.show()
