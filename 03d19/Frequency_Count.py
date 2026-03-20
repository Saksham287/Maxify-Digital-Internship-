# Count Frequency of Elements

num = [1, 2, 2, 3, 3, 3]

for x in set(num):      # turns into set
    count = 0
    for n in num:       # compares the set elements to he list 
        if n == x:      # if equal it will add to count 
            count += 1
    print(x, ":", count)
    
'''
Output:

1 : 1
2 : 2
3 : 3
'''
