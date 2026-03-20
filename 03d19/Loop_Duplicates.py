# Remove Duplicates from List

num = [1, 2, 2, 3, 4, 4, 5]

# Changing into the set to remove duplicates
set_dupl_remv = list(set(num))
print(set_dupl_remv)    # Output: [1, 2, 3, 4, 5]

# Loop and If 
loop_dupl_remv = []
i = 0
while i < len(num):
    if num[i] not in loop_dupl_remv:
        loop_dupl_remv.append(num[i])
    else:
        i += 1
print(loop_dupl_remv)

'''
Output:

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

'''
