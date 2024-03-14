from abc import ABC

class startegy(ABC):
    def attack(self):
        pass

class sword(startegy):
    def attack(self):
        print("Attack with sword!")

class arrow(startegy):
    def attack(self):
        print("Attack with bow and arrow!")

class magic_spell(startegy):
    def attack(self):
        print("Attack with magic spell")


class character:
    
    def __init__(self, startegy):
        self.startegy = startegy
    
    def set_startegy(self, startegy):
        self.startegy = startegy
    
    def attack_enemy(self):
        self.startegy.attack()


if __name__ == "__main__":
    
    Kishore = character(sword())
    Kishore.attack_enemy()
    
    Kishore.set_startegy(arrow())
    Kishore.attack_enemy()
    
    Kishore.set_startegy(magic_spell())
    Kishore.attack_enemy()