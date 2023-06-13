# Creating a basic class
class Book:
    # This is the initializer function. The object is already constructed before this function is called
    # The word self is just a naming convention, it is the object itself
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        # If you put __ before an attribute or a method, python interpreter changes the name of the attribute to prevent subclasses from overriding the attribute
        self.__secret = "This is a secret attribute"
        self.price = price

    # Instance Methods and Attributes
    def getPrice(self):
        # Checks if _discount exists
        if (hasattr(self, "_discount")):
            return self.price - (self.price * self._discount)
        return self.price
    def setDiscount(self, amount):
        # The underscore tells other programmers that the method or attribute is intended to only be used by the class
        self._discount = amount

# Creating instances of the class
book1 = Book("Harry Potter", "J.K. Rowling", 500, 30.25) # We dont pass the 'self' attribute as it is the object itself

# Print the class and Property
print(book1)
print(book1.title)
print(book1.getPrice())
book1.setDiscount(0.5)
print(book1.getPrice())
# print(book1.__secret) # This does not work
print(book1._Book__secret) # This works