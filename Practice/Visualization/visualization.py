import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# sns.set_style("whitegrid")

# yield_apples = [0.895 , 0.91 , 0.919 , 0.926 , 0.929 , 0.931]
# yield_oranges = [0.925, 0.921, 0.900, 0.895, 0.890, 0.885]
# years = [2010, 2011 , 2012 , 2013 , 2014 , 2016]
# plt.plot(years , yield_apples , "xb")
# plt.plot(years , yield_oranges , "or")
# plt.xlabel("Years")
# plt.ylabel("Yield")
# plt.title("Crop yields in pakistan")
# plt.legend(["Oranges","Apples"])
# plt.show()

flower_df = sns.load_dataset("iris")
# sns.scatterplot(x=flower_df.sepal_length , y=flower_df.sepal_width , hue = flower_df.species , s=100)
# plt.show()
# plt.plot(flower_df.sepal_length , flower_df.sepal_width)
# plt.show()
# plt.title("Distribution of sepal width")
# plt.hist(flower_df.sepal_width , bins =5 , edgecolor='black')
# plt.show()
# plt.hist(flower_df.sepal_width , bins =np.arange(2 , 5 ,0.25) , edgecolor='black')
# plt.show()

setosa_df = flower_df[flower_df.species == 'setosa']
versicolor_df = flower_df[flower_df.species == 'versicolor']
virginica_df = flower_df[flower_df.species == 'virginica']

plt.title("Distribution of sepal width")
plt.hist([setosa_df.sepal_width , versicolor_df.sepal_width , virginica_df.sepal_width] , bins =np.arange(2 , 5 ,0.25) , stacked = True , edgecolor='black' )
plt.legend(['setosa' , 'versicolor' , 'virginica'])
plt.show()