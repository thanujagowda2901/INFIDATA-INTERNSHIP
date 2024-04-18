import numpy as np
a5=np.arange(10,100,10)
print("\n a sequential array ",a5)

a4=np.random.random((2,5))
print("\n an arary random\n",a4)

a4=np.random.random([3,4])
print("\n an arary random\n",a4)

four_by_five=np.array([[1,2,3,4,5],
                       [6,7,8,9,10],
                       [11,12,13,14,15],
                       [16,17,18,19,10]])
print(four_by_five[0,:])

print(four_by_five[3,:])
print(four_by_five[2,3])

print(four_by_five[:,3:])