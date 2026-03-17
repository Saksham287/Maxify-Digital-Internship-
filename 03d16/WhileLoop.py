#While Loops

i = 1
while i <= 7:                   # loops until i reaches 8, the statement becomes false and loop ends
    print(i)
    i = i + 1
'''
Output:

1
2
3
4
5
6
7

'''

i = 1
n = int(input("Enter number between 1-20: "))
while i <= 20:
    if i == n:
        print("We found your number", n)
        break
    else:
        print(i)
        i += 1
'''
Output:

Enter number between 1-20: 15
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
We found your number 15

'''
