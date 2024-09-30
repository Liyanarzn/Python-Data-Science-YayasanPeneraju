# List 
# l = [1,2,3,4,5]
# l.insert(2,2.5)
# print(l)

# l.extend([6,7,8,9])
# print(l)

# l.append([6,7,8,9])
# print(l)
# print(len(l))

# l=[1,2,3,4,5]
# for i in l:
#     print(i)

# print (23 not in l)

# l=[1,2,3,4,5,6,7,8,9,10]
# print(l[2:6])
# print(l[::2])
# print(l[::-1])

# # print(l[-1])
# # print(l[-5])
# # print(l[::2])
# # print(l[-1:-7:-1])

# # Dictionary

# d = {"name":"JK","age":25, "rollNo":12345,"weight":80.5,"subjects":["Maths", "Science"], 
#      "address":{"DNo":5213, "SName":"1st Cross","City":"Cbe","PinCode":"6220014"},"name":"J Karthikeyan"}

# # print(d)
# # print(d["name"])
# # print(d["address"])
# # print(d["address"]["City"])
# # # print(d["subjects"][1])
# # del(d)

# # d = {1:"int", 2.4:"float",(12,13):"tuple","name":"str",2+3j:"complex"}
# # print(d)

# # for i in d:
# #     print(i, d[i].split("."))

# d = {12:"qwe", 123:"ert", 3214:"dsf"}
# print(d)
# # for i in d:
# #     print(i, d[i].split("."))



# # # for i in sorted (d):
# #     print(i, d[i],sep=("."))

# print(d[12])
# d[12]=[d[12]]
# print(d)
# d[12].append("abc")
# print(d)

#tuple
# l = [1, 2, 3, 4, 5]
# t = tuple(l)
# print(t)
# print(type(t))

t = (1,2,3,[123,34,56],"hi","hello",[12.3, 23.5, "jk",[1234,3456]],(321,432,(5677,8768)))
print(t[7][2][0])
print(type(t))