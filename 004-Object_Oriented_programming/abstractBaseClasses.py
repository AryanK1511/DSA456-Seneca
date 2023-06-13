# Use the 'abc' module from the standard library
from abc import ABC, abstractmethod
class GraphicShape(ABC): # ABC stands for abstract base class
    def __init__(self):
        super().__init__()

    @abstractmethod # This decorator indicates that the calcArea method is an abstract method
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return (self.side * self.side)

# g = GraphicShape() # Gives an error as you can't instantiate the ABC
c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())