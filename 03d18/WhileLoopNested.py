# While loops: Nested loops

i = 1
while i <= 6:
    j = 1
    while j <= 6 - i:
        print(" ", end=" ")
        j += 1
    k = 1
    while k <= (2 * i - 1):
        print("*", end=" ")
        k += 1
    
    print()
    i += 1
'''
Output:

          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * *

'''

a = 1 

while a <= 6:
    b = 1
    while b <= a:
        print(b, end=" ")
        b += 1
    print()
    a += 1
'''
Output:

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6

'''