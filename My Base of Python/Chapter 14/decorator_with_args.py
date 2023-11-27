from functools import wraps

def only_data_type_allow(data_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if all([type(i)==data_type for i in args]):
                return func(*args,**kwargs)
            return "Invalid String"
        return wrapper
    return decorator

@only_data_type_allow(str)
def string_concate(*args):
    string=""
    for i in args:
        string+=i
    return string

print(string_concate("Muhammamd ","Ali ","Samtia"))