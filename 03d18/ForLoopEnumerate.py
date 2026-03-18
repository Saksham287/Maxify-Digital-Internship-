# For loops: Iterating with enumerate

colors = ["Red", "Black", "Green", "Brown", "Yellow", "Blue"]

for i, color in enumerate(colors, start= 1):
    print(i, color)
'''
Output:

1 Red
2 Black
3 Green
4 Brown
5 Yellow
6 Blue

'''

nums = [2, 3, 4, 5, 6, 7, 8 , 9]

for i, val in enumerate(nums):
    nums[i] = val ** 2
print(nums)
'''
Output:

[4, 9, 16, 25, 36, 49, 64, 81]

'''
