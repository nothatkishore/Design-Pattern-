'''

This pattern can be used to create a copy of complex objects.

'''

from copy import deepcopy


class shape:
    
    def __init__(self, type) -> None:
        self.type = type
    
    def clone(self):
        return deepcopy(self)       #This is used to get new copy of a mentioned object

class Circle(shape):
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def info(self):
        print(f"The shape is {self.type} and radius is {self.radius}")

class Square(shape):
    
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

if __name__ == "__main__":
    
    C1 = Circle(5)
    C1.info()
    C2 = C1.clone()     #C2 is copy of complex object C1
    C2.info()           
    C2.radius = 10
    C2.info()

