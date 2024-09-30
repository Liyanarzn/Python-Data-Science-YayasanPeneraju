n1 = int(input("Enter the number of people who watched show 1"))
r1 = float(input("Enter the average rating for show 1"))

n2 = int(input("Enter the number of people who watched show 2"))
r2 = float(input("Enter the average rating for show 2"))

n3 = int(input("Enter the number of people who watched show 3"))
r3 = float(input("Enter the average rating for show 3"))


overall_average_rating = ((n1 * r1) + (n2 * r2) + (n3 * r3)) / (n1 + n2 + n3)

print(f"The overall average rating for the show is {overall_average_rating:.2f}")

# #2

# Read input for three cards
card1 = input().strip().split()
card2 = input().strip().split()
card3 = input().strip().split()

# Extract type and number for each card
type1, number1 = card1[0], card1[1]
type2, number2 = card2[0], card2[1]
type3, number3 = card3[0], card3[1]

# Check for Double Bonanza
if type1 == type2 == type3 and number1 == number2 == number3:
    print("Double Bonanza")
# Check for Bonanza
elif type1 == type2 == type3 or number1 == number2 == number3:
    print("Bonanza")
# Otherwise, No Bonanza
else:
    print("No Bonanza")

# 3 prime number
# 1.
start_num = 2
end_num = 15

for num in range(start_num, end_num):
    if num > 1:  # Check if num is greater than 1 (since 1 is not a prime number)
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end = ' ')

# 2. 
# Reading input
a = int(input())
b = int(input())

# List to store prime numbers
primes = []

# Loop through the range [a, b]
for num in range(a, b + 1):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check divisibility from 2 to sqrt(num)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

# Print the prime numbers as space-separated values
print(" ".join(map(str, primes)))

# function

def multiply(a, c=10):
    return a*c

def multiply(a, b):
    return a * b

def multiply(a, b=9):
    return a * b

a = int(input())
b = int(input())

print(f"The result is {multiply}")

def multiply(a, b = 10):
    return a * b

# Input
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# Function calls and output
print(f"The result is {multiply(a)}")
print(f"The result is {multiply(a, b)}")
print(f"The result is {multiply(a, b=9)}")

# function 2

def multiVarFunc(department, total_students, total_faculties):
#     return department, total_students, total_faculties

# # Main code to display the details
# department = input("Enter department name:\n")
# total_students = int(input("Enter the number of total students:\n"))
# total_faculties = int(input("Enter the number of total faculties:\n"))
# department, total_students, total_faculties = multiVarFunc()

# print("Details:")
# print(f"Department: {department}")
# print(f"Total students: {total_students}")
# print(f"Total faculties: {total_faculties}")

def multiVarFunc(department, total_students, total_faculties):
    return department, total_students, total_faculties

# Main code to display the details
department = input("Enter department name:\n")
total_students = int(input("Enter the number of total students:\n"))
total_faculties = int(input("Enter the number of total faculties:\n"))

# Call the function with user inputs
department, total_students, total_faculties = multiVarFunc(department, total_students, total_faculties)

# Display the details
print("Details:")
print(f"Department: {department}")
print(f"Total students: {total_students}")
print(f"Total faculties: {total_faculties}")


