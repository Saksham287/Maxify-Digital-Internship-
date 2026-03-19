# Remove duplicate numbers from the list

num = [1, 2, 3, 4, 5, 1, 4, 6, 8, 3, 3, 2, 6, 7, 8, 9, 0]
print(num)
# Output: [1, 2, 3, 4, 5, 1, 4, 6, 8, 3, 3, 2, 6, 7, 8, 9, 0]

num.sort()
print(num)
# Output: [0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]

i = 0
while i <= len(num):
    j = i + 1
    while j <= len(num) - 1:
        if num[i] == num[j]:
            num.pop(j)
        else:
            j += 1
    i += 1
print(num)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
