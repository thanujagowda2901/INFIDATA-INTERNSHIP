test_keys=['python','java','web']
test_values=[101,102,103]
print('original key list is:'+str(test_keys))
print('original value is:'+str(test_values))
# to covert lists to dictionary
res={}
for key in test_keys:
    for value in test_values:
        res[key]=value
        test_values.remove(value)
        break
print('resultant dictionary is:'+str(res))