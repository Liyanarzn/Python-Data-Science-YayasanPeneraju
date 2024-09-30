# product is the variable
# "Television" is the string value
# to differentiate the variables from the values we use double quotes""
# or single quote ''
product = "Television" # string
quantity  = 2 # integer
price = 1455.25 # float
available = True # True / False (boolean value/literal)
print ("Product:", product)
print ("Quantity:", quantity)
print ("Price:", price)
print ("Available:", available) 
# type is another built in function that tell us what is the
# data type of the variables (dynamically assigned by python)
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

total = quantity * price 
print("Total:", total)

# 
quantity = "10"
print(type(quantity))
# print ( quantity * price)

# type casting
# convert one data type to another 
# convert string to integer we have built in function in
total = int(quantity) * price 
print (total)

# convert string to float we have built in function float 
total = int(quantity) * float (price)
print (total)


firstNumber = 500
print(id(firstNumber))

secondNumber = 500
print(id(secondNumber))

firstString = "Hello"
secondString = "Hello"
print(id(firstString))
print(id(secondString))

# so far we have seen how to assign one value to one variable 
# in one line
# however we can also assign more than one value to more than 
# one variable in one line
x, y = 101, 102 
print(x)
print(y)

# how ever in python the following is not supported 
# x, y = 105 
x, y = 101 + 1, 102 + 2 
print(x)
print(y)

# Initialization 
x = 0 # numeric initializer 
x = "" # string initializer / empty string / empty brain 
x = None # no brain # keyword same as true / false 
print(type(None))
