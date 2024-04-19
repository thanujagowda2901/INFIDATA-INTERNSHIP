import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df=sns.load_dataset('iris') #loading the dataset
print(df)


#draw lineplot
sns.lineplot(x='sepal_length',y='sepal_width',data=df)
#setting the title using matplotlib
plt.title('Lineplot on IRIS data')
plt.show()