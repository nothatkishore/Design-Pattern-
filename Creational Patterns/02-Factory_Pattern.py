from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        pass

class student(IPerson):
    
    def __init__(self, name) -> None:
        self.name = name
    
    def person_method(self):
        print(f"{self.name} is a student")

class teacher(IPerson):
    
    def __init__(self, name) -> None:
        self.name = name
    
    def person_method(self):
        print(f"{self.name} is a teacher")

class PersonFactory:
    
    @staticmethod
    def build_person(person, name):
        if person == 'Student':
            return student(name)
        elif person == 'Teacher':
            return teacher(name)
        else:
            print("Object creation not valid")


if __name__ == "__main__":
    Person = input('Who are you ? ')
    name = input("What is your name:")
    obj = PersonFactory.build_person(Person, name)
    obj.person_method()