class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # __getattribute__ called when an attribute is retrieved
    # Don't directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name):
        if (name == "price"):
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    # __setattr__ called when an attribute value is set
    def __setattr__(self, name, value):
        if (name == "price"):
            if type(value) is not float:
                raise ValueError("The price must be a float")
        return super().__setattr__(name, value)

    # __getattr__ called when __getattribute__ lookup fails
    def __getattr__(self, item):
        return f"{item} is not here."