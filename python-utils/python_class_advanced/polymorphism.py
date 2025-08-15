""" 
Polymorphism (Method Overriding & Method Overloading)

Polymorphism allows the same method name to work differently for different classes.

🔹 Method Overriding (Changing Behavior in Subclasses)
"""


class LibraryItem:
    def get_details(self):
        print("This is a library item.")
        return("This is a library item")


class Book(LibraryItem):
    def get_details(self):
        print("This is a book.")

class DVD(LibraryItem):
    
    def get_details(self):
        top = super().get_details()
        print(f"{top}, Actually, this is a DVD Class")
        # print("This is a DVD.")

class Journal(LibraryItem):
    def get_details(self):
        print("This is a journal")

items = [Book(), DVD(), Journal()]

for item in items:
    item.get_details()

