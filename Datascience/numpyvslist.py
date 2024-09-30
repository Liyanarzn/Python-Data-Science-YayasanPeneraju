# quantities = [10, 20, 30, 40, 50]
# newquantities = [5, 15, 25, 35, 45]
# totalquantities = zip(quantities, newquantities)
# #zip is iterator, inside that is not ovverride 
# print(totalquantities) #print object class
# print(list(totalquantities))

# totalquantities = [x + y for x, y in zip(quantities, newquantities)]
# print()





import time
import numpy as np

size = 10000000
lista = range(0, size)
listb = range(0, size)
numpya = np.arange(0, size)
numpyb = np.arange(0, size)

starttime = time.time()
c = [x + y for x, y in zip (lista, listb)]
print(time.time()- starttime)

starttime = time.time()
d = numpya + numpyb 
print(time.time() - starttime)

print(c[0:10])
print(d[0:10])