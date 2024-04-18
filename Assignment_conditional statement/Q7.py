num_presence=int(input('enter total num of wrking days>'))
num_absence=int(input('enter num of days absence>'))
percentage=(num_presence-num_absence)/num_presence*100
print('percentage of class attended is:',percentage)
if(percentage<75):
    print('you will not able to take the exams')
else:
    print('you will be able to take the exams')