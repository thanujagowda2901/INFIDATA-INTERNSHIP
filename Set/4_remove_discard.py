s1={1,2,3,4,5,4}
s1.remove(3)
print('removed s1 is',s1)

s1.discard(1)
print('after discard(1)',s1)

s1.remove(1)  #key error
print('remove s1',s1)

s1.discard(1) #no error
print('discard s1',s1)