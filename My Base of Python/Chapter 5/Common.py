def common(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    return c
a=[1,2,3,4]
b=[1,6,9]
print(common([1,2,3,4,5],[3,7,5]))

