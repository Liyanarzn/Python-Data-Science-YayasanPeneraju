#flask is a module
# inside this module we have a class called Flask
# let us import the class "Flask"
from flask import Flask
# Let us create an instance of object of the class Flask
# "Flask" class has __init__(constructor) method
# The contructor takes the file which is going to be the main program
# as parameter
# In other words, we are saying app.py is the main program
# to Flask class
app = Flask(__name__)
#print(__name__)


#if anybody make a http request for */* then execute 
# the following function 
# which return Hello World !!! we can see that in the browser 
@app.route("/")
def say_hello():
    return "ANA BUKAN BESHE2 DO"