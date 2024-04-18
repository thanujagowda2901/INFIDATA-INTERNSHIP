import numpy as np
#create an array from list type float
a1=np.array([[1,2,3,],[4,5,6]],dtype='float')  #create an array with all float num
print('array contents are',a1) #display the created array


#create an array from tuple type float
a2=np.array((1,2,3))  #create an array from tuple
print('array contents are',a2) #display the created array

#creating a 16*173 array with all zeros
a3=np.zeros((16,173))
print("\n an array initialized with all zeros:\n",a3)


#creating a 17*17 array with all zeros
a4=np.ones((17,17))
print("\n an array initialized with all ones:\n",a4)

#creating a 17*17 array with all zeros
a4=np.full((6,5),-24.6782)  #order =6*5 required  num=-24.6782
print("\n an array initialized with all -24.6782:\n",a4)

#creating a 3*2 array with all
a4=np.random.random((3,2))
print("\n an arary random\n",a4)


a5=np.arange(0,40,5)
print("\n a sequential array with step of 5",a5)

a5=np.linspace(0,40,10)
print("\n a sequential array with step of 4",a5)

all=np.array([[1,2,3],[4,5,6]])
reshaped_array=all.reshape((1,-1))
reshaped_array_2=all.reshape((-1,1))
print('\n original array',all)
print('\n reshape array',reshaped_array)
print('\n reshape array',reshaped_array_2)





