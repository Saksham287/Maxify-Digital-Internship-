# For loops: nested loops

for i in range(1, 6):
    for j in range(i):
        print('*', end= " ")
    print()
'''
Output:

* 
* * 
* * * 
* * * * 
* * * * * 

'''

for i in range(1, 11):
    for j in range(11 - i):
        print(" ", end= " ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
'''
Output: 

                    * 
                  * * * 
                * * * * * 
              * * * * * * * 
            * * * * * * * * * 
          * * * * * * * * * * * 
        * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * * 
  
'''
