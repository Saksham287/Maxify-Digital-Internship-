#Print numbers from 1 to 20

choice = str(input("Choose one loop method (While or For):"))

if choice == "For": 
    for x in range(20):      # For loop to print the numbers 
        print(x + 1) 
elif choice == "While":
    i = 1
    while i <= 20:           # While loop to print the numbers 
        print(i)
        i += 1
else: 
    print("ERROR")
    
''' 
Output:

Choose one loop method (While or For):While
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

'''