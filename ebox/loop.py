# Input reading
N = int(input())

# Initialize variables
current = 30
step = 5
add = True  # Start with addition

# Generate and print the series
for i in range(N):
    if i < N - 1:
        print(current, end=" ")
    else:
        print(current)
    if add:
        current += step
    else:
        current -= step
    add = not add  # Alternate between addition and subtraction
    step += 3  # Step increments by 3 after each term

# Read the input values
A, B, N = map(int, input().split())

# Calculate the number of turns for Richie and Riya
richie_turns = (N + 1) // 2
riya_turns = N // 2

# Calculate the final values for Richie and Riya
C = A * (2 ** richie_turns)
D = B * (2 ** riya_turns)

# Calculate the final score
final_score = C + D

# Print the final score
print(final_score)

# Read the input value
N = int(input())

# Check if the input is valid
if N < 10:
    print("Invalid Input")
else:
    # Convert the number to a string
    N_str = str(N)
    
    # Get the first and last digits
    first_digit = int(N_str[0])
    last_digit = int(N_str[-1])
    
    # Calculate the absolute difference
    absolute_difference = abs(first_digit - last_digit)
    
    # Print the result
    print(absolute_difference)
