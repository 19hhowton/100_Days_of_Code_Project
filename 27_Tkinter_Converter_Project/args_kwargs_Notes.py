### Creating a Function with *args
def add(*args):
    return sum(args)
    
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))


### Creating a Function with **kwargs
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
        
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

### Creating a Class with **kwargs
class Car:
    
    def __init__(self, **kw):
        # self.make = kw["make"] ## Don't use [], use .get()    
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")
        
my_car = Car(make="Nissan")
