# You have to complete understanding of functions
# first class function anf closures
# then finallly we will lern about decorators

def square(a):
    return a**2

s=square
# both squares are same
# print(s(7))
# print(square(7))

# Both Name are same
# print(square.__name__)
# print(s.__name__)

# Both memory is also same
print(s)
print(square)