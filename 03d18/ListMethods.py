# List: Methods (append, remove, pop, sort)

firstList = ["Red", "Black", "Green", "Brown", "Yellow", "Blue"]
print(firstList)
# Output: ['Red', 'Black', 'Green', 'Brown', 'Yellow', 'Blue']

firstList[0] = "Maroon"     # This will change index 0 (Red) to 'Maroon'
print(firstList)
# Output: ['Maroon', 'Black', 'Green', 'Brown', 'Yellow', 'Blue']

firstList.insert(1, "Red")  # This we are inserting item at index 1
print(firstList)
# Output: ['Maroon', 'Red', 'Black', 'Green', 'Brown', 'Yellow', 'Blue']

firstList.append("Orange")  # This by default add item to the end of the list
print(firstList)
# Output: ['Maroon', 'Red', 'Black', 'Green', 'Brown', 'Yellow', 'Blue', 'Orange']

moreColors = ["Sky Blue", "Dark Green", "Purple"]
firstList.extend(moreColors)    # This adds another list/tuple to the existing list
print(firstList)
# Output: ['Maroon', 'Red', 'Black', 'Green', 'Brown', 'Yellow', 'Blue', 'Orange', 'Sky Blue', 'Dark Green', 'Purple']

firstList.remove("Sky Blue")    # Removes the item that is specified. If multiple it removes the first occurrence 
print(firstList)    
# Output: ['Maroon', 'Red', 'Black', 'Green', 'Brown', 'Yellow', 'Blue', 'Orange', 'Dark Green', 'Purple']

firstList.pop(8)    # This removes the specific index mentioned
print(firstList)
# Output: ['Maroon', 'Red', 'Black', 'Green', 'Brown', 'Yellow', 'Blue', 'Orange', 'Purple']

firstList.pop()     # This removes the last item by default
print(firstList)
# Output: ['Maroon', 'Red', 'Black', 'Green', 'Brown', 'Yellow', 'Blue', 'Orange']

firstList.sort()    # This will sort the list alphabetically by default in A-Z.
print(firstList)
#Output: ['Black', 'Blue', 'Brown', 'Green', 'Maroon', 'Orange', 'Red', 'Yellow']

firstList.sort(reverse= True)   # This will reverse the sorting to Z-A
print(firstList)
#Output: ['Yellow', 'Red', 'Orange', 'Maroon', 'Green', 'Brown', 'Blue', 'Black']