pay=45000
location='Delhi'
if location=='Mumbai':
    print('i will take it')
elif location=='Chennai':
    if pay<100000:
        print('no way')
    else:
        print('iam willing')
elif location=='Delhi' and pay>40000:
    print('iam happy to join')
elif pay>60000:
    print('i accept the offer')
else:
    print('no thanks,i can find something better')