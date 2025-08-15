from abc import ABC, abstractmethod


"""

    Abstract Class in Python
    
    🔹 Why Use Abstract Classes?
An abstract class in Python is a class that cannot be instantiated directly and is used to enforce a common structure for all its subclasses.

Enforces a Common Interface
An abstract class defines method names and signatures that all subclasses must implement.
This ensures that all child classes follow the same blueprint, making the code consistent and reliable.


what this simply implies is that, for an abstract parent class that contains an abstractmethod, all child classes must implement that abstract method

"""
class LibraryItem(ABC):
    
    def __init__(self, title):
        self.title = title
        
    @abstractmethod
    def get_details(self):
        """
            Abstract method to get details of the item
        """
        pass

class Book(LibraryItem):
    def get_details(self):
        return f"Book: {self.title}"
    

book = Book("Python Crash Course")
print(book.get_details())


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
class Cow(Animal): 
    def make_sound(self):
        return "Moo!"

dog = Dog()
print(dog.make_sound())

cat = Cat()
print(cat.make_sound())

cow = Cow()
print(cow.make_sound())