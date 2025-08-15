# Python Advanced Tasks

## 1. Classes
### Task 1: Library Management System
**Problem Statement:**
You're building a library system where users can borrow and return books. Ensure books have a title, author, and available copies. Users should be able to borrow a book if copies are available and return them incrementally.

**Task:**
Create a `Book` class with:
- `title`, `author`, and `copies` attributes.
- A `borrow(qty)` method that reduces the available copies if enough are available.
- A `return_book(qty)` method to allow partial returns.

**Expected Output:**
```python
book = Book("Python Basics", "John Doe", 3)
print(book.borrow(2))  # "You borrowed 2 copies of 'Python Basics'. 1 copies remaining."
print(book.return_book(1))  # "1 copies of 'Python Basics' returned."
```

### Task 2: Employee Record System
**Problem Statement:**
You are managing employee records. Employees have a name, ID, and department. They should be able to update their department and view details.

**Task:**
Create an `Employee` class with:
- `name`, `id`, and `department` attributes.
- An `update_department(new_department)` method.
- A `get_details()` method.

**Expected Output:**
```python
emp = Employee("Alice", 101, "HR")
emp.update_department("IT")
print(emp.get_details())  # "Alice (ID: 101) - IT"
```

---

## 2. Inheritance
### Task 1: Vehicle Hierarchy
**Problem Statement:**
You want to model a `Vehicle` system where `Car` inherits from `Vehicle` and has a fuel type.

**Task:**
Create:
- A `Vehicle` class with `brand` and `model`.
- A `Car` subclass that adds `fuel_type` and overrides a method to include this.

**Expected Output:**
```python
car = Car("Toyota", "Camry", "Petrol")
print(car.get_details())  # "Toyota Camry runs on Petrol."
```

### Task 2: Banking System
**Problem Statement:**
You need to add a `SavingsAccount` subclass that adds an interest rate to a `BankAccount` class.

**Task:**
- Create a `BankAccount` class.
- Create a `SavingsAccount` subclass with `interest_rate` and a method to calculate interest.

**Expected Output:**
```python
savings = SavingsAccount("John Doe", 1000, 5)
print(savings.calculate_interest())  # "Interest: $50"
```

---

## 3. Encapsulation
### Task 1: Secure Bank Account
**Problem Statement:**
You want to prevent users from directly modifying the balance of their bank account.

**Task:**
- Create a `BankAccount` class with a private `__balance` attribute.
- Provide getter and setter methods for secure access.
- Implement `deposit(amount)` and `withdraw(amount)` methods.

**Expected Output:**
```python
account = BankAccount("Alice", 500)
account.deposit(200)  # "Deposited successfully."
print(account.get_balance())  # "Balance: $700"
```

---

## 4. Polymorphism
### Task 1: Payment Processing
**Problem Statement:**
You are implementing a payment system where different payment methods are handled differently.

**Task:**
- Create a `Payment` base class.
- Implement `CreditCardPayment` and `PayPalPayment` subclasses with different `process()` methods.

**Expected Output:**
```python
payment = PayPalPayment()
payment.process()  # "Processing PayPal payment."
```

---

## 5. Abstract Classes
### Task 1: Employee Payroll
**Problem Statement:**
Ensure every employee subclass implements a salary calculation method.

**Task:**
- Create an abstract `Employee` class with `calculate_salary()` as an abstract method.
- Implement `Manager` and `Developer` subclasses with specific salary calculations.

**Expected Output:**
```python
manager = Manager("John", 5000)
print(manager.calculate_salary())  # "Salary: $5000"
```

---

## 6. Magic Methods
### Task 1: Fraction Addition
**Problem Statement:**
You want to implement the addition of fractions using magic methods.

**Task:**
- Create a `Fraction` class with `__add__` to add two fractions.
- Implement a `__str__` method for easy printing.

**Expected Output:**
```python
frac1 = Fraction(1, 2)
frac2 = Fraction(1, 3)
print(frac1 + frac2)  # "5/6"
```
