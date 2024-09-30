#1
# name1 = ["A","n","d","r","e","w","s"]
# n1 = 2

# del name1[n1-1]
# print(name1)

# name2 = ["J","a","c","k"]
# n2 = 4

# del name2[n2-1]
# print(name2)

# #concantenate using join to remve ['']
# name1 = ["A", "n", "d", "r", "e", "w", "s"]
# n1 = 2

# name2 = ["J", "a", "c", "k"]
# n2 = 4

# del name1[n1-1]
# # Join the elements and print
# print(''.join(name1))

# del name2[n2-1]
# # Join the elements and print
# print(''.join(name2))

# #correct answer 
# # Read input
# name = input().strip()
# n = int(input().strip())

# # Convert the string to a list to easily remove the character at the nth position
# name_list = list(name)

# # Delete the character at position n-1
# del name_list[n-1]

# # Join the list back into a string and print the result
# print(''.join(name_list))


# #2
# name = input().strip()
# name_len = len(name)

# midpoint = name_len // 2 #To take 2 word

# if midpoint 


# # Function to create a palindrome by mirroring the input string

# # input_string = input().strip()

# # Function to create a mirrored palindrome
# def make_mirrored_palindrome(s):
#     # Calculate the length of the input string
#     length = len(s)
    
#     # Determine the prefix (first half of the string)
#     prefix = s[:length // 2]
    
#     # Determine the middle character (if the length of the string is odd)
#     middle = s[length // 2] if length % 2 != 0 else ''
    
#     # Construct the mirrored palindrome by concatenating the prefix, middle (if any), and the reverse of the prefix
#     mirrored_palindrome = prefix + middle + prefix[::-1]
    
#     # Return the resulting mirrored palindrome string
#     return mirrored_palindrome

# # Read the input string from the user
# input_string = input().strip()

# # Get the mirrored palindrome version of the input string
# palindrome_string = make_mirrored_palindrome(input_string)

# # Print the resulting mirrored palindrome string
# print(palindrome_string)

# #3
# def print_pattern(n):
#     forward_slash = '/'
#     backward_slash = '\\'
#     segment = (forward_slash * n + backward_slash * n) +(forward_slash * n + backward_slash * n) 
    
#     for _ in range(4):
#         print(segment)

# # Read the input integer
# n = int(input().strip())

# # Print the pattern
# print_pattern(n)
   
# #4

# name1 = input("Enter the first string:").strip()
# name2 = input("Enter the second string:").strip()


# name_list_1 = list(name1)
# name_list_2 = list(name2)

# if name1[0] == name2[0]: 
#     concantinate_str = (name1) + "  " + (name2) 
#     print(''.join(concantinate_str))

# # else:
# #     print("Invalid Input")

# #I do on my own

# # 5

# # n_school = int(input()).split()

# # sum = 0

# # for i in range(n_school):
# #     n_student = int(input()).split()
# #     sum += n_student

# # n_book = int(input()).split()
# # total_cost = sum * n_book

# # print("Total number of books required:", sum)
# # print("Total cost:", total_cost)

# # #6 
# set_1 = set(input().split(','))
# set_2 = set(input().split(','))


# if set_1 == set_2: 
#     print("Invalid Input")

# else:
#     print(set_1 ^ set_2)

# symmetric_difference = sorted(set_1 ^ set_2)
# print(symmetric_difference)
# print("{", ", ".join(map(str, symmetric_difference)), "}")



# # # # Read the input strings and convert them to sets of integers
# # set_1 = set(map(int, input().split(',')))
# # set_2 = set(map(int, input().split(',')))

# # # Check if the sets are equal
# # if set_1 == set_2: 
# #     print("invalid set")
# # else:
# #     # Calculate the symmetric difference and convert it to a sorted list
# #     symmetric_difference = sorted(set_1 ^ set_2)
    
# #     # Print the symmetric difference formatted as a set
# #     print("{", ", ".join(map(str, symmetric_difference)), "}")

# #7 

# # Answer in function 
# from datetime import datetime

# # Function to calculate the difference between two dates
# def calculate_date_difference(date1_str, date2_str):
#     # Define the date format
#     date_format = "%b %d %Y %I:%M%p"
    
#     # Parse the input dates
#     date1 = datetime.strptime(date1_str, date_format)
#     date2 = datetime.strptime(date2_str, date_format)
    
#     # Calculate the difference
#     diff = date2 - date1
    
#     # Extract days, seconds, hours, minutes, and seconds
#     days = diff.days
#     seconds = diff.seconds
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = seconds % 60
    
#     # Format the output without leading zeros
#     result = f"{days} days, {hours}:{minutes:02}:{seconds:02}"
#     return result

# #answer in normal 
# # Sample inputs
# date1 = input().strip()
# date2 = input().strip()

# # Calculate and print the difference
# result = calculate_date_difference(date1, date2)
# print(result)

# from datetime import datetime

# # Define the date format
# date_format = "%b %d %Y %I:%M%p"

# # Read the input strings and strip any surrounding whitespace
# date1_str = input().strip()
# date2_str = input().strip()

# # Parse the input dates
# date1 = datetime.strptime(date1_str, date_format)
# date2 = datetime.strptime(date2_str, date_format)

# # Calculate the difference
# diff = date2 - date1

# # Extract days, seconds, hours, minutes, and seconds
# days = diff.days
# seconds = diff.seconds
# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# seconds = seconds % 60

# # Format the output without leading zeros for hours, but with two digits for minutes and seconds
# result = f"{days} days, {hours}:{minutes:02}:{seconds:02}"

# # Print the result
# print(result)

# #8

# # Read number of sheets from input
# n = int(input("Enter total Number of sheets: "))

# # Initialize a list to store each sheet
# sheets = []

# # Read each sheet
# for _ in range(n):
#     sheet = tuple(map(int, input().split()))
#     sheets.append(sheet)

# # Display initial attendance sheets
# print(f"Attendance Sheets with Register Number: {tuple(sheets)}")

# # Use a set to store unique register numbers
# unique_register_numbers = set()

# # Flatten sheets and add to the set of unique register numbers
# for sheet in sheets:
#     unique_register_numbers.update(sheet)

# # Convert set to a sorted tuple
# final_sheet = tuple(sorted(unique_register_numbers))

# # Display final unique register numbers
# print(f"Final sheet: {final_sheet}")

# #9
# # Read number of students
# n = int(input().strip())

# # Dictionary to store student records
# student_records = {}

# # Read each student's data
# for _ in range(n):
#     line = input().strip().split()
#     name = line[0]
#     marks = list(map(int, line[1:]))
#     student_records[name] = marks

# # Read the student name to find second-highest mark
# student_name = input().strip()

# # Check if student exists in records
# if student_name in student_records:
#     marks = student_records[student_name]
    
#     # Find the second-highest mark
#     unique_marks = set(marks)  # Use set to remove duplicates
#     if len(unique_marks) < 2:
#         # All marks are the same
#         print(f"{student_name} scored same marks in all subjects: {marks[0]}")
#     else:
#         unique_marks.remove(max(unique_marks))  # Remove the highest mark
#         second_highest = max(unique_marks)     # Find the maximum among remaining marks
#         print(f"Second Highest mark of {student_name}: {second_highest}")
# else:
#     print("Student doesn't exist")
   

# # 10
# # Read the sentence from the user
# sentence = input("Enter a sentence: ")

# # Split the sentence into words
# words = sentence.split()

# # Initialize an empty dictionary to store word counts
# word_count = {}

# # Count occurrences of each word
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# # Print the word counts
# print(word_count)

#iAssess
#1
num1 = int(input().split(','))
num2 = int(input().split(','))

set_1 = map(set(num1))
set_2 = map(set(num2))
print(set_1.issubset(set_2))
print(set_2.issubset(set_1))
# 1,2,3,4,5,6

#2
# Read the number of clients
num_clients = int(input("Enter the number of clients"))

# Initialize an empty dictionary to store client details
client_dict = {}

# Read client details
for i in range(1, num_clients + 1):
    print(f"Enter the details of the client {i}")
    name = input().strip()
    email = input().strip()
    passport_number = input().strip()
    client_dict[passport_number] = (name, email, passport_number)

# Read the passport number to search
search_passport = input("Enter the passport number of the client to be searched").strip()

# Search for client details and print output accordingly
if search_passport in client_dict:
    name, email, passport_number = client_dict[search_passport]
    print("Client Details")
    print(f"{name}--{email}--{passport_number}")
else:
    print("Client not found")

