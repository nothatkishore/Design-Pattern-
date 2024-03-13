'''
This pattern is higly helpful, when you wanna create an highly configurable object like the one demonstrated below
'''

class House: #This is the main class with lots of parameters for configuration
    def __init__(self, floors, door_type, roof_type) -> None:
        self.floors = floors
        self.door_type = door_type
        self.roof_type = roof_type
        

class HouseBuilder: #This is a builder class which will build the object for the main class
    def __init__(self) -> None:
        self.floors = None
        self.door_type = None
        self.roof_type = None
    
    def set_floors(self, floors):
        self.floors = floors
        return self
    
    def set_door(self, door_type):  
        self.door_type = door_type  
        return self
    
    def set_roof(self, roof_type):  
        self.roof_type = roof_type  
        return self
    
    def build(self):
        return House(self.floors, self.door_type, self.roof_type)
    

class Director:     #This class will instruct builder class to make a predefined configuration
    
    def __init__(self, Builder) -> None:
        self.builder = Builder
    
    def build_single(self):
        return self.builder.set_floors(1).set_door(2).set_roof("Pointy")
    
    def build_apartments(self):
        return self.builder.set_floors(1).set_door(2).set_roof("Flat")
    

if __name__ == "__main__":
    builder = HouseBuilder()
    D1 = Director(builder)
    Kishore = D1.build_single()
    K = Kishore.build()