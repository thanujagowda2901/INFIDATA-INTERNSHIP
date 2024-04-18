t1=(1,2,3,4,5)
for i in t1:
    print(i)

for i in t1[2:5]:
    print(i)

for i in t1[:3]:
    print(i)

sum=0
avg=0
for i in t1:
    sum=sum+i
print('sum of t1 is',sum)
avg=sum/len(t1)
print('avg of t1 is ',avg)