import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df=sns.load_dataset('iris') #loading the dataset



#draw lineplot
sns.boxplot(x='species',y='sepal_width',data=df,palette="Set2")
plt.show()