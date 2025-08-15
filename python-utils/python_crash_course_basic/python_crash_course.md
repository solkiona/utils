# Python Crash Course

## Introduction
Python is a powerful, high-level, and easy-to-read programming language. This crash course will cover the basics of Python, including syntax, data types, control structures, functions, and more.

## Table of Contents

### Section 1: Python Basics
1. [Installing Python](#installing-python)
2. [Hello World](#hello-world)
3. [Variables and Data Types](#variables-and-data-types)
4. [Operators](#operators)
5. [Control Flow](#control-flow)
6. [Functions](#functions)
7. [Lists, Tuples, and Dictionaries](#lists-tuples-and-dictionaries)
8. [Loops](#loops)
9. [File Handling](#file-handling)

### Section 2: Advanced Python
10. [Object-Oriented Programming](#object-oriented-programming)
11. [Modules and Packages](#modules-and-packages)

---

# Section 1: Python Basics

## Installing Python
Download and install Python from [python.org](https://www.python.org/downloads/).
Verify installation:
```sh
python --version  # or python3 --version
```

## Hello World
```python
print("Hello, World!")
```

## Variables and Data Types
### Numeric Types
```python
x = 10  # Integer
y = 3.14  # Float
z = 2 + 3j  # Complex number
```
### Numeric Methods
```python
print(abs(-10))  # 10
print(round(3.14159, 2))  # 3.14
print(int(3.7))  # 3
print(float(7))  # 7.0
```

### String Type
```python
name = "John Doe"
print(name.upper())  # JOHN DOE
print(name.lower())  # john doe
print(name.title())  # John Doe
print(name.replace("John", "Jane"))  # Jane Doe
```
### String Methods
```python
print("hello".capitalize())  # Hello
print("hello world".split())  # ['hello', 'world']
print("-".join(["apple", "banana", "cherry"]))  # apple-banana-cherry
print("hello world".startswith("hello"))  # True
print("hello world".endswith("world"))  # True
```

### Boolean Type
```python
is_student = True
is_graduated = False
print(is_student and is_graduated)  # False
print(is_student or is_graduated)  # True
print(not is_student)  # False
```

### List (Mutable, Ordered)
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)  # ['apple', 'banana', 'cherry', 'mango']
```
### List Methods
```python
fruits.insert(1, "orange")  # Insert at index 1
fruits.remove("banana")  # Remove an element
print(fruits.index("mango"))  # Find index
print(fruits.count("apple"))  # Count occurrences
fruits.sort()
print(fruits)  # Sorted list
```

### Tuple (Immutable, Ordered)
```python
coordinates = (10.0, 20.0, 30.0)
print(coordinates[1])  # 20.0
```
### Tuple Methods
```python
tuple1 = (1, 2, 3, 4, 1, 2)
print(tuple1.count(1))  # Count occurrences of 1
print(tuple1.index(3))  # Find index of element
```

### Dictionary (Key-Value Pairs, Mutable)
```python
person = {"name": "Alice", "age": 30}
person["city"] = "New York"
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
```
### Dictionary Methods
```python
print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
```

## Operators
```python
x = 10
y = 3
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x // y) # Floor Division
print(x ** y) # Exponentiation
print(x % y)  # Modulus
```

## Control Flow
### If-Else Statements
```python
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

## Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## Loops
### For Loop
```python
for i in range(5):
    print(i)
```
### While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## File Handling
```python
# Writing to a file
with open("test.txt", "w") as file:
    file.write("Hello, file!")

# Reading from a file
with open("test.txt", "r") as file:
    print(file.read())
```

---

# Section 2: Advanced Python

## Object-Oriented Programming
### Classes and Objects
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

person1 = Person("Alice", 25)
print(person1.greet())
```

### Inheritance
```python
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def study(self):
        return f"{self.name} studies at {self.school}."

student1 = Student("Bob", 20, "XYZ University")
print(student1.study())
```

## Modules and Packages
### Importing Modules
```python
import math
print(math.sqrt(16))  # 4.0
```

### Creating a Module
Create a file `mymodule.py`:
```python
def hello():
    return "Hello from mymodule!"
```

Import and use it:
```python
import mymodule
print(mymodule.hello())
```

### Installing External Packages
Use `pip` to install packages:
```sh
pip install requests
```
Use the installed package:
```python
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

---

## Conclusion
This crash course provides an introduction to Python fundamentals. Keep practicing and explore more advanced topics like web development, data science, and automation!
