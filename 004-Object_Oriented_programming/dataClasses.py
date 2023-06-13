from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 40))

@dataclass
# @dataclass(frozen=True) # This makes the dataclass immutable, from both inside and outside the class
# They automatically implement __repr__ and __eq__
class Book:
    title: str = "No Title"
    author: str = field(default = "No Author")
    pages: int = field(default_factory = price_func)
    price: float = 0 # attributes with default values have to come first

    # The __post_init__ function lets us customize additional props after the object is initialized using the built in __init__
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

# Create some book objects
b1 = Book()
print(b1)