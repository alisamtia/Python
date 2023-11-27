from functools import wraps
def only_int_allow(func):
    @wraps(func)
    def wrappers(*args,**kwargs):
        if all([type(i)==int for i in args]):
            return func(*args,**kwargs)
        return "Invalid Argument"
        # data_types=[]
        # for i in args:
        #     data_types.append(type(i)==int)
        # if all(data_types):
        #     return func(*args,**kwargs)
        # else:
        #     return "Invalid Argument"
    return wrappers





@only_int_allow
def my_sum(*args):
    total=0
    for i in args:
        total+=i
    return total
print(my_sum(1,2,3,4,5,[1,2,3]))