# Mini Challenge: Numbers divisible by 5 but not by 10

num = [10, 15, 20, 25, 30, 35, 40]

i = 0
while i <= len(num) - 1:
    if num[i] % 5 == 0 and num[i] % 10 != 0:
        i += 1
    else:
        del num[i]   
print(num)

'''
Output: 

[15, 25, 35]
'''
