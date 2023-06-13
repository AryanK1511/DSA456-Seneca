class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

# Book class inherits the Publication class
class Book(Publication):
    def __init__(self, title, author, pages, price):
        # super() calls the constructor of the base class
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Magazine(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

class Newspaper(Periodical):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)

b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", 6.0, "Daily", "New York Times Company")
# m1 = Magazine(title="Scientific American", publisher="Springer Nature", price=5.99, period="Monthly")
m1 = Magazine("Scientific American", 5.99, "Monthly", "Springer Nature")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)