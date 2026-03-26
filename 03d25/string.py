# String

s = "Hello, World!"
print(len(s))                                   # Output: 13

# String Slicing 
print(s[2 : 5])                                 # Output: llo
print(s[: 4])                                   # Output: Hell
print(s[4 :])                                   # Output: o, World!
print(s[-5 : -2])                               # Output: orl
print(s[-4: ])                                  # Output: rld!
print(s[: -4])                                  # Output: Hello, Wo

# Upper Case 
print(s.upper())                                # Output: HELLO, WORLD!

a = "i am learning python"
print(a.upper())                                # Output: I AM LEARNING PYTHON

# Lower Case
b = "I LOVE FOOD"
print(b.lower())                                # Output: i love food

# Replacing String
print(b.replace("I", "We"))                     # Output: We LOVE FOOD

# Split String
c = s.split(",")
print(c)                                        # Output: ['Hello', ' World!']

# String Concatenation
d = "Hello"
e = "World"
f = d + e
print(f)                                        # Output: HelloWorld
g = d + " " + e + "!"
print(g)                                        # Output: Hello World!

# f-String 
age = 15
txt = f"I'm {age} old. I was born {age} years ago."
print(txt)                                      # Output: I'm 15 old. I was born 15 years ago.

# Placeholders and Modifiers
price = 118
txt2 = f"The price is ${price:.2f}"              
print(txt2)                                     # Output: The price is $118.00
txt3 = f"The price is ${15 * 2}"
print(txt3)                                     # Output: The price is $30