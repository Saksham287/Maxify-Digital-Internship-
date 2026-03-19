# Types of Naming Conventions

'''

1. Camel Case (camelCase)
- First word lowercase, next words uppercase
- No spaces
Examples: studentName, totalMarks, getUserData
Used in: Java, JavaScript, C++

2. Pascal Case (PascalCase)
- Every word starts with uppercase
- No spaces
Examples: StudentName, TotalMarks, GetUserData
Used in: Class names (Java, C#, Python)

3. Snake Case (snake_case)
- All lowercase
- Words separated by underscore (_)
Examples: student_name, total_marks, get_user_data
Used in: Python

4. Upper Snake Case (UPPER_SNAKE_CASE)
- All uppercase
- Words separated by underscore (_)
Examples: MAX_SIZE, PI_VALUE, TOTAL_USERS
Used in: Constants

5. Kebab Case (kebab-case)
- All lowercase
- Words separated by hyphen (-)
Examples: student-name, total-marks, get-user-data
Used in: URLs, CSS classes, file names

6. Hungarian Notation
- Prefix indicates type or purpose
Examples: strName (string), iCount (integer), btnSubmit (button)
Note: Older style, rarely used today

7. Flat Case (flatcase)
- All lowercase, no separators
Examples: studentname, totalmarks
Note: Rarely used

'''

# Python Naming Conventions

'''

1. VARIABLE NAMES
- Use snake_case (lowercase with underscores)
Examples: student_name, total_marks, user_age

2. FUNCTION NAMES
- Use snake_case
Examples: calculate_total(), get_user_data(), print_result()

3. CLASS NAMES
- Use PascalCase (CapWords)
Examples: StudentData, BankAccount, EmployeeRecord

4. CONSTANTS
- Use UPPER_SNAKE_CASE
Examples: MAX_VALUE, PI, TOTAL_USERS

5. MODULE (FILE) NAMES
- Use lowercase, underscores allowed
Examples: math_utils.py, data_analysis.py

6. PACKAGE NAMES
- Use short lowercase names (avoid underscores if possible)
Examples: numpy, pandas

7. PRIVATE VARIABLES / METHODS
- Use single underscore (_) prefix
Examples: _hidden_value, _private_method()

8. STRONG PRIVATE (NAME MANGLING)
- Use double underscore (__) prefix
Examples: __secret_value

9. SPECIAL (MAGIC) METHODS
- Use double underscore before and after
Examples: __init__, __str__, __len__

QUICK SUMMARY
snake_case -> variables/functions
PascalCase -> classes
UPPER_SNAKE_CASE -> constants
lowercase -> modules/packages
_single _ -> private
__double__ -> magic methods

'''
