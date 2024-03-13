from abc import ABCMeta, abstractclassmethod


class IPerson(metaclass=ABCMeta):
    
    @abstractclassmethod
    def person_method():
        pass

class Person(IPerson):
    
    def person_method(self):
        print("This is a person method in person class")

class proxy_Person(IPerson):
    
    def __init__(self):
        self.person = Person()
    
    def person_method(self):
        print("This is a proxy method of person")
        self.person.person_method()


if __name__ == "__main__":
    p1 = proxy_Person()
    p1.person_method()