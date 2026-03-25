# factorial Function

def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    print("Factorial of", n, "is", fact)

factorial(8)    # Output: Factorial of 8 is 40320     
factorial(4)    # Output: Factorial of 4 is 24 

'''
8! = 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 = 40320
4! = 1 x 2 x 3 x 4 = 24
'''
