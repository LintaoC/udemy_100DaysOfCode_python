def add(*args):
    print(args[1]) # Will print the 2nd arguements, in this case 3
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 3, 5, 7))

# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    # print(kwargs)
    # print(kwargs["add"])
    # print(kwargs["multiply"])
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)