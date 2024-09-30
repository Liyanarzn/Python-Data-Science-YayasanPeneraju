# input is a built in function 
# which takes a single parameter (caption/question)
# display the caption to the user and take the keyboard input 
# assign it to the variable

firstNumber = input("Enter the first number:")
print(firstNumber)
print (type(firstNumber))

firstNumber = int(firstNumber)

secondNumber = int(input("Enter the second number:"))

print(firstNumber + secondNumber)

w = int(input("Enter branding expenses"))
x = int(input("Enter travel expenses"))
y = int(input("Enter food expenses"))
z = int(input("Enter logistics expenses"))


total = w + x + y + z

w_expense = (w / total) * 100
x_expense = (x / total) * 100
y_expense = (y / total) * 100
z_expense = (z / total) * 100

print( "Total expenses :" ,  total)
print( "Branding expenses percentage :" ,  w)
print( "Travel expenses percentage :" ,  x)
print( "Food expenses percentage :" ,  y)
print( "Logistics expenses percentage :" ,  z)
