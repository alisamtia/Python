# Decorator - enhance the functionality of other functions
# Decoraor are use to update a function 
# @ use of decorator

def decorator_function_name(any_func):
    def wrapper_function():
        print("This is awesome function")
        any_func()
    return wrapper_function

@decorator_function_name # Short cut to apply the decorator
def func_1():
    print("This is Function no.1")

def func_2():
    print("This is Function no.2")

# func_2=decorator_function_name(func_2)
func_1()
