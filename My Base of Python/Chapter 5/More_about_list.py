# generate list with range function
# something more about pop method
# index method
# pass list to a function

from re import A


number=list(range(1,21))
# print(number)


popped_item=number.pop()
# print(popped_item)

# print(number.index(1,14,28))

def list_func(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(list_func(number))
    