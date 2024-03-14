class Stock:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.investors = []
    
    def attach(self, investor):   
        if investor not in self.investors:
            self.investors.append(investor)
        else:
            print("Investor already exists")
    
    def detach(self, investor):
        if investor in self.investors:
            self.investors.remove(investor)
        else:
            print("Investor doesn't exists")
    
    def change_price(self, new_price):
        self.price = new_price
        
        for investor in self.investors:
            investor.update(self)


class investor:
    
    def __init__(self, name):
        self.name = name
    
    def update(self, stock):
        print(f"Hey, {self.name} The stock {stock.name} has been change to {stock.price}")


if __name__ == "__main__":
    google_stock = Stock("Google", 1000)
    Kishore = investor("Kishore")
    Abinav = investor("Abinav")
    google_stock.attach(Kishore)
    google_stock.attach(Abinav)
    google_stock.change_price(2000)
        