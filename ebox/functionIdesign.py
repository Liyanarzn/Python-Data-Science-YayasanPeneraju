#1 
def greet(argument1, argument2):
    return f"Hello {argument1}, {argument2}"

def main():
    print("Menu")
    print("1. Name and Message")
    print("2. Name")
    choice = input()
    
    if choice == "1":
        argument1 = input("Enter the name\n")
        argument2 = input("Enter the message\n")
    elif choice == "2":
        argument1 = input("Enter the name\n")
        argument2 = "Welcome to Python Programming"
    else:
        print("Invalid choice")
        return

    # Call the greet function and print the result
    message = greet(argument1, argument2)
    print(message)

# Directly calling the main function
main()

#2
#sol 1
def is_leap_year(year):

    if (year % Leap_Condition1 == 0 and year %)
        (Leap_Condition2 != 0) or ( year % Leap_Condition3 == 0 ):
        return True 
    else : 
        return False
#sol 2

def daysInYear(year, is_leap=False):
    # Leap year calculation
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
    return is_leap

def main():
    # Input year from the user
    year = int(input())
    
    # Check if the year is a leap year
    if daysInYear(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

# Directly calling the main function
main()
