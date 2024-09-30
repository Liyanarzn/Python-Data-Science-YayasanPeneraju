# 25/6
# list
fruits = ["apple", "orange", "mango", "banana"]
for fruit in fruits:
    print(fruit)

# should not do this (shallow copy)
# overseafruits = fruits

# deep copy
overseafruits = fruits.copy()

# or iterate through the list and create new list (for loop)
overseafruits = []
for fruit in fruits:
    overseafruits.append(fruit)
print("Copy using for loop:", overseafruits)
# no of items in the newly created list is same as original list

# list comprehension
overseafruits = [fruit for fruit in fruits]
print("Copy using list comprehension:", overseafruits)

prices = [10, 20, 30, 40, 50]

# for loop
priceswithsst = []
for price in prices:
    priceswithsst.append(price + (price * 0.06))
print("Prices with sst using for loop:", priceswithsst)

# list comprehension
priceswithsst = [price + (price * 0.06) for price in prices]
print("Prices with sst using list comprehension:", priceswithsst)

# using class map → returns map object (iterator)
# step one: convert expression into function
def calculatesst(price):
    return price + (price * 0.06)
# step two: use map class
priceswithsst = map(calculatesst, prices) 
# takes 2 parameters: function, list
# function is executed through map, thats why tak ada ()
# print results -- need to typecast because map is object (not iterable)
print("Prices with sst using map:", list(priceswithsst))

fahrenheitvalues = [32, 33, 34, 35, 36, 37, 38, 39, 40]

# for loop
celciusvalues = []
for fahrenheitvalue in fahrenheitvalues:
    celciusvalues.append((fahrenheitvalue - 32) * 5/9)
print("Celcius values using for loop", celciusvalues)

# list comprehension
celciusvalues = [(fahrenheitvalue - 32) * 5/9 for fahrenheitvalue in fahrenheitvalues]
print("Celcius values using list comprehension", celciusvalues)

# using map
def convertFtoC(fahrenheitvalue):
    return (fahrenheitvalue - 32) * 5/9
celciusvalues = map(convertFtoC, fahrenheitvalues)
print("Celcius values using map", list(celciusvalues))

celciusvalues = map ( lambda value: (value - 32)*5/9, fahrenheitvalues)
print("Celcius values using map", list(celciusvalues))

# iterate through a list of values and create a new list
# no of items in newly created list is less than or same as original list

# for loop
multiplesofthree = []
for number in range(0, 16):
    if (number % 3 == 0): multiplesofthree.append(number)
print("Multiples of Three using for loop:", multiplesofthree)

# list comprehension
multiplesofthree = [number for number in range(0, 16) if (number % 3 == 0)]
print("Multiples of Three using list comprehension:", multiplesofthree)

# using filter
def isMultipleofThree(number):
    return True if number % 3 == 0 else False
multiplesofthree = filter(isMultipleofThree, range(0, 16))
# need to typecast because filter is object (not iterable)
print("Multiples of Three using filter:", list(multiplesofthree))

numbers = [9, 4, 2, 3, 7, 6, 5, 11, 21, 18, 17, 27]

# for loop
evennumbers =[]
for number in numbers:
    if (number % 2 == 0): evennumbers.append(number)
print("Even numbers using for loop:", evennumbers)

# list comprehension
evennumbers = [number for number in numbers if (number % 2 == 0)]
print("Even numbers using list comprehension:", evennumbers)

# using filter
def isEven(num):
    return True if (num % 2 == 0) else False
evennumbers = filter(isEven, numbers)
print("Even numbers using filter:", list(evennumbers))

# iterate through a list of values and reduce it to a single values

numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Total using for loop:", total)

# since list is reduced to a single value, list comprehension cannot be used
# can use another function (not builtin) called reduce (inside module called functools)
# functools is a builtin module
from functools import reduce
def calTotal(previous, current):
    return previous + current
print("Sum using reduce:", reduce(calTotal, numbers))

# iterate and create a new list
# instead of using traditional for loop
# can use list comprehension
# list + for loop / loop inside a list
# [expression for loop condition]

numbers = [1, 2, 3]

from functools import reduce

def calTotal(previous, current):
    return previous + current
print("Sum using reduce:", reduce(calTotal, numbers))

def calFactorial(previous, current):
    return previous * current
print("Factorial using reduce:", reduce(calFactorial, numbers))

# add a third parameter so it will be initialized with 5
print("Factorial using reduce:", reduce(calFactorial, numbers, 5))
