# Method are nothing but function inside the class
# Methods take atleast 1 parameter (self)
# This parameter is used by python to pass the instance

class calculator:
    # since the method take self as parameter
    # this method can also be called as instance method
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
mycalculator = calculator(10, 20)
print(mycalculator.add())
print(mycalculator.subtract())

# There is a class which has many mo

class Utility:

    def addition(x,y):
        return x + y 
    
    def subtraction (x,y):
        return x-y
    
print(Utility.addition(10,20))
# however this can be done easily using module in python
# no need to create a class

# There are some use cases where class has properties
# but 