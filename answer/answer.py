class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # Function for deposit
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited. \nNew balance is: {self.balance}")

    # Function for withdrawal
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn. \nNew balance is: {self.balance}")

# Taking input from the user for account details
owner_name = input("Enter the owner's name: ")
initial_balance = float(input("Enter the initial balance: "))  # Using float to allow decimal amounts

# Create a BankAccount instance with the provided details
account = BankAccount(owner_name, initial_balance)

# Display current balance
print(f"\nAccount created for {account.owner} with an initial balance of {account.balance}")

# Ask for deposit and withdrawal amounts
deposit_amount = float(input("\nEnter the amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("\nEnter the amount to withdraw: "))
account.withdraw(withdraw_amount)
