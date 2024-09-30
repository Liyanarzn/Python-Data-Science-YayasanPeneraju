name = "David"
batch = 101 
fee = 1245.6578

#traditionally how we do this
inputrsting = ("Hello" + name + ", Welcome to python class")

#special string called f string
inputstring = f"Hello {name}, welcome to python class {batch}"
print(inputstring)

#align David to right
inputstring = f"Hello {name:>40s}, welcome to python class {batch}"
print(inputstring)

inputstring = f"Hello {name:^40s}, welcome to python class {batch}"
print(inputstring)

# You can also provide padding characters
inputstring = f"Hello {name:*>40s}, welcome to python class {batch}"
print(inputstring)

# Trucate to 3 characters
inputstring = f"Hello {name:>.3}, welcome to python class {batch:10d}"
print(inputstring)

# Trucate to 3 characters
inputstring = f"Hello {name:>.3}, welcome to python class {batch:<10d} in KL"
print(inputstring)

# Trucate to 3 characters
inputstring = f"Hello {name:>.3}, welcome to python class {batch:<10d} in KL for RM {fee:10.2f}"
print(inputstring)


# Trucate to 3 characters
inputstring = f"Hello {name:>.3}, welcome to python class {batch:b} in KL for RM {fee:10.2f}"
print(inputstring)

# Trucate to 3 characters
inputstring = f"Hello {name:>.3}, welcome to python class {batch:o} in KL for RM {fee:10.2f}"
print(inputstring)

# Trucate to 3 characters
inputstring = f"Hello {name:>.3}, welcome to python class {batch:x} in KL for RM {fee:10.2f}"
print(inputstring)

inputstring = f"Hello {name:>.3}, welcome to python class {batch:x} in KL for RM {fee:,.2f}"
print(inputstring)