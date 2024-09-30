#1
f = open("averageLength.txt","w")
t = "Hell"
f.write(t)
s = 0

for i in t:
    s+=(len(i))

print(s)

#2
# f - open("sample.txt","r")

# with open("sample.txt") as f:
#     lines = f.readlines()
#     # print(text)
# s = 0
# for line in lines:
#     s+=int(line.strip())

# print("The sum of the integers in the file sample.txt is", s)

with open("sample.txt") as f:
    lines = f.readlines()
    # print(text)
s = 0
for line in lines:
    s+=int(line.strip())

print("The sum of the integers in the file sample.txt is:",s)

2
f = open("frequencyFile.txt","r")

with open("frequencyFile.txt") as f:
    lines = f.readlines()

s = 0
for line in lines:
    s+=int(line.strip())

print("The sum of the integers in the file sample.txt is", s)

def count_character_frequencies(filename):
    from collections import Counter

    try:
        # Read the file content
        with open(filename, 'r') as file:
            content = file.read()

        # Convert content to lower case and filter out non-alphabetic characters
        content = ''.join(filter(str.isalpha, content.lower()))

        # Use Counter to count the frequencies of each letter
        frequencies = Counter(content)

        # Sort the frequencies by letter
        sorted_frequencies = sorted(frequencies.items())

        # Print the frequency table
        for letter, freq in sorted_frequencies:
            print(f"{letter}: {freq}")

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")

# Define the filename
filename = 'frequencyFile.txt'

# Call the function
count_character_frequencies(filename)


def write_salary_data_to_csv():
    import csv

    # Read input
    n = int(input())
    data = []

    for _ in range(n):
        name = input()
        salary = input()
        data.append((name, salary))

    # Write to CSV file
    filename = 'salaryData.csv'
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for name, salary in data:
            writer.writerow([name, salary])

    # Print the content of the CSV file
    with open(filename, 'r') as csvfile:
        print(csvfile.read())

# Call the function
write_salary_data_to_csv()
