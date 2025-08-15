""" 
🔹 Encapsulation Exercise: Bank System Simulation
Problem Statement:
You're building a simple bank system where users can deposit, withdraw, and check their balance. However, you want to ensure:
✅ Deposits are always positive.
✅ Withdrawals do not exceed the current balance.
✅ Users cannot modify the balance directly.

Task:
Create a BankAccount class with:

A private attribute __balance

A getter method to view the balance

A setter method to ensure balance updates follow the rules

A deposit(amount) method

A withdraw(amount) method

Implement encapsulation properly to prevent direct access and enforce these rules.

Expected Behavior:

account = BankAccount("Alice", 1000)

print(account.balance)   # ✅ Output: 1000

account.deposit(500)     # ✅ Deposited successfully
print(account.balance)   # ✅ Output: 1500

account.withdraw(700)    # ✅ Withdrawal successful
print(account.balance)   # ✅ Output: 800

account.withdraw(2000)   # ❌ Insufficient funds!

account.balance = 5000   # ❌ Should not allow direct modification!
🔹 Your Task
✅ Implement the BankAccount class following the rules.
✅ Test it using different cases.
✅ Ensure direct modification of balance is restricted.
"""


class BankAccount:
    def __init__(self, name, balance):
        
        self.name = name
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, amount):
        print(" ❌ Direct modification of balance is not allowed")
    def __str__(self):
        return f"Account Holder: {self.name}, Balance: {self.__balance}"
    
    
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"{amount} deposited successfully. New balance: {self.__balance}"
        else:
            print("Deposit amount must be positive")
            raise ValueError("Deposit amount must be positive")
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"{amount} withdrawn successfully. New balance: {self.__balance}"
        else:
            print("Insufficient funds!")


account = BankAccount("Alice", 1000)

# print(account.balance)   # ✅ Output: 1000

# account.deposit(500)     # ✅ Deposited successfully
# print(account.balance)   # ✅ Output: 1500

# account.withdraw(700)    # ✅ Withdrawal successful
# print(account.balance)   # ✅ Output: 800

# account.withdraw(2000)   # ❌ Insufficient funds!

account.balance = 5000   # ❌ Should not allow direct modification!
print(account.balance)
print(account)