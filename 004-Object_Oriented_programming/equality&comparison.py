class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # The __eq__ method checks for equality between two objects
    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare a book to a non-book")
        return (self.title == other.title and self.author == other.author and self.price == other.price)

    # The __ge__ method establishes >= relationship with another obj
    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare a book to a non-book")
        return self.price >= other.price
    # The __lt__ method establishes < relationship with another obj
    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare a book to a non-book")
        return self.price < other.price

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)

print(b1 == b3)
print(b1 == b2)
print(b2 >= b1)
print(b2 < b1)

books = [b1, b2, b3]
books.sort()
print([book.title for book in books])