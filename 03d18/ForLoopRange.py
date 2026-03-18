# For Loops: Using Range

for x in range(6):          # Default value for x is 0. The range function is between 0 to 6 but not including 6. 
                            # Therefore 0 to 5 will be the values that will be printed.
    print(x)
'''
Output:

0
1
2
3
4
5

'''

for x in range(2, 6):       # This range function means x is between 2 to 6, but not including 6.
                            # Therefore the values will be 2 to 5 that will be printed.
    print(x)
'''
Output:

2
3
4
5

'''

for x in range(2, 20, 4):   # This range function means that x is between 2 to 20 but not including 20.
                            # It also has a third parameter that indicates the increments between numbers.
                            # Therefore, in this scenario it will print 2 to 19.
    print(x)
'''
Output:

2
6
10
14
18

'''
