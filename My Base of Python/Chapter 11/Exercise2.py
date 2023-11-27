def func(l,**kwargs):
    list1=l
    if kwargs.get('reverse')==True:
        return [i[::-1].title() for i in l]
    else:
        return [i.title() for i in l]

ali=["muhamamd","ali",'alian','ali']
print(func(ali, reverse=True))