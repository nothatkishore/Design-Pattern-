from abc import ABC

class coffee(ABC):
    def get_ingredients(self):
        pass
    
    def print_price(self):
        pass

class classic_coffee(coffee):
    
    def get_ingredients(self):
        return "Coffee powder + water"
    
    def print_price(self):
        return 100

class cold_coffee(coffee):
    
    def __init__(self, obj):
        self.object_ = obj
    
    def get_ingredients(self):
        return self.object_.get_ingredients() + " + ICE Cubes"
    
    def print_price(self):
        return self.object_.get_price() + 100

class super_coffee(coffee):
    
    def __init__(self, obj):
        self.object_ = obj
    
    def get_ingredients(self):
        return self.object_.get_ingredients() + " + ICE Cubes + Super syrup"
    
    def print_price(self):
        return self.object_.print_price() + 200

if __name__ == "__main__":
    
    coffee = classic_coffee()
    print(coffee.get_ingredients())
    coffee2 = cold_coffee(coffee)
    print(coffee2.get_ingredients())
    coffee3 = super_coffee(coffee)
    print(coffee3.get_ingredients())
