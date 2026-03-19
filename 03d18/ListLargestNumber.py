# Find the largest number in a list

num = [12, 21, 3, 34, 82, 92, 6, 44]
print(num)

num.sort(reverse= True)     # This will put the list in descending order 
print(num)
print("Largest Number:", num[0])    # After sorting we know the largest number will be sorted to index 0

'''
Output: 

[12, 21, 3, 34, 82, 92, 6, 44]
[92, 82, 44, 34, 21, 12, 6, 3]
Largest Number: 92

'''
