# Multiple inheritance

class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside card class")

class AtmCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside Atmcard class")

class CreditCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside CreditCard class")

class DebitCard(Card):
    def __init__(self):
        pass
    def doSomething(self):
        print("Inside DebitCard class")

class BankCard(AtmCard, CreditCard, DebitCard):
    def __init__(self):
        pass
    def doSomething(self):
        #print("Inside BankCard class")
        super().doSomething()

    

# we have created 5 classes
# and in all 5 classes we have dosomething method
# and it is implemented (got code inside which is "print")
# Let us create instance of the last card

bankCard = BankCard()
bankCard.doSomething()

# you will see "Inside Ban"




