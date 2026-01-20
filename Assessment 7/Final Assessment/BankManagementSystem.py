class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display(self):
        print("\nAccount Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


accounts = {}

while True:
    print("\n--- Bank Management System ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        acc_no = int(input("Enter Account Number: "))
        name = input("Enter Account Holder Name: ")
        balance = int(input("Enter Initial Balance: "))
        accounts[acc_no] = BankAccount(acc_no, name, balance)
        print("Account created successfully.")

    elif choice == 2:
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            amount = int(input("Enter amount to deposit: "))
            accounts[acc_no].deposit(amount)
        else:
            print("Account not found.")

    elif choice == 3:
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            amount = int(input("Enter amount to withdraw: "))
            accounts[acc_no].withdraw(amount)
        else:
            print("Account not found.")

    elif choice == 4:
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            accounts[acc_no].display()
        else:
            print("Account not found.")

    elif choice == 5:
        print("Thank you for using Bank Management System.")
        break

    else:
        print("Invalid choice. Try again.")
