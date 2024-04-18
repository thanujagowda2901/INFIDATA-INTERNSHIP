#CREATING A DATAFRAME/DATASET

import pandas as pd
#how to convert dictionary to dataframe

data=pd.DataFrame({
    'name':['ali','khan','mahesh','vinit'],
    'age':[20,25,30,25],
    'branch':['cse','me','i se','ece'],
    'place':['bangalore','delhi','mysore','porbandar']
})

print(data)

#saving the dataframe created as csv file
data.to_csv('id.csv',index=False)