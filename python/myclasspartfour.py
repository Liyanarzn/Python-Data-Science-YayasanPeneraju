#has-A relationsship
# customer has-a passport
class Passport: 

    def __init__(self, country, passportnumber):
        self.country = country
        self.passportnumber = passportnumber

    def __str__(self):
        return f"Country :{self.country} \n Passport Number: {self.passportnumber}"
    
        

class Customer : #customer has a relationship, then it became properties

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        self.passport = None
    
    def __str__(self):
        message = f"First Name: {self.firstname}\n"
        message = message+ f"Last Name: {self.firstname}\n"
        message = message + f"Ic Number: {self.icnumber}\n"
        if (self.passport != None):
            message = message + self.passport.__str__() #{self.passport}
        return message



peter = Customer("Parker", "Peter")
passport = Passport("UK", "E0202932")
peter.passport = passport  # assigning passport to peter
print(peter)
# convert python obj to dict
print(peter.__dict__)
# now we know how to convert python object to a dictionary
 
# by default only string will print in string data type
