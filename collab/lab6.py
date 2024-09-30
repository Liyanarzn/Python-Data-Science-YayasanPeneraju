# Write a simple python function that returns twin primes less than 1000. If two consecutive odd numbers are both prime
# then they are known as twin primes.
# Pairs of primes that differ by 2. For example, 3 and 5, 5 and 7, 11 and 13, and 17 and 19 are twin primes.


#question 2
def prime():
    primes = []
    for num in range(2, 1000):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

def twin_primes():
    primes = prime()
    twin_primes = [(primes[i], primes[i+1]) for i in range(len(primes)-1) if primes[i+1] - primes[i] == 2]
    return twin_primes

print(twin_primes())

def twinprimes():
    twinprime = []
    for i in range (3,1000):
        twin = True
        for j in range (2,i):
            if (i % j) == 0 or ((i+2) % j) == 0:
                twin = False 
        if twin == True:
            twinprime.append([i, i+2])
    return twinprime

for number in twinprimes():
    print(number)

# question 3
# Write a simple python function that takes a number as parameter and returns the prime factors of that number.
# Prime Factorization is finding which prime numbers multiply together to make the original number.
# Example: prime factors of 56 - 2, 2, 2, 7

def primeFactorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    return factors

num = int(input("Enter a number: "))
print(primeFactorization(num))

# question 4
#Write a function that inputs a number and returns the product of digits of that number.

def product_of_each_digit(num):
    product = 1 # initialize
    while num > 0:
        product = product * (num % 10) # to extract last each of the digit (567) to 7,6, 5
        num = num //10 # to continue get each digit 56, 5,0 
        return product #return product because we want to continue get the product of each extract number

num = int(input("Please enter num:"))
product_of_each_digit(num)

# question 5

import math # to use mathsqrt

def sum_of_divisor(num):

    result = 0 # initialize the result
    divisor = 2 #find all divisor which divides "num"  

    while divisor <= (math.sqrt(num)): # iterate divisor till sqrt num (checking divisibility by all integer)
        if (num % divisor == 0): # if have remainder, it not  
            if divisor == (num // divisor): 
                result = result + divisor 
            else:
                result = result + (divisor + (num // divisor))
        divisor = divisor + 1 

    return (result + 1)
        
num = int(input("Please enter number:"))
sum_of_divisor(num)


# question 6
# number is called perfect if the sum of proper divisors of that number is equal to the number.
# For example 28 is perfect number, since 1+2+4+7+14=28. 
# Write a program to print all the perfect numbers in a given range

import math # to use mathsqrt

def sum_of_divisor(num):

    result = 0 # initialize the result
    divisor = 2 #find all divisor which divides "num"

    while divisor <= (math.sqrt(num)): # iterate divisor till sqrt num (checking divisibility by all integer)
        if (num % divisor == 0): # if have remainder, it not
            if divisor == (num // divisor):
                result = result + divisor
            else:
                result = result + (divisor + (num // divisor))
        divisor = divisor + 1

    return (result + 1)

def perfect_number(result):
   
   perfnumber = 0
   n =1
   

    for i in range (1,num):

        if result == num :
            (f"{num}, is perfect number")
        else:
            (f"{num}, is not perfect number")

num = int(input("Please enter number:"))
sum_of_divisor(num)