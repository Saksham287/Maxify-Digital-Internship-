# Palindrome check function

def is_palindrome(s):
    print(s == s[::-1])

is_palindrome("madam")          # True
is_palindrome("eye")            # True
is_palindrome("level")          # True
is_palindrome("home")           # False