"""Library Management System (LMS) for managing books and members.
"""

class LibraryItem:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.borrowed = 0
        self.available = copies - self.borrowed
        
    def get_details(self):
        """
            Get details of the item
        """
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Copies: {self.copies}"
    def borrow(self, qty):
        if qty <= self.available:
            self.borrowed += qty
            self.available -= qty
            return f"You borrowed {qty} copies of '{self.title}'. {self.available} copies remaining"
        return f"Only {self.available} copies of '{self.title}' are available."
    
    def return_item(self, qty):
        if qty <= self.borrowed:
            self.borrowed -= qty
            self.available += qty
            if self.borrowed == 0:
                return f"All copies of '{self.title}' returned."
            return f"{self.available} copies of '1984' now available."
        
        return f"You cannot return {qty} copies of '{self.title}'. You only borrowed {self.borrowed} copies."


class Book(LibraryItem):
    """
        Book class inheriting from LibraryItem and using the args and kwargs
    """
    def __init__(self, genre, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.genre = genre
        
    def get_details(self):
        return f"{super().get_details()} Genre: {self.genre}\n"


class DVD(LibraryItem):
    def __init__(self, duration, rating, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.duration = duration
        self.rating = rating
        
    def get_details(self):
        return f"{super().get_details()} Duration: {self.duration}, Rating: {self.rating}\n"


class Journal(LibraryItem):
    def __init__(self, issue_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.issue_number = issue_number
        
    def get_details(self):
        return f"{super().get_details()} Issue Number: {self.issue_number}\n"
    

book1 = Book(title="1984", author="George Orwell", year=1949, copies=3, genre="Dystopian")
dvd1 = DVD(title="Inception", author="Christopher Nolan", year=2010, copies=5, duration=148, rating="PG-13")
journal1 = Journal(issue_number=42, title="Nature", author="Various", year=2023, copies=10)

print(book1.get_details())
# Output: Title: 1984, Author: George Orwell, Year: 1949, Copies: 3, Genre: Dystopian

print(dvd1.get_details())
# Output: Title: Inception, Author: Christopher Nolan, Year: 2010, Copies: 5, Duration: 148 mins, Rating: PG-13

print(book1.borrow(2))
# Output: You borrowed 2 copies of '1984'. 1 copies remaining.

print(book1.return_item(1))
# Output: 2 copies of '1984' now available.

print(journal1.get_details())
# Output: Title: Nature, Author: Various, Year: 2023, Copies: 10

print(journal1.borrow(3))
print(journal1.return_item(3))
print(journal1.get_details())