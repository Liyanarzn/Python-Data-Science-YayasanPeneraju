firstname = "Khairi"
lastname = "Abu Bakar"
# + is arithmetic operator used for tradition
#
fullname = firstname + " " + lastname 
print(fullname)

carplate = "JCG"
number = 9876

carplatenumber = carplate + str(number)
print(carplatenumber)

# we also know * means multiplication
# how can we use * over string data

product = "book"
# when you multiply string with integer then the *becomes times operator 
print(product * 5)
print("=" * 5)

print("book"*5)


#we already know strig value (string literal) in python are enclosed
# either with double quote "" or single quote ''
# However in python you can use """.."""
# to handle multiline strings

content = "As I am not \t feeling well, \n"
content = content + "I am not able to attend the meeting, \n"
content = content + "Please proceed without \r my presence. \n"

print(content)

filepath= "c:\newfolder\table\readme.txt"
print(filepath)

filepath= "c:\\newfolder\\table\\readme.txt"
print(filepath)

#raw string

filepath =r"c:\\newfolder\\table\\readme.txt"
print(filepath)

content = """As I am not feeling well, 
I am not able to attend the meeting, 
"Please proceed without my presence. """

print (content)

# Relationship between strings and list
# strings are not nothing but list of characters
message = "Hello World" # ['H','e', 'l',]
print(message[0])
print(message[0:5])
print(message[-5:])
print(message[::-1])

mynumber = 86749
#strmynumber =str (mynumber)
#print(int(strmynumber [::-1]))
print(int(str(mynumber)[::-1]))

#####################################################
numbers = input("Enter the numbers (comma separated):")
print(numbers)
print(type(numbers))
values = numbers.split(",") #convert string many values into list
print(values)
print(type(values))

total = 0
for value in values: #we dunno how many number we have. use for in. pulls 10 into variable value
    total = total + int(value)

print(total)