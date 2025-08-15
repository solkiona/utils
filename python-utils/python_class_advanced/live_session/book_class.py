#SOLUTION TO PROBLEM 1


class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed = 0
        self.available = copies - self.borrowed
    
    
    def borrow(self, qty):
        if qty <= self.available:
            self.borrowed += qty
            self.available -= qty
            print(f"You borrowed {qty} copies of '{self.title}'. {self.available} copies available.")
            return f"You borrowed {qty} copies of '{self.title}'. {self.available} copies available"
        else:
            print(f"Sorry only {self.available} copies of '{self.title}' are available.")
            return f"Sorry you can't borrow more than avaialble copies of {self.title}"
    
    
    def return_book(self, qty):
        if qty <= self.borrowed:
            self.borrowed -= qty
            self.available += qty
            print(f"{qty} copy(ies) of '{self.title}' returned. {self.borrowed} remaining")
            return f"{qty} copy(ies) of '{self.title}' returned. "
        elif self.borrowed == 0:
            print(f"All copies of '{self.title}' returned.")
            return f"All copies of '{self.title}' returned."
        else:
            print(f"Sorry you can't return more than you borrowed")
            return f"Sorry you can't return more than you borrowed"


book = Book("Python Basics", "John Doe", 30)

book.borrow(10)
book.return_book(3)



class BankAccount:
    def __init__(self,account_name, balance=0):
        self.account_name = account_name
        self.balance = balance
        
    def __str__(self):
        return f"Account Name: {self.account_name}, Balance: {self.balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."
    
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Amount must be greater than 0."
        else:
            return "Insufficient funds."


account = BankAccount("John Doe", 1000)
print(account)
print(account.deposit(500))
print(account)
print(account.withdraw(200))
print(account)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        return f"Hello, my name is {self.name}"

class Student(Person):
    def __init__(self, school, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.school = school
        
        
    
    def study(self):
        return f"{self.name} is studying at {self.school}"

student1 = Student("XYZ University", "Bob", 20)
print(student1.study())