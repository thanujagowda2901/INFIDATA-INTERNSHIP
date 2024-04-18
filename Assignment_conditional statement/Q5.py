bike=int(input('enter the cost price'))
if(bike>100000):
    print('road tax will be 15%')
elif(bike>50000 and bike<=100000):
    print('road tax will be 10%')
elif(bike<=50000):
    print('road tax will be 5%')