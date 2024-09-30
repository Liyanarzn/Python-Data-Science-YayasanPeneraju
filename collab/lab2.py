# Question no 4
a = 57
b = 80
c = 90

# Compare the numbers using logical operatorsa
a_largest = (a > b and a > c)
b_largest = (b > a and b > c)
c_largest = (c > a and c > b)

if (a_largest == b_largest):
    print("The largest number:", c)
elif (a_largest == c_largest): 
    print("The largest number :", b)
else:
    print("The largest number:", a)

print ("The END")

# Exercise 5 

letter = "z"
vowel = "a, e, i, o, u"

if (letter == vowel):
    print("The letter is vowel")
else:
    print("the letter is consonant")

print("The END")

letter = "e"
vowel = "a", "e", "i", "o", "u"

if (letter == vowel):
    print("The letter is vowel")
else:
    print("the letter is consonant")

print("The END")

#letter = "e"
#vowel == "a" or "e" or "i" or "o" or "u"

#if (letter == vowel):
 # print("This is vowel")
#else:
 # print("This is consonant")
    
w =  float(input("Enter your wieght (Kg):"))
h = float(input("Enter your height (m):"))

BMI = w / h**2 

if (BMI < 18.5):
  print("Underweight")
elif ( BMI >= 18.5 and BMI < 24.9 ):
  print( "Normal weight")
elif (BMI >= 25 and BMI < 29.9):
  print("Overweight")
else:
  print("Obesity")

print("The END")

age = int(input("please enter your age:"))
age_not_working = age < 18 or age > 65

print(f"At {age}, you are usually not working: {age_not_working}")
