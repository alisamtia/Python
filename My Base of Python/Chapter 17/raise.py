def func(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    raise TypeError("OOPs You are passing worng data type to Function")

print(func(3,'4'))