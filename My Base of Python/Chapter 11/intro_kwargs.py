# kwargs (Keyword Argument)
# **kwargs (Double Start Opertator)

# kwarg parameter
def func(ali,**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")
# d= {'name':'Muhammad Ali','age':12}
# func(**d) #Dict Unpacking
func('ali',first_name = 'Muhammad', last_name='Ali')
