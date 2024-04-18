name=(input('enter the customer name'))
Id=int(input('enter the customer Id'))
e_bill=(int(input('enter the units')))
print('name is ',name)
print('id is',id)
if(e_bill<=100):
    print('No charge')
elif(e_bill>100 and e_bill<200):
    res=e_bill*5
    print('charge',res)
elif(e_bill>200):
    res=e_bill*10
    print('charge',res)
else:
    print('ntg')




