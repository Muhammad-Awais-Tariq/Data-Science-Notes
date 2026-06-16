import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image

# sns.set_style("whitegrid")

yield_apples = [0.895 , 0.91 , 0.919 , 0.926 , 0.929 , 0.931]
yield_oranges = [0.925, 0.921, 0.900, 0.895, 0.890, 0.885]
years = [2010, 2011 , 2012 , 2013 , 2014 , 2016]
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

# plt.title("Distribution of sepal width")
# plt.hist([setosa_df.sepal_width , versicolor_df.sepal_width , virginica_df.sepal_width] , bins =np.arange(2 , 5 ,0.25) , stacked = True , edgecolor='black' )
# plt.legend(['setosa' , 'versicolor' , 'virginica'])
# plt.show()

# plt.bar(years , yield_apples)
# plt.plot(years , yield_apples , 'o--r')
# plt.bar(years , yield_oranges , bottom = yield_apples)
# plt.show()

tips_df = sns.load_dataset("tips")
# sns.barplot(x = 'day' , y ='total_bill' , hue = 'sex' , data= tips_df)
# sns.barplot(y = 'day' , x ='total_bill' , hue = 'smoker' , data= tips_df)
# plt.show()


flights_df = sns.load_dataset('flights').pivot(columns="year" , index="month" , values="passengers")
# sns.heatmap(flights_df , fmt="d" , annot=True , cmap="Blues")
# plt.show()

img = Image.open("image (16).png")
# img_array  = np.array(img)
# plt.imshow(img_array[125:325 , 105:305])
# plt.grid(False)
# plt.axis('off')
# plt.show()
# print(img_array)

figs, axis = plt.subplots(2, 3, figsize=(16, 8) , tight_layout=True)
axis[0,0].set_title("Crop_yiels")
axis[0,0].plot(years , yield_oranges , 'o--r')
axis[0,0].plot(years , yield_apples , 's-b')
axis[0,0].set_xlabel("year")
axis[0,0].set_ylabel("yield")
axis[0,1].set_title("special_length vs width")
sns.scatterplot(x=flower_df.sepal_length , y=flower_df.sepal_width , hue = flower_df.species , s=100 , ax=axis[0,1])
axis[0,2].set_title("Distribution of sepal width")
axis[0,2].hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width],  bins=np.arange(2, 5, 0.25), edgecolor='black', stacked=True,label=['Setosa', 'Versicolor', 'Virginica'])
axis[0,2].legend()
axis[1,0].set_title("Resturant bills")
sns.barplot(x = 'day' , y ='total_bill' , hue = 'sex' , data= tips_df , ax=axis[1,0])
axis[1,1].set_title("flight traffic")
sns.heatmap(flights_df , fmt="d" , annot=True , cmap="Blues" , ax = axis[1,1])
axis[1,2].set_title("Boom")
axis[1,2].imshow(img)
axis[1,2].grid(False)
axis[1,2].set_xticks([])
axis[1,2].set_yticks([])

plt.show()