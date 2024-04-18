#ASSUMING A DATAFRAME/DATASET IS ALREADY PRESENT,
#THIS IS HOW WE READ/LOAD IT

import pandas as pd  #creating and handling dataframe
#loading id.csv into pandas dataframe
data=pd.read_csv('diabetes.csv')
print(data) #displaying the dataframe

#
print('display specfic columns')
print(data['Glucose']) #displaying single column
print(data[['Glucose','BMI']]) #display multiple column

#
print(data.shape) #display shape of dataset

print(data.size) #display size of data

#indexing
print(data.head()) #print first 5 rows of data

print(data.tail()) #print last 5 rows

