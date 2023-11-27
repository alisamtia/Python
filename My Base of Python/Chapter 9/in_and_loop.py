# in keyword in set and for loop

s= {'a','b','c'}

# in keyword tocheck if item is present or not
if 'a' in s:
    print('Present')
else:
    print('Not Present')

# for loop
for item in s:
    print(item)

l=[1,2,3,3]
print(list(set(l)))

# Math sets

s1 = {1,2,3,4}
s2 = {3,4,5,6}

# Union
print(s1|s2)

#Intersection
print(s1&s2)

