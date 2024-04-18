percentage=int(input('enter the percentage'))
if(percentage>90):
    print('A')
elif(percentage>80 and percentage<=90):
    print('B')
elif(percentage>=60 and percentage<=80):
    print('C')
elif(percentage<60):
    print('D')