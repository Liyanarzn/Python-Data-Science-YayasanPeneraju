strNumbers = input("Give me a string numbers separated by comma:")
print(strNumbers)
listStrNumbers = strNumbers.split(",")


listNumbers = []
for strNumber in listStrNumbers : 
    listNumbers.append(int(strNumber))
print(listNumbers)


uniqueNumbers = []
for count in range (0, len(listNumbers)):
  if listNumbers[count] not in uniqueNumbers:
     uniqueNumbers.append(listNumbers[count])

print(uniqueNumbers)

index = 0
for outputvariables1 in uniqueNumbers:
   innerindex = index + 1
   for outputvariables2 in uniqueNumbers[innerindex:]:
        outputvariables3 = 100 - (outputvariables1 + outputvariables2)
        if (outputvariables3 in uniqueNumbers[innerindex +1:]):
             print(outputvariables1, outputvariables2, outputvariables3)
             break
        innerindex = innerindex + 1
     index = index + 1


