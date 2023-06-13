class Book:
    # We use caps to show that this is a class variable
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # Static Methods
    __booklist = None # This is a private variable. Only one of these will ever be created
    @staticmethod
    def getBookList():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # Use the classmethod decorator to signify that the method is class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    def setTitle(self, newTitle):
        self.title = newTitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype

book1 = Book("Harry Potter", "HARDCOVER")
# book2 = Book("Batman", "COMIC") # Gives an error as comic is not a valid book type
book2 = Book("Batman", "EBOOK") # Gives an error as comic is not a valid book type
# Class methods are called using the class name
print("Book Types: ", Book.getBookTypes())
theBooks = Book.getBookList()
theBooks.append(book1)
theBooks.append(book2)
print(theBooks)