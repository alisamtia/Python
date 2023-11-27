from functools import wraps
def print_function_data(func):
    @wraps(func)
    def wrapper_func(*args,**kwargs):
        print(f"You are calling {func.__name__} Function")
        print(func.__doc__)
        return func(*args,*kwargs)
    return wrapper_func





@print_function_data
def add(a,b):
    '''This Function take two number and Return their Sum'''
    return a+b

print(add(5,5))