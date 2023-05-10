# a = '1.0'
#
# b = int(a)
#
# print(b, type(b))

# a = (1)
#
# print(a, type(a))  #

# a = [1,2,3] #1
# b = a

#b.append(4) #1

# print(a == b)  # true
# print(id(a) == id(b))  # true
# print(a, b)

# print(a is b)

# d = {
#     'a': 1,
#     'b': None,
#     'c': {
#         'd': None,
#         'e': 2,
#         'f': {}
#     }
# }

# output
# o = {
#     'a': 1,
#     'c': {
#         'e': 2,
#         'f': {}
#     }
# }


# p = []
# p.append(d)
#
# while len(p):
#
#     new_dict = p.pop()
#     for i, j in tuple(new_dict.items()):
#         if j == None:
#             new_dict.pop(i)
#         elif type(j) == dict:
#             p.append(j)
#
#
# print(d)


# def delete_none(dic):
#
#     for i, j in tuple(dic.items()):
#         if j is None:
#             dic.pop(i)
#         elif type(j) == dict:
#             delete_none(j)
#
#
# delete_none(d)
# print(d)


# p = []
# p.append(d)
#
# while p:
#     new_dic = p.pop()
#
#     for k in list(new_dic):
#         if new_dic[k] is None:
#             del new_dic[k]
#         elif isinstance(new_dic[k], dict):
#             p.append(new_dic[k])
#
# print(d)

# def delete_none(dic):
#     for k in list(dic):
#         if dic[k] is None:
#             del dic[k]
#         elif isinstance(dic[k], dict):
#             delete_none(dic[k])
#
#
# delete_none(d)
# print(d)

# will this work ??
# keys = new_dic.keys()
# for key in new_dic:
#     a = key + 1
#     new_dic[a] = new_dic[key]


# remove all keys with None

# l = [1, 2, 3] # iterable
#
# _iter = iter(l)
#
# print(len(_iter))

# while True:
#     try:
#         pass  # empty block
#         print(next(_iter))
#
#     except StopIteration:
#         print("End")
#         break
#
# for i in l:
#     print(i)


# l = [1,2,3,4.....1000]


# a = {
#     1: "akash",
#     2: "amit"
# }
#
# b = {}

# for i in tuple(a):
#     a[i+1] = "akash"

# print(a)
# {
#     1: "akash",
#     2: "akash",
#     3: "akash"
# }

# print(a)

# a = tuple(['1', 'a', ["a", "b"]])
# ab = {
#     a: "1"
# }


