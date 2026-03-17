#For Loop, Breaks & continue

colors = ["Red", "Black", "Green", "Brown", "Yellow", "Blue"]
for x in colors:
    print(x)
'''
Output:

Red
Black
Green
Brown
Yellow
Blue

'''

n = input("Enter any color from the list: ")
for x in colors:
    if x == n:
        break                                   # break: Stops the loop and execute everything till the break
    print(x)
'''
Output:

Enter any color from the list: Brown
Red
Black
Green

'''

    
m = input("Enter any color from the list: ")    
for x in colors: 
    if x == m:
        continue                                # continue: The loop continues and leaves the color that comes to be true 
    print(x)
'''
output:

Enter any color from the list: Brown
Red
Black
Green
Yellow
Blue

'''

'''
Entire Output:

Red
Black
Green
Brown
Yellow
Blue
Enter any color from the list: Brown
Red
Black
Green
Enter any color from the list: Brown
Red
Black
Green
Yellow
Blue

'''
