class Car:

    wheels = 4 #class variable

    def __init__(self):
        self.mil = 10 #instance variable
        self.com = "BMW" #instance variable

c1 = Car()
c2 = Car()

c1.mil= 8

Car.wheels = 5 #class instance
print(Car.wheels)


print(c1.com, c2.mil)
print(c2.com, c2.mil)