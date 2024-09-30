# Encapsulation 
# Encapsulatate the properties inside the class
# in other languanges we have keywords public, private, protected
# to protect the properties
# ensure that value you set to the properties must be valid 

class circle:

    def __init__(self, radius):
        self.__radius = 0 #initialize the propeties without condition
        if (isinstance(radius, int)):
            self.__radius = radius #__ new version feature
        
        else:
            print("invalid reason")
       
    #getter method and setter method
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        if (isinstance(radius, int)):
            self.__radius = radius
        else:
            print("Invalid Radius")
    #properties is a class 
    # we are calling/invoking the class by passing the mothod as argument
    # Please notice after getRadius there is no ()
    radius = property(getRadius, setRadius)  

    def area (self):
        return 3.14 * self.__radius * self.__radius
    
    def circumference(self):
        return 2 * 3.14 * self.__radius 
    
    def __str__(self):
        return f"Radius of this circle is {self.__radius}"

mycircle = circle(20)
print(mycircle)
mycircle.radius= 30
#mycircle.__radius= 30 #private properties  mycircle._radius
print(mycircle)
print(mycircle.area())
mycircle.radius = "abc"
print(mycircle)
