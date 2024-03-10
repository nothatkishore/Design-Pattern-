class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

o1 = SingleTon()
print("Object - 1 ==>", o1)
o1.data = 10

print(type(object))