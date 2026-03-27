# Create a simple expense tracker

transactions = [1000, -200, 300, -150, -50, 500]

# Total income:
def income(transactions):
    total_income = 0
    for i in transactions:
        if i >= 0:
            total_income += i
    return(f"Total Income: ${total_income}\n")

# Total Expense:
def expense(transactions):
    total_expense = 0
    for e in transactions:
        if e <= 0:
            total_expense -= (e)
    return(f"Total Expense: -${total_expense}\n")
    
# Net Balance:
def net(transactions):
    net_balance = 0
    for b in transactions:
        net_balance += b
    return(f"Net Balance: ${net_balance}\n")

#income(transactions)            # Output: Total Income: $1800
#expense(transactions)           # Output: Total Expense: -$400
#net(transactions)               # Output: Net Balance: $1400 

with open("Expense.txt", "w") as file:
    file.write(income(transactions))
    file.write(expense(transactions))
    file.write(net(transactions))
    
with open("Expense.txt", "r") as file:
    print(file.read())

'''
Output:

Total Income: $1800
Total Expense: -$400
Net Balance: $1400
'''
