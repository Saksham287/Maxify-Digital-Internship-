# Find the Second Largest Number

num = [28, 12, 56, 78, 84, 13, 28, 56, 99, 47, 85, 85]
print(num)
print(type(num))
'''
Output:
[28, 12, 56, 78, 84, 13, 28, 56, 99, 47, 85, 85]
<class 'list'>
'''

set_num = set(num)      # Changes into the set and deletes duplicate values
print(set_num)
print(type(set_num))
'''
Output:
{99, 12, 13, 78, 47, 84, 85, 56, 28}
<class 'set'>
'''
largest = 0
second_largest = 0
for x in set_num:
    if largest < x:                                 # finds the largest value 
        largest = x
    elif largest > x and x > second_largest:        
        second_largest = x 
    else:
        continue
        
print("Largest Number:" ,largest)
print("Second Largest Number:", second_largest)     

'''
Output:
Largest Number: 99
Second Largest Number: 85
'''