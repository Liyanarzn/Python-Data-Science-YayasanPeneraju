# mode:
# x create a file if it does not exist
# t is going to be a text file
# b is going to be a binary file

# open('fruits.txt', 'xt')

# to check if a file is already exists
# ways to import module:

# import os
# os.path.exists('filename')

# from os import path
# path.exists('filename')

from os.path import exists

def keyboardInput(datatype, caption, errorMessage, defaultValue = None):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            if defaultValue == None:
                value = datatype(input(caption))
            else:
                value = input(caption)
                if (value.strip()==""):
                    value = defaultValue
                else:
                    value = datatype(value)
        except:
            print(errorMessage)
        else: 
            isInvalid = False
    return value


def doMenu(filename):
    choice = -1
    while (choice != 0):
        print("-------------")
        print("| 0 - Exit   |")
        print("| 1 - List   |")
        print("| 2 - Add    |")
        print("| 3 - Edit   |")
        print("| 4 - Delete |")
        print("-------------")
        choice = keyboardInput(int, "Choice: ", "Choice must be Integer")
        if (choice == 0):
            print("Thank you for using our system")
            break
        elif (choice == 1):
            printProduct(filename)
        elif (choice == 2):
            addProduct(filename)
        elif (choice == 3):
            editProduct(filename)
        elif (choice == 4):
            deleteProduct(filename)
        

# if exists(filename):
#     pass
# else:
#     open(filename, 'xt')
def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, 'xt')
        except Exception as e:
            print("Something went wrong when we create the file:", e)
        else:
            createTitle(filename)
        finally:
            # filehandler is an object/instance of File class
            filehandler.close()


def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            filehandler.write("Product|Quantity|Price")
    except Exception as e:
        print("Something went wrong when we create the file:", e)


def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be String")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be Integer")
        price = keyboardInput(float, "Price: ", "Price must be Float")
        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we create the file:", e)

def printProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|") # strip() will remove spaces
            if index == 0:
                print(f"{"No. ":5}{product:40}{quantity:20}{price:20}")
                print("=" * 80)
            else:
                print(f"{index:<5}{product:40}{int(quantity):20}{float(price):20.2f}")
    except Exception as e:
        print("Something went wrong when we print the product:", e)

def editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in the index of the product: ", "Index must be integer")
        if index >= len(lines):
            print("Sorry product not available")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure you want to edit this product (y/n)?", "Whut")
            if confirm == 'y' :
                newproduct = keyboardInput(str, f"Product[{product}]: ", "Product must be String")
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be Integer")
                newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be Float")
                data[index] = [newproduct, newquantity, newprice]
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()  # to eliminate the last blank line
                print(newlines)
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we print the product:", e)
 

def deleteProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        index = keyboardInput(int, "Please key in the index of the product: ", "Index must be integer")
        if index >= len(lines):
            print("Sorry product not available")
        else:
            product, quantity, price = data[index]
            print(f"Product: {product}\nQuantity: {quantity}\nPrice: {price}")
            confirm = keyboardInput(str, "Are you sure you want to delete this product (y/n)?", "Whut")
            if confirm == 'y' :
                # newproduct = keyboardInput(str, f"Product[{product}]: ", "Product must be String")
                # newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", "Quantity must be Integer")
                # newprice = keyboardInput(float, f"Price[{price}]: ", "Price must be Float")
                del data[index] 
                newlines = []
                for product in data:
                    line = "|".join(map(str, product)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()  # to eliminate the last blank line
                print(newlines)
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)
    except Exception as e:
        print("Something went wrong when we print the product:", e)

filename = 'fruits.txt'
createFile(filename)
doMenu(filename)
# addProduct(filename)
# printProduct(filename) 