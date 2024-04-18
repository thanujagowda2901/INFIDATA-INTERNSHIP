def create_account():
    global cname,cid,branch,balance
    cname=input('enter the coustmer name')
    cid=int(input('enter the id'))
    branch=input('enter the Branch name')
    balance=float(input('enter the balance amount'))
def deposite():
    global balance,dep
    dep=float(input('enter the amount'))
    balance+=dep
    print('the total amount',balance)
def withdraw():
    global balance,withdraw
    withdraw=int(input('enter the amount'))
    if (withdraw<= balance):
        balance-=withdraw
        print(balance)
    else:
        print('Insufficent blance')

def display():
    print(cname)
    print(cid)
    print(branch)
    print(balance)

print('welcome to online banking')
while(True):
    choice=int(input('enter Your choice 1:create_account 2:deposite,3:withdraw, 4:display, 5:exit'))
    if choice==1:
        create_account()
    elif choice==2:
        deposite()
    elif choice==3:
        withdraw()
    elif choice==4:
        display()
    else:
        print('invalid choice')