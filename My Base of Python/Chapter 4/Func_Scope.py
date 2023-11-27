# Scope


x=5 #Global Variable

def func():
    global x
    x=7 # Local Variable
    return x
print(x)
print(func())
print(x)

# Error
# def func_2():
#     print(x)
# func_2()


