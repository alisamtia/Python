def decorator_function_name(any_func):

    def wrapper_function(*args,**kwargs):
        print("This is awesome function")
        return any_func(*args,**kwargs)
    return wrapper_function

@decorator_function_name
def func_1(a,b):
    return a+b

print(func_1(1,4))