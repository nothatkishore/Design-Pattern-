'''
Singleton pattern : This pattern is used in places where we require only 1 instance for the class and
want to provide a global point of access.
'''

class Student:
    
    __instance = None
    
    def __new__(cls, *args, **kwargs):          #This is a key word that is called before __init__
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)   #Creating object for that class
        return cls.__instance                       #Returning that object

    def __init__(self, name) -> None:               #Initialising the values for the created object
        self.number = name
     
Kishore = Student('Kishore')
Abinav = Student('Abinav')

        