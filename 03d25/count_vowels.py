# Count vowels in a string

txt = "Hello, my name is John and I love to eat Pizza. Do you like pizza?"

a = txt.count("a")
e = txt.count("e")
i = txt.count("i")
o = txt.count("o")
u = txt.count("u")
    
print(f"a:{a} \ne:{e} \ni:{i} \no:{o} \nu:{u}")
print(f"Total Vowels: {a + e + i + o + u}")
'''
Output: 

a:5 
e:5 
i:4 
o:6 
u:1
Total Vowels: 21
'''