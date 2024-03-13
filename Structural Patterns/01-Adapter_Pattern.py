class int_format:
    
    def __init__(self, number : int):
        self.number = number
    
    def print_format(self):
        return self.number

class str_format:
    @staticmethod
    def print_format():
        return "123"

class int_to_str:
    
    def __init__(self, obj):
        self.obj = obj
    
    def print_converted(self):
        return str(self.obj.print_format())

if __name__ == "__main__":
   conv = int_to_str(int_format(154))
   print(conv.print_converted() * 3)
