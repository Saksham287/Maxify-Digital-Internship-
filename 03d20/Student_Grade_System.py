# Student Pass/Fail System

grades = [35, 67, 80, 20]

for i, x in enumerate(grades, start= 1):
    if x >= 40:
        print("Student", i, ':', "Pass")
        
    else: 
        print("Student", i, ':', "Fail")

'''
Output:
Student 1 : Fail
Student 2 : Pass
Student 3 : Pass
Student 4 : Fail
'''
