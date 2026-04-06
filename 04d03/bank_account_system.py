import sqlite3


class BankAccount:
    def __init__(self, db_name="bank.db"):                  # Creating Database 
        self.db_name = db_name
        self.create_tables()

    def connect(self):                                      # Connecting to the Database 
        return sqlite3.connect(self.db_name)

    def create_tables(self):                                # Creating a Table in a Database 
        conn = self.connect()
        cursor = conn.cursor()

        # Accounts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_number INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                balance REAL NOT NULL
            )
        """)

        # Transactions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                amount REAL NOT NULL,
                transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_number) REFERENCES accounts(account_number)
            )
        """)

        conn.commit()
        conn.close()

    def create_account(self, name, address, balance):           # Creating Customer Account 
        if balance < 0:
            print("Initial balance cannot be negative.")
            return

        conn = self.connect()
        cursor = conn.cursor()
        
        # Adding account to Table 
        cursor.execute("""
            INSERT INTO accounts (name, address, balance)
            VALUES (?, ?, ?)
        """, (name, address, balance))

        conn.commit()
        conn.close()

        print(f"Account created successfully for {name} with balance {balance}.")

    def view_accounts(self):                        # How to view accounts from the Database 
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM accounts")
        accounts = cursor.fetchall()

        conn.close()

        if not accounts:
            print("No accounts found.")
            return

        print("\n--- Account Records ---")
        for account in accounts:
            print(f"Account No: {account[0]}, Name: {account[1]}, Address: {account[2]}, Balance: {account[3]}")
        print()

    def deposit(self, account_number, amount):                  # Making a deposit into the Database
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        account = cursor.fetchone()

        if account is None:
            print("Account not found.")
            conn.close()
            return

        new_balance = account[0] + amount

        # Insert credit transaction
        cursor.execute("""
            INSERT INTO transactions (account_number, transaction_type, amount)
            VALUES (?, ?, ?)
        """, (account_number, "credit", amount))

        # Update balance in accounts table
        cursor.execute("""
            UPDATE accounts
            SET balance = ?
            WHERE account_number = ?
        """, (new_balance, account_number))

        conn.commit()
        conn.close()

        print(f"Deposited {amount} into account {account_number}. New balance: {new_balance}")

    def withdraw(self, account_number, amount):              # Taking money out of account 
        if amount <= 0:
            print("Withdraw amount must be greater than 0.")
            return

        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        account = cursor.fetchone()

        if account is None:
            print("Account not found.")
            conn.close()
            return

        current_balance = account[0]

        if amount > current_balance:
            print("Insufficient funds.")
            conn.close()
            return

        new_balance = current_balance - amount

        # Insert debit transaction
        cursor.execute("""
            INSERT INTO transactions (account_number, transaction_type, amount)
            VALUES (?, ?, ?)
        """, (account_number, "debit", amount))

        # Update balance in accounts table
        cursor.execute("""
            UPDATE accounts
            SET balance = ?
            WHERE account_number = ?
        """, (new_balance, account_number))

        conn.commit()
        conn.close()

        print(f"Withdrew {amount} from account {account_number}. New balance: {new_balance}")

    def view_transactions(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()

        conn.close()

        if not transactions:
            print("No transactions found.")
            return

        print("\n--- Transaction Records ---")
        for transaction in transactions:
            print(
                f"Transaction ID: {transaction[0]}, "
                f"Account No: {transaction[1]}, "
                f"Type: {transaction[2]}, "
                f"Amount: {transaction[3]}, "
                f"Date: {transaction[4]}"
            )
        print()

    def delete_account(self, account_number):                   # Delete an existing account 
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
        account = cursor.fetchone()

        if account is None:
            print("Account not found.")
            conn.close()
            return

        # Delete related transactions first
        cursor.execute("DELETE FROM transactions WHERE account_number = ?", (account_number,))

        # Delete account
        cursor.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))

        conn.commit()
        conn.close()

        print(f"Account {account_number} deleted successfully.")


# Main program
if __name__ == "__main__":
    bank = BankAccount()

    
    bank.create_account("John", "New York", 1000)
    bank.create_account("Ben", "Westbury", 500)
    bank.create_account("Drew", "Jericho", 120000)

    bank.view_accounts()

    bank.deposit(1, 300)

    bank.withdraw(2, 200)
    
    bank.withdraw(3, 78328)

    bank.view_transactions()

    bank.delete_account(1)
    
    bank.deposit(3, 40000)

    bank.view_accounts()

    bank.view_transactions()