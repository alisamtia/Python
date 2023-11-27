from functools import wraps
def decorator_function_name(any_func):
    @wraps(any_func)
    def wrapper_function(*args,**kwargs):
        print("This is awesome function")
        return any_func(*args,**kwargs)
    return wrapper_function

@decorator_function_name
def add(a,b):
    '''This is Addition Function'''
    return a+b

# print(add(1,4))
print(add.__doc__)
print(add.__name__)