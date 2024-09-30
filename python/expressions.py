# Arithmatic Operators
# Addition / Subtraction / Multiplication / Division / Exponent
x = 7
y = 2

# expression can be based to print function
# in this case expression is and argument to print function 
print ( "Addition:" , x + y)
print ( "Substraction:" , x - y )
print ( "Multiplication:" , x * y)
print ("Division:" , x / y)
print ( "Quotient:" , x // y)
print ( "Remainder:", x % y)

# how to find exponent 
# 10 x 10 x 10 
print("Exponent:", 10 ** 3 )
print("What is the maximum number in a 64 bit env:", (2**64)-1)


#Assignment Operators 

x = 100 #we assign 100 to x
x += 1 # x = x + 1 complexity 
x += 2 # x = x + 2
x += 5 # x = x + 5 

# Fadhli Equation 
x += x + 1 # x = x + (x + 1)
# x = 108
# x = 108 + 109 = 217 
print (x)

x -= 1 # x = x - 1 
print (x)

x *= 1 # x = x * 1

myheight = 5.2
yourheight = 5.3
mybrotherheight = 5.2 

# let us create TRUE statements
print(myheight < yourheight)
print (yourheight > myheight)
print (myheight == mybrotherheight)
print (myheight != yourheight)
print (myheight <= mybrotherheight) # less than or equals to 
print (myheight <= yourheight) # less than or equals to
print (mybrotherheight >= myheight) # greater than or equals to
print (yourheight >= myheight) # greater than or equals to

# logical operator
# It actual help us to solve more than one condition 
# and: both/all conditions must be True 
# or: any one of the condition is True
a = 10
b = 7 
c = 4

#Let us create TRUE statements
print(a > b and a > c) # True means a is the biggest number
print( c < a and c < b) # True means c is the smallest number
 
print(a > b or  a > c) # true means 
# a can be bigger than b, a can be bigger than c and also 
# a can be bigger than b and c 

print ((b < a and  b > c) or (b > a and  b <c)) # Tue b is the middle number

# Negation operator 
isAvailable = True 
print(not isAvailable)
print(not not isAvailable)

# sometimes we will have some statement to be executed 
# when the condition fails (false)


