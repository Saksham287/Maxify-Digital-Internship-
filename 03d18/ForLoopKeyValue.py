# For Loops: Iterating over dictionaries using key-value pairs
student = {
    "Name": "Alex",
    "Age": 21,
    "Grade": "A"    
}

for key, value in student.items():
    print(f"{key} : {value}")
'''
Output: 

Name : Alex
Age : 21
Grade : A

'''

prices = {
    "Apple": 2,
    "Banana": 1,
    "Orange": 3
}
totalPrice = 0

for values in prices.values():
    totalPrice += values
print("Total Price: $",totalPrice) # Output: Total Price: $6

marks = {
    "Math": 85,
    "Science": 72,
    "English": 90,
    "History": 65
}

for key, value in marks.items():
    if value >= 80:
        print(f"{key} {value}")

'''
Output: 

Math 85
English 90
'''
