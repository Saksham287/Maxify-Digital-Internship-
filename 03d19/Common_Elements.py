# Find common elements between two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

num_set1 = set(list1)
num_set2 = set(list2)
common = set()

for x in num_set1:
    if x in num_set2:
        common.add(x)
print(common)

'''
Output:

{3, 4}
'''
