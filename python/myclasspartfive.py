# Is - A relationship 

class Student:
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        

# alumni extends student class
class Alumni(Student):

    def __init__(self, firstname, lastname, alumninumber):
        super().__init__(firstname, lastname)
        self.alumninumber = alumninumber # calling the init method statiscally
        #student.__init__(self, firstname, lastname)
        #we are calling the init function of the parent (DELETED)
        # to create parents obj inside the child obj. you can use super class
        # which will return the object of parents class

    def __str__(self):
        return f"First Name: {self.firstname} \
            \nLast Name: {self.lastname} \
            \nIC Number: {self.icnumber} \
            \nAlumni Number: {self.alumninumber}"
            
    
# We have
alumni= Alumni("Liyana", "Rozan", 97049)
print(alumni)
# to create 2 more object, you need 2 more parameter
