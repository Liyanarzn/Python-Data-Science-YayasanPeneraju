# principle = input("Principal : ")
# period = input("Period:")
# rate = input("Rate")
# interest = (principle * period * rate) / 100 
# print("Interest Amount:", interest)


#  runtime Error

try : 
    # we know the following line is taking user input
    # in future this may throw error
    # then you must place this code inside a block called 
    # try execpt
    # another example pput the file open code here
    principle = int(input("Principle: "))

except ValueError:
    # when that error occur what we must do
    # the code inside the except block will get executed
    # only when an error occurs
    # another example throw the errors like file corrupted/ file missing/ permission denied 
    print("Principle amount must be an Integer")

except Exception as e:
    print("Something went wrong:", e)

else: 
    # the code inside the else block gets executed
    # only when there is no error
    # another example read the content from the file
    print("All is Well")
finally:
    # The code inside this finally block will always get executed 
    # regardless of whether an error occur or not
    # another example close the file 
    print("Thank you")


# the program does not get terminated abnormally
# error system must be user friendly 
# your output must please the user (graph80)

