class LibraryItem:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.borrowed = 0
        
        
    def borrow(self, qty):
        """
            Borrow a given number of copies
        """
        if qty <= self.copies:
            self.copies -= qty
            self.borrowed += qty
            return f"You borrowed {qty} copies of '{self.title}'. {self.copies} copies remaining"
        return f"Only {self.copies} copies of '{self.title}' are available."
    
    def return_item(self, qty):
        """
            Return a given number of copies
        """
        
        if qty <= self.borrowed:
            self.copies += qty
            self.borrowed -= qty
            
            if self.borrowed == 0:
                return f"All copies of '{self.title}' returned."
            return f"{qty} copies of '{self.title}' returned. {self.borrowed} copies remaining."
        return f"You cannot return {qty} copies of '{self.title}'. You only borrowed {self.borrowed} copies."
    
    def get_details(self):
        """
            Get details of the item
        """
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nCopies: {self.copies}\n"

class Book(LibraryItem):
    """
        Book class inheriting from LibraryItem and using the args and kwargs
    """
    def __init__(self, genre="Uknown Genre", *args, **kwargs):
        self.genre = genre
        super().__init__(*args, **kwargs)
      
        
    
    def get_details(self):
        return f"{super().get_details()}Genre: {self.genre}\n"

class Magazine(LibraryItem):
    def __init__(self, title, author, year, copies, issue_number):
        super().__init__(title, author, year, copies)
        self.issue_number = issue_number
        
    def get_details(self):
        return f"{super().get_details()}, Issue Number: {self.issue_number}\n"
    
    
book1 = Book( "Dystopian Fiction", "Into the Badlands", "George Orwell", 1949, 5, )
magazine1 = Magazine("National Geographic", "Various Authors", 2023, 10, "Issue 78")

print(book1.get_details())  # Book details
print(magazine1.get_details())  # Magazine details

print(book1.borrow(3))  # Borrow 3 books
print(book1.return_item(2))  # Return 2 books
print(book1.return_item(2))  # Return remaining books
print(book1.return_item(1))  # Error: Cannot return more than borrowed
print(magazine1.borrow(5))
print(magazine1.get_details())