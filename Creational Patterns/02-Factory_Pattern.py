'''

The object creation is not explicitly mentioned.

'''



from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):         #This is the abstract class or interface for the classes
    
    @abstractstaticmethod
    def person_method():
        pass

class student(IPerson):                     #This is a student class
    
    def __init__(self, name) -> None:
        self.name = name
    
    def person_method(self):
        print(f"{self.name} is a student")

class teacher(IPerson):                     #This is a teacher class
    
    def __init__(self, name) -> None:
        self.name = name
    
    def person_method(self):
        print(f"{self.name} is a teacher")

class PersonFactory:                        #This is a factory class for the interface
    
    @staticmethod
    def build_person(person, name):
        if person == 'Student':
            return student(name)
        elif person == 'Teacher':
            return teacher(name)
        else:
            print("Object creation not valid")


if __name__ == "__main__":  
    Person = input('Who are you ? ')            #Getting input from the user on which object should be created
    name = input("What is your name:")          
    obj = PersonFactory.build_person(Person, name)  
    obj.person_method()                          #This idea provides a great encapsulation for building objects