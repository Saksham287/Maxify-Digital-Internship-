# Sets 

mySet = {"apple", "banana", "cherry", "apple"}

print(mySet)    # Output: {'apple', 'cherry', 'banana'}
# Sets don't allows duplicates, after the first occurrence second one is ignored

set2 = {True, 1, 2} 

print(set2)    # Output: {True, 2}
# Sets also sees 1 and True as same and, 0 and false as same

print(len(mySet))   # Output: 3

for x in mySet:
    print(x)
    
print("banana" in mySet)
print("banana" not in mySet)

mySet.add("Orange")
print(mySet)

set3 = {"pineapple", "mango", "papaya"}

mySet.update(set3)

print(mySet)

mySet.remove("papaya")
print(mySet)

mySet.discard("Berry")

mySet.pop()     # When you use pop in sets, there is no control over what will be removed
print(mySet)



set4 = {1, 2, 3, 4}
set5 = {"Alex", "john", "Ben"}
set6 = {"banana", "apple", "mango"}

#set7 = set4.union(set5)
set7 = set4 | set5 | set6 
print(set7)

'''
Entire Output:

{'apple', 'banana', 'cherry'}
{True, 2}
3
apple
banana
cherry
True
False
{'Orange', 'apple', 'banana', 'cherry'}
{'papaya', 'cherry', 'pineapple', 'Orange', 'apple', 'mango', 'banana'}
{'cherry', 'pineapple', 'Orange', 'apple', 'mango', 'banana'}
{'pineapple', 'Orange', 'apple', 'mango', 'banana'}
{1, 2, 3, 4, 'mango', 'apple', 'banana', 'john', 'Ben', 'Alex'}

'''