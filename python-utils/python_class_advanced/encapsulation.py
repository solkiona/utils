""" 

Encapsulation & Property Methods

Encapsulation is the practice of restricting direct access to some object attributes and using getter and setter methods instead. In Python, you can achieve this using private variables (__variable) and property decorators (@property, @setter).


Encapsulation allows you to control access to attributes and ensure that certain logic runs before modification happens.


"""


class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.__copies = copies  #Private attribute
        
    @property
    def copies(self):
        """
            Getter method for copies
        """
        return self.__copies
    
    @copies.setter
    def copies(self, qty):
        """
            Setter method for copies
        """
        try:
            if qty >= 0:
                self.__copies = qty    
            else:
                raise ValueError("Copies cannot be negative")
        except Exception as e:
            print(f"{e}")
            

book = Book("Oliver Twist", "Charles Dickens", 1837, 5)
print(book.copies)  # Accessing the private attribute using the getter
book.copies = -10
print(book.copies)  # Accessing the private attribute using the getter



class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance 
        
    @property
    def balance(self):
        """
            Getter method for balance
        """
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        """
            Setter method for balance
        """
        try:
            if amount >= 0:
                self.__balance = amount    
            else:
                raise ValueError("Balance cannot be negative")
        except Exception as e:
            print(f"{e}")
account = BankAccount("John Doe", 1000)
print(account.balance)  # Accessing the private attribute using the getter 
account.balance = -500
print(account.balance)  # Accessing the private attribute using the getter

