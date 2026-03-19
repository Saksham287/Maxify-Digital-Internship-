# Create a program to find the largest number in a list using a for loop

num = [12, 21, 3, 34, 82, 92, 6, 44]
print(num)

i = 0 
largest = num[0]

while i < len(num):
    if num[i] > largest:
        largest = num[i]
    i += 1

print("Largest Number:", largest)

'''
Output:

[12, 21, 3, 34, 82, 92, 6, 44]
Largest Number: 92

'''
