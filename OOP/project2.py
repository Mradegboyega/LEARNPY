# Define a general 'Account' class
class Account:
    def __init__(self, account_number, account_type, balance, account_holder) -> None:
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number
    
    def get_account_type(self):
        return self.account_type
    
    def get_account_details(self):
        return {
            "Account Name": self.account_holder,
            "Account Type": self.account_type,
            "Account Number": self.account_number,
            "Account Balance": self.balance
        }

# Define a 'SavingsAccount' class that inherits from 'Account'
class SavingsAccount(Account):

    def get_account_details(self):
        details = super().get_account_details()  # Use super() to call the parent class method
        details["More"] = "Personal account"
        return details

# Define a 'CurrentAccount' class that inherits from 'Account'
class CurrentAccount(Account):

    def get_account_details(self):
        details = super().get_account_details()  # Use super() to call the parent class method
        details["More"] = "Account for businesses"
        return details

# Create an instance of the 'SavingsAccount' class
toyin = SavingsAccount(565327, "Savings Account", 2000000, "Toyin Ademola")

# Perform transactions on the account

toyin.deposit(500000)
# toyin.deposit(100000)
# toyin.deposit(50000)

# print(toyin.get_balance())

toyin.withdraw(5000)

print(toyin.get_balance())
print(toyin.get_account_details())

# Create an instance of the 'CurrentAccount' class
mary = CurrentAccount(9988732, "Current", 60000, "Mary Ademola")
print(mary.get_balance())
print(mary.get_account_details())
