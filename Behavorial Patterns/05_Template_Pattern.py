from abc import ABC, abstractmethod

class Coffee(ABC):
    def makeCoffee(self):
        self.prepareIngredients()
        self.brewCoffee()
        self.pourCoffee()
        self.addCondiments()

    @abstractmethod
    def prepareIngredients(self):
        pass

    @abstractmethod
    def brewCoffee(self):
        pass

    @abstractmethod
    def pourCoffee(self):
        pass

    @abstractmethod
    def addCondiments(self):
        pass

class Espresso(Coffee):
    def prepareIngredients(self):
        print("Grinding coffee beans")

    def brewCoffee(self):
        print("Brewing espresso")

    def pourCoffee(self):
        print("Pouring espresso into a cup")

    def addCondiments(self):
        print("No condiments for espresso")

class Cappuccino(Coffee):
    def prepareIngredients(self):
        print("Grinding coffee beans and frothing milk")

    def brewCoffee(self):
        print("Brewing espresso and mixing with frothed milk")

    def pourCoffee(self):
        print("Pouring cappuccino into a cup")

    def addCondiments(self):
        print("Adding sugar or cinnamon")

# Client code
if __name__ == "__main__":
    print("Making Espresso:")
    espresso = Espresso()
    espresso.makeCoffee()
    print("\nMaking Cappuccino:")
    cappuccino = Cappuccino()
    cappuccino.makeCoffee()
