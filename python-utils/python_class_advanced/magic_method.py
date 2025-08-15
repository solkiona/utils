""" 

Dunder (Magic) Methods in Python
Dunder (double underscore) methods allow you to customize built-in behavior.  


🔹 Example: __str__ and __len__

"""


class Book:
    def __init__(self, title, copies):
        self.title = title
        self.copies = copies
        
    def __str__(self):
        return f"{self.title} ({self.copies} copies) available"
    
    def __len__(self):
        return self.copies
    
    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", self.copies + other.copies)


book = Book("Python Mastery", 5)
print(book)
print(len(book))

book2 = Book("Oliver Twist", 10)

print(book + book2)  # Using the __add__ method



""" 
🔹 Common Magic Methods

Method	        Purpose
__str__	        Defines how the object prints (print(obj))
__len__	        Defines how len(obj) behaves
__eq__	        Custom equality check (==)
__add__	        Custom addition (+)
__getitem__	    Allows obj[index]


"""