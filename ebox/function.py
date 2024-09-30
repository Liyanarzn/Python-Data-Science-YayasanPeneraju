# to find GCD and LCM
def GCD(n1, n2):
    
    while n2:
        n1, n2 = n2, n1 % n2
    return n1

def LCM(n1, n2):
    return n1 * n2 // GCD(n1, n2)

# Input
n1, n2 = map(int, input("Enter two integers: ").split())

# Output
print(f"Greatest common divisor of {n1} and {n2} = {GCD(n1, n2)}")
print(f"Least common multiple of {n1} and {n2} = {LCM(n1, n2)}")

# simple calculator

def addition(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2!=0:
        return n1 / n2 
    else:
        return "Error! Division by zero"

def modulus(n1, n2):
    if n2!=0:
        return n1 % n2
    else:
        return "Error! Division by zero"

# Display the operation menu
print("Select the operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulus")

# Get the user's choice
choice = input("Enter the choice(1/2/3/4/5): ")

# Check for valid choice
if choice in ['1', '2', '3', '4', '5']:
    n1 = float(input("Enter the first number:"))
    n2 = float(input("Enter the second number:"))

    if choice == '1':
        print(f"{n1} + {n2} = {addition(n1, n2)}")
    elif choice == '2':
        print(f"{n1} - {n2} = {subtract(n1, n2)}")
    elif choice == '3':
        print(f"{n1} * {n2} = {multiply(n1, n2)}")
    elif choice == '4':
        result = divide(n1, n2)
        if result == "Error! Division by zero.":
            print(result)
        else:
            print(f"{n1} / {n2} = {result}")
    elif choice == '5':
        result = modulus(n1, n2)
        if result == "Error! Division by zero.":
            print(result)
        else:
            print(f"{n1} % {n2} = {result}")
else:
    print("Invalid Input")

# filter events

# Function to get numbers divisible by 13 using lambda function
def filter_divisible_by_thirteen(numbers):
    return list(filter(lambda x: x % 13 == 0, numbers))

# Input
n = int(input("Enter size of list: "))
if n > 0:
    numbers = []
    print("Enter the elements in list")
    for _ in range(n):
        numbers.append(int(input()))
    
    # Get numbers divisible by 13
    result = filter_divisible_by_thirteen(numbers)
    
    # Output
    if result:
        print(" ".join(map(str, result)))
    else:
        print("No numbers divisible by 13")
else:
    print("Invalid input")
