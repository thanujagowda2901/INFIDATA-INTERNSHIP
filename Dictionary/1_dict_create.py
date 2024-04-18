#python dict ia an unordered collection of ite
#each item of a dict has a key/value pair
#dict are optimized to retrive values when the
#key is known

d1={}             #empty dict
print(d1)
print(type(d1))  #to check data type of the variable

d2=dict()  #empty dict with function
print('d1',d2)

print('dictionary with integer keys')
d3={1:'python',2:'java',3:'web'}
print(d3)

print('dictionary with mixed keys')
d5={1:'python','name':'mahesh',3:(4,5,6)} # 3:(4,5,6)=tuple value
print(d5)