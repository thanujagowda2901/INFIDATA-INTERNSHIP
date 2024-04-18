def test(a, b=5, c=10):
    print('a is',a, 'and b',b,'and c is ',c)
test(3,7)
test(25,c=24)
test(c=50,a=100)

def func(x=1,y=2):
    return x+y,x-y
x,y=func(y=2,x=1)
print(x,y)

def func(x,y=2):
    num=1
    for i in range(y):
        num=num*x
    return num
print(func(4))
print(func(4,4))