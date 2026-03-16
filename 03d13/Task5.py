#If, Elif, else 

x = 10 
y = 2
z = 3

#If
if (x > 3 and (y < z or not(z > x))): # This is true, therefore it should execute the task.
    print("The expression is true")   # Output: The expression is true

#Elif
if x < 3:                             # This statement is False
    print(x, "is Less than 3")
elif (x > 3 and y > z):               # This statement is False
    print(x, "is greater than 3 and", y, "is greater than ", z) 
elif not(z > x):                      # This statement is True, therefore it should execute the task.
    print(y, "is greater than", z)    # Output: 2 is greater than 3
    
#else
if ((x + y) == 10):                   # This statement is False
    print(x, "+", y, "= 10")
elif ((y + z) > 10):                  # This statement is False
    print(y, "+", z, "is more than 10")
else:                                 # Else statement, therefore it should execute the task.
    print(y, "+", z, "is not equal", x) # Output: 2 + 3 is not equal 10
    
'''
Entire Output:

The expression is true
2 is greater than 3
2 + 3 is not equal 10

'''
