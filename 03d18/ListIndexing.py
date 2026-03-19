# List: Indexing 

firstList = ["Red", "Black", "Green", "Brown", "Yellow", "Blue"]

print("Number of items:", len(firstList))
print(firstList[1])     # List first item index is default 0. Index 1 will print 'Black'.
print(firstList[-2])    # Negative index means counting from the back. This call means second from the last.
print(firstList[2:4])   # Ratio is same as giving a range to the list. This means between 2 to 4 index.
                        # But in this case index 2 is included and index 4 is not. 
print(firstList[:3])    # In this case the default start is 0 and its till index 3.
print(firstList[3:])    # In this case the list will print from index 3 to end.

if "Blue" in firstList:
    print("Found it")
else:
    print("Blue not found")
'''
Output: 

Number of items: 6
Black
Yellow
['Green', 'Brown']
['Red', 'Black', 'Green']
['Brown', 'Yellow', 'Blue']
Found it

'''
