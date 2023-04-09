class complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add_comp(self, c1, c2):
        temp = complex(0, 0)
        temp.real = c1.real + c2.real
        temp.imaginary = c1.imaginary + c2.imaginary
        return temp


c1 = complex(0, 0)
c2 = complex(0, 0)
c1.real = int(input("enter real part"))
c1.imaginary = int(input("enter img. part"))
c2.real = int(input("enter real part"))
c2.imaginary = int(input("enter img. part"))
c3 = complex(0, 0)
c3 = c3.add_comp(c1, c2)
print("sum is:", c3.real, "+i", (c3.imaginary))


class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def peri(self):
        return a + b + c


a = int(input("enter value for a:"))
b = int(input("enter value for b:"))
c = int(input("enter value for c:"))
object = triangle(a, b, c)
print("perimeter is:", object.peri())


class lists:
    def __init__(self, a):
        self.a = a

    def append(self, value):
        self.value = value
        a.append(value)
        return a

    def remove(self, value):
        self.value = value
        a.remove(value)
        return a

    def display(self):
        print(a)


object = lists(a)
a = [1, 2, 3, 4]
object.append(int(input("enter value to append:")))
print(a)
object.remove(int(input("enter value to remove:")))
print(a)
object.display()


class calculator:
    def multiply(self, a, b):
        self.a = a
        self.b = b
        return a * b

    def addition(self, a, b):
        self.a = a
        self.b = b
        return a + b


a = int(input("enter value of a"))
b = int(input("enter value of b"))

object1 = calculator()
choice = 1
print("1 for addition")
print("2 for multiplication")
choice = int(input("enter"))
if choice == 1:
    print(object1.addition(a, b))
elif choice == 2:
    print(object1.multiply(a, b))
else:
    print("invalid choice")


class rev:
    def __init__(self, string):
        self.string = string

    def reverse(self, string):
        string = string.split()
        for i in range(len(string)):
            reversestr = string[i]
            reversestr = reversestr[::-1]
            print(reversestr, end=" ")


string = input("enter the string:")
obj = rev(string)
obj.reverse(string)


class vehicle:
    def __init__(self, maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

    def display(self):
        print(self.maxspeed)
        print(self.mileage)


class bus(vehicle):
    pass


maxspeed = int(input("enter the speed:"))
mileage = int(input("enter the mileage:"))
obj = bus(maxspeed, mileage)
obj.display()
