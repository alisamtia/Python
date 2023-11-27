# Set data Type
# unordered collection of unique items

s = {1,2,3,2}
# cannot store dict or list
s={1,1.1,2.3,'string',}
# print(s)
l = [1,2,3,4,5,5,5,5,5,5,6,7,7,8]
# remove duplicate
s2=set(l)
# print(s2)
# print(list(set(l)))
# s.add(4)
# s.add(5)
# s.add(4)
# s.remove(2)
# s.discard(7)
s.clear()
# print(s)

s1=s.copy()
# print(s1)