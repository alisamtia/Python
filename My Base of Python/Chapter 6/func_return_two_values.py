# function returning two values
from audioop import mul


def func(int1,int2):
    add=int1+int2
    multiply=int1*int2
    # return add,multiply # Return Tuple
    return add, multiply

# print(func(2,3))
add,multiply=func(2,3)
print(add)
print(multiply)