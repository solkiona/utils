class Book:
    def __init__(self, title, author, year , copy):
        self.title = title
        self.author = author
        self.year = year
        self.copy = copy
        self.borrowed = 0
        self.available = copy - self.borrowed
    
    def borrow(self, qty):
        
        if qty <= self.available:
            self.borrowed += qty
            self.available -= qty
            print(f"{qty} copies of '{self.title}' borrowed.")
        else:
            print(f"Sorry, only {self.available} copies of '{self.title}' are available.")
    def return_book(self, qty):
        if qty < self.borrowed:
            self.borrowed -= qty
            self.available += qty
            print(f"{qty} copies of '{self.title}' returned.")
        elif qty == self.borrowed:
            self.borrowed = 0
            self.available = self.copy
            print(f"All copies of '{self.title}' returned.")
        else:
            print(f"Cannot return {qty} copies of '{self.title}'. You only borrowed {self.borrowed}.")
   
   

book1 = Book("Into the Badlands", "George Wales", 2015, 30)
book1.borrow(3)
print(book1.available)
book1.return_book(3)
# book1.return_book(3)




# class Book:
#     def __init__(self, title, author, year , copy):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.copy = copy
#         self.borrowed = 0
#         self.available = copy - self.borrowed
        
    
#     def borrow(self, qty):
#         if qty <= self.available:
#             self.borrowed += qty
#             self.available -= qty
#             print(f"{qty} copies of '{self.title}' borrowed.")
#             return(f"You borrowed {qty} copies of '{self.title}'")
#         else:
#             print(f"Sorry only {self.available} copies of '{self.title}' are available.")
#             return(f"Sorry only {self.available} copies of '{self.title}' are available")

#     def return_book(self, qty):
#         if qty > self.borrowed:
#             print(f"Sorry you can't return more than you borrowed")
#             return(f"Sorry you can't return more than you borrowed")
#         elif qty < self.borrowed:
#             self.borrowed -= qty
#             self.available += qty
#             print(f"{qty} copies of '{self.title}' returned.")
#             return(f"{qty} copies of '{self.title}' returned.")
#         elif qty == self.borrowed:
#             self.borrowed = 0
#             self.available = self.copy

# book1 = Book("Into the Badlands", "George Wales", 2015, 30)
# book1.borrow(3)
# print(book1.available)
# book1.return_book(2)
# print(book1.available)
# book1.return_book(2)
# print(book1.available)
# book1.return_book(1)
# print(book1.available)
# # book1.return_book(3)