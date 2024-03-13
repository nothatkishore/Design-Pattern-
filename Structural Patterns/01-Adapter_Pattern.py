from abc import ABCMeta, abstractstaticmethod

class IA(metaclass = ABCMeta):
    @abstractstaticmethod
    def print_class():
        '''This is a abstract method'''

class A(IA):
    @staticmethod
    def print_class():
        print("This is class A")

class IB(metaclass = ABCMeta):
    @abstractstaticmethod
    def print_value():
        '''This is a abstract method'''

class B(IB):
    @staticmethod
    def print_value():
        print("This is class B")

if __name__ == "__main__":
    objectA = A()
    A.print_class()
    objectB = B()
    B.print_value()