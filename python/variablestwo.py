# so far we learn how to assign a single value to a 
# single variable and we also learn how to assign
# multiple values to multiple variables

fruit = "apple"
fruit01, fruit02 = "apple", "orange"

fruit = ["apple", "rambutan", "durian", "orange", "mango","papaya", "banana", "grapes"]
 
#indexing and selection
print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])# grapses

# how many items we have in the list
# you can get it using the function len
print("Maximum Index: " , len(fruit) - 1 )

print("Number of item: " ,len(fruit))

print(fruit[-1])
print(fruit[-2])
print(fruit[-3])
print(fruit[-4])
print(fruit[-5])

# Maximum index in negatice is same as num of items

#in python we have something called Range
# start_index:end_index
# this process is also called slisomn
print(fruit[1:3])
print(fruit[1:4])
print(fruit[:4])
print(fruit[0:1])
print(fruit[:])

fruit = ["apple", "rambutan", "durian", "orange", "mango","papaya", "banana", "grapes"]
 
# The range can also have 3rd argument, which is step up argument
print(fruit[0:8])
print(fruit[0:8:21])
print(fruit[0:8:2])
print(fruit[0:8:3])

# start index must be less than end index
print(fruit[-5:-1]) # grapes did not come out because -1 is not included
print(fruit[-1:-5])
print(fruit[-1:-5:-1]) # it reverse the list already
# to reverse the entire list
print(fruit [::-1]) 
