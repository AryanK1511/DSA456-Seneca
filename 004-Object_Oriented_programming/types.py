class Book:
    def __init__(self, title, author, pages, price):
        pass

book1 = Book("Harry Potter", "J.K. Rowling", 500, 30.25)
book2 = Book("Rich Dad Poor Dad", "R. Kiyosaki", 250, 21.15)

# Checking the type
print(type(book1))
# Comparing the type
print(type(book1) == type(book2))
# Use instance to compare specific instance to a known type
print(isinstance(book1, Book))
print(isinstance(book1, object)) # everything is an instance of object class
# All classes in python derive from object