#Program to find the largest of 3 numbers

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if (x > y and x > z):
    print("Largest number is:", x)
elif (y > x and y > z):
    print("Largest number is:", y)
else:
    print("Largest number is:", z)
    
'''
Output:

Enter first number: 12
Enter second number: 435
Enter third number: 212
Largest number is: 435

Enter first number: 1
Enter second number: 2
Enter third number: 3
Largest number is: 3


'''
