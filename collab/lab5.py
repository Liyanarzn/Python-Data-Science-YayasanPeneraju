no = 1 
num = 2 
count =0

print("No. Perfect Number:",)

while count < 10: 
  primenumber = True 
  for i in range(2, num):
    if (num % i == 0):
      primenumber = False
      break

  if primenumber:
    p = num 
    q = 2**p - 1 
    for j in range(2, q):
      if (q % j == 0):
        primenumber = False 
        break

    if primenumber:
        perfectnumber = q *  2 **(p-1)
        print(no, " ", perfectnumber)
        count = count + 1
        no = no + 1 

  num = num + 1