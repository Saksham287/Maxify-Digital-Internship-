# Create a Bank Account System using class

class BankAccount: 
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")                # Added if-else after online search 
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance. Cannot withdraw.")
        else: 
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount}")
            print(f"${amount} withdrawn successfully.")
    
    def display_balance(self):
        print(f"{self.account_holder}'s Current Balance: ${self.balance}")
    
    def save_transactions(self):
        with open("bank.txt", "w") as file:
            file.write(f"Account Holder: {self.account_holder}\n")
            file.write("Transaction History:\n")
            for x in self.transactions:
                file.write(x + "\n")


account1 = BankAccount("John", 1000)

account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.deposit(758)
account1.deposit(0)
account1.withdraw(1)
account1.withdraw(2100)
account1.withdraw(57)
account1.display_balance()
account1.save_transactions()

'''
Output:

John's Current Balance: $1000
$500 deposited successfully.
$200 withdrawn successfully.
$758 deposited successfully.
Invalid deposit amount.
$1 withdrawn successfully.
Insufficient balance. Cannot withdraw.
$57 withdrawn successfully.
John's Current Balance: $2000
'''
