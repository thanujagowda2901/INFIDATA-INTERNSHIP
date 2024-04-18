#remove a particular item in a dict by using the pop() method.
#this method removes an item with the provided key and returns the value.
#popitem() method can be used to remove and return an arbitary(key, value)
#item pair form the dict.
#all the item can be removed at once, using the clear() method.
#we can also use the del keyword to remove individual items or the entire
#dict itself

d1={1:2,2:4,3:9,4:16,5:25,6:36}
print(d1)

print('pop value is:',d1.pop(2))
print('updated dictionary is',d1)

print('pop item is',d1.popitem())  #remove an arbitrary item, return (key,value)
print('updated dictionary is',d1)

print('clear dictionary is',d1.clear())  #remove all items
print('updated dictionary is',d1)

del d1  #delete the dict itself
print(d1) #error

