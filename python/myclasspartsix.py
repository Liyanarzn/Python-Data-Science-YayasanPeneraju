# Polymorphism

class Gender:
    def __init__(self):
        pass
    def doCarryObjects(self):
        pass

class Male(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry heavy objects")

class Female(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry light objects")     

def getGender(name):
    if "A/L" in name:
        return Male()
    else:
        return Female()
    
# Python dynamically set the data type for the gender variable 
#sometimes it becomes Male object
# sometimes it becomes Female Objects
gender = getGender("Khairi A/L Abu Bakar")
gender.doCarryObjects()
print(type(gender)) #<class'___main___.Male

gender = getGender("Aida A/P Abu Bakar")
gender.doCarryObjects()
print(type(gender))
    
    



    