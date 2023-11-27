# *args with normal Parameters

def multiply_nums(ali,*args):
    multiply=1
    print(ali)
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(1,2,3))

