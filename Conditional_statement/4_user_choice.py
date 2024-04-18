n1=int(input('enter the num'))
n2=int(input('enter the num'))
ch=int(input('enter ur choice 1:add,2:sub,3:mul,4:div,5:mod'))
if(ch==1):
    res=n1+n2
    print("add a {0} and {1} is {2}".format(n1,n2,res))
elif(ch==2):
    res=n1-n2
    print('sub a {0} and {1} is {2}'.format(n1,n2,res))
elif(ch==3):
    res=n1*n2
    print('mul a {0} and {1} is {2}'.format(n1,n2,res))
elif(ch==4):
    res=n1/n2
    print('div a {0} and {1} is {2}'.format(n1,n2,res))
elif(ch==5):
    res=n1%n2
    print('mod a {0} and {1} is {2}'.format(n1,n2,res))
else:
    print('invalid choice')



