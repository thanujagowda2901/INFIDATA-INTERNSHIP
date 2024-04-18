import pandas as pd  #used handling data frame

df=pd.read_csv('diabetes.csv') #loading data into a dataframe

#head
print('accessing from the dataset from first 10 rows \n',df.head(10))
print('accessing from the dataset from first 5 rows \n',df.head())

#tail
print('accessing from the dataset from last 10 rows \n',df.tail(10))
print('accessing from the dataset from last 5 rows \n',df.head())

print(df.shape) #rows and columns values
print(df.columns[df.isna().any()]) #to check for null values

#information data
print('basic info:\n',df.info())

#basic statistical information
print('statistical info:\n',df.describe())